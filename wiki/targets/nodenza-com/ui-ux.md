---
title: "UI & UX Architecture: nodenza-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: nodenza-com

## Overview & Design Identity
- **Target**: `nodenza-com` (**Home · Nodenza**)
- **Production URL**: [https://nodenza.com/](https://nodenza.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×3312px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#e6efff` canvas, `#000000` ink, `#ffffff` accent)
- **Summary**: Nosenza invests globally in early-stage biotech, medtech, and healthcare companies advancing life sciences and improving patient outcomes.
- **Total Clean CSS Variables Extracted**: `30` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aspekta`
- **Body Font Stack**: `Aspekta`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 68.4px`, `font-weight: 500`, `letter-spacing: -2.16px`); rule `.title` (`line-height: 0.95`, `letter-spacing: -0.03em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 68.4px`, `font-weight: 500`, `letter-spacing: -2.16px`); rule `h2` (`font-size: var(--f-b)`, `line-height: 1`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 21.6px`, `font-weight: 400`, `letter-spacing: -0.36px`); rule `p` (`font-size: var(--f-d)`, `line-height: 1.3`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 21.6px`, `font-weight: 400`, `letter-spacing: -0.36px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e6efff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffffff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#32006f` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#00a0d2` | `.wpcf7 form .wpcf7-response-output { border: #00a0d2 }` |
| **Variable Token (`--c5`)** | `#ee0000` | `var(--c5)` in `:root` |
| **Variable Token (`--c7`)** | `#bfbfbf` | `var(--c7)` in `:root` |
| **Variable Token (`--c8`)** | `#5e5e5e` | `var(--c8)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--app-height` | `100vh` | Layout / Spatial Grid Token |
| `--headroom-height` | `auto` | Layout / Spatial Grid Token |
| `--c0` | `#ffffff` | Color / Atmospheric Token |
| `--c1` | `#000000` | Color / Atmospheric Token |
| `--c2` | `#32006f` | Color / Atmospheric Token |
| `--c3` | `#e6efff` | Color / Atmospheric Token |
| `--c4` | `rgba(127, 173, 255, 0.2)` | Color / Atmospheric Token |
| `--c5` | `#ee0000` | Color / Atmospheric Token |
| `--c6` | `rgba(0, 0, 0, 0.7)` | Color / Atmospheric Token |
| `--c7` | `#bfbfbf` | Color / Atmospheric Token |
| `--c8` | `#5e5e5e` | Color / Atmospheric Token |
| `--wr` | `20rem` | Dimension / Scale Token |
| `--awr` | `calc(-1 * var(--wr))` | Design System Custom Token |
| `--gap` | `20rem` | Layout / Spatial Grid Token |
| `--sl` | `max(1px, 1rem)` | Dimension / Scale Token |
| `--br1` | `10rem` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hide-scrollbar> — `nodenza-com`)**:
   - Landmark `<header class="hide-scrollbar">` (`1440px`) hosting `Home · Nodenza` navigation (`Home · Our Team · Portfolio · News · Webinars`), DOM attributes (`data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`, `data-acsb-force-visible="true"`, `data-acsb`), and stylesheet rule `html { font-size: 0.0625vw; background-color: var(--c3); }`.
2. **Hero Stage & Focal Lead (<section.hero-snap__slide> — `Experience the explosive power of `)**:
   - Landmark `<section class="hero-snap__slide">` presenting display lead `Experience the explosive power of when science me...` and copy excerpt *"Enabling disruptive life sciences technology."* over `#e6efff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hero-snap__slide:nth(2)> — `Enabling disruptive life sciences `)**:
   - Landmark `<section class="hero-snap__slide">` rendering section `Enabling disruptive life sciences technology.` with copy *"Press Option+1 for screen-reader mode, Option+0 to cancel"*, asset references (`embed`, `styles.css`, `style.css`, `main.css`), and grid rule `body { overflow-x: hidden; }`.
4. **Interactive Detail & Feature Matrix (<section.hero-snap__slide:nth(3)> — `Press Option+1 for screen-reader m`)**:
   - Landmark `<section class="hero-snap__slide">` framing `Press Option+1 for screen-reader mode, Option+0 ` and `Established by a team of experienced life scienc` (*"Established by a team of experienced life sciences entrepreneurs,"*) with `#ffffff` surface cards, `#ffffff` accents, and `.wrapper { width: 100%; margin: 0 auto; padding: 0 var(--wr); max-width: var(--mw); }`.
5. **Colophon & Global Directory Footer (<footer.acsb-sr-alert> — `https://nodenza.com/`)**:
   - Landmark `<footer class="acsb-sr-alert">` anchoring `Home · Nodenza` footer links (`Home · Our Team · Portfolio · News · Webinars`), copy *"We leverage our team’s 100+ years experience in the creation"*, and `#00a0d2` structural dividers.
