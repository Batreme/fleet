---
title: "UI & UX Architecture: sincro-es_en-us"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: sincro-es_en-us

## Overview & Design Identity
- **Target**: `sincro-es_en-us` (**Us - Sincro**)
- **Production URL**: [https://sincro.es/en/us/](https://sincro.es/en/us/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#081423` ink, `#0040ff` accent)
- **Summary**: Navigating complexity together
- **Total Clean CSS Variables Extracted**: `133` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Schibsted Grotesk`
- **Body Font Stack**: `Schibsted Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 143.856px`, `line-height: 129.47px`, `font-weight: 400`, `letter-spacing: -2.87712px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 55.944px`, `line-height: 61.5384px`, `font-weight: 400`, `letter-spacing: -1.07892px`); rule `h2` (`font-size: var(--text-bodyMobM,.9375rem)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy**: live computed `body` (`font-size: 15.984px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-base: 100%`, `--text-base--line-height: normal`, `--text-bodyTagline: 5.5rem`; rule `p` (`font-size: var(--text-bodyMobL)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15.984px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-sm: .75rem`, `--text-sm--line-height: 1.25`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#081423` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#081423` | `:placeholder-shown { background-color: #081423 }` |
| **Interactive Accent / Highlight** | `#0040ff` | `var(--color-vividBlueHover)` in `:root` |
| **Secondary / Muted Copy** | `#ff7cc1` | `var(--color-pink)` in `:root` |
| **Structural Hairline Border** | `#808080` | `.border-gray-400 { border-color: #808080 }` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.75rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.25` | Typography Ink Token |
| `--text-base` | `100%` | Typography Ink Token |
| `--text-base--line-height` | `normal` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--tracking-wide` | `.025em` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--radius-xs` | `.125rem` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `sincro-es_en-us`)**:
   - Landmark `<header class="top-0 left-0">` (`1440px`) hosting `Us - Sincro` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-8de50b09`, `data-swiper-slide-index="0"`, `data-swiper-slide-index="1"`, `data-swiper-slide-index="2"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.flex-1> — `20 years of being who we say we ar`)**:
   - Landmark `<main class="flex-1 max-w-full">` presenting display lead `20 years of being who we say we are` and copy excerpt *"Navigating complexity together"* over `#ffffff` canvas and `#081423` ink.
3. **Primary Showcase & Content Grid (<main.max-w-full> — `UNE Standard`)**:
   - Landmark `<main class="flex-1 max-w-full">` rendering section `UNE Standard` with copy *"We aim to be the strategic partner that brings excellence, techno"*, asset references (`entry.BcfY3otZ.css`, `Media.DbUUtcYg.css`, `PageBuilder.D9iVxonM.css`, `SchibstedGrotesk-Regular.woff2`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.relative> — `Driven by and for the people`)**:
   - Landmark `<main class="flex-1 max-w-full">` framing `Driven by and for the people` and `Building networks` (*"To help you navigate complexity with direction and confidence."*) with `#081423` surface cards, `#0040ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-mediumGrey> — `https://sincro.es/en/us/`)**:
   - Landmark `<footer class="border-mediumGrey pt-XL">` anchoring `Us - Sincro` footer links (`Overview · Index · Archive · About · Contact`), copy *"We were born and grew faithful to a simple idea: that consul"*, and `#808080` structural dividers.
