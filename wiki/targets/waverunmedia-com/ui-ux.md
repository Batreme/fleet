---
title: "UI & UX Architecture: waverunmedia-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: waverunmedia-com

## Overview & Design Identity
- **Target**: `waverunmedia-com` (**WaveRun Media**)
- **Production URL**: [https://waverunmedia.com/](https://waverunmedia.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#0000ff` accent)
- **Summary**: WaveRun Media captures the pulse of real stories that move markets and shape culture.
- **Total Clean CSS Variables Extracted**: `103` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Satoshi`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 86.4px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50.4px`, `line-height: 55.44px`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#4b4b4b` | `.deco-lines--grey div { background-color: #4b4b4b }` |
| **Interactive Accent / Highlight** | `#0000ff` | `var(--wndb--color--primary)` in `:root` |
| **Secondary / Muted Copy** | `#0000ff` | `var(--wndb--color--secondary)` in `:root` |
| **Structural Hairline Border** | `#00a0d2` | `.wpcf7 form .wpcf7-response-output { border: #00a0d2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wndb-mask-color` | `rgba(0,0,0,.15)` | Brand / Palette Token |
| `--wndb-mask-position` | `50% 50% at 50% 20%` | Dimension / Scale Token |
| `--wndb-mask-opacity` | `0.35` | Design System Custom Token |
| `--nfd-wb-anim-transition-duration` | `1400ms` | Motion / Easing Token |
| `--nfd-wb-anim-transition-delay` | `50ms` | Motion / Easing Token |
| `--nfd-wb-anim-transition-easing-function` | `cubic-bezier(0.4,1,0.65,1)` | Motion / Easing Token |
| `--slide-media-height` | `98.8vw` | Layout / Spatial Grid Token |
| `--wndb--max-w--prose` | `min(65ch,1100px)` | Layout / Spatial Grid Token |
| `--wndb--text-scale-factor` | `1` | Typography Ink Token |
| `--wndb--text--xs` | `0.75rem` | Typography Ink Token |
| `--wndb--text--sm` | `0.875rem` | Typography Ink Token |
| `--wndb--text--base` | `1rem` | Typography Ink Token |
| `--wndb--text--md` | `1.125rem` | Typography Ink Token |
| `--wndb--text--lg` | `1.5rem` | Typography Ink Token |
| `--wndb--text--xl` | `2.375rem` | Typography Ink Token |
| `--wndb--text--huge` | `clamp(2.75rem,1.4688rem + 2.5vw,3.5rem)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `waverunmedia-com`)**:
   - Landmark `<header class="header js-header">` (`1440x80px`) hosting `WaveRun Media` navigation (`Home · About · Partners · KWILL Advisors · ADTV`), DOM attributes (`data-globals="("ajax_url":"https://..."`, `data-video-ready="true"`, `data-video-ready="true"`, `data-from="center"`), and stylesheet rule `html { font-size:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<article.universal> — `the flow of culture`)**:
   - Landmark `<article class="universal">` presenting display lead `the flow of culture` and copy excerpt *"WaveRun Media captures the pulse of real stories that move market"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Stories in Motion`)**:
   - Landmark `<section class="hero hero--bottom">` rendering section `Stories in Motion` with copy *"Featuring Rashauna Scott"*, asset references (`apple-icon-57x57.png`, `apple-icon-60x60.png`, `apple-icon-72x72.png`, `apple-icon-76x76.png`), and grid rule `a:active { outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.slider-block> — `Flippin’ in Heels`)**:
   - Landmark `<section class="slider-block">` framing `Flippin’ in Heels` and `The Elevator Pitch` (*"Featuring Kareem Edwards"*) with `#4b4b4b` surface cards, `#0000ff` accents, and `strong { font-weight:700 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://waverunmedia.com/`)**:
   - Landmark `<footer class="footer">` anchoring `WaveRun Media` footer links (`Home · About · Partners · KWILL Advisors · ADTV`), copy *"New Killah Priest video"*, and `#00a0d2` structural dividers.
