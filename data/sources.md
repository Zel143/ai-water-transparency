# Source Log

Log every source used anywhere in this repo here. Format:

```
- [Company/Topic] "Title" — Publisher, Date — URL — retrieved YYYY-MM-DD — used in: [file(s)]
```

## Seed sources (from initial research, July 2026)

- Pax Silica land deal — w.media, 2026 — https://w.media/philippines-earmarks-4000-acre-land-as-ai-hub-under-us-led-pax-silica/ — used in: case_study/new_clark_city.md
- Pax Silica protest — Manila Times, July 19 2026 — https://www.manilatimes.net/2026/07/19/news/national/scientists-environmentalists-farmers-hit-pax-silica-ai-hub/2386994 — used in: case_study/new_clark_city.md
- Pax Silica overview/concerns — Rappler, 2026 — https://www.rappler.com/technology/features/things-to-know-pax-silica-philippines-goals-concerns/ — used in: case_study/new_clark_city.md
- Pax Silica mineral criticism — SCMP, 2026 — https://www.scmp.com/week-asia/economics/article/3360932/philippines-pax-silica-ai-hub-plan-slammed-mineral-plunder — used in: case_study/new_clark_city.md
- Pax Silica power needs — Inquirer, 2026 — https://business.inquirer.net/596398/pax-silicas-mammoth-power-needs-draw-maharlika-foreign-interest — used in: case_study/new_clark_city.md
- Water-demand math (15B liters/1GW facility, Central Luzon deficit) — Luis Buenaventura, X thread, July 2026 — https://x.com/helloluis/status/2078689261461852432 — used in: case_study/new_clark_city.md
- Data center water transparency gap — AGU Advances (Privette et al.), Feb 2026 — https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025AV002140 — used in: README.md
- Investor pressure on Amazon/Microsoft/Google — Tom's Hardware, April 2026 — https://www.tomshardware.com/tech-industry/investors-push-amazon-microsoft-and-google-to-disclose-data-center-water-and-power-consumption — used in: README.md
- Data Center Water and Energy Transparency Act / POWER Act — ABA Water Spring 2026 Report — https://www.americanbar.org/groups/infrastructure-regulated-industries/resources/committee-articles/2026/water-spring-2026-report/ — used in: solutions/policy_solutions.md
- Durbin introduces Data Center Water and Energy Transparency Act — Durbin Senate press release, March 2026 — https://www.durbin.senate.gov/newsroom/press-releases/as-utility-costs-rise-durbin-introduces-new-legislation-to-bring-transparency-to-energy-and-water-consumption-by-data-centers — retrieved 2026-07-21 — used in: README.md, solutions/policy_solutions.md
- Illinois POWER Act fails to advance (session ended May 31, 2026) — Circle of Blue / Capitol News Illinois / STLPR, May–June 2026 — https://www.circleofblue.org/2026/water-policy-politics/illinois-fails-to-pass-landmark-act-requiring-responsible-data-center-energy-and-water-use/ — retrieved 2026-07-21 — used in: README.md, solutions/policy_solutions.md
- Company transparency rankings (Digiconomist) — Axios, July 10 2026 — https://www.axios.com/2026/07/10/ai-big-tech-transparency-electricity-water-use — used in: README.md
- Data center water problem policy recommendations — ITIF, July 6 2026 — https://itif.org/publications/2026/07/06/the-data-center-water-problem-is-soluble/ — used in: solutions/policy_solutions.md

## Corpus sources (primary documents, retrieved 2026-07-21)

