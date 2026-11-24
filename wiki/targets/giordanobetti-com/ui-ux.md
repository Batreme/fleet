---
title: "UI & UX Architecture: giordanobetti-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: giordanobetti-com

## Overview & Design Identity
- **Target**: `giordanobetti-com` (**Giordano Betti - Independent Cinematographer**)
- **Production URL**: [https://giordanobetti.com/](https://giordanobetti.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#171717` / `#ffffff`)
- **Summary**: Giordano Betti is an independent cinematographer and Director of Photography based in Tuscany, Italy.
- **Total Clean CSS Variables Extracted**: `20` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Host Grotesk`
- **Body Font Stack**: `Host Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 62.048px`, `line-height: 49.6384px`, `font-weight: 400`, `letter-spacing: -1%`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#171717` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `50 { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#ffffff` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ffffff` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | hairline divider derived from secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Host Grotesk", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `"Instrument Serif", ui-serif, serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--blur-lg` | `16px` | Elevation / Border Token |
| `--aspect-video` | `16 / 9` | Design System Custom Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-foreground` | `#fff` | Typography Ink Token |
| `--color-background` | `#171717` | Canvas / Surface Token |
| `--gap` | `clamp(14px, 1.5vw, 32px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `giordanobetti-com`)**:
   - Landmark `<header class="header js-header">` (`1440x123px`) hosting `Giordano Betti - Independent Cinemat` navigation (`instagram instagram · youtube youtube · linkedin linkedin`), DOM attributes (`data-v-ad171e27`, `data-v-67aeeb6a`, `data-v-6d80a5f8`, `data-v-794a89b8`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.home-content> — `Giordano Betti - Independent Cinem`)**:
   - Landmark `<section class="home-content f-grid">` presenting display lead `Giordano Betti - Independent Cinematographer` and copy excerpt *"Accademia Bizantina"* over `#171717` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.home-content__footer> — `AVAVAV X ADIDAS SS25`)**:
   - Landmark `<section class="home-content__footer f-grid">` rendering section `AVAVAV X ADIDAS SS25` with copy *"Cinematographer 1AC Colorist"*, asset references (`entry.B8GcDMgn.css`, `Footer.BHv6vXkB.css`, `Action.C2i8mHMB.css`, `MoZuWBAS.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.f-grid> — `Parlami D'Amore Mariu`)**:
   - Landmark `<section class="home-content__footer f-grid">` framing `Parlami D'Amore Mariu` and `60 years of Felsina` (*"Livestream director"*) with `#000000` surface cards, `#ffffff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.header__section> — `https://giordanobetti.com/`)**:
   - Landmark `<footer class="header__section">` anchoring `Giordano Betti - Independent Cin` footer links (`instagram instagram · youtube youtube · linkedin linkedin`), copy *"An independent cinematographer and director of photography b"*, and `#ffffff` structural dividers.
