# UI & UX Architecture: www-pragenhatlen-com

## Overview & Design Identity
- **Target**: `www-pragenhatlen-com` (**Prägen Hätlen · Swiss watchmaking for the crypto community.**)
- **Production URL**: [https://www.pragenhatlen.com/](https://www.pragenhatlen.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#52667e` / `#000`)
- **Summary**: Trust, precision, resilience and uncompromising attention to detail.
- **Total Clean CSS Variables Extracted**: `78` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `RedHatMono`
- **Monospace / Technical Font Stack**: `RedHatMono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#52667e` | `var(--watch-color-mid)` in `:root` |
| **Primary Typography Ink** | `#0c1114` | `var(--watch-color-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--color-black)` in `:root` |
| **Secondary / Muted Copy** | `#ecebea` | `var(--color-light)` in `:root` |
| **Structural Hairline Border** | `#bdc4d4` | `var(--color-blue-sky)` in `:root` |
| **Variable Token (`--color-white--40`)** | `#ffffff66` | `var(--color-white--40)` in `:root` |
| **Variable Token (`--color-white--16`)** | `#ffffff29` | `var(--color-white--16)` in `:root` |
| **Variable Token (`--color-white--4`)** | `#ffffff0a` | `var(--color-white--4)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-background-color` | `var(--color-blue-sky)` | Canvas / Surface Token |
| `--base-text-color` | `var(--color-onyx-blue)` | Typography Ink Token |
| `--watch-color-mid` | `#52667e` | Brand / Palette Token |
| `--watch-color-dark` | `#0c1114` | Canvas / Surface Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Header-module__top__mJsjm> — `www-pragenhatlen-com`)**:
   - Landmark `<header class="Header-module__top__mJsjm">` hosting `Prägen Hätlen · Swiss watchmaking fo` navigation (`[02] A b o u t · [04] F A Q`), DOM attributes (`data-modal-id="cart"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.App-module__root__JTuhI { background-color:var(--color-bg) }`.
2. **Hero Stage & Focal Lead (<section.BlockEdito-module__root__-Hj6g> — `Trust, precision, resilience and u`)**:
   - Landmark `<section class="BlockEdito-module__root__-Hj6g">` presenting display lead `Trust, precision, resilience and uncompromising a...` and copy excerpt *"label_rotate_phone*"* over `#52667e` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.BlockEdito-module__root__-Hj6g> — `These principles guide everything `)**:
   - Landmark `<section class="BlockEdito-module__root__-Hj6g">` rendering section `These principles guide everything we build.` with copy *"This website uses cookies to analyze traffic and improve your exp"*, asset references (`watch-background-drawing-D_cIL0zr...`, `cart-DdlU5Vpi.png`, `engrave_blue-Bx6rooYN.jpg`, `www.pragenhatlen.com`), and grid rule `.App-module__link__jsQ7Z { color:var(--color-black) }`.
4. **Interactive Detail & Feature Matrix (<section.BlockEdito-module__root__-Hj6g> — `The founder`)**:
   - Landmark `<section class="BlockEdito-module__root__-Hj6g">` framing `The founder` and `The Atelier` (*"[01] C o l l e c t i o n"*) with `#fff` surface cards, `#000` accents, and `.App-module__link__jsQ7Z:hover { color:var(--color-blue-cher-ami) }`.
5. **Colophon & Global Directory Footer (<footer.Footer-module__root__oib9b> — `https://www.pragenhatlen.com/`)**:
   - Landmark `<footer class="Footer-module__root__oib9b">` anchoring `Prägen Hätlen · Swiss watchmakin` footer links (`[02] A b o u t · [04] F A Q`), copy *"[03] P l a c e y o u r i n t e r e s t"*, and `#bdc4d4` structural dividers.
