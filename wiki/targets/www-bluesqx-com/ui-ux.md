---
title: "UI & UX Architecture: www-bluesqx-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-bluesqx-com

## Overview & Design Identity
- **Target**: `www-bluesqx-com` (**Blue Square X – Premium LED Displays & Immersive Digital Experiences**)
- **Production URL**: [https://www.bluesqx.com/](https://www.bluesqx.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)
- **Summary**: We design and deliver high-end LED display systems and immersive digital experiences for luxury brands, retail spaces, and iconic environ...
- **Total Clean CSS Variables Extracted**: `67` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Beausite Classic`
- **Body Font Stack**: `Beausite Classic`
- **Monospace / Technical Font Stack**: `Fira Sans`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 56px`, `font-weight: 500`, `letter-spacing: -2px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 56px`, `line-height: 56px`, `font-weight: 500`, `letter-spacing: -2px`); rule `h2` (`letter-spacing: -.125rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--_typography---font-styles--body: "Beausite Classic",Arial,sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--_ui-styles---radius--xxsmall: .125rem`, `--_ui-styles---radius--small: .25rem`; rule `.label` (`font-size: 0.75rem`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1b1e24` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0000ff` | `.button.is-alternate.is-form:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#fd7070` | `.news-category { color: #fd7070 }` |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--_primitives---colors--neutral`)** | `#7d8086` | `var(--_primitives---colors--neutral)` in `:root` |
| **Variable Token (`--_primitives---opacity--transparent`)** | `#fff0` | `var(--_primitives---opacity--transparent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_primitives---colors--white` | `#fff` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `"Beausite Classic",Arial,sans-serif` | Typography / Scale Token |
| `--_primitives---colors--neutral-darkest` | `#1b1e24` | Canvas / Surface Token |
| `--_typography---font-styles--heading` | `"Beausite Classic",Arial,sans-serif` | Typography Ink Token |
| `--outline-button--text` | `var(--_primitives---colors--neutral-darkest)` | Typography Ink Token |
| `--header--link-color-hover` | `var(--_primitives---colors--blue-accent)` | Typography Ink Token |
| `--_primitives---colors--neutral` | `#7d8086` | Brand / Palette Token |
| `--_primitives---colors--neutral-darker` | `#1b1e24` | Canvas / Surface Token |
| `--_ui-styles---radius--xxsmall` | `.125rem` | Elevation / Border Token |
| `--button--border` | `var(--_primitives---colors--neutral-darkest)` | Elevation / Border Token |
| `--button--background` | `var(--_primitives---colors--neutral-darkest)` | Canvas / Surface Token |
| `--button--text` | `var(--_primitives---colors--white)` | Typography Ink Token |
| `--_primitives---opacity--transparent` | `#fff0` | Color / Atmospheric Token |
| `--_primitives---opacity--neutral-darkest-15` | `#1b1e2426` | Canvas / Surface Token |
| `--outline-button--border` | `var(--_primitives---opacity--neutral-darkest-15)` | Elevation / Border Token |
| `--outline-button--background` | `var(--_primitives---opacity--transparent)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navbar_menu> — `www-bluesqx-com`)**:
   - Landmark `<nav class="navbar_menu w-nav-menu">` (`636x35px`) hosting `Blue Square X – Premium LED Displays` navigation (`Art & Museums · Corporate · Hospitality · Luxury Living · Luxury Real Estate`), DOM attributes (`data-wf-domain="www.bluesqx.com"`, `data-wf-page="69272aa8c1734eeb3d97ece3"`, `data-wf-site="69272aa5c1734eeb3d97e49c"`, `data-lenis-prevent="true"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.banner_component> — `Immersive Experiences. Lasting Imp`)**:
   - Landmark `<section class="banner_component dark">` presenting display lead `Immersive Experiences. Lasting Impressions.` and copy excerpt *"Stay Inspired! Subscribe for the latest Blue Square X updates."* over `#ffffff` canvas and `#1b1e24` ink.
3. **Primary Showcase & Content Grid (<section.section_header> — `Build Your Immersive Experiences`)**:
   - Landmark `<section class="section_header dark">` rendering section `Build Your Immersive Experiences` with copy *"Trusted by the industry leaders:"*, asset references (`cdn.prod.website-files.com`, `bluesquarex.webflow.shared.3fa960...`, `data.js`, `recaptcha__en.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_services-cards> — `Discover LED Indoor and Outdoor Pr`)**:
   - Landmark `<section class="section_services-cards base">` framing `Discover LED Indoor and Outdoor Products` and `Vision + Experience` (*"We design, build, create, and support environments that captivate"*) with `#ffff00` surface cards, `#0000ff` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.bluesqx.com/`)**:
   - Landmark `<footer class="footer dark">` anchoring `Blue Square X – Premium LED Disp` footer links (`Art & Museums · Corporate · Hospitality · Luxury Living · Luxury Real Estate`), copy *"Shaping bold ideas into immersive plans that seamlessly unit"*, and `#e2e2e2` structural dividers.
