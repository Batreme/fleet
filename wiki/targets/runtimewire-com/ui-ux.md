# UI & UX Architecture: runtimewire-com

## Overview & Design Identity
- **Target**: `runtimewire-com` (**RuntimeWire: Breaking tech news. Before everyone else.**)
- **Production URL**: [https://runtimewire.com](https://runtimewire.com)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#000000` accent)
- **Summary**: Breaking tech news. Before everyone else. Independent investigations, original reporting and a continuous news feed covering startups and...
- **Total Clean CSS Variables Extracted**: `209` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.028em!important`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`letter-spacing: .09em`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: CSS variables `--font-mono: var(--app-font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`; rule `small` (`font-size: 12px`, `line-height: 1.45`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `textarea { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#000000` | `.border-black { border-color: black }` (`#000000`) |
| **Secondary / Muted Copy** | `#0003` | `20 { border-color: #0003 }` |
| **Structural Hairline Border** | `#0000ff` | `20 { border-color: blue }` (`#0000ff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pro-ring-angle` | `0deg` | Elevation / Border Token |
| `--font-mono` | `var(--app-font-mono)` | Typography / Scale Token |
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-300` | `oklch(80.8% .114 19.571)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-orange-200` | `oklch(90.1% .076 70.697)` | Brand / Palette Token |
| `--color-orange-300` | `oklch(83.7% .128 66.29)` | Brand / Palette Token |
| `--color-orange-400` | `oklch(75% .183 55.934)` | Brand / Palette Token |
| `--color-orange-500` | `oklch(70.5% .213 47.604)` | Brand / Palette Token |
| `--color-orange-600` | `oklch(64.6% .222 41.116)` | Brand / Palette Token |
| `--color-amber-50` | `oklch(98.7% .022 95.277)` | Brand / Palette Token |
| `--color-amber-100` | `oklch(96.2% .059 95.617)` | Brand / Palette Token |
| `--color-amber-200` | `oklch(92.4% .12 95.746)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.public-site-header> — `runtimewire-com`)**:
   - Landmark `<header class="public-site-header flex">` hosting `RuntimeWire: Breaking tech news. Bef` navigation (`Investigations · Stories · AI · Startups · Venture`), DOM attributes (`data-testid="skip-to-content"`, `data-anim="static"`, `data-testid="header-search-button"`, `data-testid="theme-switch"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Startup Spotlight: Sweatpals sells`)**:
   - Landmark `<section class="relative overflow-hidden">` presenting display lead `Startup Spotlight: Sweatpals sells run clubs the...` and copy excerpt *"You're browsing RuntimeWire with JavaScript disabled. Articles an"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.flex> — `Kalshi in talks at $65B valuation `)**:
   - Landmark `<article class="flex flex-col">` rendering section `Kalshi in talks at $65B valuation days after clos...` with copy *"Win an NVIDIA DGX Spark"*, asset references (`investigations.xml`, `stories.xml`, `featured`, `favicon.ico`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `Editor’s picks`)**:
   - Landmark `<article class="flex flex-col">` framing `Editor’s picks` and `Win an NVIDIA DGX Spark` (*"The Daily Briefing"*) with `#0000` surface cards, `#000000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://runtimewire.com`)**:
   - Landmark `<footer class="border-t border-border">` anchoring `RuntimeWire: Breaking tech news.` footer links (`Investigations · Stories · AI · Startups · Venture`), copy *"The Daily Briefing Subscribe →"*, and `#0000ff` structural dividers.
