---
title: "UI & UX Architecture: relevovinco-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: relevovinco-com

## Overview & Design Identity
- **Target**: `relevovinco-com` (**Relevo & Vinco — inkless packaging, pressed into the board**)
- **Production URL**: [https://relevovinco.com/](https://relevovinco.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#d4b08f` canvas, `#36261a` ink, `#6b4c34` accent)
- **Summary**: Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, die-cut and fold raw board so a brand is something people fe...
- **Total Clean CSS Variables Extracted**: `29` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 34px`, `line-height: 52.7px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 86.4px`, `line-height: 79.488px`, `font-weight: 700`, `letter-spacing: 0.864px`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`); rule `p` (`font-size: clamp(26px,2.8vw,42px)`, `line-height: 1.12`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#d4b08f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#36261a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#47331f` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#6b4c34` | live computed `h2` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#6b4c34` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#6b4c34` | hairline divider derived from live computed `h2` `color` (`computed_styles.json`) |
| **Variable Token (`--color-3`)** | `#f7e8d2` | `var(--color-3)` in `:root` |
| **Variable Token (`--color-6`)** | `#1f140b` | `var(--color-6)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-1` | `#d4b08f` | Brand / Palette Token |
| `--color-2` | `#36261a` | Brand / Palette Token |
| `--color-3` | `#f7e8d2` | Brand / Palette Token |
| `--color-4` | `#6b4c34` | Brand / Palette Token |
| `--color-5` | `#47331f` | Brand / Palette Token |
| `--color-6` | `#1f140b` | Brand / Palette Token |
| `--font-1` | `"Gabarito", "Gabarito Fallback", "Arial", sans-serif` | Typography / Scale Token |
| `--font-2` | `"Instrument Sans", "Instrument Sans Fallback", "Arial", sans-serif` | Typography / Scale Token |
| `--radius-1` | `6px` | Elevation / Border Token |
| `--radius-2` | `50%` | Elevation / Border Token |
| `--radius-3` | `clamp(18px, 2.4vw, 34px)` | Elevation / Border Token |
| `--shadow-7` | `1px 1px 0 color-mix(in srgb, var(--color-3) 75%, transparent)` | Elevation / Border Token |
| `--shadow-14` | `10px 16px 18px color-mix(in srgb, var(--color-6) 32%, transparent)` | Elevation / Border Token |
| `--space-1` | `clamp(20px, 6.5vw, 96px)` | Layout / Spatial Grid Token |
| `--space-2` | `clamp(96px, 15vh, 180px)` | Layout / Spatial Grid Token |
| `--hero-cap` | `min(16vh, 11.2vw)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `relevovinco-com`)**:
   - Landmark `<header class="lenis">` (`1440x68px`) hosting `Relevo & Vinco — inkless packaging, ` navigation (`Finishes · Process · Work · Boards · Contact`), DOM attributes (`data-fonts`, `data-part="layers"`, `data-part="tokens"`, `data-part="base"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.relief-defs> — `STAND OUT. PRESS IN.`)**:
   - Landmark `<section class="relief-defs">` presenting display lead `STAND OUT. PRESS IN.` and copy excerpt *"Relevo & Vinco is an inkless packaging workshop in Porto. We embo"* over `#d4b08f` canvas and `#36261a` ink.
3. **Primary Showcase & Content Grid (<section.relief-defs__shade> — `Stand out. Press in.`)**:
   - Landmark `<section class="relief-defs__shade">` rendering section `Stand out. Press in.` with copy *"Order a sample kit"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `gabarito-a94f9001.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.nav__bar> — `Ink fades. Foil peels. Pressure st`)**:
   - Landmark `<section class="nav__bar">` framing `Ink fades. Foil peels. Pressure stays.` and `Six ways to say it without ink` (*"Every box we make carries its brand in the board itself: raised w"*) with `#47331f` surface cards, `#6b4c34` accents, and `img { display:block;max-width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://relevovinco.com/`)**:
   - Landmark `<footer class="m-text-3">` anchoring `Relevo & Vinco — inkless packagi` footer links (`Finishes · Process · Work · Boards · Contact`), copy *"Nothing to scuff off in transit and nothing to separate at t"*, and `#6b4c34` structural dividers.
