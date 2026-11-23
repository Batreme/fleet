---
title: "UI & UX Architecture: moderncraftaz-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: moderncraftaz-com

## Overview & Design Identity
- **Target**: `moderncraftaz-com` (**Select A Location · AllHaus**)
- **Production URL**: [https://moderncraftaz.com/](https://moderncraftaz.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#404040` ink, `#0074db` accent)
- **Summary**: Crafting exceptional residences with unmatched service in Arizona, Montana, and beyond.
- **Total Clean CSS Variables Extracted**: `32` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `helveticaneue`
- **Body Font Stack**: `helveticaneue`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 86.4px`, `font-weight: 200`, `letter-spacing: 1px`)
- **Section Heading (`H2`)**: observed font-size ladder: `72px`, `16px`, `1em`, `80%`, `75%`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `body` (`font-size: 16px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#404040` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0074db` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0074db` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#00a0d2` | `.wpcf7 form .wpcf7-response-output { border: #00a0d2 }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--wp--style--global--content-size` | `650px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1200px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `1.5rem` | Layout / Spatial Grid Token |
| `--sk-size` | `40px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.yoast-schema-graph> — `moderncraftaz-com`)**:
   - Landmark `<header class="yoast-schema-graph">` (`1440px`) hosting `Select A Location · AllHaus` navigation (`AZ AZ AZ · CO CO CO · MT MT MT`), DOM attributes (`data-again="always_show"`, `data-wait="load"`, `data-wait-sec="2"`, `data-nosnippet`), and stylesheet rule `input { overflow: visible; }`.
2. **Hero Stage & Focal Lead (<section.ct-section> — `UNPARALLELLED SERVICE FOR EXCEPTIO`)**:
   - Landmark `<section class="ct-section">` presenting display lead `UNPARALLELLED SERVICE FOR EXCEPTIONAL HOMES` and copy excerpt *"Code Snippet ma-customfonts 3.4.2"* over `#ffffff` canvas and `#404040` ink.
3. **Primary Showcase & Content Grid (<section.ct-section:nth(2)> — `Unparallelled Service For Exceptio`)**:
   - Landmark `<section class="ct-section">` rendering section `Unparallelled Service For Exceptional Homes` with copy *"UNPARALLELLED SERVICE FOR EXCEPTIONAL HOMES"*, asset references (`recaptcha__en.js`, `cdn.jsdelivr.net`, `embed`, `ma-customfonts.css`), and grid rule `video { display: inline-block; }`.
4. **Interactive Detail & Feature Matrix (<section.ct-section:nth(3)> — `moderncraftaz-com Interactive Matr`)**:
   - Landmark `<section class="ct-section">` framing `moderncraftaz-com Interactive Matrix` and `moderncraftaz-com Archive & Directory` (*"Unparallelled Service For Exceptional Homes"*) with `#dddddd` surface cards, `#0074db` accents, and `sup { vertical-align: baseline; }`.
5. **Colophon & Global Directory Footer (<footer.page> — `https://moderncraftaz.com/`)**:
   - Landmark `<footer class="page">` anchoring `Select A Location · AllHaus` footer links (`AZ AZ AZ · CO CO CO · MT MT MT`), copy *"moderncraftaz-com Interactive Matrix"*, and `#00a0d2` structural dividers.
