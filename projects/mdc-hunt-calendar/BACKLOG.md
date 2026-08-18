# MDC Hunt Calendar backlog

**App on this site:** [../mdc-hunt-calendar/](./)  
**Original:** https://github.com/edoDev/MDC-Hunt-Calendar-2025 · https://edodev.github.io/MDC-Hunt-Calendar-2025/  
**Updated:** 2026-08-18

The July 2 planning backlog said “no code changes yet.” That is stale. The copied app already has the 2026–27 window, bear overlay, scouting planner, JSON season file, and PWA shell.

**MDC Fall Deer & Turkey Hunting Regulations handbook is now published.** Verification work is unblocked. Do not hunt off unverified hatched bars.

## Now — handbook pass

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| M-001 | Re-verify Jefferson County antlerless open-county status | P0 | open | `needs_verification: county_open_status` on early + late antlerless. |
| M-002 | Re-verify 2026 mandatory CWD sampling counties / days | P0 | open | Advisory still says “voluntary_expected” from 2025. |
| M-003 | Confirm deer Telecheck wording against the booklet | P0 | open | App says 10 p.m. day of harvest. |
| M-004 | Link the published handbook in the footer and `seasons-2026.json` | P0 | open | Replace “when published” language. |
| M-005 | Bump `sw.js` cache id after any regulation edit | P0 | open | Current cache: `mdc-cal-2026-07-02`. |
| M-006 | Clear the in-app “booklet pending” reminder once M-001–M-004 land | P1 | open | Reminder id `booklet-verification`. |

## Built (do not rebuild)

- 2026–27 deer dates (commission Dec 12, 2025) and calendar window Sep 1 2026 – Jan 15 2027
- CWD management-zone banner removed; early/late antlerless layers
- Black bear Oct 17–30, BMZ 2, permit-status setting, quota hotline
- Scouting locations / sessions / observations + JSON export/import
- Pre-season scouting report
- Offline PWA (manifest + service worker)
- REG / MODEL / LOG labeling

## Next features

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| M-010 | Phone layout under ~480px (week strip / agenda) | P1 | open | Desktop/print is the current bias. |
| M-011 | Stand-wind matcher with manual wind entry | P1 | open | Offline-native. Label as MODEL. |
| M-012 | Prime legal-light shading on day cells | P2 | open | Already computed. |
| M-013 | Fall turkey overlay | P2 | open | Dates overlap the window; still an open product call. |
| M-014 | Configurable location (not only Pevely) | P2 | open | Changes sun/rut assumptions — must stay labeled. |
| M-015 | Persistent-storage nudge + export reminder | P2 | open | iOS can evict localStorage. |
| M-016 | Season summary report (days hunted / harvests) | P2 | open | |
| M-017 | Weather strip (online, cached, stamped) | P3 | idea | CORS / key decision. |

## Truth rule

No regulatory date ships without `source_url` + `verified_date`. Handbook citations replace newsroom-only citations wherever the booklet is the authority.
