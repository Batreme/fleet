---
title: "UI & UX Architecture: thunder-buns-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: thunder-buns-com

## Overview & Design Identity
- **Target**: `thunder-buns-com` (**Thunderbuns · Smashburgers Delivered**)
- **Production URL**: [https://thunder-buns.com/](https://thunder-buns.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#12220f` / `#0000ee`)
- **Summary**: The best smash burgers, 100% halal. Delivered across the Netherlands, Belgium and Germany. Order through your usual delivery app.
- **Total Clean CSS Variables Extracted**: `124` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bowlby One`
- **Body Font Stack**: `Satoshi`
- **Monospace / Technical Font Stack**: `Haffer Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 130px`, `line-height: 114.4px`, `font-weight: 700`); rule `h1` (`font-size: min(14.5em,130px)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 175px`, `line-height: 154px`, `font-weight: 700`); rule `h2` (`font-size: 3.3em`, `line-height: .88`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 1.4em`, `line-height: 1.2`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#12220f` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#faf7ec` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1e351f` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Structural Hairline Border** | `#d4dae0` | `var(--cc-btn-secondary-hover-border-color)` in `:root` |
| **Variable Token (`--cc-bg`)** | `#ffffff` | `var(--cc-bg)` in `:root` |
| **Variable Token (`--cc-primary-color`)** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Variable Token (`--cc-btn-primary-bg`)** | `#30363c` | `var(--cc-btn-primary-bg)` in `:root` |
| **Variable Token (`--cc-btn-primary-hover-bg`)** | `#000000` | `var(--cc-btn-primary-hover-bg)` in `:root` |
| **Variable Token (`--cc-btn-secondary-bg`)** | `#eaeff2` | `var(--cc-btn-secondary-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-modal-border-radius` | `.5rem` | Elevation / Border Token |
| `--cc-btn-border-radius` | `.4rem` | Elevation / Border Token |
| `--cc-modal-transition-duration` | `.25s` | Motion / Easing Token |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` | Typography Ink Token |
| `--cc-modal-margin` | `1rem` | Layout / Spatial Grid Token |
| `--cc-z-index` | `2147483647` | Elevation / Border Token |
| `--cc-bg` | `#fff` | Canvas / Surface Token |
| `--cc-primary-color` | `#2c2f31` | Brand / Palette Token |
| `--cc-secondary-color` | `#5e6266` | Brand / Palette Token |
| `--cc-btn-primary-bg` | `#30363c` | Canvas / Surface Token |
| `--cc-btn-primary-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` | Brand / Palette Token |
| `--cc-btn-primary-hover-bg` | `#000` | Canvas / Surface Token |
| `--cc-btn-primary-hover-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` | Brand / Palette Token |
| `--cc-btn-secondary-bg` | `#eaeff2` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `thunder-buns-com`)**:
   - Landmark `<header class="lenis">` (`1440x132px`) hosting `Thunderbuns · Smashburgers Delivered` navigation (`English · Nederlands · Deutsch · Français · Order`), DOM attributes (`data-ga-id="G-DKWN4TYM2V"`, `data-barba="wrapper"`, `data-scrolling-started="false"`, `data-scrolling-direction="up"`), and stylesheet rule `.mapboxgl-canvas { position:absolute;left:0;top:0 }`.
2. **Hero Stage & Focal Lead (<section.award> — `BURGERS THAT HIT LIKE LIGHTNING.`)**:
   - Landmark `<section class="award">` presenting display lead `BURGERS THAT HIT LIKE LIGHTNING.` and copy excerpt *"ORDER THUNDERBUNS ONLINE -"* over `#12220f` canvas and `#faf7ec` ink.
3. **Primary Showcase & Content Grid (<section.award:nth(2)> — `Burgers that hit like lightning.`)**:
   - Landmark `<section class="award">` rendering section `Burgers that hit like lightning.` with copy *"We make smashburgers. Two patties, smashed onto a screaming hot p"*, asset references (`tb-favicon2.png`, `BowlbyOne-Regular.woff2`, `Satoshi-Regular.woff2`, `image.mux.com`), and grid rule `.mapboxgl-map:-webkit-full-screen { width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.award:nth(3)> — `Who are we? What do we do? Where a`)**:
   - Landmark `<section class="award">` framing `Who are we? What do we do? Where are we?` and `Winner Thuisbezorgd.nl Award 2025 “Best National...` (*"You'll now find us in 130+ locations across the Netherlands, Belg"*) with `#1e351f` surface cards, `#0000ee` accents, and `.mapboxgl-canary { background-color:salmon }`.
5. **Colophon & Global Directory Footer (<footer.shape> — `https://thunder-buns.com/`)**:
   - Landmark `<footer class="shape">` anchoring `Thunderbuns · Smashburgers Deliv` footer links (`English · Nederlands · Deutsch · Français · Order`), copy *"Thunderbuns Aachen"*, and `#d4dae0` structural dividers.
