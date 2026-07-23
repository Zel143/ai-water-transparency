---
name: research-topic
description: Orchestrates this project's research pipeline for a new topic or question (e.g. "find sources for X", "research Y for the case study"). Searches, verifies against primary sources, logs citations, writes a working-note finding, then hands off to promote-finding and/or track-gap. Use whenever the user asks to research, source, or investigate something for ai-water-transparency.
---

# Research a topic for ai-water-transparency

You are the orchestrator for this project's research pipeline. Four other skills
in this directory do specific jobs — `log-source`, `promote-finding`, `track-gap`,
`curate-commit` — and you call them via the Skill tool at the right point below.
Do not reimplement their jobs inline; invoke them.

## When this runs

Any request to research, source, investigate, or "find out about" a topic
relevant to corporate water disclosure, AI data center infrastructure, or the
Pax Silica / New Clark City case study.

## Pipeline

### 1. Search

Run WebSearch across enough angles to triangulate, not just one query — this
project has been burned before by single-source numbers (see the Amazon
9.4B/9.4B episode in `context/FINDINGS.md`). 3-5 queries covering different
facets of the topic is typical.

### 2. Verify — this is the step that matters most

This project's non-negotiable rule (see `context/FINDINGS.md` and
`data/sources.md`'s "Verification pass" precedent): **quantified is not the
same as verifiable.** For every number or claim you intend to use:

- WebFetch the primary source directly where possible (official report, .gov
  press release, company blog, academic paper).
- If WebFetch is blocked (403, paywall — this repo has a known list: Rappler,
  Inquirer, Axios, ABA, Authorea, Tom's Hardware among others), corroborate via
  WebSearch across 2+ independent outlets instead, and say so explicitly in the
  citation ("via search corroboration, fetch blocked").
- **Flag marketing/SEO/consulting-blog sources that lack a visible primary
  source or methodology.** Numbers that "converge" across several such sites
  are not independent corroboration of each other — they're often the same
  unsourced number copy-pasted. Do not treat them as verified; note them as
  "directionally consistent, not independently verified" and prefer a
  government, academic, or company-primary source instead (see the cooling-
  systems research precedent: Microsoft's own blog and LBNL/NERSC were used as
  anchors; introl/Adam Silva Consulting/IPValueLabs/Energy Solutions
  Intelligence were explicitly NOT logged as sources).
- A company's own claim about itself (a vendor blog, an ESG report) is a
  source, but label it as self-reported, not independent — same treatment this
  project already gives Amazon's and Microsoft's own sustainability claims.

### 3. Log every source — call `log-source`

Invoke the `log-source` skill once per source (or once for a batch from the
same research pass) with: title, publisher, date, URL, retrieval date (today),
verification method, and which file(s) will use it. This is not optional even
for sources you plan to exclude — logging the exclusion and why is itself part
of this project's paper trail (see the "Caveat" blocks already in
`data/sources.md` and `context/FINDINGS.md`).

### 4. Write the working-note finding

Append a dated section to `context/FINDINGS.md` (gitignored working notes)
summarizing what was found, what's verified vs. not, and any numbers worth
carrying forward. Follow the existing style in that file: plain statement of
the finding, then caveats, then what's still open. Do not touch any public doc
(`README.md`, `solutions/policy_solutions.md`, `case_study/*.md`,
`corpus/README.md`) at this step — that's `promote-finding`'s job, and it
requires confirmation.

### 5. Hand off

- If the finding is solid enough to belong in a public doc (verified against a
  primary/independent source, not just marketing-blog convergence): invoke
  `promote-finding` with the finding and its target file. It will draft the
  edit and ask for confirmation itself — you don't need to ask again.
- If the research surfaced an open question, a disclosure absence, or
  something worth tracking over time rather than stating as settled: invoke
  `track-gap` with the gap description. It drafts a GitHub issue + a
  `context/NEXT_STEPS.md` line and asks for confirmation before creating either.
- If files were written this session and the user hasn't said whether they
  want to commit: don't invoke `curate-commit` unprompted — mention that
  changes are ready to commit and let the user ask (this project's git-commit
  rule is "only when explicitly requested").

## What never happens automatically

Per this project's autonomy setting: research, verification, and writing to
`context/FINDINGS.md` / `data/sources.md` proceed without asking. Editing any
public-facing doc, opening a GitHub issue, or any git operation always pauses
for explicit confirmation — enforced by `promote-finding`, `track-gap`, and
`curate-commit` themselves, not by you re-asking on top of them.
