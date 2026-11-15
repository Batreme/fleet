# UI & UX Architecture: north-cloud

## Overview & Design Identity
- **Target**: `north-cloud` (**North - Take control of your cloud costs with AI-powered FinOps - North**)
- **Production URL**: [https://north.cloud](https://north.cloud)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121314` / `#f8fcfd`)
- **Summary**: Manage and optimize cloud, AI, and data spend in one platform. Gain full visibility, automate savings, and eliminate manual FinOps work.
- **Total Clean CSS Variables Extracted**: `181` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Untitled Sans`
- **Body Font Stack**: `Degrad Mono`
- **Monospace / Technical Font Stack**: `Degrad Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.6rem`, `9.6rem`, `100%`, `6.4rem`, `12rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.6rem`, `9.6rem`, `100%`, `6.4rem`, `12rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.6rem`, `9.6rem`, `100%`, `6.4rem`, `12rem`)
- **Metadata & Labels**: CSS variables `--form-label-opacity: .6`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#121314` | `var(--form-inline-submit-bg)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#afb8c2` | `var(--cc-primary-color)` in `:root` |
| **Interactive Accent / Highlight** | `#f8fcfd` | `var(--cc-toggle-on-bg)` in `:root` |
| **Secondary / Muted Copy** | `#d591fe` | `var(--form-error-color)` in `:root` |
| **Structural Hairline Border** | `#f92e21` | `var(--red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--form-inline-field-bg` | `transparent` | Canvas / Surface Token |
| `--form-inline-field-border` | `1px solid #121314` | Elevation / Border Token |
| `--form-inline-submit-bg` | `#121314` | Canvas / Surface Token |
| `--form-inline-submit-color` | `var(--subscribe-accent, #d591fe)` | Brand / Palette Token |
| `--form-inline-h` | `4.8rem` | Dimension / Scale Token |
| `--form-inline-radius` | `8rem` | Elevation / Border Token |
| `--form-inline-pad-x` | `2.4rem` | Layout / Spatial Grid Token |
| `--form-inline-submit-w` | `100%` | Dimension / Scale Token |
| `--form-inline-gap` | `.8rem` | Layout / Spatial Grid Token |
| `--logowall-gap` | `2.4rem` | Layout / Spatial Grid Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--spacing-0` | `0` | Layout / Spatial Grid Token |
| `--spacing-4` | `.4rem` | Layout / Spatial Grid Token |
| `--spacing-15` | `1.5rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `north-cloud`)**:
   - Landmark `<header class="header">` hosting `North - Take control of your cloud c` navigation (`Features · Manage · AI Agent · Coststreams · Analyze`), DOM attributes (`data-theme="black"`, `data-header`, `data-astro-cid-gxxacloy`, `data-dom="desktop-menu"`), and stylesheet rule `before { display:block }`.
2. **Hero Stage & Focal Lead (<section.c-heroHome> — `Contact`)**:
   - Landmark `<section class="c-heroHome heroHome">` presenting display lead `Contact` and copy excerpt *"Features Manage AI Agent Coststreams Analyze Anomalies GreenOps O"* over `#121314` canvas and `#f8fcfd` ink.
3. **Primary Showcase & Content Grid (<section.c-logoWall> — `North`)**:
   - Landmark `<section class="c-logoWall logoWall">` rendering section `North` with copy *"Manage AI Agent Coststreams Analyze Anomalies GreenOps"*, asset references (`untitled-sans-regular.woff2`, `untitled-sans-medium.woff2`, `favicon.ico`, `favicon-180x180.png`), and grid rule `last-of-type { padding-bottom:1.6rem }`.
4. **Interactive Detail & Feature Matrix (<section.c-layer> — `T h e F i n a n c i a l O p e r a `)**:
   - Landmark `<section class="c-layer layer">` framing `T h e F i n a n c i a l O p e r a t i n g S y s t...` and `I n t e l l i g e n c e L a y e r` (*"Optimize Coverage Rightsize Tokenflow"*) with `#afb8c2` surface cards, `#f8fcfd` accents, and `.loaded { background-image:none!important }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://north.cloud`)**:
   - Landmark `<footer class="c-footer footer">` anchoring `North - Take control of your clo` footer links (`Features · Manage · AI Agent · Coststreams · Analyze`), copy *"Integrations AWS GCP Azure All Integrations"*, and `#f92e21` structural dividers.
