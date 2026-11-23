---
title: "UI & UX Architecture: www-studioplato-co"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-studioplato-co

## Overview & Design Identity
- **Target**: `www-studioplato-co` (**Studio Plato - Contemporary Interior Design**)
- **Production URL**: [https://www.studioplato.co/](https://www.studioplato.co/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0082f3`)
- **Summary**: STUDIO PLATO specializes in interior and architecture design. Connect with us for innovative design solutions.
- **Total Clean CSS Variables Extracted**: `11` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Opensaucesans`
- **Body Font Stack**: `Opensaucesans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20px`, `line-height: 20px`, `font-weight: 600`, `letter-spacing: -0.4px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 11.52px`, `line-height: 11.52px`, `font-weight: 500`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11.52px`, `line-height: 11.52px`, `font-weight: 500`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#808080` | `figcaption { color: grey }` (`#808080`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--grey-darkest`)** | `#4f4f4f` | `var(--grey-darkest)` in `:root` |
| **Variable Token (`--grey-lightest`)** | `#dddddd` | `var(--grey-lightest)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--grey-darkest` | `#4f4f4f` | Canvas / Surface Token |
| `--white` | `white` | Canvas / Surface Token |
| `--black` | `black` | Canvas / Surface Token |
| `--site-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--grey-lightest` | `#ddd` | Canvas / Surface Token |
| `--spacing-120` | `7.5em` | Layout / Spatial Grid Token |
| `--spacing-200` | `12.5em` | Layout / Spatial Grid Token |
| `--grey-dark` | `grey` | Canvas / Surface Token |
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--plato-nav-blur` | `0.005em` | Layout / Spatial Grid Token |
| `--plato-nav-opacity` | `0.959856` | Layout / Spatial Grid Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--www-studioplato--bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-studioplato--ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-studioplato-co`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `Studio Plato - Contemporary Interior` navigation (`Projects · Studio · Services · Insights · Instagram`), DOM attributes (`data-wf-domain="www.studioplato.co"`, `data-wf-page="6a27da652c4e1ce8d473b28a"`, `data-wf-site="69fc480c359115ee0044a0b6"`, `data-plato-home-guard`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.cursor_follower> — `Studio Plato - Contemporary Interi`)**:
   - Landmark `<div class="cursor_follower">` presenting display lead `Studio Plato - Contemporary Interior Design` and copy excerpt *"Contemporary interior design for successful living."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.cursor_follower:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="cursor_follower">` rendering section `Featured Work & Interactive Showcase` with copy *"I n t e r i o r d e s i g n p r o j e c t f o r a t i n y a p a r"*, asset references (`cdn.prod.website-files.com`, `studio-plato.webflow.shared.d6524...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.cursor_follower:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="cursor_follower">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Projects —"*) with `#ffff00` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-instrumentsans-n3-active> — `https://www.studioplato.co/`)**:
   - Landmark `<footer class="wf-instrumentsans-n3-active">` anchoring `Studio Plato - Contemporary Inte` footer links (`Projects · Studio · Services · Insights · Instagram`), copy *"S t u d i o P l a t o"*, and `#e2e2e2` structural dividers.
