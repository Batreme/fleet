# UI & UX Architecture: giordanobetti-com

## Overview & Design Identity
- **Target**: `giordanobetti-com` (**Giordano Betti - Independent Cinematographer**)
- **Production URL**: [https://giordanobetti.com/](https://giordanobetti.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`)
- **Summary**: Giordano Betti is an independent cinematographer and Director of Photography based in Tuscany, Italy.
- **Total Clean CSS Variables Extracted**: `20` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Host Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#171717` | `var(--color-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#000000` | `50 { background-color: black }` (`#000000`) |
| **Structural Hairline Border** | `#ffffff` | `.debug .f-cell { background-color: white }` (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Host Grotesk", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `"Instrument Serif", ui-serif, serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--blur-lg` | `16px` | Elevation / Border Token |
| `--aspect-video` | `16 / 9` | Design System Custom Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-foreground` | `#fff` | Typography Ink Token |
| `--color-background` | `#171717` | Canvas / Surface Token |
| `--gap` | `clamp(14px, 1.5vw, 32px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `giordanobetti-com`)**:
   - Landmark `<header class="header js-header">` hosting `Giordano Betti - Independent Cinemat` navigation (`instagram instagram · youtube youtube · linkedin linkedin`), DOM attributes (`data-v-ad171e27`, `data-v-67aeeb6a`, `data-v-6d80a5f8`, `data-v-794a89b8`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.contact-modal> — `Something in mind?`)**:
   - Landmark `<section class="contact-modal f-grid">` presenting display lead `Something in mind?` and copy excerpt *"Giordano Betti Independent Cinematographer"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.home-content> — `Giordano Betti - Independent Cinem`)**:
   - Landmark `<section class="home-content f-grid">` rendering section `Giordano Betti - Independent Cinematographer` with copy *"Independent Cinematographer"*, asset references (`entry.B8GcDMgn.css`, `Footer.BHv6vXkB.css`, `Action.C2i8mHMB.css`, `MoZuWBAS.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.home-content__footer> — `Jupiter`)**:
   - Landmark `<section class="home-content__footer f-grid">` framing `Jupiter` and `AVAVAV X ADIDAS SS25` (*"Something in mind?"*) with `#171717` surface cards, `#0000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.header__section> — `https://giordanobetti.com/`)**:
   - Landmark `<footer class="header__section">` anchoring `Giordano Betti - Independent Cin` footer links (`instagram instagram · youtube youtube · linkedin linkedin`), copy *"Let's create something meaningful together."*, and `#ffffff` structural dividers.
