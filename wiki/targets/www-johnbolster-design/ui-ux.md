---
title: "UI & UX Architecture: www-johnbolster-design"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-johnbolster-design

## Overview & Design Identity
- **Target**: `www-johnbolster-design` (**John Bolster · Brand Identity Designer and Art Director, Saratoga Spring...**)
- **Production URL**: [https://www.johnbolster.design/](https://www.johnbolster.design/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#eceae2` / `#4b5cff`)
- **Summary**: Independent brand identity designer and art director in Saratoga Springs, NY. Brand strategy, identity, print and web for businesses, hig...
- **Total Clean CSS Variables Extracted**: `22` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `BebasProBold`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 252px`, `line-height: 216.72px`, `font-weight: 400`); CSS variables `--display: "BebasPro","Bebas Neue","Arial Narrow",Impact,sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 123.84px`, `line-height: 106.502px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--body: "Geist",ui-sans-serif,system-ui,sans-serif`; rule `p` (`font-size: clamp(15px,1.15vw,18px)`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--mono: "Geist Mono",ui-monospace,Menlo,monospace`; rule `.mono` (`font-size: 12px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#eceae2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#121413` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffa500` | `#distinkt { background: orange }` (`#ffa500`) |
| **Interactive Accent / Highlight** | `#4b5cff` | `#menu .menu-sub a:hover { color: #4b5cff }` |
| **Secondary / Muted Copy** | `#5e6360` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#2234e0` | `var(--line)` in `:root` |
| **Variable Token (`--hair`)** | `#d3d0c6` | `var(--hair)` in `:root` |
| **Variable Token (`--orange`)** | `#f47920` | `var(--orange)` in `:root` |
| **Variable Token (`--black`)** | `#0a0a0a` | `var(--black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#ECEAE2` | Canvas / Surface Token |
| `--ink` | `#121413` | Typography Ink Token |
| `--muted` | `#5E6360` | Color / Atmospheric Token |
| `--hair` | `#D3D0C6` | Color / Atmospheric Token |
| `--line` | `#2234E0` | Color / Atmospheric Token |
| `--orange` | `#F47920` | Color / Atmospheric Token |
| `--black` | `#0A0A0A` | Canvas / Surface Token |
| `--display` | `"BebasPro","Bebas Neue","Arial Narrow",Impact,sans-serif` | Design System Custom Token |
| `--body` | `"Geist",ui-sans-serif,system-ui,sans-serif` | Dimension / Scale Token |
| `--mono` | `"Geist Mono",ui-monospace,Menlo,monospace` | Typography / Scale Token |
| `--serif` | `"DM Serif Display",Georgia,serif` | Typography / Scale Token |
| `--gut` | `max(16px, env(safe-area-inset-left, 0px))` | Dimension / Scale Token |
| `--gutR` | `max(16px, env(safe-area-inset-right, 0px))` | Dimension / Scale Token |
| `--fp` | `1` | Design System Custom Token |
| `--sc` | `var(--ink)` | Design System Custom Token |
| `--on` | `clamp(0, calc((var(--fp) * 1.7 - var(--li,0) * .22) * 15 - var(--i)), 1)` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bar> — `www-johnbolster-design`)**:
   - Landmark `<header class="bar">` (`1440x64px`) hosting `John Bolster · Brand Identity Design` navigation (`01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`), DOM attributes (`data-sdkn="@vercel/analytics"`, `data-sdkv="2.0.1"`, `data-go="hero"`, `data-go="about"`), and stylesheet rule `html { background:var(--bg) }`.
2. **Hero Stage & Focal Lead (<section.st> — `JOHN BOLSTER`)**:
   - Landmark `<section class="st">` presenting display lead `JOHN BOLSTER` and copy excerpt *"Thoughtful brand identity and design for brands and everything th"* over `#eceae2` canvas and `#121413` ink.
3. **Primary Showcase & Content Grid (<section.st:nth(2)> — `J o h n B o l s t e r`)**:
   - Landmark `<section class="st">` rendering section `J o h n B o l s t e r` with copy *"Designer · Since 2002"*, asset references (`favicon-32.png`, `icon-512.png`, `apple-touch-icon.png`, `bebas-neue-pro-semiexp-bold.woff2`), and grid rule `body::-webkit-scrollbar { display:none;width:0;height:0 }`.
4. **Interactive Detail & Feature Matrix (<section.st:nth(3)> — `L e t ' s m a k e s o m e t h i n `)**:
   - Landmark `<section class="st">` framing `L e t ' s m a k e s o m e t h i n g` and `I n d e p e n d e n t B r a n d D e s i g n e r` (*"I n d e p e n d e n t B r a n d D e s i g n e r"*) with `#ffa500` surface cards, `#4b5cff` accents, and `img { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.burger> — `https://www.johnbolster.design/`)**:
   - Landmark `<footer class="burger">` anchoring `John Bolster · Brand Identity De` footer links (`01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`), copy *"I n d e p e n d e n t"*, and `#2234e0` structural dividers.
