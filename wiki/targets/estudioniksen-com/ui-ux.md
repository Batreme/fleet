# UI & UX Architecture: estudioniksen-com

## Overview & Design Identity
- **Target**: `estudioniksen-com` (**Estudio Niksen**)
- **Production URL**: [https://estudioniksen.com/](https://estudioniksen.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)
- **Summary**: We are an independent lifestyle brand presenting elevated garments and living-space goods through a mix of influences.
- **Total Clean CSS Variables Extracted**: `624` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Frama`
- **Body Font Stack**: `PP Neue Montreal`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: var(--x-heading-level1-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: var(--x-heading-level2-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-xxs)`, `line-height: 1.1`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: CSS variables `--text-xs: 12px`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--pswp-bg)` in `:root` |
| **Primary Typography Ink** | `#222` | `var(--pswp-placeholder-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--pswp-icon-color)` in `:root` |
| **Interactive Accent / Highlight** | `#4f4f4f` | `var(--pswp-icon-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#f0f0f0` | `var(--color-gray-200)` in `:root` |
| **Structural Hairline Border** | `#a0a1a0` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--pswp-preloader-color`)** | `#4f4f4f66` | `var(--pswp-preloader-color)` in `:root` |
| **Variable Token (`--pswp-preloader-color-secondary`)** | `#ffffffe6` | `var(--pswp-preloader-color-secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pswp-bg` | `#000` | Canvas / Surface Token |
| `--pswp-placeholder-bg` | `#222` | Canvas / Surface Token |
| `--pswp-root-z-index` | `100000` | Elevation / Border Token |
| `--pswp-preloader-color` | `#4f4f4f66` | Brand / Palette Token |
| `--pswp-preloader-color-secondary` | `#ffffffe6` | Brand / Palette Token |
| `--pswp-icon-color` | `#fff` | Brand / Palette Token |
| `--pswp-icon-color-secondary` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-color` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-width` | `2px` | Layout / Spatial Grid Token |
| `--pswp-error-text-color` | `var(--pswp-icon-color)` | Typography Ink Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-gray-200` | `#f0f0f0` | Brand / Palette Token |
| `--color-gray-300` | `#a0a1a0` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-header_inner> — `estudioniksen-com`)**:
   - Landmark `<header class="c-header_inner">` hosting `Estudio Niksen` navigation (`Shop All · Outerwear · All Outerwear · Coats · Jackets`), DOM attributes (`data-template="index"`, `data-smooth-scrolling="true"`, `data-scroll-orientation="vertical"`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"We use cookies and other technologies to personalize your experie"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.shopify-pc__banner__dialog> — `Join the family`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` rendering section `Join the family` with copy *"Manage preferences"*, asset references (`a2f45e7b43c941fd84b3f91a8.js`, `favicon.svg`, `site.webmanifest`, `vite-main-C-QMCZi1.css`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-pc__banner__dialog> — `Fall Winter '26`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` framing `Fall Winter '26` and `New arrivals` (*"Free shipping on orders over $250 CAD"*) with `#fff` surface cards, `#4f4f4f` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.container> — `https://estudioniksen.com/`)**:
   - Landmark `<footer class="container mt-fluid-3xl">` anchoring `Estudio Niksen` footer links (`Shop All · Outerwear · All Outerwear · Coats · Jackets`), copy *"Early-access to our drops, secret password to our only annua"*, and `#a0a1a0` structural dividers.
