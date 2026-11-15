# UI & UX Architecture: siglitos-com

## Overview & Design Identity
- **Target**: `siglitos-com` (**Siglitos · Polos flash que despiertan la imaginación**)
- **Production URL**: [https://siglitos.com](https://siglitos.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ffed00`)
- **Summary**: Siglitos son polos flash con 6 sabores y personalidad propia. Sin lactosa, sin gluten. El verano que activa la imaginación de los niños —...
- **Total Clean CSS Variables Extracted**: `160` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Golos Text`
- **Body Font Stack**: `Hobeaux`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--h1-body: 32px`; rule `h1` (`font-size: 52px`, `line-height: 1em`, `letter-spacing: 0`, `font-weight: 700`)
- **Section Heading (`H2`)**: CSS variables `--h2-body: 24px`; rule `h2` (`font-size: 48px`, `line-height: 1em`, `letter-spacing: 0`, `font-weight: 700`)
- **Body Copy**: CSS variables `--h1-body: 32px`, `--h2-body: 24px`, `--h3-body: 16px`; rule `,p` (`font-size: inherit`, `line-height: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `1em`, `80%`, `75%`, `100%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#0e0e0e` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fee214` | `var(--color-yellow-0)` in `:root` |
| **Interactive Accent / Highlight** | `#ffed00` | `var(--color-yellow-1)` in `:root` |
| **Secondary / Muted Copy** | `#fff700` | `var(--color-yellow-2)` in `:root` |
| **Structural Hairline Border** | `#fcfc63` | `var(--color-yellow-3)` in `:root` |
| **Variable Token (`--color-green-0`)** | `#a2f708` | `var(--color-green-0)` in `:root` |
| **Variable Token (`--color-green-1`)** | `#93f100` | `var(--color-green-1)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--kncc-primary` | `var(--color-black)` | Brand / Palette Token |
| `--kncc-primary-hover` | `var(--color-black)` | Brand / Palette Token |
| `--kncc-primary-text` | `var(--color-white)` | Typography Ink Token |
| `--font-primary` | `"Hobeaux",sans-serif` | Brand / Palette Token |
| `--font-secondary` | `"Golos Text",sans-serif` | Brand / Palette Token |
| `--cursor-default` | `url(imgs/cursor/basic.svg) 0 0,auto!important` | Design System Custom Token |
| `--cursor-pointer` | `url(imgs/cursor/pointer.svg) 0 0,auto!important` | Design System Custom Token |
| `--cursor-click` | `url(imgs/cursor/click.svg) 0 0,auto!important` | Design System Custom Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-black` | `#0e0e0e` | Canvas / Surface Token |
| `--color-yellow-0` | `#fee214` | Brand / Palette Token |
| `--color-yellow-1` | `#ffed00` | Brand / Palette Token |
| `--color-yellow-2` | `#fff700` | Brand / Palette Token |
| `--color-yellow-3` | `#fcfc63` | Brand / Palette Token |
| `--color-green-0` | `#a2f708` | Brand / Palette Token |
| `--color-green-1` | `#93f100` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.b-header__menu> — `siglitos-com`)**:
   - Landmark `<nav class="b-header__menu">` hosting `Siglitos · Polos flash que despierta` navigation (`Nosotros · Contacto · Jugar`), DOM attributes (`data-cfasync="false"`, `data-pagespeed-no-defer`, `data-wp-strategy="defer"`, `data-cfasync="false"`), and stylesheet rule `html { line-height:1.15;-webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.all-components> — `Usamos cookies`)**:
   - Landmark `<section class="all-components o-main">` presenting display lead `Usamos cookies` and copy excerpt *"Los Siglitos son seres pequeños, traviesos y poderosísimos que vi"* over `#fff` canvas and `#0e0e0e` ink.
3. **Primary Showcase & Content Grid (<section.all-components> — `Los Siglitos son seres pequeños, t`)**:
   - Landmark `<section class="all-components o-main">` rendering section `Los Siglitos son seres pequeños, traviesos y pod` with copy *"Al congelarlos, sus poderes se activan y se vuelven transferibles"*, asset references (`recaptcha__en.js`, `embed`, `styles.css`, `consent.css`), and grid rule `main { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.all-components> — `Al congelarlos, sus poderes se act`)**:
   - Landmark `<section class="all-components o-main">` framing `Al congelarlos, sus poderes se activan y se vuel` and `Descubre sus personalidades y empieza a poner lo` (*"Descubre sus personalidades y empieza a poner los poderes en tus "*) with `#fee214` surface cards, `#ffed00` accents, and `pre { font-family:monospace,monospace;font-size:1em }`.
5. **Colophon & Global Directory Footer (<footer.page-template-default> — `https://siglitos.com`)**:
   - Landmark `<footer class="page-template-default">` anchoring `Siglitos · Polos flash que despi` footer links (`Nosotros · Contacto · Jugar`), copy *"Puro placer, sin subtextos, sin excusas. No tiene vergüenza "*, and `#fcfc63` structural dividers.
