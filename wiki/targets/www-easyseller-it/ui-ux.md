# UI & UX Architecture: www-easyseller-it

## Overview & Design Identity
- **Target**: `www-easyseller-it` (**EASYSELLER · Sales Digital Agency**)
- **Production URL**: [https://www.easyseller.it/](https://www.easyseller.it/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d6efd` / `#d63384`)
- **Summary**: Aiutiamo i brand e retail multibrand a crescere online attraverso percorsi completi di consulenza · digitalizzazione · gestione · promozi...
- **Total Clean CSS Variables Extracted**: `451` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Font1`
- **Body Font Stack**: `Font2`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--h1-val: 14rem`, `--h1-font-size: calc(var(--h1-val) + 0.2 * ((100vw - 1440px) / 200))`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **Section Heading (`H2`)**: CSS variables `--h2-val: 10rem`, `--h2-font-size: calc(var(--h2-val) + 0.2 * ((100vw - 1440px) / 200))`; rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: calc(var(--p-font-size) + 0.5...`, `line-height: 150%`)
- **Metadata & Labels**: CSS variables `--p-small-val: 1rem`, `--p-small-font-size: calc(var(--p-small-val) + 0.2 * ((100vw - 1440px) / 200))`; rule `,small` (`font-size: .875em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d6efd` | `var(--bs-blue)` in `:root` |
| **Primary Typography Ink** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Interactive Accent / Highlight** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Secondary / Muted Copy** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Structural Hairline Border** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Variable Token (`--bs-yellow`)** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Variable Token (`--bs-green`)** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-black`)** | `#000` | `var(--bs-black)` in `:root` |
| **Variable Token (`--bs-white`)** | `#fff` | `var(--bs-white)` in `:root` |
| **Variable Token (`--bs-gray`)** | `#6c757d` | `var(--bs-gray)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
| **Variable Token (`--bs-gray-100`)** | `#f8f9fa` | `var(--bs-gray-100)` in `:root` |
| **Variable Token (`--bs-gray-200`)** | `#e9ecef` | `var(--bs-gray-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-purple` | `#6f42c1` | Color / Atmospheric Token |
| `--bs-pink` | `#d63384` | Typography Ink Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |
| `--bs-orange` | `#fd7e14` | Color / Atmospheric Token |
| `--bs-yellow` | `#ffc107` | Color / Atmospheric Token |
| `--bs-green` | `#198754` | Color / Atmospheric Token |
| `--bs-teal` | `#20c997` | Color / Atmospheric Token |
| `--bs-cyan` | `#0dcaf0` | Color / Atmospheric Token |
| `--bs-black` | `#000` | Canvas / Surface Token |
| `--bs-white` | `#fff` | Canvas / Surface Token |
| `--bs-gray` | `#6c757d` | Color / Atmospheric Token |
| `--bs-gray-dark` | `#343a40` | Canvas / Surface Token |
| `--bs-gray-100` | `#f8f9fa` | Color / Atmospheric Token |
| `--bs-gray-200` | `#e9ecef` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.py-4> — `www-easyseller-it`)**:
   - Landmark `<header class="py-4 ready">` hosting `EASYSELLER · Sales Digital Agency` navigation (`Instagram · LinkedIn · Facebook · Youtube · Servizi`), DOM attributes (`data-wp-strategy="defer"`, `data-barba="wrapper"`, `data-barba="container"`, `data-barba-namespace="home"`), and stylesheet rule `before { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero_section> — `E l e v a t e Y o u r S a l e s`)**:
   - Landmark `<section class="hero_section">` presenting display lead `E l e v a t e Y o u r S a l e s` and copy excerpt *"Dal 2013 il nostro obiettivo è aiutarti a vendere di più, acquisi"* over `#0d6efd` canvas and `#6610f2` ink.
3. **Primary Showcase & Content Grid (<section.py-5> — `Aiutiamo i brand e retail multibra`)**:
   - Landmark `<section class="py-5">` rendering section `Aiutiamo i brand e retail multibrand a crescere o...` with copy *"Alcuni dei brand che abbiamo supportato nel raggiungere nuovi ris"*, asset references (`favicon.png`, `embed`, `styles.css`, `bootstrap.min.css`), and grid rule `root { scroll-behavior:smooth }`.
4. **Interactive Detail & Feature Matrix (<section.py-5> — `Operatività concreta.`)**:
   - Landmark `<section class="py-5">` framing `Operatività concreta.` and `Focus sui risultati.` (*"Woman · Man · Kids Beachwear"*) with `#6f42c1` surface cards, `#d63384` accents, and `address { margin-bottom:1rem;font-style:normal;line-height:inherit }`.
5. **Colophon & Global Directory Footer (<footer.py-5> — `https://www.easyseller.it/`)**:
   - Landmark `<footer class="py-5">` anchoring `EASYSELLER · Sales Digital Agenc` footer links (`Instagram · LinkedIn · Facebook · Youtube · Servizi`), copy *"Woman · Man Beachwear"*, and `#fd7e14` structural dividers.
