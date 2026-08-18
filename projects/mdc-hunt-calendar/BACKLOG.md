# MDC Hunt Calendar backlog

**App on this site:** [../mdc-hunt-calendar/](./)  
**Original:** https://github.com/edoDev/MDC-Hunt-Calendar-2025 · https://edodev.github.io/MDC-Hunt-Calendar-2025/  
**Updated:** 2026-08-18

## Handbook pass (2026-08-18)

Verified against local copies:

- `2026 FDT_508.pdf` — *2026 Fall Deer & Turkey Hunting Regulations and Information* (MDC, PDF dated 2026-06-16, 72 pages)
- `Missouri_White-Tailed_Deer_Management_Plan_2025.pdf` — *Missouri White-tailed Deer Management Plan 2025–2034* (strategic only; no Jefferson dates)

| ID | Item | Pri | Status | Result |
|----|------|-----|--------|--------|
| M-000 | Drop year from product title | P0 | done | `MDC Hunt Calendar` in `<title>`, `<h1>`, manifest, PNG/iCal names |
| M-001 | Jefferson antlerless open-county status | P0 | done | **OPEN.** FDT p.25 orange; 3 CSR 10-7.433 lists Jefferson. Four firearms antlerless permits (p.17). Hatched bars removed. |
| M-002 | 2026 mandatory CWD sampling | P0 | done | Jefferson **not** on Nov 14–15 2026 map (FDT p.7). Voluntary testing all season. |
| M-003 | Deer Telecheck wording | P0 | done | Out of county **or** 10 p.m. day of harvest, **whichever comes first** (FDT pp.6, 64–65). |
| M-004 | Link published handbook | P0 | done | Footer + header link to `2026 FDT_508.pdf`. Plan PDF linked as context. |
| M-005 | Bump service-worker cache | P0 | done | `mdc-cal-2026-08-18` |
| M-006 | Clear “booklet pending” reminder | P1 | done | Reminder removed. |

Season dates on p.72 match what was already in the app. Bear overlay was not in the FDT booklet; still sourced from 3 CSR 10-7.900 / MDC bear pages.

## Built

- 2026–27 deer dates and calendar window Sep 1 2026 – Jan 15 2027
- CWD management-zone banner removed; early/late antlerless layers
- Black bear Oct 17–30, BMZ 2, permit-status setting, quota hotline
- Scouting locations / sessions / observations + JSON export/import
- Trip notes with optional on-device GPS
- Stand-wind matcher (manual wind; MODEL/LOG)
- Pre-season scouting report
- Offline PWA (manifest + service worker)
- REG / MODEL / LOG labeling
- Year dropped from the product title
- 2026 FDT booklet verification for Jefferson County
- Year-over-year 2025–26 → 2026–27 breakdown (`CHANGES-2026.md` + in-app What's new)

## Next features

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| M-010 | Tighten phone layout under ~480px | P1 | open | Next 7/14 day views exist; month grid is still desktop-first. |
| M-012 | Prime legal-light shading on day cells | P2 | open | Already computed. Confirm it is visible, not only documented. |
| M-013 | Fall turkey overlay | P2 | open | FDT p.72: archery turkey same window as archery deer; firearms turkey Oct 1–31 in open counties (p.22). Still a product call. |
| M-014 | Configurable location (not only Pevely) | P2 | open | Changes sun/rut assumptions — must stay labeled. |
| M-015 | Persistent-storage nudge + export reminder | P2 | open | iOS can evict localStorage. |
| M-016 | Season summary report (days hunted / harvests) | P2 | open | |
| M-017 | Weather strip (online, cached, stamped) | P3 | idea | CORS / key decision. |
| M-018 | Managed-hunt markers for nearby CAs | P3 | idea | FDT pp.32–40; only if a hunt is in reach of Pevely. |

## Truth rule

No regulatory date ships without `source_url` + `verified_date`. The Fall booklet is the authority for deer/turkey season facts. The deer management plan is strategy, not a date source.
