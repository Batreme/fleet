# UI & UX Architecture: davaris-gr

## Overview & Design Identity
- **Target**: `davaris-gr` (**Homepage - Davaris**)
- **Production URL**: [https://davaris.gr/](https://davaris.gr/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0d6efd` canvas, `#6610f2` ink, `#d63384` accent)
- **Summary**: We are a family-owned company built on heritage, excellence, and a human-centric approach. Taking all the necessary steps for the protect...
- **Total Clean CSS Variables Extracted**: `223` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Moderat`
- **Body Font Stack**: `Moderat Extended`
- **Monospace / Technical Font Stack**: `Moderat Mono`
- **Hero Display (`H1`)**: CSS variables `--fs-h1: clamp(3.75rem, 3.09rem + 2.817vw, 5.625rem)`, `--lh-h1: .9`; rule `,.h1` (`line-height: 1.2`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--fs-h2: clamp(2.125rem, 1.4rem + 3.6vw, 4.688rem)`, `--lh-h2: 1`; rule `,.h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: 1.125rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `var(--bs-body-font-size)`, `2.5rem`, `2rem`, `1.75rem`)

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

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--space-xs` | `clamp(1rem, 2.2vw, 2.65rem)` | Layout / Spatial Grid Token |
| `--space-sm` | `clamp(1.875rem, 4.43vw, 5.3125rem)` | Layout / Spatial Grid Token |
| `--space-md` | `clamp(2.5rem, 6.5vw, 7.8125rem)` | Layout / Spatial Grid Token |
| `--space-lg` | `clamp(3.75rem, 8.85vw, 10.625rem)` | Layout / Spatial Grid Token |
| `--block-spacing` | `var(--space-lg)` | Layout / Spatial Grid Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `davaris-gr`)**:
   - Landmark `<header class="site-header">` hosting `Homepage - Davaris` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-cfasync="false"`, `data-no-minify="true"`, `data-no-optimize="1"`, `data-noptimize="1"`), and stylesheet rule `.flickity-enabled { position:relative }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Fashion textiles that inspire`)**:
   - Landmark `<section class="hero hero--video">` presenting display lead `Fashion textiles that inspire` and copy excerpt *"E-Showroom E-Showroom"* over `#0d6efd` canvas and `#6610f2` ink.
3. **Primary Showcase & Content Grid (<section.scrolled-text> — `We are a family-owned company buil`)**:
   - Landmark `<section class="scrolled-text u-escape-container">` rendering section `We are a family-owned company built on heritage,...` with copy *"Collections Collections Plain Explore Collection Fancy Explore Co"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `.flickity-enabled:focus { outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.collections-media> — `Collections`)**:
   - Landmark `<section class="collections-media u-escape-container">` framing `Collections` and `Plain Collection` (*"Plain Explore Collection"*) with `#6f42c1` surface cards, `#d63384` accents, and `.flickity-viewport { overflow:hidden;position:relative;height:100%;touch-action:pan-y }`.
5. **Colophon & Global Directory Footer (<footer.nav-primary__footer> — `https://davaris.gr/`)**:
   - Landmark `<footer class="nav-primary__footer">` anchoring `Homepage - Davaris` footer links (`Overview · Index · Archive · About · Contact`), copy *"Explore Collection"*, and `#fd7e14` structural dividers.
