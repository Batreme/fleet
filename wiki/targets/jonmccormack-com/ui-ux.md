---
title: "UI & UX Architecture: jonmccormack-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: jonmccormack-com

## Overview & Design Identity
- **Target**: `jonmccormack-com` (**Patterns - Jon McCormack**)
- **Production URL**: [https://jonmccormack.com/](https://jonmccormack.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#111111` ink, `#ffcc00` accent)
- **Summary**: Explore the intriguing repeating patterns in nature that captivate the eye and remind us of the awe and beauty in the world.
- **Total Clean CSS Variables Extracted**: `213` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aeonik Pro`
- **Body Font Stack**: `Aeonik Pro`
- **Monospace / Technical Font Stack**: `Fira Code`
- **Hero Display (`H1`)**: observed font-size ladder: `31.68px`, `18.4064px`, `20.304px`, `31.2px`, `clamp(1.95rem, 1.6vw, 2.8rem)`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 31.68px`, `line-height: 34.848px`, `font-weight: 400`); rule `h2` (`font-size: 13px`, `line-height: 15px`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 18.4064px`, `line-height: 27.6096px`, `font-weight: 300`); rule `p` (`line-height: 18px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20.304px`, `line-height: 30.456px`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111111` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#ffcc00` | `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }` |
| **Secondary / Muted Copy** | `#888888` | `.ytp-ad-overlay-attribution { color: #888888 }` |
| **Structural Hairline Border** | `#e2e2e2` | `elative-container .ytp-ad-info-... { border-color: #e2e2e2 }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
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
| `--wp--style--global--content-size` | `735px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `2200px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `1.2rem` | Layout / Spatial Grid Token |
| `--jm-shell-header` | `10vh` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wp-block-template-part> — `jonmccormack-com`)**:
   - Landmark `<header class="wp-block-template-part">` (`1440x87px`) hosting `Patterns - Jon McCormack` navigation (`Patterns · News · TEDx · Book · Bio`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-interactive="core/navigation"`, `data-wp-context="("overlayOpenedBy":("..."`, `data-wp-on--click="actions.openMenuOnClick"`), and stylesheet rule `html.jm-splash-viewed .jm-splash { display: none !important; }`.
2. **Hero Stage & Focal Lead (<article.jm-patterns-landing__item> — `Patterns - Jon McCormack`)**:
   - Landmark `<article class="jm-patterns-landing__item">` presenting display lead `Patterns - Jon McCormack` and copy excerpt *"Explore the intriguing repeating patterns in nature that captivat"* over `#ffffff` canvas and `#111111` ink.
3. **Primary Showcase & Content Grid (<article.jm-patterns-landing__item:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<article class="jm-patterns-landing__item">` rendering section `Featured Work & Interactive Showcase` with copy *"Patterns - Jon McCormack"*, asset references (`cdnjs.cloudflare.com`, `www.googletagmanager.com`, `embed`, `splash.css`), and grid rule `textarea:focus { outline: none !important; box-shadow: none !important; }`.
4. **Interactive Detail & Feature Matrix (<article.jm-patterns-landing__item:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<article class="jm-patterns-landing__item">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#dddddd` surface cards, `#ffcc00` accents, and `selection { background: rgb(144, 144, 144); color: white; }`.
5. **Colophon & Global Directory Footer (<footer.wp-block-template-part> — `https://jonmccormack.com/`)**:
   - Landmark `<footer class="wp-block-template-part">` anchoring `Patterns - Jon McCormack` footer links (`Patterns · News · TEDx · Book · Bio`), copy *"Technical Architecture & Narrative"*, and `#e2e2e2` structural dividers.
