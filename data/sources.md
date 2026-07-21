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
- Data Center Transparency Act / POWER Act — ABA Water Spring 2026 Report — https://www.americanbar.org/groups/infrastructure-regulated-industries/resources/committee-articles/2026/water-spring-2026-report/ — used in: solutions/policy_solutions.md
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

**Corpus note:** text extracted from the official PDFs with pypdf (see analysis/). Extraction is lossy on tables/figures — cross-check any specific number against the original PDF page before quoting it.

**Note:** re-verify these are still live/accurate before publishing the repo publicly — several are recent news items (weeks old as of this scaffold) and situations like Pax Silica are actively developing.
