# UI & UX Architecture: allsorts-andrew-rip

## Overview & Design Identity
- **Target**: `allsorts-andrew-rip` (**Allsorts · Andrew Robinson**)
- **Production URL**: [https://allsorts.andrew.rip](https://allsorts.andrew.rip)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#888`)
- **Summary**: Liquorice allsorts to throw, pile and frame, rendered in your browser. Save one as a wallpaper. By Andrew Robinson.
- **Total Clean CSS Variables Extracted**: `1` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Soehne`
- **Body Font Stack**: `Tiempos Fine`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `body { background: #000 }` |
| **Primary Typography Ink** | `#ddd` | `.hud.svelte-qxof8p { color: #ddd }` |
| **Elevated Surface / Card Substrate** | `#fff` | `.big.svelte-qxof8p { color: #fff }` |
| **Interactive Accent / Highlight** | `#888` | `.dim.svelte-qxof8p { color: #888 }` |
| **Secondary / Muted Copy** | `#777` | `.dim.svelte-1tmptad { color: #777 }` |
| **Structural Hairline Border** | `#999` | `.quiet.svelte-1yxt74e { color: #999 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `48px` | Layout / Spatial Grid Token |
| `--allsorts-andrew--bg` | `#000` | Canvas Substrate (from `body { background: #000 }`) |
| `--allsorts-andrew--ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--allsorts-andrew--surface` | `#fff` | Surface Substrate (stylesheet-derived) |
| `--allsorts-andrew--accent` | `#888` | Interactive Accent (stylesheet-derived) |
| `--allsorts-andrew--muted` | `#777` | Secondary Ink (stylesheet-derived) |
| `--allsorts-andrew--border` | `#999` | Structural Border (stylesheet-derived) |
| `--allsorts-andrew--container` | `460px` | Container Bound (stylesheet-derived) |
| `--allsorts-andrew--gap` | `12px` | Grid Gutter (stylesheet-derived) |
| `--allsorts-andrew--pad` | `8px` | Lateral Padding (stylesheet-derived) |
| `--allsorts-andrew--ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--allsorts-andrew--radius` | `6px` | Corner Radius (stylesheet-derived) |
| `--allsorts-andrew--fs-base` | `13px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.stage> — `allsorts-andrew-rip`)**:
   - Landmark `<header class="stage">` hosting `Allsorts · Andrew Robinson` navigation (`Andrew Robinson`), DOM attributes (`data-website-id="ffd157e7-cca9-4ad9-ad..."`, `data-domains="allsorts.andrew.rip"`, `data-auto-track="true"`, `data-auto-pageview="false"`), and stylesheet rule `font-face { font-family:Soehne;src:url(../../../fonts/soehne-leicht.woff2)format("wo... }`.
2. **Hero Stage & Focal Lead (<div.svelte-1pzb9eq> — `Allsorts · Andrew Robinson`)**:
   - Landmark `<div class="svelte-1pzb9eq">` presenting display lead `Allsorts · Andrew Robinson` and copy excerpt *"Allsorts Andrew Robinson"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.light> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="light">` rendering section `Featured Work & Interactive Showcase` with copy *"Liquorice allsorts to throw, pile and frame, rendered on your gra"*, asset references (`start.ChVgNEA1.js`, `payload.DSmR2FwN.js`, `CRzLMJPS.js`, `CKKoTArS.js`), and grid rule `body { overscroll-behavior:none;background:000;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<div.fallback> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="fallback">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Open it in the latest Chrome, Edge or Safari. In an app? Open it "*) with `#fff` surface cards, `#888` accents, and `.row.svelte-qxof8p { justify-content:space-between;gap:12px;display:flex }`.
5. **Colophon & Global Directory Footer (<footer.words> — `https://allsorts.andrew.rip`)**:
   - Landmark `<footer class="words">` anchoring `Allsorts · Andrew Robinson` footer links (`Andrew Robinson`), copy *"Technical Architecture & Narrative"*, and `#999` structural dividers.
