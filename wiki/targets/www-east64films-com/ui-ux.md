---
title: "UI & UX Architecture: www-east64films-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-east64films-com

## Overview & Design Identity
- **Target**: `www-east64films-com` (**EAST 64 Films · Tokyo-Based International Production Company**)
- **Production URL**: [https://www.east64films.com/](https://www.east64films.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#222222` canvas, `#ece9e2` ink, `#3498db` accent)
- **Summary**: EAST 64 Films is a Tokyo-based production company working across Japan and abroad. From commercials, music videos, and branded content to...
- **Total Clean CSS Variables Extracted**: `111` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `matrix-ii-ext-semi-narrow`
- **Body Font Stack**: `Noto Sans JP`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44px`, `line-height: 55px`, `font-weight: 400`)
- **Section Heading (`H2`)**: observed font-size ladder: `44px`, `16px`, `11px`, `80%`, `75%`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 29.5px`, `font-weight: 500`); CSS variables `--font-size-base: var(--font-size-md)`; rule `p` (`font-size: 13px`, `line-height: 1.4`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: 20.2812px`, `font-weight: 400`); CSS variables `--base-letter-spacing: 0em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#222222` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ece9e2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#3b3b3b` | `.footer { background: #3b3b3b }` |
| **Interactive Accent / Highlight** | `#3498db` | `.c-form__btn-primary { background-color: #3498db }` |
| **Secondary / Muted Copy** | `#808080` | `.has-cyan-bluish-gray-color { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#e74c3c` | `.c-form__group.has-error select { border-color: #e74c3c }` |
| **Variable Token (`--cl-blue`)** | `#4eaebf` | `var(--cl-blue)` in `:root` |
| **Variable Token (`--cl-yellow`)** | `#f6b000` | `var(--cl-yellow)` in `:root` |
| **Variable Token (`--cl-green`)** | `#00a44d` | `var(--cl-green)` in `:root` |
| **Variable Token (`--cl-red`)** | `#e43936` | `var(--cl-red)` in `:root` |
| **Variable Token (`--cl-orange`)** | `#f46f2c` | `var(--cl-orange)` in `:root` |
| **Variable Token (`--cl-dark`)** | `#151515` | `var(--cl-dark)` in `:root` |
| **Variable Token (`--cl-white`)** | `#ffffff` | `var(--cl-white)` in `:root` |
| **Variable Token (`--cl-whitegray`)** | `#eeeeee` | `var(--cl-whitegray)` in `:root` |
| **Variable Token (`--cl-black`)** | `#1a1a1a` | `var(--cl-black)` in `:root` |
| **Variable Token (`--cl-lightgray`)** | `#b9b9b9` | `var(--cl-lightgray)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cl-blue` | `#4eaebf` | Color / Atmospheric Token |
| `--cl-yellow` | `#f6b000` | Color / Atmospheric Token |
| `--cl-green` | `#00a44d` | Color / Atmospheric Token |
| `--cl-red` | `#e43936` | Color / Atmospheric Token |
| `--cl-orange` | `#f46f2c` | Color / Atmospheric Token |
| `--cl-dark` | `#151515` | Canvas / Surface Token |
| `--cl-white` | `#ffffff` | Canvas / Surface Token |
| `--cl-whitegray` | `#eeeeee` | Canvas / Surface Token |
| `--cl-black` | `#1a1a1a` | Canvas / Surface Token |
| `--cl-blackgray` | `#222222` | Canvas / Surface Token |
| `--cl-lightgray` | `#b9b9b9` | Canvas / Surface Token |
| `--cl-base` | `var(--cl-white)` | Design System Custom Token |
| `--cl-bg` | `var(--cl-blackgray)` | Canvas / Surface Token |
| `--fw-regular` | `400` | Design System Custom Token |
| `--fw-medium` | `500` | Design System Custom Token |
| `--fw-bold` | `700` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-east64films-com`)**:
   - Landmark `<header class="site-header">` (`1440x33px`) hosting `EAST 64 Films · Tokyo-Based Internat` navigation (`T T O O P P · W W O O R R K K S S · A A B B O O U U T T`), DOM attributes (`data-lang-suffix="/"`, `data-lang-suffix="/"`, `data-lang-suffix="/"`, `data-lang-suffix="/works/"`), and stylesheet rule `.tk-matrix-ii { font-family: "matrix-ii",serif; }`.
2. **Hero Stage & Focal Lead (<section.p-works> — `EAST 64 Films · Tokyo-Based Intern`)**:
   - Landmark `<section class="p-works">` presenting display lead `EAST 64 Films · Tokyo-Based International Produc` and copy excerpt *"C o m m e r c i a l s , F i l m s , C r e a t i v e C a m p a i g"* over `#222222` canvas and `#ece9e2` ink.
3. **Primary Showcase & Content Grid (<section.p-works:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="p-works">` rendering section `Featured Work & Interactive Showcase` with copy *"C o m m e r c i a l s ,"*, asset references (`knx0cof.css`, `fonts.googleapis.com`, `fonts.gstatic.com`, `favicon.ico`), and grid rule `.tk-matrix-ii-extra { font-family: "matrix-ii-extra",serif; }`.
4. **Interactive Detail & Feature Matrix (<section.p-works:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="p-works">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"C a m p a i g n s ,"*) with `#3b3b3b` surface cards, `#3498db` accents, and `.tk-matrix-ii-display-hilite-scr { font-family: "matrix-ii-display-hilite-scr",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.l-footer> — `https://www.east64films.com/`)**:
   - Landmark `<footer class="l-footer">` anchoring `EAST 64 Films · Tokyo-Based Inte` footer links (`T T O O P P · W W O O R R K K S S · A A B B O O U U T T`), copy *"M u s i c V i d e o s , B r a n d e d C o n t e n t , e t c "*, and `#e74c3c` structural dividers.
