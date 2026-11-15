# UI & UX Architecture: ross-oneill-com

## Overview & Design Identity
- **Target**: `ross-oneill-com` (**Ross O'Neill · Freelance Web Developer and Designer in Perth**)
- **Production URL**: [https://ross-oneill.com/](https://ross-oneill.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f7` accent)
- **Summary**: Freelance web developer and designer in North Beach, Perth. Fast custom websites for WA businesses, built and looked after by the person...
- **Total Clean CSS Variables Extracted**: `360` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--color-body: var(--color-gray-600)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#da0a2c` | `var(--color-accent)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f5f7` | `var(--color-offwhite)` in `:root` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#ffffff` | `:disabled:checked:after { background-color: white }` (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-200` | `oklch(88.5% .062 18.334)` | Brand / Palette Token |
| `--color-red-300` | `oklch(80.8% .114 19.571)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-red-900` | `oklch(39.6% .141 25.723)` | Brand / Palette Token |
| `--color-red-950` | `oklch(25.8% .092 26.042)` | Brand / Palette Token |
| `--color-orange-50` | `oklch(98% .016 73.684)` | Brand / Palette Token |
| `--color-orange-100` | `oklch(95.4% .038 75.164)` | Brand / Palette Token |
| `--color-orange-200` | `oklch(90.1% .076 70.697)` | Brand / Palette Token |
| `--color-orange-300` | `oklch(83.7% .128 66.29)` | Brand / Palette Token |
| `--color-orange-400` | `oklch(75% .183 55.934)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header-content> — `ross-oneill-com`)**:
   - Landmark `<header class="header-content fixed">` hosting `Ross O'Neill · Freelance Web Develop` navigation (`About Me · Plans · Work · Blog · Get in Touch`), DOM attributes (`data-astro-exec`, `data-cfasync="false"`, `data-icon="carbon:arrow-right"`, `data-icon="carbon:arrow-right"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `Ross O'Neill, a Perth-based web de`)**:
   - Landmark `<section class="bg-white py-28">` presenting display lead `Ross O'Neill, a Perth-based web developer who tra...` and copy excerpt *"Ross O'Neill, a Perth-based web developer who transforms designs "* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Margaret River Region`)**:
   - Landmark `<section class="bg-white pb-12">` rendering section `Margaret River Region` with copy *"Swipe to See Full Portfolio"*, asset references (`favicon.ico`, `favicon.svg`, `sitemap-index.xml`, `static.cloudflareinsights.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Capes Foundation`)**:
   - Landmark `<section class="relative py-12">` framing `Capes Foundation` and `CMEWA` (*"See Full Portfolio"*) with `#da0a2c` surface cards, `#f5f5f7` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://ross-oneill.com/`)**:
   - Landmark `<footer class="relative text-white">` anchoring `Ross O'Neill · Freelance Web Dev` footer links (`About Me · Plans · Work · Blog · Get in Touch`), copy *"Margaret River Region"*, and `#ffffff` structural dividers.
