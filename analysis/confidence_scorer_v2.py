"""
confidence_scorer_v2.py

Second iteration of the water-disclosure scorer. Same two axes as v1
(confidence vs. transparency), with four fixes motivated by the Amazon
spot-check (2026-07-21):

1. Site-level detection that actually fires: spaCy NER place entities
   (GPE/LOC/FAC) instead of the v1 "facility in X" regex that never matched
   real report phrasing. Continent/region names don't count -- a number tied
   to "North America" is still an aggregate.
2. Boilerplate filter: repeated page furniture (nav headers, TOC strings)
   is detected per document as high-frequency 8-token shingles and stripped
   before scoring; verbless "sentences" and duplicates are dropped.
3. Transparency split: `has_quant` (any real number) and `site_level`
   (a number tied to a specific place) are reported separately. The spread
   between them per company is the metric v1 couldn't see -- and the one
   independent audits actually measure.
4. Lexicon matching uses word boundaries (v1's substring counting let
   "may" match inside "maybe"), and "as of" is demoted from assertive to
   neutral -- it fires on inventory-style sentences with little content.

Usage:
    python confidence_scorer_v2.py ../corpus/*.txt --csv results_v2.csv
    python confidence_scorer_v2.py ../corpus/*.txt --plot
    python confidence_scorer_v2.py ../corpus/amazon_sustainability_2025.txt --dump 10
"""

import argparse
import glob
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

try:
    import spacy
    _NLP = spacy.load("en_core_web_sm")
except Exception:
    _NLP = None  # regex fallbacks below; site-level detection degrades most


# ---------------------------------------------------------------------------
# Lexicons -- word-boundary matched (fix #4). Still hand-built; iterate as
# more reports are read.
# ---------------------------------------------------------------------------

HEDGING_PHRASES = [
    "aim to", "aims to", "working toward", "working towards", "committed to",
    "strive to", "striving to", "on track to", "in the process of",
    "continue to explore", "exploring ways to", "long-term goal",
    "where feasible", "where possible", "where appropriate",
    "we believe", "we expect", "expected to", "intend to", "intends to",
    "plan to", "plans to", "may", "could", "potentially", "in some cases",
]

ASSERTIVE_MARKERS = [
    "achieved", "reduced by", "increased by", "reported", "measured",
    "verified", "audited", "site-specific", "facility-level",
    "third-party verified",
    # "as of" removed (fix #4): confident-sounding but content-free
]

QUANT_PATTERN = re.compile(
    r"\b\d[\d,]*(\.\d+)?\s*(liters?|litres?|gallons?|m3|cubic meters?|"
    r"billion|million|trillion|%|percent|MW|GW|MWh|GWh|kWh)\b",
    re.IGNORECASE,
)

# Places too coarse to count as "site-level" -- a number tied to one of these
# is still an aggregate figure.
REGION_STOPLIST = {
    "europe", "north america", "south america", "asia", "africa", "oceania",
    "asia pacific", "apac", "emea", "latin america", "the americas",
    "the united states", "united states", "u.s.", "us", "usa", "the us",
    "global", "worldwide", "earth", "the world",
}

# Regex fallback for place refs when spaCy is unavailable: "in Mississippi,
# U.S." / "in Hong Kong, China" / "in India". Deliberately conservative.
PLACE_FALLBACK = re.compile(
    r"\bin ([A-Z][a-z]+(?: [A-Z][a-z]+)?)(?:, ([A-Z][\w. ]{1,20}))?\b"
)

_WORD = re.compile(r"\S+")


def _compile_lexicon(phrases):
    return [re.compile(r"\b" + re.escape(p) + r"\b", re.IGNORECASE) for p in phrases]


_HEDGE_RES = _compile_lexicon(HEDGING_PHRASES)
_ASSERT_RES = _compile_lexicon(ASSERTIVE_MARKERS)


@dataclass
class SentenceScore:
    text: str
    hedge_hits: int = 0
    assertive_hits: int = 0
    has_quant: bool = False
    site_level: bool = False

    @property
    def confidence_score(self) -> float:
        return self.assertive_hits - self.hedge_hits

    @property
    def transparency_score(self) -> int:
        # 0 = no number; 1 = a number, but aggregate; 2 = a number tied to a place
        return int(self.has_quant) + int(self.site_level)


# ---------------------------------------------------------------------------
# Fix #2: boilerplate handling
# ---------------------------------------------------------------------------

def _furniture_shingles(text: str, n: int = 8, min_count: int = 5) -> set:
    """Token 8-grams that repeat >= min_count times across the document are
    page furniture (nav headers, section-title strips), not prose."""
    tokens = _WORD.findall(text)
    counts = Counter(tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1))
    return {s for s, c in counts.items() if c >= min_count}


def _strip_furniture(sentence: str, shingles: set, n: int = 8) -> str:
    if not shingles:
        return sentence
    tokens = _WORD.findall(sentence)
    keep, i = [], 0
    while i < len(tokens):
        if tuple(tokens[i:i + n]) in shingles:
            # skip the whole repeated run, extending past the first window
            i += n
            while i < len(tokens) and tuple(tokens[i - n + 1:i + 1]) in shingles:
                i += 1
        else:
            keep.append(tokens[i])
            i += 1
    return " ".join(keep)


