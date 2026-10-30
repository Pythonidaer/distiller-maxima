# Reading roadmap: content and navigation rules

This is the current working baseline for this app, intended to inform a future shared standard across typography-learning, color-learning, and related repositories. It does not claim those other repositories already implement every rule here.

## Purpose and provenance

Help a reader choose something worth learning, understand why it matters, and find a manageable starting point. Preserve the reader's freedom to explore a topic independently.

1. Collect the supplied bookmark titles, recover full titles and direct URLs against the existing public listing snapshot, and merge duplicates by URL. The current collection contains 206 resources.
2. Curate the collection into topics and two roadmaps. Classification began with titles; subsequent topic-guide commentary draws on written resource pages. A suggested sequence is editorial guidance, not a required prerequisite chain.
3. Synthesize related resources into original topic commentary. Explain connections and differences instead of paraphrasing every article in order. Keep direct source links beneath each discussion.
4. Explain what the reader might learn, why it might be useful, where to begin, and a small way to try it. Use concrete examples from the material where they clarify the idea.
5. State review limits accurately: video-course descriptions were read, but videos were not watched and tutorial code was not executed. Do not imply practical verification or exhaustive source coverage. Older setup instructions and product comparisons may need checking against current official documentation.
6. Revise classifications and presentation using reader feedback. Keep each resource on one roadmap and retain its source link.

## Language for directing future writing

- **Voice:** the consistent personality of the writing. Use a friendly, candid, human-to-human voice: knowledgeable without talking down to a learner.
- **Tone:** how that voice responds to the situation. Be encouraging when suggesting practice, precise when explaining a distinction, and matter-of-fact about limitations.
- **Plain language:** use familiar words, active verbs, and direct sentences. Introduce a technical term with its meaning when it helps the reader learn the vocabulary; do not remove useful terminology just to sound simple.
- **Curation:** choose and group material around the reader's interests and tasks. A collection is more useful when the reader can see why items belong together.
- **Synthesis:** connect ideas across sources in original prose. Preserve meaningful disagreements, caveats, and differences in scope.
- **Scaffolding:** offer a manageable first step, followed by a deeper resource or exercise. Avoid presenting every foundation as something that must be mastered before starting.
- **Information hierarchy:** use a page title, topic sections, subsections, and source lists so readers can scan before reading closely.
- **Progressive disclosure:** reveal secondary choices when requested. The mobile navigation starts closed, its submenus start closed, and the article outline reveals the current section's subsections.
- **Wayfinding:** make the reader's location and next choices visible through meaningful labels, active states, section links, and routes back to the roadmap.

### Writing rules

Lead with what the topic offers the reader. Explain why a resource is useful rather than calling it essential or comprehensive without evidence. Use connected paragraphs, usually moving from an approachable entry point to a deeper question or a small exercise. Prefer concrete tasks over motivational slogans. Address the reader as “you” naturally; avoid forced enthusiasm, guarantees, and generic encouragement. Distinguish an author's claim from established evidence. Link original resources and write original commentary rather than reproducing their content. Use lists when the information is genuinely parallel; use prose for explanation.

### Reusable writing brief

> Write a friendly reading guide for a curious learner. Curate the sources by topic and synthesize their connections in original prose. Explain what I could learn, why I might care, where to begin, and one small way to try it. Use plain language while introducing useful technical vocabulary. Keep the tone encouraging and candid, without hype or invented prerequisites. Link the sources and disclose what you did and did not review.

## Shared navigation baseline

Preserve the typography-learning-derived header and round mobile control when extending navigation. Match the host site's typography, spacing, focus treatment, and colors; do not redesign the control incidentally.

| Available viewport width | Main navigation | Article outline |
| --- | --- | --- |
| Up to 639px | Round hamburger; menu and submenus initially closed | Inline “Jump to a section” disclosure |
| 640–700px | Round hamburger; menu and submenus initially closed | Sticky side outline with a compact reading layout |
| 701–1179px | Roadmaps, Guides, About; first two have submenus | Sticky side outline, 180px column with 24px gap |
| 1180px and above | Same three main items | Wider right-side outline, 260px column, outer right gutter |

These are CSS viewport widths, not device detection. A tablet in split screen may use a different layout from the same tablet in full screen. Reassess the thresholds if labels, text scaling, or available space cause wrapping or crowding.

### Submenu behavior

- Use native `details` and `summary` disclosures; submenu destinations remain ordinary links.
- Start submenus closed on initial load, on mobile menu reopening, and after changing the responsive navigation mode. Readers choose what to reveal.
- On wider screens, open submenus on hover only for a fine pointer that supports hover. Also support click, tap, and keyboard activation; never require hover.
- Keep only one desktop submenu open. Close it when the pointer leaves unless focus remains inside. Escape closes the open menu; return focus to its trigger when appropriate. Outside interaction dismisses navigation.
- The mobile trigger exposes its expanded state and controls relationship. Hidden mobile navigation is inert. Keep visible focus indicators and touch targets of at least 44px in the shared navigation.
- Preserve an active destination indicator. Avoid raw data downloads as primary navigation items.

## Article-template side navigation

Use the side outline for long, sectioned reading templates, not automatically for every page or roadmap diagram. Build links from H2 sections and H3 subsections so the outline follows the article's actual structure.

