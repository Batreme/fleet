# UI & UX Architecture: tour-kyrgyzstan-com

## Overview & Design Identity
- **Target**: `tour-kyrgyzstan-com` (**Tour Kyrgyzstan — Central Asia, unmapped**)
- **Production URL**: [https://tour-kyrgyzstan.com/](https://tour-kyrgyzstan.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#FFFFFF` canvas, `#000000` ink, `#fff` accent)
- **Summary**: Discover authentic Kyrgyzstan tours. Mountain trekking, nomadic culture, and professional video production services.
- **Total Clean CSS Variables Extracted**: `6` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Fragment Mono`
- **Monospace / Technical Font Stack**: `Fragment Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`)
- **Body Copy**: rule `body` (`font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#FFFFFF` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#000000` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dc2f02` | `.nav__links a:hover { color: #dc2f02 }` |
| **Interactive Accent / Highlight** | `#fff` | `.nav__mobile-menu > a { color: #fff }` |
| **Secondary / Muted Copy** | `#b52501` | `.hero__cta:hover { background: #b52501 }` |
| **Structural Hairline Border** | `#0d0d0d` | `.section--dark { background: #0d0d0d }` |

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
| `--tour-kyrgyzstan--bg` | `#FFFFFF` | Canvas Substrate (from `var(--paper)` in `:root`) |
| `--tour-kyrgyzstan--ink` | `#000000` | Primary Typography Ink (stylesheet-derived) |
| `--tour-kyrgyzstan--surface` | `#dc2f02` | Surface Substrate (stylesheet-derived) |
| `--tour-kyrgyzstan--accent` | `#fff` | Interactive Accent (stylesheet-derived) |
| `--tour-kyrgyzstan--muted` | `#b52501` | Secondary Ink (stylesheet-derived) |
| `--tour-kyrgyzstan--border` | `#0d0d0d` | Structural Border (stylesheet-derived) |
| `--tour-kyrgyzstan--container` | `1400px` | Container Bound (stylesheet-derived) |
| `--tour-kyrgyzstan--gap` | `8px` | Grid Gutter (stylesheet-derived) |
| `--tour-kyrgyzstan--pad` | `24px` | Lateral Padding (stylesheet-derived) |
| `--tour-kyrgyzstan--ease` | `cubic-bezier(.16,1,.3,1)` | Primary Easing Function |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `tour-kyrgyzstan-com`)**:
   - Landmark `<nav class="nav">` hosting `Tour Kyrgyzstan — Central Asia, unma` navigation (`Gallery · Expeditions`), DOM attributes (`data-line="0"`, `data-line="1"`, `data-index="0"`, `data-index="1"`), and stylesheet rule `root { --paper: FFFFFF; --ink: 000000; --ink-soft: rgba(0,0,0,.65); --ink-faint... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Central Asia like you've never ima`)**:
   - Landmark `<section class="hero">` presenting display lead `Central Asia like you've never imagined` and copy excerpt *"K y r g y z s t a n i s h o m e t o u s . W e ' d l o v e t o s h"* over `#FFFFFF` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Journeys, which don't exist in gui`)**:
   - Landmark `<section class="section">` rendering section `Journeys, which don't exist in guidebooks` with copy *"K y r g y z s t a n i s h o m e t o u s ."*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `cassette.webp`), and grid rule `html { scroll-behavior: smooth; overflow-x: hidden; -webkit-text-size-adjust: 1... }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Immersive nomadic experience`)**:
   - Landmark `<section class="section">` framing `Immersive nomadic experience` and `We also provide professional production services` (*"W e ' d l o v e t o s h o w i t t o y o u ."*) with `#dc2f02` surface cards, `#fff` accents, and `img { display: block; max-width: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tour-kyrgyzstan.com/`)**:
   - Landmark `<footer class="footer section--dark">` anchoring `Tour Kyrgyzstan — Central Asia, ` footer links (`Gallery · Expeditions`), copy *"Cycling Expedition"*, and `#0d0d0d` structural dividers.
