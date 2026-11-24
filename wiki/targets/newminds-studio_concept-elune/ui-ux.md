---
title: "UI & UX Architecture: newminds-studio_concept-elune"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: newminds-studio_concept-elune

## Overview & Design Identity
- **Target**: `newminds-studio_concept-elune` (**ELUNE — A Private Symptom Diary · New Minds Product Case**)
- **Production URL**: [https://newminds.studio/concept-elune](https://newminds.studio/concept-elune)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#faf7f3` canvas, `#4b303a` ink, `#d8ff65` accent)
- **Summary**: Inside ELUNE by New Minds: a calm daily check-in, a searchable symptom diary and privacy by design. Explore the iOS and Android product i...
- **Total Clean CSS Variables Extracted**: `53` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EluneSerif`
- **Body Font Stack**: `EluneSans`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 99px`, `line-height: 100.98px`, `font-weight: 400`, `letter-spacing: -4.455px`); rule `h1` (`font-size: clamp(60px,6.9vw,99px)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 63.36px`, `line-height: 64.6272px`, `font-weight: 400`, `letter-spacing: -2.8512px`); rule `h2` (`line-height: 1.02`, `letter-spacing: -.045em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 28px`, `font-weight: 400`); rule `p` (`font-size: 12px`, `line-height: 1.7`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 21px`, `font-weight: 400`); CSS variables `--mono: "DM Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`; rule `nav` (`font-size: 12px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#faf7f3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#4b303a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e6e0ef` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#d8ff65` | `.button-primary { background: #d8ff65 }` |
| **Secondary / Muted Copy** | `#a3a4ad` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e6ddd7` | `var(--ec-line)` in `:root` |
| **Variable Token (`--ec-muted`)** | `#74666b` | `var(--ec-muted)` in `:root` |
| **Variable Token (`--bg`)** | `#07080b` | `var(--bg)` in `:root` |
| **Variable Token (`--bg-soft`)** | `#0d0f14` | `var(--bg-soft)` in `:root` |
| **Variable Token (`--panel-solid`)** | `#11131a` | `var(--panel-solid)` in `:root` |
| **Variable Token (`--text`)** | `#f5f3ef` | `var(--text)` in `:root` |
| **Variable Token (`--muted-2`)** | `#6d707b` | `var(--muted-2)` in `:root` |
| **Variable Token (`--violet`)** | `#a88cff` | `var(--violet)` in `:root` |
| **Variable Token (`--cyan`)** | `#78e7ff` | `var(--cyan)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ec-ink` | `#4b303a` | Typography Ink Token |
| `--ec-muted` | `#74666b` | Color / Atmospheric Token |
| `--ec-paper` | `#faf7f3` | Canvas / Surface Token |
| `--ec-line` | `#e6ddd7` | Color / Atmospheric Token |
| `--bg` | `#07080b` | Canvas / Surface Token |
| `--bg-soft` | `#0d0f14` | Canvas / Surface Token |
| `--panel` | `rgba(18, 20, 27, 0.72)` | Color / Atmospheric Token |
| `--panel-solid` | `#11131a` | Color / Atmospheric Token |
| `--line` | `rgba(255, 255, 255, 0.12)` | Color / Atmospheric Token |
| `--line-strong` | `rgba(255, 255, 255, 0.2)` | Color / Atmospheric Token |
| `--text` | `#f5f3ef` | Typography Ink Token |
| `--muted` | `#a3a4ad` | Color / Atmospheric Token |
| `--muted-2` | `#6d707b` | Color / Atmospheric Token |
| `--acid` | `#d8ff65` | Color / Atmospheric Token |
| `--violet` | `#a88cff` | Color / Atmospheric Token |
| `--cyan` | `#78e7ff` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.ec-header> — `newminds-studio_concept-elune`)**:
   - Landmark `<header class="ec-header">` (`1440x96px`) hosting `ELUNE — A Private Symptom Diary · Ne` navigation (`Our work · Meet ELUNE ↗`), DOM attributes (`data-target="newminds-studio_concept-elune"`), and stylesheet rule `font-face { font-family:EluneSerif;src:url('/elune-newsreader.ttf') format('truetype... }`.
2. **Hero Stage & Focal Lead (<section.ec-hero> — `A little space to understand yours`)**:
   - Landmark `<section class="ec-hero">` presenting display lead `A little space to understand yourself.` and copy excerpt *"A NEW MINDS PRODUCT / iOS + ANDROID"* over `#faf7f3` canvas and `#4b303a` ink.
3. **Primary Showcase & Content Grid (<section.ec-section> — `Less to navigate. More room to not`)**:
   - Landmark `<section class="ec-section ec-opening">` rendering section `Less to navigate. More room to notice.` with copy *"A private symptom and cycle diary. Designed to make daily recordi"*, asset references (`concept-elune`, `elune-product-case.css`, `elune-product-today.jpg (ELUNE Today screen with a cycle overv...)`, `elune-product-symptoms.jpg (ELUNE check-in with optional intensit...)`), and grid rule `.elune-case a { color:inherit;text-decoration:none }`.
4. **Interactive Detail & Feature Matrix (<section.ec-feature> — `A quick check-in. At your own pace`)**:
   - Landmark `<section class="ec-feature ec-feature-warm">` framing `A quick check-in. At your own pace.` and `Your own starting point` (*"In private testing on iPhone and Android."*) with `#e6e0ef` surface cards, `#d8ff65` accents, and `.elune-case a:focus-visible { outline:3px solid 6c4960;outline-offset:5px }`.
5. **Colophon & Global Directory Footer (<footer.ec-footer> — `https://newminds.studio/concept-elune`)**:
   - Landmark `<footer class="ec-footer">` anchoring `ELUNE — A Private Symptom Diary ` footer links (`Our work · Meet ELUNE ↗`), copy *"Actual product interface · Example records"*, and `#e6ddd7` structural dividers.
