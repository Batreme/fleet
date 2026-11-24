---
title: "UI & UX Architecture: www-apc-pallets-nl"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-apc-pallets-nl

## Overview & Design Identity
- **Target**: `www-apc-pallets-nl` (**Algemeen Pallet Centrum · APC**)
- **Production URL**: [https://www.apc-pallets.nl/](https://www.apc-pallets.nl/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0082f3`)
- **Summary**: Pallets kopen? Nieuwe, gebruikte & gerecyclede pallets gemaakt van gecertificeerd hout. Sterk, betrouwbaar & op maat voor jouw logistiek....
- **Total Clean CSS Variables Extracted**: `201` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aspekta`
- **Body Font Stack**: `Aspekta`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_typography---font-size--h1: 3.75rem`, `--_typography---font-size--display: 6rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 60px`, `font-weight: 350`); CSS variables `--_typography---font-size--h2: 3rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 21.6px`, `font-weight: 400`); CSS variables `--consent-studio-mixed-body-font-weight: inherit`, `--consent-studio-typo-body-min-font-size: 14px`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 21.6px`, `font-weight: 400`); CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--normal)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#042a22` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f5f5` | `var(--consent-studio-default-header-action-bg-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#333333` | `var(--consent-studio-default-heading-text-color)` in `:root` |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--swatch--white)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--brand-text)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--1-35)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-400)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--normal)` | Typography Ink Token |
| `--site--gutter` | `2rem` | Layout / Spatial Grid Token |
| `--_spacing---space--10rem` | `10rem` | Layout / Spatial Grid Token |
| `--radius--main` | `.5rem` | Elevation / Border Token |
| `--_theme---background-2` | `var(--swatch--pale-green)` | Canvas / Surface Token |
| `--site--column-count` | `12` | Layout / Spatial Grid Token |
| `--_responsive---large` | `1` | Design System Custom Token |
| `--_responsive---medium` | `0` | Design System Custom Token |
| `--_responsive---small` | `0` | Design System Custom Token |
| `--_responsive---xsmall` | `0` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav_component> — `www-apc-pallets-nl`)**:
   - Landmark `<nav class="nav_component">` (`1440x80px`) hosting `Algemeen Pallet Centrum · APC` navigation (`Contact · Vacatures · Nieuwe pallets · Gebruikte pallets · Gerecyclede pallets`), DOM attributes (`data-wf-domain="www.apc-pallets.nl"`, `data-wf-page="693a8a0b940fefc38834a6ec"`, `data-wf-site="693a8a0a940fefc38834a67f"`, `data-padding-bottom="none"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.u-section> — `Makers van pallets`)**:
   - Landmark `<section class="u-section section_header">` presenting display lead `Makers van pallets` and copy excerpt *"Wat wij maken, maakt een verschil"* over `#ffffff` canvas and `#042a22` ink.
3. **Primary Showcase & Content Grid (<section.section_home_subheader> — `Twijfel over de juiste pallet?`)**:
   - Landmark `<section class="u-section section_home_subheader">` rendering section `Twijfel over de juiste pallet?` with copy *"W i j m a k e n n i e u w e p a l l e t s e n g e b r u i k t e p"*, asset references (`cdn.prod.website-files.com`, `apcdev.webflow.shared.2991ca99e.css`, `clarity.js`, `array.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.u-section:nth(2)> — `Aandacht voor kwaliteit met gecert`)**:
   - Landmark `<section class="u-section">` framing `Aandacht voor kwaliteit met gecertificeerd hout` and `Ontdek meer over onze` (*"Nieuwe , Gebruikte of Maatwerk pallets"*) with `#f5f5f5` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://www.apc-pallets.nl/`)**:
   - Landmark `<footer class="footer_component">` anchoring `Algemeen Pallet Centrum · APC` footer links (`Contact · Vacatures · Nieuwe pallets · Gebruikte pallets · Gerecyclede pallets`), copy *"Elke toepassing vraagt om een andere oplossing. We denken gr"*, and `#e2e2e2` structural dividers.
