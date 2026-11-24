---
title: "UI & UX Architecture: www-esrbespoke-au"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-esrbespoke-au

## Overview & Design Identity
- **Target**: `www-esrbespoke-au` (**ESR**)
- **Production URL**: [https://www.esrbespoke.au/](https://www.esrbespoke.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#9ca3af`)
- **Summary**: Three decades of restoring excellence and reigniting the joy of the drive.
- **Total Clean CSS Variables Extracted**: `8` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `__bodyFont_0f148b`
- **Body Font Stack**: `__bodyFont_0f148b`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 62px`, `line-height: 58.9px`, `font-weight: 500`, `letter-spacing: -0.62px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 500`, `letter-spacing: -0.4px`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 23.4px`, `font-weight: 300`); CSS variables `--body-font: "__bodyFont_0f148b","__bodyFont_Fallback_0f148b",helvetica,arial,sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 14px`, `font-weight: 300`, `letter-spacing: 1.26px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2299dd` | `#nprogress .bar { background: #2299dd }` |
| **Interactive Accent / Highlight** | `#9ca3af` | `textarea::placeholder { color: #9ca3af }` |
| **Secondary / Muted Copy** | `#9ca3af` | `textarea::placeholder { color: #9ca3af }` |
| **Structural Hairline Border** | `#e6e6e6` | `var(--border)` in `:root` (`rgba(0,0,0,0.1)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--foreground-rgb` | `0,0,0` | Typography Ink Token |
| `--background-rgb` | `255,255,255` | Canvas / Surface Token |
| `--border-rgb` | `0,0,0` | Elevation / Border Token |
| `--scrollbarWidth` | `0px` | Layout / Spatial Grid Token |
| `--body-font` | `"__bodyFont_0f148b","__bodyFont_Fallback_0f148b",helvetica,arial,sans-serif` | Typography / Scale Token |
| `--foreground` | `#fff` | Typography Ink Token |
| `--background` | `#ffffff` | Canvas / Surface Token |
| `--border` | `rgba(0,0,0,0.1)` | Elevation / Border Token |
| `--tw-content` | `""` | Design System Custom Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--www-esrbespoke-a-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-esrbespoke-a-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-auto> — `www-esrbespoke-au`)**:
   - Landmark `<header class="w-auto grid-layout">` (`1440x85px`) hosting `ESR` navigation (`Services · Partners · About · Contact · Careers`), DOM attributes (`data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.keen-slider__slide { min-height:100%;overflow:hidden;position:relative;width:100% }`.
2. **Hero Stage & Focal Lead (<section.w-auto> — `Exceptional is our standard`)**:
   - Landmark `<section class="w-auto grid-layout">` presenting display lead `Exceptional is our standard` and copy excerpt *"A u t o m o t i v e G r o u p since 1989"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.items-end> — `E x c e p t i o n a l i s o u r s `)**:
   - Landmark `<section class="w-auto items-end">` rendering section `E x c e p t i o n a l i s o u r s t a n d a r d` with copy *"( 0 2 ) 9 7 3 5 1 1 1 1 e n q u i r i e s @ e s r b e s p o k e ."*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `favicon.ico`), and grid rule `nprogress { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.mb-8> — `ESR is recognised as an official P`)**:
   - Landmark `<section class="w-auto mb-8">` framing `ESR is recognised as an official Porsche Certifie...` and `At ESR, we offer a complete end-to-end service ex...` (*"4 1 9 - 4 3 1 C a n t e r b u r y R o a d , C a m p s i e N S W 2"*) with `#2299dd` surface cards, `#9ca3af` accents, and `nprogress .bar { background:29d;position:fixed;z-index:1031;top:0;left:0;width:100%;heigh... }`.
5. **Colophon & Global Directory Footer (<footer.clip> — `https://www.esrbespoke.au/`)**:
   - Landmark `<footer class="clip mono">` anchoring `ESR` footer links (`Services · Partners · About · Contact · Careers`), copy *"E S R B e s p o k e S t u d i o"*, and `#e6e6e6` structural dividers.
