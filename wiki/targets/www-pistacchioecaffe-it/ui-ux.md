---
title: "UI & UX Architecture: www-pistacchioecaffe-it"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-pistacchioecaffe-it

## Overview & Design Identity
- **Target**: `www-pistacchioecaffe-it` (**Pistacchio & Caffè**)
- **Production URL**: [http://www.pistacchioecaffe.it](http://www.pistacchioecaffe.it)
- **Final Redirected URL**: [https://pistacchioecaffe.it/](https://pistacchioecaffe.it/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#302c27` ink, `#ff0000` accent)
- **Summary**: Scopri il mondo di Francesca, interior designer e stylist. Dal design d'interni allo styling personalizzato, troverai soluzioni creative...
- **Total Clean CSS Variables Extracted**: `45` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `velourlight`
- **Body Font Stack**: `velourlight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 3vw`, `line-height: 1.2`, `font-weight: normal`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 43.2px`, `line-height: 51.84px`, `font-weight: 400`); rule `h2` (`font-size: 2.5vw`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 30px`, `font-weight: 400`); rule `body` (`font-size: 18px`, `line-height: 30px`, `font-weight: normal`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 30px`, `font-weight: 400`); rule `.label` (`font-size: 17px`, `line-height: 1`, `font-weight: normal`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#302c27` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.woocommerce a.remove { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#767676` | `var(--wc-subtext)` in `:root` |
| **Structural Hairline Border** | `#ebebeb` | `var(--iub-granular-border)` in `:root` (`rgba(0, 0, 0, 0.08)`) |
| **Variable Token (`--text-main-color`)** | `#465565` | `var(--text-main-color)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--woocommerce`)** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Variable Token (`--wc-green`)** | `#007518` | `var(--wc-green)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-main-color` | `#465565` | Typography Ink Token |
| `--app-height` | `100%` | Layout / Spatial Grid Token |
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
| `--woocommerce` | `#720eec` | Color / Atmospheric Token |
| `--wc-green` | `#007518` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-pistacchioecaffe-it`)**:
   - Landmark `<header class="site-header">` (`1440x101px`) hosting `Pistacchio & Caffè` navigation (`contattami · 0,00 €`), DOM attributes (`data-cmp-ab="2"`, `data-cmp-info="10"`, `data-cmp-ab="2"`, `data-cmp-info="2"`), and stylesheet rule `urger.is-active .hamburger-inner:... { background-color: FFFAF0; }`.
2. **Hero Stage & Focal Lead (<article.post-7> — `Benvenuti nel mio mondo!`)**:
   - Landmark `<article class="post-7 page">` presenting display lead `Benvenuti nel mio mondo!` and copy excerpt *"Ciao, sono Francesca, interior designer e stylist. Ascolto, proge"* over `#ffffff` canvas and `#302c27` ink.
3. **Primary Showcase & Content Grid (<article.page> — `E colore sia.`)**:
   - Landmark `<article class="post-7 page">` rendering section `E colore sia.` with copy *"Amo disegnare e scrivere, ognuna di queste passioni è entrata pre"*, asset references (`30300652.js`, `core-it.js`, `recaptcha__en.js`, `jquery.min.js`), and grid rule `.hamburger-inner { display: block; top: 50%; margin-top: -1px; }`.
4. **Interactive Detail & Feature Matrix (<article.type-page> — `Progetto per te.`)**:
   - Landmark `<article class="post-7 page">` framing `Progetto per te.` and `Ogni luogo ha il suo colore` (*"Potrei definire il mio stile POP_MINIMALE ma non dimentico mai co"*) with `#dddddd` surface cards, `#ff0000` accents, and `.hamburger-inner::after { content: ""; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `http://www.pistacchioecaffe.it`)**:
   - Landmark `<footer class="site-footer contenitore-flex">` anchoring `Pistacchio & Caffè` footer links (`contattami · 0,00 €`), copy *"Il mio mondo è fatto di mille possibilità e sfaccettature, f"*, and `#ebebeb` structural dividers.
