---
title: "UI & UX Architecture: explorajourneys-com_int-en-explora-journal"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: explorajourneys-com_int-en-explora-journal

## Overview & Design Identity
- **Target**: `explorajourneys-com_int-en-explora-journal` (**The Explora Journal, A Magazine by Explora Journeys**)
- **Production URL**: [https://explorajourneys.com/int/en/explora-journal](https://explorajourneys.com/int/en/explora-journal)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f2ef` canvas, `#222222` ink, `#06b6d4` accent)
- **Summary**: Step aboard The Explora Journal for stories of ships and destinations, from wellness and dining to ports and cultures, told through the O...
- **Total Clean CSS Variables Extracted**: `11` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `WT Monarch Nova`
- **Body Font Stack**: `Shapiro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40.05px`, `line-height: 56.07px`, `font-weight: 400`); rule `.title` (`font-size: 24px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20px`, `line-height: 28px`, `font-weight: 100`); rule `h2` (`font-size: 1.5em`, `font-weight: bold`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 26px`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 26px`, `font-weight: 400`); rule `.label` (`font-size: 9pt`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f2ef` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#222222` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e7e1da` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#06b6d4` | `.vc-date__btn { color: #06b6d4 }` |
| **Secondary / Muted Copy** | `#666666` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#eeeeee` | `.fa-border { border: #eeeeee }` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--animate-duration` | `1s` | Motion / Easing Token |
| `--animate-delay` | `1s` | Motion / Easing Token |
| `--animate-repeat` | `1` | Motion / Easing Token |
| `--alert-height` | `0px` | Layout / Spatial Grid Token |
| `--menu-height-desktop` | `95px` | Layout / Spatial Grid Token |
| `--menu-height-mobile` | `80px` | Layout / Spatial Grid Token |
| `--partner-header-height` | `0px` | Layout / Spatial Grid Token |
| `--hero-component-height` | `calc(100svh - 80px)` | Layout / Spatial Grid Token |
| `--hero-component-height-full` | `var(--hero-component-height)` | Layout / Spatial Grid Token |
| `--gradient-angle` | `0deg` | Design System Custom Token |
| `--contact-banner-height` | `0px` | Layout / Spatial Grid Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--tw-bg-opacity` | `1` | Canvas / Surface Token |
| `--tw-shadow` | `0 9px 20px rgba(0, 0, 0, .1)` | Elevation / Border Token |
| `--explorajourneys--bg` | `#f4f2ef` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--explorajourneys--ink` | `#222222` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.experiencefragment> — `explorajourneys-com_int-en-explora-journal`)**:
   - Landmark `<header class="experiencefragment header-sticky">` (`1440x0px`) hosting `The Explora Journal, A Magazine by E` navigation (`Find a journey · All Destinations · Alaska · Asia · Grand Journeys`), DOM attributes (`data-destex-discover-bound`, `data-description="Scene7DefaultCSS"`, `data-component="ScrollBar"`, `data-namespace="s7classic"`), and stylesheet rule `.fa-lg { font-size:1.33333333em;line-height:.75em;vertical-align:-15% }`.
2. **Hero Stage & Focal Lead (<section.emag-home-hero> — `The Explora Journal`)**:
   - Landmark `<section class="emag-home-hero emag-home-hero--imageBackground">` presenting display lead `The Explora Journal` and copy excerpt *"A Magazine by Explora Journeys"* over `#f4f2ef` canvas and `#222222` ink.
3. **Primary Showcase & Content Grid (<section.emag-home-grid> — `Introducing EXPLORA III`)**:
   - Landmark `<section class="emag-home-grid">` rendering section `Introducing EXPLORA III` with copy *"Wrong email address Primary Email Address* Add Another Email Addr"*, asset references (`0.8.77`, `187102487`, `adalyser.js`, `insight.min.js`), and grid rule `.fa-2x { font-size:2em }`.
4. **Interactive Detail & Feature Matrix (<article.article-card> — `From Sea Salt to Soil`)**:
   - Landmark `<article class="article-card card--small">` framing `From Sea Salt to Soil` and `Advocating for the Ocean` (*"Wrong email address"*) with `#e7e1da` surface cards, `#06b6d4` accents, and `.fa-3x { font-size:3em }`.
5. **Colophon & Global Directory Footer (<footer.quotesubject> — `https://explorajourneys.com/int/en/explora-journal`)**:
   - Landmark `<footer class="quotesubject">` anchoring `The Explora Journal, A Magazine ` footer links (`Find a journey · All Destinations · Alaska · Asia · Grand Journeys`), copy *"Primary Email Address*"*, and `#eeeeee` structural dividers.
