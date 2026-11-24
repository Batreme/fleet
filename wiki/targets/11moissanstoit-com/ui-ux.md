---
title: "UI & UX Architecture: 11moissanstoit-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: 11moissanstoit-com

## Overview & Design Identity
- **Target**: `11moissanstoit-com` (**11 mois sans toi(t), le tour du monde de Josué & Philippe**)
- **Production URL**: [https://11moissanstoit.com/](https://11moissanstoit.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fee422` / `#151723`)
- **Summary**: Tour du monde autobiographique 2010-2011 de Josué & Philippe. 11 mois, des dizaines d'étapes, des milliers de tweets, de photos et de sou...
- **Total Clean CSS Variables Extracted**: `9` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Founders Grotesk X-Condensed`
- **Body Font Stack**: `Founders Grotesk X-Condensed`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `120px`, `12px`, `1em`, `80%`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `120px`, `12px`, `1em`, `80%`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 20px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fee422` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#c7cedb` | `.img-wait-logo:after { background-color: #c7cedb }` |
| **Interactive Accent / Highlight** | `#151723` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#151723` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dbc522` | `15 { border-color: #dbc522 }` |
| **Variable Token (`--white-clear`)** | `#ffffff` | `var(--white-clear)` in `:root` |
| **Variable Token (`--medium-blue-grey`)** | `#92939d` | `var(--medium-blue-grey)` in `:root` |
| **Variable Token (`--hyper-light-blue-grey`)** | `#e8edf3` | `var(--hyper-light-blue-grey)` in `:root` |
| **Variable Token (`--brown-yellow-bright`)** | `#d1c658` | `var(--brown-yellow-bright)` in `:root` |
| **Variable Token (`--blue-notif`)** | `#3acfe1` | `var(--blue-notif)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--primary-yellow` | `#fee422` | Brand / Palette Token |
| `--dark-blue` | `#151723` | Canvas / Surface Token |
| `--white-clear` | `#fff` | Canvas / Surface Token |
| `--medium-blue-grey` | `#92939d` | Color / Atmospheric Token |
| `--hyper-light-blue-grey` | `#e8edf3` | Canvas / Surface Token |
| `--brown-yellow-bright` | `#d1c658` | Color / Atmospheric Token |
| `--blue-notif` | `#3acfe1` | Color / Atmospheric Token |
| `--background` | `#fee422` | Canvas / Surface Token |
| `--foreground` | `#151723` | Typography Ink Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--11moissanstoit-c-bg` | `#fee422` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--11moissanstoit-c-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.h-full> — `11moissanstoit-com`)**:
   - Landmark `<header class="h-full">` (`1440px`) hosting `11 mois sans toi(t), le tour du mond` navigation (`MapLibre · EOxCloudless 2024 · CC BY-NC-SA · À propos`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.font-condensed> — `11 mois sans toi(t), le tour du mo`)**:
   - Landmark `<section class="font-condensed font-medium">` presenting display lead `11 mois sans toi(t), le tour du monde de Josué &` and copy excerpt *"OCTOBER 2010. PHILIPPE AND JOSUÉ, TWO CHILDHOOD FRIENDS, MAKE THE"* over `#fee422` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.font-medium> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="font-condensed font-medium">` rendering section `Featured Work & Interactive Showcase` with copy *"October 2010. Philippe and Josué , two childhood friends, make th"*, asset references (`logo-vecto.svg`, `photoLogo_11moissanstoi.png`, `2_er3-xpipny2.css`, `3cwyw8ne2vg7_.js`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.uppercase> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="font-condensed font-medium">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"a journey told in real time through their digital footprints, on "*) with `#c7cedb` surface cards, `#151723` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.inset-0> — `https://11moissanstoit.com/`)**:
   - Landmark `<footer class="inset-0">` anchoring `11 mois sans toi(t), le tour du ` footer links (`MapLibre · EOxCloudless 2024 · CC BY-NC-SA · À propos`), copy *"15 years later, for the anniversary of our return (August 24"*, and `#dbc522` structural dividers.
