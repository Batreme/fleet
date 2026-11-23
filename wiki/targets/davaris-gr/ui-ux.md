---
title: "UI & UX Architecture: davaris-gr"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: davaris-gr

## Overview & Design Identity
- **Target**: `davaris-gr` (**Homepage - Davaris**)
- **Production URL**: [https://davaris.gr/](https://davaris.gr/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f2e5` canvas, `#2e1414` ink, `#f65f00` accent)
- **Summary**: We are a family-owned company built on heritage, excellence, and a human-centric approach. Taking all the necessary steps for the protect...
- **Total Clean CSS Variables Extracted**: `223` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Moderat Extended`
- **Body Font Stack**: `Moderat`
- **Monospace / Technical Font Stack**: `Moderat Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 90px`, `line-height: 81px`, `font-weight: 500`, `letter-spacing: -1.8px`); CSS variables `--fs-h1: clamp(3.75rem, 3.09rem + 2.817vw, 5.625rem)`, `--lh-h1: .9`; rule `,.h1` (`line-height: 1.2`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 60.0048px`, `line-height: 60.0048px`, `font-weight: 500`, `letter-spacing: 2.40019px`); CSS variables `--fs-h2: clamp(2.125rem, 1.4rem + 3.6vw, 4.688rem)`, `--lh-h2: 1`; rule `,.h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: 1.125rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f2e5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#2e1414` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#f65f00` | `var(--bs-link-color)` in `:root` |
| **Secondary / Muted Copy** | `#6c757d` | `var(--bs-secondary)` in `:root` |
| **Structural Hairline Border** | `#e9ecef` | `var(--bs-light-border-subtle)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--space-xs` | `clamp(1rem, 2.2vw, 2.65rem)` | Layout / Spatial Grid Token |
| `--space-sm` | `clamp(1.875rem, 4.43vw, 5.3125rem)` | Layout / Spatial Grid Token |
| `--space-md` | `clamp(2.5rem, 6.5vw, 7.8125rem)` | Layout / Spatial Grid Token |
| `--space-lg` | `clamp(3.75rem, 8.85vw, 10.625rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `davaris-gr`)**:
   - Landmark `<header class="site-header">` (`1440x72px`) hosting `Homepage - Davaris` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-cfasync="false"`, `data-no-minify="true"`, `data-no-optimize="1"`, `data-noptimize="1"`), and stylesheet rule `.flickity-enabled { position:relative }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Fashion textiles that inspire`)**:
   - Landmark `<section class="hero hero--video">` presenting display lead `Fashion textiles that inspire` and copy excerpt *"62 Ermou Str, 144 52 Metamorfosi, Greece"* over `#f5f2e5` canvas and `#2e1414` ink.
3. **Primary Showcase & Content Grid (<section.scrolled-text> — `We are a family-owned company buil`)**:
   - Landmark `<section class="scrolled-text u-escape-container">` rendering section `We are a family-owned company built on heritage,...` with copy *"TEXTILE EXCELLENCE"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `.flickity-enabled:focus { outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.collections-media> — `Plain Collection`)**:
   - Landmark `<section class="collections-media u-escape-container">` framing `Plain Collection` and `Fancy Collection` (*"We are a family-owned company built on heritage, excellence, and "*) with `#dddddd` surface cards, `#f65f00` accents, and `.flickity-viewport { overflow:hidden;position:relative;height:100%;touch-action:pan-y }`.
5. **Colophon & Global Directory Footer (<footer.nav-primary__footer> — `https://davaris.gr/`)**:
   - Landmark `<footer class="nav-primary__footer">` anchoring `Homepage - Davaris` footer links (`Overview · Index · Archive · About · Contact`), copy *"Premium fabrics crafted for elegance, versatility, and super"*, and `#e9ecef` structural dividers.
