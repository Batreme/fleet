---
title: "UI & UX Architecture: morrow-valerian-studio"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: morrow-valerian-studio

## Overview & Design Identity
- **Target**: `morrow-valerian-studio` (**MORROW**)
- **Production URL**: [https://morrow.valerian.studio](https://morrow.valerian.studio)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#c4c4c4` accent)
- **Summary**: FALL26’ KNITWEAR PORCELAIN
- **Total Clean CSS Variables Extracted**: `56` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `editorialNew`
- **Body Font Stack**: `ppNeueMontreal`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-display: clamp(1.75rem, 3vw, 3rem)`, `--text-display--line-height: 1.2`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 32px`, `font-weight: 500`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-body: 14px`, `--text-body--line-height: calc(1.25 / .875)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | `.text-black { color: black }` (`#000000`) |
| **Elevated Surface / Card Substrate** | `#f5f5f5` | `.cart-item-image { background: #f5f5f5 }` |
| **Interactive Accent / Highlight** | `#c4c4c4` | `.cart-quantity button:disabled { color: #c4c4c4 }` |
| **Secondary / Muted Copy** | `#737373` | `.cart-item-size { color: #737373 }` |
| **Structural Hairline Border** | `#e5e5e5` | `.cart-header { border-bottom: #e5e5e5 }` |
| **Variable Token (`--color-red-800`)** | `#9f0712` | `var(--color-red-800)` in `:root` |
| **Variable Token (`--color-rose-500`)** | `#ff2357` | `var(--color-rose-500)` in `:root` |
| **Variable Token (`--color-neutral-50`)** | `#fafafa` | `var(--color-neutral-50)` in `:root` |
| **Variable Token (`--color-neutral-300`)** | `#d4d4d4` | `var(--color-neutral-300)` in `:root` |
| **Variable Token (`--color-neutral-400`)** | `#a1a1a1` | `var(--color-neutral-400)` in `:root` |
| **Variable Token (`--color-neutral-600`)** | `#525252` | `var(--color-neutral-600)` in `:root` |
| **Variable Token (`--color-neutral-900`)** | `#171717` | `var(--color-neutral-900)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-pp-neue-montreal), Arial, sans-serif` | Typography / Scale Token |
| `--color-red-800` | `#9f0712` | Brand / Palette Token |
| `--color-rose-500` | `#ff2357` | Brand / Palette Token |
| `--color-neutral-50` | `#fafafa` | Brand / Palette Token |
| `--color-neutral-100` | `#f5f5f5` | Brand / Palette Token |
| `--color-neutral-200` | `#e5e5e5` | Brand / Palette Token |
| `--color-neutral-300` | `#d4d4d4` | Brand / Palette Token |
| `--color-neutral-400` | `#a1a1a1` | Brand / Palette Token |
| `--color-neutral-500` | `#737373` | Brand / Palette Token |
| `--color-neutral-600` | `#525252` | Brand / Palette Token |
| `--color-neutral-900` | `#171717` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xs` | `20rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-nav> — `morrow-valerian-studio`)**:
   - Landmark `<header class="site-nav col-start-1">` (`1440x68px`) hosting `MORROW` navigation (`MORROW · Shop · All products · Clothes · Accessories`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.cart-dialog::backdrop { background:0 0 }`.
2. **Hero Stage & Focal Lead (<section.h-svh> — `Pace Base Layer`)**:
   - Landmark `<section class="h-svh grid-cols-12">` presenting display lead `Pace Base Layer` and copy excerpt *"KNITWEAR PORCELAIN"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.grid-cols-12> — `Everyday Long Sleeve`)**:
   - Landmark `<section class="grid-cols-12 gap-x-gutter">` rendering section `Everyday Long Sleeve` with copy *"Built for the changing rhythm of the season, Fall 2026 introduces"*, asset references (`3p45zkgyngvyk.css`, `19h1-_j7inwm4.css`, `376za7hcbsln-.css`, `2x1xg-ar74jvz.css`), and grid rule `.cart-scrim { pointer-events:none;background:00000047;position:absolute;inset:0 }`.
4. **Interactive Detail & Feature Matrix (<article.group> — `Tempo Running Shorts`)**:
   - Landmark `<article class="group font-sans">` framing `Tempo Running Shorts` and `Stride Windbreaker` (*"Explore the collection"*) with `#f5f5f5` surface cards, `#c4c4c4` accents, and `.cart-panel { background:fff;flex-direction:column;width:min(100%,480px);height:100%;m... }`.
5. **Colophon & Global Directory Footer (<footer.px-page> — `https://morrow.valerian.studio`)**:
   - Landmark `<footer class="px-page font-sans">` anchoring `MORROW` footer links (`MORROW · Shop · All products · Clothes · Accessories`), copy *"Stories of people, places and the details that shape the way"*, and `#e5e5e5` structural dividers.
