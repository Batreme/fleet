# UI & UX Architecture: www-arsenals-com

## Overview & Design Identity
- **Target**: `www-arsenals-com` (**Arsenals · Liberty is built**)
- **Production URL**: [http://www.arsenals.com](http://www.arsenals.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#061a2b` / `#0000`)
- **Summary**: Liberty is built. Arsenals builds a new maritime arsenal: autonomous, attritable, massed. The Harpoon is our first asset.
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Battling`
- **Body Font Stack**: `Clearface`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `270px`, `44px`, `80px`, `94px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `270px`, `44px`, `80px`, `94px`)
- **Body Copy**: rule `p` (`font-size: 44px`, `line-height: 54px`, `letter-spacing: 0`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `270px`, `44px`, `80px`, `94px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#061a2b` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#f0ebde` | `var(--cream)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0003` | `#dim { background: #0003 }` |
| **Interactive Accent / Highlight** | `#0000` | `.menu-m .menu-box { border-color: #0000 }` |
| **Secondary / Muted Copy** | `#fff` | `.glint { color: #fff }` |
| **Structural Hairline Border** | `#dfe` | `#hud { color: #dfe }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--in` | `80px` | Dimension / Scale Token |
| `--lead` | `108px` | Dimension / Scale Token |
| `--edge` | `9px` | Dimension / Scale Token |
| `--hv-ease` | `cubic-bezier(.65, 0, .35, 1)` | Motion / Easing Token |
| `--hv-time` | `.5s` | Motion / Timing Token |
| `--lightningcss-dark` | `initial` | Canvas / Surface Token |
| `--bg` | `#061a2b` | Canvas / Surface Token |
| `--cream` | `#f0ebde` | Color / Atmospheric Token |
| `--edge-x` | `0px` | Dimension / Scale Token |
| `--edge-top` | `0px` | Dimension / Scale Token |
| `--sw` | `1` | Design System Custom Token |
| `--period` | `1.8s` | Motion / Timing Token |
| `--lo` | `0.2` | Design System Custom Token |
| `--hi` | `0.95` | Design System Custom Token |
| `--www-arsenals-com-bg` | `#061a2b` | Canvas Substrate (from `var(--bg)` in `:root`) |
| `--www-arsenals-com-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.el> — `www-arsenals-com`)**:
   - Landmark `<nav class="el">` hosting `Arsenals · Liberty is built` navigation (`Careers Careers · LinkedIn LinkedIn`), DOM attributes (`data-layout="width"`, `data-hover-style="none"`, `data-btn="frame"`, `data-layout="desktop"`), and stylesheet rule `body { overflow-x:hidden }`.
2. **Hero Stage & Focal Lead (<section.glints> — `Arsenals`)**:
   - Landmark `<section class="glints">` presenting display lead `Arsenals` and copy excerpt *"Contact Us Contact Us"* over `#061a2b` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.out> — `Liberty is built`)**:
   - Landmark `<section class="out">` rendering section `Liberty is built` with copy *"Liberty is not granted. Not given. It must be built. And today it"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `stage { pointer-events:none;isolation:isolate;position:fixed;inset:0;overflow:hi... }`.
4. **Interactive Detail & Feature Matrix (<section.el> — `A modular fleet that adapts to the`)**:
   - Landmark `<section class="el copy">` framing `A modular fleet that adapts to the mission` and `The Harpoon. Our first asset. Completely autonom` (*"The Harpoon. Our first asset. Completely autonomous. Deployable b"*) with `#0003` surface cards, `#0000` accents, and `.frame { transform-origin:0 0;width:1920px;height:1080px;display:block;position:a... }`.
5. **Colophon & Global Directory Footer (<footer.el> — `http://www.arsenals.com`)**:
   - Landmark `<footer class="el">` anchoring `Arsenals · Liberty is built` footer links (`Careers Careers · LinkedIn LinkedIn`), copy *"Copyright © 2026 Arsenals. All rights reserved."*, and `#dfe` structural dividers.
