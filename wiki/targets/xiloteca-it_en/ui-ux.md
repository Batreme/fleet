# UI & UX Architecture: xiloteca-it_en

## Overview & Design Identity
- **Target**: `xiloteca-it_en` (**Xiloteca Trevigiana. Woods from around the world. Digital Museum.**)
- **Production URL**: [https://xiloteca.it/en/](https://xiloteca.it/en/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d6efd` / `#d63384`)
- **Summary**: Xiloteca Trevigiana. From the heart of the forests to the future of business, wood tells stories. Digital Museum of Wood Sustainability.
- **Total Clean CSS Variables Extracted**: `1001` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Mono`
- **Body Font Stack**: `raty`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: CSS variables `--bs-h1-font-size: 7.5rem`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **Section Heading (`H2`)**: CSS variables `--bs-h2-font-size: 5.5rem`; rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: CSS variables `--bs-body-color-rgb: 33,37,41`, `--bs-body-bg-rgb: 255,255,255`, `--bs-body-font-family: var(--bs-font-sans-serif)`; rule `p` (`font-size: var(--bs-h1-font-size)`, `line-height: 1`, `letter-spacing: -.04em`, `font-weight: var(--bs-font...`)
- **Metadata & Labels**: CSS variables `--search-filter-label-scale-font-size: var(--bs-body-font-size-sm)`, `--search-filter-label-color: var(--bs-dark-bs-body-color)`, `--search-filter-label-scale: 2`; rule `,small` (`font-size: .875em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d6efd` | `var(--bs-blue)` in `:root` |
| **Primary Typography Ink** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5533ff` | `var(--bs-purple)` in `:root` |
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
| `--bs-purple` | `#5533ff` | Color / Atmospheric Token |
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
1. **Brand Header & Navigation Bar (<header.fixed-top> — `xiloteca-it_en`)**:
   - Landmark `<header class="fixed-top">` hosting `Xiloteca Trevigiana. Woods from arou` navigation (`Xiloteca Trevigiana · The initiative · Digital collection · Interactive game · Wood Glossary`), DOM attributes (`data-cookieconsent="statistics"`, `data-cookieconsent="statistics"`, `data-cookieconsent="statistics"`, `data-cookieconsent="ignore"`), and stylesheet rule `before { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `Xiloteca Trevigiana. Woods from ar`)**:
   - Landmark `<main class="site-main">` presenting display lead `Xiloteca Trevigiana. Woods from around the world.` and copy excerpt *"Informazioni sui cookie"* over `#0d6efd` canvas and `#6610f2` ink.
3. **Primary Showcase & Content Grid (<main.site-main> — `From the heart of the forests to t`)**:
   - Landmark `<main class="site-main">` rendering section `From the heart of the forests to the future of bu...` with copy *"Selezione del consenso"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `cc.js`), and grid rule `root { scroll-behavior:smooth }`.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `Explore according to your profile`)**:
   - Landmark `<main class="site-main">` framing `Explore according to your profile` and `Necessari 3 I cookie necessari contribuiscono a ` (*"Necessari 3 I cookie necessari contribuiscono a rendere fruibile "*) with `#5533ff` surface cards, `#d63384` accents, and `address { margin-bottom:1rem;font-style:normal;line-height:inherit }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://xiloteca.it/en/`)**:
   - Landmark `<footer class="site-footer pt-12">` anchoring `Xiloteca Trevigiana. Woods from ` footer links (`Xiloteca Trevigiana · The initiative · Digital collection · Interactive game · Wood Glossary`), copy *"Cloudflare 1 Per saperne di più su questo fornitore cf.turns"*, and `#fd7e14` structural dividers.
