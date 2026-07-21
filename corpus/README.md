# Corpus

Drop cleaned plain-text versions of each source here, one file per report, named:
`{company}_{report_type}_{year}.txt` e.g. `microsoft_sustainability_2026.txt`

## Sources to pull (starter list)

| Company | Document | Where to find it |
|---|---|---|
| Microsoft | Latest Environmental Sustainability Report | microsoft.com/sustainability |
| Google | Environmental Report | sustainability.google |
| Amazon | Sustainability Report | sustainability.aboutamazon.com |
| Meta | Sustainability Report (2026 report expected late summer/fall 2026) | sustainability.fb.com |
| BCDA (Pax Silica) | New Clark City / Pax Silica press releases | bcda.gov.ph |

## Rules for adding a source

1. Save the **raw text**, not a summary — the scorer needs actual sentences.
2. Note the exact URL and retrieval date in `data/sources.md` before you paste anything in here.
3. Do not paste large verbatim excerpts into any report/markdown you write *about* the corpus — quote sparingly and cite. The `corpus/` folder itself is your working data, not a publication, so full text is fine here; just don't reproduce big chunks of it in your README or write-up.
4. If a company's report doesn't mention water at all in a given year, log that absence in `data/sources.md` — it's a finding, not a gap to skip.
