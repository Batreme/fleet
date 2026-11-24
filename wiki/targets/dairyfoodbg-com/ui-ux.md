---
title: "UI & UX Architecture: dairyfoodbg-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: dairyfoodbg-com

## Overview & Design Identity
- **Target**: `dairyfoodbg-com` (**Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer**)
- **Production URL**: [https://dairyfoodbg.com/](https://dairyfoodbg.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)
- **Summary**: Private-label manufacturer of UHT milk, creams and protein drinks. Four aseptic filling lines, 28 export markets, co-development from rec...
- **Total Clean CSS Variables Extracted**: `167` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Verdana`
- **Body Font Stack**: `Albertsans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`); CSS variables `--_type---family--display: Bricolagegrotesquesemicondensed,Verdana,sans-serif`, `--_type---leading--display: 1`, `--_type---scale--display: 6em`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 44px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`); CSS variables `--_type---family--body: Albertsans,Verdana,sans-serif`, `--_type---leading--body: 1.5`, `--_type---tracking--body: 0em`; rule `body` (`font-size: var(--size-font)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13px`, `line-height: 19.5px`, `font-weight: 400`); CSS variables `--_component---sizing--container-small: 64em`, `--_component---sizing--container-x-small: 48em`, `--cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0d2759` | live computed `nav` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d7ecf6` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.eu-bar__link { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#6b6b6b` | `var(--cc-color-muted)` in `:root` |
| **Structural Hairline Border** | `#e0e5f0` | `var(--_colors---semantic--border)` in `:root` (`21489524`) |
| **Variable Token (`--_colors---brand--green-hover`)** | `#2e7031` | `var(--_colors---brand--green-hover)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_type---family--body` | `Albertsans,Verdana,sans-serif` | Typography / Scale Token |
| `--_colors---semantic--content-primary` | `var(--_colors---neutral--700)` | Brand / Palette Token |
| `--_type---scale--base` | `1em` | Typography / Scale Token |
| `--_type---weight--regular` | `400` | Typography / Scale Token |
| `--_padding---section--lg` | `7.5em` | Layout / Spatial Grid Token |
| `--_padding---container--page` | `1.25em` | Layout / Spatial Grid Token |
| `--_padding---section--md` | `5em` | Layout / Spatial Grid Token |
| `--_colors---semantic--bg` | `var(--_colors---brand--cloud)` | Canvas / Surface Token |
| `--_component---sizing--container-small` | `64em` | Layout / Spatial Grid Token |
| `--_space---2xl` | `3em` | Layout / Spatial Grid Token |
| `--_space---sm` | `.5em` | Layout / Spatial Grid Token |
| `--_colors---brand--green-hover` | `#2e7031` | Brand / Palette Token |
| `--_type---scale--xs` | `.75em` | Typography / Scale Token |
| `--_type---weight--semibold` | `600` | Typography / Scale Token |
| `--_type---tracking--eyebrow` | `.2em` | Typography / Scale Token |
| `--_type---family--display` | `Bricolagegrotesquesemicondensed,Verdana,sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar> — `dairyfoodbg-com`)**:
   - Landmark `<header class="navbar">` (`1440x57px`) hosting `Dairy Food Bulgaria — Private-Label ` navigation (`Home · About · Products · Packaging · Catalog`), DOM attributes (`data-wf-domain="dairyfoodbg.com"`, `data-wf-page="6a450776d63ee937af4d29d7"`, `data-wf-site="6a450773d63ee937af4d28ea"`, `data-cc="analytics"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Elevate your brand`)**:
   - Landmark `<section class="hero">` presenting display lead `Elevate your brand` and copy excerpt *"From product development and packaging to large-scale manufacturi"* over `#ffffff` canvas and `#0d2759` ink.
3. **Primary Showcase & Content Grid (<section.about> — `Traditional craftsmanship with mod`)**:
   - Landmark `<section class="about">` rendering section `Traditional craftsmanship with modern UHT technol...` with copy *"Leading producer of private-label UHT dairy in Bulgaria. Leading "*, asset references (`cdn.prod.website-files.com`, `dairy-food.shared.ce91a50f0.min.css`, `dairy-food.6a450776d63ee937af4d29...`, `6abf58390100a7826e7f0b59_favicon-...`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.home-products> — `Customizable Products`)**:
   - Landmark `<section class="home-products">` framing `Customizable Products` and `Flexible Packaging` (*"Leading producer of private-label UHT dairy in Bulgaria."*) with `#d7ecf6` surface cards, `#0000ff` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://dairyfoodbg.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Dairy Food Bulgaria — Private-La` footer links (`Home · About · Products · Packaging · Catalog`), copy *"Start Your Project"*, and `#e0e5f0` structural dividers.
