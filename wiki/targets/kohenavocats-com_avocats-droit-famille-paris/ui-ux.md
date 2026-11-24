---
title: "UI & UX Architecture: kohenavocats-com_avocats-droit-famille-paris"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: kohenavocats-com_avocats-droit-famille-paris

## Overview & Design Identity
- **Target**: `kohenavocats-com_avocats-droit-famille-paris` (**Avocat Droit de la Famille Paris · Divorce, Garde d'Enfants, Succession**)
- **Production URL**: [https://kohenavocats.com/avocats-droit-famille-paris/](https://kohenavocats.com/avocats-droit-famille-paris/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0077ed` accent)
- **Summary**: Avocat en droit de la famille à Paris. Divorce amiable ou contentieux, garde d'enfants, pension alimentaire, succession. Première analyse...
- **Total Clean CSS Variables Extracted**: `298` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Lato`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44px`, `line-height: 50.6px`, `font-weight: 900`, `letter-spacing: -1.1px`); CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: clamp(26px, 6vw, 86px)`, `line-height: 1.12`, `letter-spacing: -.025em`, `font-weight: 900`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 110.88px`, `line-height: 97.5744px`, `font-weight: 900`, `letter-spacing: -7.2072px`); rule `h2` (`font-size: clamp(18px, 0.9rem + 0.6vw, 2...`, `line-height: 1.12`, `letter-spacing: 0.02em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 18px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--e-global-typography-primary-letter-spacing: -0.3px`, `--e-global-typography-secondary-letter-spacing: 0px`, `--e-global-typography-text-letter-spacing: -0.8px`; rule `small` (`font-size: 11px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6faff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0077ed` | `.kcf-wrap .kcf-btn:hover { background: #0077ed }` |
| **Secondary / Muted Copy** | `#7c7c7c` | `var(--e-global-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#dce3e7` | `var(--kohen-avis-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp--style--global--content-size` | `800px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1200px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--justify-content` | `initial` | Design System Custom Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |
| `--order` | `initial` | Design System Custom Token |
| `--align-self` | `initial` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `kohenavocats-com_avocats-droit-famille-paris`)**:
   - Landmark `<header class="elementor elementor-25177">` (`1440x60px`) hosting `Avocat Droit de la Famille Paris · D` navigation (`Urgence pénale · Garde à vue · Détention provisoire · Cour d’assises · Instruction pénale`), DOM attributes (`data-kfh-variant="transparent"`, `data-cfasync="false"`, `data-no-minify="1"`, `data-no-optimize="1"`), and stylesheet rule `.site-header .site-title { font-size:2.5rem;font-weight:500;line-height:1.2 }`.
2. **Hero Stage & Focal Lead (<section.kfh-conversion> — `AVOCAT EN DROIT DE LA FAMILLE À PA`)**:
   - Landmark `<section class="kfh-conversion kfg-unified">` presenting display lead `AVOCAT EN DROIT DE LA FAMILLE À PARIS` and copy excerpt *"Divorce Séparation Enfants Succession"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.kohen-avis-panel> — `Avocat en droit de la famille à Pa`)**:
   - Landmark `<section class="kohen-avis-panel kohen-avis-wrap">` rendering section `Avocat en droit de la famille à Paris` with copy *"droit de la famille"*, asset references (`scevent.min.js`, `insight.min.js`, `bat.js`, `scripts.clarity.ms`), and grid rule `.site-header .site-branding { display:flex;flex-direction:column;gap:.5rem;justify-content:center }`.
4. **Interactive Detail & Feature Matrix (<section.knp> — `Recevez une première analyse`)**:
   - Landmark `<section class="knp knp--manuel">` framing `Recevez une première analyse` and `Ils parlent de nous` (*"Première analyse écrite 80 € TTC"*) with `#f6faff` surface cards, `#0077ed` accents, and `.site-header .header-inner { display:flex;flex-wrap:wrap;justify-content:space-between }`.
5. **Colophon & Global Directory Footer (<footer.kohen-avis-panel-footer> — `https://kohenavocats.com/avocats-droit-famille-paris/`)**:
   - Landmark `<footer class="kohen-avis-panel-footer">` anchoring `Avocat Droit de la Famille Paris` footer links (`Urgence pénale · Garde à vue · Détention provisoire · Cour d’assises · Instruction pénale`), copy *"Première analyse écrite"*, and `#dce3e7` structural dividers.
