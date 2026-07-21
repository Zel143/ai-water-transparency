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

## Known limitations (be upfront about these in your writeup)

1. **Lexicon is hand-built and incomplete.** It will miss creative hedging and reward companies for happening to use certain stock phrases. Expect to iterate on `HEDGING_PHRASES` and `ASSERTIVE_MARKERS` after reading 2–3 real reports.
2. **Sentence-level scoring loses context.** A hedge in one sentence followed by a hard number in the next should probably be read together — consider a sliding-window or paragraph-level pass as a v2.
3. **This measures rhetoric, not ground truth.** A company could score "transparent" by this metric while still omitting facility-level data entirely (e.g., disclosing global totals with lots of specific-sounding numbers). Cross-check your findings against independent audits (e.g., the VU Amsterdam Digiconomist rankings) rather than trusting the script's score in isolation.
4. **Small corpus, no statistical significance testing.** With ~5 companies you're doing qualitative comparison, not a statistically powered study — say so plainly in your conclusions.
