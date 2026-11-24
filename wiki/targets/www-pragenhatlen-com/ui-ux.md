---
title: "UI & UX Architecture: www-pragenhatlen-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-pragenhatlen-com

## Overview & Design Identity
- **Target**: `www-pragenhatlen-com` (**Prägen Hätlen · Swiss watchmaking for the crypto community.**)
- **Production URL**: [https://www.pragenhatlen.com/](https://www.pragenhatlen.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ecebea` / `#0000ff`)
- **Summary**: Trust, precision, resilience and uncompromising attention to detail.
- **Total Clean CSS Variables Extracted**: `78` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: `RedHatMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 39.6px`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ecebea` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c1114` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.BaseButton-module__white__qygOa { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.App-module__link__jsQ7Z:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `.StickyModal-module__header__LViCK { border-bottom: #ffffff }` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--breakpoint-mobile` | `320px` | Dimension / Scale Token |
| `--breakpoint-mobile-horizontal` | `500px` | Dimension / Scale Token |
| `--breakpoint-tablet` | `768px` | Dimension / Scale Token |
| `--breakpoint-tablet-height` | `950px` | Layout / Spatial Grid Token |
| `--breakpoint-laptop` | `1024px` | Dimension / Scale Token |
| `--breakpoint-bigLaptop-min` | `1366px` | Dimension / Scale Token |
| `--breakpoint-bigLaptop` | `1440px` | Dimension / Scale Token |
| `--breakpoint-desktop` | `1680px` | Dimension / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-white--40` | `#ffffff66` | Canvas / Surface Token |
| `--color-white--16` | `#ffffff29` | Canvas / Surface Token |
| `--color-white--4` | `#ffffff0a` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-black--50` | `#00000080` | Canvas / Surface Token |
| `--color-black--30` | `#0000004d` | Canvas / Surface Token |
| `--color-black--24` | `#0000003d` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Header-module__top__mJsjm> — `www-pragenhatlen-com`)**:
   - Landmark `<header class="Header-module__top__mJsjm">` (`1440x76px`) hosting `Prägen Hätlen · Swiss watchmaking fo` navigation (`[02] A b o u t · [04] F A Q`), DOM attributes (`data-modal-id="cart"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.App-module__root__JTuhI { background-color:var(--color-bg) }`.
2. **Hero Stage & Focal Lead (<section.HeroVideo-module__root__FiOC1> — `THE SCARCEST ASSET, ON YOUR WRIST`)**:
   - Landmark `<section class="HeroVideo-module__root__FiOC1">` presenting display lead `THE SCARCEST ASSET, ON YOUR WRIST` and copy excerpt *"Limited Edition. Swiss-made. Crypto Native"* over `#ecebea` canvas and `#0c1114` ink.
3. **Primary Showcase & Content Grid (<section.RotateScreen-module__root__m8vUV> — `The scarcest asset, on your wrist`)**:
   - Landmark `<section class="RotateScreen-module__root__m8vUV">` rendering section `The scarcest asset, on your wrist` with copy *"Prägen Hätlen introduces a new relationship between craftsmanship"*, asset references (`watch-background-drawing-D_cIL0zr...`, `cart-DdlU5Vpi.png`, `engrave_blue-Bx6rooYN.jpg`, `www.pragenhatlen.com`), and grid rule `.App-module__link__jsQ7Z { color:var(--color-black) }`.
4. **Interactive Detail & Feature Matrix (<section.RotateScreen-module__hidden__pMK7C> — `Precision in every layer`)**:
   - Landmark `<section class="RotateScreen-module__hidden__pMK7C">` framing `Precision in every layer` and `Plate Customization` (*"By scanning the watch crystal with a smartphone, collectors are c"*) with `#ffffff` surface cards, `#0000ff` accents, and `.App-module__link__jsQ7Z:hover { color:var(--color-blue-cher-ami) }`.
5. **Colophon & Global Directory Footer (<footer.Footer-module__root__oib9b> — `https://www.pragenhatlen.com/`)**:
   - Landmark `<footer class="Footer-module__root__oib9b">` anchoring `Prägen Hätlen · Swiss watchmakin` footer links (`[02] A b o u t · [04] F A Q`), copy *"Through this interaction, they can access the associated Pro"*, and `#ffffff` structural dividers.
