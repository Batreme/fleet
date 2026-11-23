---
title: "UI & UX Architecture: www-xantium-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-xantium-com

## Overview & Design Identity
- **Target**: `www-xantium-com` (**Xantium**)
- **Production URL**: [https://www.xantium.com](https://www.xantium.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#221f25` canvas, `#f5f5f2` ink, `#c9ff8b` accent)
- **Summary**: Xantium
- **Total Clean CSS Variables Extracted**: `43` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Mono`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 57.6px`, `font-weight: 400`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 57.6px`, `font-weight: 400`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-body: system-ui,sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--font-space-mono: "Space Mono","Space Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#221f25` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f2` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-cache-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#c9ff8b` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#084432` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#413f44` | `15 { border-color: #413f44 }` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter","Inter Fallback"` | Typography / Scale Token |
| `--font-space-mono` | `"Space Mono","Space Mono Fallback"` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1/.75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25/.875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5/1)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `www-xantium-com`)**:
   - Landmark `<header class="pointer-events-none inset-x-0">` (`1440x40px`) hosting `Xantium` navigation (`Home · How We Work · Our Culture · Our Team · Careers`), DOM attributes (`data-precedence="next"`, `data-nimg="fill"`, `data-nimg="fill"`, `data-nimg="fill"`), and stylesheet rule `nter_fe8b9d92-module__LINzvG__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.z-3> — `WE BUILD TECHNOLOGY ENHANCED BY HU`)**:
   - Landmark `<section class="z-3 py-16">` presenting display lead `WE BUILD TECHNOLOGY ENHANCED BY HUMAN INSIGHT TO...` and copy excerpt *"At Xantium, quantitative researchers, developers, fundamental ana"* over `#221f25` canvas and `#f5f5f2` ink.
3. **Primary Showcase & Content Grid (<section.py-16> — `We build technology enhanced by hu`)**:
   - Landmark `<section class="z-3 py-16">` rendering section `We build technology enhanced by human insight to...` with copy *"We are a global multi-strategy investment firm integrating quanti"*, asset references (`28e60ca39c9ae554-s.p.7a4e9fcc.woff2`, `83afe278b6a6bb3c-s.p.3a6ba036.woff2`, `8d05cfa5faa8406c-s.p.4adea45d.woff2`, `d7a0600e467cf0bd-s.p.20ecb425.woff2`), and grid rule `inter_fe8b9d92-module__LINzvG__va... { --font-inter:"Inter","Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Founded in 2019 as part of Tudor G`)**:
   - Landmark `<section class="py-16 relative">` framing `Founded in 2019 as part of Tudor Group` and `250+ people across 4 offices` (*"If you're drawn to complex problems and collaborative discovery, "*) with `#000000` surface cards, `#c9ff8b` accents, and `mono_e13c1f09-module__VyLqqa__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.bg-cache-black> — `https://www.xantium.com`)**:
   - Landmark `<footer class="bg-cache-black relative">` anchoring `Xantium` footer links (`Home · How We Work · Our Culture · Our Team · Careers`), copy *"Global presence, market breadth, scale"*, and `#413f44` structural dividers.
