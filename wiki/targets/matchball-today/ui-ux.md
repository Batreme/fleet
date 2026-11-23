---
title: "UI & UX Architecture: matchball-today"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: matchball-today

## Overview & Design Identity
- **Target**: `matchball-today` (**Matchball · Football quiz: name the match ball in flight**)
- **Production URL**: [https://matchball.today/](https://matchball.today/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#5c5c57`)
- **Summary**: A free football quiz: historic match balls fly past in 3D and you name them. Every World Cup ball since 1930, plus Euros, Champions Leagu...
- **Total Clean CSS Variables Extracted**: `18` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 123.84px`, `line-height: 111.456px`, `font-weight: 400`, `letter-spacing: 1.2384px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 17px`, `line-height: 1.2`, `letter-spacing: -.01em`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 15px`, `line-height: 1.4`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#121212` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1f8a4c` | `.fin-dia-casillas i.bien { background: #1f8a4c }` |
| **Interactive Accent / Highlight** | `#5c5c57` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#5c5c57` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f0f0f0` | `.vitrina-ficha { border: #f0f0f0 }` |
| **Variable Token (`--boton-gris`)** | `#efefea` | `var(--boton-gris)` in `:root` |
| **Variable Token (`--boton-gris-encima`)** | `#e4e4de` | `var(--boton-gris-encima)` in `:root` |
| **Variable Token (`--linea`)** | `#e2e2dc` | `var(--linea)` in `:root` |
| **Variable Token (`--apagado`)** | `#deded8` | `var(--apagado)` in `:root` |
| **Variable Token (`--noche`)** | `#07090d` | `var(--noche)` in `:root` |
| **Variable Token (`--fallo`)** | `#b3261e` | `var(--fallo)` in `:root` |
| **Variable Token (`--estudio`)** | `#f7f7f4` | `var(--estudio)` in `:root` |
| **Variable Token (`--estudio`)** | `#e9e9e4` | `var(--estudio)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tinta` | `#121212` | Canvas / Surface Token |
| `--papel` | `#fff` | Color / Atmospheric Token |
| `--superficie` | `#fff` | Color / Atmospheric Token |
| `--boton-gris` | `#efefea` | Color / Atmospheric Token |
| `--boton-gris-encima` | `#e4e4de` | Color / Atmospheric Token |
| `--gris` | `#5c5c57` | Color / Atmospheric Token |
| `--linea` | `#e2e2dc` | Color / Atmospheric Token |
| `--apagado` | `#deded8` | Color / Atmospheric Token |
| `--noche` | `#07090d` | Color / Atmospheric Token |
| `--fallo` | `#b3261e` | Color / Atmospheric Token |
| `--estudio` | `linear-gradient(180deg, #fff 0%, #f7f7f4 55%, #e9e9e4 100%)` | Color / Atmospheric Token |
| `--ancho` | `600px` | Dimension / Scale Token |
| `--margen` | `16px` | Dimension / Scale Token |
| `--cabecera` | `56px` | Dimension / Scale Token |
| `--alto-juego` | `288px` | Dimension / Scale Token |
| `--panel` | `clamp(360px, 29vw, 440px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navegacion> — `matchball-today`)**:
   - Landmark `<nav class="navegacion portada-iconos">` (`175x44px`) hosting `Matchball · Football quiz: name the ` navigation (`Shop`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `a.boton-perfil { -webkit-tap-highlight-color:transparent;background:0 0;border:0 }`.
2. **Hero Stage & Focal Lead (<main.portada> — `MATCHBALL`)**:
   - Landmark `<main class="portada">` presenting display lead `MATCHBALL` and copy excerpt *"Historic footballs fly past. Name the ball or its tournament and "* over `#ffffff` canvas and `#121212` ink.
3. **Primary Showcase & Content Grid (<main.portada:nth(2)> — `Matchball`)**:
   - Landmark `<main class="portada">` rendering section `Matchball` with copy *"3 balls a day · no sign-up"*, asset references (`3nv7-x9qmrpfu.css`, `2ud8dty-w4gn-.css`, `2x5jyq1p60s2x.css`, `17ygr9mac-are.css`), and grid rule `.navegacion { white-space:nowrap;align-items:center;display:flex }`.
4. **Interactive Detail & Feature Matrix (<main.portada:nth(3)> — `3 balls a day · no sign-up`)**:
   - Landmark `<main class="portada">` framing `3 balls a day · no sign-up` and `matchball-today Archive & Directory` (*"Matchball"*) with `#1f8a4c` surface cards, `#5c5c57` accents, and `.cabecera-coleccion { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.nav> — `https://matchball.today/`)**:
   - Landmark `<footer class="nav">` anchoring `Matchball · Football quiz: name ` footer links (`Shop`), copy *"3 balls a day · no sign-up"*, and `#f0f0f0` structural dividers.
