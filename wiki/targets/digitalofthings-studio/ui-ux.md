---
title: "UI & UX Architecture: digitalofthings-studio"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: digitalofthings-studio

## Overview & Design Identity
- **Target**: `digitalofthings-studio` (**digital of things · user experience digital studio**)
- **Production URL**: [https://digitalofthings.studio/](https://digitalofthings.studio/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#dbffad`)
- **Summary**: digital of things is an independent user experience digital studio based in Barcelona. We design and build websites, e-commerce and digit...
- **Total Clean CSS Variables Extracted**: `3` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Apple Color Emoji`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `.title` (`font-size: 15px`, `line-height: 19px`, `letter-spacing: -.15px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 15px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: -0.15px`); rule `h2` (`font-size: 16px`, `line-height: 22px`, `letter-spacing: -.16px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 15px`, `line-height: 20px`, `letter-spacing: -.15px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#212121` | `.stack-item-content-wrapper { background: #212121 }` |
| **Interactive Accent / Highlight** | `#dbffad` | `.cookie-consent__actions button { color: #dbffad }` |
| **Secondary / Muted Copy** | `#9ca3af` | `input::-moz-placeholder { color: #9ca3af }` |
| **Structural Hairline Border** | `#dbffad` | `.cookie-consent__actions button { border: #dbffad }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mask-x` | `50%` | Dimension / Scale Token |
| `--mask-y` | `50%` | Dimension / Scale Token |
| `--mask-radius` | `0px` | Elevation / Border Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--tw-skew-x` | `0` | Design System Custom Token |
| `--tw-skew-y` | `0` | Design System Custom Token |
| `--tw-scale-x` | `1` | Design System Custom Token |
| `--tw-scale-y` | `1` | Design System Custom Token |
| `--tw-scroll-snap-strictness` | `proximity` | Design System Custom Token |
| `--tw-ring-offset-width` | `0px` | Layout / Spatial Grid Token |
| `--digitalofthings--bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--digitalofthings--ink` | `#ffffff` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.js> — `digitalofthings-studio`)**:
   - Landmark `<nav class="js">` (`1440px`) hosting `digital of things · user experience ` navigation (`Projects · Pet Projects · Contact · Easter Eggs · Clients`), DOM attributes (`data-prefix`, `data-home-title="digital of things · u..."`, `data-ga="G-WW56TNJ6LL"`, `data-cf-beacon="("token": "fcd04126c7..."`), and stylesheet rule `.__className_8eaea4 { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.has-bar> — `digital of things — user experienc`)**:
   - Landmark `<section class="has-bar">` presenting display lead `digital of things — user experience digital studi...` and copy excerpt *"Explore our projects"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.antialiased> — `Selected projects`)**:
   - Landmark `<section class="antialiased">` rendering section `Selected projects` with copy *"or know more about us"*, asset references (`manifest.webmanifest`, `digitalofthings.studio`, `favicon.ico`, `icon-512.png`), and grid rule `.__className_8c25df { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
4. **Interactive Detail & Feature Matrix (<section.custom-cursor> — `or know more about us`)**:
   - Landmark `<section class="custom-cursor">` framing `or know more about us` and `User experience digital studio` (*"User experience digital studio"*) with `#212121` surface cards, `#dbffad` accents, and `html { scroll-behavior:smooth }`.
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://digitalofthings.studio/`)**:
   - Landmark `<footer class="app-footer">` anchoring `digital of things · user experie` footer links (`Projects · Pet Projects · Contact · Easter Eggs · Clients`), copy *"Turning ideas into digital experiences."*, and `#dbffad` structural dividers.
