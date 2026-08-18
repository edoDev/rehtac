# Rehtac AI

Public site for [Rehtac](https://edodev.github.io/rehtac/) — lean AI systems for people who ship.

The landing page is the same design as `rehtac-ai-test.html` from the original session.

## Unlisted lab

`/projects/` is **not** linked from the public site. It is a single GitHub Pages tree that holds pet projects so we do not need a new Pages site for each one.

| Path | What lives here | Original repo |
|------|-----------------|---------------|
| [`/projects/stigref/`](projects/stigref/) | Hub + backlog. Live app stays on the original Pages site (≈117 MB of STIG JSON). | [edoDev/stigref](https://github.com/edoDev/stigref) |
| [`/projects/adaptpad/`](projects/adaptpad/) | Canonical AdaptPad app | [edoDev/AdaptPad](https://github.com/edoDev/AdaptPad) |
| [`/projects/mdc-hunt-calendar/`](projects/mdc-hunt-calendar/) | 2026–27 Jefferson County hunt calendar PWA | [edoDev/MDC-Hunt-Calendar-2025](https://github.com/edoDev/MDC-Hunt-Calendar-2025) |
| [`/projects/stl-fish-fry-finder/`](projects/stl-fish-fry-finder/) | St. Louis Friday fish-fry map | [edoDev/STLFishFryFinder](https://github.com/edoDev/STLFishFryFinder) |

Each project folder has a `BACKLOG.md`. The MDC Fall handbook is now published — verification items are unblocked. AdaptPad-Grok and AdaptPad-Claude are the same `index.html` as AdaptPad; reconciliation notes are in the AdaptPad backlog. stigref’s known component failures are listed in its backlog rather than copying 19k data files into this repo.

## Local preview

```powershell
cd C:\Rehtac
python -m http.server 8080
```

Then open http://localhost:8080/ and the unlisted hub at http://localhost:8080/projects/.

## Publish

Push `main`. GitHub Actions deploys Pages to `https://edodev.github.io/rehtac/`.
