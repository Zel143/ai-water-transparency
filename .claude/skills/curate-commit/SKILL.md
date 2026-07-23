---
name: curate-commit
description: Reviews pending working-tree changes in ai-water-transparency, drafts a commit message matching this project's history style, and asks for confirmation before committing — then asks separately before pushing. Use at the end of a research/curation session, or whenever the user asks to commit or push.
---

# Commit and push curated changes

## Only when explicitly asked

Never invoke this speculatively at the end of a research pass just because
files changed — this project's rule (and Claude Code's general one) is commit
only on explicit request. `research-topic` should mention that changes are
ready, not trigger this skill on its own.

## Review before drafting

1. `git status` — check what's actually staged/unstaged. Note if
   `context/*.md` files show as changed — they're gitignored
   (`.gitignore:6: context/`) and will never appear in `git status` as
   trackable; if the user asks to commit something under `context/`, say so
   instead of trying (see the prior exchange where this was clarified).
2. `git diff` on everything about to be committed — read it, don't just trust
   the file list. Flag anything that looks like it doesn't belong (a stray
   scratch file, something that reveals a source not yet logged in
   `data/sources.md`).
3. `git log --oneline -10` for style calibration.

## Commit message style (match existing history)

This repo's commits read like: `<Action> <what>: <the interesting finding or
reason>`, e.g. "Add v3 table scorer: structured site-level disclosure inverts
the rhetoric ranking" or "Source verification pass: correct bill name/date,
POWER Act outcome, water projections." Lead with the verb, keep the subject
line under ~70 characters, and let the body (if any) carry the "why" — usually
one or two sentences, not a bullet list. Never mention this skill, Claude, or
the automation pipeline in the message itself.

## Confirmation gates (both required, separately)

1. Show the drafted commit message and the file list before running
   `git commit`. Wait for explicit go-ahead.
2. After committing, ask separately before `git push` — do not chain them
   automatically even if the user approved the commit. A push is visible on
   the shared remote; a commit alone is not.

## Standard git safety

No `--amend`, no `--no-verify`, no force-push, no committing anything under
`context/` (gitignored on purpose — see `.gitignore`). Stage specific files by
name, not `git add -A`, and check `git status` after staging to confirm
nothing unexpected got swept in.
