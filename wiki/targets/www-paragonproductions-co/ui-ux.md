# UI & UX Architecture: www-paragonproductions-co

## Overview & Design Identity
- **Target**: `www-paragonproductions-co` (**PARAGON · Creative Production Studio**)
- **Production URL**: [https://www.paragonproductions.co/](https://www.paragonproductions.co/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ff5b4b` canvas, `#f8f8f8` ink, `#ffcdd2` accent)
- **Summary**: PARAGON is a production partner driven by pursuit. We team up with brands and agencies to craft commercials, branded films, and campaigns...
- **Total Clean CSS Variables Extracted**: `118` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Review Condensed`
- **Body Font Stack**: `Proxima Nova`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: rule `p` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **Metadata & Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--max-width--small: 80rem`, `--max-width--extra-small: 50rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ff5b4b` | `var(--_color---swatch--red)` in `:root` |
| **Primary Typography Ink** | `#100f0f` | `var(--_color---swatch--black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6d6c6c` | `var(--_color---swatch--grey-500)` in `:root` |
| **Interactive Accent / Highlight** | `#ffcdd2` | `var(--_color---system--error-light)` in `:root` |
| **Secondary / Muted Copy** | `#d32f2f` | `var(--_color---system--error)` in `:root` |
| **Structural Hairline Border** | `#f8f8f8` | `var(--_color---swatch--white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background--primary` | `var(--_color---swatch--white)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font-family--tertiary)` | Typography Ink Token |
| `--_theme---text--primary` | `var(--_color---swatch--black)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--131-5)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font-weight--normal)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--0em)` | Typography Ink Token |
| `--_typography---font-family--secondary` | `"Review Condensed",Arial,sans-serif` | Brand / Palette Token |
| `--_typography---font-weight--medium` | `500` | Typography / Scale Token |
| `--_text-style---margin-top` | `var(--_spacing---space--4)` | Typography Ink Token |
| `--_text-style---margin-bottom` | `var(--_spacing---space--5)` | Typography Ink Token |
| `--_color---swatch--red` | `#ff5b4b` | Brand / Palette Token |
| `--_typography---font-family--primary` | `"Proxima Nova",Arial,sans-serif` | Brand / Palette Token |
| `--_theme---text--secondary` | `var(--_color---swatch--grey-500)` | Typography Ink Token |
| `--_typography---font-weight--thin` | `100` | Typography / Scale Token |
| `--_typography---font-weight--extra-light` | `200` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav_wrap> — `www-paragonproductions-co`)**:
   - Landmark `<nav class="nav_wrap">` hosting `PARAGON · Creative Production Studio` navigation (`Skip to main content · Work · Who We Are · News · Contact Us`), DOM attributes (`data-wf-domain="www.paragonproduction..."`, `data-wf-page="68be24b22b086720602bcd26"`, `data-wf-site="68be24b22b086720602bcd38"`, `data-wf-intellimize-customer-id="117787750"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.home-hero_wrap> — `Always In PURSUIT`)**:
   - Landmark `<section class="home-hero_wrap">` presenting display lead `Always In PURSUIT` and copy excerpt *"Skip to main content"* over `#ff5b4b` canvas and `#f8f8f8` ink.
3. **Primary Showcase & Content Grid (<section.home-services_wrap> — `What We Do`)**:
   - Landmark `<section class="home-services_wrap">` rendering section `What We Do` with copy *"Instagram Instagram Instagram"*, asset references (`cdn.prod.website-files.com`, `paragonproductions.webflow.shared...`, `paragonproductions.webflow.68be24...`, `gtm.js`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.featured-work_wrap> — `PARAGON is a production partner dr`)**:
   - Landmark `<section class="featured-work_wrap">` framing `PARAGON is a production partner driven by pursuit.` and `BUILT FOR THE CHASE` (*"LinkedIn LinkedIn LinkedIn"*) with `#6d6c6c` surface cards, `#ffcdd2` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.paragonproductions.co/`)**:
   - Landmark `<footer class="footer_wrap">` anchoring `PARAGON · Creative Production St` footer links (`Skip to main content · Work · Who We Are · News · Contact Us`), copy *"ALWAYS IN PURSUIT //"*, and `#f8f8f8` structural dividers.
