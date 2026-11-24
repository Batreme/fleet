---
title: "UI & UX Architecture: vivmgmt-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: vivmgmt-com

## Overview & Design Identity
- **Target**: `vivmgmt-com` (**Photographer Agency & Commercial Photo Production — ViV MGMT**)
- **Production URL**: [https://vivmgmt.com/](https://vivmgmt.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ebebeb` accent)
- **Summary**: Representing commercial photographers, directors, and creatives while providing full-service photo and video production for brands nation...
- **Total Clean CSS Variables Extracted**: `37` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica Now Display`
- **Body Font Stack**: `Helvetica Now Display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 24px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--media-seek-backward-button-display: none`, `--media-seek-forward-button-display: none`, `--media-playback-rate-button-display: none`; rule `h1` (`font-size: 16px`, `line-height: 150%`, `letter-spacing: .01em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96.0048px`, `line-height: 96.0048px`, `font-weight: 400`); rule `h2` (`font-size: 16px`, `line-height: 150%`, `letter-spacing: .01em`)
- **Body Copy**: live computed `body` (`font-size: 24px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: clamp(24px,8vw,44px)`, `line-height: 90%`, `letter-spacing: .01em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 24px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ebebeb` | `.c-btn { background-color: #ebebeb }` |
| **Interactive Accent / Highlight** | `#ebebeb` | `.c-btn { background-color: #ebebeb }` |
| **Secondary / Muted Copy** | `#878787` | `.c-artist__nav-btn { color: #878787 }` |
| **Structural Hairline Border** | `#878787` | hairline divider derived from `.c-artist__nav-btn { color: #878787 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-page-bg` | `#ffffff` | Canvas / Surface Token |
| `--color-page-text` | `#000000` | Typography Ink Token |
| `--space-xs` | `clamp(.3125rem, .2344rem + .3906vw, .625rem)` | Layout / Spatial Grid Token |
| `--space-s` | `clamp(.625rem, .4688rem + .7813vw, 1.25rem)` | Layout / Spatial Grid Token |
| `--space-m` | `clamp(1.25rem, .9375rem + 1.5625vw, 2.5rem)` | Layout / Spatial Grid Token |
| `--space-l` | `clamp(1.875rem, 1.4063rem + 2.3438vw, 3.75rem)` | Layout / Spatial Grid Token |
| `--space-xl` | `clamp(2.5rem, 1.875rem + 3.125vw, 5rem)` | Layout / Spatial Grid Token |
| `--space-2xl` | `clamp(3.125rem, 2.3438rem + 3.9063vw, 6.25rem)` | Layout / Spatial Grid Token |
| `--space-3xl` | `clamp(3.75rem, 2.8125rem + 4.6875vw, 7.5rem)` | Layout / Spatial Grid Token |
| `--space-4xl` | `clamp(4.375rem, 3.2813rem + 5.4688vw, 8.75rem)` | Layout / Spatial Grid Token |
| `--space-5xl` | `clamp(5rem, 3.75rem + 6.25vw, 10rem)` | Layout / Spatial Grid Token |
| `--space-xs-s` | `clamp(.3125rem, .0781rem + 1.1719vw, 1.25rem)` | Layout / Spatial Grid Token |
| `--space-s-m` | `clamp(.625rem, .1563rem + 2.3438vw, 2.5rem)` | Layout / Spatial Grid Token |
| `--space-m-l` | `clamp(1.25rem, .625rem + 3.125vw, 3.75rem)` | Layout / Spatial Grid Token |
| `--space-l-xl` | `clamp(1.875rem, 1.0938rem + 3.9063vw, 5rem)` | Layout / Spatial Grid Token |
| `--space-xl-2xl` | `clamp(2.5rem, 1.5625rem + 4.6875vw, 6.25rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.c-navbar> — `vivmgmt-com`)**:
   - Landmark `<nav class="c-navbar">` (`1440x41px`) hosting `Photographer Agency & Commercial Pho` navigation (`ViV Management · Artists · News · About · All`), DOM attributes (`data-col="1"`, `data-href="/artist/edward-tran"`, `data-cycle="[("t":"img","url":"ht..."`, `data-col="2"`), and stylesheet rule `html { box-sizing:border-box;-ms-overflow-style:scrollbar }`.
2. **Hero Stage & Focal Lead (<section.c-home__gallery> — `ViV — artist management + producti`)**:
   - Landmark `<section class="c-home__gallery">` presenting display lead `ViV — artist management + production` and copy excerpt *"Artist management + production."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.c-home__gallery:nth(2)> — `ARTURO TORRES x MARINE LAYER`)**:
   - Landmark `<section class="c-home__gallery">` rendering section `ARTURO TORRES x MARINE LAYER` with copy *"ViV is an artist management and production company."*, asset references (`www.datocms-assets.com`, `image.mux.com`, `stream.mux.com`, `GaramondNarrow-Regular.woff2`), and grid rule `after { box-sizing:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.c-home__gallery:nth(3)> — `DANIELLE MOORE x OLD NAVY BTS`)**:
   - Landmark `<section class="c-home__gallery">` framing `DANIELLE MOORE x OLD NAVY BTS` and `JONATHAN MANNION x NIKE` (*"V i V i s a n a r t i s t m a n a g e m e n t a n d p r o d u c t"*) with `#ebebeb` surface cards, `#ebebeb` accents, and `.container { position:relative;margin-left:auto;margin-right:auto;padding-right:10px;... }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://vivmgmt.com/`)**:
   - Landmark `<footer class="c-footer">` anchoring `Photographer Agency & Commercial` footer links (`ViV Management · Artists · News · About · All`), copy *"m a n a g e m e n t"*, and `#878787` structural dividers.
