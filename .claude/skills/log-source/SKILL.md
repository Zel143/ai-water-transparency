---
name: log-source
description: Appends a citation to data/sources.md in this project's established format, including a verification-method note. Use whenever a source has been found (and verified, or explicitly marked unverifiable/excluded) and needs to be logged before its content is used anywhere else in the repo. Usually invoked by research-topic, but can be called directly.
---

# Log a source to data/sources.md

## Format (from the file's own header — do not deviate)

```
- [Company/Topic] "Title" — Publisher, Date — URL — retrieved YYYY-MM-DD — used in: [file(s)]
```

In practice, established entries also append a verification-method clause
after the `used in:` pointer (or folded into the line) — reuse these phrasings
rather than inventing new ones, so the log stays scannable:

- `verified by direct fetch` — WebFetch succeeded and content was read directly.
- `via search corroboration (fetch blocked)` / `search-verified` — WebFetch
  failed (403/paywall) but the claim is corroborated across 2+ independent
  outlets via WebSearch.
- `paywalled, existence + thesis verified` — could not read the full text but
  confirmed the source exists and its headline claim, via secondary coverage.
- `unfetchable (login wall)` — noted but flagged as an individual's estimate
  or otherwise not an official figure, per the Buenaventura X-thread precedent.
- `search-verified absence` — used when the finding IS that a source does
  NOT mention something (e.g. BCDA's zero water mentions); state what was
  searched for and confirm nothing was found, don't just assert absence.

## Where it goes

Append under a dated section header for the research pass
(`## <Topic> research (retrieved YYYY-MM-DD)`), matching the existing pattern
of dated sections in the file (e.g. "Verification pass — 2026-07-21",
"Cooling systems research (retrieved 2026-07-23)"). Create a new header if none
exists yet for this topic/date; don't scatter entries under unrelated headers.

## Sources to explicitly exclude, not silently omit

If a source was considered and rejected — no visible methodology, marketing
copy, unsourced numbers repeated across several similar sites, a vendor
comparing itself to a strawman — **log that exclusion too**, in a `**Caveat:**`
line at the end of the section, naming the sites and why. This project treats
"what we deliberately didn't cite and why" as part of the record (see the
cooling-systems research precedent excluding introl.com, Adam Silva
Consulting, IPValueLabs, and Energy Solutions Intelligence, and the Vantage
Data Centers blog's self-comparison-to-a-strawman).

## After logging

Report back to whatever invoked this (usually `research-topic`) with a
one-line confirmation of what was logged and under which header, so the
calling skill can reference it when writing the FINDINGS.md entry or a
promotion/issue draft.
