---
title: "UI & UX Architecture: www-alpineguides-co-nz"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-alpineguides-co-nz

## Overview & Design Identity
- **Target**: `www-alpineguides-co-nz` (**Alpine Guides Aoraki · NZ Mountain Guiding Since 1966**)
- **Production URL**: [https://www.alpineguides.co.nz/](https://www.alpineguides.co.nz/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#191919` canvas, `#ffffff` ink, `#ffcc00` accent)
- **Summary**: Explore guided ascents, mountaineering courses, ski touring, Tasman Glacier heli-hike and alpine adventures in Aoraki/Mount Cook with pro...
- **Total Clean CSS Variables Extracted**: `236` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Mozillaheadline Variablefont Wdth Wght`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 112px`, `line-height: 100.8px`, `font-weight: 800`, `letter-spacing: -3.2px`); CSS variables `--_responsive---h1: 7rem`, `--_responsive---h1-line-height: .5rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 43.2px`, `font-weight: 600`, `letter-spacing: -0.96px`); CSS variables `--_responsive---h2: 3rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--_responsive---paragraph: 1.4rem`, `--_responsive---paragraph_small: 1rem`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14.4px`, `line-height: 15px`, `font-weight: 200`, `letter-spacing: 0.8px`); CSS variables `--_text-syle---letter-spacing: 0rem`, `--_responsive---spacer-small: .7rem`, `--_responsive---paragraph_small: 1rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#191919` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#343435` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffcc00` | `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }` |
| **Secondary / Muted Copy** | `#333333` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--_theme---agl-gold`)** | `#fcb124` | `var(--_theme---agl-gold)` in `:root` |
| **Variable Token (`--_theme---white`)** | `#f2f2f3` | `var(--_theme---white)` in `:root` |
| **Variable Token (`--_theme---carbon`)** | `#1e1e1e` | `var(--_theme---carbon)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_text-syle---font-family` | `Robotocondensed, Arial, sans-serif` | Typography Ink Token |
| `--_theme---color--heading` | `var(--_theme---white)` | Typography Ink Token |
| `--_responsive---h1` | `7rem` | Typography / Scale Token |
| `--_text-syle---line-height` | `1.25` | Typography Ink Token |
| `--_text-syle---font-weight` | `200` | Typography Ink Token |
| `--_text-syle---letter-spacing` | `0rem` | Typography Ink Token |
| `--_responsive---h2` | `3rem` | Typography / Scale Token |
| `--_theme---color--eyebrow` | `var(--_theme---agl-gold)` | Brand / Palette Token |
| `--_text-syle---text-size` | `var(--_responsive---paragraph)` | Typography Ink Token |
| `--_theme---color--text` | `var(--_theme---white)` | Typography Ink Token |
| `--_responsive---paragraph` | `1.4rem` | Typography / Scale Token |
| `--_theme---agl-gold` | `#fcb124` | Brand / Palette Token |
| `--_theme---color--border` | `var(--_theme---ash)` | Brand / Palette Token |
| `--_theme---color--background` | `var(--_theme---black)` | Canvas / Surface Token |
| `--_theme---white` | `#f2f2f3` | Canvas / Surface Token |
| `--_theme---carbon` | `#1e1e1e` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-alpineguides-co-nz`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `Alpine Guides Aoraki · NZ Mountain G` navigation (`prepare · contact us · alpine hiking · learn the ropes · guided ascents`), DOM attributes (`data-wf-domain="www.alpineguides.co.nz"`, `data-wf-page="6948a91537f8a4167b84e785"`, `data-wf-site="6948a91537f8a4167b84e770"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.explore-mega> — `Expert Mountain Adventures Since 1`)**:
   - Landmark `<section class="explore-mega">` presenting display lead `Expert Mountain Adventures Since 1966` and copy excerpt *"Alpine Guides offers unmatched access to the vast mountain playgr"* over `#191919` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.prepare-mega> — `Alpine Guides offers unmatched acc`)**:
   - Landmark `<section class="prepare-mega">` rendering section `Alpine Guides offers unmatched access to the vas` with copy *"A spectacular heli-hike experience exploring the white ice of New"*, asset references (`cdn.prod.website-files.com`, `alpine-guides.webflow.shared.ac09...`, `www-widgetapi.js`, `recaptcha__en.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.c-hero> — `A spectacular heli-hike experience`)**:
   - Landmark `<section class="c-hero">` framing `A spectacular heli-hike experience exploring the` and `A 7-day intermediate-level course teaching an in` (*"A 7-day intermediate-level course teaching an introduction to mod"*) with `#343435` surface cards, `#ffcc00` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.alpineguides.co.nz/`)**:
   - Landmark `<footer class="footer">` anchoring `Alpine Guides Aoraki · NZ Mounta` footer links (`prepare · contact us · alpine hiking · learn the ropes · guided ascents`), copy *"A tailor-made package for bespoke mountaineering and ski tou"*, and `#3898ec` structural dividers.
