---
title: "UI & UX Architecture: straw-page"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: straw-page

## Overview & Design Identity
- **Target**: `straw-page` (**Straw.Page - Extremely simple website builder**)
- **Production URL**: [https://straw.page](https://straw.page)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ffff00` accent)
- **Summary**: Straw.Page is the world's simplest website builder. Create unique websites from your mobile device.
- **Total Clean CSS Variables Extracted**: `4` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Yantramanav`
- **Body Font Stack**: `Frank Ruhl Libre`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: normal`, `font-weight: 700`); rule `h1` (`font-size: 80px`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 60px`, `line-height: normal`, `font-weight: 700`); rule `h2` (`font-size: 18px`, `font-weight: 100`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-weight: 900`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | live computed `h2` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `.final button:hover { background: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#df001d` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#eeeeee` | `.fa-border { border: #eeeeee }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lefter` | `0px` | Dimension / Scale Token |
| `--eyeballHeight` | `40px` | Layout / Spatial Grid Token |
| `--eyeballWidth` | `40px` | Layout / Spatial Grid Token |
| `--pupilColor` | `#000` | Brand / Palette Token |
| `--straw-page-bg` | `#ffffff` | Canvas Substrate (from live computed `browser-default` `background-color` (`computed_styles.json`)) |
| `--straw-page-ink` | `#000000` | Primary Typography Ink (computed-derived) |
| `--straw-page-surface` | `#ffff00` | Surface Substrate (computed-derived) |
| `--straw-page-accent` | `#ffff00` | Interactive Accent (computed-derived) |
| `--straw-page-muted` | `#df001d` | Secondary Ink (computed-derived) |
| `--straw-page-border` | `#eeeeee` | Structural Border (computed-derived) |
| `--straw-page-container` | `1440px` | Container Bound (computed-derived) |
| `--straw-page-gap` | `10px` | Grid Gutter (computed-derived) |
| `--straw-page-pad` | `40px` | Lateral Padding (computed-derived) |
| `--straw-page-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--straw-page-radius` | `40px` | Corner Radius (computed-derived) |
| `--straw-page-fs-base` | `80px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.first> — `straw-page`)**:
   - Landmark `<header class="first">` (`1440px`) hosting `Straw.Page - Extremely simple websit` navigation (`Pricing · Twitter · Premium · Email · Terms`), DOM attributes (`data-open="signIn"`, `data-open="signUp"`, `data-cf-beacon="("version":"2024.11.0..."`), and stylesheet rule `.fa-lg { font-size:1.33333em;line-height:.75em;vertical-align:-.0667em }`.
2. **Hero Stage & Focal Lead (<div.first> — `STRAW.PAGE`)**:
   - Landmark `<div class="first">` presenting display lead `STRAW.PAGE` and copy excerpt *"Check your email for a password reset link. Be sure to check your"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.first:nth(2)> — `Forgot password`)**:
   - Landmark `<div class="first">` rendering section `Forgot password` with copy *"Straw.Page lets you create unique websites straight from your pho"*, asset references (`all.min.css`, `jquery.min.js`, `apple-touch-icon.png`, `favicon-32x32.png`), and grid rule `.fa-xs { font-size:.75em }`.
4. **Interactive Detail & Feature Matrix (<div.first:nth(3)> — `Straw.Page`)**:
   - Landmark `<div class="first">` framing `Straw.Page` and `Extremely simple website builder` (*"Create websites from your phone"*) with `#ffff00` surface cards, `#ffff00` accents, and `.fa-sm { font-size:.875em }`.
5. **Colophon & Global Directory Footer (<footer.innerSun> — `https://straw.page`)**:
   - Landmark `<footer class="innerSun">` anchoring `Straw.Page - Extremely simple we` footer links (`Pricing · Twitter · Premium · Email · Terms`), copy *"A drag and drop website builder that works on mobile."*, and `#eeeeee` structural dividers.
