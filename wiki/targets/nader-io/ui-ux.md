# UI & UX Architecture: nader-io

## Overview & Design Identity
- **Target**: `nader-io` (**Nader Cserny**)
- **Production URL**: [https://nader.io](https://nader.io)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0a0a0a` ink, `#1a1a1a` accent)
- **Summary**: Product leader specializing in agentic AI systems and blockchain tools. Founder, builder, and advisor, from strategy to shipped code.
- **Total Clean CSS Variables Extracted**: `74` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter-1977dbd7896d9b1f`
- **Body Font Stack**: `Inter-1977dbd7896d9b1f fallback: Arial`
- **Monospace / Technical Font Stack**: `JetBrains Mono-7037818b06159deb`
- **Hero Display (`H1`)**: CSS variables `--text-display: clamp(3.25rem, 11vw, 6.5rem)`, `--text-display--line-height: .95`, `--text-display--letter-spacing: -.04em`; rule `h1` (`font-size: clamp(40px,5.5vw,70px)`, `line-height: 1.1`, `letter-spacing: -.04em`, `font-weight: 400`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: .8125rem`, `line-height: 1.35`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: .9375rem`)
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-jetbrains-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#f6f6f6` | `var(--color-surface)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0a0a0a` | `var(--color-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#1a1a1a` | `var(--color-prose)` in `:root` |
| **Secondary / Muted Copy** | `#666` | `var(--color-muted)` in `:root` |
| **Structural Hairline Border** | `#8a8a8a` | `var(--color-faint)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rule` | `var(--color-rule)` | Design System Custom Token |
| `--signal` | `var(--color-accent)` | Design System Custom Token |
| `--paper` | `var(--color-surface)` | Canvas / Surface Token |
| `--font-sans` | `var(--font-inter)` | Typography / Scale Token |
| `--font-mono` | `var(--font-jetbrains-mono)` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `nader-io`)**:
   - Landmark `<header class="site-header relative">` hosting `Nader Cserny` navigation (`Poster Live · Chaos Edition · Cinquanta Edition · Circles Edition · Number Wall Edition`), DOM attributes (`data-site="nader.io"`, `data-edition-menu`, `data-astro-cid-ylg3fdu2`, `data-astro-cid-lcdefpme`), and stylesheet rule `body.home-page .site-header { margin-bottom:0;padding-bottom:1.5rem }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Hi, I’m Nader. Hi I’m Nader`)**:
   - Landmark `<section class="home-hero">` presenting display lead `Hi, I’m Nader. Hi I’m Nader` and copy excerpt *"Editions Poster Live Chaos Edition Cinquanta Edition Circles Edit"* over `#fff` canvas and `#0a0a0a` ink.
3. **Primary Showcase & Content Grid (<section.home-section> — `Shipping AI workflows`)**:
   - Landmark `<section class="home-section">` rendering section `Shipping AI workflows` with copy *"Number Wall Edition"*, asset references (`favicon.svg`, `favicon.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `body.home-page main { padding-top:1.5rem }`.
4. **Interactive Detail & Feature Matrix (<article.home-cap> — `Scaling blockchain dApps`)**:
   - Landmark `<article class="home-cap">` framing `Scaling blockchain dApps` and `Leading 0-to-1 products` (*"Personal Computer Edition"*) with `#0a0a0a` surface cards, `#1a1a1a` accents, and `body.home-page .site-footer { margin-top:4rem }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://nader.io`)**:
   - Landmark `<footer class="site-footer mt-20">` anchoring `Nader Cserny` footer links (`Poster Live · Chaos Edition · Cinquanta Edition · Circles Edition · Number Wall Edition`), copy *"Monochrome Edition"*, and `#8a8a8a` structural dividers.
