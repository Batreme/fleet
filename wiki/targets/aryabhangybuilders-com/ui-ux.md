# UI & UX Architecture: aryabhangybuilders-com

## Overview & Design Identity
- **Target**: `aryabhangybuilders-com` (**Premium Builders In Kochi · Flats & Apartments · Arya Bhangy**)
- **Production URL**: [https://aryabhangybuilders.com/](https://aryabhangybuilders.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#222222` ink, `#b2b2be` accent)
- **Summary**: RERA-registered 2.5, 3 & 4 BHK apartments in Vyttila and Kumbalam, Kochi, from a family group building since 1969. Book a site visit.
- **Total Clean CSS Variables Extracted**: `171` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `CS Alpha`
- **Body Font Stack**: `Jost`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`
- **Section Heading (`H2`)**: rule `h2` (`font-size: 36px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `2.5em`, `100px`, `15px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `2.5em`, `100px`, `15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--e-social-icon-icon-color)` in `:root` |
| **Primary Typography Ink** | `#222222` | `var(--contrast)` in `:root` |
| **Elevated Surface / Card Substrate** | `#575760` | `var(--contrast-2)` in `:root` |
| **Interactive Accent / Highlight** | `#b2b2be` | `var(--contrast-3)` in `:root` |
| **Secondary / Muted Copy** | `#f0f0f0` | `var(--base)` in `:root` |
| **Structural Hairline Border** | `#f7f8f9` | `var(--base-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--flex-right` | `flex-start` | Design System Custom Token |
| `--justify-content` | `var(--flex-right,flex-end)` | Design System Custom Token |
| `--e-global-color-v4-white` | `var(--white)` | Canvas / Surface Token |
| `--e-global-color-v4-black` | `var(--black)` | Canvas / Surface Token |
| `--e-global-color-v4-cream-50` | `var(--cream-50)` | Brand / Palette Token |
| `--e-global-color-v4-cream-100` | `var(--cream-100)` | Brand / Palette Token |
| `--e-global-color-v4-cream-150` | `var(--cream-150)` | Brand / Palette Token |
| `--e-global-color-v4-cream-200` | `var(--cream-200)` | Brand / Palette Token |
| `--e-global-color-v4-beige-300` | `var(--beige-300)` | Brand / Palette Token |
| `--e-global-color-v4-beige-400` | `var(--beige-400)` | Brand / Palette Token |
| `--e-global-color-v4-taupe-450` | `var(--taupe-450)` | Brand / Palette Token |
| `--e-global-color-v4-taupe-500` | `var(--taupe-500)` | Brand / Palette Token |
| `--e-global-color-v4-charcoal` | `var(--charcoal)` | Brand / Palette Token |
| `--e-global-color-v4-charcoal-900` | `var(--charcoal-900)` | Brand / Palette Token |
| `--e-global-color-v4-charcoal-800` | `var(--charcoal-800)` | Brand / Palette Token |
| `--e-global-color-v4-charcoal-700` | `var(--charcoal-700)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `aryabhangybuilders-com`)**:
   - Landmark `<header class="elementor elementor-5070">` hosting `Premium Builders In Kochi · Flats & ` navigation (`Home · Residential · Commercial · Our Legacy · Testimonials`), DOM attributes (`data-elementor-device-mode="desktop"`, `data-opened="1"`, `data-elementor-type="header"`, `data-elementor-id="5070"`), and stylesheet rule `.e--ua-appleWebkit.rtl { --flex-right:flex-start }`.
2. **Hero Stage & Focal Lead (<article.post-2414> — `Premium Apartments in Kochi, by Ar`)**:
   - Landmark `<article class="post-2414 page">` presenting display lead `Premium Apartments in Kochi, by Arya Bhangy Builders` and copy excerpt *"sales@aryabhangybuilders.com"* over `#fff` canvas and `#222222` ink.
3. **Primary Showcase & Content Grid (<article.post-2414> — `Years in Business`)**:
   - Landmark `<article class="post-2414 page">` rendering section `Years in Business` with copy *"Enquire on WhatsApp."*, asset references (`1806948866520083`, `fbevents.js`, `gtm.js`, `embed`), and grid rule `widget-social-icons.e-grid-align-... { --justify-content:var(--flex-right,flex-end) }`.
4. **Interactive Detail & Feature Matrix (<article.post-2414> — `sq.ft. Developed in Kochi`)**:
   - Landmark `<article class="post-2414 page">` framing `sq.ft. Developed in Kochi` and `Transparent Transactions` (*"Est. 1969 · Kochi, Kerala"*) with `#575760` surface cards, `#b2b2be` accents, and `e-grid-align-right .elementor-gri... { margin-inline:calc(.5 * var(--grid-column-gap)) }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://aryabhangybuilders.com/`)**:
   - Landmark `<footer class="elementor elementor-6448">` anchoring `Premium Builders In Kochi · Flat` footer links (`Home · Residential · Commercial · Our Legacy · Testimonials`), copy *"F o r u s , r e a l e s t a t e i s m o r e t h a n c o n s "*, and `#f7f8f9` structural dividers.
