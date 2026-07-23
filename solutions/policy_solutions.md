# Solutions: Water Consumption & Transparency

Organized by who has to act, since "we need accountability" only becomes actionable once you know which lever belongs to whom.

## 1. Disclosure & Governance (regulators, investors)

| Solution | Status (mid-2026) | Feasibility |
|---|---|---|
| Standardized facility-level water reporting (not just global aggregates) | Proposed federally (Durbin's Data Center Water and Energy Transparency Act, March 2026); Illinois POWER Act (Feb 2026) died without a vote at May 31, 2026 session end | Medium — faces industry pushback on compliance cost; Illinois outcome shows even disclosure-only mandates stall |
| Mandatory water-risk assessment before new facility approval | Recommended by ITIF (2026), not yet mandatory | High — cheapest lever, mostly a paperwork/process change |
| Investor-driven disclosure pressure (shareholder proposals) | Already happening — 12+ investors pressed Amazon/Microsoft/Google ahead of 2026 AGMs | High — already moving without new law |
| Disclosure of water/energy commitments *inside* incentive agreements (tax breaks, land deals) | Not currently required | Medium — directly relevant to cases like Pax Silica, where the land deal preceded any public water plan |

## 2. Engineering / Technical

Cooling is the one lever a company controls directly (no legislation needed), which is why it belongs here with real numbers, cost included — the point of this table is to price out the alternatives to evaporative cooling, not to pre-filter for the cheapest one.

| Solution | Water impact | Cost / energy trade-off | Status (mid-2026) |
|---|---|---|---|
| Closed-loop, zero-water-evaporation chip-level cooling | Avoids >125 million liters/year per datacenter vs. an evaporative design of the same size (Microsoft's own figure) | "Nominal increase" in annual energy use per Microsoft, offset by warmer loop temperatures + high-efficiency economizing chillers — no cost figure disclosed | Piloting in Phoenix, AZ and Mt. Pleasant, WI in 2026; Microsoft's stated goal is fleet-wide by late 2027 for all datacenters designed from Aug 2024 onward |
| Direct-to-chip (D2C) liquid cooling | Eliminates the water draw open evaporative towers require; now the default for high-density AI racks (Blackwell-class GPUs exceed air cooling's ~40 kW/rack physics ceiling) | ~$650,000 per MW of cooling capacity (trade-press estimate) — cheaper than immersion, pricier than air/evaporative to install | Already dominant for new AI-training halls; Google's Ironwood TPUs and Microsoft's Azure fleet both liquid-cooled from the chip up |
| Immersion cooling (single- and multi-phase) | Same water elimination as D2C, plus a much smaller mechanical footprint | ~$1,000,000 per MW for single-phase; multi-phase costs more still and is "impractical for budget-conscious data centers" per trade press — the most expensive mainstream option, deployed anyway at the highest densities | Niche but growing for the highest-density racks where D2C isn't enough |
| Air-cooled / dry closed-loop systems generally | Removes evaporative water loss entirely | Directionally verified independently: a 2-year Lawrence Berkeley National Lab efficiency effort on NERSC's liquid/direct-to-chip-cooled Perlmutter system cut non-IT power 42%, saving >2M kWh and ~500,000 gallons of water a year (~$200k/year) — real measured numbers, not a vendor estimate | Ongoing at DOE-operated supercomputing facilities; Doudna (NERSC's next flagship) due late 2026 on the same approach |
| Reclaimed/greywater cooling | Already used by some hyperscalers; needs local wastewater infrastructure (see Maynilad's New Clark City proposal) | Avoids the capital cost of a redesigned cooling loop, but shifts the burden onto local water infrastructure instead of removing it | K-Water/Maynilad JV proposal (see case study) |
| Site selection tied to real watershed capacity, not just power/land availability | Prevents the failure mode outright rather than mitigating it after the fact | Cheapest lever in principle (a siting decision, not new hardware) but requires giving up otherwise-attractive sites | The core failure mode in New Clark City — land and power were secured before water was |
| Waste heat reuse (district heating, etc.) | Doesn't solve water use directly but reduces the cooling load driving it | Requires a nearby heat-demand customer (district heating network, industrial user) to be economical | Limited outside dense urban/industrial contexts |

**Caveat on the cost figures above:** the $650k/MW (D2C) and ~$1M/MW (single-phase immersion) numbers come from a single trade-press comparison (Data Center Knowledge), not a vendor spec sheet or an institutional study — treat them as one estimate, not a market consensus. Several data-center-consulting marketing sites converge on similar ranges (roughly $2,500–4,500/kW premium over air cooling, 90–98% water-use reduction for immersion) but none of them cite primary data, so those are noted here as directionally consistent, not independently verified — do not upgrade them to cited facts without a better source (vendor quote, ASHRAE/Uptime Institute figure). The Microsoft and LBNL figures above are the two anchors in this table actually verified against a primary source; see `data/sources.md`.

## 3. Community / Local Level

- Local watershed-level environmental review requirements before large loads are approved (ITIF recommendation)
- Public, non-technical water-impact summaries for affected communities — not just ESG-report language aimed at investors
- Independent third-party audits (e.g., the VU Amsterdam/Digiconomist transparency rankings) as a public accountability mechanism separate from self-reported ESG data

## The Honest Caveat

None of these solutions fix the underlying tension: AI compute demand is rising faster than water-efficient cooling tech is being deployed. Disclosure alone doesn't reduce consumption — it just makes the trade-off visible. Your repo's contribution is making that trade-off *harder to obscure with confident language*, not solving the physics of cooling a GPU cluster.
