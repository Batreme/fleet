# UI & UX Architecture: sincro-es_en-us

## Overview & Design Identity
- **Target**: `sincro-es_en-us` (**Us - Sincro**)
- **Production URL**: [https://sincro.es/en/us/](https://sincro.es/en/us/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#36f` accent)
- **Summary**: Navigating complexity together
- **Total Clean CSS Variables Extracted**: `133` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Schibsted Grotesk`
- **Body Font Stack**: `AtAero Retina`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-bodyCaption)`, `var(--text-bodyL)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--text-bodyMobM,.9375rem)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy**: CSS variables `--text-base: 100%`, `--text-base--line-height: normal`, `--text-bodyTagline: 5.5rem`; rule `p` (`font-size: var(--text-bodyMobS,.8125rem)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Metadata & Labels**: CSS variables `--text-sm: .75rem`, `--text-sm--line-height: 1.25`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff7cc1` | `var(--color-pink)` in `:root` |
| **Interactive Accent / Highlight** | `#36f` | `var(--color-blue)` in `:root` |
| **Secondary / Muted Copy** | `#0040ff` | `var(--color-vividBlueHover)` in `:root` |
| **Structural Hairline Border** | `#081423` | `var(--color-darkBlue)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.75rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.25` | Typography Ink Token |
| `--text-base` | `100%` | Typography Ink Token |
| `--text-base--line-height` | `normal` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--tracking-wide` | `.025em` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--radius-xs` | `.125rem` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `sincro-es_en-us`)**:
   - Landmark `<header class="fixed top-0">` hosting `Us - Sincro` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-8de50b09`, `data-swiper-slide-index="0"`, `data-swiper-slide-index="1"`, `data-swiper-slide-index="2"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<main.relative> — `20 years of being who we say we ar`)**:
   - Landmark `<main class="relative flex">` presenting display lead `20 years of being who we say we are` and copy excerpt *"Tax and Accounting"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.relative> — `UNE Standard`)**:
   - Landmark `<main class="relative flex">` rendering section `UNE Standard` with copy *"Navigating complexity together"*, asset references (`entry.BcfY3otZ.css`, `Media.DbUUtcYg.css`, `PageBuilder.D9iVxonM.css`, `SchibstedGrotesk-Regular.woff2`), and grid rule `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`.
4. **Interactive Detail & Feature Matrix (<main.relative> — `Our values`)**:
   - Landmark `<main class="relative flex">` framing `Our values` and `Driven by and for the people` (*"Our expertise Services"*) with `#ff7cc1` surface cards, `#36f` accents, and `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://sincro.es/en/us/`)**:
   - Landmark `<footer class="border-t border-mediumGrey">` anchoring `Us - Sincro` footer links (`Overview · Index · Archive · About · Contact`), copy *"We aim to be the strategic partner that brings excellence, t"*, and `#081423` structural dividers.
