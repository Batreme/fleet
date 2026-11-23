---
title: "UI & UX Architecture: therechabite-com-au"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: therechabite-com-au

## Overview & Design Identity
- **Target**: `therechabite-com-au` (**The Rechabite • Multi-level Palace of Surprise and Delight**)
- **Production URL**: [https://therechabite.com.au/](https://therechabite.com.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0f0f0f` canvas, `#ffffff` ink, `#000000` accent)
- **Summary**: M e e t M e A t T h e R e c h a b i t e
- **Total Clean CSS Variables Extracted**: `73` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Founders Grotesk Condensed`
- **Body Font Stack**: `Founders Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 201.6px`, `line-height: 141.12px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 30px`, `font-weight: 400`, `letter-spacing: 0.72px`); rule `h2` (`font-size: max(18px,1.1vw)`, `line-height: 1`, `font-weight: var(--font-we...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`, `letter-spacing: -0.8px`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-body: "Founders Grotesk", sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`, `letter-spacing: -0.8px`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0f0f0f` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ff5598` | `var(--color-hot-pink)` in `:root` |
| **Structural Hairline Border** | `#000000` | `.border-black { border-color: #000000 }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
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
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `therechabite-com-au`)**:
   - Landmark `<header class="pointer-events-none top-0">` (`1430x119px`) hosting `The Rechabite • Multi-level Palace o` navigation (`What’s On What’s On · Rechabite Hall · Hello Rooftop · Double Rainbow · Goodwill Club`), DOM attributes (`data-optimized="1"`, `data-optimized="1"`, `data-optimized="1"`, `data-optimized="1"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.min-h-lvh> — `MEET ME AT THE RECH A BITE`)**:
   - Landmark `<section class="min-h-lvh bg-light-black">` presenting display lead `MEET ME AT THE RECH A BITE` and copy excerpt *"From scorching cabaret and red-hot comedy to live music that’ll m"* over `#0f0f0f` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.bg-light-black> — `M e e t M e A t T h e R e c h a b `)**:
   - Landmark `<section class="bg-light-black relative">` rendering section `M e e t M e A t T h e R e c h a b i t e` with copy *"What's on What's on"*, asset references (`clarity.js`, `z0jl5zt2hc`, `4457171594343694`, `fbevents.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.overflow-hidden> — `THE CBD TOUR · A YOU WOULDN’T LIVE`)**:
   - Landmark `<section class="overflow-hidden text-white">` framing `THE CBD TOUR · A YOU WOULDN’T LIVE SHOW` and `Buckshot with Sidney Phillips, Oscar18` (*"What’s on What’s on"*) with `#000000` surface cards, `#000000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-light-black> — `https://therechabite.com.au/`)**:
   - Landmark `<footer class="bg-light-black text-white">` anchoring `The Rechabite • Multi-level Pala` footer links (`What’s On What’s On · Rechabite Hall · Hello Rooftop · Double Rainbow · Goodwill Club`), copy *"R ech a b i t e Hall"*, and `#000000` structural dividers.
