# UI & UX Architecture: jaspreetsingh-xyz

## Overview & Design Identity
- **Target**: `jaspreetsingh-xyz` (**Jaspreet Singh · Designer & Developer**)
- **Production URL**: [https://jaspreetsingh.xyz/](https://jaspreetsingh.xyz/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#2f2c29`)
- **Summary**: Jaspreet Singh designs and builds products that make complex things feel simple, from UX and design systems to production front-end engin...
- **Total Clean CSS Variables Extracted**: `131` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Swanky and Moo Moo`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f7f4ed` | `var(--color-case-ground)` in `:root` |
| **Interactive Accent / Highlight** | `#2f2c29` | `var(--color-case-ink)` in `:root` |
| **Secondary / Muted Copy** | `#625b52` | `var(--color-case-muted)` in `:root` |
| **Structural Hairline Border** | `#4b453e` | `var(--color-case-header-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-950` | `oklch(25.8% .092 26.042)` | Brand / Palette Token |
| `--color-orange-200` | `oklch(90.1% .076 70.697)` | Brand / Palette Token |
| `--color-orange-700` | `oklch(55.3% .195 38.402)` | Brand / Palette Token |
| `--color-orange-800` | `oklch(47% .157 37.304)` | Brand / Palette Token |
| `--color-orange-950` | `oklch(26.6% .079 36.259)` | Brand / Palette Token |
| `--color-amber-100` | `oklch(96.2% .059 95.617)` | Brand / Palette Token |
| `--color-amber-400` | `oklch(82.8% .189 84.429)` | Brand / Palette Token |
| `--color-amber-950` | `oklch(27.9% .077 45.635)` | Brand / Palette Token |
| `--color-emerald-100` | `oklch(95% .052 163.051)` | Brand / Palette Token |
| `--color-emerald-500` | `oklch(69.6% .17 162.48)` | Brand / Palette Token |
| `--color-emerald-950` | `oklch(26.2% .051 172.552)` | Brand / Palette Token |
| `--color-blue-50` | `oklch(97% .014 254.604)` | Brand / Palette Token |
| `--color-blue-100` | `oklch(93.2% .032 255.585)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.box-border> — `jaspreetsingh-xyz`)**:
   - Landmark `<header class="box-border absolute">` hosting `Jaspreet Singh · Designer & Develope` navigation (`About About · Work Work · Contact Contact`), DOM attributes (`data-portfolio-hydrated="true"`, `data-slot="link"`, `data-slot="link"`, `data-slot="link"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.site-container> — `Hello, I'm Jaspreet`)**:
   - Landmark `<section class="site-container relative">` presenting display lead `Hello, I'm Jaspreet` and copy excerpt *"Designer & Developer"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.site-container> — `Designer, Developer by profession`)**:
   - Landmark `<section class="site-container relative">` rendering section `Designer, Developer by profession` with copy *"Hello, I'm Jaspreet"*, asset references (`main-BQKRg_5e.js`, `vendor-CUM6pZK6.js`, `motion-DEa3jZ1l.js`, `index-CCN64OyI.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.relative> — `Polymath by ambition`)**:
   - Landmark `<article class="relative block">` framing `Polymath by ambition` and `Selected works` (*"I design and build digital products for a living. Still figuring "*) with `#f7f4ed` surface cards, `#2f2c29` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://jaspreetsingh.xyz/`)**:
   - Landmark `<footer class="relative pt-16">` anchoring `Jaspreet Singh · Designer & Deve` footer links (`About About · Work Work · Contact Contact`), copy *"I design and build digital products for a living."*, and `#4b453e` structural dividers.