def _has_verb(sent_doc) -> bool:
    return any(t.pos_ in ("VERB", "AUX") for t in sent_doc)


# ---------------------------------------------------------------------------
# Fix #1: site-level detection
# ---------------------------------------------------------------------------

def _place_refs(sent_doc, sentence: str) -> list:
    if sent_doc is not None:
        places = [e.text for e in sent_doc.ents if e.label_ in ("GPE", "LOC", "FAC")]
    else:
        places = []
        for m in PLACE_FALLBACK.finditer(sentence):
            places.append(m.group(1))
            if m.group(2):
                places.append(m.group(2))
    return [p for p in places if p.strip().lower() not in REGION_STOPLIST]


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_text(text: str) -> tuple:
    """Returns (scores, n_dropped): per-sentence scores for water sentences,
    and how many water sentences the boilerplate/dedupe filters removed."""
    shingles = _furniture_shingles(text)
    water_re = re.compile(r"\bwater\b", re.IGNORECASE)

    if _NLP is not None:
        # NER + POS needed per sentence; chunk to stay under spaCy's max length
        docs = [_NLP(text[i:i + 500_000]) for i in range(0, len(text), 500_000)]
        raw_sents = [s for d in docs for s in d.sents]
    else:
        raw_sents = [None]  # placeholder; regex path below

    if _NLP is None:
        sent_iter = [(None, s.strip()) for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    else:
        sent_iter = [(s, s.text.strip()) for s in raw_sents if s.text.strip()]

    scores, seen, dropped = [], set(), 0
    for sent_doc, raw in sent_iter:
        if not water_re.search(raw):
            continue
        cleaned = _strip_furniture(raw, shingles)
        if not water_re.search(cleaned):
            dropped += 1  # the only "water" mention was in page furniture
            continue
        key = re.sub(r"\W+", "", cleaned.lower())
        if key in seen:
            dropped += 1
            continue
        seen.add(key)
        if sent_doc is not None and not _has_verb(sent_doc):
            dropped += 1
            continue

        s = SentenceScore(text=cleaned)
        s.hedge_hits = sum(len(rx.findall(cleaned)) for rx in _HEDGE_RES)
        s.assertive_hits = sum(len(rx.findall(cleaned)) for rx in _ASSERT_RES)
        s.has_quant = bool(QUANT_PATTERN.search(cleaned))
        s.site_level = s.has_quant and bool(_place_refs(sent_doc, cleaned))
        scores.append(s)
    return scores, dropped


def summarize(company: str, scores: list, dropped: int) -> dict:
    if not scores:
        return {"company": company, "water_sentences": 0, "dropped": dropped,
                "avg_confidence": None, "pct_quant": None, "pct_site_level": None,
                "avg_transparency": None, "gap": None}
    n = len(scores)
    avg_conf = sum(s.confidence_score for s in scores) / n
    avg_trans = sum(s.transparency_score for s in scores) / n
    return {
        "company": company,
        "water_sentences": n,
        "dropped": dropped,
        "avg_confidence": round(avg_conf, 3),
        "pct_quant": round(100 * sum(s.has_quant for s in scores) / n, 1),
        # the number v1 couldn't measure: how much of the quantified talk is place-tied
        "pct_site_level": round(100 * sum(s.site_level for s in scores) / n, 1),
        "avg_transparency": round(avg_trans, 3),
        "gap": round(avg_conf - avg_trans, 3),
    }


def main():
    # Windows consoles default to cp1252, which chokes on PDF-extracted glyphs
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="Text files to score (supports globs)")
    parser.add_argument("--plot", action="store_true", help="Scatter plot of transparency vs. confidence")
    parser.add_argument("--csv", default=None, help="Optional path to write summary CSV")
    parser.add_argument("--dump", type=int, default=0, metavar="N",
                        help="Print the N highest-transparency sentences per file (for auditing the metric)")
    args = parser.parse_args()

    all_files = []
    for pattern in args.files:
        all_files.extend(glob.glob(pattern))

    rows = []
    for fp in all_files:
        path = Path(fp)
        company = path.stem.split("_")[0]
        text = path.read_text(encoding="utf-8", errors="ignore")
        scores, dropped = score_text(text)
        rows.append(summarize(company, scores, dropped))
        if args.dump:
            print(f"\n=== {company}: top {args.dump} by transparency ===")
            top = sorted(scores, key=lambda s: (s.transparency_score, s.confidence_score), reverse=True)
            for s in top[:args.dump]:
                flags = f"trans={s.transparency_score} conf={s.confidence_score:+.0f} site={s.site_level}"
                print(f"[{flags}] {' '.join(s.text.split())[:300]}\n")

    df = pd.DataFrame(rows)
    print(df.to_string(index=False))

    if args.csv:
        df.to_csv(args.csv, index=False)
        print(f"\nSaved summary to {args.csv}")

    if args.plot:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.scatter(df["avg_transparency"], df["avg_confidence"])
        for _, row in df.iterrows():
            ax.annotate(row["company"], (row["avg_transparency"], row["avg_confidence"]))
        ax.set_xlabel("Transparency (quant + site-level density)")
        ax.set_ylabel("Confidence (rhetorical assertiveness)")
        ax.set_title("Confidence vs. Transparency in Water Disclosures (v2)")
        ax.axline((0, 0), slope=1, linestyle="--", color="gray", alpha=0.5)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
