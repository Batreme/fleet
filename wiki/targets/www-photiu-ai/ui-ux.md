# UI & UX Architecture: www-photiu-ai

## Overview & Design Identity
- **Target**: `www-photiu-ai` (**Remove Background, Upscale & Erase Objects – Photiu.ai**)
- **Production URL**: [https://www.photiu.ai](https://www.photiu.ai)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f9f9` canvas, `#000000` ink, `#000000` accent)
- **Summary**: Discover Photiu.ai's AI tools: remove backgrounds, upscale images, and erase unwanted objects. Achieve stunning photo edits online quickl...
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roboto`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.875rem`, `line-height: 2.25rem`, `font-weight: 700`)
- **Body Copy**: rule `p` (`line-height: 1.625`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f9f9` | `var(--board-black-color)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--termly-theme-background-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#003afa` | `var(--termly-theme-button-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--termly-theme-color)` in `:root` |
| **Secondary / Muted Copy** | `#e5e7eb` | `:before { border: #e5e7eb }` |
| **Structural Hairline Border** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-width` | `1200px` | Layout / Spatial Grid Token |
| `--header-h` | `80px` | Layout / Spatial Grid Token |
| `--header-h-sm` | `60px` | Layout / Spatial Grid Token |
| `--footer-h` | `200px` | Dimension / Scale Token |
| `--board-black-color` | `#f8f9f9` | Canvas / Surface Token |
| `--board-white-color` | `transparent` | Canvas / Surface Token |
| `--termly-prompt-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--termly-theme-background-color` | `#ffffff` | Canvas / Surface Token |
| `--termly-theme-button-background-color` | `#003afa` | Canvas / Surface Token |
| `--termly-theme-button-text-color` | `#ffffff` | Typography Ink Token |
| `--termly-theme-color` | `#000000` | Brand / Palette Token |
| `--termly-theme-font-family` | `Roboto, "Open Sans", Arial, Helvetica` | Brand / Palette Token |
| `--termly-theme-font-size` | `12px` | Brand / Palette Token |
| `--termly-z-index` | `var(--termly-override-z-index, 999999)` | Elevation / Border Token |
| `--www-photiu-ai-bg` | `#f8f9f9` | Canvas Substrate (from `var(--board-black-color)` in `:root`) |
| `--www-photiu-ai-ink` | `#000000` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.hidden> — `www-photiu-ai`)**:
   - Landmark `<nav class="hidden">` hosting `Remove Background, Upscale & Erase O` navigation (`Pricing · Blog · feedback`), DOM attributes (`data-precedence="next"`, `data-termly-part="consent-banner"`, `data-termly-position="bottom"`, `data-termly-size="compact"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.w-full> — `Remove background`)**:
   - Landmark `<section class="w-full">` presenting display lead `Remove background` and copy excerpt *"Remove Background Remove Background Instantly remove the backgrou"* over `#f8f9f9` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `Remove backgrounds instantly with `)**:
   - Landmark `<section class="w-full">` rendering section `Remove backgrounds instantly with just one click!` with copy *"Remove Background Instantly remove the background of your photos."*, asset references (`gtm.js`, `eTI4g9fAtUixpHto8YooHCfeUPdUHEz0P...`, `3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5`, `www.googletagmanager.com`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.w-full> — `HD Background Removal`)**:
   - Landmark `<section class="w-full">` framing `HD Background Removal` and `Erase Freely, Cut Perfectly` (*"Instantly remove the background of your photos."*) with `#003afa` surface cards, `#000000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://www.photiu.ai`)**:
   - Landmark `<footer class="flex w-full">` anchoring `Remove Background, Upscale & Era` footer links (`Pricing · Blog · feedback`), copy *"Image Upscale Effortlessly enhance your image quality."*, and `#9ca3af` structural dividers.
