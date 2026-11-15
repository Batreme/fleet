# UI & UX Architecture: 100yearsmonet-com

## Overview & Design Identity
- **Target**: `100yearsmonet-com` (**Monet 100 — A century without Claude Monet · 3D gallery**)
- **Production URL**: [https://100yearsmonet.com](https://100yearsmonet.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0b1020`)
- **Summary**: A hundred years after Claude Monet’s death: walk on water through his paintings into the room of Water Lilies. An immersive 3D tribute wi...
- **Total Clean CSS Variables Extracted**: `7` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Quelia`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `18px`, `36px`, `1.1em`, `clamp(1.3rem,2.2vw,2rem)`)
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -.01em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `18px`, `36px`, `1.1em`, `clamp(1.3rem,2.2vw,2rem)`)
- **Metadata & Labels**: rule `small` (`letter-spacing: .12em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `body { background: #000 }` |
| **Primary Typography Ink** | `#e5dce9` | `body { color: #e5dce9 }` |
| **Elevated Surface / Card Substrate** | `#777` | `button { color: #777 }` |
| **Interactive Accent / Highlight** | `#0b1020` | `.mui-pre { background: #0b1020 }` |
| **Secondary / Muted Copy** | `#1a1a22` | `.mui .mui-sound { color: #1a1a22 }` |
| **Structural Hairline Border** | `#fff` | `.mui-gtitle svg { fill: #fff }` |
| **Variable Token (`--mui-cream`)** | `#FCF4E9` | `var(--mui-cream)` in stylesheet |
| **Variable Token (`--mui-ink`)** | `#282B36` | `var(--mui-ink)` in stylesheet |
| **Variable Token (`--mui-night`)** | `#15141f` | `var(--mui-night)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cat` | `calc(1 - var(--p,0))` | Design System Custom Token |
| `--fs` | `min(52vh,30vw)` | Dimension / Scale Token |
| `--snd-r` | `var(--mui-gutter,24px)` | Dimension / Scale Token |
| `--snd-b` | `calc(26px + env(safe-area-inset-bottom,0px))` | Dimension / Scale Token |
| `--bx` | `50%` | Dimension / Scale Token |
| `--by` | `46%` | Dimension / Scale Token |
| `--ch` | `150px` | Dimension / Scale Token |
| `--mui-cream` | `#FCF4E9` | Color / Atmospheric Token |
| `--mui-cream-rgb` | `252 244 233` | Design System Custom Token |
| `--mui-ink` | `#282B36` | Typography Ink Token |
| `--mui-night` | `#15141f` | Color / Atmospheric Token |
| `--mui-serif` | `"Quelia","Iowan Old Style",Georgia,serif` | Typography / Scale Token |
| `--mui-sans` | `"Manrope","Helvetica Neue",Arial,system-ui,sans-serif` | Typography / Scale Token |
| `--mui-ui` | `"Manrope","Helvetica Neue",Arial,system-ui,sans-serif` | Dimension / Scale Token |
| `--100yearsmonet-co-bg` | `#000` | Canvas Substrate (from `body { background: #000 }`) |
| `--100yearsmonet-co-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mui-hud> — `100yearsmonet-com`)**:
   - Landmark `<header class="mui-hud mui-hud--top">` hosting `Monet 100 — A century without Claude` navigation (`Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`), DOM attributes (`data-title-stay`, `data-enter="sound"`, `data-v="Dawn"`, `data-card="impression"`), and stylesheet rule `body { background:000 }`.
2. **Hero Stage & Focal Lead (<section.mui-hero> — `100 Years without Monet`)**:
   - Landmark `<section class="mui-hero">` presenting display lead `100 Years without Monet` and copy excerpt *"Claude Monet died at Giverny on 5 December 1926. A hundred years "* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.mui-card> — `100 years without Monet`)**:
   - Landmark `<article class="mui-card">` rendering section `100 years without Monet` with copy *"This experience needs JavaScript and WebGL."*, asset references (`favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`, `quelia.woff2`), and grid rule `canvas { position:fixed;inset:0;width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<article.mui-card> — `Impression, Sunrise`)**:
   - Landmark `<article class="mui-card">` framing `Impression, Sunrise` and `Woman with a Parasol` (*"Claude Monet 1926 — 2026"*) with `#777` surface cards, `#0b1020` accents, and `journey { height:2000vh;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.mui-garden> — `https://100yearsmonet.com`)**:
   - Landmark `<footer class="mui-garden">` anchoring `Monet 100 — A century without Cl` footer links (`Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`), copy *"He died at Giverny on 5 December 1926. A century later, walk"*, and `#fff` structural dividers.
