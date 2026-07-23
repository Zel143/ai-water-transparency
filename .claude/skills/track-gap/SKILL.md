---
name: track-gap
description: Drafts a GitHub issue plus a context/NEXT_STEPS.md line for an open question, disclosure absence, or unresolved gap surfaced during research — matching this repo's established issue structure. Always drafts both and asks for confirmation before running gh issue create or editing NEXT_STEPS.md. Use when something is worth tracking over time rather than stating as settled fact.
---

# Track an open gap

## When this applies

Use for things that AREN'T resolved yet and need someone (a future you, or an
external actor) to close them later — a company hasn't disclosed something, a
technology choice is unconfirmed, a report hasn't been published yet. Not for
things that are just unfinished writing work (that's a plain TODO, not a
tracked gap) — the Pax Silica cooling-disclosure issue (#1) is the reference
example: a real-world fact is missing, not a repo task.

## Issue structure (reuse this exactly — it's the established template)

```markdown
## The gap

[What's missing, and what estimate/claim currently fills the silence by
default — name the specific sources checked that don't answer it.]

## Why it matters

[Tie back to this project's core thesis: confident/quantified language vs.
actual disclosure. Say concretely what would change if the gap were filled —
e.g. a number that would shift by an order of magnitude.]

## What's already public (and what it doesn't answer)

[Bullet each source that WAS checked, with date, and what it does/doesn't say.]

## What would close this

[Concrete things that would resolve it: a filing, a permit, a direct statement
naming the specific facility/decision, not just a general product-line claim.]

## Sources

[Same format as data/sources.md — title, publisher, date, URL, retrieved date,
verification method. Include a line explicitly flagging any claim that's
general-capability-only and not tied to the specific case (see the Schneider
Electric line in issue #1 as the pattern: "no source ties it to New Clark City
specifically — flagged here as a gap, not a citation of fact.")]
```

## Title convention

`<Entity/Project>: <what hasn't been disclosed>` — e.g. "Pax Silica / New Clark
City: cooling technology for the AI hub has never been publicly disclosed."
Specific enough to be searchable later, not a vague "investigate X."

## Label

Check `gh label list` first. Default GitHub labels only exist in this repo
(no custom ones yet) — `question` is the established fit for "we need more
information / confirmation from an external party" (used on issue #1). Don't
invent new labels without asking.

## NEXT_STEPS.md line

Append to the ordered queue in `context/NEXT_STEPS.md`, referencing the issue
number (create the GitHub issue FIRST, since the line cites its number):

```
<N>. Track whether <gap> — see GitHub issue #<issue-number>
    (<issue-url>). [One or two sentences: what the default assumption is right
    now, and what would materially change if the gap were resolved.] Re-check
    [triggering event/date if there is one].
```

## Confirmation

Draft the full issue body and the NEXT_STEPS.md line, show both, and ask for
explicit confirmation before running `gh issue create` or editing
`context/NEXT_STEPS.md`. This is a hard gate regardless of what invoked this
skill — opening a GitHub issue is a visible, external action.

## After creating

Report the issue URL back. If the user later asks to close it, close as
"documented" (repo-side) while distinguishing that from the real-world
question being resolved — see issue #1's closing comment as the pattern: don't
conflate "we wrote it down" with "the gap is actually filled."
