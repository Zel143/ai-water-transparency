"""
table_scorer_v3.py

Structured-disclosure scorer: the complement to the sentence-based rhetoric
scorers (v1/v2). Motivated by two findings the sentence scorers were blind to:

- Microsoft's site-level water data lives in Table 15 of its Data Fact Sheet
  (~29 named locations x electricity/withdrawal/%non-potable/replenishment).
- Google's site-level water data lives in its report appendix ("Water use by
  data center location", ~38 locations x withdrawal/discharge/consumption) —
  *inside the very document the sentence scorer processed*, invisible because
  table rows aren't sentences.

This scorer detects table rows that tie a named location to numeric metrics
and reports, per document:

- water_site_rows / other_site_rows  -- site-metric rows in water vs. non-water
  table context (PUE and grid-mix tables are "other")
- unique_water_sites                 -- distinct named locations with water data
- median_metrics_per_site            -- numeric cells per water row
- withheld_cells / withheld_rate     -- cells marked * or long-dash (disclosed
  as withheld/not-applicable), a transparency signal of its own

Detection is heuristic and tuned on PDF-extracted text (pypdf), so treat
counts as floors, not exact: wrapped multi-line rows are merged best-effort,
and rows whose location the NER misses are dropped. Use --dump to audit.

Usage:
    python table_scorer_v3.py ../corpus/*.txt --csv results_v3.csv
    python table_scorer_v3.py ../corpus/google_environmental_2026.txt --dump
"""

import argparse
import glob
import re
import statistics
import sys
from pathlib import Path

import pandas as pd

try:
    import spacy
    _NLP = spacy.load("en_core_web_sm")
except Exception:
    _NLP = None

REGION_STOPLIST = {
    "europe", "north america", "south america", "asia", "africa", "oceania",
    "asia pacific", "apac", "emea", "latin america", "the americas",
    "united states", "united states of america", "global", "worldwide",
    "rest of world", "total", "subtotal", "average", "by region", "by source",
}

# Rows led by these are table furniture or aggregates, not sites.
NONSITE_LEAD = re.compile(
    r"^(total|subtotal|global|average|by region|by source|rest of world|"
    r"north america|latin america|europe|asia|freshwater|water withdraw|"
    r"water discharge|water consum|water replenish|waste|offices|data centers?\b)",
    re.IGNORECASE,
)

# Grid operators / utilities are organizations, not data center sites.
ORG_HINT = re.compile(
    r"\b(energy|grid|power|authority|operator|interconnect|company|utilit)\w*",
    re.IGNORECASE,
)

UNIT_WORDS = re.compile(
    r"\b(million gallons?|megaliters?|metric tons?|gallons?|liters?|litres?|"
    r"pue|mwh|gwh|kwh|ml|m3|unit|%)\b",
    re.IGNORECASE,
)

NUM_TOKEN = re.compile(r"^<?\d[\d,]*(\.\d+)?%?$")
WITHHELD_TOKEN = re.compile(r"^[*—–‒\-�]$")  # �: dash lost in PDF extraction

COUNTRY_WORDS = {
    "australia", "austria", "belgium", "canada", "chile", "china", "denmark",
    "finland", "france", "germany", "india", "indonesia", "ireland", "italy",
    "japan", "malaysia", "mexico", "netherlands", "poland", "singapore",
    "spain", "sweden", "taiwan", "korea",
}

WATER_HEADER = re.compile(r"\bwater\b", re.IGNORECASE)

OTHER_SECTION = re.compile(
    r"\b(PUE|power usage effectiveness|energy efficiency|emissions?|carbon|"
    r"waste|packaging|biodiversity|renewable|electricity mix|carbon-free)\b",
    re.IGNORECASE,
)


def _tokens(line: str):
    return line.split()


def _cells(tokens):
    """Trailing run of numeric/withheld/unit tokens; returns (numeric, withheld)."""
    numeric, withheld = 0, 0
    for t in tokens:
        if NUM_TOKEN.match(t):
            numeric += 1
        elif WITHHELD_TOKEN.match(t):
            withheld += 1
    return numeric, withheld


def _place_chunk(line: str) -> str:
    """Text before the first numeric/withheld cell, minus unit words."""
    out = []
    for t in _tokens(line):
        if NUM_TOKEN.match(t) or WITHHELD_TOKEN.match(t):
            break
        out.append(t)
    chunk = UNIT_WORDS.sub(" ", " ".join(out))
    return re.sub(r"\s+", " ", chunk).strip(" ,.-")


