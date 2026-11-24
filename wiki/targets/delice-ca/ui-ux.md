---
title: "UI & UX Architecture: delice-ca"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: delice-ca

## Overview & Design Identity
- **Target**: `delice-ca` (**Accueil - Délice**)
- **Production URL**: [https://delice.ca/](https://delice.ca/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f8efdc` / `#185abc`)
- **Summary**: Pizza Délice depuis 1970 Au cœur de Lévis, alliant chaleur, grandeur et convivialité dans une ambiance vibrante et accueillante.
- **Total Clean CSS Variables Extracted**: `76` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Filson Soft`
- **Body Font Stack**: `Filson Soft`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 18px`, `line-height: 24.3px`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 64px`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: max(14px,min(14px,.875rem))`, `line-height: 1.4`, `letter-spacing: 0`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8efdc` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#de2b2b` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.flickity-button:hover { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#185abc` | `.rc-2fa-submit-button-holder bu... { background-color: #185abc }` |
| **Secondary / Muted Copy** | `#91964f` | `var(--secondary-500)` in `:root` |
| **Structural Hairline Border** | `#b2b2b2` | `kbox-hover .recaptcha-checkbox-... { border: #b2b2b2 }` |
| **Variable Token (`--primary-300`)** | `#f5dbca` | `var(--primary-300)` in `:root` |
| **Variable Token (`--on-primary-300-alt`)** | `#7c2627` | `var(--on-primary-300-alt)` in `:root` |

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
   - Landmark `<header class="c-header">` (`1440x156px`) hosting `Accueil - Délice` navigation (`Les menus · Le restaurant`), DOM attributes (`data-module-swup="m1"`, `data-module-scroll="m2"`, `data-module-effects="m3"`, `data-module-dev-utils="m4"`), and stylesheet rule `.flickity-enabled { position:relative }`.
2. **Hero Stage & Focal Lead (<section.c-hero> — `PIZZA DÉLICE DEPUIS 1970 Au cœur d`)**:
   - Landmark `<section class="c-hero">` presenting display lead `PIZZA DÉLICE DEPUIS 1970 Au cœur de Lévis, allian...` and copy excerpt *"Au cœur de Lévis, alliant chaleur, grandeur et convivialité dans "* over `#f8efdc` canvas and `#de2b2b` ink.
3. **Primary Showcase & Content Grid (<section.o-section> — `Pizza Délice depuis 1970 Au cœur d`)**:
   - Landmark `<section class="o-section u-relative">` rendering section `Pizza Délice depuis 1970 Au cœur de Lévis, allian...` with copy *"Des saveurs du monde, des ingrédients frais, et des plats pensés "*, asset references (`recaptcha__en.js`, `script.js`, `www.googletagmanager.com`, `mainCss.css`), and grid rule `.flickity-viewport { touch-action:pan-y;height:100%;position:relative;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.o-section:nth(2)> — `Un choix pour tous les goûts`)**:
   - Landmark `<section class="o-section">` framing `Un choix pour tous les goûts` and `Plaisirs du jour` (*"Vos fins d’après-midi, rehaussées."*) with `#ffffff` surface cards, `#185abc` accents, and `.flickity-slider { width:100%;height:100%;position:absolute;left:0 }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://delice.ca/`)**:
   - Landmark `<footer class="c-footer">` anchoring `Accueil - Délice` footer links (`Les menus · Le restaurant`), copy *"Tous les jours de 14 h à 18 h."*, and `#b2b2b2` structural dividers.
