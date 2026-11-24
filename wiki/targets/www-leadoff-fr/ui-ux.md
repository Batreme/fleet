---
title: "UI & UX Architecture: www-leadoff-fr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-leadoff-fr

## Overview & Design Identity
- **Target**: `www-leadoff-fr` (**Agence digitale à Vannes : web, mobile & acquisition · LEADOFF**)
- **Production URL**: [https://www.leadoff.fr](https://www.leadoff.fr)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0000ff` canvas, `#ffffff` ink, `#ffff00` accent)
- **Summary**: LEADOFF conçoit des applications web et mobiles, sites e-commerce et stratégies d’acquisition. Une équipe digitale experte basée à Vannes.
- **Total Clean CSS Variables Extracted**: `23` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NewTitle-Variable`
- **Body Font Stack**: `GeneralSans-Variable`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 129.6px`, `line-height: 132.84px`, `font-weight: 650`, `letter-spacing: 1.296px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 144px`, `line-height: 144px`, `font-weight: 650`, `letter-spacing: 1.44px`); rule `,h2` (`font-size: max(80px,min(10vw,100vw))`, `font-weight: 650`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `,p` (`font-size: max(18px,min(.9vw,100vw))`, `line-height: 1.5`, `letter-spacing: .03em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0000ff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.loader.loader--black { background: #000000 }` |
| **Interactive Accent / Highlight** | `#ffff00` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#000000` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000099` | `.bg-yellow .editorial-flow-cont... { border-color: #000099 }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--focus-color` | `#00f` | Brand / Palette Token |
| `--focus-ring-color` | `var(--focus-color)` | Brand / Palette Token |
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
| `--menu-focus-color` | `#ff0` | Brand / Palette Token |
| `--menu-focus-contrast` | `#000` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-leadoff-fr`)**:
   - Landmark `<header class="lenis">` (`1440x0px`) hosting `Agence digitale à Vannes : web, mobi` navigation (`Services Services · Projets Projets · À propos À propos · L’équipe L’équipe · Manifeste Manifeste`), DOM attributes (`data-barba="wrapper"`, `data-skip-link-ready="true"`, `data-icon="false"`, `data-icon="false"`), and stylesheet rule `.loader.loader--hidden { opacity:0;-webkit-transform:scale(.98);transform:scale(.98) }`.
2. **Hero Stage & Focal Lead (<section.observe-section> — `DES APPLICATIONS ET DES SITES QUI `)**:
   - Landmark `<section class="observe-section bg-blue">` presenting display lead `DES APPLICATIONS ET DES SITES QUI PERFORMENT` and copy excerpt *"Rapide. Fluide. Bien pensé. Pas un projet bricolé qui commence à "* over `#0000ff` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.editorial-pitch> — `Des applications et des sites qui `)**:
   - Landmark `<section class="editorial-pitch observe-section">` rendering section `Des applications et des sites qui performent` with copy *"Des applications et"*, asset references (`bundle.68ec1454.css`, `jquery.min.js`, `jquery-migrate.min.js`, `cropped-FAVICON-1-32x32.jpg`), and grid rule `.loader .loader-word { display:-webkit-box;display:-ms-flexbox;display:flex;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.editorial-highlight> — `On conçoit des solutions pensées p`)**:
   - Landmark `<section class="editorial-highlight observe-section">` framing `On conçoit des solutions pensées pour durer` and `Ce qu’on fait (et bien)` (*"des sites qui performent"*) with `#000000` surface cards, `#ffff00` accents, and `.loader .loader-skip:focus-visible { color:ff0;outline:none }`.
5. **Colophon & Global Directory Footer (<footer.observe-section> — `https://www.leadoff.fr`)**:
   - Landmark `<footer class="observe-section bg-blue">` anchoring `Agence digitale à Vannes : web, ` footer links (`Services Services · Projets Projets · À propos À propos · L’équipe L’équipe · Manifeste Manifeste`), copy *"Un site web, une boutique en ligne, une application… C’est u"*, and `#000099` structural dividers.
