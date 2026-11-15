# UI & UX Architecture: thestudiobyjuliegranger-com

## Overview & Design Identity
- **Target**: `thestudiobyjuliegranger-com` (**The Studio by Julie Granger**)
- **Production URL**: [https://thestudiobyjuliegranger.com/](https://thestudiobyjuliegranger.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#FFFDE2` ink, `#006ba1` accent)
- **Summary**: Une méthode unique alliant barre, yoga et renforcement, développée depuis plus de 12 ans et déjà adoptée par des milliers de femmes à tra...
- **Total Clean CSS Variables Extracted**: `27` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Newsreader`
- **Body Font Stack**: `Open Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 26px`, `line-height: 1.1`, `font-weight: 400`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Interactive Accent / Highlight** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Secondary / Muted Copy** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Structural Hairline Border** | `#FFFDE2` | `var(--mega-nav-cta-loader-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gap` | `12px` | Layout / Spatial Grid Token |
| `--clip` | `0` | Design System Custom Token |
| `--radius` | `20px` | Elevation / Border Token |
| `--reviews-slides-per-view` | `1.2` | Design System Custom Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mega-nav-header> — `thestudiobyjuliegranger-com`)**:
   - Landmark `<header class="mega-nav-header">` hosting `The Studio by Julie Granger` navigation (`Connexion · en · Connexion Connexion · Méthode et Résultats`), DOM attributes (`data-legal-modal-bound="true"`, `data-cookie-notice-ready="true"`, `data-cfasync="false"`, `data-pagespeed-no-defer`), and stylesheet rule `.account-auth__backdrop { position:absolute;inset:0;background:rgba(71,64,64,.32);backdrop-filter:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Un corps sculpté avec élégance`)**:
   - Landmark `<section class="hero hero--home">` presenting display lead `Un corps sculpté avec élégance` and copy excerpt *"Connexion Connexion"* over `#7a00df` canvas and `#FFFDE2` ink.
3. **Primary Showcase & Content Grid (<section.logos> — `Une méthode complète pour sculpter`)**:
   - Landmark `<section class="logos">` rendering section `Une méthode complète pour sculpter le corps` with copy *"E s s a i g r a t u i t"*, asset references (`clarity.js`, `z5quve8kus`, `matomo.js`, `gtm.js`), and grid rule `.account-auth__container--forgot { opacity:1;pointer-events:auto;transform:translateX(0);visibility:visible }`.
4. **Interactive Detail & Feature Matrix (<section.benefits> — `Barre`)**:
   - Landmark `<section class="benefits">` framing `Barre` and `Pilates` (*"Méthode et Résultats"*) with `#007cba` surface cards, `#006ba1` accents, and `.account-auth__inner { width:100%;max-width:464px;margin:auto }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://thestudiobyjuliegranger.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `The Studio by Julie Granger` footer links (`Connexion · en · Connexion Connexion · Méthode et Résultats`), copy *"The Studio par Julie Granger"*, and `#FFFDE2` structural dividers.
