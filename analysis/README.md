# Analysis Methodology

## Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Running

```bash
python confidence_scorer.py ../corpus/*.txt --csv results.csv --plot
```

## What the score means

- **Confidence score** (per water-related sentence): assertive markers ("achieved," "reduced by," "third-party verified") minus hedging markers ("aim to," "working toward," "may"). Positive = confident/assertive tone.
- **Transparency score**: whether the sentence contains an actual quantified figure (liters, %, MW) and/or names a specific facility/location. Range 0–2 per sentence.
- **Gap** = avg confidence − avg transparency, per company. This is the headline metric. A large positive gap means a company's water language sounds more certain than the data backs up. A negative or near-zero gap means the confident language is backed by real specifics.

## v2 scorer (`confidence_scorer_v2.py`)

Built after spot-checking v1's top Amazon sentences exposed four problems. v2:

1. **Detects site-level disclosure properly** — spaCy NER place entities (GPE/LOC/FAC) instead of v1's `facility in X` regex, which never fired on real report phrasing ("In Mississippi, U.S., …"). Continent/region names don't count: a number tied to "North America" is still an aggregate.
2. **Filters PDF boilerplate** — repeated page furniture (nav headers, TOC strips) is detected as high-frequency 8-token shingles and stripped; verbless and duplicate sentences are dropped. This removed 37 junk "sentences" from Amazon alone.
3. **Splits transparency into `pct_quant` vs. `pct_site_level`** — any-number density vs. place-tied-number density. The spread between them is the dimension independent audits actually measure, and the one v1 couldn't see.
4. **Word-boundary lexicon matching, and "as of" demoted** from assertive to neutral (it fired on confident-sounding, low-content inventory sentences).

```bash
python confidence_scorer_v2.py ../corpus/*.txt --csv results_v2.csv --plot
python confidence_scorer_v2.py ../corpus/amazon_sustainability_2025.txt --dump 10   # audit what the metric rewards
```

**Key v2 result (July 2026 corpus):** requiring site-level specificity collapses everyone. Amazon leads `pct_quant` (17.8% of water sentences contain a real number) but only ~2–4% of any company's water sentences tie a number to a named place — Microsoft, Google, and Meta round to 0%. The v1 "Amazon most transparent" ranking was measuring number *density*, not disclosure *granularity*; on granularity, all four reports are near-uniformly aggregate, which is consistent with (rather than contradicting) the independent audits that criticize site-level opacity.

## Known limitations (be upfront about these in your writeup)

1. **Lexicon is hand-built and incomplete.** It will miss creative hedging and reward companies for happening to use certain stock phrases. Expect to iterate on `HEDGING_PHRASES` and `ASSERTIVE_MARKERS` after reading 2–3 real reports.
2. **Sentence-level scoring loses context.** A hedge in one sentence followed by a hard number in the next should probably be read together — consider a sliding-window or paragraph-level pass as a v2.
3. **This measures rhetoric, not ground truth.** A company could score "transparent" by this metric while still omitting facility-level data entirely (e.g., disclosing global totals with lots of specific-sounding numbers). Cross-check your findings against independent audits (e.g., the VU Amsterdam Digiconomist rankings) rather than trusting the script's score in isolation.
4. **Small corpus, no statistical significance testing.** With ~5 companies you're doing qualitative comparison, not a statistically powered study — say so plainly in your conclusions.
