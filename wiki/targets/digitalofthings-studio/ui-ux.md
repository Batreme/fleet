# UI & UX Architecture: digitalofthings-studio

## Overview & Design Identity
- **Target**: `digitalofthings-studio` (**digital of things · user experience digital studio**)
- **Production URL**: [https://digitalofthings.studio/](https://digitalofthings.studio/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000`)
- **Summary**: digital of things is an independent user experience digital studio based in Barcelona. We design and build websites, e-commerce and digit...
- **Total Clean CSS Variables Extracted**: `3` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `FoundersGrotesk-Medium`
- **Body Font Stack**: `CenturyExpandedBT-Roman`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: rule `.title` (`font-size: 15px`, `line-height: 19px`, `letter-spacing: -.15px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 16px`, `line-height: 22px`, `letter-spacing: -.16px`)
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 20px`, `letter-spacing: -.15px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `17px`, `24px`, `clamp(32px,5.6vw,56px)`, `18px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `body { background-color: #fff }` |
| **Primary Typography Ink** | `#ff0` | `.debug-info { background-color: #ff0 }` |
| **Elevated Surface / Card Substrate** | `#ececec` | `body { background-color: #ececec }` |
| **Interactive Accent / Highlight** | `#000` | `.loading-container { background-color: #000 }` |
| **Secondary / Muted Copy** | `#0000` | `:before { border: #0000 }` |
| **Structural Hairline Border** | `#dbffad` | `content-stack-container .expose... { background: #dbffad }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mask-x` | `50%` | Dimension / Scale Token |
| `--mask-y` | `50%` | Dimension / Scale Token |
| `--mask-radius` | `0px` | Elevation / Border Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--tw-skew-x` | `0` | Design System Custom Token |
| `--tw-skew-y` | `0` | Design System Custom Token |
| `--tw-scale-x` | `1` | Design System Custom Token |
| `--tw-scale-y` | `1` | Design System Custom Token |
| `--tw-scroll-snap-strictness` | `proximity` | Design System Custom Token |
| `--tw-ring-offset-width` | `0px` | Layout / Spatial Grid Token |
| `--digitalofthings--bg` | `#fff` | Canvas Substrate (from `body { background-color: #fff }`) |
| `--digitalofthings--ink` | `#000` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.js> — `digitalofthings-studio`)**:
   - Landmark `<nav class="js">` hosting `digital of things · user experience ` navigation (`Projects · Pet Projects · Contact · Easter Eggs · Clients`), DOM attributes (`data-prefix`, `data-home-title="digital of things · u..."`, `data-ga="G-WW56TNJ6LL"`, `data-cf-beacon="("token": "fcd04126c7..."`), and stylesheet rule `.__className_8eaea4 { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.has-bar> — `User experience digital studio`)**:
   - Landmark `<section class="has-bar">` presenting display lead `User experience digital studio` and copy excerpt *"We use Google Analytics cookies to understand how the site is use"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.antialiased> — `digital of things — user experienc`)**:
   - Landmark `<section class="antialiased">` rendering section `digital of things — user experience digital studi...` with copy *"Explore our projects"*, asset references (`manifest.webmanifest`, `digitalofthings.studio`, `favicon.ico`, `icon-512.png`), and grid rule `.__className_8c25df { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
4. **Interactive Detail & Feature Matrix (<section.cookie-consent> — `Explore`)**:
   - Landmark `<section class="cookie-consent">` framing `Explore` and `Selected projects` (*"or know more about us"*) with `#ececec` surface cards, `#000` accents, and `html { scroll-behavior:smooth }`.
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://digitalofthings.studio/`)**:
   - Landmark `<footer class="app-footer">` anchoring `digital of things · user experie` footer links (`Projects · Pet Projects · Contact · Easter Eggs · Clients`), copy *"User experience digital studio"*, and `#dbffad` structural dividers.
