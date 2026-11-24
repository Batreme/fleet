---
title: "UI & UX Architecture: faithibiza-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: faithibiza-com

## Overview & Design Identity
- **Target**: `faithibiza-com` (**Faith Ibiza · VIP Ibiza Concierge Services**)
- **Production URL**: [https://faithibiza.com/](https://faithibiza.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#eeebe4` canvas, `#4c5b6b` ink, `#204ce5` accent)
- **Summary**: Travelling to Ibiza and looking for a VIP experience? Our concierge services will ensure you experience all that the White Isle has to of...
- **Total Clean CSS Variables Extracted**: `242` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Eastern Harrogate`
- **Body Font Stack**: `Afacad Flux`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 149.999px`, `line-height: 164.999px`, `font-weight: 400`); rule `h1` (`font-size: 2.5em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 110px`, `line-height: 121px`, `font-weight: 400`); rule `h2` (`font-size: 2em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 10px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--modal-size-small: 500px`, `--gf-label-width: 30%`, `--gf-label-req-gap: 6px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#eeebe4` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#4c5b6b` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#204ce5` | `var(--gf-color-primary)` in `:root` |
| **Secondary / Muted Copy** | `#8daeb6` | `var(--c-secondary)` in `:root` |
| **Structural Hairline Border** | `#d4c9ff` | `var(--outline-purple)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--cookieadmin-primary-color`)** | `#001d39` | `var(--cookieadmin-primary-color)` in `:root` |
| **Variable Token (`--cookieadmin-primary-hover-color`)** | `#985e23` | `var(--cookieadmin-primary-hover-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--i-star` | `url(https://faithibiza.com/wp-content/themes/general-block-wp/img/star.svg)` | Dimension / Scale Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--cookieadmin-primary-color` | `#001d39` | Brand / Palette Token |
| `--cookieadmin-primary-hover-color` | `#985e23` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `faithibiza-com`)**:
   - Landmark `<header class="site-header">` (`1440x0px`) hosting `Faith Ibiza · VIP Ibiza Concierge Se` navigation (`About · About Us · Charity Work · Latest News · Where to stay`), DOM attributes (`data-optimized="1"`, `data-optimized="1"`, `data-optimized="2"`, `data-optimized="1"`), and stylesheet rule `ideo.background::-webkit-media-co... { display:none!important;opacity:0 }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `unforgettable`)**:
   - Landmark `<main class="site-main">` presenting display lead `unforgettable` and copy excerpt *"Your holiday shouldn’t be spent worrying about bookings, transfer"* over `#eeebe4` canvas and `#4c5b6b` ink.
3. **Primary Showcase & Content Grid (<main.site-main:nth(2)> — `For the best Ibiza experience...`)**:
   - Landmark `<main class="site-main">` rendering section `For the best Ibiza experience...` with copy *"Use Up/Down Arrow keys to increase or decrease volume."*, asset references (`recaptcha__en.js`, `cdn.jsdelivr.net`, `unpkg.com`, `www.google.com`), and grid rule `it-media-controls-start-playback-... { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<main.site-main:nth(3)> — `Book with Faith`)**:
   - Landmark `<main class="site-main">` framing `Book with Faith` and `COME FOR THE BEACHES` (*"Exceptional island knowledge to ensure your stay in Ibiza is unfo"*) with `#dddddd` surface cards, `#204ce5` accents, and `root { --wp-admin-border-width-focus:1.5px }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://faithibiza.com/`)**:
   - Landmark `<footer class="site-footer is-dark">` anchoring `Faith Ibiza · VIP Ibiza Concierg` footer links (`About · About Us · Charity Work · Latest News · Where to stay`), copy *"PART OF THE O BEACH GROUP"*, and `#d4c9ff` structural dividers.
