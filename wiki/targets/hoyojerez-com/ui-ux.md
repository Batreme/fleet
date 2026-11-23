---
title: "UI & UX Architecture: hoyojerez-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: hoyojerez-com

## Overview & Design Identity
- **Target**: `hoyojerez-com` (**HOYO Jerez · Discoteca en Jerez de la Frontera**)
- **Production URL**: [https://hoyojerez.com/](https://hoyojerez.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#010101` / `#5be010`)
- **Summary**: HOYO, la discoteca de Jerez de la Frontera. Entra en el túnel: próximas fiestas y entradas, las fotos de cada noche y dónde encontrarnos.
- **Total Clean CSS Variables Extracted**: `6` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Panchang`
- **Body Font Stack**: `Morganite`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `9.52381px`, `14px`, `10px`, `13px`, `28px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 9.52381px`, `line-height: 9.52381px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 9.52381px`, `line-height: 9.52381px`, `font-weight: 400`); rule `p` (`font-size: 13px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 9.52381px`, `line-height: 9.52381px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#010101` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1d1d1b` | `._linea_1qcud_61 { background: #1d1d1b }` |
| **Interactive Accent / Highlight** | `#5be010` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#5be010` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#343434` | `preferences_1d25v_98 ._necessar... { border-top: #343434 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tamano` | `22px` | Dimension / Scale Token |
| `--nivel` | `1` | Design System Custom Token |
| `--pista` | `2px` | Dimension / Scale Token |
| `--pulgar` | `9px` | Dimension / Scale Token |
| `--retraso` | `.2s` | Motion / Timing Token |
| `--cookies-tapa` | `311px` | Dimension / Scale Token |
| `--hoyojerez-com-bg` | `#010101` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--hoyojerez-com-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--hoyojerez-com-surface` | `#1d1d1b` | Surface Substrate (computed-derived) |
| `--hoyojerez-com-accent` | `#5be010` | Interactive Accent (computed-derived) |
| `--hoyojerez-com-muted` | `#5be010` | Secondary Ink (computed-derived) |
| `--hoyojerez-com-border` | `#343434` | Structural Border (computed-derived) |
| `--hoyojerez-com-container` | `1440px` | Container Bound (computed-derived) |
| `--hoyojerez-com-gap` | `20px` | Grid Gutter (computed-derived) |
| `--hoyojerez-com-pad` | `20px` | Lateral Padding (computed-derived) |
| `--hoyojerez-com-ease` | `cubic-bezier(.2,.85,.25,1)` | Primary Easing Function |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `hoyojerez-com`)**:
   - Landmark `<header class="lenis">` (`1400x50px`) hosting `HOYO Jerez · Discoteca en Jerez de l` navigation (`Galería · Eventos · Contacto`), DOM attributes (`data-astro-cid-wetux6vv`, `data-astro-exec`, `data-astro-transition-persist="hoyo-tunnel"`, `data-persistent-tunnel`), and stylesheet rule `._panel_1d25v_1 { padding:22px;bottom:28px;left:28px }`.
2. **Hero Stage & Focal Lead (<main.main-content> — `Eventos`)**:
   - Landmark `<main class="main-content">` presenting display lead `Eventos` and copy excerpt *"Paciencia, se está cargando el Hoyo."* over `#010101` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.main-content:nth(2)> — `Galería`)**:
   - Landmark `<main class="main-content">` rendering section `Galería` with copy *"La conexión va lenta · seguimos cargando"*, asset references (`index.astro_astro_type_script_ind...`, `alien.DVECqh-s.glb`, `pulsador.BQ51WIjM.glb`, `draco_wasm_wrapper.js`), and grid rule `._panel_1d25v_1 h2 { text-transform:uppercase;color:5be010;margin:8px 0 12px;font:900 44px/.9... }`.
4. **Interactive Detail & Feature Matrix (<main.main-content:nth(3)> — `Proyección`)**:
   - Landmark `<main class="main-content">` framing `Proyección` and `No se pudo cargar el Hoyo` (*"No se pudo cargar el Hoyo"*) with `#1d1d1b` surface cards, `#5be010` accents, and `._panel_1d25v_1 p { margin:0 0 14px;font-size:13px }`.
5. **Colophon & Global Directory Footer (<footer.intro-cargando> — `https://hoyojerez.com/`)**:
   - Landmark `<footer class="intro-cargando">` anchoring `HOYO Jerez · Discoteca en Jerez ` footer links (`Galería · Eventos · Contacto`), copy *"HOYO / Tu privacidad"*, and `#343434` structural dividers.
