"""
confidence_scorer.py

Scores corporate water-disclosure text on two independent axes:

1. CONFIDENCE score  -- how assertive/hedged the rhetoric is
2. TRANSPARENCY score -- how much concrete, checkable information is actually disclosed

The interesting output is the *gap* between the two: a report can sound
very confident while disclosing very little (high confidence, low transparency),
or read cautiously while actually being specific (low confidence, high transparency).

Usage:
    python confidence_scorer.py ../corpus/microsoft_sustainability_2026.txt
    python confidence_scorer.py ../corpus/*.txt --plot
"""

import argparse
import glob
import re
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

try:
    import spacy
    _NLP = spacy.load("en_core_web_sm")
except Exception:
    _NLP = None  # falls back to a naive sentence splitter if spaCy model isn't installed


# ---------------------------------------------------------------------------
# Lexicons -- extend these as you read more reports. This is the part of the
# methodology most worth iterating on; treat it as a living artifact, not a
# fixed rulebook.
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
    "verified", "audited", "as of", "at our facility in", "at our",
    "site-specific", "facility-level", "third-party verified",
]

QUANT_PATTERN = re.compile(
    r"\b\d[\d,]*(\.\d+)?\s*(liters?|litres?|gallons?|billion|million|trillion|%|percent|MW|GW|MWh|GWh)\b",
    re.IGNORECASE,
)

FACILITY_PATTERN = re.compile(
    r"\b(data center in|facility in|campus in|site in|located in)\s+[A-Z][\w\s]{2,30}",
)


@dataclass
class SentenceScore:
    text: str
    hedge_hits: int = 0
    assertive_hits: int = 0
    has_quant: bool = False
    has_facility_ref: bool = False

    @property
    def confidence_score(self) -> float:
        # Net assertiveness: assertive markers push up, hedges pull down.
        return self.assertive_hits - self.hedge_hits

    @property
    def transparency_score(self) -> int:
        return int(self.has_quant) + int(self.has_facility_ref)


def _sentences(text: str):
    if _NLP is not None:
        doc = _NLP(text)
        return [s.text.strip() for s in doc.sents if s.text.strip()]
    # naive fallback
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def score_text(text: str) -> list[SentenceScore]:
    # Only score sentences that are plausibly about water, to avoid diluting
    # the signal with unrelated sustainability content (carbon, biodiversity, etc.)
    water_terms = re.compile(r"\bwater\b", re.IGNORECASE)
    results = []
    for sent in _sentences(text):
        if not water_terms.search(sent):
            continue
        s = SentenceScore(text=sent)
        low = sent.lower()
        s.hedge_hits = sum(low.count(p) for p in HEDGING_PHRASES)
        s.assertive_hits = sum(low.count(p) for p in ASSERTIVE_MARKERS)
        s.has_quant = bool(QUANT_PATTERN.search(sent))
        s.has_facility_ref = bool(FACILITY_PATTERN.search(sent))
        results.append(s)
    return results


def summarize(company: str, scores: list[SentenceScore]) -> dict:
    if not scores:
        return {
            "company": company,
            "water_sentences": 0,
            "avg_confidence": None,
            "avg_transparency": None,
            "gap": None,
        }
    avg_conf = sum(s.confidence_score for s in scores) / len(scores)
    avg_trans = sum(s.transparency_score for s in scores) / len(scores)
    return {
        "company": company,
        "water_sentences": len(scores),
        "avg_confidence": round(avg_conf, 3),
        "avg_transparency": round(avg_trans, 3),
        # gap > 0 means the report sounds more confident than it is transparent
        "gap": round(avg_conf - avg_trans, 3),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="Text files to score (supports globs)")
    parser.add_argument("--plot", action="store_true", help="Show a confidence-vs-transparency scatter plot")
    parser.add_argument("--csv", default=None, help="Optional path to write summary CSV")
    args = parser.parse_args()

    all_files = []
    for pattern in args.files:
        all_files.extend(glob.glob(pattern))

    rows = []
    for fp in all_files:
        path = Path(fp)
        company = path.stem.split("_")[0]
        text = path.read_text(encoding="utf-8", errors="ignore")
        scores = score_text(text)
        rows.append(summarize(company, scores))

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
        ax.set_xlabel("Transparency (concrete disclosure density)")
        ax.set_ylabel("Confidence (rhetorical assertiveness)")
        ax.set_title("Confidence vs. Transparency in Water Disclosures")
        ax.axline((0, 0), slope=1, linestyle="--", color="gray", alpha=0.5)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
