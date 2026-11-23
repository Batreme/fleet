---
title: "UI & UX Architecture: seemecreative-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: seemecreative-com

## Overview & Design Identity
- **Target**: `seemecreative-com` (**SEE ME Creative**)
- **Production URL**: [https://seemecreative.com/](https://seemecreative.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f7f7` canvas, `#333333` ink, `#ffa500` accent)
- **Summary**: SEE ME emerged from the desire to forge a creative environment that reimagines the ways in which we tell, create, and share stories.
- **Total Clean CSS Variables Extracted**: `26` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ABC Favorit`
- **Body Font Stack**: `ABC Favorit`
- **Monospace / Technical Font Stack**: `ABC Favorit Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50px`, `line-height: 45px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 18px`, `line-height: 130%`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--unit-margin-small: 10px`, `--unit-max-width-small: 680px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f7f7` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#333333` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `:after { background-color: #ffffff }` |
| **Interactive Accent / Highlight** | `#ffa500` | `.menu a.router-link-active .index { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#ffa500` | `.glyph { color: orange }` (`#ffa500`) |
| **Structural Hairline Border** | `#ffa500` | hairline divider derived from `.glyph { color: orange }` (`#ffa500`) |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-gray`)** | `#b2b2b2` | `var(--color-gray)` in `:root` |
| **Variable Token (`--color-orange`)** | `#ff5600` | `var(--color-orange)` in `:root` |
| **Variable Token (`--color-orange-inverse`)** | `#00a9ff` | `var(--color-orange-inverse)` in `:root` |
| **Variable Token (`--color-off-white`)** | `#f9f3f2` | `var(--color-off-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-white` | `#f8f7f7` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-gray` | `#b2b2b2` | Brand / Palette Token |
| `--color-charcoal` | `#333` | Brand / Palette Token |
| `--color-orange` | `#ff5600` | Brand / Palette Token |
| `--color-orange-inverse` | `#00a9ff` | Brand / Palette Token |
| `--color-off-white` | `#f9f3f2` | Canvas / Surface Token |
| `--color-white-inverse` | `#f8f7f7` | Canvas / Surface Token |
| `--unit-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--unit-gap` | `25px` | Layout / Spatial Grid Token |
| `--unit-max-width` | `1800px` | Layout / Spatial Grid Token |
| `--unit-header-height` | `66px` | Layout / Spatial Grid Token |
| `--font-primary` | `"ABC Favorit",sans-serif` | Brand / Palette Token |
| `--font-secondary` | `"Cardinal Fruit Web",serif` | Brand / Palette Token |
| `--font-tertiary` | `"ABC Favorit Mono",monospace` | Typography / Scale Token |
| `--easing-motion` | `cubic-bezier(0.4,0,0.2,1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.global-header> — `seemecreative-com`)**:
   - Landmark `<header class="global-header header">` (`1440x66px`) hosting `SEE ME Creative` navigation (`001 Work · 002 Artists · 003 About · 004 News`), DOM attributes (`data-capo`, `data-v-344bacdf`, `data-v-bd05448e`, `data-v-61c5c60e`), and stylesheet rule `before { background-color:ff7e26;mix-blend-mode:color;z-index:200 }`.
2. **Hero Stage & Focal Lead (<section.page> — `SEE ME Creative`)**:
   - Landmark `<section class="page page-home">` presenting display lead `SEE ME Creative` and copy excerpt *"sayhello@seemecreative.com"* over `#f8f7f7` canvas and `#333333` ink.
3. **Primary Showcase & Content Grid (<section.page-home> — `Where your vision goes to grow`)**:
   - Landmark `<section class="page page-home">` rendering section `Where your vision goes to grow` with copy *"SEE ME Creative"*, asset references (`entry.BKkY1yHX.css`, `wp-image.abO9u4pg.css`, `grid-work.Dsp1qX9O.css`, `grid-masonry.BnNvLTuH.css`), and grid rule `after { background-color:fff;z-index:100 }`.
4. **Interactive Detail & Feature Matrix (<section.page:nth(2)> — `WE ARE A FULL-SERVICE CREATIVE AGE`)**:
   - Landmark `<section class="page page-home">` framing `WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO...` and `「 WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING...` (*"Where your vision goes to grow"*) with `#ffffff` surface cards, `#ffa500` accents, and `.item { width:calc(33% - 10px) }`.
5. **Colophon & Global Directory Footer (<footer.wp-seo> — `https://seemecreative.com/`)**:
   - Landmark `<footer class="wp-seo">` anchoring `SEE ME Creative` footer links (`001 Work · 002 Artists · 003 About · 004 News`), copy *"WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO..."*, and `#ffa500` structural dividers.
