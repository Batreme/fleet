---
title: "UI & UX Architecture: www-paragonproductions-co"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-paragonproductions-co

## Overview & Design Identity
- **Target**: `www-paragonproductions-co` (**PARAGON · Creative Production Studio**)
- **Production URL**: [https://www.paragonproductions.co/](https://www.paragonproductions.co/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#100f0f` canvas, `#f8f8f8` ink, `#ff0000` accent)
- **Summary**: PARAGON is a production partner driven by pursuit. We team up with brands and agencies to craft commercials, branded films, and campaigns...
- **Total Clean CSS Variables Extracted**: `118` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Review Condensed`
- **Body Font Stack**: `Roobert`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 35.2px`, `font-weight: 500`); rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 32px`, `line-height: 35.2px`, `font-weight: 500`); rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.96px`, `font-weight: 400`); rule `p` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.96px`, `font-weight: 400`); CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--max-width--small: 80rem`, `--max-width--extra-small: 50rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#100f0f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f8f8f8` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.nav_mobile_link.w--current { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--_color---swatch--red`)** | `#ff5b4b` | `var(--_color---swatch--red)` in `:root` |

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
   - Landmark `<nav class="nav_wrap">` (`1440x114px`) hosting `PARAGON · Creative Production Studio` navigation (`Work · Who We Are · News · Contact Us · Vimeo`), DOM attributes (`data-wf-domain="www.paragonproduction..."`, `data-wf-page="68be24b22b086720602bcd26"`, `data-wf-site="68be24b22b086720602bcd38"`, `data-wf-intellimize-customer-id="117787750"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.home-hero_wrap> — `ALWAYS IN PURSUIT`)**:
   - Landmark `<section class="home-hero_wrap">` presenting display lead `ALWAYS IN PURSUIT` and copy excerpt *"To us, that’s simple: grow every day, put people first, and never"* over `#100f0f` canvas and `#f8f8f8` ink.
3. **Primary Showcase & Content Grid (<section.home-services_wrap> — `Always In PURSUIT`)**:
   - Landmark `<section class="home-services_wrap">` rendering section `Always In PURSUIT` with copy *"Creative Creative Creative Creative Creative Creative Creative Cr"*, asset references (`cdn.prod.website-files.com`, `paragonproductions.webflow.shared...`, `paragonproductions.webflow.68be24...`, `gtm.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.featured-work_wrap> — `PARAGON is a production partner dr`)**:
   - Landmark `<section class="featured-work_wrap">` framing `PARAGON is a production partner driven by pursuit.` and `BUILT FOR THE CHASE` (*"Ideas worth chasing start here. We ground them in research, sharp"*) with `#222222` surface cards, `#ff0000` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.paragonproductions.co/`)**:
   - Landmark `<footer class="footer_wrap">` anchoring `PARAGON · Creative Production St` footer links (`Work · Who We Are · News · Contact Us · Vimeo`), copy *"Campaign Development"*, and `#3898ec` structural dividers.
