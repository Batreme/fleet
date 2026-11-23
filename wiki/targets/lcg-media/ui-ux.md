---
title: "UI & UX Architecture: lcg-media"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lcg-media

## Overview & Design Identity
- **Target**: `lcg-media` (**LCG · The Agency That Fights for American Families**)
- **Production URL**: [https://lcg.media](https://lcg.media)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#de204e`)
- **Summary**: LCG provides hands-on consulting and creative solutions to support conservative campaigns and drive results for American Families.
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Soehne Breit Kraftig`
- **Body Font Stack**: `PP Mori`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 74.0571px`, `line-height: 99.9771px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 41.1429px`, `line-height: 57.6px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 10.2857px`, `line-height: 10.2857px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10.2857px`, `line-height: 10.2857px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.rendered body { background: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#de204e` | `var(--color-highlight)` in `:root` |
| **Secondary / Muted Copy** | `#68675f` | `nimated .subheader__wrapper spa... { color: #68675f }` |
| **Structural Hairline Border** | `#000000` | `.cursor__bullet { border: #000000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ease-in-sine` | `cubic-bezier(0.47, 0, 0.745, 0.715)` | Motion / Easing Token |
| `--ease-out-sine` | `cubic-bezier(0.39, 0.575, 0.565, 1)` | Motion / Easing Token |
| `--ease-in-out-sine` | `cubic-bezier(0.445, 0.05, 0.55, 0.95)` | Motion / Easing Token |
| `--ease-in-quad` | `cubic-bezier(0.55, 0.085, 0.68, 0.53)` | Motion / Easing Token |
| `--ease-out-quad` | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | Motion / Easing Token |
| `--ease-in-out-quad` | `cubic-bezier(0.455, 0.03, 0.515, 0.955)` | Motion / Easing Token |
| `--ease-in-cubic` | `cubic-bezier(0.55, 0.055, 0.675, 0.19)` | Motion / Easing Token |
| `--ease-out-cubic` | `cubic-bezier(0.215, 0.61, 0.355, 1)` | Motion / Easing Token |
| `--ease-in-out-cubic` | `cubic-bezier(0.645, 0.045, 0.355, 1)` | Motion / Easing Token |
| `--ease-in-quart` | `cubic-bezier(0.895, 0.03, 0.685, 0.22)` | Motion / Easing Token |
| `--ease-out-quart` | `cubic-bezier(0.165, 0.84, 0.44, 1)` | Motion / Easing Token |
| `--ease-in-out-quart` | `cubic-bezier(0.77, 0, 0.175, 1)` | Motion / Easing Token |
| `--ease-in-quint` | `cubic-bezier(0.755, 0.05, 0.855, 0.06)` | Motion / Easing Token |
| `--ease-out-quint` | `cubic-bezier(0.23, 1, 0.32, 1)` | Motion / Easing Token |
| `--ease-in-out-quint` | `cubic-bezier(0.86, 0, 0.07, 1)` | Motion / Easing Token |
| `--ease-in-expo` | `cubic-bezier(0.95, 0.05, 0.795, 0.035)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navigation> — `lcg-media`)**:
   - Landmark `<nav class="navigation">` (`1440px`) hosting `LCG · The Agency That Fights for Ame` navigation (`Home · Cases · Capabilities · Creed · Contact`), DOM attributes (`data-template="page"`, `data-svg-origin="121 36"`, `data-svg-origin="121 36"`, `data-svg-origin="0 0"`), and stylesheet rule `.app { height:100%;overflow:clip;position:relative;width:100% }`.
2. **Hero Stage & Focal Lead (<section.header> — `The Agency That Fights for America`)**:
   - Landmark `<section class="header header--left">` presenting display lead `The Agency That Fights for American Families Cons...` and copy excerpt *"The Agency That Fights for"* over `#121212` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.logo-video> — `The Agency That Fights for A m e r`)**:
   - Landmark `<section class="logo-video">` rendering section `The Agency That Fights for A m e r i c a n F a m...` with copy *"C a s e s C a s e s"*, asset references (`mask.svg`, `bundle.ea4ceea.css`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `before { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.subheader> — `C a s e s C a s e s`)**:
   - Landmark `<section class="subheader subheader--right">` framing `C a s e s C a s e s` and `C a p a b i l i t i e s C a p a b i l i t i e s` (*"C a p a b i l i t i e s C a p a b i l i t i e s"*) with `#000000` surface cards, `#de204e` accents, and `video { margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:b... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://lcg.media`)**:
   - Landmark `<footer class="footer">` anchoring `LCG · The Agency That Fights for` footer links (`Home · Cases · Capabilities · Creed · Contact`), copy *"C r e e d C r e e d"*, and `#000000` structural dividers.
