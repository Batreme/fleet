---
title: "UI & UX Architecture: www-rebelliously-optimistic-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-rebelliously-optimistic-com

## Overview & Design Identity
- **Target**: `www-rebelliously-optimistic-com` (**Rebelliously Optimistic — A movement for the human future**)
- **Production URL**: [https://www.rebelliously-optimistic.com/](https://www.rebelliously-optimistic.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0a66c2`)
- **Summary**: A movement for the human future in the age of AI. Quarterly gatherings and Human Notes for people who refuse to let progress be anything...
- **Total Clean CSS Variables Extracted**: `16` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(38px,5vw,56px)`, `line-height: 1.05`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96px`, `line-height: 96px`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: calc(6em + 13.3px)`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `.meta` (`font-size: 13px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7f0e1` | `.ro-voices-dialog { background: #f7f0e1 }` |
| **Interactive Accent / Highlight** | `#0a66c2` | `.sign-studio .btn-li { background: #0a66c2 }` |
| **Secondary / Muted Copy** | `#b9a39f` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#cfc6ca` | `var(--line)` in `:root` (`3e1c2a40`) |
| **Variable Token (`--line`)** | `#3e1c2a` | `var(--line)` in `:root` |
| **Variable Token (`--line-cream`)** | `#f3ebd9` | `var(--line-cream)` in `:root` |
| **Variable Token (`--bg`)** | `#1c0c14` | `var(--bg)` in `:root` |
| **Variable Token (`--accent`)** | `#c2676a` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-ink`)** | `#fff6e8` | `var(--accent-ink)` in `:root` |
| **Variable Token (`--focus`)** | `#f0b3a6` | `var(--focus)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--line` | `#3e1c2a40` | Color / Atmospheric Token |
| `--line-soft` | `#3e1c2a1f` | Color / Atmospheric Token |
| `--line-faint` | `#3e1c2a14` | Color / Atmospheric Token |
| `--line-cream` | `#f3ebd938` | Color / Atmospheric Token |
| `--line-cream-soft` | `#f3ebd91f` | Color / Atmospheric Token |
| `--bg` | `#1c0c14` | Canvas / Surface Token |
| `--ink` | `#f3ebd9` | Typography Ink Token |
| `--muted` | `#b9a39f` | Color / Atmospheric Token |
| `--faint` | `#f3ebd924` | Color / Atmospheric Token |
| `--chip` | `#f3ebd912` | Color / Atmospheric Token |
| `--accent` | `#c2676a` | Brand / Palette Token |
| `--accent-ink` | `#fff6e8` | Typography Ink Token |
| `--focus` | `#f0b3a6` | Color / Atmospheric Token |
| `--sans` | `"Instrument Sans", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--serif` | `"Instrument Serif", Georgia, "Times New Roman", serif` | Typography / Scale Token |
| `--lightningcss-dark` | `initial` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `www-rebelliously-optimistic-com`)**:
   - Landmark `<header class="top-0 left-0">` (`1440x67px`) hosting `Rebelliously Optimistic — A movement` navigation (`The Experience · Human Notes · Sign manifesto`), DOM attributes (`data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`, `data-engine="three.js r184"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.hidden> — `Rebelliously Optimistic — A moveme`)**:
   - Landmark `<section class="hidden relative">` presenting display lead `Rebelliously Optimistic — A movement for the hum` and copy excerpt *"Rebelliously Optimistic is an ongoing quarterly leadership experi"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="bg-background text-foreground">` rendering section `Featured Work & Interactive Showcase` with copy *"Elevating shared humanity in the age of AI."*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="relative z-10">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"W r i t e i t i n a h u m a n v o i c e ."*) with `#f7f0e1` surface cards, `#0a66c2` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bottom-0> — `https://www.rebelliously-optimistic.com/`)**:
   - Landmark `<footer class="bottom-0 left-0">` anchoring `Rebelliously Optimistic — A move` footer links (`The Experience · Human Notes · Sign manifesto`), copy *"A leadership experience and people movement for those who be"*, and `#cfc6ca` structural dividers.
