# UI & UX Architecture: ciuslabs-com

## Overview & Design Identity
- **Target**: `ciuslabs-com` (**CIUSLABS — Independent Product Lab for Apps & AI Tools**)
- **Production URL**: [https://ciuslabs.com/](https://ciuslabs.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#008b66`)
- **Summary**: We design, build and run our own mobile apps and AI tools, and co-build with a few founders a year: one squad, from first sketch to a pro...
- **Total Clean CSS Variables Extracted**: `460` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `appFont`
- **Body Font Stack**: `appFont Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--ds-text-h1-size: 48px`, `--ds-text-h1-line: 52px`, `--ds-text-h1-weight: 500`; rule `h1` (`font-size: 40px`, `line-height: 1.05`, `letter-spacing: -.035em`)
- **Section Heading (`H2`)**: CSS variables `--ds-text-h2-size: 36px`, `--ds-text-h2-line: 40px`, `--ds-text-h2-weight: 500`; rule `h2` (`font-size: 32px`, `line-height: 1.1`, `letter-spacing: -.025em`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--ds-text-body-size: 16px`; rule `p` (`line-height: 18px`)
- **Metadata & Labels**: CSS variables `--font-mono: var(--ds-font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#797e7e` | `var(--ds-mark-subtle)` in `:root` |
| **Interactive Accent / Highlight** | `#008b66` | `var(--ds-success)` in `:root` |
| **Secondary / Muted Copy** | `#003d2b` | `var(--ds-success-text)` in `:root` |
| **Structural Hairline Border** | `#f9b649` | `var(--ds-warning)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--ds-font-sans)` | Typography / Scale Token |
| `--font-mono` | `var(--ds-font-mono)` | Typography / Scale Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-500` | `oklch(55.1% .027 264.364)` | Brand / Palette Token |
| `--color-zinc-100` | `oklch(96.7% .001 286.375)` | Brand / Palette Token |
| `--color-zinc-200` | `oklch(92% .004 286.32)` | Brand / Palette Token |
| `--color-zinc-700` | `oklch(37% .013 285.805)` | Brand / Palette Token |
| `--color-zinc-900` | `oklch(21% .006 285.885)` | Brand / Palette Token |
| `--color-neutral-200` | `oklch(92.2% 0 none)` | Brand / Palette Token |
| `--color-neutral-950` | `oklch(14.5% 0 none)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xs` | `20rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.flex> — `ciuslabs-com`)**:
   - Landmark `<header class="flex shrink-0">` hosting `CIUSLABS — Independent Product Lab f` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-brand="ciuslabs"`, `data-theme="light"`, `data-redirect-timezone="1"`, `data-scroll-behavior="smooth"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.hero-section> — `Designing, building and running th`)**:
   - Landmark `<section class="hero-section relative">` presenting display lead `Designing, building and running the products we own.` and copy excerpt *"Skip to main content"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.stats-section> — `One line takes an idea from first `)**:
   - Landmark `<section class="stats-section relative">` rendering section `One line takes an idea from first question to liv...` with copy *"Products P r o d u c t s"*, asset references (`Logo.svg`, `horus.svg`, `ae4eeb438964a460.css`, `344affef6ccd7e28.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Discover`)**:
   - Landmark `<section class="relative w-full">` framing `Discover` and `Architect` (*"Pricing P r i c i n g"*) with `#797e7e` surface cards, `#008b66` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://ciuslabs.com/`)**:
   - Landmark `<footer class="relative w-full">` anchoring `CIUSLABS — Independent Product L` footer links (`Overview · Index · Archive · About · Contact`), copy *"Contact C o n t a c t"*, and `#f9b649` structural dividers.
