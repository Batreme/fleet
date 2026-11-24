---
title: "UI & UX Architecture: aestudio-studio_hozon"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: aestudio-studio_hozon

## Overview & Design Identity
- **Target**: `aestudio-studio_hozon` (**Hozon — Pickle & Fermented Food Recipe App**)
- **Production URL**: [https://aestudio.studio/hozon](https://aestudio.studio/hozon)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×3312px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#008000`)
- **Summary**: Find Japanese pickle recipes and fermented food recipes in Hozon for iPhone. Explore quick pickles and nukazuke, track jars and discover...
- **Total Clean CSS Variables Extracted**: `10` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Georgia`
- **Body Font Stack**: `Hiragino Kaku Gothic ProN`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 324px`, `line-height: 246.24px`, `font-weight: 900`, `letter-spacing: -24.3px`); rule `h1` (`font-size: clamp(100px,22.5vw,345px)`, `line-height: .76`, `letter-spacing: -.075em`, `font-weight: 900`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 100.8px`, `line-height: 100.8px`, `font-weight: 400`, `letter-spacing: -6.552px`); rule `h2` (`font-size: clamp(32px,3.4vw,52px)`, `line-height: 1.04`, `letter-spacing: -.045em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 15px`, `line-height: 1.7`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: normal`, `font-weight: 400`); rule `nav` (`font-size: 14px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#20221c` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eef0e5` | `.scroll-link:hover { background: #eef0e5 }` |
| **Interactive Accent / Highlight** | `#008000` | `.text-link:hover { color: green }` (`#008000`) |
| **Secondary / Muted Copy** | `#62665b` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#dedfd7` | `var(--line)` in `:root` |
| **Variable Token (`--green`)** | `#4b603c` | `var(--green)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#20221c` | Typography Ink Token |
| `--green` | `#4b603c` | Color / Atmospheric Token |
| `--line` | `#dedfd7` | Color / Atmospheric Token |
| `--paper` | `#fff` | Canvas / Surface Token |
| `--muted` | `#62665b` | Color / Atmospheric Token |
| `--angle` | `-26deg` | Design System Custom Token |
| `--px` | `0px` | Dimension / Scale Token |
| `--sy` | `0px` | Dimension / Scale Token |
| `--study-shift` | `0px` | Dimension / Scale Token |
| `--rock` | `0deg` | Design System Custom Token |
| `--aestudio-studio--bg` | `#ffffff` | Canvas Substrate (from live computed `html` `background-color` (`computed_styles.json`)) |
| `--aestudio-studio--ink` | `#20221c` | Primary Typography Ink (computed-derived) |
| `--aestudio-studio--surface` | `#eef0e5` | Surface Substrate (computed-derived) |
| `--aestudio-studio--accent` | `#008000` | Interactive Accent (computed-derived) |
| `--aestudio-studio--muted` | `#62665b` | Secondary Ink (computed-derived) |
| `--aestudio-studio--border` | `#dedfd7` | Structural Border (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `aestudio-studio_hozon`)**:
   - Landmark `<header class="header">` (`1440x98px`) hosting `Hozon — Pickle & Fermented Food Reci` navigation (`The app · The idea`), DOM attributes (`data-depth="-0.65"`, `data-depth="0.65"`, `data-depth="-0.3"`, `data-depth="0.4"`), and stylesheet rule `button { font:inherit;color:inherit }`.
2. **Hero Stage & Focal Lead (<section.hero> — `HOZON`)**:
   - Landmark `<section class="hero">` presenting display lead `HOZON` and copy excerpt *"THE ART OF KEEPING."* over `#ffffff` canvas and `#20221c` ink.
3. **Primary Showcase & Content Grid (<section.app-section> — `A little time. A lot of flavour.`)**:
   - Landmark `<section class="app-section section-wrap">` rendering section `A little time. A lot of flavour.` with copy *"A pickling companion. A slower kind of good."*, asset references (`hozon`, `favicon.svg`, `jar-v1.webp`, `cucumber-v2.webp`), and grid rule `img { display:block;max-width:100%;height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.idea-section> — `Pickle recipes. Fermented favourit`)**:
   - Landmark `<section class="idea-section section-wrap">` framing `Pickle recipes. Fermented favourites.` and `Less waste. More wonder.` (*"FRESH TODAY. SAVOURED TOMORROW."*) with `#eef0e5` surface cards, `#008000` accents, and `focus-visible { outline:3px solid var(--green);outline-offset:6px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://aestudio.studio/hozon`)**:
   - Landmark `<footer class="footer">` anchoring `Hozon — Pickle & Fermented Food ` footer links (`The app · The idea`), copy *"Turn everyday ingredients into something worth waiting for. "*, and `#dedfd7` structural dividers.
