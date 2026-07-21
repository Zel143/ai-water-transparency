# Confidence vs. Candor: Auditing Corporate Water Disclosure Rhetoric in AI Data Centers

## Research Question

**Do companies phrase their water disclosures with more confidence than the underlying data warrants — and does that rhetorical confidence correlate (or anti-correlate) with actual transparency?**

This project treats corporate sustainability/ESG reports as a text corpus and asks whether the *linguistic framing* of water-use claims (hedged vs. assertive, vague vs. quantified) tracks the *actual information density* disclosed (facility-level numbers vs. aggregate/global figures). It's the same instinct behind an "Overtrust Index" for AI outputs — applied here to corporate water reporting instead.

## Why This Matters

- North American data centers consumed an estimated ~1 trillion liters of water in 2025, and hyperscale water demand is projected to reach 1.4 trillion liters/year globally by 2030.
- Independent transparency audits already show a real spread: Meta ranks most transparent, Google/Microsoft roughly tied, Amazon least transparent — but transparency rank doesn't track efficiency rank, meaning "says more" ≠ "does better."
- Investors (a dozen+ shareholders ahead of 2026 AGMs) are explicitly pressuring Amazon, Microsoft, and Google for site-level (not aggregate) water disclosure.
- Legislative responses are emerging but stalled/early: the federal Data Center Transparency Act (introduced Jan 2026) and Illinois' proposed "POWER Act."

## Case Study: Pax Silica / New Clark City, Philippines

A live, ongoing example rather than a hypothetical — see `case_study/new_clark_city.md`. The Philippines joined the US-led Pax Silica alliance in 2026, earmarking 4,000 acres in New Clark City, Tarlac for an AI/data center hub. A single 1GW facility there would require ~15 billion liters of water/year — roughly 2x the city's current total water demand — in a province where a third of rice fields already lack direct irrigation.

## Repo Structure

```
ai-water-transparency/
├── README.md                      <- you are here
├── corpus/                        <- raw + cleaned disclosure text (ESG reports, press releases)
│   └── README.md                  <- sourcing guide + citation log
├── analysis/
│   ├── confidence_scorer.py       <- hedging/assertiveness + quantification scoring
│   ├── requirements.txt
│   └── README.md                  <- methodology notes
├── case_study/
│   └── new_clark_city.md          <- Pax Silica water-deficit case study
├── solutions/
│   └── policy_solutions.md        <- disclosure & engineering solutions, mapped to feasibility
└── data/
    └── sources.md                 <- citation log for every figure used in this repo
```

## Methodology (short version)

1. **Corpus**: Pull the latest sustainability/ESG reports from Google, Microsoft, Amazon, Meta, plus BCDA/Pax Silica public statements.
2. **Confidence scoring**: Score each water-related passage for hedging language (e.g. "aim to," "working toward," "committed to") vs. assertive/quantified language (specific liters, specific facility, specific date).
3. **Transparency scoring**: Independently score the same passage for information density — is there a real number? Is it facility-level or aggregate/global? Is there a source/methodology footnote?
4. **Correlate**: Plot confidence score against transparency score per company/report. The interesting finding isn't "some companies are vaguer" — it's *whether high rhetorical confidence substitutes for low actual disclosure*.

## Status

This is a scaffold. Next steps: populate `corpus/` with real report text, run `analysis/confidence_scorer.py`, and fill in `data/sources.md` with every citation as you go — treat that file as non-negotiable, since the whole project's credibility rests on accurate sourcing.
