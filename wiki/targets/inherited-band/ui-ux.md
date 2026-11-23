---
title: "UI & UX Architecture: inherited-band"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: inherited-band

## Overview & Design Identity
- **Target**: `inherited-band` (**INHERITED**)
- **Production URL**: [https://inherited.band/](https://inherited.band/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×844px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#eee2c5` ink, `#fcfffe` accent)
- **Summary**: INHERITED BAND
- **Total Clean CSS Variables Extracted**: `5` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Founders Grotesk`
- **Body Font Stack**: `Founders Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 103.5px`, `line-height: 103.5px`, `font-weight: 700`, `letter-spacing: -10.35px`); rule `.h1` (`line-height: .85`, `letter-spacing: -.1em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 22.5px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.3375px`)
- **Body Copy**: live computed `body` (`font-size: 13.5px`, `line-height: 16.335px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13.5px`, `line-height: 16.335px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#eee2c5` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d50305` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#fcfffe` | `<meta name="theme-color" content="#FCFFFE">` in `dom.html` |
| **Secondary / Muted Copy** | `#eee2c5` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#eee2c5` | hairline divider derived from secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--margin` | `20rem` | Layout / Spatial Grid Token |
| `--gap` | `20rem` | Layout / Spatial Grid Token |
| `--column` | `calc((var(--rvw) * 100 - var(--margin) * 2 - var(--gap) * 5) / 6)` | Layout / Spatial Grid Token |
| `--rvw` | `14.4px` | Layout / Spatial Grid Token |
| `--right-height` | `692px` | Layout / Spatial Grid Token |
| `--inherited-band-bg` | `#000000` | Canvas Substrate (from live computed `html` `background-color` (`computed_styles.json`)) |
| `--inherited-band-ink` | `#eee2c5` | Primary Typography Ink (computed-derived) |
| `--inherited-band-surface` | `#d50305` | Surface Substrate (computed-derived) |
| `--inherited-band-accent` | `#fcfffe` | Interactive Accent (computed-derived) |
| `--inherited-band-muted` | `#eee2c5` | Secondary Ink (computed-derived) |
| `--inherited-band-border` | `#eee2c5` | Structural Border (computed-derived) |
| `--inherited-band-container` | `1440px` | Container Bound (computed-derived) |
| `--inherited-band-gap` | `18px` | Grid Gutter (computed-derived) |
| `--inherited-band-pad` | `18px` | Lateral Padding (computed-derived) |
| `--inherited-band-ease` | `cubic-bezier(.6,.14,0,1)` | Primary Easing Function |
| `--inherited-band-radius` | `0px` | Corner Radius (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `inherited-band`)**:
   - Landmark `<header class="header">` (`1440x900px`) hosting `INHERITED` navigation (`INHERITED · Spotify · Instagram · Tik Tok · Contact us`), DOM attributes (`data-touch="false"`, `data-custom-loaded="true"`, `data-title="about"`, `data-title="members"`), and stylesheet rule `body { font-size:15rem;line-height:1.21;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.member> — `I N H E R I T E D`)**:
   - Landmark `<section class="member show">` presenting display lead `I N H E R I T E D` and copy excerpt *"Metalcore Deathcore"* over `#000000` canvas and `#eee2c5` ink.
3. **Primary Showcase & Content Grid (<section.no-transition> — `2016 Deathcore Metalcore`)**:
   - Landmark `<section class="member no-transition">` rendering section `2016 Deathcore Metalcore` with copy *"Guitarist Producer"*, asset references (`fav.ico`, `fav.svg`, `fav-mask.svg`, `apple-touch.png`), and grid rule `.h3 { line-height:1;letter-spacing:-.015em;margin:0;text-transform:uppercase;f... }`.
4. **Interactive Detail & Feature Matrix (<section.member:nth(2)> — `E d e r A n a y a`)**:
   - Landmark `<section class="member no-transition">` framing `E d e r A n a y a` and `( Me, Myself, and Sam )` (*"( Me, Myself, and Sam )"*) with `#d50305` surface cards, `#fcfffe` accents, and `.h1 { font-size:115rem }`.
5. **Colophon & Global Directory Footer (<footer.items> — `https://inherited.band/`)**:
   - Landmark `<footer class="items">` anchoring `INHERITED` footer links (`INHERITED · Spotify · Instagram · Tik Tok · Contact us`), copy *"E d e r A n a y a"*, and `#eee2c5` structural dividers.
