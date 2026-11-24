---
title: "UI & UX Architecture: www-eladiodieste-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-eladiodieste-com

## Overview & Design Identity
- **Target**: `www-eladiodieste-com` (**Eladio Dieste**)
- **Production URL**: [https://www.eladiodieste.com/](https://www.eladiodieste.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#a55f2d`)
- **Summary**: Eladio Dieste (1917–2000), ingeniero uruguayo. Biografía, trayectoria y obras: bóvedas de ladrillo, estructuras de cascarón y la revoluci...
- **Total Clean CSS Variables Extracted**: `46` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `font`
- **Body Font Stack**: `font`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 17.5524px`, `line-height: 26.3287px`, `font-weight: 400`); CSS variables `--text-5xl: 3rem`, `--text-5xl--line-height: 1`, `--text-6xl: 3.75rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 122.867px`, `line-height: 122.867px`, `font-weight: 400`, `letter-spacing: -6.14335px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 17.5524px`, `line-height: 26.3287px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17.5524px`, `line-height: 26.3287px`, `font-weight: 500`, `letter-spacing: -0.0175524px`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f1ece8` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eadfd2` | `var(--background)` in `:root` |
| **Interactive Accent / Highlight** | `#a55f2d` | live computed `main` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#a55f2d` | live computed `main` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `.border-off-white { border-color: #ffffff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#eadfd2` | Canvas / Surface Token |
| `--foreground` | `#a55f2d` | Typography Ink Token |
| `--off-white` | `#f1ece8` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1/.75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25/.875)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75/1.125)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |
| `--text-xl--line-height` | `calc(1.75/1.25)` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.font-medium> — `www-eladiodieste-com`)**:
   - Landmark `<nav class="font-medium pointer-events-auto">` (`1405x26px`) hosting `Eladio Dieste` navigation (`Inicio · Obra · Vida · Carrera · English`), DOM attributes (`data-scroll-orientation="vertical"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `font_b50abbf3-module__9ye_bG__cla... { font-family:font,font Fallback }`.
2. **Hero Stage & Focal Lead (<section.text-background> — `Eladio Dieste`)**:
   - Landmark `<section class="text-background invisible">` presenting display lead `Eladio Dieste` and copy excerpt *"Foto: (FADU, UDELAR)"* over `#000000` canvas and `#f1ece8` ink.
3. **Primary Showcase & Content Grid (<section.px-global> — `Vivienda Berlingieri (Próximamente`)**:
   - Landmark `<section class="px-global pt-6">` rendering section `Vivienda Berlingieri (Próximamente)` with copy *"Todos los derechos reservados © 2026"*, asset references (`die_grotesk_a_medium-s.p.221bfec9...`, `die_grotesk_a_regular-s.p.e93e1fc...`, `bg.webp`, `inf-4.webp`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.gap-5> — `Iglesia de Atlántida Cristo Obrero`)**:
   - Landmark `<section class="px-global gap-5">` framing `Iglesia de Atlántida Cristo Obrero y Nuestra Seño...` and `Fábrica TEM S.A. (Próximamente)` (*"Eladio Dieste, el ingeniero uruguayo, cuya obra hizo que el modo "*) with `#eadfd2` surface cards, `#a55f2d` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.h-dvh> — `https://www.eladiodieste.com/`)**:
   - Landmark `<footer class="h-dvh overflow-hidden">` anchoring `Eladio Dieste` footer links (`Inicio · Obra · Vida · Carrera · English`), copy *"Eladio Dieste, el ingeniero uruguayo, cuya obra hizo que el "*, and `#ffffff` structural dividers.
