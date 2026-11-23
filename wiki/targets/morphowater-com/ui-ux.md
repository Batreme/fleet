---
title: "UI & UX Architecture: morphowater-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: morphowater-com

## Overview & Design Identity
- **Target**: `morphowater-com` (**MORPHO · Natural Spring Water from Costa Rica**)
- **Production URL**: [https://morphowater.com](https://morphowater.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#101820` / `#0000ff`)
- **Summary**: Discover MORPHO natural spring water from Costa Rica. Explore our source, still water in 12 oz aluminum cans, and our upcoming sparkling...
- **Total Clean CSS Variables Extracted**: `83` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gotham`
- **Body Font Stack**: `Gotham`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 97.92px`, `line-height: 88.128px`, `font-weight: 300`, `letter-spacing: -6.3648px`); rule `h1` (`font-size: clamp(68px,7.6vw,120px)`, `line-height: 1.015`, `letter-spacing: -5px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 51.84px`, `line-height: 58.0608px`, `font-weight: 300`, `letter-spacing: -2px`); rule `h2` (`font-size: clamp(43px,4vw,62px)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-reveal: 1`; rule `p` (`font-size: 11px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `nav` (`font-size: 11px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#101820` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000080` | `::selection { background: navy }` (`#000080`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.flow-page button:focus-visible { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#6b7080` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#2b363f` | `var(--menu-rule)` in `:root` (`d0edff24`) |
| **Variable Token (`--navy`)** | `#0a127b` | `var(--navy)` in `:root` |
| **Variable Token (`--ink`)** | `#20274a` | `var(--ink)` in `:root` |
| **Variable Token (`--paper`)** | `#faf9f6` | `var(--paper)` in `:root` |
| **Variable Token (`--line`)** | `#dbdddf` | `var(--line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--navy` | `#0a127b` | Layout / Spatial Grid Token |
| `--ink` | `#20274a` | Typography Ink Token |
| `--paper` | `#faf9f6` | Canvas / Surface Token |
| `--muted` | `#6b7080` | Color / Atmospheric Token |
| `--line` | `#dbdddF` | Color / Atmospheric Token |
| `--serif` | `Georgia,"Times New Roman",serif` | Typography / Scale Token |
| `--scroll` | `0px` | Dimension / Scale Token |
| `--flow-surface` | `#101820` | Canvas / Surface Token |
| `--panel-opacity` | `1` | Design System Custom Token |
| `--copy-opacity` | `1` | Typography Ink Token |
| `--read-progress` | `1` | Design System Custom Token |
| `--read-rest-opacity` | `.43` | Design System Custom Token |
| `--pour-progress` | `0` | Design System Custom Token |
| `--pour-finish` | `0` | Design System Custom Token |
| `--benefit-opacity` | `1` | Design System Custom Token |
| `--read-dim` | `.4` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.morpho-header> — `morphowater-com`)**:
   - Landmark `<header class="morpho-header">` (`1440x94px`) hosting `MORPHO · Natural Spring Water from C` navigation (`The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`), DOM attributes (`data-journey-critical`, `data-journey-styles`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.morpho-consent p { margin:0;color:c7d8e2 }`.
2. **Hero Stage & Focal Lead (<section.flow-journey> — `A world within.`)**:
   - Landmark `<section class="flow-journey">` presenting display lead `A world within.` and copy excerpt *"NATURAL COSTA RICAN SPRING WATER"* over `#101820` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.territory-journey> — `A small click. A world opens.`)**:
   - Landmark `<section class="territory-journey coastal-story">` rendering section `A small click. A world opens.` with copy *"Natural spring water from Costa Rica."*, asset references (`gotham-light-common.woff2`, `gotham-book-common.woff2`, `publico-headline-light-italic-com...`, `wordmark-white.webp`), and grid rule `.morpho-consent .consent-title { font-size:17px;color:fff;margin-bottom:7px }`.
4. **Interactive Detail & Feature Matrix (<article.territory-panel> — `Let the outside in.`)**:
   - Landmark `<article class="territory-panel">` framing `Let the outside in.` and `Back to what matters.` (*"Still and sparkling. In aluminum cans."*) with `#000080` surface cards, `#0000ff` accents, and `.consent-actions { display:flex;gap:12px;margin-top:16px }`.
5. **Colophon & Global Directory Footer (<footer.flow-footer> — `https://morphowater.com`)**:
   - Landmark `<footer class="flow-footer morpho-footer">` anchoring `MORPHO · Natural Spring Water fr` footer links (`The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`), copy *"FROM COSTA RICA. INTO YOUR ELEMENT."*, and `#2b363f` structural dividers.
