# UI & UX Architecture: www-davidecarusio-it

## Overview & Design Identity
- **Target**: `www-davidecarusio-it` (**Davide Carusio - Web Designer / Webflow Dev**)
- **Production URL**: [https://www.davidecarusio.it/](https://www.davidecarusio.it/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#f9efe7`)
- **Summary**: Freelance web designer and Webflow expert in Italy. Fast, custom-built websites from design to development for agencies and international...
- **Total Clean CSS Variables Extracted**: `19` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`)
- **Body Copy**: rule `body` (`font-size: var(--size-font)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--button-043-color)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--button-043-color-focus)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1c1c1b` | `.underlay-nav__container { color: #1c1c1b }` |
| **Interactive Accent / Highlight** | `#f9efe7` | `.underlay-nav__container { color: #f9efe7 }` |
| **Secondary / Muted Copy** | `#000000` | `::selection { background-color: black }` (`#000000`) |
| **Structural Hairline Border** | `#f5ede4` | `.cursor-bubble { background-color: #f5ede4 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size-unit` | `16` | Layout / Spatial Grid Token |
| `--size-container-ideal` | `1440` | Layout / Spatial Grid Token |
| `--size-container-min` | `1280px` | Layout / Spatial Grid Token |
| `--size-container-max` | `1920px` | Layout / Spatial Grid Token |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container-max))` | Layout / Spatial Grid Token |
| `--button-043-color` | `#fff` | Brand / Palette Token |
| `--button-043-color-background` | `currentColor` | Canvas / Surface Token |
| `--button-043-hover-color-background` | `currentColor` | Canvas / Surface Token |
| `--button-043-icon-color` | `currentColor` | Brand / Palette Token |
| `--button-043-icon-color-background` | `transparent` | Canvas / Surface Token |
| `--button-043-color-focus` | `#000` | Brand / Palette Token |
| `--button-043-padding` | `0.3em 0.5em` | Layout / Spatial Grid Token |
| `--button-043-border-radius` | `0.125em` | Elevation / Border Token |
| `--button-043-icon-border-radius` | `0.125em` | Elevation / Border Token |
| `--button-043-text-duplicate-distance` | `1.5em` | Typography Ink Token |
| `--button-043-focus-inset` | `-0.125em` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.underlay-nav__header> — `www-davidecarusio-it`)**:
   - Landmark `<nav class="underlay-nav__header">` hosting `Davide Carusio - Web Designer / Webf` navigation (`davide carusio · Projects · Services · IT · G e t i n t o u c h`), DOM attributes (`data-wf-page="6aabacfa3017369152d1f8b2"`, `data-wf-site="6a3a84272e4493d30711d604"`, `data-theme-nav="light"`, `data-bg-nav="light"`), and stylesheet rule `focus { outline:none; }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `Privacy Policy`)**:
   - Landmark `<section class="hero_wrap">` presenting display lead `Privacy Policy` and copy excerpt *"t h e b e s t p i z z a i s t h e m a r g h e r i t a"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.sticky-title-wrapper> — `Data Controller`)**:
   - Landmark `<section class="sticky-title-wrapper">` rendering section `Data Controller` with copy *"P r o j e c t s P r o j e c t s"*, asset references (`normalize.css`, `webflow.css`, `davidecarusio-it-v3.webflow.css`, `favicon.png`), and grid rule `html.lenis body { height: auto; }`.
4. **Interactive Detail & Feature Matrix (<section.work_wrap> — `Data Collected`)**:
   - Landmark `<section class="work_wrap">` framing `Data Collected` and `Purpose of Processing` (*"S e r v i c e s S e r v i c e s"*) with `#1c1c1b` surface cards, `#f9efe7` accents, and `.lenis-stopped { overflow: clip; }`.
5. **Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.davidecarusio.it/`)**:
   - Landmark `<footer class="footer-wrap">` anchoring `Davide Carusio - Web Designer / ` footer links (`davide carusio · Projects · Services · IT · G e t i n t o u c h`), copy *"G e t i n t o u c h"*, and `#f5ede4` structural dividers.