- Each section and subsection has a stable, unique ID and a real fragment link.
- Clicking either level scrolls smoothly to that heading below the sticky header. Clicking the same link again still scrolls. Respect the user's Reduced Motion preference with instant movement.
- Keep URL fragments usable for deep links, browser history, and sharing. Initial fragment restoration does not animate a long journey through the article.
- Open the selected section’s submenu immediately and keep it stable during smooth scrolling. Resume reading-position tracking when scrolling finishes or the reader interrupts it. Do not cycle through intervening submenus.
- Track the actual scrolling container, which here is `siteShell`, rather than assuming the browser window scrolls.
- Mark the current heading with `aria-current="location"` and a visible treatment beyond color alone. Reveal only the active section's subsections; keep the current outline link visible within its scrollable area.
- Keep the outline sticky and independently scrollable. Expanding it must not shift the article. Do not count section highlighting as saved progress or completion tracking.
- Below the outline threshold, retain the inline contents disclosure. Test the layout with touch, keyboard, text zoom, and tablet split-screen sizes.

## Methodology footer

Include a lowercase “methodology” label and a short, readable account of collection, curation, synthesis, presentation, and review limits. Keep it distinct from article prose using a system monospace stack: `ui-monospace, SFMono-Regular, Menlo, Consolas, Liberation Mono, monospace`. This complements the app's Arial/Helvetica sans serif without a font download.

Use a readable size, generous line height, restrained contrast, and a link to these Markdown rules. Write lowercase text directly instead of applying CSS text-transform to unrelated content. The footer is supplementary context, not a prerequisite for using the page.

## Verification and future standardization

Check source links and heading targets, parent and child outline clicks, repeat clicks, smooth scrolling, Reduced Motion, sticky-header offsets, mobile closed defaults, touch submenu activation, keyboard focus, Escape, and outside dismissal. Confirm actual tablet split-screen behavior on a device; CSS breakpoints alone are not device testing.

Before rolling this baseline into other repositories, compare their existing menus and templates. Reuse behavior and accessibility contracts while preserving each site's content and visual identity. This document records the current implementation and intended checks, not a claim that every device scenario has been tested.

## Public-facing templates and icon baseline

Use the same article shell for About: persistent main navigation, heading hierarchy, responsive contents, and an automatically generated side outline. Write for an outside reader; exclude conversational references and collection-capture details. Explain the purpose of the collection and the process of synthesizing source material. Credit roadmap.sh as the educational visual inspiration without implying affiliation.

The lowercase methodology footer uses a native disclosure, initially closed. Keep rules and article collection links adjacent outside the disclosure. The public collection schema records stable ID, title, URL, roadmap, group, and topic; it is source mapping, not the guide commentary itself.

Use Google's Material Icons SVG paths consistently for forward arrows, expand controls, hamburger, and close actions. Icons inherit currentColor and are decorative when visible labels or button accessible names already convey the action. Preserve the icon license. Do not mix Unicode arrows or CSS-drawn chevrons into this system.

## Copy and hero update

Use direct, conversational wording. Avoid cinematic contrast slogans and semicolons in reader-facing prose. The home page uses the author’s first-person account. The hero title is “Know before you flow,” set in vivid pink Grime Slime Dripping. Its personal-use demo is included only in the private Sites QA preview, with the supplied font notice. Do not copy it to public production without checking the appropriate font license.

The hero uses a near-black background (#050505) and neon pink (#ff36c9). The same accent supplies logo and link underlines while text remains dark on light reading pages. Dripping title line height leaves room for the font’s lower details.

## Hero and authorship refinements

Use Chat-6.1 Sol Light as the credited tool in the author’s first-person methodology. About explains the learning and job-search context, the two matching roadmap/guide pairs, educational inspiration from roadmap.sh, and the documented repeatable workflow. Center the hero, use its width for a single-line desktop title, and allow wrapping below 1000px. Both hero actions share neon-pink hover backgrounds with black text. The logo underline appears only on hover or keyboard focus. Footer social links use MUI brand icons with accessible profile names.

## Motion and footer refinement

Stagger hero entrance using ease-out: title 550ms at 0ms, paragraph 500ms at 150ms, and CTA group 400ms at 300ms. Transition CTA background, text, and border colors over 180ms for hover and focus. Disable entrance and transition effects for Reduced Motion. Keep the methodology disclosure and social controls aligned on one footer row. Rules and collection links belong inside the disclosure. Use the display font only for the landing hero, with standard headings for About. Guide navigation labels must not assume the visitor came from a roadmap.

## Shared design baseline and hero navigation

Use design-system.css as the shared semantic-token and role layer, loaded after component styles. Keep the existing font families. Use 13/14px supporting text, 16px UI text, 18px reading text, 20px leads, 24px subsections, 26–32px sections, and 32–48px page titles. Body line height is 1.75. Spacing follows 4, 8, 12, 16, 24, 32, 48, 64px. Preserve roadmap canvas geometry and 16px node labels. Pink covers interaction accents, blue covers roadmap relationships, and neutrals cover reading surfaces and text. Transparent navigation is a dark-hero template variant only. Switch to the solid header as the hero’s 60% point passes beneath the sticky header, retain solid menu surfaces, and respect Reduced Motion for the transition.

## Final header and heading consistency

All content-page H1s share one complete role: Arial stack, 600 weight, clamp(32px,4vw,48px), 1.12 line height, and -1px tracking. The experimental landing hero is separate. Mobile top-level About uses the same 600 weight as Roadmaps and Guides. The dark-hero header uses a 14px backdrop blur and subtle black tint until it changes to the light header. Remove roadmap-introduction guide links because the main navigation already supplies those destinations.

## Soft hero header and overview copy

Use a 5px backdrop blur on a dark translucent pseudo-element, feathered to transparent over the header’s lower edge. Keep the navigation labels outside the blur layer. This replaces the uniform 14px blur to reduce pink haze. The hero paragraph connects the collection overview with choosing a topic before focused reading.
