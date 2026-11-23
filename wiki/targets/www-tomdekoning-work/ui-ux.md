---
title: "UI & UX Architecture: www-tomdekoning-work"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-tomdekoning-work

## Overview & Design Identity
- **Target**: `www-tomdekoning-work` (**tomdekoning.work — Building brands that turn heads**)
- **Production URL**: [https://www.tomdekoning.work/](https://www.tomdekoning.work/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffa500`)
- **Summary**: Freelance creative director in the Netherlands. Strategy, (web)design & development for brands that want to stand out. 8+ years experienc...
- **Total Clean CSS Variables Extracted**: `19` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Ppneuemontreal`
- **Body Font Stack**: `Playfair Display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `canvas-modal-luma` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | `.w-button { color: #ffffff }` |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert > div.w-ac... { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#ffa500` | `.button { background-color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#808080` | `.text-color-grey { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--black`)** | `#0b0b0b` | `var(--black)` in `:root` |
| **Variable Token (`--sand`)** | `#e7e1d7` | `var(--sand)` in `:root` |
| **Variable Token (`--orange`)** | `#f34213` | `var(--orange)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--black` | `#0b0b0b` | Canvas / Surface Token |
| `--sand` | `#e7e1d7` | Color / Atmospheric Token |
| `--orange` | `#f34213` | Color / Atmospheric Token |
| `--white` | `white` | Canvas / Surface Token |
| `--button-097-color` | `#E7E1D7` | Brand / Palette Token |
| `--button-097-color-background` | `#F34213` | Canvas / Surface Token |
| `--button-097-hover-color` | `#0B0B0B` | Brand / Palette Token |
| `--button-097-hover-color-background` | `#E7E1D7` | Canvas / Surface Token |
| `--button-097-color-focus` | `#E7E1D7` | Brand / Palette Token |
| `--button-097-border-radius` | `0.5em` | Elevation / Border Token |
| `--button-097-dot-border-radius` | `0.25em` | Elevation / Border Token |
| `--button-097-padding-right` | `0.75em` | Layout / Spatial Grid Token |
| `--button-097-padding-left` | `1em` | Layout / Spatial Grid Token |
| `--button-097-gap` | `0.375em` | Layout / Spatial Grid Token |
| `--button-097-dot-size` | `0.5em` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navbar> — `www-tomdekoning-work`)**:
   - Landmark `<nav class="navbar">` (`1440px`) hosting `tomdekoning.work — Building brands t` navigation (`MENU`), DOM attributes (`data-wf-domain="www.tomdekoning.work"`, `data-wf-page="6a981ab95ec4bc0363c7f6b9"`, `data-wf-site="6947d4a42871d2972031e9ab"`, `data-scroll-orientation="vertical"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.w-mod-ix> — `t o mdek o ning .w o rk`)**:
   - Landmark `<section class="w-mod-ix">` presenting display lead `t o mdek o ning .w o rk` and copy excerpt *"A B O U T A B O U T"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.wf-playfairdisplay-n6-active> — `A B O U T A B O U T`)**:
   - Landmark `<section class="wf-playfairdisplay-n6-active">` rendering section `A B O U T A B O U T` with copy *"C O N T A C T C O N T A C T"*, asset references (`cdn.prod.website-files.com`, `tdk-work.webflow.shared.09be52ab1...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.wf-playfairdisplay-n5-active> — `C O N T A C T C O N T A C T`)**:
   - Landmark `<section class="wf-playfairdisplay-n5-active">` framing `C O N T A C T C O N T A C T` and `I kill average brands and rebuild them, stronger` (*"I kill average brands and rebuild them, stronger, sharper, unforg"*) with `#222222` surface cards, `#ffa500` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-playfairdisplay-n3-active> — `https://www.tomdekoning.work/`)**:
   - Landmark `<footer class="wf-playfairdisplay-n3-active">` anchoring `tomdekoning.work — Building bran` footer links (`MENU`), copy *"I’m a freelance creative director based in the Netherlands. "*, and `#3898ec` structural dividers.
