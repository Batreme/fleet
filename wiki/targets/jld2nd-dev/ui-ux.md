---
title: "UI & UX Architecture: jld2nd-dev"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: jld2nd-dev

## Overview & Design Identity
- **Target**: `jld2nd-dev` (**JLD'2nd – Designer & Developer**)
- **Production URL**: [https://jld2nd.dev](https://jld2nd.dev)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#121212` canvas, `#ffffff` ink, `#f6c53a` accent)
- **Summary**: I believe web design should be as expressive as the ideas behind it. Driven by curiosity, I explore new possibilities at the intersection...
- **Total Clean CSS Variables Extracted**: `63` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Minecraft`
- **Body Font Stack**: `Mozilla Headline`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--fs-display-2xl: clamp(3.75rem, 3.5536rem + .9821vw, 5.125rem)`, `--fs-display-xl: clamp(3.5rem, calc(3.4rem + .5vw), 4rem)`, `--fs-display-lg: clamp(3.125rem, 2.9018rem + 1.1161vw, 4.6875rem)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 70.9998px`, `line-height: 70.9998px`, `font-weight: 600`, `letter-spacing: 5px`)
- **Body Copy**: live computed `body` (`font-size: 16.9995px`, `line-height: 25.4993px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16.9995px`, `line-height: 25.4993px`, `font-weight: 400`); CSS variables `--fs-text-sm: .875rem`, `--fs-text-xs: .75rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#263238` | `var(--base-bg-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#f6c53a` | `.dock-btn { color: #f6c53a }` |
| **Secondary / Muted Copy** | `#11b76b` | `var(--base-text-success)` in `:root` |
| **Structural Hairline Border** | `#dddedf` | `var(--base-border-color)` in `:root` |
| **Variable Token (`--color-lime`)** | `#ceff00` | `var(--color-lime)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-gutter` | `40px` | Layout / Spatial Grid Token |
| `--fs-display-2xl` | `clamp(3.75rem, 3.5536rem + .9821vw, 5.125rem)` | Dimension / Scale Token |
| `--fs-display-xl` | `clamp(3.5rem, calc(3.4rem + .5vw), 4rem)` | Dimension / Scale Token |
| `--fs-display-lg` | `clamp(3.125rem, 2.9018rem + 1.1161vw, 4.6875rem)` | Dimension / Scale Token |
| `--fs-display-md` | `clamp(2.8125rem, 2.6339rem + .8929vw, 4.0625rem)` | Dimension / Scale Token |
| `--fs-display-sm` | `clamp(2.25rem , calc(2.2rem + .25vw), 2.5rem)` | Dimension / Scale Token |
| `--fs-display-xs` | `clamp(1.875rem, calc(1.85rem + .125vw), 2rem)` | Dimension / Scale Token |
| `--fs-text-xl` | `clamp(1.25rem , calc(1.2rem + .25vw), 1.5rem)` | Typography Ink Token |
| `--fs-text-lg` | `clamp(1.125rem, calc(1.1rem + .125vw),1.25rem)` | Typography Ink Token |
| `--fs-text-md` | `clamp(1rem, .9821rem + .0893vw, 1.125rem)` | Typography Ink Token |
| `--fs-text-sm` | `.875rem` | Typography Ink Token |
| `--fs-text-xs` | `.75rem` | Typography Ink Token |
| `--color-ink` | `#121212` | Typography Ink Token |
| `--color-lime` | `#ceff00` | Brand / Palette Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--form-gap` | `20px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `jld2nd-dev`)**:
   - Landmark `<header class="sticky">` (`1440x0px`) hosting `JLD'2nd – Designer & Developer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-no-grid`, `data-section="hero"`, `data-section="about"`, `data-section="pixels"`), and stylesheet rule `main-content:focus { outline:none }`.
2. **Hero Stage & Focal Lead (<section.section> — `T u r n i n g P i x e l s i n t o `)**:
   - Landmark `<section class="section grid-container">` presenting display lead `T u r n i n g P i x e l s i n t o M e m o r a b l...` and copy excerpt *"E x p e r i e n c e s ."* over `#121212` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.p-relative> — `T h e C r e a t o r B e h i n d t `)**:
   - Landmark `<section class="section p-relative">` rendering section `T h e C r e a t o r B e h i n d t h e C o d e a n...` with copy *"t h o u g h t f u l"*, asset references (`favicon.ico`, `favicon-32x32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:auto;line-height:1.15 }`.
4. **Interactive Detail & Feature Matrix (<section.h-150> — `I t a l l s t a r t s w i t h t h `)**:
   - Landmark `<section class="section p-relative">` framing `I t a l l s t a r t s w i t h t h e p i x e l s .` and `T h i s i s w h e r e i d e a s t a k e s h a p e .` (*"s t r u c t u r e ,"*) with `#263238` surface cards, `#f6c53a` accents, and `section { display:block }`.
5. **Colophon & Global Directory Footer (<footer.home-footer> — `https://jld2nd.dev`)**:
   - Landmark `<footer class="home-footer">` anchoring `JLD'2nd – Designer & Developer` footer links (`Overview · Index · Archive · About · Contact`), copy *"i n t e r a c t i o n ,"*, and `#dddedf` structural dividers.
