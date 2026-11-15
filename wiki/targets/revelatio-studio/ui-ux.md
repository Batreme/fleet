# UI & UX Architecture: revelatio-studio

## Overview & Design Identity
- **Target**: `revelatio-studio` (**Revelatio · Branding, Product Design & Code**)
- **Production URL**: [https://revelatio.studio/](https://revelatio.studio/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ff0`)
- **Summary**: Revelatio is an integrated studio for branding, product design, and code, building digital experiences and brand systems for ambitious co...
- **Total Clean CSS Variables Extracted**: `22` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Grotesk Text Pro 55 Roman`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: `monospace!important`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--tbg)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--tfg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `a { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#ff0` | `mark { background: #ff0 }` |
| **Secondary / Muted Copy** | `#333` | `body { color: #333 }` |
| **Structural Hairline Border** | `#3898ec` | `.w-button { background-color: #3898ec }` |
| **Variable Token (`--color--neutral--900`)** | `#ffffff52` | `var(--color--neutral--900)` in `:root` |
| **Variable Token (`--color--neutral--200`)** | `#00000014` | `var(--color--neutral--200)` in `:root` |
| **Variable Token (`--color--neutral--800`)** | `#ffffff29` | `var(--color--neutral--800)` in `:root` |
| **Variable Token (`--color--neutral--300`)** | `#00000029` | `var(--color--neutral--300)` in `:root` |
| **Variable Token (`--color--neutral--400`)** | `#00000052` | `var(--color--neutral--400)` in `:root` |
| **Variable Token (`--color--neutral--500`)** | `#000000a3` | `var(--color--neutral--500)` in `:root` |
| **Variable Token (`--color--neutral--600`)** | `#ffffff0a` | `var(--color--neutral--600)` in `:root` |
| **Variable Token (`--color--neutral--700`)** | `#ffffff14` | `var(--color--neutral--700)` in `:root` |
| **Variable Token (`--color--neutral--1000`)** | `#ffffffa3` | `var(--color--neutral--1000)` in `:root` |
| **Variable Token (`--color--neutral--100`)** | `#0000000a` | `var(--color--neutral--100)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color--neutral--light` | `white` | Canvas / Surface Token |
| `--color--neutral--dark` | `black` | Canvas / Surface Token |
| `--color--neutral--900` | `#ffffff52` | Brand / Palette Token |
| `--color--neutral--200` | `#00000014` | Brand / Palette Token |
| `--color--neutral--800` | `#ffffff29` | Brand / Palette Token |
| `--color--neutral--300` | `#00000029` | Brand / Palette Token |
| `--color--neutral--400` | `#00000052` | Brand / Palette Token |
| `--color--neutral--500` | `#000000a3` | Brand / Palette Token |
| `--color--neutral--600` | `#ffffff0a` | Brand / Palette Token |
| `--color--neutral--700` | `#ffffff14` | Brand / Palette Token |
| `--color--neutral--1000` | `#ffffffa3` | Brand / Palette Token |
| `--color--neutral--100` | `#0000000a` | Brand / Palette Token |
| `--connected-color` | `var(--color-two)` | Brand / Palette Token |
| `--menu-width` | `16em` | Layout / Spatial Grid Token |
| `--menu-transition-settings` | `height 200ms ease,max-height 200ms ease` | Motion / Easing Token |
| `--clock-rotate-direction` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navbar> — `revelatio-studio`)**:
   - Landmark `<nav class="navbar">` hosting `Revelatio · Branding, Product Design` navigation (`Work · Approach · About · Careers · EN`), DOM attributes (`data-wf-domain="revelatio.studio"`, `data-wf-page="6a1dba8694fc8f455cf55833"`, `data-wf-site="6a1dba8694fc8f455cf5585d"`, `data-scale-hover-bound="1"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.w-mod-ix> — `Branding, Product Design & Code. O`)**:
   - Landmark `<div class="w-mod-ix">` presenting display lead `Branding, Product Design & Code. One integrated v...` and copy excerpt *"G e t i n t o u c h"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<div.lenis> — `We partner with companies of all s`)**:
   - Landmark `<div class="lenis">` rendering section `We partner with companies of all sizes, across in...` with copy *"S e e a l l p r o j e c t s"*, asset references (`cdn.prod.website-files.com`, `pt-br`, `revelatio-studio.webflow.shared.6...`, `6a1adb7b38c8bf5b0bcefe1c_revelati...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.lenis-smooth> — `Waterloo, New York, Boca Raton, At`)**:
   - Landmark `<div class="lenis-smooth">` framing `Waterloo, New York, Boca Raton, Atlanta, Los Ange...` and `Nothing here happened overnight. Each number repr...` (*"Fractional Brand Leadership Innovation Advisory Dedicated Brand S"*) with `#0000` surface cards, `#ff0` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://revelatio.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Revelatio · Branding, Product De` footer links (`Work · Approach · About · Careers · EN`), copy *"Fractional Brand Leadership"*, and `#3898ec` structural dividers.
