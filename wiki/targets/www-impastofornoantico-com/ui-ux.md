---
title: "UI & UX Architecture: www-impastofornoantico-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-impastofornoantico-com

## Overview & Design Identity
- **Target**: `www-impastofornoantico-com` (**Handcrafted Bread with Soul - Impasto**)
- **Production URL**: [https://www.impastofornoantico.com/](https://www.impastofornoantico.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#efefe7` canvas, `#312426` ink, `#0082f3` accent)
- **Summary**: Discover Impasto’s soulful, handcrafted bread - Rye, Focaccia, Sourdough. Experience the rhythm of baking with care. Order or contact us...
- **Total Clean CSS Variables Extracted**: `236` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `aaux-next`
- **Body Font Stack**: `ff-scala`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--h1--margin-bottom: var(--space--3)`, `--h1--font-family: var(--all-headings--heading-font-family)`, `--h1--font-size: var(--size--5rem)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 168px`, `line-height: 168px`, `font-weight: 400`, `letter-spacing: -5.03999px`); CSS variables `--h2--margin-bottom: var(--space--3)`, `--h2--font-family: var(--all-headings--heading-font-family)`, `--h2--font-size: var(--size--4rem)`
- **Body Copy**: live computed `body` (`font-size: 19.2px`, `line-height: 28.8px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 19.2px`, `line-height: 28.8px`, `font-weight: 400`); CSS variables `--text-main--letter-spacing: var(--letter-spacing--0em)`, `--h1--letter-spacing: var(--all-headings--heading-letter-spacing)`, `--h2--letter-spacing: var(--all-headings--heading-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#efefe7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#312426` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#d9cec3` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--theme--background` | `var(--swatch--light)` | Canvas / Surface Token |
| `--text-main--font-family` | `var(--font--second-family)` | Typography Ink Token |
| `--theme--text` | `var(--swatch--dark)` | Typography Ink Token |
| `--text-main--font-size` | `1.2rem` | Typography Ink Token |
| `--text-main--line-height` | `var(--line-height--1-5)` | Typography Ink Token |
| `--text-main--font-weight` | `var(--font--primary-regular)` | Typography Ink Token |
| `--text-main--letter-spacing` | `var(--letter-spacing--0em)` | Typography Ink Token |
| `--h1--margin-bottom` | `var(--space--3)` | Typography / Scale Token |
| `--h1--font-family` | `var(--all-headings--heading-font-family)` | Typography / Scale Token |
| `--h1--font-size` | `var(--size--5rem)` | Typography / Scale Token |
| `--h1--line-height` | `var(--all-headings--heading-line-height)` | Typography / Scale Token |
| `--h1--font-weight` | `var(--font--primary-medium)` | Typography / Scale Token |
| `--h1--letter-spacing` | `var(--all-headings--heading-letter-spacing)` | Typography / Scale Token |
| `--h2--margin-bottom` | `var(--space--3)` | Typography / Scale Token |
| `--h2--font-family` | `var(--all-headings--heading-font-family)` | Typography / Scale Token |
| `--h2--font-size` | `var(--size--4rem)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navigation> — `www-impastofornoantico-com`)**:
   - Landmark `<nav class="navigation">` (`1440x900px`) hosting `Handcrafted Bread with Soul - Impast` navigation (`Home · About · Products · Stockists · Wholesale`), DOM attributes (`data-wf-domain="www.impastofornoantic..."`, `data-wf-page="6774ded4742b832f88f9825e"`, `data-wf-site="6774ded4742b832f88f98269"`, `data-navigation-status="not-active"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.scaling-element-header> — `FOCACCIA`)**:
   - Landmark `<section class="scaling-element-header">` presenting display lead `FOCACCIA` and copy excerpt *"For generations, the Villani family has followed a time-honored m"* over `#efefe7` canvas and `#312426` ink.
3. **Primary Showcase & Content Grid (<section.scaling-element-video> — `CIABATTA`)**:
   - Landmark `<section class="scaling-element-video">` rendering section `CIABATTA` with copy *"It’s a method rooted in patience, respect for ingredients, and a "*, asset references (`cdn.prod.website-files.com`, `impasto-tag.webflow.shared.02cb07...`, `recaptcha__en.js`, `gvw6vxl.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.scaling-element-video:nth(2)> — `SOURDOUGH`)**:
   - Landmark `<section class="scaling-element-video">` framing `SOURDOUGH` and `Our ongoing pursuit of quality ensures that our ` (*"Our ongoing pursuit of quality ensures that our bread evolves wit"*) with `#ffff00` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://www.impastofornoantico.com/`)**:
   - Landmark `<footer class="footer_component">` anchoring `Handcrafted Bread with Soul - Im` footer links (`Home · About · Products · Stockists · Wholesale`), copy *"Today, a new approach is taking shape — one that still value"*, and `#e2e2e2` structural dividers.
