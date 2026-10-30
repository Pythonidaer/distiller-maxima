# Distiller Maxima publishing

Use Sites as the QA preview before GitHub Pages production releases. Preserve the QA site's audience. Publish to production when requested after review.

Before deployment, apply https://github.com/Pythonidaer/llm-instruction-toolkit/blob/main/design/publishing/link-previews.md. Prepare initial-HTML metadata and static share images, preserve indexing intent, and verify deployed pages and images. Report platform-preview testing separately from implementation.

Run `python guides/build.py` and `python guides/check.py`. Metadata defaults to https://pythonidaer.github.io/distiller-maxima/ including the project subdirectory. For Sites QA, set SITE_ORIGIN to the QA origin so preview assets use that deployment. Canonical page URLs always point to production. Preserve current noindex decisions unless explicitly requested otherwise.

Static share artwork and icons are committed in dist/assets. Regeneration is optional with `python guides/generate-share-assets.py` (Pillow required). The normal build does not require Pillow.
