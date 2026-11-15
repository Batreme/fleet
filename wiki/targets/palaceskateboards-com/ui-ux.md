# UI & UX Architecture: palaceskateboards-com

## Overview & Design Identity
- **Target**: `palaceskateboards-com` (**PALACE SKATEBOARDS**)
- **Production URL**: [https://palaceskateboards.com/](https://palaceskateboards.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#e4e4e4`)
- **Summary**: GULLY SH*T
- **Total Clean CSS Variables Extracted**: `81` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Helvetica W01`
- **Body Font Stack**: `Helvetica Neue LT Std Condensed`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2.25rem`, `font-weight: 700`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 60px`, `--text-2xl--line-height: 60px`, `--text-3xl: 72px`; rule `h2` (`font-size: 1.5rem`, `font-weight: 700`)
- **Body Copy**: CSS variables `--text-base: 16px`, `--text-base--line-height: 16px`; rule `p` (`font-size: .875rem`, `line-height: 1.625`)
- **Metadata & Labels**: CSS variables `--text-xs: 10px`, `--text-xs--line-height: 10px`, `--text-sm: 12px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f5f5f5` | `var(--color-grey-050)` in `:root` |
| **Interactive Accent / Highlight** | `#e4e4e4` | `var(--color-grey-100)` in `:root` |
| **Secondary / Muted Copy** | `#c4c4c4` | `var(--color-grey-250)` in `:root` |
| **Structural Hairline Border** | `#9a9a9a` | `var(--color-grey-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--text-xs` | `10px` | Typography Ink Token |
| `--text-xs--line-height` | `10px` | Typography Ink Token |
| `--text-sm` | `12px` | Typography Ink Token |
| `--text-sm--line-height` | `12px` | Typography Ink Token |
| `--text-base` | `16px` | Typography Ink Token |
| `--text-base--line-height` | `16px` | Typography Ink Token |
| `--text-lg` | `32px` | Typography Ink Token |
| `--text-lg--line-height` | `32px` | Typography Ink Token |
| `--text-xl` | `45px` | Typography Ink Token |
| `--text-xl--line-height` | `45px` | Typography Ink Token |
| `--text-2xl` | `60px` | Typography Ink Token |
| `--text-2xl--line-height` | `60px` | Typography Ink Token |
| `--text-3xl` | `72px` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `palaceskateboards-com`)**:
   - Landmark `<header class="fixed pointer-events-none">` hosting `PALACE SKATEBOARDS` navigation (`Web Shop · Shops · Advice · Cart`), DOM attributes (`data-application="hydrogen"`, `data-shop-id="3053289"`, `data-storefront-id="1000010054"`, `data-monorail-region="global"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.min-h-dvh> — `PALACE LONDON`)**:
   - Landmark `<main class="min-h-dvh flex">` presenting display lead `PALACE LONDON` and copy excerpt *"PALACE LIVING PROOF"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.min-h-dvh> — `PALACE LIVING PROOF`)**:
   - Landmark `<main class="min-h-dvh flex">` rendering section `PALACE LIVING PROOF` with copy *"PALACE NIKE MANOR PLACE"*, asset references (`favicon.svg`, `neue-helvetica-w01-v2-Del-pFKJ.woff2`, `neue-helvetica-w01-CykExj90.woff2`, `cdn.shopify.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.min-h-dvh> — `PALACE NIKE MANOR PLACE`)**:
   - Landmark `<main class="min-h-dvh flex">` framing `PALACE NIKE MANOR PLACE` and `WINTER 2026 RANGE` (*"Delivery Information"*) with `#f5f5f5` surface cards, `#e4e4e4` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://palaceskateboards.com/`)**:
   - Landmark `<footer class="relative z-1">` anchoring `PALACE SKATEBOARDS` footer links (`Web Shop · Shops · Advice · Cart`), copy *"Returns Information"*, and `#9a9a9a` structural dividers.
