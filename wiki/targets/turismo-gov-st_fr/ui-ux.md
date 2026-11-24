---
title: "UI & UX Architecture: turismo-gov-st_fr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: turismo-gov-st_fr

## Overview & Design Identity
- **Target**: `turismo-gov-st_fr` (**Homepage · São Tomé E Príncipe**)
- **Production URL**: [https://turismo.gov.st/fr](https://turismo.gov.st/fr)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#eeedea` canvas, `#000000` ink, `#008000` accent)
- **Summary**: Ce que vous devez savoir sur la taxe de tourisme
- **Total Clean CSS Variables Extracted**: `103` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `gyst-variable`
- **Body Font Stack**: `Outfit`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 50px`, `line-height: 55px`, `font-weight: 400`, `letter-spacing: 0.5px`); CSS variables `--font-display: gyst-variable,serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 35px`, `line-height: 38.5px`, `font-weight: 400`, `letter-spacing: 0.35px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-body: Outfit,Arial,Helvetica,sans-serif`, `--paragraph-max-width: 100%`, `--paragraph-margin-bottom: 0`; rule `p` (`font-size: var(--fz-size, 1.7rem)`, `line-height: 1.5`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#eeedea` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.progress__track { background-color: #ffffff }` |
| **Interactive Accent / Highlight** | `#008000` | `.button--primary--dark { color: green }` (`#008000`) |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#bbbbbb` | `.webform-readonly textarea { border-color: #bbbbbb }` |
| **Variable Token (`--color-green--dark`)** | `#38492a` | `var(--color-green--dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-white--30` | `rgba(255, 255, 255, 0.3)` | Canvas / Surface Token |
| `--color-white--00` | `rgba(255, 255, 255, 0)` | Canvas / Surface Token |
| `--color-white--15` | `rgba(255, 255, 255, 0.15)` | Canvas / Surface Token |
| `--color-white--08` | `rgba(255, 255, 255, 0.08)` | Canvas / Surface Token |
| `--color-black` | `#000000` | Canvas / Surface Token |
| `--color-black--05` | `rgba(0, 0, 0, 0.05)` | Canvas / Surface Token |
| `--color-black--08` | `rgba(0, 0, 0, 0.08)` | Canvas / Surface Token |
| `--color-black--15` | `rgba(0, 0, 0, 0.15)` | Canvas / Surface Token |
| `--color-black--00` | `rgba(0, 0, 0, 0)` | Canvas / Surface Token |
| `--color-black--10` | `rgba(0, 0, 0, 0.1)` | Canvas / Surface Token |
| `--color-black--30` | `rgba(0, 0, 0, 0.3)` | Canvas / Surface Token |
| `--color-black--50` | `rgba(0, 0, 0, 0.5)` | Canvas / Surface Token |
| `--color-black--70` | `rgba(0, 0, 0, 0.7)` | Canvas / Surface Token |
| `--color-green--dark` | `#38492A` | Canvas / Surface Token |
| `--color-green--dark--30` | `rgba(56, 73, 42, 0.3)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Header> — `turismo-gov-st_fr`)**:
   - Landmark `<header class="Header">` (`1440x120px`) hosting `Homepage · São Tomé E Príncipe` navigation (`Nature · Un éden insulaire · Une flore luxuriante · Plages de sable doré · Croyances`), DOM attributes (`data-barba="wrapper"`, `data-once="form-single-submit we..."`, `data-off-canvas-main-canvas`, `data-container-query-observer-bae45330cd3d4e0e96b60d26b57009b5-1795453191897-0`), and stylesheet rule `.webform-flexbox { display: flex; margin: 1em -0.5em; }`.
2. **Hero Stage & Focal Lead (<section.Homepage> — `São Tomé e Príncipe`)**:
   - Landmark `<section class="Homepage node">` presenting display lead `São Tomé e Príncipe` and copy excerpt *"Ce que vous devez savoir sur la taxe de tourisme"* over `#eeedea` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.ParagraphImmersiveMesh> — `Pourquoi São Tomé?`)**:
   - Landmark `<section class="ParagraphImmersiveMesh paragraph">` rendering section `Pourquoi São Tomé?` with copy *"expérience sensorielle"*, asset references (`sdk.js`, `gtm.js`, `favicon.png`, `webform.element.flexbox.css`), and grid rule `.webform-flexbox .webform-flexbox { margin: 1em 0; }`.
4. **Interactive Detail & Feature Matrix (<section.ParagraphVerticalSlider> — `Une expérience totale, pure et sau`)**:
   - Landmark `<section class="ParagraphVerticalSlider paragraph">` framing `Une expérience totale, pure et sauvage` and `Nos activités` (*"envoûtement océanique"*) with `#ffffff` surface cards, `#008000` accents, and `.webform-flexbox--justify-flex-start { justify-content: flex-start; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://turismo.gov.st/fr`)**:
   - Landmark `<footer class="footer">` anchoring `Homepage · São Tomé E Príncipe` footer links (`Nature · Un éden insulaire · Une flore luxuriante · Plages de sable doré · Croyances`), copy *"immersion culturelle"*, and `#bbbbbb` structural dividers.
