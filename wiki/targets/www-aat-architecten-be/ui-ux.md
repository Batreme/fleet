# UI & UX Architecture: www-aat-architecten-be

## Overview & Design Identity
- **Target**: `www-aat-architecten-be` (**AAT Architecten**)
- **Production URL**: [https://www.aat-architecten.be/](https://www.aat-architecten.be/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#ababab` accent)
- **Summary**: Architectenbureau uit Turnhout (Antwerpen), actief in een ruimer gebied. Architectuurprojecten voor openbare besturen, scholen en bedrijv...
- **Total Clean CSS Variables Extracted**: `148` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Suisse Intl`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--h1-size: clamp(32px, 3vw + 1.5rem, 72px)`
- **Section Heading (`H2`)**: CSS variables `--h2-size: clamp(28px, 2.2vw + 1.2rem, 48px)`; rule `h2` (`font-size: var(--h4-size)!important`, `font-weight: var(--font-we...`)
- **Body Copy**: rule `p` (`font-size: var(--text-13)`, `line-height: 1`)
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1d1d1b` | `var(--color-black-500)` in `:root` |
| **Interactive Accent / Highlight** | `#ababab` | `var(--color-grey-500)` in `:root` |
| **Secondary / Muted Copy** | `#ddd` | `var(--color-grey-300)` in `:root` |
| **Structural Hairline Border** | `#93c572` | `var(--color-alert-green-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-green-500` | `oklch(72.3% .219 149.579)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |
| `--color-blue-600` | `oklch(54.6% .245 262.881)` | Brand / Palette Token |
| `--color-gray-50` | `oklch(98.5% .002 247.839)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% .01 258.338)` | Brand / Palette Token |
| `--color-gray-500` | `oklch(55.1% .027 264.364)` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |
| `--color-gray-700` | `oklch(37.3% .034 259.733)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--breakpoint-sm` | `576px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-wrapper__row> — `www-aat-architecten-be`)**:
   - Landmark `<header class="site-wrapper__row site-wrapper__row--header">` hosting `AAT Architecten` navigation (`Projecten · Over · Contact`), DOM attributes (`data-lenis-prevent`, `data-split="heading"`, `data-duration="1.6"`, `data-stagger="0.18"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.header> — `Wij ontwerpen gebouwen die werken `)**:
   - Landmark `<section class="header js-header">` presenting display lead `Wij ontwerpen gebouwen die werken voor publieke r...` and copy excerpt *"info@aat-architecten.be"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.home-intro-block> — `Projecten`)**:
   - Landmark `<section class="home-intro-block mb-g">` rendering section `Projecten` with copy *"Wij ontwerpen gebouwen die werken voor"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.block-featured-projects> — `Wij ontwerpen gebouwen die werken `)**:
   - Landmark `<section class="block-featured-projects block-featured-projects--first">` framing `Wij ontwerpen gebouwen die werken voor` and `publieke ruimtes, scholen en bedrijven, en` (*"publieke ruimtes, scholen en bedrijven, en"*) with `#1d1d1b` surface cards, `#ababab` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.mobile-nav__footer> — `https://www.aat-architecten.be/`)**:
   - Landmark `<footer class="mobile-nav__footer">` anchoring `AAT Architecten` footer links (`Projecten · Over · Contact`), copy *"vertrekken daarbij steeds van de ruimte"*, and `#93c572` structural dividers.
