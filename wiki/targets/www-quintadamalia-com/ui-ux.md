# UI & UX Architecture: www-quintadamalia-com

## Overview & Design Identity
- **Target**: `www-quintadamalia-com` (**Quinta D. Amália - Redefining Luxury Living in Portugal**)
- **Production URL**: [https://www.quintadamalia.com/](https://www.quintadamalia.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0d6efd` canvas, `#6610f2` ink, `#d63384` accent)
- **Summary**: Set in the heart of Vila Nova de Gaia, Quinta D. Amália is more than a residence - it’s a lifestyle defined by exclusivity, wellness & na...
- **Total Clean CSS Variables Extracted**: `574` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aladin`
- **Body Font Stack**: `Big Shoulders Display`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: rule `,small` (`font-size: .875em`)

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
1. **Brand Header & Navigation Bar (<header.qda-header> — `www-quintadamalia-com`)**:
   - Landmark `<header class="qda-header">` hosting `Quinta D. Amália - Redefining Luxury` navigation (`Home · About · Apartments · Lifestyle · Contact`), DOM attributes (`data-rocket-preload`, `data-wpr-hosted-gf-parameters="family=Big+Shoulders+..."`, `data-wpr-hosted-gf-parameters="family=Big+Shoulders+..."`, `data-wpr-hosted-gf-parameters`), and stylesheet rule `.fadeIn { -webkit-animation-name:fadeIn;animation-name:fadeIn }`.
2. **Hero Stage & Focal Lead (<div.elementor> — `W h e r e l u x u r y m e e t s s `)**:
   - Landmark `<div class="elementor elementor-385">` presenting display lead `W h e r e l u x u r y m e e t s s e r e n i t y` and copy excerpt *"Quinta D. Amália is more than a residence - it’s a lifestyle defi"* over `#0d6efd` canvas and `#6610f2` ink.
3. **Primary Showcase & Content Grid (<div.elementor> — `W e l c o m e t o Q u i n t a D . `)**:
   - Landmark `<div class="elementor elementor-385">` rendering section `W e l c o m e t o Q u i n t a D . A m á l i a` with copy *"Every residence is a masterpiece of craftsmanship, featuring prem"*, asset references (`a61f2901ff646b2ab74adf1962144.css`, `8vIH7w4qzmVxm2BL9A.woff2`, `marcellus-weo_ebrok8hqldviaf81vvo...`, `css2`), and grid rule `.fadeInDown { -webkit-animation-name:fadeInDown;animation-name:fadeInDown }`.
4. **Interactive Detail & Feature Matrix (<div.elementor> — `Quinta D. Amália: A Vision of Time`)**:
   - Landmark `<div class="elementor elementor-385">` framing `Quinta D. Amália: A Vision of Timeless Elegance` and `V a r i o u s O p t i o n s` (*"With construction beginning in Q4 2026, Quinta D. Amália is poise"*) with `#6f42c1` surface cards, `#d63384` accents, and `.fadeInLeft { -webkit-animation-name:fadeInLeft;animation-name:fadeInLeft }`.
5. **Colophon & Global Directory Footer (<footer.home> — `https://www.quintadamalia.com/`)**:
   - Landmark `<footer class="home">` anchoring `Quinta D. Amália - Redefining Lu` footer links (`Home · About · Apartments · Lifestyle · Contact`), copy *"Elegant Simplicity"*, and `#fd7e14` structural dividers.
