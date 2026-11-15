# UI & UX Architecture: www-lamagadan-studio

## Overview & Design Identity
- **Target**: `www-lamagadan-studio` (**La Magadán · Branding y diseño para emprendedoras**)
- **Production URL**: [https://www.lamagadan.studio/](https://www.lamagadan.studio/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#b00020` canvas, `#fff` ink, `#222` accent)
- **Summary**: Soy Cristina, diseñadora y creativa en La Magadán. Ayudo a emprendedoras como tú a crear marcas que conectan, destacan y venden.
- **Total Clean CSS Variables Extracted**: `0` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.85em`, `15px`, `16px`, `clamp(48px, 9vw, 132px)`, `clamp(52px, 6.4vw, 96px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.85em`, `15px`, `16px`, `clamp(48px, 9vw, 132px)`, `clamp(52px, 6.4vw, 96px)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.85em`, `15px`, `16px`, `clamp(48px, 9vw, 132px)`, `clamp(52px, 6.4vw, 96px)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.85em`, `15px`, `16px`, `clamp(48px, 9vw, 132px)`, `clamp(52px, 6.4vw, 96px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#b00020` | `.sc-logic-error { background: #b00020 }` |
| **Primary Typography Ink** | `#fff` | `.sc-logic-error { color: #fff }` |
| **Elevated Surface / Card Substrate** | `#F5F5F5` | `body { background: #F5F5F5 }` |
| **Interactive Accent / Highlight** | `#222` | `body { color: #222 }` |
| **Secondary / Muted Copy** | `#E9BC3C` | `a:hover { color: #E9BC3C }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--www-lamagadan-st-bg` | `#b00020` | Canvas Substrate (from `.sc-logic-error { background: #b00020 }`) |
| `--www-lamagadan-st-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--www-lamagadan-st-surface` | `#F5F5F5` | Surface Substrate (stylesheet-derived) |
| `--www-lamagadan-st-accent` | `#222` | Interactive Accent (stylesheet-derived) |
| `--www-lamagadan-st-muted` | `#E9BC3C` | Secondary Ink (stylesheet-derived) |
| `--www-lamagadan-st-border` | `#fff` | Structural Border (stylesheet-derived) |
| `--www-lamagadan-st-container` | `60ch` | Container Bound (stylesheet-derived) |
| `--www-lamagadan-st-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--www-lamagadan-st-pad` | `4px` | Lateral Padding (stylesheet-derived) |
| `--www-lamagadan-st-ease` | `cubic-bezier(0.4,0,0.2,1)` | Primary Easing Function |
| `--www-lamagadan-st-radius` | `2px` | Corner Radius (stylesheet-derived) |
| `--www-lamagadan-st-fs-base` | `.85em` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sc-host> — `www-lamagadan-studio`)**:
   - Landmark `<header class="sc-host">` hosting `La Magadán · Branding y diseño para ` navigation (`Quién soy · Proyectos · Servicios · Mi proceso · Testimonios`), DOM attributes (`data-dc-tpl="1"`, `data-dc-tpl="2"`, `data-dc-tpl="3"`, `data-dc-tpl="4"`), and stylesheet rule `l.sc-dc-streaming .sc-interp.sc-m... { position:relative; background:color-mix(in srgb,currentColor 5%,transpar... }`.
2. **Hero Stage & Focal Lead (<section.scp0> — `Branding para emprendedoras con un`)**:
   - Landmark `<section class="scp0">` presenting display lead `Branding para emprendedoras con una historia que...` and copy excerpt *"¿Hablamos? ¿Hablamos?"* over `#b00020` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.scp1> — `Hola, soy Cristina`)**:
   - Landmark `<section class="scp1">` rendering section `Hola, soy Cristina` with copy *"Acompaño a mujeres emprendedoras como tú a construir su identidad"*, asset references (`favicon.png`, `apple-touch-icon.png`, `support.js`, `react.production.min.js`), and grid rule `before { animation:none; background:color-mix(in srgb,currentColor 8%,transparent) }`.
4. **Interactive Detail & Feature Matrix (<section.sc-interp> — `Lo que busco`)**:
   - Landmark `<section class="sc-interp">` framing `Lo que busco` and `Lo que hago` (*"01 Lo que busco Busco la esencia de tu proyecto para que tu marca"*) with `#F5F5F5` surface cards, `#222` accents, and `.sc-host.sc-has-error { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.scp3> — `https://www.lamagadan.studio/`)**:
   - Landmark `<footer class="scp3">` anchoring `La Magadán · Branding y diseño p` footer links (`Quién soy · Proyectos · Servicios · Mi proceso · Testimonios`), copy *"Busco la esencia de tu proyecto para que tu marca sea fiel a"*, and `#fff` structural dividers.
