---
title: "UI & UX Architecture: www-lesgmstudios-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-lesgmstudios-com

## Overview & Design Identity
- **Target**: `www-lesgmstudios-com` (**GM Studios — Du contenu qui dépasse les chiffres**)
- **Production URL**: [https://www.lesgmstudios.com/](https://www.lesgmstudios.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#070707` canvas, `#ffffff` ink, `#00a2ff` accent)
- **Summary**: Agence de contenu & studio d'enregistrement à Montréal. 1 milliard de vues générées pour nos clients.
- **Total Clean CSS Variables Extracted**: `87` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `clashDisplay`
- **Body Font Stack**: `clashDisplay`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 15.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--font-display: var(--font-clash), system-ui, sans-serif`; rule `h1` (`font-size: 2.5rem`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 86.4px`, `font-weight: 600`); rule `h2` (`font-size: var(--h2-size,clamp(38px, 5.1...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`letter-spacing: 0`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`; rule `.label` (`font-size: 14px`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#070707` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0c0c0c` | `var(--color-bg-page)` in `:root` |
| **Interactive Accent / Highlight** | `#00a2ff` | `.selectable .vdpCellContent { color: #00a2ff }` |
| **Secondary / Muted Copy** | `#d0d5dd` | `var(--date-time-picker-disabled-text)` in `:root` |
| **Structural Hairline Border** | `#08090a` | `var(--appointment_widgets-border-color)` in `:root` (`1018281a`) |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-max` | `1440px` | Layout / Spatial Grid Token |
| `--font-sans` | `var(--font-geist), system-ui, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--leading-snug` | `1.375` | Typography / Scale Token |
| `--radius-xs` | `4px` | Elevation / Border Token |
| `--radius-sm` | `8px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-lesgmstudios-com`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x97px`) hosting `GM Studios — Du contenu qui dépasse ` navigation (`Accueil · Agence · Évènements · Cas clients · Équipe`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-svg-origin="709.5 452.36"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.inset-x-0> — `DU CONTENU QUI DÉPASSE LES CHIFFRE`)**:
   - Landmark `<section class="inset-x-0 top-0">` presenting display lead `DU CONTENU QUI DÉPASSE LES CHIFFRES` and copy excerpt *"Acceptez les témoins marketing pour afficher la vidéo."* over `#070707` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.overflow-x-clip> — `Du contenu qui dé p asse les chiff`)**:
   - Landmark `<section class="overflow-x-clip py-10">` rendering section `Du contenu qui dé p asse les chiffres` with copy *"Selon plus de 450 clients satisfaits"*, asset references (`ClashDisplay_Bold-s.p.2nvxwaktzfx...`, `ClashDisplay_Medium-s.p.0olkjtjdv...`, `ClashDisplay_Regular-s.p.2qbs-i2c...`, `ClashDisplay_Semibold-s.p.082yiqt...`), and grid rule `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`.
4. **Interactive Detail & Feature Matrix (<section.noise-layer> — `Clients & Partenaires`)**:
   - Landmark `<section class="noise-layer py-32">` framing `Clients & Partenaires` and `Nos services` (*"Studio de production à Montréal"*) with `#0c0c0c` surface cards, `#00a2ff` accents, and `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`.
5. **Colophon & Global Directory Footer (<footer.overflow-x-clip> — `https://www.lesgmstudios.com/`)**:
   - Landmark `<footer class="overflow-x-clip bg-transparent">` anchoring `GM Studios — Du contenu qui dépa` footer links (`Accueil · Agence · Évènements · Cas clients · Équipe`), copy *"Du contenu qui dé p asse"*, and `#08090a` structural dividers.
