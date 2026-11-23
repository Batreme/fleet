---
title: "UI & UX Architecture: chandebootcamp-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: chandebootcamp-com

## Overview & Design Identity
- **Target**: `chandebootcamp-com` (**Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam**)
- **Production URL**: [http://chandebootcamp.com/](http://chandebootcamp.com/)
- **Final Redirected URL**: [https://www.chandebootcamp.com/](https://www.chandebootcamp.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3eb` / `#236c3c`)
- **Summary**: Chande Bootcamp by Mingg is a retreat that connects Vietnamese designers: three days to listen, share and show the love at Ke Retreat, Ha...
- **Total Clean CSS Variables Extracted**: `77` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Phudu`
- **Body Font Stack**: `Phudu`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80.0244px`, `line-height: 57.6176px`, `font-weight: 700`, `letter-spacing: -3.20098px`); CSS variables `--g3-display: 'Phudu', ui-sans-serif, system-ui, sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 79.5px`, `line-height: 62.01px`, `font-weight: 700`, `letter-spacing: -3.18px`); rule `h2` (`font-size: max(2.2rem, calc(80 * var(--u)))`, `line-height: .8`, `letter-spacing: -.04em`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 600`); rule `body` (`font-weight: 600`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 11.52px`, `font-weight: 500`, `letter-spacing: -0.24px`); CSS variables `--mono: max(11px, calc(14 * var(--fu)))`, `--g3-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace`; rule `.mono` (`line-height: .96`, `letter-spacing: -.02em`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f3eb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f0e3` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#236c3c` | `.hs-foot__cta1 { background: #236c3c }` |
| **Secondary / Muted Copy** | `#838b89` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cbcbc4` | `var(--line)` in `:root` (`rgba(15,21,19,.18)`) |
| **Variable Token (`--panel`)** | `#1b2625` | `var(--panel)` in `:root` |
| **Variable Token (`--green`)** | `#245535` | `var(--green)` in `:root` |
| **Variable Token (`--lime`)** | `#68f12b` | `var(--lime)` in `:root` |
| **Variable Token (`--ink`)** | `#0f1513` | `var(--ink)` in `:root` |
| **Variable Token (`--cap-ink`)** | `#e9e2c8` | `var(--cap-ink)` in `:root` |
| **Variable Token (`--cap-block`)** | `#102a19` | `var(--cap-block)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cream` | `#f4f3eb` | Color / Atmospheric Token |
| `--panel` | `#1b2625` | Color / Atmospheric Token |
| `--green` | `#245535` | Color / Atmospheric Token |
| `--lime` | `#68f12b` | Color / Atmospheric Token |
| `--ink` | `#0f1513` | Typography Ink Token |
| `--bar` | `5rem` | Dimension / Scale Token |
| `--fold` | `calc(100svh - var(--bar))` | Dimension / Scale Token |
| `--img` | `25` | Design System Custom Token |
| `--cap` | `56` | Design System Custom Token |
| `--hi` | `calc(var(--img) * 1svh)` | Dimension / Scale Token |
| `--y3` | `calc(2 * var(--hi))` | Design System Custom Token |
| `--y4` | `calc(3 * var(--hi))` | Design System Custom Token |
| `--cap-bg` | `#236c3c` | Canvas / Surface Token |
| `--cap-ink` | `#e9e2c8` | Typography Ink Token |
| `--cap-block` | `#102a19` | Color / Atmospheric Token |
| `--tb` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.abs> — `chandebootcamp-com`)**:
   - Landmark `<nav class="abs pills">` (`320x56px`) hosting `Chande Bootcamp 2026 by Mingg Patreo` navigation (`Explore Gallery · About us`), DOM attributes (`data-chande-loading`, `data-chande-transition`, `data-barba="wrapper"`, `data-transition-wrap`), and stylesheet rule `body { overflow-x:clip; overscroll-behavior-x:none; -webkit-text-size-adjust:10... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `CHANDE BOOTCAMP BY. MINGG`)**:
   - Landmark `<section class="hero">` presenting display lead `CHANDE BOOTCAMP BY. MINGG` and copy excerpt *"Special event organized by Mingg Patreon - Design community"* over `#f4f3eb` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hs> — `Chande Bootcamp By. Mingg`)**:
   - Landmark `<section class="hs hs-intro">` rendering section `Chande Bootcamp By. Mingg` with copy *"2-4 October Ke Retreat - Hanoi, VN"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `.hero { transition:background-color .6s ease }`.
4. **Interactive Detail & Feature Matrix (<section.hs-story> — `An event for all designers to conn`)**:
   - Landmark `<section class="hs hs-story">` framing `An event for all designers to connect. Listen & s...` and `(12) Events at bootcamp` (*"A community connecting event for Vietnamese designers. In the mos"*) with `#f5f0e3` surface cards, `#236c3c` accents, and `.hero__intro-text { transition:color .6s ease }`.
5. **Colophon & Global Directory Footer (<footer.hs> — `http://chandebootcamp.com/`)**:
   - Landmark `<footer class="hs hs-foot">` anchoring `Chande Bootcamp 2026 by Mingg Pa` footer links (`Explore Gallery · About us`), copy *"[ UIUX design community ]"*, and `#cbcbc4` structural dividers.