def _is_place(chunk: str) -> bool:
    if not chunk or len(chunk) > 60:
        return False
    if chunk.lower() in REGION_STOPLIST:
        return False
    if NONSITE_LEAD.match(chunk):
        return False
    if ORG_HINT.search(chunk):
        return False
    if not chunk[0].isupper():
        return False
    # structural signals first — robust to NER missing small city names:
    # "City (ST)" / "City, ST" US-state style
    if re.search(r"\([A-Z]{2}\)|,\s*[A-Z]{2}\b", chunk):
        return True
    # "City Country" style (last word a country, at least one word before it)
    words = chunk.split()
    if len(words) >= 2 and words[-1].lower() in COUNTRY_WORDS:
        return True
    if _NLP is not None:
        doc = _NLP(chunk)
        ents = [e for e in doc.ents if e.label_ in ("GPE", "LOC", "FAC")]
        # exclude chunks that are ONLY a coarse region/country
        return any(e.text.lower() not in REGION_STOPLIST for e in ents)
    return False


def _merge_wrapped(lines):
    """Merge a place-only line with following numeric/unit-only lines (wrapped
    table rows, e.g. Google's Douglas County multi-source breakdown)."""
    merged, i = [], 0
    while i < len(lines):
        line = lines[i].strip()
        toks = _tokens(line)
        numeric, withheld = _cells(toks)
        if line and numeric + withheld < 2 and _is_place(_place_chunk(line)):
            j, acc, label_lines = i + 1, [line], 0
            while j < len(lines) and j - i <= 7:
                nxt = lines[j].strip()
                ntoks = _tokens(nxt)
                nnum, nwith = _cells(ntoks)
                only_data = ntoks and all(
                    NUM_TOKEN.match(t) or WITHHELD_TOKEN.match(t) or UNIT_WORDS.match(t)
                    or t.lower().strip(",") in
                    ("potable", "non-potable", "reclaimed", "wastewater", "water", "gallons", "million")
                    for t in ntoks
                )
                if only_data and (nnum + nwith):
                    acc.append(nxt)
                    j += 1
                elif only_data and label_lines < 2:
                    # source-breakdown label rows ("Potable water") between the
                    # site name and its wrapped numbers
                    acc.append(nxt)
                    label_lines += 1
                    j += 1
                else:
                    break
            if len(acc) > 1:
                merged.append(" ".join(acc))
                i = j
                continue
        merged.append(line)
        i += 1
    return merged


def _header_like(line: str) -> bool:
    toks = _tokens(line)
    if not toks:
        return False
    numeric, _ = _cells(toks)
    alpha = sum(1 for t in toks if any(c.isalpha() for c in t))
    return alpha >= 3 and numeric <= 2


def score_file(path: Path) -> dict:
    raw_lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    lines = _merge_wrapped(raw_lines)

    water_context = False
    water_rows, other_rows = [], []
    for line in lines:
        if _header_like(line):
            # sticky table-context switch: a header mentioning water flips on;
            # only a header naming a different section flips off (neutral
            # column-header lines like "Location Unit ..." keep the state)
            if WATER_HEADER.search(line):
                water_context = True
            elif OTHER_SECTION.search(line):
                water_context = False
            continue
        toks = _tokens(line)
        numeric, withheld = _cells(toks)
        if numeric + withheld < 2:
            continue
        chunk = _place_chunk(line)
        if not _is_place(chunk):
            continue
        row = {"site": chunk, "numeric": numeric, "withheld": withheld, "line": line}
        (water_rows if water_context else other_rows).append(row)

    company = path.stem.split("_")[0]
    doc = path.stem
    if not water_rows:
        return {"document": doc, "company": company, "water_site_rows": 0,
                "unique_water_sites": 0, "median_metrics_per_site": None,
                "withheld_cells": 0, "withheld_rate": None,
                "other_site_rows": len(other_rows)}
    withheld_total = sum(r["withheld"] for r in water_rows)
    cells_total = withheld_total + sum(r["numeric"] for r in water_rows)
    return {
        "document": doc,
        "company": company,
        "water_site_rows": len(water_rows),
        "unique_water_sites": len({r["site"] for r in water_rows}),
        "median_metrics_per_site": statistics.median(r["numeric"] for r in water_rows),
        "withheld_cells": withheld_total,
        "withheld_rate": round(withheld_total / cells_total, 3) if cells_total else None,
        "other_site_rows": len(other_rows),
    }, water_rows


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="Corpus text files (supports globs)")
    parser.add_argument("--csv", default=None, help="Optional path to write summary CSV")
    parser.add_argument("--dump", action="store_true",
                        help="Print every detected water site row (audit mode)")
    args = parser.parse_args()

    all_files = []
    for pattern in args.files:
        all_files.extend(glob.glob(pattern))

    rows = []
    for fp in all_files:
        result = score_file(Path(fp))
        if isinstance(result, tuple):
            summary, water_rows = result
        else:
            summary, water_rows = result, []
        rows.append(summary)
        if args.dump and water_rows:
            print(f"\n=== {summary['document']}: detected water site rows ===")
            for r in water_rows:
                print(f"  [{r['numeric']} metrics, {r['withheld']} withheld] {r['line'][:160]}")

    df = pd.DataFrame(rows)
    print(df.to_string(index=False))
    if args.csv:
        df.to_csv(args.csv, index=False)
        print(f"\nSaved summary to {args.csv}")


if __name__ == "__main__":
    main()
