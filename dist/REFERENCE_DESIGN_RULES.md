# Typography roadmap design rules

These rules apply to the approved Typography roadmap, including its integrated typography-learning/roadmap/ page. They supplement the Type Study website baseline and override its general component sizing only inside the diagram. The reference is the compact roadmap.sh diagram shown in Johnny’s screenshots, not a conventional mobile card layout.

## 1. Content and provenance

- Use the 43 terms, definitions, and examples from Pythonidaer/typography-learning `dist/vocabulary.html` as the vocabulary source.
- Keep each source term’s ID and link directly to its vocabulary entry.
- Use the source’s six groups as the main sequence. Group introductions and practice prompts are authored for this roadmap; record that distinction in project documentation rather than a repetitive label in every lesson.
- Place full definitions, examples, practice, and source links in the opened lesson, not in diagram boxes.
- Do not silently replace the vocabulary with a different curriculum. Review updated source content before synchronizing later changes.

## 2. Diagram density

- Show one concise term per box. No second-line “Open topic,” “Main topic,” or progress sentence.
- Use a 1000-unit design canvas, 16-unit diagram text, 38-unit box heights, 44-unit branch row pitch, 240-unit main nodes, and 280-unit supporting nodes.
- Center text with 3-unit vertical and 8-unit horizontal padding. The single-line label, not a large touch-card convention, determines the box’s height.
- Keep main nodes visually distinct using weight and a light neutral fill. Keep supporting boxes white with a clear dark outline.
- Box outlines use a subtle 4-unit corner radius, an intentional reference-specific exception to the original square diagram treatment.
- Avoid stage counters and repeated titles outside the main topic node.
- Do not change the graph into large stacked cards on mobile.

## 3. Fit and zoom

- Preserve the same graph geometry across device sizes.
- Start at Fit: scale the complete canvas to the available container width, never wider than its natural design width.
- Reserve the scaled graph’s actual height and width; a transformed 1000px canvas must not create unintentional document overflow.
- Keep browser pinch zoom enabled. Do not add a Zoom/Fit selector or its toolbar; the diagram fits automatically.
- Use the browser’s native zoom and panning behavior. Do not introduce a second manual scale state.
- Tiny fit-scale labels are an explicitly requested overview mode. Keep native pinch zoom available for readable labels and larger interaction targets. Do not add a list view, search input, or progress bar. Do not claim compressed targets meet ordinary minimum target-size guidance.
- Navigation and lesson controls retain usable text and control sizes; their sizing is independent of diagram scaling.

## 4. Connections

- Use a clearly contrasting blue connection color (#3378ba), with neutral boxes. Blue connections are a scoped exception to Type Study’s original all-neutral palette.
- Main sequence: solid, 4-unit stroke.
- Supporting relationships: dotted, 3-unit stroke, round caps, dash pattern 1 7.
- Fan-out branches: cubic Bézier curves from the main box side to the supporting box’s facing side. Do not use rigid repeated elbows for all relationships.
- Define thickness, dash pattern, and curve geometry separately so they can be changed independently.
- Keep lines behind nodes and terminate them exactly at node boundaries.
- Encode relationships in edge data; styling must correspond to meaning, not random decoration.
- Use a small line legend describing the actual relationship styles.

## 5. Header and embedded scrolling

- The site owns one vertical scroll container (`siteShell`) with viewport height.
- Put the header first in that container and use `position: sticky; top: 0` inside it.
- Do not position the header against the outer native webview’s moving viewport with `position: fixed`.
- Do not add a duplicate fixed-header spacer or body top padding. Sticky positioning preserves the header’s normal layout footprint.
- Keep the header outside transformed or scaled diagram ancestors.
- Track scroll styling against the actual site scroll container.
- Retain the opaque navigation dropdown and keyboard dismissal behavior.
- The site controls its own header; ChatGPT’s native Share, close, and Edit site controls remain outside the site’s control.

## 6. Keyboard and interaction

- Keep topic controls as real buttons with an accessible name containing the topic.
- Preserve visible focus, modal Escape dismissal, source links, and return focus after closing a lesson.
- Do not include progress controls, a progress footer, or Next topic actions. Each topic is an independent information view.
- Retain the existing no-emoji rule and approved centralized close SVG.

## 7. Verification

- Check term count and source parity; every glossary term must appear exactly once.
- Check stable node IDs, valid edge endpoints, label clearance, graph bounds, and diagram fit widths.
- Check Fit at 320, 375, 390, 430, 768, and desktop widths. Check native pinch zoom separately.
- Review header behavior in the ChatGPT iOS Site viewer, native browser, pinch zoom, navigation opening, and page scrolling.
- Code checks establish source and geometry properties. They do not establish rendered browser or iOS correctness.
- Record screenshot observations separately from inferred causes. Do not claim a native embedded header bug is visually fixed without checking the resulting view.

## 8. Full-screen topic details on mobile

- Selecting any node opens a full-screen information modal at 700px viewport width and below, matching the reference’s reading-first layout.
- Remove the browser dialog’s default margins and maximum dimensions. Use the full available website viewport, an opaque white surface, and internal vertical scrolling.
- Integrate a compact close button in the modal’s top-right corner. Use the approved 18px close SVG inside a transparent 40px button. Do not reserve an entire controls row or add a gray tile. Respect safe-area insets and reserve focus clearance beside the topic metadata.
- Present the topic title, definition, example, practice, and source as readable content. Use 18px definition text with 1.7 line height.
- Keep Escape dismissal, modal focus containment, and return focus to the originating node. Desktop uses the full-height right-side panel defined below.
- Do not recreate the reference’s unrelated signup, AI, or account toolbar controls.

## 9. Minimal interface copy

- No Zoom/Fit toolbar or instructions referring to a zoom toggle. Keep automatic width fitting and native pinch zoom enabled.
- Do not show “Your typography-learning vocabulary page” or other repetitive source metadata in topic modals. Maintain provenance in project documentation and retain the useful further-reading link.

## 10. Larger-screen topic panel

- Above 700px, topic information opens immediately in a 600px-wide panel against the right viewport edge, filling the viewport height. Cap width at the available viewport.
- Use a lightly darkened, unblurred overlay: rgba(0,0,0,.25).
- Do not animate, slide, or fade either the panel or its overlay.
- Keep internal vertical scrolling, native modal focus containment, Escape/backdrop dismissal, and the existing compact close control.
- Preserve the approved full-screen mobile layout at 700px and below. Keep these desktop overrides scoped to the roadmap dialog.

## 11. Navigation and footer

- Roadmap is the last menu item on every Type Study page: last/rightmost in desktop navigation and bottommost in the mobile dropdown.
- Omit the repeated Type Study heading and vocabulary-count/source sentence from the roadmap footer. Retain the design rules link.

