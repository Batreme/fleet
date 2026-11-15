# UI & UX Architecture: delice-ca

## Overview & Design Identity
- **Target**: `delice-ca` (**Accueil - Délice**)
- **Production URL**: [https://delice.ca/](https://delice.ca/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5dbca` / `#f8efdc`)
- **Summary**: Pizza Délice depuis 1970 Au cœur de Lévis, alliant chaleur, grandeur et convivialité dans une ambiance vibrante et accueillante.
- **Total Clean CSS Variables Extracted**: `76` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Filson Soft`
- **Body Font Stack**: `Ivy Mode`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`)
- **Body Copy**: rule `p` (`font-size: max(14px,min(14px,.875rem))`, `line-height: 1.4`, `letter-spacing: 0`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5dbca` | `var(--primary-300)` in `:root` |
| **Primary Typography Ink** | `#de2b2b` | `var(--on-primary-300)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7c2627` | `var(--on-primary-300-alt)` in `:root` |
| **Interactive Accent / Highlight** | `#f8efdc` | `var(--on-primary-500)` in `:root` |
| **Secondary / Muted Copy** | `#91964f` | `var(--secondary-500)` in `:root` |
| **Structural Hairline Border** | `#273e2a` | `var(--secondary-700)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--header-banner-height` | `2.75rem` | Layout / Spatial Grid Token |
| `--header-inner-height` | `clamp(64px, 47.0986px + 4.50704vw, 7rem)` | Layout / Spatial Grid Token |
| `--header-height` | `calc(var(--header-banner-height) + var(--header-inner-height))` | Layout / Spatial Grid Token |
| `--menu-banner-height` | `2.5rem` | Layout / Spatial Grid Token |
| `--menu-nav-height` | `6rem` | Layout / Spatial Grid Token |
| `--promotion-media-size` | `min(34rem, 55vh)` | Layout / Spatial Grid Token |
| `--section-spacing-top-default` | `clamp(64px, 41.4648px + 6.00939vw, 8rem)` | Layout / Spatial Grid Token |
| `--section-spacing-bottom-default` | `clamp(64px, 41.4648px + 6.00939vw, 8rem)` | Layout / Spatial Grid Token |
| `--section-spacing-top-compact` | `clamp(64px, 64px + 0vw, 4rem)` | Layout / Spatial Grid Token |
| `--section-spacing-bottom-compact` | `clamp(64px, 64px + 0vw, 4rem)` | Layout / Spatial Grid Token |
| `--container-spacing-md` | `clamp(32px, 20.7324px + 3.0047vw, 4rem)` | Layout / Spatial Grid Token |
| `--primary-300` | `#f5dbca` | Brand / Palette Token |
| `--primary-300-rgb` | `245, 219, 202` | Brand / Palette Token |
| `--on-primary-300` | `#de2b2b` | Brand / Palette Token |
| `--on-primary-300-rgb` | `222, 43, 43` | Brand / Palette Token |
| `--on-primary-300-alt` | `#7c2627` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-header> — `delice-ca`)**:
   - Landmark `<header class="c-header">` hosting `Accueil - Délice` navigation (`Les menus · Le restaurant`), DOM attributes (`data-module-swup="m1"`, `data-module-scroll="m2"`, `data-module-effects="m3"`, `data-module-dev-utils="m4"`), and stylesheet rule `.flickity-enabled { position:relative }`.
2. **Hero Stage & Focal Lead (<section.c-hero> — `Pizza Délice depuis 1970 Au cœur d`)**:
   - Landmark `<section class="c-hero">` presenting display lead `Pizza Délice depuis 1970 Au cœur de Lévis, allian...` and copy excerpt *"Tous les jours de 14 h à 18 h."* over `#f5dbca` canvas and `#273e2a` ink.
3. **Primary Showcase & Content Grid (<section.o-section> — `Un choix pour tous les goûts`)**:
   - Landmark `<section class="o-section u-relative">` rendering section `Un choix pour tous les goûts` with copy *"Tous les jours de 11 h à 15 h."*, asset references (`recaptcha__en.js`, `script.js`, `www.googletagmanager.com`, `mainCss.css`), and grid rule `.flickity-viewport { touch-action:pan-y;height:100%;position:relative;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.o-section> — `Plaisirs du jour`)**:
   - Landmark `<section class="o-section">` framing `Plaisirs du jour` and `Happy Hour` (*"Tous les mardis de 11 h à 22 h."*) with `#7c2627` surface cards, `#f8efdc` accents, and `.flickity-slider { width:100%;height:100%;position:absolute;left:0 }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://delice.ca/`)**:
   - Landmark `<footer class="c-footer">` anchoring `Accueil - Délice` footer links (`Les menus · Le restaurant`), copy *"20 % de rabais en livraison et pour emporter."*, and `#273e2a` structural dividers.
