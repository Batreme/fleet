# UI & UX Architecture: zeropact-co

## Overview & Design Identity
- **Target**: `zeropact-co` (**Zeropact · Life Cycle Analysis (LCA) & Product Carbon Footprint**)
- **Production URL**: [https://zeropact.co](https://zeropact.co)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#E5E7EB` canvas, `#0A0A0A` ink, `#7C88AC` accent)
- **Summary**: Worlds Most Advanced Product Carbon Footprint AI-Powered Software
- **Total Clean CSS Variables Extracted**: `424` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Zalando Sans Expanded`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--display: flex`, `--e-n-carousel-swiper-slides-to-display: 3`, `--page-title-display: block`; rule `h1` (`font-weight: var(--e-globa...`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-weight: var(--e-globa...`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: CSS variables `--e-n-carousel-arrow-prev-caption-spacing: 15px`, `--e-n-carousel-arrow-next-caption-spacing: 15px`, `--arrow-prev-caption-spacing: 15px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#E5E7EB` | `var(--border-color)` in `:root` |
| **Primary Typography Ink** | `#FFFFFF` | `var(--e-n-carousel-arrow-normal-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#376CDF` | `var(--e-n-carousel-dots-normal-color)` in `:root` |
| **Interactive Accent / Highlight** | `#7C88AC` | `var(--e-global-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#4A5565` | `var(--e-global-color-text)` in `:root` |
| **Structural Hairline Border** | `#0A0A0A` | `var(--e-search-placeholder-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--flex-grow` | `var( --container-widget-flex-grow )` | Design System Custom Token |
| `--display` | `flex` | Design System Custom Token |
| `--flex-direction` | `row` | Design System Custom Token |
| `--container-widget-width` | `calc( ( 1 - var( --container-widget-flex-grow ) ) * 100% )` | Layout / Spatial Grid Token |
| `--container-widget-height` | `100%` | Layout / Spatial Grid Token |
| `--container-widget-flex-grow` | `1` | Layout / Spatial Grid Token |
| `--container-widget-align-self` | `stretch` | Layout / Spatial Grid Token |
| `--flex-wrap-mobile` | `wrap` | Layout / Spatial Grid Token |
| `--align-items` | `center` | Design System Custom Token |
| `--gap` | `53px 53px` | Layout / Spatial Grid Token |
| `--row-gap` | `53px` | Layout / Spatial Grid Token |
| `--column-gap` | `53px` | Layout / Spatial Grid Token |
| `--padding-top` | `80px` | Layout / Spatial Grid Token |
| `--padding-bottom` | `80px` | Layout / Spatial Grid Token |
| `--padding-left` | `20px` | Layout / Spatial Grid Token |
| `--padding-right` | `20px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `zeropact-co`)**:
   - Landmark `<header class="elementor elementor-198">` hosting `Zeropact · Life Cycle Analysis (LCA)` navigation (`Home · Solutions · E-Commerce · Logistics · Enterprise`), DOM attributes (`data-precedence="default"`, `data-precedence="default"`, `data-precedence="default"`, `data-precedence="default"`), and stylesheet rule `ementor-widget-video .elementor-w... { aspect-ratio:var(--video-aspect-ratio) }`.
2. **Hero Stage & Focal Lead (<div.site-page-root> — `life Cycle analysis (“LCA”)`)**:
   - Landmark `<div class="site-page-root">` presenting display lead `life Cycle analysis (“LCA”)` and copy excerpt *"Solutions E-Commerce Logistics Enterprise Digital Product Passpor"* over `#E5E7EB` canvas and `#0A0A0A` ink.
3. **Primary Showcase & Content Grid (<div.site-page-root> — `World's most advanced Ai-powered e`)**:
   - Landmark `<div class="site-page-root">` rendering section `World's most advanced Ai-powered engine designed...` with copy *"Digital Product Passport"*, asset references (`styles-nW61obKD.css`, `2555c6801d335bcfd3cdccb22cdb3e1e.css`, `863d0923110b7e2df40bdfebd60fedff.css`, `55ee03d21b51256d575abda3ce68a9da.css`), and grid rule `r-widget-video .elementor-wrapper... { background-color:000;border:none;display:flex;height:100%;width:100% }`.
4. **Interactive Detail & Feature Matrix (<div.site-page-root> — `Life Cycle Analysis ("LCA")`)**:
   - Landmark `<div class="site-page-root">` framing `Life Cycle Analysis ("LCA")` and `AI-Powered Last-Mile CO2 emissions at Scale` (*"Scale from one to thousands of SKUs with automated, ISO 14067-com"*) with `#376CDF` surface cards, `#7C88AC` accents, and `e .elementor-custom-embed-image-o... { background-position:50%;background-size:cover;inset:0;position:absolute }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://zeropact.co`)**:
   - Landmark `<footer class="elementor elementor-172">` anchoring `Zeropact · Life Cycle Analysis (` footer links (`Home · Solutions · E-Commerce · Logistics · Enterprise`), copy *"Explore our Solutions"*, and `#0A0A0A` structural dividers.
