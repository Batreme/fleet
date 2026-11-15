# UI & UX Architecture: patmos-studio

## Overview & Design Identity
- **Target**: `patmos-studio` (**Patmos · Wahr, Gut, Schön**)
- **Production URL**: [https://patmos.studio/](https://patmos.studio/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#8f8f8f` accent)
- **Summary**: A Gestalting™ practice at the intersection of business and art. Across strategy, organization, branding, design, marketing, product, arch...
- **Total Clean CSS Variables Extracted**: `72` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Patmos Serif`
- **Body Font Stack**: `Noto Sans JP`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-weight: 300`)
- **Section Heading (`H2`)**: rule `h2` (`line-height: 1.6!important`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--spacing-14-16)`, `var(--spacing-16-20)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--spacing-14-16)`, `var(--spacing-16-20)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-bg)` in `:root` |
| **Primary Typography Ink** | `#f5f5f5` | `var(--color-bg-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-fg)` in `:root` |
| **Interactive Accent / Highlight** | `#8f8f8f` | `var(--color-fg-muted)` in `:root` |
| **Secondary / Muted Copy** | `#ddd` | `var(--color-fg-muted-strong)` in `:root` |
| **Structural Hairline Border** | `#787878` | `var(--color-neutral)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cols` | `var(--_cols)` | Layout / Spatial Grid Token |
| `--header-height` | `18rem` | Layout / Spatial Grid Token |
| `--mt` | `var(--_mt)` | Design System Custom Token |
| `--span` | `var(--_span)` | Design System Custom Token |
| `--start` | `var(--_start)` | Design System Custom Token |
| `--spacing` | `.0625rem` | Layout / Spatial Grid Token |
| `--spacing-base` | `.9375rem` | Layout / Spatial Grid Token |
| `--spacing-10-11` | `clamp(.625rem,.6016rem + .0935vw,.6875rem)` | Layout / Spatial Grid Token |
| `--spacing-12-13` | `clamp(.75rem,.7266rem + .0935vw,.8125rem)` | Layout / Spatial Grid Token |
| `--spacing-14-16` | `clamp(.875rem,.8283rem + .1869vw,1rem)` | Layout / Spatial Grid Token |
| `--spacing-14-17` | `clamp(.875rem,.8049rem + .2831vw,1.0625rem)` | Layout / Spatial Grid Token |
| `--spacing-15-16` | `clamp(.9375rem,.9141rem + .0935vw,1rem)` | Layout / Spatial Grid Token |
| `--spacing-16-17` | `clamp(1rem,.9765rem + .0935vw,1.0625rem)` | Layout / Spatial Grid Token |
| `--spacing-16-18` | `clamp(1rem,.9533rem + .1869vw,1.125rem)` | Layout / Spatial Grid Token |
| `--spacing-16-19` | `clamp(1rem,.9299rem + .2804vw,1.1875rem)` | Layout / Spatial Grid Token |
| `--spacing-16-20` | `clamp(1rem,.374vw + .907rem,1.25rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.visible> — `patmos-studio`)**:
   - Landmark `<nav class="visible fixed">` hosting `Patmos · Wahr, Gut, Schön` navigation (`Home · Prologue · Episode · Scene · Epilogue`), DOM attributes (`data-typeface="serif"`, `data-path="/contact/"`, `data-path="/"`, `data-path="/prologue/"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.row-span-full> — `( Patmos ) Wahr, Gut, Schön`)**:
   - Landmark `<main class="row-span-full">` presenting display lead `( Patmos ) Wahr, Gut, Schön` and copy excerpt *"Loading complete. Choose whether to play sound."* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.row-span-full> — `Loading complete. Choose whether t`)**:
   - Landmark `<main class="row-span-full">` rendering section `Loading complete. Choose whether to play sound.` with copy *"Praksis of Gestalting"*, asset references (`dlr2ezd.js`, `favicon.svg`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.row-span-full> — `Praksis of Gestalting`)**:
   - Landmark `<main class="row-span-full">` framing `Praksis of Gestalting` and `( Das Wahre, Gute, Schöne )` (*"( Das Wahre, Gute, Schöne )"*) with `#000` surface cards, `#8f8f8f` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.swup-enabled> — `https://patmos.studio/`)**:
   - Landmark `<footer class="swup-enabled">` anchoring `Patmos · Wahr, Gut, Schön` footer links (`Home · Prologue · Episode · Scene · Epilogue`), copy *"Praksis of Gestalting"*, and `#787878` structural dividers.
