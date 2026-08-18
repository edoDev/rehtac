# AdaptPad backlog

**App on this site:** [../adaptpad/](./)  
**Original:** https://github.com/edoDev/AdaptPad · https://edodev.github.io/AdaptPad/  
**Updated:** 2026-08-18

## Fork reconciliation

Three GitHub repos exist. Their `index.html` is **the same file** (SHA-256 `044FE55E…`, 53,250 bytes, 1,231 lines).

| Repo | Extra files | Code delta vs AdaptPad |
|------|-------------|------------------------|
| `edoDev/AdaptPad` | `todo.md` | Canonical |
| `edoDev/AdaptPad-Grok` | `.grok/` forge prompts + same `todo.md` | None |
| `edoDev/AdaptPad-Claude` | `AdaptPad-main.zip` + same `todo.md` | None |

**Decision for this lab:** ship one copy (`/projects/adaptpad/`). Keep the Grok forge notes as context, do not merge a second editor. Later: archive or redirect the fork repos so they stop looking like parallel products.

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| A-000 | Declare this tree the canonical AdaptPad | P0 | done | Copied 2026-08-18 |
| A-000b | Archive or README-redirect AdaptPad-Grok and AdaptPad-Claude | P2 | open | After this site is the daily URL |

## Broken / half-working (from the original `todo.md`)

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| A-001 | Paragraph format from the style dropdown | P0 | open | Suspected unclosed theme/style tag. Add a Normal option. |
| A-002 | Table export formatting | P0 | open | Tables do not survive export cleanly. |
| A-003 | Find and replace | P1 | open | |
| A-004 | Pretty vs raw/code view next to export | P1 | open | See the markup, not only the rendered page. |
| A-005 | Filename box in the header | P1 | open | |
| A-006 | Default export name = first 60 chars of the first line | P1 | open | When no name is set. |
| A-007 | Code block option | P2 | open | Toolbar already has a Code Block control — confirm it works. |
| A-008 | Print | P2 | open | |
| A-009 | Wider page, narrower default margins | P2 | open | |
| A-010 | Always keep ~5 trailing blank lines so the page can grow | P2 | open | |

## Later

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| A-011 | Images → text (OCR) | P3 | idea | Heavy for a no-backend pad. Only if it stays optional. |
| A-012 | Send to Grok / Claude / GitHub | P3 | idea | Conflicts with the “no decorative AI chrome” Grok-fork rule. Needs an explicit product call. |
| A-013 | Post to a social story | P3 | idea | Same. |
| A-014 | Share URL that encodes the whole document | P3 | idea | Original note: “RIP text messages.” Cap size or drop. |

## Constraint from AdaptPad-Grok

The Grok fork never changed code, but it did lock a vibe: instant load, no typing lag, no settings drawers, no background work the user did not ask for. Prefer fixing A-001–A-006 over adding A-012–A-014.
