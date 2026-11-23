---
title: "UI & UX Architecture: www-lev-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-lev-com

## Overview & Design Identity
- **Target**: `www-lev-com` (**Lev · The AI platform for commercial real estate**)
- **Production URL**: [https://www.lev.com/](https://www.lev.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#5c7563`)
- **Summary**: Lev combines the industry's largest source of real-time commercial real estate data with purpose-built AI to transform the way sponsors a...
- **Total Clean CSS Variables Extracted**: `1012` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IBM Plex Sans`
- **Body Font Stack**: `IBM Plex Sans`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80.64px`, `line-height: 86.2848px`, `font-weight: 500`, `letter-spacing: -3.6288px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-size-base)`, `line-height: var(--tw-leading,var(...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 36.8px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `h2` (`font-size: var(--text-size-base)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base--line-height: calc(1.5 / 1)`, `--insights-body: 13px`, `--mini-demo-body-size: 13px`; rule `p` (`line-height: 1.55`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: "IBM Plex Mono", ui-monospace, monospace`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm--line-height: calc(1.25 / .875)`; rule `small` (`font-size: 11px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1d211e` | `var(--m-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e7e5db` | `var(--illustration-surface)` in `:root` |
| **Interactive Accent / Highlight** | `#5c7563` | `var(--illustration-accent)` in `:root` |
| **Secondary / Muted Copy** | `#9da19f` | `var(--call-text-muted)` in `:root` |
| **Structural Hairline Border** | `#dde2de` | `var(--m-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--primitive-black` | `0 0 0` | Canvas / Surface Token |
| `--primitive-white` | `1 0 0` | Canvas / Surface Token |
| `--primitive-neutral-950` | `.1448 0 0` | Design System Custom Token |
| `--primitive-neutral-900` | `.2046 0 0` | Design System Custom Token |
| `--primitive-neutral-800` | `.2686 0 0` | Design System Custom Token |
| `--primitive-neutral-700` | `.3715 0 0` | Design System Custom Token |
| `--primitive-neutral-600` | `.4386 0 0` | Design System Custom Token |
| `--primitive-neutral-500` | `.5555 0 0` | Design System Custom Token |
| `--primitive-neutral-400` | `.709 0 0` | Design System Custom Token |
| `--primitive-neutral-300` | `.8699 0 0` | Design System Custom Token |
| `--primitive-neutral-200` | `.9219 0 0` | Design System Custom Token |
| `--primitive-neutral-100` | `.9702 0 0` | Design System Custom Token |
| `--primitive-neutral-50` | `.9851 0 0` | Design System Custom Token |
| `--primitive-abyss-950` | `.1987 .0229 195.47` | Design System Custom Token |
| `--primitive-abyss-900` | `.2496 .0227 195.79` | Design System Custom Token |
| `--primitive-abyss-800` | `.2966 .0188 196.19` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-lev-com`)**:
   - Landmark `<header class="site-header top-0">` (`1440x60px`) hosting `Lev · The AI platform for commercial` navigation (`Talk to sales`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Do less work. Close more deals.`)**:
   - Landmark `<section class="dark">` presenting display lead `Do less work. Close more deals.` and copy excerpt *"Lev brings cutting-edge superintelligence products and experience"* over `#ffffff` canvas and `#1d211e` ink.
3. **Primary Showcase & Content Grid (<section.marketing-page-section> — `Purpose built for your commercial `)**:
   - Landmark `<section class="marketing-page-section scroll-mt-16">` rendering section `Purpose built for your commercial real estate wor...` with copy *"Trusted by leading commercial real estate teams"*, asset references (`matthews.svg`, `time-equities.svg`, `mag-capital.svg`, `essex-capital-markets.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.border-rule> — `Source new deals from billions of `)**:
   - Landmark `<section class="marketing-page-section border-rule">` framing `Source new deals from billions of data points.` and `Screen deals in seconds against your buy box.` (*"Source new deals from billions of data points. Find NYC sponsors "*) with `#e7e5db` surface cards, `#5c7563` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.mt-7> — `https://www.lev.com/`)**:
   - Landmark `<footer class="mt-7">` anchoring `Lev · The AI platform for commer` footer links (`Talk to sales`), copy *"new deals from billions of data points."*, and `#dde2de` structural dividers.
