---
title: "UI & UX Architecture: www-lingers-it_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-lingers-it_en

## Overview & Design Identity
- **Target**: `www-lingers-it_en` (**Lingers – your hotel in Girlan**)
- **Production URL**: [https://www.lingers.it/en](https://www.lingers.it/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f7f7` canvas, `#777162` ink, `#000000` accent)
- **Summary**: Lingers is more than a hotel in Girlan. It’s your hideaway that makes you want to stay a little longer. And we can’t wait to welcome you.
- **Total Clean CSS Variables Extracted**: `61` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cinzel`
- **Body Font Stack**: `Cormorant Garamond`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 9.008px`, `line-height: 10.8096px`, `font-weight: 400`, `letter-spacing: 2.1px`); rule `h1` (`line-height: 1.2`, `letter-spacing: 2.1px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 9.008px`, `line-height: 9.008px`, `font-weight: 400`, `letter-spacing: 1.8px`); rule `h2` (`font-size: 1em`, `line-height: 1`, `letter-spacing: 1.8px`)
- **Body Copy**: live computed `body` (`font-size: 9.008px`, `line-height: 11.26px`, `font-weight: 400`); rule `p` (`font-size: 12px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 9.008px`, `line-height: 11.26px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f7f7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#777162` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#c4c4c4` | `var(--BN-dynform--clr-selection-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#9f9b91` | `var(--bl-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#0084f8` | `var(--BN-dynform--clr-schema-1-border)` in `:root` |
| **Variable Token (`--BN-dynform--clr-selection-text`)** | `#0b0b0b` | `var(--BN-dynform--clr-selection-text)` in `:root` |
| **Variable Token (`--BN-dynform--clr-form-bg`)** | `#ffffff` | `var(--BN-dynform--clr-form-bg)` in `:root` |
| **Variable Token (`--BN-dynform--clr-button-bg`)** | `#2865ad` | `var(--BN-dynform--clr-button-bg)` in `:root` |
| **Variable Token (`--BN-dynform--clr-schema-2-bg`)** | `#e2f0fd` | `var(--BN-dynform--clr-schema-2-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--BN-dynform--ff` | `inherit` | Design System Custom Token |
| `--BN-dynform--fw-bold` | `700` | Design System Custom Token |
| `--BN-dynform--fw-light` | `300` | Canvas / Surface Token |
| `--BN-dynform--fw-regular` | `400` | Design System Custom Token |
| `--BN-dynform--clr-scrollbar-thumb` | `#C4C4C4` | Color / Atmospheric Token |
| `--BN-dynform--clr-scrollbar-track` | `transparent` | Design System Custom Token |
| `--BN-dynform--clr-selection-bg` | `#C4C4C4` | Canvas / Surface Token |
| `--BN-dynform--clr-selection-text` | `#0B0B0B` | Typography Ink Token |
| `--BN-dynform--clr-form-bg` | `#ffffff` | Canvas / Surface Token |
| `--BN-dynform--clr-button-bg` | `#2865AD` | Canvas / Surface Token |
| `--BN-dynform--clr-button-border` | `#2865AD` | Elevation / Border Token |
| `--BN-dynform--clr-button-text` | `#ffffff` | Typography Ink Token |
| `--BN-dynform--clr-schema-1-bg` | `#0084F8` | Canvas / Surface Token |
| `--BN-dynform--clr-schema-1-border` | `#0084F8` | Elevation / Border Token |
| `--BN-dynform--clr-schema-1-text` | `#ffffff` | Typography Ink Token |
| `--BN-dynform--clr-schema-2-bg` | `#E2F0FD` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.DNA-section> — `www-lingers-it_en`)**:
   - Landmark `<header class="DNA-section">` (`1440x0px`) hosting `Lingers – your hotel in Girlan` navigation (`DE · IT · EN`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `page { margin:.5cm }`.
2. **Hero Stage & Focal Lead (<section.DNA-module> — `LINGER A LITTLE LONGER. IN OUR CHA`)**:
   - Landmark `<section class="DNA-module">` presenting display lead `LINGER A LITTLE LONGER. IN OUR CHARMING HOTEL IN...` and copy excerpt *"Lingers is an extraordinary place. Not your typical hotel in Girl"* over `#f7f7f7` canvas and `#777162` ink.
3. **Primary Showcase & Content Grid (<section.DNA-module:nth(2)> — `Linger a little longer. In our cha`)**:
   - Landmark `<section class="DNA-module">` rendering section `Linger a little longer. In our charming hotel in...` with copy *"Linger a little longer. In our charming hotel in Girlan."*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `body { font-family:Arial,sans-serif;font-size:12px }`.
4. **Interactive Detail & Feature Matrix (<section.DNA-module:nth(3)> — `Culinary concept: morning & aftern`)**:
   - Landmark `<section class="DNA-module">` framing `Culinary concept: morning & afternoon` and `Get active at our hotel in Girlan in South Tyrol` (*"Lingers is an extraordinary place. Not your typical hotel in Girl"*) with `#c4c4c4` surface cards, `#000000` accents, and `a:visited { text-decoration:none }`.
5. **Colophon & Global Directory Footer (<footer.DNA-section> — `https://www.lingers.it/en`)**:
   - Landmark `<footer class="DNA-section">` anchoring `Lingers – your hotel in Girlan` footer links (`DE · IT · EN`), copy *"We are the Lingers!"*, and `#0084f8` structural dividers.
