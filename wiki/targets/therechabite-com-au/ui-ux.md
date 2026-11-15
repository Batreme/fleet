# UI & UX Architecture: therechabite-com-au

## Overview & Design Identity
- **Target**: `therechabite-com-au` (**The Rechabite • Multi-level Palace of Surprise and Delight**)
- **Production URL**: [https://therechabite.com.au/](https://therechabite.com.au/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#fe2902` accent)
- **Summary**: M e e t M e A t T h e R e c h a b i t e
- **Total Clean CSS Variables Extracted**: `73` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Founders Grotesk Condensed`
- **Body Font Stack**: `Founders Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `1.25em`, `2.25em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: max(18px,1.1vw)`, `line-height: 1`, `font-weight: var(--font-we...`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-body: "Founders Grotesk", sans-serif`
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0f0f0f` | `var(--color-light-black)` in `:root` |
| **Interactive Accent / Highlight** | `#fe2902` | `var(--color-red-hot)` in `:root` |
| **Secondary / Muted Copy** | `#ff8f5f` | `var(--color-peachy)` in `:root` |
| **Structural Hairline Border** | `#9947b7` | `var(--color-light-purple)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25em` | Layout / Spatial Grid Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-tighter` | `-.05em` | Typography / Scale Token |
| `--tracking-normal` | `0em` | Typography / Scale Token |
| `--leading-snug` | `1.375` | Typography / Scale Token |
| `--radius-xs` | `.125rem` | Elevation / Border Token |
| `--radius-sm` | `.25rem` | Elevation / Border Token |
| `--radius-md` | `.375rem` | Elevation / Border Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `therechabite-com-au`)**:
   - Landmark `<header class="pointer-events-none fixed">` hosting `The Rechabite • Multi-level Palace o` navigation (`What’s On What’s On · Rechabite Hall · Hello Rooftop · Double Rainbow · Goodwill Club`), DOM attributes (`data-optimized="1"`, `data-optimized="1"`, `data-optimized="1"`, `data-optimized="1"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `M e e t M e A t T h e R e c h a b `)**:
   - Landmark `<section class="relative flex">` presenting display lead `M e e t M e A t T h e R e c h a b i t e` and copy excerpt *"What’s On What’s On"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `WHAT’S ON`)**:
   - Landmark `<section class="relative bg-light-black">` rendering section `WHAT’S ON` with copy *"Our Spaces Our Spaces Rechabite Hall Hello Rooftop Double Rainbow"*, asset references (`clarity.js`, `z0jl5zt2hc`, `4457171594343694`, `fbevents.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.overflow-hidden> — `Mike Midnight & Deep Creep (US)`)**:
   - Landmark `<section class="overflow-hidden text-white">` framing `Mike Midnight & Deep Creep (US)` and `3 YEARS OF SYBER: PERTH` (*"Our Spaces Our Spaces"*) with `#0f0f0f` surface cards, `#fe2902` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-light-black> — `https://therechabite.com.au/`)**:
   - Landmark `<footer class="bg-light-black text-white">` anchoring `The Rechabite • Multi-level Pala` footer links (`What’s On What’s On · Rechabite Hall · Hello Rooftop · Double Rainbow · Goodwill Club`), copy *"Eat and Drink Eat and Drink Hello Rooftop Double Rainbow Gif"*, and `#9947b7` structural dividers.
