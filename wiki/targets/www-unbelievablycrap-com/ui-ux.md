---
title: "UI & UX Architecture: www-unbelievablycrap-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-unbelievablycrap-com

## Overview & Design Identity
- **Target**: `www-unbelievablycrap-com` (**Liubomyr Ulytskyi - Digital Designer**)
- **Production URL**: [https://www.unbelievablycrap.com/](https://www.unbelievablycrap.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#e8271c`)
- **Summary**: Liubomyr Ulytskyi — Digital Designer, award-winning UI/UX Designer, art director, conceptualist.
- **Total Clean CSS Variables Extracted**: `86` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Supply Sans`
- **Body Font Stack**: `PP Supply Sans`
- **Monospace / Technical Font Stack**: `PP Supply Mono`
- **Hero Display (`H1`)**: observed font-size ladder: `128px`, `16px`, `10px`, `14px`, `var(--ui-10)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 128px`, `line-height: 102px`, `font-weight: 400`, `letter-spacing: -5.12px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: var(--ui-10)`, `line-height: 10px`, `letter-spacing: -0.4px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-mono: 'PP Supply Mono',ui-monospace,'SF Mono','Roboto Mono',monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#393939` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#e8271c` | `.trk__btn:hover { color: #e8271c }` |
| **Secondary / Muted Copy** | `#393939` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#393939` | hairline divider derived from live computed `button` `color` (`computed_styles.json`) |
| **Variable Token (`--c-fog`)** | `#afafaf` | `var(--c-fog)` in `:root` |
| **Variable Token (`--c-slate`)** | `#6e6e6e` | `var(--c-slate)` in `:root` |
| **Variable Token (`--c-label`)** | `#636363` | `var(--c-label)` in `:root` |
| **Variable Token (`--c-fade`)** | `#c3c3c3` | `var(--c-fade)` in `:root` |
| **Variable Token (`--ui-grey`)** | `#c8c8c8` | `var(--ui-grey)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-mono` | `'PP Supply Mono',ui-monospace,'SF Mono','Roboto Mono',monospace` | Typography / Scale Token |
| `--c-white` | `#ffffff` | Canvas / Surface Token |
| `--c-fog` | `#afafaf` | Color / Atmospheric Token |
| `--c-slate` | `#6e6e6e` | Color / Atmospheric Token |
| `--c-label` | `#636363` | Color / Atmospheric Token |
| `--c-fade` | `#c3c3c3` | Color / Atmospheric Token |
| `--c-ink` | `#393939` | Typography Ink Token |
| `--hud-size` | `14px` | Layout / Spatial Grid Token |
| `--tracking` | `-0.04em` | Typography / Scale Token |
| `--ui-ink` | `#393939` | Typography Ink Token |
| `--ui-dim` | `rgba(57,57,57,.5)` | Color / Atmospheric Token |
| `--ui-red` | `#e8271c` | Color / Atmospheric Token |
| `--ui-grey` | `#c8c8c8` | Color / Atmospheric Token |
| `--ui-bar` | `#393939` | Color / Atmospheric Token |
| `--ui-10` | `10px` | Dimension / Scale Token |
| `--ui-14` | `14px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.ftr__nav> — `www-unbelievablycrap-com`)**:
   - Landmark `<nav class="ftr__nav">` (`181x10px`) hosting `Liubomyr Ulytskyi - Digital Designer` navigation (`index · work · gallery · 404`), DOM attributes (`data-err-src="ERR_ART"`, `data-err-src="ERR_CARD"`, `data-mesh-var="FIGURE_LITE"`, `data-mesh-var="LOGO_MESH"`), and stylesheet rule `.ftr { position: fixed; inset: 0; z-index: 62; color: 000; pointer-events: none... }`.
2. **Hero Stage & Focal Lead (<main.gate> — `find your way out of here`)**:
   - Landmark `<main class="gate">` presenting display lead `find your way out of here` and copy excerpt *"CASE FILE: THE MAN BEHIND THE IMAGE"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.gate__bg> — `CASE FILE: THE MAN BEHIND THE IMAG`)**:
   - Landmark `<main class="gate__bg">` rendering section `CASE FILE: THE MAN BEHIND THE IMAGE` with copy *"The first mistake was assuming Liubomyr was looking for something"*, asset references (`favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`), and grid rule `.ftr.is-live { visibility: visible; }`.
4. **Interactive Detail & Feature Matrix (<main.gate__logo> — `The first mistake was assuming Liu`)**:
   - Landmark `<main class="gate__logo">` framing `The first mistake was assuming Liubomyr was look` and `He was 0looking for what 3was hiding.` (*"He was 0looking for what 3was hiding."*) with `#393939` surface cards, `#e8271c` accents, and `.ftr.is-open button { pointer-events: auto; }`.
5. **Colophon & Global Directory Footer (<footer.bar> — `https://www.unbelievablycrap.com/`)**:
   - Landmark `<footer class="bar">` anchoring `Liubomyr Ulytskyi - Digital Desi` footer links (`index · work · gallery · 404`), copy *"There’s a difference."*, and `#393939` structural dividers.
