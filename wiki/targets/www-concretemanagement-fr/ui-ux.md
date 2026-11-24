---
title: "UI & UX Architecture: www-concretemanagement-fr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-concretemanagement-fr

## Overview & Design Identity
- **Target**: `www-concretemanagement-fr` (**Concrete.**)
- **Production URL**: [https://www.concretemanagement.fr/](https://www.concretemanagement.fr/)
- **Final Redirected URL**: [https://www.concretemanagement.ch/fr](https://www.concretemanagement.ch/fr)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×872px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#141416` canvas, `#ffffff` ink, `#0082f3` accent)
- **Summary**: L’immobilier, pensé pour vous
- **Total Clean CSS Variables Extracted**: `25` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Otto`
- **Body Font Stack**: `Interdisplay`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 144px`, `line-height: 129.6px`, `font-weight: 300`, `letter-spacing: -10.08px`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 72px`, `font-weight: 300`, `letter-spacing: -5.04px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 24px`, `line-height: 20.8px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#141416` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert > div.w-ac... { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#97968d` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--_colors---kaki--base`)** | `#dcd9c8` | `var(--_colors---kaki--base)` in `:root` |
| **Variable Token (`--_colors---brown--base`)** | `#5f4242` | `var(--_colors---brown--base)` in `:root` |
| **Variable Token (`--_colors---cream--base`)** | `#fffdf1` | `var(--_colors---cream--base)` in `:root` |
| **Variable Token (`--_colors---dark--light`)** | `#2c2b2f` | `var(--_colors---dark--light)` in `:root` |
| **Variable Token (`--_colors---white--20`)** | `#fff3` | `var(--_colors---white--20)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_colors---dark--base` | `#141416` | Canvas / Surface Token |
| `--_colors---white--base` | `white` | Canvas / Surface Token |
| `--_colors---kaki--base` | `#dcd9c8` | Brand / Palette Token |
| `--xl` | `12.5em` | Dimension / Scale Token |
| `--_sizes---space--md` | `2.5em` | Layout / Spatial Grid Token |
| `--_sizes---space--sm` | `1.5em` | Layout / Spatial Grid Token |
| `--_colors---dark--20` | `#14141633` | Canvas / Surface Token |
| `--_sizes---space--lg` | `5em` | Layout / Spatial Grid Token |
| `--_colors---brown--base` | `#5f4242` | Brand / Palette Token |
| `--_colors---cream--base` | `#fffdf1` | Brand / Palette Token |
| `--_colors---kaki--dark` | `#97968d` | Canvas / Surface Token |
| `--_colors---dark--light` | `#2c2b2f` | Canvas / Surface Token |
| `--_colors---white--20` | `#fff3` | Canvas / Surface Token |
| `--_colors---white--50` | `#ffffff80` | Canvas / Surface Token |
| `--_colors---dark--50` | `#14141680` | Canvas / Surface Token |
| `--_sizes---perc-60` | `60%` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-concretemanagement-fr`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `Concrete.` navigation (`Paris · Lausanne · Propriétaires + · Locataires + · À propos`), DOM attributes (`data-wf-domain="www.concretemanagemen..."`, `data-wf-page="6966a64d3505e01c9d776d27"`, `data-wf-site="6966a64c3505e01c9d776d0f"`, `data-wf--buttonsimple--variant="cream"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `L’immobilier, pensé pour vous`)**:
   - Landmark `<section class="hero">` presenting display lead `L’immobilier, pensé pour vous` and copy excerpt *"Demander une estimation"* over `#141416` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.presentation> — `Concrete est une structure de gest`)**:
   - Landmark `<section class="presentation u-section">` rendering section `Concrete est une structure de gestion patrimonial...` with copy *"Gestion moyenne durée"*, asset references (`cdn.prod.website-files.com`, `concrete-3b73a4.webflow.shared.4d...`, `69809783d135718ad587d127_favicon.png`, `69809785d587f5575f03e822_favicon-...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.stacking> — `Votre patrimoine, notre expertise`)**:
   - Landmark `<section class="stacking u-section">` framing `Votre patrimoine, notre expertise` and `Gestion moyenne durée` (*"Gestion courte durée"*) with `#222222` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.portail-btn> — `https://www.concretemanagement.fr/`)**:
   - Landmark `<footer class="portail-btn">` anchoring `Concrete.` footer links (`Paris · Lausanne · Propriétaires + · Locataires + · À propos`), copy *"Trouver un appartement"*, and `#3898ec` structural dividers.
