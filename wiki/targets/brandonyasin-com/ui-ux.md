---
title: "UI & UX Architecture: brandonyasin-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: brandonyasin-com

## Overview & Design Identity
- **Target**: `brandonyasin-com` (**Brandon Yasin — Creative Director & Designer**)
- **Production URL**: [https://brandonyasin.com](https://brandonyasin.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#363229` canvas, `#c3beb1` ink, `#ffeb48` accent)
- **Summary**: Brand, digital and spatial design within lifestyle and luxury. AI scales the production, not the craft. Based in Denmark, working globally.
- **Total Clean CSS Variables Extracted**: `18` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Unica Pro`
- **Body Font Stack**: `Neue Haas Unica Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 90.144px`, `line-height: 111.779px`, `font-weight: 400`, `letter-spacing: -3.60576px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40.032px`, `line-height: 48.0384px`, `font-weight: 400`, `letter-spacing: -1.60128px`)
- **Body Copy**: live computed `body` (`font-size: 15.984px`, `line-height: 20.7792px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 12px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#363229` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#c3beb1` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.img-wrap:after { background-color: #000000 }` |
| **Interactive Accent / Highlight** | `#ffeb48` | `::-moz-placeholder { color: #ffeb48 }` |
| **Secondary / Muted Copy** | `#111111` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `:before { border: #ffffff }` |
| **Variable Token (`--color-bg`)** | `#f8f6f2` | `var(--color-bg)` in `:root` |
| **Variable Token (`--selection-bg`)** | `#443000` | `var(--selection-bg)` in `:root` |
| **Variable Token (`--color-green`)** | `#263b1c` | `var(--color-green)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-main` | `#111` | Brand / Palette Token |
| `--color-bg` | `#f8f6f2` | Canvas / Surface Token |
| `--selection-color` | `#111` | Brand / Palette Token |
| `--selection-bg` | `#44300033` | Canvas / Surface Token |
| `--focus-bg` | `var(--color-main)` | Canvas / Surface Token |
| `--focus-color` | `var(--color-bg)` | Brand / Palette Token |
| `--lvh` | `1vh` | Layout / Spatial Grid Token |
| `--svh` | `1vh` | Layout / Spatial Grid Token |
| `--img-over-opacity` | `0` | Design System Custom Token |
| `--bg-brightness` | `1` | Canvas / Surface Token |
| `--size` | `1168` | Layout / Spatial Grid Token |
| `--cut` | `100%` | Dimension / Scale Token |
| `--color-green` | `#263b1c` | Brand / Palette Token |
| `--line-x` | `0px` | Dimension / Scale Token |
| `--line-w` | `0` | Design System Custom Token |
| `--rows-tile-h` | `19.9rem` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `brandonyasin-com`)**:
   - Landmark `<header class="header font-body-12">` (`1440x84px`) hosting `Brandon Yasin — Creative Director & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hid="initial-time-theme"`, `data-v-b4d4802c`, `data-slug="/archive"`, `data-menu-title-lag`), and stylesheet rule `.font-headline-1 { letter-spacing:-.04em;font:400 5.4rem/1.24 Neue Haas Unica Pro,Helvetica... }`.
2. **Hero Stage & Focal Lead (<section.archive-container> — `archive`)**:
   - Landmark `<section class="archive-container container">` presenting display lead `archive` and copy excerpt *"Every project begins with observation. Understanding the context,"* over `#363229` canvas and `#c3beb1` ink.
3. **Primary Showcase & Content Grid (<section.header> — `Every project begins with observat`)**:
   - Landmark `<section class="header about-header">` rendering section `Every project begins with observation. Understan` with copy *"Brandon Awwwards Site of the day SOTD Yasin Site of the day SOTD "*, asset references (`entry.CxmSBJR3.css`, `BUkWhEWa.js`, `DK3Fl9T5.js`, `IQKDJ7dv.js`), and grid rule `.font-headline-2 { letter-spacing:0;font:251 2.8rem/1.2 Neue Haas Unica Pro,Helvetica Neue,... }`.
4. **Interactive Detail & Feature Matrix (<section.holder> — `Brandon Awwwards Site of the day S`)**:
   - Landmark `<section class="holder">` framing `Brandon Awwwards Site of the day SOTD Yasin Site` and `Brandon Awwwards Site of the day SOTD` (*"Brandon Awwwards Site of the day SOTD"*) with `#000000` surface cards, `#ffeb48` accents, and `.font-headline-2-large { letter-spacing:0;font:251 5.5rem/1.24 Neue Haas Unica Pro,Helvetica Neue... }`.
5. **Colophon & Global Directory Footer (<footer.menu-tile> — `https://brandonyasin.com`)**:
   - Landmark `<footer class="menu-tile">` anchoring `Brandon Yasin — Creative Directo` footer links (`Overview · Index · Archive · About · Contact`), copy *"Site of the day SOTD"*, and `#ffffff` structural dividers.
