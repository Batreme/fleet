---
title: "UI & UX Architecture: thestudiobyjuliegranger-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: thestudiobyjuliegranger-com

## Overview & Design Identity
- **Target**: `thestudiobyjuliegranger-com` (**The Studio by Julie Granger**)
- **Production URL**: [https://thestudiobyjuliegranger.com/](https://thestudiobyjuliegranger.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#474040` ink, `#91befc` accent)
- **Summary**: Une méthode unique alliant barre, yoga et renforcement, développée depuis plus de 12 ans et déjà adoptée par des milliers de femmes à tra...
- **Total Clean CSS Variables Extracted**: `37` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Newsreader Hero`
- **Body Font Stack**: `Open Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 42px`, `line-height: 46.2px`, `font-weight: 400`); rule `h2` (`font-size: 26px`, `line-height: 1.1`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#474040` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f6f0` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#91befc` | `.hero__retreat-badge { background-color: #91befc }` |
| **Secondary / Muted Copy** | `#665c5a` | `var(--consent-soft-ink)` in `:root` |
| **Structural Hairline Border** | `#e4dfda` | `var(--consent-line)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

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
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--site-fixed-header-offset` | `70px` | Layout / Spatial Grid Token |
| `--site-no-hero-top-gap` | `18px` | Layout / Spatial Grid Token |
| `--site-anchor-scroll-gap` | `16px` | Layout / Spatial Grid Token |
| `--reviews-slides-per-view` | `1.2` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mega-nav-header> — `thestudiobyjuliegranger-com`)**:
   - Landmark `<header class="mega-nav-header">` (`1340x92px`) hosting `The Studio by Julie Granger` navigation (`Connexion · en · Connexion Connexion · Méthode et Résultats · Corps qui a changé`), DOM attributes (`data-cookieconsent="ignore"`, `data-implementation="wp"`, `data-cbid="22577dd5-f8e6-45b3-bb..."`, `data-culture="FR"`), and stylesheet rule `.banp-request-push-permission-button { margin-right:10px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Un corps sculpté avec élégance`)**:
   - Landmark `<section class="hero hero--home">` presenting display lead `Un corps sculpté avec élégance` and copy excerpt *"La méthode unique de The Studio mêle barre, yoga et renforcement "* over `#ffffff` canvas and `#474040` ink.
3. **Primary Showcase & Content Grid (<section.logos> — `Une méthode complète pour sculpter`)**:
   - Landmark `<section class="logos">` rendering section `Une méthode complète pour sculpter le corps` with copy *"C o m m e n c e r l ’ e s s a i"*, asset references (`matomo.js`, `gtm.js`, `state.js`, `widgetIcon.min.js`), and grid rule `.banp-ajax-success { display:inline-block;font-size:1.2em;margin:0 10px;vertical-align:middle }`.
4. **Interactive Detail & Feature Matrix (<section.benefits> — `The Studio by Julie Granger`)**:
   - Landmark `<section class="benefits">` framing `The Studio by Julie Granger` and `Si vous vous reconnaissez, The Studio est fait po...` (*"Pour tous les niveaux"*) with `#f6f6f0` surface cards, `#91befc` accents, and `.banp-ajax-error { color:b81c23 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://thestudiobyjuliegranger.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `The Studio by Julie Granger` footer links (`Connexion · en · Connexion Connexion · Méthode et Résultats · Corps qui a changé`), copy *"Des workouts adaptés à tous les niveaux"*, and `#e4dfda` structural dividers.
