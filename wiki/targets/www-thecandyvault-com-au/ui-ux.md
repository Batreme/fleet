# UI & UX Architecture: www-thecandyvault-com-au

## Overview & Design Identity
- **Target**: `www-thecandyvault-com-au` (**The Candy Vault · Buy Sweets Online · Australia**)
- **Production URL**: [https://www.thecandyvault.com.au/](https://www.thecandyvault.com.au/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0f2ccf` canvas, `#eaefff` ink, `#acbeff` accent)
- **Summary**: Shop delicious lollies, chocolates and sweet treats online at The Candy Vault. Discover a colourful range of favourites delivered across...
- **Total Clean CSS Variables Extracted**: `2102` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `wf_4a14a20dcc7e4329bafffebe1`
- **Body Font Stack**: `bricolage-grotesque`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--display: inline-block`, `--wbu-heading-h1-font-size: 32px`, `--wbu-heading-h1-line-height: 40px`
- **Section Heading (`H2`)**: CSS variables `--wst-color-subtitle: rgb(var(--color_46))`, `--wst-font-style-h2: var(--font_2)`, `--wbu-heading-h2-font-size: 24px`
- **Body Copy**: CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`
- **Metadata & Labels**: CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`, `--wbu-text-small-size: 12px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0f2ccf` | `var(--wbu-color-blue-0)` in `:root` |
| **Primary Typography Ink** | `#2f5dff` | `var(--wbu-color-blue-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#597dff` | `var(--wbu-color-blue-200)` in `:root` |
| **Interactive Accent / Highlight** | `#acbeff` | `var(--wbu-color-blue-300)` in `:root` |
| **Secondary / Muted Copy** | `#d5dfff` | `var(--wbu-color-blue-400)` in `:root` |
| **Structural Hairline Border** | `#eaefff` | `var(--wbu-color-blue-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--one-unit` | `1vw` | Dimension / Scale Token |
| `--section-max-width` | `9999px` | Layout / Spatial Grid Token |
| `--spx-stopper-max` | `9999px` | Dimension / Scale Token |
| `--spx-stopper-min` | `0px` | Dimension / Scale Token |
| `--browser-zoom` | `1` | Design System Custom Token |
| `--safari-sticky-fix` | `opacity` | Design System Custom Token |
| `--experimental-safari-sticky-fix` | `translateZ(0)` | Design System Custom Token |
| `--wst-button-color-fill-primary` | `rgb(var(--color_48))` | Brand / Palette Token |
| `--wst-button-color-border-primary` | `rgb(var(--color_49))` | Brand / Palette Token |
| `--wst-button-color-text-primary` | `rgb(var(--color_50))` | Typography Ink Token |
| `--wst-button-color-fill-primary-hover` | `rgb(var(--color_51))` | Brand / Palette Token |
| `--wst-button-color-border-primary-hover` | `rgb(var(--color_52))` | Brand / Palette Token |
| `--wst-button-color-text-primary-hover` | `rgb(var(--color_53))` | Typography Ink Token |
| `--wst-button-color-fill-primary-disabled` | `rgb(var(--color_54))` | Brand / Palette Token |
| `--wst-button-color-border-primary-disabled` | `rgb(var(--color_55))` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.comp-kbgakxea> — `www-thecandyvault-com-au`)**:
   - Landmark `<header class="comp-kbgakxea S829f_">` hosting `The Candy Vault · Buy Sweets Online ` navigation (`Home · All Products · Gummies & Jellies · Sour & Fizzy · Straps & Cables`), DOM attributes (`data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `Fancy a sweet raid?`)**:
   - Landmark `<section class="ke5pl1 comp-kbgakxea_r_comp-kbgajy18">` presenting display lead `Fancy a sweet raid?` and copy excerpt *"Skip to Main Content"* over `#0f2ccf` canvas and `#eaefff` ink.
3. **Primary Showcase & Content Grid (<section.ke5pl1> — `Explore our collection of old favo`)**:
   - Landmark `<section class="ke5pl1 comp-mu3xtrpz">` rendering section `Explore our collection of old favourites, new dis...` with copy *"Shop All Products Gummies & Jellies Sour & Fizzy Straps & Cables "*, asset references (`f415e2_d11d56bae7454bc98dfbe3e86d...`, `bundle.tracing.es5.min.js`, `minified.js`, `focus-within-polyfill.js`), and grid rule `root::view-transition { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.ke5pl1> — `Too Sweet to Spook`)**:
   - Landmark `<section class="ke5pl1 comp-mu19a2q3">` framing `Too Sweet to Spook` and `What Are You Craving?` (*"Lollipops & Individually Wrapped"*) with `#597dff` surface cards, `#acbeff` accents, and `SITE_HEADER { view-transition-name:header-group }`.
5. **Colophon & Global Directory Footer (<footer.comp-mu93k1t9> — `https://www.thecandyvault.com.au/`)**:
   - Landmark `<footer class="comp-mu93k1t9 S829f_">` anchoring `The Candy Vault · Buy Sweets Onl` footer links (`Home · All Products · Gummies & Jellies · Sour & Fizzy · Straps & Cables`), copy *"30% off Black Friday ✦ Stay Tuned ✦"*, and `#eaefff` structural dividers.
