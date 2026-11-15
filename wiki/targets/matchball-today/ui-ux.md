# UI & UX Architecture: matchball-today

## Overview & Design Identity
- **Target**: `matchball-today` (**Matchball · Football quiz: name the match ball in flight**)
- **Production URL**: [https://matchball.today/](https://matchball.today/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#e4e4de`)
- **Summary**: A free football quiz: historic match balls fly past in 3D and you name them. Every World Cup ball since 1930, plus Euros, Champions Leagu...
- **Total Clean CSS Variables Extracted**: `18` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Anton`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `22px`, `13px`, `15px`, `14px`, `16px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 17px`, `line-height: 1.2`, `letter-spacing: -.01em`, `font-weight: 700`)
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 1.4`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `22px`, `13px`, `15px`, `14px`, `16px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | `var(--tinta)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--papel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#efefea` | `var(--boton-gris)` in `:root` |
| **Interactive Accent / Highlight** | `#e4e4de` | `var(--boton-gris-encima)` in `:root` |
| **Secondary / Muted Copy** | `#5c5c57` | `var(--gris)` in `:root` |
| **Structural Hairline Border** | `#e2e2dc` | `var(--linea)` in `:root` |
| **Variable Token (`--apagado`)** | `#deded8` | `var(--apagado)` in `:root` |
| **Variable Token (`--noche`)** | `#07090d` | `var(--noche)` in `:root` |
| **Variable Token (`--fallo`)** | `#b3261e` | `var(--fallo)` in `:root` |
| **Variable Token (`--estudio`)** | `#f7f7f4` | `var(--estudio)` in `:root` |
| **Variable Token (`--estudio`)** | `#e9e9e4` | `var(--estudio)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cabecera` | `calc(56px + var(--aviso-cookies,0px))` | Dimension / Scale Token |
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
| `--alto-juego` | `288px` | Dimension / Scale Token |
| `--panel` | `clamp(360px, 29vw, 440px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fondo-campo> — `matchball-today`)**:
   - Landmark `<header class="fondo-campo">` hosting `Matchball · Football quiz: name the ` navigation (`Play, it’s free · All 50 match balls`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `a.boton-perfil { -webkit-tap-highlight-color:transparent;background:0 0;border:0 }`.
2. **Hero Stage & Focal Lead (<main.portada> — `Matchball`)**:
   - Landmark `<main class="portada">` presenting display lead `Matchball` and copy excerpt *"Historic footballs fly past. Name the ball or its tournament and "* over `#121212` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.portada> — `Historic footballs fly past. Name `)**:
   - Landmark `<main class="portada">` rendering section `Historic footballs fly past. Name the ball or it` with copy *"3 balls a day · no sign-up"*, asset references (`3nv7-x9qmrpfu.css`, `2ud8dty-w4gn-.css`, `00esfrgi11p6i.css`, `0ezmmnallg5cg.css`), and grid rule `.cabecera-coleccion { position:relative }`.
4. **Interactive Detail & Feature Matrix (<main.portada> — `3 balls a day · no sign-up`)**:
   - Landmark `<main class="portada">` framing `3 balls a day · no sign-up` and `All 50 match balls` (*"All 50 match balls"*) with `#efefea` surface cards, `#e4e4de` accents, and `after { content:"";background:currentColor;height:1.5px;position:absolute;bottom... }`.
5. **Colophon & Global Directory Footer (<footer.boton-perfil> — `https://matchball.today/`)**:
   - Landmark `<footer class="boton-perfil">` anchoring `Matchball · Football quiz: name ` footer links (`Play, it’s free · All 50 match balls`), copy *"3 balls a day · no sign-up"*, and `#e2e2dc` structural dividers.
