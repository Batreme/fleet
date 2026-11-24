---
title: "UI & UX Architecture: allsorts-andrew-rip"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: allsorts-andrew-rip

## Overview & Design Identity
- **Target**: `allsorts-andrew-rip` (**Allsorts · Andrew Robinson**)
- **Production URL**: [https://allsorts.andrew.rip](https://allsorts.andrew.rip)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#dddddd`)
- **Summary**: Liquorice allsorts to throw, pile and frame, rendered in your browser. Save one as a wallpaper. By Andrew Robinson.
- **Total Clean CSS Variables Extracted**: `1` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Soehne`
- **Body Font Stack**: `Tiempos Fine`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `15px`, `13px`, `12px`, `14px`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `15px`, `13px`, `12px`, `14px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 21.75px`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#111111` | `.lens.svelte-11id0ew { background: #111111 }` |
| **Interactive Accent / Highlight** | `#dddddd` | `.panel.svelte-1yxt74e button { color: #dddddd }` |
| **Secondary / Muted Copy** | `#777777` | `.dim.svelte-1tmptad { color: #777777 }` |
| **Structural Hairline Border** | `#262626` | `.total.svelte-qxof8p { border-top: #262626 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `48px` | Layout / Spatial Grid Token |
| `--allsorts-andrew--bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--allsorts-andrew--ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--allsorts-andrew--surface` | `#111111` | Surface Substrate (computed-derived) |
| `--allsorts-andrew--accent` | `#dddddd` | Interactive Accent (computed-derived) |
| `--allsorts-andrew--muted` | `#777777` | Secondary Ink (computed-derived) |
| `--allsorts-andrew--border` | `#262626` | Structural Border (computed-derived) |
| `--allsorts-andrew--container` | `1440px` | Container Bound (computed-derived) |
| `--allsorts-andrew--gap` | `12px` | Grid Gutter (computed-derived) |
| `--allsorts-andrew--pad` | `8px` | Lateral Padding (computed-derived) |
| `--allsorts-andrew--ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--allsorts-andrew--radius` | `999px` | Corner Radius (computed-derived) |
| `--allsorts-andrew--fs-base` | `16px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.stage> — `allsorts-andrew-rip`)**:
   - Landmark `<header class="stage">` (`1440px`) hosting `Allsorts · Andrew Robinson` navigation (`Andrew Robinson`), DOM attributes (`data-website-id="ffd157e7-cca9-4ad9-ad..."`, `data-domains="allsorts.andrew.rip"`, `data-auto-track="true"`, `data-auto-pageview="false"`), and stylesheet rule `font-face { font-family:Soehne;src:url(../../../fonts/soehne-leicht.woff2)format("wo... }`.
2. **Hero Stage & Focal Lead (<div.svelte-1pzb9eq> — `Allsorts · Andrew Robinson`)**:
   - Landmark `<div class="svelte-1pzb9eq">` presenting display lead `Allsorts · Andrew Robinson` and copy excerpt *"Allsorts Andrew Robinson"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.light> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="light">` rendering section `Featured Work & Interactive Showcase` with copy *"Liquorice allsorts to throw, pile and frame, rendered on your gra"*, asset references (`start.ChVgNEA1.js`, `payload.DSmR2FwN.js`, `CRzLMJPS.js`, `CKKoTArS.js`), and grid rule `body { overscroll-behavior:none;background:000;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<div.fallback> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="fallback">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Open it in the latest Chrome, Edge or Safari. In an app? Open it "*) with `#111111` surface cards, `#dddddd` accents, and `.row.svelte-qxof8p { justify-content:space-between;gap:12px;display:flex }`.
5. **Colophon & Global Directory Footer (<footer.words> — `https://allsorts.andrew.rip`)**:
   - Landmark `<footer class="words">` anchoring `Allsorts · Andrew Robinson` footer links (`Andrew Robinson`), copy *"Technical Architecture & Narrative"*, and `#262626` structural dividers.