- [Microsoft] "2026 Environmental Sustainability Report" (covers FY2025) — Microsoft, July 2026 — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Sustainability-Report-PDF.pdf — retrieved 2026-07-21 — used in: corpus/microsoft_sustainability_2026.txt
- [Google] "2026 Environmental Report" (covers FY2025) — Google, 2026 — https://storage.googleapis.com/gweb-mobius-cdn/sustainability/uploads/7f477eb723fe0c23d03f94b90a08882b9f28187d.pdf (linked from https://sustainability.google/reports/google-2026-environmental-report/) — retrieved 2026-07-21 — used in: corpus/google_environmental_2026.txt
- [Amazon] "2025 Amazon Sustainability Report" (covers FY2024; latest available as of July 2026) — Amazon, 2025 — https://sustainability.aboutamazon.com/2025-amazon-sustainability-report.pdf — retrieved 2026-07-21 — used in: corpus/amazon_sustainability_2025.txt
- [Meta] "2025 Sustainability Report" (covers FY2024; Meta's 2026 report not yet published as of July 2026 — reporting-cycle lag itself worth noting in the writeup) — Meta, Aug 2025 — https://sustainability.atmeta.com/wp-content/uploads/2025/08/Meta_2025-Sustainability-Report_.pdf — retrieved 2026-07-21 — used in: corpus/meta_sustainability_2025.txt

- [BCDA] "New Clark City to serve as AI hub under US-led Pax Silica Initiative" — BCDA press release, April 20, 2026 — https://bcda.gov.ph/news/new-clark-city-serve-ai-hub-under-us-led-pax-silica-initiative — retrieved 2026-07-21 — used in: corpus/bcda_paxsilica_2026.txt, case_study/new_clark_city.md
  - **Finding (absence):** the flagship 4,000-acre AI-hub announcement contains **zero mentions of water** — no supply plan, no consumption estimate, no watershed reference. Logged per corpus rule 4.
- [PH Government] "Defense chief dismisses water scarcity fears for Pax Silica project" — Manila Bulletin, July 20, 2026 — https://mb.com.ph/2026/07/20/defense-chief-dismisses-water-scarcity-fears-for-pax-silica-project — retrieved 2026-07-21 — used in: case_study/new_clark_city.md (Teodoro quotes; news article, deliberately NOT in corpus/ — scored corpus is limited to first-party statements so reporter prose doesn't contaminate the rhetoric scores)

- [PH Government] "BCDA reviewing Korean water proposal" — Tarlakenyo, Feb 2026 — https://tarlakenyo.com/2026/02/bcda-reviewing-korean-water-proposal/ — retrieved 2026-07-21 — used in: case_study/new_clark_city.md (K-Water/Maynilad ₱15B joint venture, 20–30M → 150M L/day capacity figures)

- [Microsoft] "2026 Environmental Sustainability Report — Data Fact Sheet" (covers FY2025) — Microsoft, July 2026 — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf — retrieved 2026-07-21 — used in: corpus/microsoft_datafactsheet_2026.txt, README.md
  - **Finding:** Table 15 ("FY25 Datacenter water and electricity use by location") discloses per-city electricity (MWh), water withdrawal (ML), % non-potable, and replenishment for ~29 named datacenter locations — the site-level disclosure the narrative report lacks (some cells withheld, marked * or —). The sentence-based scorer rates this document LOWER than the narrative (5.3% vs 8.5% pct_quant, both 0% site-level) because tabular disclosure is invisible to sentence-level scoring — a methodological boundary now noted in README.md.

**Corpus note:** text extracted from the official PDFs with pypdf (see analysis/). Extraction is lossy on tables/figures — cross-check any specific number against the original PDF page before quoting it.

## Verification pass — 2026-07-21

All seed sources re-checked (direct fetch where possible, search corroboration where bot-blocked):

- **Verified by direct fetch:** w.media (exact date: April 28, 2026), Manila Times (protest date July 13 confirmed; Tapang quotes verbatim), SCMP (July 17, 2026), ITIF (July 6, 2026, Robin Gaster; four policy recommendations confirmed), Tom's Hardware (headline confirms "more than a dozen shareholders", site-specific disclosure demand, ahead of annual meetings).
- **Live, verified via search (fetch bot-blocked, 403):** Rappler, Inquirer (5GW figure, BCDA sourcing power outside NCC, and Maharlika interest all corroborated), Axios (Digiconomist ranking confirmed: Meta 1st, Google/Microsoft toss-up 2nd, Amazon last; also — Amazon has the strongest water-efficiency *figure* while ranking last on transparency, and Microsoft newly disclosed site-level metrics, called "a significant improvement" by de Vries-Gao), ABA (bill facts confirmed via Durbin press release and Illinois coverage instead).
- **Paywalled, existence + thesis verified:** AGU Advances Privette et al. — "Data Centers Water Footprint: The Need for More Transparency," Privette, Barros & Cai, AGU Advances 7, e2025AV002140 (2026). The ~1 trillion liters (North America, 2025) figure is corroborated by multiple secondary sources; the previously cited "1.4 trillion liters by 2030" could NOT be corroborated and was replaced in README.md with UC Riverside's 1.1–1.7 trillion gallons by 2027 projection.
- **Unfetchable (login wall):** Buenaventura X thread — URL still live per search index; its 15B-liters-per-1GW estimate is consistent with Tapang's independently reported 5M gallons/day figure (≈7B liters/yr) as an order-of-magnitude cross-check, and is credited as an individual's estimate, not an official figure.

**Corrections applied this pass:** federal bill is the "Data Center Water and Energy Transparency Act" (Durbin, March 2026), not "Data Center Transparency Act, Jan 2026"; Illinois POWER Act (introduced Feb 11, 2026) died without a floor vote at the May 31, 2026 session end; README's unsupported 1.4T-liter 2030 projection replaced.

**Note:** re-verify again before any formal publication — Pax Silica in particular is developing week to week (framework signing targeted for the November 2026 ASEAN Summit).
