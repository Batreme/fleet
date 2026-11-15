# UI & UX Architecture: www-apc-pallets-nl

## Overview & Design Identity
- **Target**: `www-apc-pallets-nl` (**Algemeen Pallet Centrum · APC**)
- **Production URL**: [https://www.apc-pallets.nl/](https://www.apc-pallets.nl/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0c473b` / `#e3f1e0`)
- **Summary**: Pallets kopen? Nieuwe, gebruikte & gerecyclede pallets gemaakt van gecertificeerd hout. Sterk, betrouwbaar & op maat voor jouw logistiek....
- **Total Clean CSS Variables Extracted**: `164` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aspekta`
- **Body Font Stack**: `.875rem`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_typography---font-size--h1: 3.75rem`, `--_typography---font-size--display: 6rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: CSS variables `--_typography---font-size--h2: 3rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--normal)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0c473b` | `var(--swatch--mid-green)` in `:root` |
| **Primary Typography Ink** | `#90c685` | `var(--swatch--light-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#042a22` | `var(--swatch--dark-green)` in `:root` |
| **Interactive Accent / Highlight** | `#e3f1e0` | `var(--swatch--pale-green)` in `:root` |
| **Secondary / Muted Copy** | `#ccb4d8` | `var(--swatch--purple)` in `:root` |
| **Structural Hairline Border** | `#0000` | `a { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav_component> — `www-apc-pallets-nl`)**:
   - Landmark `<nav class="nav_component">` hosting `Algemeen Pallet Centrum · APC` navigation (`Contact · Vacatures · Nieuwe pallets · Gebruikte pallets · Gerecyclede pallets`), DOM attributes (`data-wf-domain="www.apc-pallets.nl"`, `data-wf-page="693a8a0b940fefc38834a6ec"`, `data-wf-site="693a8a0a940fefc38834a67f"`, `data-padding-bottom="none"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.u-section> — `Makers van pallets`)**:
   - Landmark `<section class="u-section section_header">` presenting display lead `Makers van pallets` and copy excerpt *"Gerecyclede pallets"* over `#0c473b` canvas and `#e3f1e0` ink.
3. **Primary Showcase & Content Grid (<section.u-section> — `Twijfel over de juiste pallet?`)**:
   - Landmark `<section class="u-section section_home_subheader">` rendering section `Twijfel over de juiste pallet?` with copy *"Makers van verschil"*, asset references (`cdn.prod.website-files.com`, `apcdev.webflow.shared.2991ca99e.css`, `clarity.js`, `array.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.u-section> — `Aandacht voor kwaliteit met gecert`)**:
   - Landmark `<section class="u-section">` framing `Aandacht voor kwaliteit met gecertificeerd hout` and `ISPM15` (*"Wat wij maken, maakt een verschil"*) with `#042a22` surface cards, `#e3f1e0` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://www.apc-pallets.nl/`)**:
   - Landmark `<footer class="footer_component">` anchoring `Algemeen Pallet Centrum · APC` footer links (`Contact · Vacatures · Nieuwe pallets · Gebruikte pallets · Gerecyclede pallets`), copy *"W i j m a k e n n i e u w e p a l l e t s e n g e b r u i k "*, and `#0000` structural dividers.
