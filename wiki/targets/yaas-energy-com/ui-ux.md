# UI & UX Architecture: yaas-energy-com

## Overview & Design Identity
- **Target**: `yaas-energy-com` (**YAAS Energy — Zero-Sugar Energy Drink in 5 Bold Flavors**)
- **Production URL**: [https://yaas-energy.com/](https://yaas-energy.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0b0a09` ink, `#f3d118` accent)
- **Summary**: YAAS — zero-sugar, 5-calorie energy drink in 5 bold flavors: Citrus Lemon, Blueberry Rush, Wild Strawberry, Solar Orange, Green Apple. No...
- **Total Clean CSS Variables Extracted**: `54` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Soledago`
- **Body Font Stack**: `Bounded`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Soledago", "Arial Narrow", system-ui, -apple-system, sans-serif`
- **Section Heading (`H2`)**: CSS variables `--h2g: 0`
- **Body Copy**: CSS variables `--font-body: "Helvetica Neue", Arial, system-ui, -apple-system, sans-serif`, `--text-body: calc(16px * var(--ui-scale))`, `--text-body-sm: calc(14px * var(--ui-scale))`
- **Metadata & Labels**: CSS variables `--caption-top: 625px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#212121` | `var(--ink-on-light)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdfaf1` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#f3d118` | `var(--bg-color)` in `:root` |
| **Secondary / Muted Copy** | `#e43a6c` | `var(--card-color)` in `:root` |
| **Structural Hairline Border** | `#0b0a09` | `html { background: #0b0a09 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-display` | `"Soledago", "Arial Narrow", system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--font-body` | `"Helvetica Neue", Arial, system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--font-beiruti` | `"Bounded", "Helvetica Neue", Arial, system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--ui-scale` | `1` | Design System Custom Token |
| `--ink` | `#ffffff` | Typography Ink Token |
| `--ink-soft` | `rgba(255, 255, 255, .85)` | Typography Ink Token |
| `--ink-on-light` | `#212121` | Canvas / Surface Token |
| `--ink-on-light-soft` | `rgba(33, 33, 33, .72)` | Canvas / Surface Token |
| `--block-gap` | `calc(120px * var(--ui-scale))` | Layout / Spatial Grid Token |
| `--heading-gap` | `50px` | Typography Ink Token |
| `--block-heading` | `clamp(30px, 4.17vw, calc(80px * var(--ui-scale)))` | Typography Ink Token |
| `--text-body` | `calc(16px * var(--ui-scale))` | Typography Ink Token |
| `--text-body-sm` | `calc(14px * var(--ui-scale))` | Typography Ink Token |
| `--content-gutter` | `30px` | Layout / Spatial Grid Token |
| `--content-inline` | `var(--content-gutter)` | Design System Custom Token |
| `--paper` | `#fdfaf1` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.hero-nav> — `yaas-energy-com`)**:
   - Landmark `<nav class="hero-nav">` hosting `YAAS Energy — Zero-Sugar Energy Drin` navigation (`Flavors · About us · FAQ · Contacts`), DOM attributes (`data-seo="1"`, `data-seo="1"`, `data-seo="1"`, `data-seo="1"`), and stylesheet rule `root { --block-heading: clamp(30px, 4.17vw, calc(80px * var(--ui-scale))) }`.
2. **Hero Stage & Focal Lead (<section.intro-wrap> — `5 Flavors. 1 Energy.`)**:
   - Landmark `<section class="intro-wrap">` presenting display lead `5 Flavors. 1 Energy.` and copy excerpt *"Yes, we use cookies. Sugar-free."* over `#ffffff` canvas and `#0b0a09` ink.
3. **Primary Showcase & Content Grid (<section.screen2> — `YAAS. That feeling when everything`)**:
   - Landmark `<section class="screen2 is-arc-running">` rendering section `YAAS. That feeling when everything just hits diff...` with copy *"Google Analytics cookies show us how the site performs. No ads, n"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png`), and grid rule `html { background:0b0a09 }`.
4. **Interactive Detail & Feature Matrix (<section.screen2-arc> — `This isn't about hyping you up. It`)**:
   - Landmark `<section class="screen2-arc">` framing `This isn't about hyping you up. It's about stayin...` and `Hanging with the squad till sunrise` (*"Zero-sugar energy for people who move at their own speed. Flavor "*) with `#fdfaf1` surface cards, `#f3d118` accents, and `button { font-family:inherit;color:inherit;background:none;border:none;cursor:poi... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yaas-energy.com/`)**:
   - Landmark `<footer class="site-footer is-reveal">` anchoring `YAAS Energy — Zero-Sugar Energy ` footer links (`Flavors · About us · FAQ · Contacts`), copy *"This isn't about hyping you up. It's about staying locked in"*, and `#0b0a09` structural dividers.
