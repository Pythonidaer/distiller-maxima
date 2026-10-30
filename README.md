# Distiller Maxima

A collection of over 200 freeCodeCamp resources organized into two roadmaps and original reading guides. The About page explains the project, its process, and its limits for readers.

## Development

This is a buildless HTML, CSS, and JavaScript site. Serve `dist/` locally. Run `python3 guides/build.py` after changing templates or commentary, followed by `python3 guides/check.py`. The check verifies all 206 source links, 102 guide targets, and local links.

`guides/home.html` and `guides/about.html` are page templates. `guides/build.py` generates the shared navigation, methodology disclosure, article collection, guides, and source links. `guides/material_icons.py` inserts Google's Material Icons SVGs; paths are unchanged, with decorative SVG wrappers adapted for currentColor and accessibility. See `dist/MATERIAL-ICONS-LICENSE.txt` (Apache-2.0) and https://github.com/google/material-design-icons.

Roadmap visuals borrow the approach of https://roadmap.sh/ for educational purposes, adapted through the typography-learning project. No affiliation or endorsement is implied.

## Deployment

Pushes to main run the GitHub Pages workflow, validate the site, and upload `dist/`. If automatic Pages enablement is unavailable, select GitHub Actions under Settings → Pages.

See [METHODOLOGY.md](METHODOLOGY.md) for writing, navigation, and responsive-template rules. Written resource pages informed original commentary; video courses were not watched and tutorial code was not run.
