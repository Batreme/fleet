# UI & UX Architecture: traced-life

## Overview & Design Identity
- **Target**: `traced-life` (**At-Home Environmental Exposure Test · Traced**)
- **Production URL**: [https://traced.life/](https://traced.life/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f5` accent)
- **Summary**: Trace 15 environmental elements from one strand of hair. A personal 30-day timeline, percentile rankings against a global database, and g...
- **Total Clean CSS Variables Extracted**: `117` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Saans`
- **Body Font Stack**: `Saans Semi Mono`
- **Monospace / Technical Font Stack**: `Saans Semi Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2.5rem`, `line-height: 100%`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.5rem`, `line-height: 110%`)
- **Body Copy**: CSS variables `--oke-bodyText-fontWeight: 400`, `--oke-bodyText-fontSize: var(--oke-text-regular,14px)`, `--oke-bodyText-fontFamily: inherit`; rule `p` (`font-size: 1rem`, `line-height: 120%`)
- **Metadata & Labels**: CSS variables `--font-mono: "Saans Semi Mono",monospace`, `--default-mono-font-family: var(--font-mono)`, `--oke-text-small: 0.75rem`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d9d9d9` | `var(--color-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f5f5` | `var(--color-light)` in `:root` |
| **Secondary / Muted Copy** | `#f8f8f8` | `var(--color-light-70)` in `:root` |
| **Structural Hairline Border** | `#fafafa` | `var(--color-light-50)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Saans",sans-serif` | Typography / Scale Token |
| `--font-serif` | `"Serrif",serif` | Typography / Scale Token |
| `--font-mono` | `"Saans Semi Mono",monospace` | Typography / Scale Token |
| `--spacing` | `0.063rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--radius-lg` | `1.5rem` | Elevation / Border Token |
| `--radius-xl` | `2rem` | Elevation / Border Token |
| `--ease-in` | `cubic-bezier(.4,0,1,1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0,0,.2,1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--aspect-video` | `16/9` | Design System Custom Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.contents> — `traced-life`)**:
   - Landmark `<header class="contents">` hosting `At-Home Environmental Exposure Test ` navigation (`Shop · What we test · Report · Science · Our story`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="70566805578"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `before { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Time leaves traces. Now you can re`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Time leaves traces. Now you can read them.` and copy excerpt *"Learn What we test Report Science Our story Journal FAQs"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `Why Traced?`)**:
   - Landmark `<section class="w-full relative">` rendering section `Why Traced?` with copy *"Traced™ Environmental Exposure Test"*, asset references (`awin-shopify-integration-code.js`, `loader.js`, `sealsubscriptions.js`, `990232790301153`), and grid rule `webkit-file-upload-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.w-full> — `The difference`)**:
   - Landmark `<section class="w-full relative">` framing `The difference` and `How It Works` (*"Nickel contaminants"*) with `#d9d9d9` surface cards, `#f5f5f5` accents, and `file-selector-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.contents> — `https://traced.life/`)**:
   - Landmark `<footer class="contents">` anchoring `At-Home Environmental Exposure T` footer links (`Shop · What we test · Report · Science · Our story`), copy *"Trace your exposures"*, and `#fafafa` structural dividers.
