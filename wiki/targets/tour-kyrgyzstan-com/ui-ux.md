---
title: "UI & UX Architecture: tour-kyrgyzstan-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: tour-kyrgyzstan-com

## Overview & Design Identity
- **Target**: `tour-kyrgyzstan-com` (**Tour Kyrgyzstan — Central Asia, unmapped**)
- **Production URL**: [https://tour-kyrgyzstan.com/](https://tour-kyrgyzstan.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#dc2f02` accent)
- **Summary**: Discover authentic Kyrgyzstan tours. Mountain trekking, nomadic culture, and professional video production services.
- **Total Clean CSS Variables Extracted**: `6` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Fragment Mono`
- **Monospace / Technical Font Stack**: `Fragment Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48.96px`, `line-height: 47.9808px`, `font-weight: 800`, `letter-spacing: -0.9792px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 42px`, `line-height: 45.36px`, `font-weight: 800`, `letter-spacing: -0.84px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `body` (`font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dc2f02` | `.video-feature__watch:hover { background: #dc2f02 }` |
| **Interactive Accent / Highlight** | `#dc2f02` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#dc2f02` | `.footer__contacts a:hover { color: #dc2f02 }` |
| **Structural Hairline Border** | `#d1d1d1` | `.founder-grid { border: #d1d1d1 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#FFFFFF` | Canvas / Surface Token |
| `--ink` | `#000000` | Typography Ink Token |
| `--ink-soft` | `rgba(0,0,0,.65)` | Typography Ink Token |
| `--ink-faint` | `rgba(0,0,0,.45)` | Typography Ink Token |
| `--hero-vh` | `900px` | Layout / Spatial Grid Token |
| `--seg-w` | `30px` | Dimension / Scale Token |
| `--tour-kyrgyzstan--bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--tour-kyrgyzstan--ink` | `#000000` | Primary Typography Ink (computed-derived) |
| `--tour-kyrgyzstan--surface` | `#dc2f02` | Surface Substrate (computed-derived) |
| `--tour-kyrgyzstan--accent` | `#dc2f02` | Interactive Accent (computed-derived) |
| `--tour-kyrgyzstan--muted` | `#dc2f02` | Secondary Ink (computed-derived) |
| `--tour-kyrgyzstan--border` | `#d1d1d1` | Structural Border (computed-derived) |
| `--tour-kyrgyzstan--container` | `1400px` | Container Bound (computed-derived) |
| `--tour-kyrgyzstan--gap` | `8px` | Grid Gutter (computed-derived) |
| `--tour-kyrgyzstan--pad` | `40px` | Lateral Padding (computed-derived) |
| `--tour-kyrgyzstan--ease` | `cubic-bezier(.16,1,.3,1)` | Primary Easing Function |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `tour-kyrgyzstan-com`)**:
   - Landmark `<nav class="nav">` (`1400x60px`) hosting `Tour Kyrgyzstan — Central Asia, unma` navigation (`Gallery · Expeditions`), DOM attributes (`data-line="0"`, `data-line="1"`, `data-index="0"`, `data-index="1"`), and stylesheet rule `root { --paper: FFFFFF; --ink: 000000; --ink-soft: rgba(0,0,0,.65); --ink-faint... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `CENTRAL ASIA LIKE YOU'VE NEVER IMA`)**:
   - Landmark `<section class="hero">` presenting display lead `CENTRAL ASIA LIKE YOU'VE NEVER IMAGINED` and copy excerpt *"JOURNEYS WHICH DON'T EXIST IN GUIDEBOOKS. TREKKING, NOMADIC CULTU"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Central Asia like you've never ima`)**:
   - Landmark `<section class="section">` rendering section `Central Asia like you've never imagined` with copy *"K y r g y z s t a n i s h o m e t o u s . W e ' d l o v e t o s h"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `cassette.webp`), and grid rule `html { scroll-behavior: smooth; overflow-x: hidden; -webkit-text-size-adjust: 1... }`.
4. **Interactive Detail & Feature Matrix (<section.section:nth(2)> — `K y r g y z s t a n i s h o m e t `)**:
   - Landmark `<section class="section">` framing `K y r g y z s t a n i s h o m e t o u s . W e ' ` and `K y r g y z s t a n i s h o m e t o u s .` (*"K y r g y z s t a n i s h o m e t o u s ."*) with `#dc2f02` surface cards, `#dc2f02` accents, and `img { display: block; max-width: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tour-kyrgyzstan.com/`)**:
   - Landmark `<footer class="footer section--dark">` anchoring `Tour Kyrgyzstan — Central Asia, ` footer links (`Gallery · Expeditions`), copy *"W e ' d l o v e t o s h o w i t t o y o u ."*, and `#d1d1d1` structural dividers.
