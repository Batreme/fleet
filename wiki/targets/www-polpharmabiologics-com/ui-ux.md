# UI & UX Architecture: www-polpharmabiologics-com

## Overview & Design Identity
- **Target**: `www-polpharmabiologics-com` (**Polpharma Biologics · Global Biosimilar Developer & Manufacturer**)
- **Production URL**: [https://www.polpharmabiologics.com/](https://www.polpharmabiologics.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#0000` / `#333`)
- **Summary**: Polpharma Biologics is a global biosimilar developer and manufacturer, taking biosimilars from cell to sell with an international track r...
- **Total Clean CSS Variables Extracted**: `63` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Seasonsans`
- **Body Font Stack**: `Concrettem`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Body Copy**: CSS variables `--body: Seasonsans,Arial,sans-serif`, `--_rich---rich-body--body-font-family: var(--body)`, `--_rich---rich-body--body-font-color: #16151780`
- **Metadata & Labels**: CSS variables `--_rich---rich-body--body-letter-spacing: var(--_🟢-typography---body-large--letter-spacing)`, `--caption-family: Seasonsans,Arial,sans-serif`, `--_rich---rich-heading--heading-letter-spacing: var(--_🟢-typography---title-small--letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `a { background-color: #0000 }` |
| **Primary Typography Ink** | `#000` | `mark { color: #000 }` |
| **Elevated Surface / Card Substrate** | `#ff0` | `mark { background: #ff0 }` |
| **Interactive Accent / Highlight** | `#333` | `body { color: #333 }` |
| **Secondary / Muted Copy** | `#fff` | `body { background-color: #fff }` |
| **Structural Hairline Border** | `#3898ec` | `.w-button { background-color: #3898ec }` |
| **Variable Token (`--_rich---rich-body--body-font-color`)** | `#16151780` | `var(--_rich---rich-body--body-font-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav_component> — `www-polpharmabiologics-com`)**:
   - Landmark `<header class="nav_component">` hosting `Polpharma Biologics · Global Biosimi` navigation (`Company · About us · What we do · Pipeline · Partnerships`), DOM attributes (`data-wf-domain="www.polpharmabiologic..."`, `data-wf-page="6a55f3be4b824306906ca2f0"`, `data-wf-site="6a55f3bb4b824306906ca274"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Biosimilarity isn’t discovered. It`)**:
   - Landmark `<section class="section is-home-hero">` presenting display lead `Biosimilarity isn’t discovered. It’s engineered.` and copy excerpt *"Precision in every molecule."* over `#0000` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.section> — `A pure-play biosimilar company wit`)**:
   - Landmark `<section class="section is-home-how-it-works">` rendering section `A pure-play biosimilar company with an internatio...` with copy *"Built to accelerate biosimilars development – cell to sell."*, asset references (`cdn.prod.website-files.com`, `polpharmaxwidehue-staging.webflow...`, `insight.min.js`, `6aaa7fea366a958e0f892178_webclip.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `We produce impact-driven biosimila`)**:
   - Landmark `<section class="section is-home-we-know">` framing `We produce impact-driven biosimilars. From concep...` and `We know` (*"Approved biosimilars"*) with `#ff0` surface cards, `#333` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.section> — `https://www.polpharmabiologics.com/`)**:
   - Landmark `<footer class="section is-dark">` anchoring `Polpharma Biologics · Global Bio` footer links (`Company · About us · What we do · Pipeline · Partnerships`), copy *"Years biologics expertise"*, and `#3898ec` structural dividers.
