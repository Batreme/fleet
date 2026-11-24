---
title: "UI & UX Architecture: errormade-tech"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: errormade-tech

## Overview & Design Identity
- **Target**: `errormade-tech` (**Entrance — Errormade**)
- **Production URL**: [https://errormade.tech/](https://errormade.tech/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#777777`)
- **Summary**: Selected graphic design and art direction by Errormade.
- **Total Clean CSS Variables Extracted**: `82` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `end`
- **Body Font Stack**: `end`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 14px`, `font-weight: 700`, `letter-spacing: -0.48px`); rule `h1` (`letter-spacing: inherit`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16px`, `line-height: 14px`, `font-weight: 400`, `letter-spacing: -0.48px`); rule `h2` (`letter-spacing: inherit`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 14px`, `font-weight: 400`, `letter-spacing: -0.48px`); rule `p` (`font-size: 9px`, `line-height: 1.4`, `letter-spacing: .05em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 14px`, `font-weight: 400`, `letter-spacing: -0.48px`); CSS variables `--object-caption-height: 36.5px`, `--object-caption-bottom: calc(var(--mobile-footer-bottom) + 25px)`; rule `small` (`font-size: 9px`, `line-height: 1.4`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `nav` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#262626` | `.footer-divider { background: #262626 }` |
| **Interactive Accent / Highlight** | `#777777` | `.tools-header > button { color: #777777 }` |
| **Secondary / Muted Copy** | `#747474` | `var(--tools-muted)` in `:root` |
| **Structural Hairline Border** | `#262626` | `var(--case-divider-color)` in `:root` (`rgb(255 255 255 / 15%)`) |
| **Variable Token (`--media-hover-outline`)** | `#e5e5e5` | `var(--media-hover-outline)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-margin` | `16px` | Layout / Spatial Grid Token |
| `--safe-top` | `env(safe-area-inset-top, 0px)` | Dimension / Scale Token |
| `--safe-bottom` | `env(safe-area-inset-bottom, 0px)` | Dimension / Scale Token |
| `--grid-columns` | `12` | Layout / Spatial Grid Token |
| `--grid-gap` | `8px` | Layout / Spatial Grid Token |
| `--header-content-gap` | `84px` | Layout / Spatial Grid Token |
| `--site-header-bottom` | `82px` | Layout / Spatial Grid Token |
| `--ink` | `#000` | Typography Ink Token |
| `--muted` | `rgb(0 0 0 / 25%)` | Color / Atmospheric Token |
| `--rule` | `rgb(0 0 0 / 15%)` | Color / Atmospheric Token |
| `--page-background` | `#fff` | Canvas / Surface Token |
| `--media-hover-outline` | `#e5e5e5` | Elevation / Border Token |
| `--media-hover-icon-invert` | `0` | Design System Custom Token |
| `--row-motion-x` | `0px` | Motion / Easing Token |
| `--media-flip-angle` | `0deg` | Design System Custom Token |
| `--media-flip-opacity` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `errormade-tech`)**:
   - Landmark `<header class="site-header header-motion-ready">` (`1408x36px`) hosting `Entrance — Errormade` navigation (`Entrance · Work · Errormade · About · .obj`), DOM attributes (`data-read-only-preview`, `data-static-export="959f9f266ae66e5a"`, `data-theme="light"`, `data-mobile-glass="webgl"`), and stylesheet rule `html.lenis body { height: auto; }`.
2. **Hero Stage & Focal Lead (<article.project> — `Entrance — Errormade`)**:
   - Landmark `<article class="project has-custom-layout">` presenting display lead `Entrance — Errormade` and copy excerpt *"Visual, Art direction, Motion Design"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.has-custom-layout> — `Bushido Zho S&T`)**:
   - Landmark `<article class="project has-custom-layout">` rendering section `Bushido Zho S&T` with copy *"Digital, Art direction"*, asset references (`favicon.svg`, `5by7-bold.ttf`, `lenis.css`, `styles.css`), and grid rule `.lenis-stopped { overflow: clip; }`.
4. **Interactive Detail & Feature Matrix (<article.project:nth(2)> — `Forgotten Garden`)**:
   - Landmark `<article class="project has-custom-layout">` framing `Forgotten Garden` and `3 дня дождя "Алекситимия"` (*"Visual, Art direction, Merchandise Design, Graphic Design, AI Cam"*) with `#262626` surface cards, `#777777` accents, and `.lenis.lenis-smooth iframe { pointer-events: none; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://errormade.tech/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Entrance — Errormade` footer links (`Entrance · Work · Errormade · About · .obj`), copy *"Visual, Art direction"*, and `#262626` structural dividers.
