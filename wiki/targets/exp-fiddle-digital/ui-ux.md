# UI & UX Architecture: exp-fiddle-digital

## Overview & Design Identity
- **Target**: `exp-fiddle-digital` (**Fiddle.Digital — Experiments**)
- **Production URL**: [https://exp.fiddle.digital](https://exp.fiddle.digital)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#101214` / `#544d56`)
- **Summary**: Ideas taking shape through code and design.
- **Total Clean CSS Variables Extracted**: `74` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `JP`
- **Monospace / Technical Font Stack**: `KHTekaMono`
- **Hero Display (`H1`)**: CSS variables `--h1: calc(var(--h2)*var(--type-step))`, `--h1-lh: calc(var(--body-line-height)*pow(var(--line-height-step), 3))`; rule `,h1` (`font-size: var(--h1)`, `line-height: var(--h1-lh)`, `letter-spacing: calc(var(--h1)/100*va...`)
- **Section Heading (`H2`)**: CSS variables `--h2: calc(var(--h3)*var(--type-step))`, `--h2-lh: calc(var(--body-line-height)*pow(var(--line-height-step), 2))`; rule `,h2` (`font-size: var(--h2)`, `line-height: var(--h2-lh)`, `letter-spacing: calc(var(--h2)/100*va...`)
- **Body Copy**: CSS variables `--body-font-size: 1rem`, `--body-line-height: 1.2`, `--fdcm--body-text-main-default: #ded4e6`; rule `p` (`font-size: clamp(12px,var(--fdcm--font-s...`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `var(--body-font-size)`, `1rem`, `var(--h1)`, `var(--h2)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#101214` | `var(--fdcm--bg-default)` in `:root` |
| **Primary Typography Ink** | `#ded4e6` | `var(--fdcm--body-text-main-default)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b8a5b8` | `var(--fdcm--body-text-secondary-default)` in `:root` |
| **Interactive Accent / Highlight** | `#544d56` | `var(--fdcm--ui-secondary-default)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--fdcm--ui-highlight-main-default)` in `:root` |
| **Structural Hairline Border** | `#746a76` | `var(--fdcm--ui-highlight-secondary-default)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--left` | `1` | Design System Custom Token |
| `--top` | `1` | Design System Custom Token |
| `--width` | `1` | Layout / Spatial Grid Token |
| `--height` | `1` | Layout / Spatial Grid Token |
| `--exp-width` | `calc(var(--col)*6 + var(--g-gap)*5)` | Layout / Spatial Grid Token |
| `--exp-height` | `calc(100svh - var(--h1)*2)` | Layout / Spatial Grid Token |
| `--g-columns` | `6` | Layout / Spatial Grid Token |
| `--l-delay` | `calc(sibling-index()*var(--exp-overlay-strip-delay))` | Motion / Easing Token |
| `--type-step` | `1.333` | Typography / Scale Token |
| `--body-font-size` | `1rem` | Typography / Scale Token |
| `--body-line-height` | `1.2` | Typography / Scale Token |
| `--line-height-step` | `var(--body-line-height) /var(--type-step)` | Typography / Scale Token |
| `--mm` | `calc(var(--m)/var(--type-step))` | Design System Custom Token |
| `--h6` | `calc(var(--p)*var(--type-step))` | Design System Custom Token |
| `--h5` | `calc(var(--h6)*var(--type-step))` | Design System Custom Token |
| `--h4` | `calc(var(--h5)*var(--type-step))` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.vault> — `exp-fiddle-digital`)**:
   - Landmark `<header class="vault">` hosting `Fiddle.Digital — Experiments` navigation (`FD.Exp · Let's talk`), DOM attributes (`data-string-scroll-mode="smooth"`, `data-string-scroll-device="desktop"`, `data-engine="three.js r182"`, `data-v-5709dad2`), and stylesheet rule `.video-wrap.-fit { align-items:center;display:flex;justify-content:center;overflow:hidden;p... }`.
2. **Hero Stage & Focal Lead (<main.page> — `Fiddle.Digital — Experiments`)**:
   - Landmark `<main class="page home-page">` presenting display lead `Fiddle.Digital — Experiments` and copy excerpt *"Customize Settings"* over `#101214` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.page> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="page home-page">` rendering section `Featured Work & Interactive Showcase` with copy *"Fiddle.Digital — Experiments"*, asset references (`favicon.ico`, `apple-touch-icon-57x57.png`, `apple-touch-icon-72x72.png`, `apple-touch-icon-114x114.png`), and grid rule `.video-wrap.-fit video { height:100%;left:0;-o-object-fit:cover;object-fit:cover;position:relativ... }`.
4. **Interactive Detail & Feature Matrix (<main.page> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="page home-page">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#b8a5b8` surface cards, `#544d56` accents, and `.slider { align-items:center;display:flex;flex-direction:column;justify-content:fl... }`.
5. **Colophon & Global Directory Footer (<footer.gl-layer> — `https://exp.fiddle.digital`)**:
   - Landmark `<footer class="gl-layer">` anchoring `Fiddle.Digital — Experiments` footer links (`FD.Exp · Let's talk`), copy *"Technical Architecture & Narrative"*, and `#746a76` structural dividers.
