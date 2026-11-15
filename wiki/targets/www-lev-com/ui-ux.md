# UI & UX Architecture: www-lev-com

## Overview & Design Identity
- **Target**: `www-lev-com` (**Lev · The AI platform for commercial real estate**)
- **Production URL**: [https://www.lev.com/](https://www.lev.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#243c33` / `#fbfaf6`)
- **Summary**: Lev combines the industry's largest source of real-time commercial real estate data with purpose-built AI to transform the way sponsors a...
- **Total Clean CSS Variables Extracted**: `972` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IBM Plex Sans`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Sans`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-size-base)`, `line-height: var(--tw-leading,var(...`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `h2` (`font-size: var(--text-size-base)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy**: CSS variables `--text-base--line-height: calc(1.5 / 1)`, `--insights-body: 13px`, `--mini-demo-body-size: 13px`; rule `p` (`line-height: 1.55`)
- **Metadata & Labels**: CSS variables `--font-mono: "IBM Plex Mono", ui-monospace, monospace`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm--line-height: calc(1.25 / .875)`; rule `small` (`font-size: 11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#243c33` | `var(--illustration-foreground)` in `:root` |
| **Primary Typography Ink** | `#5c7563` | `var(--illustration-accent)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d6e1d3` | `var(--illustration-fill)` in `:root` |
| **Interactive Accent / Highlight** | `#fbfaf6` | `var(--illustration-on-accent)` in `:root` |
| **Secondary / Muted Copy** | `#e7e5db` | `var(--illustration-surface)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--m-surface)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--shimmer-angle` | `20deg` | Design System Custom Token |
| `--scroll-fade-t` | `0px` | Dimension / Scale Token |
| `--scroll-fade-b` | `0px` | Dimension / Scale Token |
| `--scroll-fade-s` | `0px` | Dimension / Scale Token |
| `--scroll-fade-e` | `0px` | Dimension / Scale Token |
| `--scroll-fade-mask` | `initial` | Design System Custom Token |
| `--shimmer-image` | `initial` | Design System Custom Token |
| `--shimmer-text-fill` | `initial` | Typography Ink Token |
| `--beam-angle` | `0deg` | Design System Custom Token |
| `--font-sans` | `"IBM Plex Sans", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--font-mono` | `"IBM Plex Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--color-red-300` | `oklch(var(--primitive-red-300))` | Brand / Palette Token |
| `--color-red-400` | `oklch(var(--primitive-red-400))` | Brand / Palette Token |
| `--color-red-500` | `oklch(var(--primitive-red-500))` | Brand / Palette Token |
| `--color-red-700` | `oklch(var(--primitive-red-700))` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-lev-com`)**:
   - Landmark `<header class="site-header fixed">` hosting `Lev · The AI platform for commercial` navigation (`Login · Talk to sales`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Do less work. Close more deals.`)**:
   - Landmark `<section class="dark">` presenting display lead `Do less work. Close more deals.` and copy excerpt *"Lev brings cutting-edge superintelligence products and experience"* over `#243c33` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.marketing-page-section> — `Workflows`)**:
   - Landmark `<section class="marketing-page-section scroll-mt-16">` rendering section `Workflows` with copy *"Trusted by leading commercial real estate teams"*, asset references (`matthews.svg`, `time-equities.svg`, `mag-capital.svg`, `essex-capital-markets.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.Footer-module__yg9ahW__column> — `Products`)**:
   - Landmark `<section class="Footer-module__yg9ahW__column">` framing `Products` and `Platform` (*"See their success stories"*) with `#d6e1d3` surface cards, `#fbfaf6` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.lev.com/`)**:
   - Landmark `<footer class="site-footer border-t">` anchoring `Lev · The AI platform for commer` footer links (`Login · Talk to sales`), copy *"Commercial real estate software"*, and `#fff` structural dividers.
