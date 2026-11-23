---
title: "UI & UX Architecture: auge-xp-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: auge-xp-com

## Overview & Design Identity
- **Target**: `auge-xp-com` (**Digital Experience Studio · AUGE Experience**)
- **Production URL**: [https://auge-xp.com/](https://auge-xp.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×940px`, Mobile `390×884px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#edeee5` / `#fdf48b`)
- **Summary**: AUGE Experience is an independent digital experience studio creating websites, digital products, interactive installations and creative t...
- **Total Clean CSS Variables Extracted**: `37` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ppNeueMontreal`
- **Body Font Stack**: `ppNeueMontreal`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--font-farnham-display: "farnhamDisplay", "farnhamDisplay Fallback"`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 28.5px`, `line-height: 24.225px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 38px`, `line-height: 38px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#edeee5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `40 { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#fdf48b` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000000` | `botDialogBodyLevelButtonLevelOp... { border-color: #000000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"ppNeueMontreal", "ppNeueMontreal Fallback"` | Typography / Scale Token |
| `--font-greed-bold` | `"greedBold", "greedBold Fallback"` | Typography / Scale Token |
| `--font-farnham-display` | `"farnhamDisplay", "farnhamDisplay Fallback"` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--leading-normal` | `1.5` | Typography / Scale Token |
| `--aspect-video` | `16 / 9` | Design System Custom Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-background` | `#edeee5` | Canvas / Surface Token |
| `--color-foreground` | `#000` | Typography Ink Token |
| `--color-accent` | `#fdf48b` | Brand / Palette Token |
| `--font-greed` | `var(--font-greed-bold), sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.text-foreground> — `auge-xp-com`)**:
   - Landmark `<header class="text-foreground">` (`1440x0px`) hosting `Digital Experience Studio · AUGE Exp` navigation (`Works · About · Let's talk`), DOM attributes (`data-precedence="next"`, `data-cbid="ced38b07-60a9-4c9f-ba..."`, `data-blockingmode="auto"`, `data-culture="EN"`), and stylesheet rule `real_f02daa13-module__qtcTEa__cla... { font-family:ppNeueMontreal,ppNeueMontreal Fallback }`.
2. **Hero Stage & Focal Lead (<main.min-h-dvh> — `AUGE EXPERIENCE© RCCS YFZVYTYHHV©`)**:
   - Landmark `<main class="min-h-dvh relative">` presenting display lead `AUGE EXPERIENCE© RCCS YFZVYTYHHV©` and copy excerpt *"An award-winning digital experience studio partnering with ambiti"* over `#edeee5` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.relative> — `AC40 Lunarossa`)**:
   - Landmark `<main class="min-h-dvh relative">` rendering section `AC40 Lunarossa` with copy *"An award-winning digital experience studio partnering with ambiti"*, asset references (`logo.svg`, `HJGhjOeW_p3Yd8NW_viru-cover.3.jpg`, `nTk2Qb6LITpLW8TG_maison_cover.jpg`, `pUkcTZHGA7KhlJZ0_lunarossa_cover_...`), and grid rule `treal_f02daa13-module__qtcTEa__va... { --font-sans:"ppNeueMontreal", "ppNeueMontreal Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.min-h-dvh:nth(2)> — `Don Molinico`)**:
   - Landmark `<main class="min-h-dvh relative">` framing `Don Molinico` and `Il Capo Production` (*"create distinctive experiences through"*) with `#ffffff` surface cards, `#fdf48b` accents, and `font-face { font-family:greedBold;src:url(../media/Greed_Bold-s.p.2gpcionblp7lf.woff... }`.
5. **Colophon & Global Directory Footer (<footer.CybotCookiebotDialogContentWrapper> — `https://auge-xp.com/`)**:
   - Landmark `<footer class="CybotCookiebotDialogContentWrapper">` anchoring `Digital Experience Studio · AUGE` footer links (`Works · About · Let's talk`), copy *"design, technology and creative"*, and `#000000` structural dividers.
