# STL Fish Fry Finder backlog

**App on this site:** [../stl-fish-fry-finder/](./)  
**Original:** https://github.com/edoDev/STLFishFryFinder · https://edodev.github.io/STLFishFryFinder/  
**Updated:** 2026-08-18

Single-page Leaflet map of Friday fish fries within about 60 miles of St. Louis. Dataset was compiled from a February 2026 multi-source search prompt. There was no project backlog before this file.

## Now

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| F-001 | Mark every listing with last-verified date and source URL | P0 | open | Treat current pins as unverified until a human pass. |
| F-002 | Confirm Lent-only vs year-round vs “other Fridays” | P0 | open | This is the main product claim. |
| F-003 | Drop closed / moved / one-off events | P0 | open | Especially church halls that change each year. |
| F-004 | Hours, price band, and cash-vs-card on the detail pane | P1 | open | |
| F-005 | Distance filter from a chosen point (downtown / home) | P1 | open | Radius is currently a compile-time 60 miles. |
| F-006 | Mobile layout: map / list / detail stacking | P1 | open | Desktop three-pane is tight on a phone. |

## Later

| ID | Item | Pri | Status | Notes |
|----|------|-----|--------|-------|
| F-007 | Lent 2027 refresh pass | P1 | open | Next seasonal deadline. |
| F-008 | “Open now / this Friday” chip during Lent | P2 | open | Needs hours (F-004). |
| F-009 | User correction via mailto or a form (no backend) | P2 | open | |
| F-010 | Illinois vs Missouri filter | P2 | open | |
| F-011 | Offline cache of the page + tiles policy | P3 | idea | Tiles are a CDN; do not promise full offline maps. |
| F-012 | Split listings into a JSON file | P2 | open | Same move the hunt calendar already made. |

## Out of scope

- Paid placement or affiliate links
- Scraping Facebook at browse time
- Claiming completeness
