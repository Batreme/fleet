---
title: "UI & UX Architecture: thetiebreak-merci-michel-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: thetiebreak-merci-michel-com

## Overview & Design Identity
- **Target**: `thetiebreak-merci-michel-com` (**The Tie-break!**)
- **Production URL**: [https://thetiebreak.merci-michel.com/](https://thetiebreak.merci-michel.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#fff302`)
- **Summary**: Play the game and discover the latest New Balance X Miu Miu collection with Coco Gauff.
- **Total Clean CSS Variables Extracted**: `16` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument`
- **Body Font Stack**: `WorkSans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 112.5px`, `line-height: 112.5px`, `font-weight: 400`)
- **Section Heading (`H2`)**: observed font-size ladder: `112.5px`, `7.5px`, `12px`, `1.4em`, `2.4em`
- **Body Copy**: live computed `body` (`font-size: 7.5px`, `line-height: 8.25px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 7.5px`, `line-height: 8.25px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | `::-moz-selection { color: #000000 }` |
| **Elevated Surface / Card Substrate** | `#05152d` | `#preloader .preloader-background { background: #05152d }` |
| **Interactive Accent / Highlight** | `#fff302` | `var(--ui-color-primary-hover)` in `:root` |
| **Secondary / Muted Copy** | `#000000` | secondary opacity step of `::-moz-selection { color: #000000 }` |
| **Structural Hairline Border** | `#000000` | hairline divider derived from secondary opacity step of `::-moz-selection { color: #000000 }` |
| **Variable Token (`--ui-colors`)** | `#142a48` | `var(--ui-colors)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-text` | `10px` | Typography Ink Token |
| `--padding` | `max(6px, calc(var(--base-text) * .15))` | Layout / Spatial Grid Token |
| `--ui-colors` | `bg-primary:#000 / primary:#fff / blue:#142a48 / primary-hover:#fff302` | Brand / Palette Token |
| `--ui-color-bg-primary` | `#000` | Canvas / Surface Token |
| `--ui-color-primary` | `#fff` | Brand / Palette Token |
| `--ui-color-blue` | `#142a48` | Brand / Palette Token |
| `--ui-color-primary-hover` | `#fff302` | Brand / Palette Token |
| `--miumiu-header` | `1.5em` | Layout / Spatial Grid Token |
| `--ball-size` | `max(35px, 1.8vw)` | Layout / Spatial Grid Token |
| `--bounce-height` | `90px` | Layout / Spatial Grid Token |
| `--floor-height` | `0px` | Layout / Spatial Grid Token |
| `--duration` | `.8s` | Motion / Easing Token |
| `--exit-duration` | `.3s` | Motion / Easing Token |
| `--scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--inner-height` | `900px` | Layout / Spatial Grid Token |
| `--vp-height` | `900px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.desktop> — `thetiebreak-merci-michel-com`)**:
   - Landmark `<header class="desktop">` (`1440px`) hosting `The Tie-break!` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-active-route="Home"`, `data-v-app`, `data-v-04734283`, `data-v-7fa37a60`), and stylesheet rule `.webgl-canvas { outline:none }`.
2. **Hero Stage & Focal Lead (<section.view> — `The Tie-break!`)**:
   - Landmark `<section class="view view-home">` presenting display lead `The Tie-break!` and copy excerpt *"Play the game and discover the latest New Balance X Miu Miu colle"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.view-home> — `Play the game and discover the lat`)**:
   - Landmark `<section class="view view-home">` rendering section `Play the game and discover the latest New Balanc` with copy *"The Tie-break!"*, asset references (`utag.js`, `favicon.ico`, `favicon_dark.svg`, `favicon_light.svg`), and grid rule `hover { border-color:transparent }`.
4. **Interactive Detail & Feature Matrix (<section.view:nth(2)> — `thetiebreak-merci-michel-com Inter`)**:
   - Landmark `<section class="view view-home">` framing `thetiebreak-merci-michel-com Interactive Matrix` and `thetiebreak-merci-michel-com Archive & Directory` (*"Play the game and discover the latest New Balanc"*) with `#05152d` surface cards, `#fff302` accents, and `before { transform:scale(1.1) }`.
5. **Colophon & Global Directory Footer (<footer.ui> — `https://thetiebreak.merci-michel.com/`)**:
   - Landmark `<footer class="ui">` anchoring `The Tie-break!` footer links (`Overview · Index · Archive · About · Contact`), copy *"thetiebreak-merci-michel-com Interactive Matrix"*, and `#000000` structural dividers.
