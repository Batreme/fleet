---
title: "UI & UX Architecture: thecassandravale-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: thecassandravale-com

## Overview & Design Identity
- **Target**: `thecassandravale-com` (**Cassandra Vale · Fashion, Stories & Branded Content**)
- **Production URL**: [https://thecassandravale.com/](https://thecassandravale.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#131313` canvas, `#ffffff` ink, `#ff1053` accent)
- **Summary**: Cassandra Vale brings together fashion, short-form stories, editorial imagery and branded collaborations.
- **Total Clean CSS Variables Extracted**: `43` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Monument`
- **Body Font Stack**: `Monument`
- **Monospace / Technical Font Stack**: `Andale Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 201.6px`, `line-height: 161.28px`, `font-weight: 700`, `letter-spacing: -10.08px`); rule `h1` (`font-size: 44px`, `line-height: 54px`, `font-weight: 600`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 26px`, `line-height: 26px`, `font-weight: 700`, `letter-spacing: -0.26px`); rule `h2` (`font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 29px`, `font-weight: 400`); CSS variables `--nectar-body-line-height: 29px`, `--nectar-body-font-size: 16px`; rule `p` (`font-size: 14px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 29px`, `font-weight: 400`); rule `.label` (`font-size: 14px`, `line-height: 1`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#131313` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `slide-out-widget-area-toggle .l... { background-color: #000000 }` |
| **Interactive Accent / Highlight** | `#ff1053` | `var(--nectar-extra-color-gradient-1)` in `:root` |
| **Secondary / Muted Copy** | `#888888` | `gle #single-meta ul .meta-share... { color: #888888 }` |
| **Structural Hairline Border** | `#2c353b` | `#wp-admin-bar-my-account.with-a... { border: #2c353b }` |
| **Variable Token (`--nectar-extra-color-gradient-1`)** | `#3452ff` | `var(--nectar-extra-color-gradient-1)` in `:root` |
| **Variable Token (`--nectar-extra-color-gradient-2`)** | `#32d6ff` | `var(--nectar-extra-color-gradient-2)` in `:root` |
| **Variable Token (`--nectar-extra-color-gradient-2`)** | `#2ac4ea` | `var(--nectar-extra-color-gradient-2)` in `:root` |
| **Variable Token (`--nectar-extra-color-2`)** | `#bf7741` | `var(--nectar-extra-color-2)` in `:root` |
| **Variable Token (`--nectar-extra-color-3`)** | `#bb3a4e` | `var(--nectar-extra-color-3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp--style--global--content-size` | `1300px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1300px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--height` | `32px` | Layout / Spatial Grid Token |
| `--scroll-bar-w` | `-2px` | Dimension / Scale Token |
| `--nectar-font-light-color` | `#ffffff` | Canvas / Surface Token |
| `--page-color-change-section-transition-time` | `0.8s` | Brand / Palette Token |
| `--nectar-cubic-bezier-out` | `cubic-bezier(0.3, 1, 0.3, 1)` | Brand / Palette Token |
| `--nectar-cubic-bezier-in-out` | `cubic-bezier(0.76, 0, 0.24, 1)` | Brand / Palette Token |
| `--nectar-header-hover-timing` | `0.65s` | Brand / Palette Token |
| `--mobile-container-width` | `88%` | Layout / Spatial Grid Token |
| `--nectar-extra-color-gradient-1` | `linear-gradient(to right,#ff1053,#3452ff)` | Brand / Palette Token |
| `--nectar-extra-color-gradient-2` | `linear-gradient(to right,#32d6ff,#2AC4EA)` | Brand / Palette Token |
| `--nectar-accent-color` | `#ffffff` | Brand / Palette Token |
| `--nectar-extra-color-1` | `#131313` | Brand / Palette Token |
| `--nectar-extra-color-2` | `#bf7741` | Brand / Palette Token |
| `--nectar-extra-color-3` | `#bb3a4e` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.js> — `thecassandravale-com`)**:
   - Landmark `<header class="js">` (`1440x49px`) hosting `Cassandra Vale · Fashion, Stories & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-pagespeed-no-defer`, `data-nowprocket`, `data-wpacu-skip`, `data-no-optimize`), and stylesheet rule `logo.no-image { transition:color .3s ease,margin .3s ease }`.
2. **Hero Stage & Focal Lead (<div.lenis> — `TOO LOUD`)**:
   - Landmark `<div class="lenis">` presenting display lead `TOO LOUD` and copy excerpt *"SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEVER MAKES A BETTER"* over `#131313` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.lenis-scrolling> — `SHE TAKES THE LONG WAY, THE FAST L`)**:
   - Landmark `<div class="lenis-scrolling">` rendering section `SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEV` with copy *"TO MAKE IT WORTH SHOWING UP FOR."*, asset references (`embed`, `icomoon.woff`, `HERO5_OPT-1024x768.jpg`, `HERO5_OPT.jpg`), and grid rule `.transparent { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<div.js_active> — `TO MAKE IT WORTH SHOWING UP FOR.`)**:
   - Landmark `<div class="js_active">` framing `TO MAKE IT WORTH SHOWING UP FOR.` and `ARTEM MARKOVSKY / ARCR` (*"ARTEM MARKOVSKY / ARCR"*) with `#000000` surface cards, `#ff1053` accents, and `.transparent>.nectar-global-section { pointer-events:all }`.
5. **Colophon & Global Directory Footer (<footer.vc_desktop> — `https://thecassandravale.com/`)**:
   - Landmark `<footer class="vc_desktop">` anchoring `Cassandra Vale · Fashion, Storie` footer links (`Overview · Index · Archive · About · Contact`), copy *"TO MAKE IT WORTH SHOWING UP FOR."*, and `#2c353b` structural dividers.
