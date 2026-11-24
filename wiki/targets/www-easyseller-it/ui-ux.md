---
title: "UI & UX Architecture: www-easyseller-it"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-easyseller-it

## Overview & Design Identity
- **Target**: `www-easyseller-it` (**EASYSELLER · Sales Digital Agency**)
- **Production URL**: [https://www.easyseller.it/](https://www.easyseller.it/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0d6efd`)
- **Summary**: Aiutiamo i brand e retail multibrand a crescere online attraverso percorsi completi di consulenza · digitalizzazione · gestione · promozi...
- **Total Clean CSS Variables Extracted**: `451` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Font2`
- **Body Font Stack**: `Font1`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 172.8px`, `line-height: 207.36px`, `font-weight: 400`); CSS variables `--h1-val: 14rem`, `--h1-font-size: calc(var(--h1-val) + 0.2 * ((100vw - 1440px) / 200))`; rule `h1` (`font-size: 12vw`, `line-height: 120%`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96px`, `line-height: 105.6px`, `font-weight: 400`); CSS variables `--h2-val: 10rem`, `--h2-font-size: calc(var(--h2-val) + 0.2 * ((100vw - 1440px) / 200))`; rule `h2` (`font-size: var(--h4-font-size)`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: calc(var(--p-font-size) + 0.5...`, `line-height: 150%`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--p-small-val: 1rem`, `--p-small-font-size: calc(var(--p-small-val) + 0.2 * ((100vw - 1440px) / 200))`; rule `,small` (`font-size: .875em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0d6efd` | `var(--bs-primary)` in `:root` |
| **Secondary / Muted Copy** | `#6c757d` | `var(--bs-secondary)` in `:root` |
| **Structural Hairline Border** | `#9ec5fe` | `var(--bs-primary-border-subtle)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--bs-indigo`)** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Variable Token (`--bs-purple`)** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Variable Token (`--bs-pink`)** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Variable Token (`--bs-red`)** | `#dc3545` | `var(--bs-red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-purple` | `#6f42c1` | Color / Atmospheric Token |
| `--bs-pink` | `#d63384` | Typography Ink Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.py-4> — `www-easyseller-it`)**:
   - Landmark `<header class="py-4 ready">` (`1440x76px`) hosting `EASYSELLER · Sales Digital Agency` navigation (`Instagram · LinkedIn · Facebook · Youtube · Servizi`), DOM attributes (`data-wp-strategy="defer"`, `data-barba="wrapper"`, `data-barba="container"`, `data-barba-namespace="home"`), and stylesheet rule `.wpcf7 .hidden-fields-container { display: none; }`.
2. **Hero Stage & Focal Lead (<section.hero_section> — `Elevate Your Sales`)**:
   - Landmark `<section class="hero_section">` presenting display lead `Elevate Your Sales` and copy excerpt *"Dal 2013 il nostro obiettivo è aiutarti a vendere di più, acquisi"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.py-5> — `E l e v a t e Y o u r S a l e s`)**:
   - Landmark `<section class="py-5">` rendering section `E l e v a t e Y o u r S a l e s` with copy *"Alcuni dei brand che abbiamo supportato nel raggiungere nuovi ris"*, asset references (`favicon.png`, `embed`, `styles.css`, `bootstrap.min.css`), and grid rule `.wpcf7 form .wpcf7-response-output { margin: 2em 0.5em 1em; padding: 0.2em 1em; border: 2px solid 00a0d2; }`.
4. **Interactive Detail & Feature Matrix (<section.py-5:nth(2)> — `Aiutiamo i brand e retail multibra`)**:
   - Landmark `<section class="py-5">` framing `Aiutiamo i brand e retail multibrand a crescere o...` and `Operatività concreta.` (*"Woman · Man · Kids Beachwear"*) with `#dddddd` surface cards, `#0d6efd` accents, and `form.submitting .wpcf7-response-o... { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.py-5> — `https://www.easyseller.it/`)**:
   - Landmark `<footer class="py-5">` anchoring `EASYSELLER · Sales Digital Agenc` footer links (`Instagram · LinkedIn · Facebook · Youtube · Servizi`), copy *"Woman · Man Beachwear"*, and `#9ec5fe` structural dividers.
