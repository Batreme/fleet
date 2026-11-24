---
title: "UI & UX Architecture: webdesign-kernjosh-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: webdesign-kernjosh-com

## Overview & Design Identity
- **Target**: `webdesign-kernjosh-com` (**Josh Kern**)
- **Production URL**: [https://webdesign.kernjosh.com](https://webdesign.kernjosh.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f1e6` / `#007aff`)
- **Summary**: Josh Kern - webdesign and dev. Some work, info, and how to get in touch.
- **Total Clean CSS Variables Extracted**: `64` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 15.3px`, `line-height: 26.775px`, `font-weight: 400`); CSS variables `--about-font-display: "UglyDave", cursive`; rule `h1` (`font-size: clamp(.9rem,1.7vmin,1.1rem)`, `line-height: 1.75`, `font-weight: inherit`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 26.4px`, `font-weight: 400`, `letter-spacing: -0.24px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--about-font-body: "DM Sans", sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--about-font-label: "DM Sans", sans-serif`, `--about-label-size: .98rem`, `--about-label-tracking: -.005em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f1e6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c0908` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ece3cb` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#007aff` | `.mail-nav__btn { color: #007aff }` |
| **Secondary / Muted Copy** | `#3f3f3f` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#8b8983` | `.nico-batt { border: #8b8983 }` |
| **Variable Token (`--base-200`)** | `#e0dfd7` | `var(--base-200)` in `:root` |
| **Variable Token (`--base-300`)** | `#5f5f5f` | `var(--base-300)` in `:root` |
| **Variable Token (`--kuli-ground`)** | `#e6dfd0` | `var(--kuli-ground)` in `:root` |
| **Variable Token (`--buy-bg`)** | `#2a1d15` | `var(--buy-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-100` | `#f5f1e6` | Color / Atmospheric Token |
| `--base-200` | `#e0dfd7` | Color / Atmospheric Token |
| `--base-300` | `#5f5f5f` | Color / Atmospheric Token |
| `--base-350` | `#3f3f3f` | Color / Atmospheric Token |
| `--base-400` | `#0c0908` | Color / Atmospheric Token |
| `--kuli-pad-top` | `clamp(8.5rem, 18vh, 11.5rem)` | Layout / Spatial Grid Token |
| `--kuli-thumb-h` | `clamp(3rem, 7vh, 4.5rem)` | Dimension / Scale Token |
| `--kuli-ground` | `#e6dfd0` | Color / Atmospheric Token |
| `--kuli-line-h` | `9px` | Dimension / Scale Token |
| `--buy-bg` | `#2a1d15` | Canvas / Surface Token |
| `--kuli-box-ink` | `6px` | Typography Ink Token |
| `--kuli-phone-ratio` | `720 / 1278` | Design System Custom Token |
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--ease-spring` | `cubic-bezier(.34, 1.56, .64, 1)` | Motion / Easing Token |
| `--frame-w` | `min(calc(62vh * 16 / 10), 88vw)` | Dimension / Scale Token |
| `--enter-op` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `webdesign-kernjosh-com`)**:
   - Landmark `<nav class="nav">` (`1440x42px`) hosting `Josh Kern` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-landscape="primary"`, `data-back-pill`, `data-back-arrow-path`, `data-work-open`), and stylesheet rule `selection { color:0a0a0a;background:fff19a }`.
2. **Hero Stage & Focal Lead (<section.desk> — `Hey my name is Josh and I cool web`)**:
   - Landmark `<section class="desk">` presenting display lead `Hey my name is Josh and I cool websites :)` and copy excerpt *"I ask a lot of questions because I want the website to feel like "* over `#f5f1e6` canvas and `#0c0908` ink.
3. **Primary Showcase & Content Grid (<section.work-stage> — `Getting to know you`)**:
   - Landmark `<section class="work-stage">` rendering section `Getting to know you` with copy *"1 Getting to know you I ask a lot of questions because I want the"*, asset references (`favicon.png`, `apple-touch-icon.png`, `challenges.cloudflare.com`, `main-CwptEoZ4.js`), and grid rule `font-face { font-family:Outfit;src:url(/assets/Outfit-Variable-D6ftewdU.woff2)format... }`.
4. **Interactive Detail & Feature Matrix (<section.process-shell> — `Building the site`)**:
   - Landmark `<section class="process-shell">` framing `Building the site` and `Handover & going live` (*"I start exploring ideas for the landing page by throwing a lot of"*) with `#ece3cb` surface cards, `#007aff` accents, and `root { --base-100:f5f1e6;--base-200:e0dfd7;--base-300:5f5f5f;--base-350:3f3f3f;... }`.
5. **Colophon & Global Directory Footer (<footer.legal-footer> — `https://webdesign.kernjosh.com`)**:
   - Landmark `<footer class="legal-footer">` anchoring `Josh Kern` footer links (`Overview · Index · Archive · About · Contact`), copy *"3 Building the site I build everything with custom code, add"*, and `#8b8983` structural dividers.
