# UI & UX Architecture: morphowater-com

## Overview & Design Identity
- **Target**: `morphowater-com` (**MORPHO · Natural Spring Water from Costa Rica**)
- **Production URL**: [https://morphowater.com](https://morphowater.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#d0edff` canvas, `#101820` ink, `#ffffff` accent)
- **Summary**: Discover MORPHO natural spring water from Costa Rica. Explore our source, still water in 12 oz aluminum cans, and our upcoming sparkling...
- **Total Clean CSS Variables Extracted**: `83` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Publico Headline`
- **Body Font Stack**: `Gotham`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(46px,6.1vw,94px)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 44px`)
- **Body Copy**: CSS variables `--body-reveal: 1`; rule `p` (`font-size: 12px`)
- **Metadata & Labels**: rule `small` (`font-size: 8px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d0edff` | `var(--brand-flight)` in `:root` |
| **Primary Typography Ink** | `#0a127b` | `var(--brand-reserve)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0056d4` | `var(--brand-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `var(--brand-purity)` in `:root` |
| **Secondary / Muted Copy** | `#101820` | `var(--brand-premium)` in `:root` |
| **Structural Hairline Border** | `#6b7080` | `var(--muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand-flight` | `#d0edff` | Canvas / Surface Token |
| `--brand-reserve` | `#0a127b` | Brand / Palette Token |
| `--brand-blue` | `#0056d4` | Brand / Palette Token |
| `--brand-purity` | `#ffffff` | Brand / Palette Token |
| `--brand-premium` | `#101820` | Brand / Palette Token |
| `--ink` | `var(--brand-premium)` | Typography Ink Token |
| `--paper` | `var(--brand-purity)` | Canvas / Surface Token |
| `--flow-serif` | `"Publico Headline",Georgia,serif` | Typography / Scale Token |
| `--brand-secondary` | `color-mix(in srgb,var(--brand-premium) 68%,white)` | Brand / Palette Token |
| `--brand-rule` | `color-mix(in srgb,var(--brand-premium) 20%,transparent)` | Brand / Palette Token |
| `--read-progress` | `0` | Design System Custom Token |
| `--read-rest-opacity` | `.34` | Design System Custom Token |
| `--word-on` | `clamp(0,calc((var(--read-progress) - var(--word-start))*40),1)` | Design System Custom Token |
| `--flow-surface` | `#101820` | Canvas / Surface Token |
| `--panel-opacity` | `1` | Design System Custom Token |
| `--copy-opacity` | `1` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.morpho-header> — `morphowater-com`)**:
   - Landmark `<header class="morpho-header">` hosting `MORPHO · Natural Spring Water from C` navigation (`The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`), DOM attributes (`data-journey-critical`, `data-journey-styles`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.flow-page em { font-family:var(--flow-serif);font-style:italic;font-weight:300;font-syn... }`.
2. **Hero Stage & Focal Lead (<section.flow-journey> — `A world within.`)**:
   - Landmark `<section class="flow-journey">` presenting display lead `A world within.` and copy excerpt *"Skip the introduction"* over `#d0edff` canvas and `#101820` ink.
3. **Primary Showcase & Content Grid (<section.territory-journey> — `A small click. A world opens.`)**:
   - Landmark `<section class="territory-journey coastal-story">` rendering section `A small click. A world opens.` with copy *"NATURAL COSTA RICAN SPRING WATER"*, asset references (`gotham-light-common.woff2`, `gotham-book-common.woff2`, `publico-headline-light-italic-com...`, `wordmark-white.webp`), and grid rule `.flow-page .flow-header img { filter:none }`.
4. **Interactive Detail & Feature Matrix (<article.territory-panel> — `Let the outside in.`)**:
   - Landmark `<article class="territory-panel">` framing `Let the outside in.` and `Back to what matters.` (*"Natural spring water from Costa Rica."*) with `#0056d4` surface cards, `#ffffff` accents, and `.flow-page .flow-skip { color:var(--brand-premium) }`.
5. **Colophon & Global Directory Footer (<footer.flow-footer> — `https://morphowater.com`)**:
   - Landmark `<footer class="flow-footer morpho-footer">` anchoring `MORPHO · Natural Spring Water fr` footer links (`The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`), copy *"Still and sparkling. In aluminum cans."*, and `#6b7080` structural dividers.
