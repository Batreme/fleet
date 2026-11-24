---
title: "UI & UX Architecture: www-thecandyvault-com-au"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-thecandyvault-com-au

## Overview & Design Identity
- **Target**: `www-thecandyvault-com-au` (**The Candy Vault · Buy Sweets Online · Australia**)
- **Production URL**: [https://www.thecandyvault.com.au/](https://www.thecandyvault.com.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: Shop delicious lollies, chocolates and sweet treats online at The Candy Vault. Discover a colourful range of favourites delivered across...
- **Total Clean CSS Variables Extracted**: `2102` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `bricolage-grotesque`
- **Body Font Stack**: `wfont_e0cabf_4a14a20dcc7e4329bafffebe1c...`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 112.5px`, `line-height: 112.5px`, `font-weight: 700`, `letter-spacing: -3.375px`); CSS variables `--display: inline-block`, `--wbu-heading-h1-font-size: 32px`, `--wbu-heading-h1-line-height: 40px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 33.75px`, `line-height: 43.875px`, `font-weight: 400`); CSS variables `--wst-font-style-h2: var(--font_2)`, `--wbu-heading-h2-font-size: 24px`, `--wbu-heading-h2-line-height: 32px`
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`, `--wbu-text-small-size: 12px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#cccccc` | `.eTBpzs:before { background-color: #cccccc }` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#f1c1db` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#5e97ff` | `var(--stroke)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--one-unit` | `1vw` | Dimension / Scale Token |
| `--section-max-width` | `9999px` | Layout / Spatial Grid Token |
| `--spx-stopper-max` | `9999px` | Dimension / Scale Token |
| `--spx-stopper-min` | `0px` | Dimension / Scale Token |
| `--browser-zoom` | `1` | Design System Custom Token |
| `--wst-button-color-fill-primary` | `rgb(var(--color_48))` | Brand / Palette Token |
| `--wst-button-color-border-primary` | `rgb(var(--color_49))` | Brand / Palette Token |
| `--wst-button-color-text-primary` | `rgb(var(--color_50))` | Typography Ink Token |
| `--wst-button-color-fill-primary-hover` | `rgb(var(--color_51))` | Brand / Palette Token |
| `--wst-button-color-border-primary-hover` | `rgb(var(--color_52))` | Brand / Palette Token |
| `--wst-button-color-text-primary-hover` | `rgb(var(--color_53))` | Typography Ink Token |
| `--wst-button-color-fill-primary-disabled` | `rgb(var(--color_54))` | Brand / Palette Token |
| `--wst-button-color-border-primary-disabled` | `rgb(var(--color_55))` | Brand / Palette Token |
| `--wst-button-color-text-primary-disabled` | `rgb(var(--color_56))` | Typography Ink Token |
| `--wst-button-color-fill-secondary` | `rgb(var(--color_57))` | Brand / Palette Token |
| `--wst-button-color-border-secondary` | `rgb(var(--color_58))` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.comp-kbgakxea> — `www-thecandyvault-com-au`)**:
   - Landmark `<header class="comp-kbgakxea S829f_">` (`1440x101px`) hosting `The Candy Vault · Buy Sweets Online ` navigation (`Home · All Products · Gummies & Jellies · Sour & Fizzy · Straps & Cables`), DOM attributes (`data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `Fancy a sweet raid?`)**:
   - Landmark `<section class="ke5pl1 comp-mu3xtrpz">` presenting display lead `Fancy a sweet raid?` and copy excerpt *"Christmas has arrived at The Candy Vault!"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.comp-mu19a2q3> — `Explore our collection of old favo`)**:
   - Landmark `<section class="ke5pl1 comp-mu19a2q3">` rendering section `Explore our collection of old favourites, new dis...` with copy *"Too Sweet to Spook"*, asset references (`f415e2_d11d56bae7454bc98dfbe3e86d...`, `minified.js`, `focus-within-polyfill.js`, `www.thecandyvault.com.au`), and grid rule `root::view-transition { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.comp-mu43swgv-container> — `Too Sweet to Spook`)**:
   - Landmark `<section class="ke5pl1 comp-mu43swgv-container">` framing `Too Sweet to Spook` and `What Are You Craving?` (*"Get ready for little monsters at the door with our collection of "*) with `#cccccc` surface cards, `#0000ee` accents, and `SITE_HEADER { view-transition-name:header-group }`.
5. **Colophon & Global Directory Footer (<footer.comp-mu93k1t9> — `https://www.thecandyvault.com.au/`)**:
   - Landmark `<footer class="comp-mu93k1t9 S829f_">` anchoring `The Candy Vault · Buy Sweets Onl` footer links (`Home · All Products · Gummies & Jellies · Sour & Fizzy · Straps & Cables`), copy *"Stock Up for Halloween"*, and `#5e97ff` structural dividers.
