---
title: "UI & UX Architecture: www-zagrebwebusluge-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-zagrebwebusluge-com

## Overview & Design Identity
- **Target**: `www-zagrebwebusluge-com` (**Web agencija i digitalna rješenja · Zagreb Web Usluge**)
- **Production URL**: [https://www.zagrebwebusluge.com/](https://www.zagrebwebusluge.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#090909` / `#ffb189`)
- **Summary**: Zagreb Web Usluge povezuje web dizajn, WordPress, web trgovine, SEO i sadržaj. Istražite usluge, proces i koncepte za svoj digitalni nastup.
- **Total Clean CSS Variables Extracted**: `84` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Satoshi`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 95.76px`, `line-height: 87.1416px`, `font-weight: 900`, `letter-spacing: -5.7456px`); rule `h1` (`letter-spacing: -.065em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 25.92px`, `font-weight: 900`, `letter-spacing: -0.672px`); rule `h2` (`letter-spacing: -.052em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--zr-body: ZwuKarla,Arial,sans-serif`, `--co-body: clamp(15px, 1.12vw, 18px)`; rule `p` (`font-size: 1rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); CSS variables `--co-caption: clamp(11px, .8vw, 13px)`; rule `small` (`letter-spacing: 0`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#090909` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#eee7da` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0b0a` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffb189` | `var(--zr-accent-2)` in `:root` |
| **Secondary / Muted Copy** | `#aaa99e` | `var(--nav-muted)` in `:root` |
| **Structural Hairline Border** | `#30323e` | `var(--zr-line)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--zr-bg`)** | `#08090d` | `var(--zr-bg)` in `:root` |
| **Variable Token (`--zr-panel`)** | `#11131a` | `var(--zr-panel)` in `:root` |

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
| `--wp--style--global--content-size` | `1200px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1440px` | Layout / Spatial Grid Token |
| `--zr-bg` | `#08090d` | Canvas / Surface Token |
| `--zr-panel` | `#11131a` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.zm-header> — `www-zagrebwebusluge-com`)**:
   - Landmark `<header class="zm-header zwu-header">` (`1440x110px`) hosting `Web agencija i digitalna rješenja · ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hero-intro-mode="signature"`, `data-hero-intro="fallback"`, `data-zwu-style-bundle="1"`, `data-wp-strategy="defer"`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.wp-block-group> — `Web stranice koje nose vaš potpis.`)**:
   - Landmark `<section class="wp-block-group zm-hero">` presenting display lead `Web stranice koje nose vaš potpis.` and copy excerpt *"ZAGREB WEB USLUGE DIZAJN · WORDPRESS · WEB TRGOVINE"* over `#090909` canvas and `#eee7da` ink.
3. **Primary Showcase & Content Grid (<section.zm-partners> — `Povjerenje i pristup`)**:
   - Landmark `<section class="wp-block-group zm-partners">` rendering section `Povjerenje i pristup` with copy *"HRVATSKA ZAGREB / EUROPE"*, asset references (`site-icon-32-v150.png`, `hero-mobile-wide-941-v150b.avif`, `hero-mobile-mid-941-v150b.avif`, `hero-mobile-941-v143b.avif`), and grid rule `body.zr-site { margin:0;background:var(--zr-bg);color:var(--zr-text);font:400 18px/1.6... }`.
4. **Interactive Detail & Feature Matrix (<section.zm-services> — `Jasna strategija`)**:
   - Landmark `<section class="wp-block-group zm-services">` framing `Jasna strategija` and `Autorski dizajn` (*"Zagreb Web Usluge Dizajn · WordPress · Web trgovine"*) with `#0a0b0a` surface cards, `#ffb189` accents, and `body.zr-site a { color:inherit;text-decoration:none }`.
5. **Colophon & Global Directory Footer (<footer.zwu-footer> — `https://www.zagrebwebusluge.com/`)**:
   - Landmark `<footer class="zwu-footer zm-footer">` anchoring `Web agencija i digitalna rješenj` footer links (`Overview · Index · Archive · About · Contact`), copy *"Od prve odluke o sadržaju do WordPress predaje. Oblikujemo w"*, and `#30323e` structural dividers.
