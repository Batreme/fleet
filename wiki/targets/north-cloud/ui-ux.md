---
title: "UI & UX Architecture: north-cloud"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: north-cloud

## Overview & Design Identity
- **Target**: `north-cloud` (**North.cloud · Take control of your cloud costs with AI-powered FinOps.**)
- **Production URL**: [https://north.cloud](https://north.cloud)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121314` / `#b055e6`)
- **Summary**: North is the financial operating system for cloud, AI, and data. Allocate spend, catch anomalies, and automate savings across AWS, Azure,...
- **Total Clean CSS Variables Extracted**: `183` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Untitled Sans`
- **Body Font Stack**: `Untitled Sans`
- **Monospace / Technical Font Stack**: `Degrad Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 96px`, `line-height: 88.32px`, `font-weight: 500`, `letter-spacing: -3.84px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96px`, `line-height: 88.32px`, `font-weight: 500`, `letter-spacing: -3.84px`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--form-label-opacity: .6`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#121314` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#afb8c2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#b055e6` | `.comparison .button-content:las... { background: #b055e6 }` |
| **Secondary / Muted Copy** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Structural Hairline Border** | `#d4dae0` | `var(--cc-btn-secondary-hover-border-color)` in `:root` |
| **Variable Token (`--cc-bg`)** | `#ffffff` | `var(--cc-bg)` in `:root` |
| **Variable Token (`--cc-primary-color`)** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Variable Token (`--cc-btn-primary-bg`)** | `#30363c` | `var(--cc-btn-primary-bg)` in `:root` |
| **Variable Token (`--cc-btn-secondary-bg`)** | `#eaeff2` | `var(--cc-btn-secondary-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-modal-border-radius` | `.5rem` | Elevation / Border Token |
| `--cc-btn-border-radius` | `.4rem` | Elevation / Border Token |
| `--cc-modal-transition-duration` | `.25s` | Motion / Easing Token |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` | Typography Ink Token |
| `--cc-modal-margin` | `1rem` | Layout / Spatial Grid Token |
| `--cc-z-index` | `2147483647` | Elevation / Border Token |
| `--cc-bg` | `#fff` | Canvas / Surface Token |
| `--cc-primary-color` | `#2c2f31` | Brand / Palette Token |
| `--cc-secondary-color` | `#5e6266` | Brand / Palette Token |
| `--cc-btn-primary-bg` | `#30363c` | Canvas / Surface Token |
| `--cc-btn-primary-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` | Brand / Palette Token |
| `--cc-btn-primary-hover-bg` | `#000` | Canvas / Surface Token |
| `--cc-btn-primary-hover-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` | Brand / Palette Token |
| `--cc-btn-secondary-bg` | `#eaeff2` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `north-cloud`)**:
   - Landmark `<header class="header">` (`1440x85px`) hosting `North.cloud · Take control of your c` navigation (`Features · Manage · AI Agent · Coststreams · Analyze`), DOM attributes (`data-theme="black"`, `data-header`, `data-astro-cid-gxxacloy`, `data-dom="desktop-menu"`), and stylesheet rule `.pointer-events-none { pointer-events:none }`.
2. **Hero Stage & Focal Lead (<section.c-heroHome> — `THE FINANCIAL OPERATING SYSTEM FOR`)**:
   - Landmark `<section class="c-heroHome heroHome">` presenting display lead `THE FINANCIAL OPERATING SYSTEM FOR CLOUD, AI, AND...` and copy excerpt *"The Financial Operating System"* over `#121314` canvas and `#afb8c2` ink.
3. **Primary Showcase & Content Grid (<section.c-logoWall> — `The Financial Operating System For`)**:
   - Landmark `<section class="c-logoWall logoWall">` rendering section `The Financial Operating System For Cloud, AI, And...` with copy *"For Cloud, AI, And Data."*, asset references (`untitled-sans-regular.woff2`, `untitled-sans-medium.woff2`, `favicon.ico`, `favicon-180x180.png`), and grid rule `.collapse { visibility:collapse }`.
4. **Interactive Detail & Feature Matrix (<section.c-layer> — `I n t e l l i g e n c e L a y e r`)**:
   - Landmark `<section class="c-layer layer">` framing `I n t e l l i g e n c e L a y e r` and `A u t o m a t i o n L a y e r` (*"North provides the intelligence layer for every dollar your cloud"*) with `#000000` surface cards, `#b055e6` accents, and `.invisible { visibility:hidden }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://north.cloud`)**:
   - Landmark `<footer class="c-footer footer">` anchoring `North.cloud · Take control of yo` footer links (`Features · Manage · AI Agent · Coststreams · Analyze`), copy *"C l o u d f i n a n c e"*, and `#d4dae0` structural dividers.
