# UI & UX Architecture: vault-hyperiux-com

## Overview & Design Identity
- **Target**: `vault-hyperiux-com` (**Hyperiux Vault - React & Next.js Interaction Effects.**)
- **Production URL**: [https://vault.hyperiux.com](https://vault.hyperiux.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#1d1d1d`)
- **Summary**: Start with 70+ free source-first effects. Upgrade to Pro for 180+ effects.
- **Total Clean CSS Variables Extracted**: `156` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `aeonikPro`
- **Body Font Stack**: `aeonikPro Fallback`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2.5rem`, `line-height: 1.2`, `letter-spacing: -.025em`, `font-weight: 700`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`, `line-height: 1.3`, `font-weight: 700`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--docs-body: #3a3a3a`
- **Metadata & Labels**: CSS variables `--font-plex-mono: "IBM Plex Mono","IBM Plex Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#272727` | `var(--blog-border-color)` in `:root` |
| **Interactive Accent / Highlight** | `#1d1d1d` | `var(--blog-bg-subtle)` in `:root` |
| **Secondary / Muted Copy** | `#6f6f6f` | `var(--btn-pre)` in `:root` |
| **Structural Hairline Border** | `#000c` | `var(--docs-table-header-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-aeonik` | `"aeonikPro","aeonikPro Fallback"` | Typography / Scale Token |
| `--font-avenir` | `"avenirNext","avenirNext Fallback"` | Typography / Scale Token |
| `--font-plex-mono` | `"IBM Plex Mono","IBM Plex Mono Fallback"` | Typography / Scale Token |
| `--g-shift` | `0px` | Dimension / Scale Token |
| `--beam-angle` | `0deg` | Design System Custom Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-orange-500` | `oklch(70.5% .213 47.604)` | Brand / Palette Token |
| `--color-amber-300` | `oklch(87.9% .169 91.605)` | Brand / Palette Token |
| `--color-amber-500` | `oklch(76.9% .188 70.08)` | Brand / Palette Token |
| `--color-yellow-400` | `oklch(85.2% .199 91.936)` | Brand / Palette Token |
| `--color-green-400` | `oklch(79.2% .209 151.711)` | Brand / Palette Token |
| `--color-green-500` | `oklch(72.3% .219 149.579)` | Brand / Palette Token |
| `--color-emerald-400` | `oklch(76.5% .177 163.223)` | Brand / Palette Token |
| `--color-gray-50` | `oklch(98.5% .002 247.839)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.flex> — `vault-hyperiux-com`)**:
   - Landmark `<nav class="flex items-center">` hosting `Hyperiux Vault - React & Next.js Int` navigation (`Docs D o c s Docs · Blog B l o g Blog`), DOM attributes (`data-sidebar="expanded"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_94f36e { font-family:aeonikPro,aeonikPro Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `The Interaction Layer Your Website`)**:
   - Landmark `<section class="relative z-10">` presenting display lead `The Interaction Layer Your Website Is Missing .` and copy excerpt *"This website uses cookies. Learn More"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.section-x> — `Built for Teams Where the Frontend`)**:
   - Landmark `<section class="section-x relative">` rendering section `Built for Teams Where the Frontend is the Brand.` with copy *"Effects E f f e c t s Effects"*, asset references (`homepage-hero.webp`, `656d53d6ca76b151.css`, `a3fd77dbb258dcd6.css`, `ee41bfcc83e4e14b.css`), and grid rule `.__variable_94f36e { --font-aeonik:"aeonikPro","aeonikPro Fallback" }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `Every moment, already built.`)**:
   - Landmark `<article class="flex flex-col">` framing `Every moment, already built.` and `One command. Real files.` (*"Templates T e m p l a t e s Templates"*) with `#272727` surface cards, `#1d1d1d` accents, and `.__className_91351b { font-family:avenirNext,avenirNext Fallback }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://vault.hyperiux.com`)**:
   - Landmark `<footer class="relative z-200">` anchoring `Hyperiux Vault - React & Next.js` footer links (`Docs D o c s Docs · Blog B l o g Blog`), copy *"Pricing P r i c i n g Pricing"*, and `#000c` structural dividers.
