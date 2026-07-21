# Confidence vs. Candor: Auditing Corporate Water Disclosure Rhetoric in AI Data Centers

## Research Question

**Do companies phrase their water disclosures with more confidence than the underlying data warrants — and does that rhetorical confidence correlate (or anti-correlate) with actual transparency?**

This project treats corporate sustainability/ESG reports as a text corpus and asks whether the *linguistic framing* of water-use claims (hedged vs. assertive, vague vs. quantified) tracks the *actual information density* disclosed (facility-level numbers vs. aggregate/global figures). It's the same instinct behind an "Overtrust Index" for AI outputs — applied here to corporate water reporting instead.

## Why This Matters

- North American data centers consumed an estimated ~1 trillion liters of water in 2025; UC Riverside researchers project global AI demand could drive 1.1–1.7 trillion *gallons* of annual water withdrawals by 2027.
- Independent transparency audits already show a real spread: Meta ranks most transparent, Google/Microsoft roughly tied, Amazon least transparent — but transparency rank doesn't track efficiency rank, meaning "says more" ≠ "does better."
- Investors (a dozen+ shareholders ahead of 2026 AGMs) are explicitly pressuring Amazon, Microsoft, and Google for site-level (not aggregate) water disclosure.
- Legislative responses are emerging but stalled/early: Sen. Durbin's federal Data Center Water and Energy Transparency Act (introduced March 2026) and Illinois' POWER Act (introduced Feb 2026; failed to reach a vote before the session ended May 31, 2026).

## Case Study: Pax Silica / New Clark City, Philippines

A live, ongoing example rather than a hypothetical — see `case_study/new_clark_city.md`. The Philippines joined the US-led Pax Silica alliance in 2026, earmarking 4,000 acres in New Clark City, Tarlac for an AI/data center hub. A single 1GW facility there would require ~15 billion liters of water/year — roughly 2x the city's current total water demand — in a province where a third of rice fields already lack direct irrigation.

## Repo Structure

