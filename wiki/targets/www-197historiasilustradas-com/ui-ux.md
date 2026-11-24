---
title: "UI & UX Architecture: www-197historiasilustradas-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-197historiasilustradas-com

## Overview & Design Identity
- **Target**: `www-197historiasilustradas-com` (**197 Historias Ilustradas**)
- **Production URL**: [https://www.197historiasilustradas.com/](https://www.197historiasilustradas.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#171717` ink, `#171717` accent)
- **Summary**: 197 historias ilustradas es un proyecto que busca dar a conocer la vida de cada una de las personas detenidas desaparecidas nacidas en Ur...
- **Total Clean CSS Variables Extracted**: `32` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `font`
- **Body Font Stack**: `font`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`)
- **Section Heading (`H2`)**: observed font-size ladder: `17px`, `13.8125px`, `1em`, `80%`, `75%`
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13.8125px`, `line-height: 17.9563px`, `font-weight: 400`, `letter-spacing: -3%`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171717` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#171717` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#737373` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#b2b2b2` | `30 { border-color: #b2b2b2 }` |
| **Variable Token (`--color-neutral-300`)** | `#d4d4d4` | `var(--color-neutral-300)` in `:root` |
| **Variable Token (`--color-neutral-400`)** | `#a1a1a1` | `var(--color-neutral-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#171717` | Typography Ink Token |
| `--muted` | `#737373` | Color / Atmospheric Token |
| `--ease` | `cubic-bezier(.645,.045,.355,1)` | Motion / Easing Token |
| `--ease-out-expo` | `cubic-bezier(.19,1,.22,1)` | Motion / Easing Token |
| `--ease-base` | `cubic-bezier(.46,.03,.12,1)` | Motion / Easing Token |
| `--ease-magic` | `cubic-bezier(.33,0,0,1)` | Motion / Easing Token |
| `--ease-quart` | `cubic-bezier(.41,.35,.2,1)` | Motion / Easing Token |
| `--ease-overshoot` | `cubic-bezier(.175,.885,.43,1.6)` | Motion / Easing Token |
| `--ease-anticipate` | `cubic-bezier(1,-.4,.35,.95)` | Motion / Easing Token |
| `--scrollbar-gutter` | `0px` | Layout / Spatial Grid Token |
| `--color-neutral-300` | `#d4d4d4` | Brand / Palette Token |
| `--color-neutral-400` | `#a1a1a1` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.px-global> — `www-197historiasilustradas-com`)**:
   - Landmark `<header class="px-global top-0">` (`1430x52px`) hosting `197 Historias Ilustradas` navigation (`[ Grilla ] · [ Listado ] · [ Galería ]`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --color-neutral-300:lab(84.92% 0 -.0000119209);--color-neutral-400:lab(6... }`.
2. **Hero Stage & Focal Lead (<div.is-ready> — `197 Historias Ilustradas`)**:
   - Landmark `<div class="is-ready">` presenting display lead `197 Historias Ilustradas` and copy excerpt *"Entre las décadas de 1970 y 1980, tanto Uruguay como Argentina at"* over `#ffffff` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<div.px-global> — `Entre las décadas de 1970 y 1980, `)**:
   - Landmark `<div class="px-global">` rendering section `Entre las décadas de 1970 y 1980, tanto Uruguay ` with copy *"Historias Ilustradas"*, asset references (`882aee3e7e5fa64f.css`, `3068344f6b59fc28.css`, `a6a883b7ec42f0a6.js`, `1c40893e27076bb9.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.fixed> — `Historias Ilustradas`)**:
   - Landmark `<div class="fixed">` framing `Historias Ilustradas` and `E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 ` (*"E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 8 0 , t a n t o U"*) with `#000000` surface cards, `#171717` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.top-0> — `https://www.197historiasilustradas.com/`)**:
   - Landmark `<footer class="top-0">` anchoring `197 Historias Ilustradas` footer links (`[ Grilla ] · [ Listado ] · [ Galería ]`), copy *"R e c o r d a r e s v o l v e r a d a r v i d a ; p o r q u "*, and `#b2b2b2` structural dividers.
