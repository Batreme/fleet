# UI & UX Architecture: montarville-ca

## Overview & Design Identity
- **Target**: `montarville-ca` (**montarville · Une approche globale et intégrée dans la gestion de vos pr...**)
- **Production URL**: [https://montarville.ca/](https://montarville.ca/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#fafafa` accent)
- **Summary**: Un partenaire engagé. Une expertise reconnue. Une exécution maîtrisée. - Une approche globale et intégrée dans la gestion de vos projets...
- **Total Clean CSS Variables Extracted**: `89` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `General Sans`
- **Body Font Stack**: `Sono`
- **Monospace / Technical Font Stack**: `Fira Sans`
- **Hero Display (`H1`)**: CSS variables `--font-size-h1: calc(128 / var(--base-px, 18) * 1rem)`; rule `h1` (`font-size: var(--font-size-h1)`, `line-height: 1em`, `font-weight: 600`)
- **Section Heading (`H2`)**: CSS variables `--font-size-h2-xl: calc(96 / var(--base-px, 18) * 1rem)`, `--font-size-h2: calc(72 / var(--base-px, 18) * 1rem)`; rule `h2` (`font-size: var(--font-size-h2-xl)`, `line-height: 1.02em`, `font-weight: 600`)
- **Body Copy**: CSS variables `--font-size-body-lg: calc(24 / var(--base-px, 18) * 1rem)`, `--font-size-body: max(14px, calc(18 / var(--base-px, 18) * 1rem))`, `--font-size-body-sm: max(13px, calc(16 / var(--base-px, 18) * 1rem))`; rule `p` (`font-size: 1rem`)
- **Metadata & Labels**: CSS variables `--font-size-caption: max(12px, calc(14 / var(--base-px, 18) * 1rem))`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--ff_wp_tracking_background_color)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--ff_wp_tracking_text_color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#191919` | `var(--color-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#fafafa` | `var(--color-text)` in `:root` |
| **Secondary / Muted Copy** | `#d0112b` | `var(--ff_banner_bg_color)` in `:root` |
| **Structural Hairline Border** | `#121212` | `var(--color-link)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fa-animation-direction` | `reverse` | Motion / Easing Token |
| `--fa-style-family-brands` | `"Font Awesome 6 Brands"` | Brand / Palette Token |
| `--fa-font-brands` | `normal 400 1em/1 "Font Awesome 6 Brands"` | Brand / Palette Token |
| `--fa-font-regular` | `normal 400 1em/1 "Font Awesome 6 Free"` | Typography / Scale Token |
| `--fa-style-family-classic` | `"Font Awesome 6 Free"` | Typography / Scale Token |
| `--fa-font-solid` | `normal 900 1em/1 "Font Awesome 6 Free"` | Typography / Scale Token |
| `--ff_wp_tracking_ease` | `cubic-bezier(0.25, 1, 0.5, 1)` | Typography / Scale Token |
| `--ff_wp_tracking_border_color` | `rgb(0 0 0 / 50%)` | Brand / Palette Token |
| `--ff_wp_tracking_background_color` | `#fff` | Canvas / Surface Token |
| `--ff_wp_tracking_text_color` | `#000` | Typography Ink Token |
| `--ff_wp_tracking_wrapper_padding` | `1.5rem` | Typography / Scale Token |
| `--ff_wp_tracking_dynamic-viewport-height` | `100vh` | Typography / Scale Token |
| `--font-size-h1` | `calc(128 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h2-xl` | `calc(96 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h2` | `calc(72 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h3` | `calc(48 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-header> — `montarville-ca`)**:
   - Landmark `<header class="c-header">` hosting `montarville · Une approche globale e` navigation (`À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`), DOM attributes (`data-browser="Chrome"`, `data-browser-version="124.0.0.0"`, `data-platform="Apple"`, `data-os="Mac OS"`), and stylesheet rule `.fa { font-family:var(--fa-style-family,"Font Awesome 6 Free");font-weight:var... }`.
2. **Hero Stage & Focal Lead (<section.c-home-intro> — `Un partenaire engagé . Une experti`)**:
   - Landmark `<section class="c-home-intro">` presenting display lead `Un partenaire engagé . Une expertise reconnue. Un...` and copy excerpt *"Accéder au contenu principal"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.c-home-about> — `Partenaire de vos réussites`)**:
   - Landmark `<section class="c-home-about">` rendering section `Partenaire de vos réussites` with copy *"Expertises Découvrir Gestion de construction Projets forfaitaires"*, asset references (`orphisme_photographie_20210816-_2...`, `favicon.ico`, `FiraSans-Bold.woff2`, `GeneralSans-Variable.woff2`), and grid rule `.fas { font-family:"Font Awesome 6 Free" }`.
4. **Interactive Detail & Feature Matrix (<section.c-home-target> — `Vous êtes...`)**:
   - Landmark `<section class="c-home-target">` framing `Vous êtes...` and `Architecte, designer, ou ingénieur?` (*"Gestion de construction"*) with `#191919` surface cards, `#fafafa` accents, and `.fab { font-family:"Font Awesome 6 Brands" }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://montarville.ca/`)**:
   - Landmark `<footer class="c-footer">` anchoring `montarville · Une approche globa` footer links (`À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`), copy *"Projets forfaitaires"*, and `#121212` structural dividers.
