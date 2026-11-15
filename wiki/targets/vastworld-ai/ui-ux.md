# UI & UX Architecture: vastworld-ai

## Overview & Design Identity
- **Target**: `vastworld-ai` (**VAST-A global Leading AI Company**)
- **Production URL**: [https://vastworld.ai/](https://vastworld.ai/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#7a5a12`)
- **Summary**: VAST-A global Leading AI Company
- **Total Clean CSS Variables Extracted**: `140` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Saans VF`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: calc(var(--txt-4xl) * var(--u))`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: calc(var(--txt-5xl) * var(--u))`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: calc(var(--txt-3xl) * var(--u))`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--lh-body: 1.35`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0006` | `var(--ds-dim)` in `:root` |
| **Interactive Accent / Highlight** | `#7a5a12` | `var(--ds-accent-gold)` in `:root` |
| **Secondary / Muted Copy** | `#FFFFFF` | `var(--navbar-ink-light)` in `:root` |
| **Structural Hairline Border** | `#000000` | `var(--navbar-ink-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-neutral-400` | `oklch(70.8% 0 none)` | Brand / Palette Token |
| `--color-neutral-900` | `oklch(20.5% 0 none)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `calc(4 * var(--u))` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75 / 1.125)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `vastworld-ai`)**:
   - Landmark `<header class="fixed z-30">` hosting `VAST-A global Leading AI Company` navigation (`Home · Research · Universe · Product · About`), DOM attributes (`data-barba="wrapper"`, `data-root`, `data-stats-panels-wrapper`, `data-barba="container"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.pb-16> — `B u i l d Y o u r W o r l d s`)**:
   - Landmark `<section class="pb-16 relative">` presenting display lead `B u i l d Y o u r W o r l d s` and copy excerpt *"Try Tripo Try Tripo Try Tripo"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.group> — `V A S T - A G l o b a l L e a d i `)**:
   - Landmark `<article class="group flex">` rendering section `V A S T - A G l o b a l L e a d i n g A I C o m p...` with copy *"V A S T - A G l o b a l"*, asset references (`InstrumentSans-variable-latin.woff2`, `favicon.ico`, `apple-touch-icon.png`, `page-wrapper.BKmYtgLc.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.group> — `B u i l t o n R e s e a r c h`)**:
   - Landmark `<article class="group flex">` framing `B u i l t o n R e s e a r c h` and `F r o m A s s e t s t o W o r l d s` (*"L e a d i n g A I C o m p a n y"*) with `#0006` surface cards, `#7a5a12` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.pointer-events-none> — `https://vastworld.ai/`)**:
   - Landmark `<footer class="pointer-events-none w-full">` anchoring `VAST-A global Leading AI Company` footer links (`Home · Research · Universe · Product · About`), copy *"Believing that 3D is the native form of the world, VAST turn"*, and `#000000` structural dividers.
