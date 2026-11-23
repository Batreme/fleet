---
title: "UI & UX Architecture: drshabri-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: drshabri-com

## Overview & Design Identity
- **Target**: `drshabri-com` (**Cosmetic Dentist & Facial Aesthetics, Marylebone**)
- **Production URL**: [https://drshabri.com/](https://drshabri.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1a1a1a` ink, `#375efb` accent)
- **Summary**: Cosmetic dentist and facial aesthetics in Marylebone and Beaconsfield. Dr Shabri treats the smile, skin and facial proportions as one con...
- **Total Clean CSS Variables Extracted**: `171` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 63px`, `line-height: 63px`, `font-weight: 300`); CSS variables `--page-title-display: block`, `--display: flex`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 56px`, `line-height: 56px`, `font-weight: 300`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d6f3e6` | `>.ti-inner { background-color: #d6f3e6 }` |
| **Interactive Accent / Highlight** | `#375efb` | `.elementor .e-button-base { background-color: #375efb }` |
| **Secondary / Muted Copy** | `#4a4a4a` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cccccc` | `var(--iti-border-color)` in `:root` |
| **Variable Token (`--iti-hover-color`)** | `#000000` | `var(--iti-hover-color)` in `:root` |
| **Variable Token (`--iti-icon-color`)** | `#555555` | `var(--iti-icon-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp--style--global--content-size` | `800px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1200px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--iti-flag-width` | `20px` | Layout / Spatial Grid Token |
| `--iti-flag-count` | `244` | Design System Custom Token |
| `--iti-hover-color` | `#0000000d` | Brand / Palette Token |
| `--iti-border-color` | `#ccc` | Brand / Palette Token |
| `--iti-country-selector-bg` | `#fff` | Canvas / Surface Token |
| `--iti-icon-color` | `#555` | Brand / Palette Token |
| `--iti-spacer-horizontal` | `10px` | Layout / Spatial Grid Token |
| `--iti-flag-height` | `calc(var(--iti-flag-width)*3/4)` | Layout / Spatial Grid Token |
| `--iti-globe-icon-size` | `17px` | Layout / Spatial Grid Token |
| `--iti-clear-icon-size` | `15px` | Layout / Spatial Grid Token |
| `--iti-border-width` | `1px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `drshabri-com`)**:
   - Landmark `<header class="elementor elementor-15">` (`1440x70px`) hosting `Cosmetic Dentist & Facial Aesthetics` navigation (`DENTISTRY · Dental Consultation · Gum Contouring · Internal Bleaching · Teeth Whitening`), DOM attributes (`data-wpmeteor-mouseover="true"`, `data-wpmeteor-mouseout="true"`, `data-wpmeteor-nooptimize="true"`, `data-phast-no-defer`), and stylesheet rule `.dialog-message { box-sizing:border-box;line-height:1.5 }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `Dr Shabri creates transformations `)**:
   - Landmark `<main class="site-main post-13">` presenting display lead `Dr Shabri creates transformations that look inevi...` and copy excerpt *"A space dedicated to restoring harmony between your smile, skin a"* over `#ffffff` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<main.post-13> — `Cosmetic dentistry, facial aesthet`)**:
   - Landmark `<main class="site-main post-13">` rendering section `Cosmetic dentistry, facial aesthetics, regenerati...` with copy *"Begin a Conversation"*, asset references (`www.googletagmanager.com`, `embed`, `jquery.min.js`, `jquery-migrate.min.js`), and grid rule `.dialog-close-button:hover { color:var(--e-a-color-txt-hover) }`.
4. **Interactive Detail & Feature Matrix (<main.page> — `Three Disciplines. One way of look`)**:
   - Landmark `<main class="site-main post-13">` framing `Three Disciplines. One way of looking.` and `“A transformation so considered, it looks like it...` (*"Dentistry centred on health, proportion and longevity."*) with `#d6f3e6` surface cards, `#375efb` accents, and `.dialog-prevent-scroll { max-height:100vh;overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://drshabri.com/`)**:
   - Landmark `<footer class="elementor elementor-314">` anchoring `Cosmetic Dentist & Facial Aesthe` footer links (`DENTISTRY · Dental Consultation · Gum Contouring · Internal Bleaching · Teeth Whitening`), copy *"From preventative and restorative care to comprehensive smil"*, and `#cccccc` structural dividers.
