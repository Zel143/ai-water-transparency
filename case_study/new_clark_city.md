# Case Study: Pax Silica and New Clark City, Tarlac

## Background

In April 2026 the Philippines became the 13th signatory of the Pax Silica Declaration, a US-led alliance (also including Australia, Japan, Singapore, the UK, and others) aimed at securing silicon, semiconductor, and AI supply chains. As part of this, a 4,000-acre (~1,620-hectare) site inside New Clark City, Capas, Tarlac was earmarked as an AI/data center industrial hub, with Foxconn reportedly anchoring the first facility. Projected electricity demand for the hub could reach at least 5 gigawatts — enough that the lead Philippine agency (BCDA) is already looking outside New Clark City for power sources.

## The Water Problem, Specifically

- A single 1GW data center at the site is estimated to require roughly 15 billion liters of water per year — about **2x New Clark City's current total water demand**.
- Tarlac province is already water-stressed: about a third of its rice fields lack direct irrigation and depend on pumps or rainwater.
- Central Luzon as a whole runs an estimated 5 trillion-liter annual water deficit.
- The Philippines experiences heavy rainfall overall, but local water *access* — not total rainfall — is the actual constraint, especially during summer months.

## Public Reaction

On July 13, 2026, a coalition of scientists, environmentalists, and farmers marched from Manila to the US Embassy to oppose the hub. Dr. Giovanni Tapang (UP College of Science) warned of a resource-conflict dynamic: because access to water at this scale will effectively go to whoever can pay for it, poorer residents risk losing out. Critics have also framed the deal as a form of resource "neocolonialism," pointing out the Philippines is the only Pax Silica member offering land at this scale.

## The Government's Water Rhetoric

The official record so far is an instance of the project's core pattern:

- **BCDA's flagship announcement (April 20, 2026) contains zero mentions of water.** The press release covers land area, lease terms, supply-chain framing, and job creation — no supply plan, consumption estimate, or watershed reference. (Full text in `corpus/bcda_paxsilica_2026.txt`; absence logged in `data/sources.md`.)
- **The first substantive government water statement came only after the protests** — Defense Secretary Gilberto Teodoro Jr., July 20, 2026: "There is no reason to worry. What we should be concerned about is the improper use of water. Water can also be recycled. If you collect water, you can build impounding systems." And: "The DENR or anybody will not approve any project without water system sustainability."

Note the form of the reassurance: assertive, zero quantities, no named source or watershed — deferring to a future regulatory approval rather than presenting a water balance. High confidence, low transparency, in exactly the sense the scorer measures for the corporate corpus.

## What's Being Done (as of mid-2026)

- A joint K-Water (Korea) / Maynilad bid — a proposed 50-year, ~₱15-billion joint venture — would manage New Clark City's water and wastewater systems, raising supply capacity from the current 20–30 million liters/day to ~150 million liters/day.
- New Clark City signed a partnership with Marubeni (Japan) in June 2026 to upgrade energy infrastructure.
- Neither of these is a completed water solution yet — they're the closest existing steps toward one. (For scale: 150M L/day ≈ 55B liters/year of *total city supply capacity* against ~15B liters/year demanded by each 1GW of data center.)

## Why This Case Study Matters for the Repo

Pax Silica is a live test of the exact disclosure-transparency question this project is built around: an international agreement was signed and a 4,000-acre commitment made *before* a public water plan existed. That sequencing — commitment first, water accounting later — is a pattern worth checking for in the corporate corpus too.

## Sources

- w.media, "Philippines earmarks 4,000-acre land as AI hub under US-led Pax Silica," 2026
- Manila Times, "Scientists, environmentalists, farmers hit Pax Silica AI hub," July 19, 2026
- Rappler, "What is Pax Silica? What are its goals, and what concerns does it raise?", 2026
- SCMP, "Philippines' Pax Silica AI hub plan slammed for mineral 'plunder'," 2026
- Inquirer, "Pax Silica's mammoth power needs draw Maharlika, foreign interest," 2026
- Luis Buenaventura (X/Twitter thread), water-demand estimate calculations, July 2026
- BCDA press release, "New Clark City to serve as AI hub under US-led Pax Silica Initiative," April 20, 2026
- Manila Bulletin, "Defense chief dismisses water scarcity fears for Pax Silica project," July 20, 2026
- Tarlakenyo, "BCDA reviewing Korean water proposal," Feb 2026 (K-Water/Maynilad joint venture details)

*(Log full URLs and retrieval dates in `data/sources.md`.)*
