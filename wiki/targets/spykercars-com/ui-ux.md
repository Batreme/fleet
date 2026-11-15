# UI & UX Architecture: spykercars-com

## Overview & Design Identity
- **Target**: `spykercars-com` (**Hand-Built Super Sports Cars Since 1880 · Spyker Cars**)
- **Production URL**: [https://spykercars.com/](https://spykercars.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#0000` accent)
- **Summary**: Spyker builds highly exclusive, hand-built super sports cars in the Netherlands. Discover the C8 Preliator XXV Coupé and the marque's sto...
- **Total Clean CSS Variables Extracted**: `169` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `swiss721`
- **Body Font Stack**: `swiss721 Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 38px`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Labels**: CSS variables `--font-mono: ui-monospace,SFMono-Regular,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f24822` | `.animated-grid__col { background-color: #f24822 }` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#1d1d1b` | `::selection { background-color: #1d1d1b }` |
| **Structural Hairline Border** | `#000000` | `.border-black { border-color: black }` (`#000000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-swiss-721),sans-serif` | Typography / Scale Token |
| `--font-mono` | `ui-monospace,SFMono-Regular,monospace` | Typography / Scale Token |
| `--color-red-300` | `oklch(80.8% .114 19.571)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-cyan-300` | `oklch(86.5% .127 207.078)` | Brand / Palette Token |
| `--color-blue-600` | `oklch(54.6% .245 262.881)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-gray-500` | `oklch(55.1% .027 264.364)` | Brand / Palette Token |
| `--color-neutral-50` | `oklch(98.5% 0 none)` | Brand / Palette Token |
| `--color-neutral-100` | `oklch(97% 0 none)` | Brand / Palette Token |
| `--color-neutral-200` | `oklch(92.2% 0 none)` | Brand / Palette Token |
| `--color-neutral-300` | `oklch(87% 0 none)` | Brand / Palette Token |
| `--color-neutral-400` | `oklch(70.8% 0 none)` | Brand / Palette Token |
| `--color-neutral-500` | `oklch(55.6% 0 none)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.container> — `spykercars-com`)**:
   - Landmark `<nav class="container grid">` hosting `Hand-Built Super Sports Cars Since 1` navigation (`Home · Heritage · Boutique · News · Contact`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `after { transform:translateY(-2px) }`.
2. **Hero Stage & Focal Lead (<section.lenis-autoToggle> — `The next chapter of Spyker T h e n`)**:
   - Landmark `<section class="lenis-autoToggle">` presenting display lead `The next chapter of Spyker T h e n e x t c h a p...` and copy excerpt *"Skip to main content"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.sr-only> — `P u r e P a s s i o n`)**:
   - Landmark `<article class="sr-only">` rendering section `P u r e P a s s i o n` with copy *"C8 Preliator XXV Coupé"*, asset references (`f13a7bda184fa931.css`, `86c130d7567786c0.css`, `3c4afd8b2a3df79a.css`, `cdb4fb19178d4946.css`), and grid rule `.icon--copy { height:1.5384615385rem;width:1.5384615385rem }`.
4. **Interactive Detail & Feature Matrix (<section.w-full> — `N u l l a T e n a c i I n v i a E `)**:
   - Landmark `<section class="w-full relative">` framing `N u l l a T e n a c i I n v i a E s t V i a` and `T h e S p y k e r h e r i t a g e` (*"info@spykercars.com"*) with `#f24822` surface cards, `#0000` accents, and `.icon--copy .stroke { fill:none;stroke:currentColor;stroke-width:1px }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://spykercars.com/`)**:
   - Landmark `<footer class="relative z-30">` anchoring `Hand-Built Super Sports Cars Sin` footer links (`Home · Heritage · Boutique · News · Contact`), copy *"For press contacts:"*, and `#000000` structural dividers.
