# stigref backlog

**Home:** [Rehtac lab](../) · **Live app:** https://edodev.github.io/stigref/  
**Source:** https://github.com/edoDev/stigref  
**Updated:** 2026-08-18  
**Status:** Migrated as a hub only. Do not mark the product healthy until P0 items below are re-verified on the live site.

The July 2026 in-repo backlog listed every feature `done`. That is not the working truth. Several basic surfaces fail or are empty. This file is the Rehtac-level list.

## Now

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| S-001 | Reproduce and write down which basic UI pieces fail | P0 | open | Search, rule open, copy packs, product hubs, KEV, insights. Start from a cold Pages load. |
| S-002 | Search must return ranked hits without a full 21 MB index download | P0 | open | Shards exist; confirm they load on Pages and the worker does not die. |
| S-003 | Opening a rule by ID (`SV-…`) must show check/fix text | P0 | open | Today this means one JSON fetch per rule among 19k files. Failures look like “component is broken.” |
| S-004 | Shareable deep links must survive refresh on GitHub Pages | P0 | open | SPA + `base: /stigref/`. 404 on refresh is a basic-component fail. |
| S-005 | Copy ID / citation / check / fix must work without a console error | P0 | open | Clipboard path + fallback. |
| S-006 | CCI browser and NIST page must not be empty shells | P1 | open | Live `meta.json`: `controls: 0`, `ccis: 0`. NIST is a stub. |
| S-007 | Product hub / Intune meter must load or show a real error | P1 | open | Retry UI exists; confirm it is what users actually see. |
| S-008 | Next DISA quarterly import (post April 2026) | P1 | open | Dual-quarter tree tooling is ready; content is not. |
| S-009 | Decide whether Rehtac will ever host the data | P2 | open | Only after a thinner artifact (few shards, not 19k files). |

## Later

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| S-010 | Split `RuleDetailPage` | P2 | open | Accepted residual from July review. |
| S-011 | Playwright smoke against Pages | P2 | open | No e2e today. |
| S-012 | CIS ID cleanup against Workbench PDFs | P2 | open | Content, not code. |
| S-013 | Rebuild with a new Vite `base` if we ever nest the app | P2 | blocked | Blocked on S-009. |

## Explicitly not doing here

- Copying `data/rules/by-id/*` into `C:\Rehtac`.
- Turning stigref into an assessment tool (STIG Manager / eMASS / .ckl).
- CUI / CAC-only libraries.

## Evidence snapshot (live `data/meta.json`, fetched 2026-08-18)

- `stigs`: 303 · `rules`: 19403 · `searchDocuments`: 19706
- `rulesWithCve`: 5 · `rulesWithKev`: 0 · `controls`: 0 · `ccis`: 0
- Source zip: `U_SRG-STIG_Library_April_2026.zip`
- On-disk library: 117.26 MB / 19,725 files
