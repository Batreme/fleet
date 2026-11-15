# UI & UX Architecture: annnimate-com

## Overview & Design Identity
- **Target**: `annnimate-com` (**GSAP Motion Components for React & Vue · Annnimate**)
- **Production URL**: [https://annnimate.com](https://annnimate.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f5f5f5`)
- **Summary**: Production GSAP motion components for React and Vue. Every component is built to the standard we ship for real brands. By Good Fella.
- **Total Clean CSS Variables Extracted**: `453` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `,.h1` (`font-size: var(--font-size-4xl)`, `line-height: 1.2`, `letter-spacing: -.04em`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `,.h2` (`font-size: var(--font-size-2xl)`, `line-height: 1.2`, `letter-spacing: -.03em`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-size-base: clamp(1rem,.95rem + .25vw,1.125rem)`
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-geist-mono),"SF Mono",Monaco,"Cascadia Code",monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fafafa` | `var(--gray-50)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f5f5` | `var(--gray-100)` in `:root` |
| **Secondary / Muted Copy** | `#eee` | `var(--gray-150)` in `:root` |
| **Structural Hairline Border** | `#e8e8e8` | `var(--gray-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--angle` | `0deg` | Design System Custom Token |
| `--font-mono` | `var(--font-geist-mono),"SF Mono",Monaco,"Cascadia Code",monospace` | Typography / Scale Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-amber-400` | `oklch(82.8% .189 84.429)` | Brand / Palette Token |
| `--color-amber-500` | `oklch(76.9% .188 70.08)` | Brand / Palette Token |
| `--color-lime-50` | `oklch(98.6% .031 120.757)` | Brand / Palette Token |
| `--color-lime-100` | `oklch(96.7% .067 122.328)` | Brand / Palette Token |
| `--color-lime-200` | `oklch(93.8% .127 124.321)` | Brand / Palette Token |
| `--color-lime-300` | `oklch(89.7% .196 126.665)` | Brand / Palette Token |
| `--color-lime-400` | `oklch(84.1% .238 128.85)` | Brand / Palette Token |
| `--color-lime-500` | `oklch(76.8% .233 130.85)` | Brand / Palette Token |
| `--color-lime-600` | `oklch(64.8% .2 131.684)` | Brand / Palette Token |
| `--color-lime-700` | `oklch(53.2% .157 131.589)` | Brand / Palette Token |
| `--color-lime-800` | `oklch(45.3% .124 130.933)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.v2-header> — `annnimate-com`)**:
   - Landmark `<header class="v2-header inset-x-0">` hosting `GSAP Motion Components for React & V` navigation (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `host { --glass-primary:color-mix(in srgb,var(--color-muted)70%,transparent) }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Give any site award‑level animatio`)**:
   - Landmark `<section class="relative flex">` presenting display lead `Give any site award‑level animation in minutes.` and copy excerpt *"Get access Get access"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Try it before you copy it.`)**:
   - Landmark `<section class="bg-background pt-64">` rendering section `Try it before you copy it.` with copy *"Curated, not a catalog dump."*, asset references (`edoardo_avatar.avif`, `lukas_avatar.avif`, `matthew_avatar.avif`, `3e5aujvbo39dz.css`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.bg-background> — `Client-ready the moment you paste `)**:
   - Landmark `<section class="bg-background py-64">` framing `Client-ready the moment you paste it.` and `Motion that wins the pitch` (*"Every component built to the bar we ship for real brands. Filter,"*) with `#fafafa` surface cards, `#f5f5f5` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.annnimate-footer> — `https://annnimate.com`)**:
   - Landmark `<footer class="annnimate-footer relative">` anchoring `GSAP Motion Components for React` footer links (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), copy *"Browse the library Browse the library"*, and `#e8e8e8` structural dividers.
