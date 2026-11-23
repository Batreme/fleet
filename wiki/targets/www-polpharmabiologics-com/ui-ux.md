---
title: "UI & UX Architecture: www-polpharmabiologics-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-polpharmabiologics-com

## Overview & Design Identity
- **Target**: `www-polpharmabiologics-com` (**Polpharma Biologics · Global Biosimilar Developer & Manufacturer**)
- **Production URL**: [https://www.polpharmabiologics.com/](https://www.polpharmabiologics.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0082f3`)
- **Summary**: Polpharma Biologics is a global biosimilar developer and manufacturer, taking biosimilars from cell to sell with an international track r...
- **Total Clean CSS Variables Extracted**: `45` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Concrettem`
- **Body Font Stack**: `Seasonsans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 80px`, `font-weight: 400`, `letter-spacing: -3.2px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 64.8px`, `font-weight: 400`, `letter-spacing: -2.4px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--body: Seasonsans,Arial,sans-serif`, `--_rich---rich-body--body-font-family: var(--body)`, `--_rich---rich-body--body-size: var(--_🟢-typography---body-large--font-size)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_rich---rich-body--body-letter-spacing: var(--_🟢-typography---body-large--letter-spacing)`, `--caption-family: Seasonsans,Arial,sans-serif`, `--_rich---rich-heading--heading-letter-spacing: var(--_🟢-typography---title-small--letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#005453` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#e6efef` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--_rich---rich-body--body-font-color`)** | `#161517` | `var(--_rich---rich-body--body-font-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--body` | `Seasonsans,Arial,sans-serif` | Design System Custom Token |
| `--heading-family` | `Concrettem,Arial,sans-serif` | Typography Ink Token |
| `--title-family` | `Seasonsans,Arial,sans-serif` | Typography / Scale Token |
| `--_rich---rich-body--body-font-family` | `var(--body)` | Typography / Scale Token |
| `--_rich---rich-body--body-font-color` | `#16151780` | Brand / Palette Token |
| `--_rich---rich-body--body-size` | `var(--_🟢-typography---body-large--font-size)` | Layout / Spatial Grid Token |
| `--_rich---rich-body--body-line-height` | `var(--_🟢-typography---body-large--line-height)` | Typography / Scale Token |
| `--_rich---rich-body--body-weight` | `var(--_🟢-typography---body-large--font-weight)` | Design System Custom Token |
| `--_rich---rich-body--body-letter-spacing` | `var(--_🟢-typography---body-large--letter-spacing)` | Typography / Scale Token |
| `--_rich---rich-spacing--body-margin-bottom` | `1.25rem` | Layout / Spatial Grid Token |
| `--_rich---rich-spacing--quote-margin-vertical` | `2rem` | Layout / Spatial Grid Token |
| `--_rich---rich-quote--quote-border-color` | `var(--_🟢-colors---primary--red)` | Brand / Palette Token |
| `--_rich---rich-quote--quote-font-color` | `var(--_🟢-colors---primary--deep-green)` | Brand / Palette Token |
| `--_sizing---padding-section--zero` | `0rem` | Layout / Spatial Grid Token |
| `--_sizing---padding-section--large-160` | `10rem` | Layout / Spatial Grid Token |
| `--caption-family` | `Seasonsans,Arial,sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav_component> — `www-polpharmabiologics-com`)**:
   - Landmark `<header class="nav_component">` (`1425x90px`) hosting `Polpharma Biologics · Global Biosimi` navigation (`Company · About us · What we do · Pipeline · Partnerships`), DOM attributes (`data-wf-domain="www.polpharmabiologic..."`, `data-wf-page="6a55f3be4b824306906ca2f0"`, `data-wf-site="6a55f3bb4b824306906ca274"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Biosimilarity isn’t discovered. It`)**:
   - Landmark `<section class="section is-home-hero">` presenting display lead `Biosimilarity isn’t discovered. It’s engineered.` and copy excerpt *"Precision in every molecule."* over `#ffffff` canvas and `#005453` ink.
3. **Primary Showcase & Content Grid (<section.is-home-how-it-works> — `A pure-play biosimilar company wit`)**:
   - Landmark `<section class="section is-home-how-it-works">` rendering section `A pure-play biosimilar company with an internatio...` with copy *"Built to accelerate biosimilars development – cell to sell."*, asset references (`cdn.prod.website-files.com`, `polpharmaxwidehue-staging.webflow...`, `insight.min.js`, `6aaa7fea366a958e0f892178_webclip.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.is-home-we-know> — `We produce impact-driven biosimila`)**:
   - Landmark `<section class="section is-home-we-know">` framing `We produce impact-driven biosimilars. From concep...` and `Swiss engineered, supplied globally` (*"Approved biosimilars"*) with `#ffff00` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.section> — `https://www.polpharmabiologics.com/`)**:
   - Landmark `<footer class="section is-dark">` anchoring `Polpharma Biologics · Global Bio` footer links (`Company · About us · What we do · Pipeline · Partnerships`), copy *"Years biologics expertise"*, and `#e2e2e2` structural dividers.
