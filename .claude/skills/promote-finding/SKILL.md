---
name: promote-finding
description: Drafts the promotion of a verified working-note finding (from context/FINDINGS.md or a just-completed research pass) into a public-facing doc — README.md, solutions/policy_solutions.md, case_study/*.md, corpus/README.md. Always drafts the exact edit and asks for explicit confirmation before writing it. Use when a finding is solid enough to leave "working notes" status.
---

# Promote a finding into a public doc

## Gate: check before drafting anything

A finding may only be promoted if:

1. It has a corresponding `data/sources.md` entry with a verification-method
   note (see `log-source`'s conventions) — not just "found on the internet."
2. If the underlying source is marketing/SEO/consulting-blog material with no
   visible methodology, it may NOT be stated as fact. Either find a better
   anchor (government, academic, or company-primary source) first, or phrase
   it explicitly as an unverified/directional claim with the caveat inline —
   the same treatment `solutions/policy_solutions.md` gives its trade-press
   cost figures ("single trade-press estimate, not a vendor spec sheet").
3. If it's a company's own claim about itself, it gets labeled as self-reported
   (matching how this repo treats Amazon's and Microsoft's ESG claims), not
   presented as independently confirmed.

If the gate fails, stop and say so instead of drafting an edit — tell the
caller (usually `research-topic`) what's missing (a better source, a caveat,
a self-report label) rather than promoting anyway.

## Drafting the edit

- Match the target file's existing voice: measured, hedges where evidence is
  thin, states single-source vs. multi-source explicitly, prefers "here's what
  we know and don't know" over confident synthesis. This project's own thesis
  is that confident language without backing is the failure mode it's
  documenting — its own writing should not repeat that failure.
- Prefer extending an existing table/section over adding new headers, unless
  the finding genuinely doesn't fit anywhere existing.
- Cross-reference other files where relevant (e.g. a cooling finding in the
  case study points at `solutions/policy_solutions.md` §2, and vice versa) —
  this repo consistently links related content across files rather than
  duplicating it.
- Show the exact diff (old text → new text, or the new block being added) in
  your response before writing anything.

## Confirmation

Ask the user to confirm the exact drafted edit before calling Edit/Write.
Don't ask a vague "should I proceed" — show the text and ask them to approve
or adjust it. This is a hard gate regardless of what invoked this skill.

## After applying

- Mention whether `context/PROJECT_STATE.md`'s "Last updated" line or "Where
  things stand" summary is now stale (don't update it automatically — that
  file is a snapshot the user maintains deliberately).
- Do not commit. That's `curate-commit`'s job, invoked separately and only
  when the user asks.
