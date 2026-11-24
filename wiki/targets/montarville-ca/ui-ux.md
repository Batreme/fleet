---
title: "UI & UX Architecture: montarville-ca"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: montarville-ca

## Overview & Design Identity
- **Target**: `montarville-ca` (**montarville · Une approche globale et intégrée dans la gestion de vos pr...**)
- **Production URL**: [https://montarville.ca/](https://montarville.ca/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#121212` canvas, `#fafafa` ink, `#d0112b` accent)
- **Summary**: Un partenaire engagé. Une expertise reconnue. Une exécution maîtrisée. - Une approche globale et intégrée dans la gestion de vos projets...
- **Total Clean CSS Variables Extracted**: `89` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `General Sans`
- **Body Font Stack**: `General Sans`
- **Monospace / Technical Font Stack**: `Fira Sans`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 36px`, `line-height: 39.6px`, `font-weight: 600`); CSS variables `--font-size-h1: calc(128 / var(--base-px, 18) * 1rem)`; rule `h1` (`font-size: var(--font-size-h1)`, `line-height: 1em`, `font-weight: 600`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96px`, `line-height: 96px`, `font-weight: 600`); CSS variables `--font-size-h2-xl: calc(96 / var(--base-px, 18) * 1rem)`, `--font-size-h2: calc(72 / var(--base-px, 18) * 1rem)`; rule `h2` (`font-size: var(--font-size-h2-xl)`, `line-height: 1.02em`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 13.5px`, `line-height: 13.5px`, `font-weight: 400`); CSS variables `--font-size-body-lg: calc(24 / var(--base-px, 18) * 1rem)`, `--font-size-body: max(14px, calc(18 / var(--base-px, 18) * 1rem))`, `--font-size-body-sm: max(13px, calc(16 / var(--base-px, 18) * 1rem))`; rule `p` (`font-size: 1rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13.5px`, `line-height: 13.5px`, `font-weight: 400`); CSS variables `--font-size-caption: max(12px, calc(14 / var(--base-px, 18) * 1rem))`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fafafa` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d0112b` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#d0112b` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#000000` | `var(--ff_wp_tracking_text_color)` in `:root` |
| **Structural Hairline Border** | `#090909` | `var(--ff_wp_tracking_border_color)` in `:root` (`rgb(0 0 0 / 50%)`) |
| **Variable Token (`--ff_wp_tracking_background_color`)** | `#ffffff` | `var(--ff_wp_tracking_background_color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ff_wp_tracking_ease` | `cubic-bezier(0.25, 1, 0.5, 1)` | Typography / Scale Token |
| `--ff_wp_tracking_border_color` | `rgb(0 0 0 / 50%)` | Brand / Palette Token |
| `--ff_wp_tracking_background_color` | `#fff` | Canvas / Surface Token |
| `--ff_wp_tracking_text_color` | `#000` | Typography Ink Token |
| `--ff_wp_tracking_wrapper_padding` | `1.5rem` | Typography / Scale Token |
| `--ff_wp_tracking_dynamic-viewport-height` | `100vh` | Typography / Scale Token |
| `--fa-style-family-brands` | `"Font Awesome 6 Brands"` | Brand / Palette Token |
| `--fa-font-brands` | `normal 400 1em/1 "Font Awesome 6 Brands"` | Brand / Palette Token |
| `--fa-font-regular` | `normal 400 1em/1 "Font Awesome 6 Free"` | Typography / Scale Token |
| `--fa-style-family-classic` | `"Font Awesome 6 Free"` | Typography / Scale Token |
| `--fa-font-solid` | `normal 900 1em/1 "Font Awesome 6 Free"` | Typography / Scale Token |
| `--font-size-h1` | `calc(128 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h2-xl` | `calc(96 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h2` | `calc(72 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h3` | `calc(48 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h4` | `calc(32 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-header> — `montarville-ca`)**:
   - Landmark `<header class="c-header">` (`1440x0px`) hosting `montarville · Une approche globale e` navigation (`À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`), DOM attributes (`data-browser="Chrome"`, `data-browser-version="131.0.0.0"`, `data-platform="Apple"`, `data-os="Mac OS"`), and stylesheet rule `.ff-wp-tracking h3 { font-size:1.6rem }`.
2. **Hero Stage & Focal Lead (<section.c-home-intro> — `Un partenaire engagé. Une expertis`)**:
   - Landmark `<section class="c-home-intro">` presenting display lead `Un partenaire engagé. Une expertise reconnue. Une...` and copy excerpt *"Du début à la fin, nous avons le souci de livrer un projet à la h"* over `#121212` canvas and `#fafafa` ink.
3. **Primary Showcase & Content Grid (<section.c-home-about> — `Un partenaire engagé . Une experti`)**:
   - Landmark `<section class="c-home-about">` rendering section `Un partenaire engagé . Une expertise reconnue. Un...` with copy *"Une approche globale et intégrée dans la gestion de vos projets d"*, asset references (`orphisme_photographie_20210816-_2...`, `favicon.ico`, `FiraSans-Bold.woff2`, `GeneralSans-Variable.woff2`), and grid rule `.ff-wp-tracking h4 { font-size:1.3rem }`.
4. **Interactive Detail & Feature Matrix (<section.c-home-target> — `Partenaire de vos réussites`)**:
   - Landmark `<section class="c-home-target">` framing `Partenaire de vos réussites` and `Vous êtes...` (*"Que vous soyez au stade de la planification, à la recherche d’un "*) with `#d0112b` surface cards, `#d0112b` accents, and `.ff-wp-tracking p { font-size:1rem;margin-top:1em }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://montarville.ca/`)**:
   - Landmark `<footer class="c-footer">` anchoring `montarville · Une approche globa` footer links (`À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`), copy *"montarville . se distingue par sa capacité à offrir un servi"*, and `#090909` structural dividers.