```
ai-water-transparency/
├── README.md                      <- you are here
├── corpus/                        <- raw + cleaned disclosure text (ESG reports, press releases)
│   └── README.md                  <- sourcing guide + citation log
├── analysis/
│   ├── confidence_scorer.py       <- v1: hedging/assertiveness + quantification scoring
│   ├── confidence_scorer_v2.py    <- v2: + site-level detection, boilerplate filter
│   ├── table_scorer_v3.py         <- v3: structured site-level table disclosure
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

## Preliminary Findings (July 2026 corpus)

The corpus holds the latest official report from each company (Microsoft 2026, Google 2026, Amazon 2025, Meta 2025 — see `data/sources.md`). Two rounds of scoring produced one finding worth stating carefully and one illustrative case.

### Number density is not transparency

The v1 scorer (`analysis/confidence_scorer.py`) ranked **Amazon most transparent** — the exact opposite of the independent Digiconomist audit, which ranked Amazon least transparent and Meta most. Spot-checking Amazon's top-scoring sentences explained the contradiction: v1's transparency score was effectively measuring *number density* (does a sentence contain a quantity?), while its facility detector never fired on real report phrasing, so it could not see *granularity* (is the number tied to a named place?).

The v2 scorer (`analysis/confidence_scorer_v2.py`) fixes this — NER-based place detection, PDF-boilerplate filtering, and a split between `pct_quant` (any real number) and `pct_site_level` (a number tied to a specific place):

| company | water sentences | pct_quant | pct_site_level |
|---|---|---|---|
| amazon | 90 | 17.8% | 4.4% (~2% after removing infographic artifacts) |
| meta | 61 | 13.1% | 0.0% |
| google | 147 | 8.8% | 0.7% (one sentence) |
| microsoft | 94 | 8.5% | 0.0% |

**Requiring site-level specificity collapses every company to near zero.** Amazon leads raw number density, but ≥95% of every company's quantified water sentences are aggregate (global or regional totals). The verified site-level disclosures across all four reports amount to a handful of sentences — Amazon's Mississippi reclaimed-water deal and India sewage-treatment plants, one Google sentence. Microsoft's and Meta's zeros were hand-audited: their top quantified sentences are all global figures with no place named.

Read together, the script and the audit stop contradicting each other: they measure different things. Amazon *sounds* most quantified; on the granularity dimension auditors actually care about, all four narrative reports are equally opaque. One caveat matured into its own instrument. Site-level data turns out to exist for two companies — but in **tables**, which sentence scoring cannot see: Microsoft's companion Data Fact Sheet carries Table 15 (~29 cities × electricity/withdrawal/%-non-potable/replenishment, some cells withheld), and Google's per-site water table (~38 locations × withdrawal/discharge/consumption) sits in the appendix *of the very report the sentence scorer processed*. The v3 table scorer (`analysis/table_scorer_v3.py`) measures this structured layer directly:

| company | prose "sounds quantified" (v2 pct_quant) | structured site-level water disclosure (v3) |
|---|---|---|
| amazon | **17.8%** (highest) | **0 sites — across all three scored documents** |
| google | 8.8% (lowest with Microsoft) | **37 sites × 4 metrics, 0 withheld** (in main report's appendix) |
| microsoft | 8.5% | 26 sites × 3 metrics, ~11% cells withheld (in annex fact sheet) |
| meta | 13.1% | ~18 sites × 5-yr withdrawal history (in separate Environmental Data Index) |

The rhetoric axis and the structure axis **disagree, almost perfectly inversely**: three of four companies publish real per-site water tables — always in appendices or annex documents, never in the narrative a casual reader sees — while Amazon, the company with the most quantified-sounding prose, is the only one publishing no structured site-level water data anywhere in its scored documents (main report, AWS summary, and methodology paper included). This is the project's research question answered in preliminary form: confident, number-dense rhetoric is not where the real disclosure lives, and measuring only the narrative layer gets the transparency ranking almost exactly backwards. It also independently reproduces the Digiconomist audit's ranking (Meta/Google/Microsoft above Amazon) from document structure alone. Meta — the most hedged and least number-dense reporter here — is the one independent auditors rank most transparent, suggesting **rhetorical number-density and audit-grade transparency are, if anything, anti-correlated** in this corpus. (Caveats apply: four reports, hand-built lexicon — see `analysis/README.md`.)

### Case in point: Amazon's 9.4-billion-liter coincidence

Amazon's 2025 report states that data centers **withdrew 9.4 billion liters** (p. 14) and that replenishment projects **returned 9.4 billion liters** to communities (p. 16) — identical headline figures. Yet the same report claims only **75% progress** toward its water-positive goal, and the endnote formula behind that number (endnote 16, p. 50: *(reused water + replenishment) ÷ (withdrawal − sustainable sources)*) relies on component volumes — credited replenishment, reused water, the "sustainable sources" subtraction — that are **not disclosed anywhere in the report**. The 75% cannot be recomputed from the report's own published numbers; the reconciliation lives in an external methodology document, and the matching 9.4B figures are a two-significant-figure rounding coincidence with (likely) different scopes.

This is the project's thesis in miniature: **quantified is not the same as verifiable.** The most number-dense report of the four publishes a headline goal metric that its own numbers cannot reproduce.

Follow-up with the methodology document itself (March 2026, now in `corpus/`) deepens rather than resolves this: it defines every term in the formula — reused water, VWBA-accounted replenishment, the sustainable-sources subtraction — but publishes **no annual component volumes**, so the 75% stays non-recomputable even with the methodology in hand. It also reveals that the two matching 9.4B figures are categorically different measurements: withdrawal is metered, while replenishment volumes are largely *modeled* (precipitation-based estimates and "conservative assumptions" for projects that can't be measured).

## Status

Corpus populated and scored (v1 + v2); findings above are preliminary. Remaining work: BCDA/Pax Silica statements for the corpus, re-verification of time-sensitive sources in `data/sources.md`, and a re-run when Meta's 2026 report lands. Every citation goes in `data/sources.md` — treat that file as non-negotiable, since the whole project's credibility rests on accurate sourcing.
