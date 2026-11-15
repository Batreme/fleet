---
title: "UI Prompt Blueprint: matchball-today"
date: 2026-11-15
target: "[[overview|matchball-today]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#e4e4de`)"
---

# UI Design System & Master Generation Blueprint: matchball-today

> **Matchball · Football quiz: name the match ball in flight** (https://matchball.today/) — A free football quiz: historic match balls fly past in 3D and you name them. Every World Cup ball since 1930, plus Euros, Champions Leagu...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Matchball · Football quiz: name the match ball in flight** (`https://matchball.today/`). A free football quiz: historic match balls fly past in 3D and you name them. Every World Cup ball since 1930, plus Euros, Champions Leagu...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#e4e4de`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#121212` (`var(--tinta)` in `:root`) paired with `#fff` primary typography and `#e4e4de` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter Tight` for display copy (`Matchball`) with `Anton` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `374px` container bounds (`gap: 12px`, padding `10px`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `374px` extracted from `matchball-today` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `14px`, `50%`, `12px`, `16px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 374px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:374px)`, `@media not all and (min-width:900px) and (min-aspect-ratio:1)`, `@media (orientation:landscape) and (max-height:500px) and (max-w...`, `@media (min-width:900px) and (min-aspect-ratio:1)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
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

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
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

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter Tight`.
- **Primary Body Stack**: `Anton`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `22px`, `13px`, `15px`, `14px`, `16px`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 17px`, `line-height: 1.2`, `letter-spacing: -.01em`, `font-weight: 700`).
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 1.4`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `22px`, `13px`, `15px`, `14px`, `16px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.panel-cargando .panel-cifras`**: `transition: opacity .2s` extracted from `matchball-today` stylesheet.
- **Selector `.resultado [data-entra]`**: `transition: opacity .22s ease-out` extracted from `matchball-today` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `matchball-today` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.fondo-campo>` and `<main.portada>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Matchball · Football quiz: name the match  │
│ ====================================================================== │
│ [ <header.fondo-campo>     | Play, it’s free · All 50 match balls   ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.portada>                                       |   │
│ | H1: Matchball                                                    |   │
│ | Substrate: #121212    | Ink: #fff       | Accent: #e4e4de        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.portada>            ) max-w: 374px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Historic footballs fly past. |  | 3 balls a day · no sign-up   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.fondo-camp] -> [<main.portada>] -> [<main.portada>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.boton-perfil> ) | https://matchball.today/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
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

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: matchball-today (Matchball · Football quiz: name the match ball in flight)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `matchball-today` (**Matchball · Football quiz: name the match ball in flight** — `https://matchball.today/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#e4e4de`).
- **Identity & Domain Context**: A free football quiz: historic match balls fly past in 3D and you name them. Every World Cup ball since 1930, plus Euros, Champions Leagu...
- **Primary Substrate**: `#121212` (`var(--tinta)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#e4e4de`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#121212` (`var(--tinta)` in `:root`) paired with `#fff` primary typography and `#e4e4de` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter Tight` for display copy (`Matchball`) with `Anton` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `374px` container bounds (`gap: 12px`, padding `10px`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `matchball-today` in your global stylesheet:

:root {
  /* Matchball · Football quiz: name the match ball in flight (matchball-today) — Ground-Truth Extracted CSS Variables */
  --cabecera: calc(56px + var(--aviso-cookies,0px)); /* Dimension / Scale Token (matchball-today) */
  --tinta: #121212; /* Canvas / Surface Token (matchball-today) */
  --papel: #fff; /* Color / Atmospheric Token (matchball-today) */
  --superficie: #fff; /* Color / Atmospheric Token (matchball-today) */
  --boton-gris: #efefea; /* Color / Atmospheric Token (matchball-today) */
  --boton-gris-encima: #e4e4de; /* Color / Atmospheric Token (matchball-today) */
  --gris: #5c5c57; /* Color / Atmospheric Token (matchball-today) */
  --linea: #e2e2dc; /* Color / Atmospheric Token (matchball-today) */
  --apagado: #deded8; /* Color / Atmospheric Token (matchball-today) */
  --noche: #07090d; /* Color / Atmospheric Token (matchball-today) */
  --fallo: #b3261e; /* Color / Atmospheric Token (matchball-today) */
  --estudio: linear-gradient(180deg, #fff 0%, #f7f7f4 55%, #e9e9e4 100%); /* Color / Atmospheric Token (matchball-today) */
  --ancho: 600px; /* Dimension / Scale Token (matchball-today) */
  --margen: 16px; /* Dimension / Scale Token (matchball-today) */
  --alto-juego: 288px; /* Dimension / Scale Token (matchball-today) */
  --panel: clamp(360px, 29vw, 440px); /* Dimension / Scale Token (matchball-today) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#121212` — grounded in `var(--tinta)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--papel)` in `:root`
- **Elevated Surface / Card Substrate**: `#efefea` — grounded in `var(--boton-gris)` in `:root`
- **Interactive Accent / Highlight**: `#e4e4de` — grounded in `var(--boton-gris-encima)` in `:root`
- **Secondary / Muted Copy**: `#5c5c57` — grounded in `var(--gris)` in `:root`
- **Structural Hairline Border**: `#e2e2dc` — grounded in `var(--linea)` in `:root`
- **Variable Token (`--apagado`)**: `#deded8` — grounded in `var(--apagado)` in `:root`
- **Variable Token (`--noche`)**: `#07090d` — grounded in `var(--noche)` in `:root`
- **Variable Token (`--fallo`)**: `#b3261e` — grounded in `var(--fallo)` in `:root`
- **Variable Token (`--estudio`)**: `#f7f7f4` — grounded in `var(--estudio)` in `:root`
- **Variable Token (`--estudio`)**: `#e9e9e4` — grounded in `var(--estudio)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `374px` extracted from `matchball-today` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 374px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (max-width:374px)`, `@media not all and (min-width:900px) and (min-aspect-ratio:1)`, `@media (orientation:landscape) and (max-height:500px) and (max-w...`, `@media (min-width:900px) and (min-aspect-ratio:1)`
- **Corner Radii**: `14px`, `50%`, `12px`, `16px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Anton`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `22px`, `13px`, `15px`, `14px`, `16px`)
- **H2 Section Rule**: rule `h2` (`font-size: 17px`, `line-height: 1.2`, `letter-spacing: -.01em`, `font-weight: 700`)
- **Body Copy Rule**: rule `p` (`font-size: 15px`, `line-height: 1.4`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `22px`, `13px`, `15px`, `14px`, `16px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `matchball-today` (`Matchball · Football quiz: name the match ball in flight`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fondo-campo> — `matchball-today`)**:
   - DOM & Selectors: Landmark `<header class="fondo-campo">` hosting `Matchball · Football quiz: name the ` navigation (`Play, it’s free · All 50 match balls`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `a.boton-perfil { -webkit-tap-highlight-color:transparent;background:0 0;border:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fondo-campo> — `matchball-today`)` (`matchball-today`) adapts across `@media (max-width:374px)`, `@media not all and (min-width:900px) and (min-aspect-ratio:1)`, `@media (orientation:landscape) and (max-height:500px) and (max-w...`, `@media (min-width:900px) and (min-aspect-ratio:1)` with `cubic-bezier(.2,.8,.2,1)` transitions and links `Play, it’s free · All 50 match balls`.
2. **Hero Stage & Focal Lead (<main.portada> — `Matchball`)**:
   - DOM & Selectors: Landmark `<main class="portada">` presenting display lead `Matchball` and copy excerpt *"Historic footballs fly past. Name the ball or its tournament and "* over `#121212` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#121212` background with `#fff` headline `Matchball`.
3. **Primary Showcase & Content Grid (<main.portada> — `Historic footballs fly past. Name `)**:
   - DOM & Selectors: Landmark `<main class="portada">` rendering section `Historic footballs fly past. Name the ball or it` with copy *"3 balls a day · no sign-up"*, asset references (`3nv7-x9qmrpfu.css`, `2ud8dty-w4gn-.css`, `00esfrgi11p6i.css`, `0ezmmnallg5cg.css`), and grid rule `.cabecera-coleccion { position:relative }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.portada> — `Historic footballs fly past. Name `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 374px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.portada> — `3 balls a day · no sign-up`)**:
   - DOM & Selectors: Landmark `<main class="portada">` framing `3 balls a day · no sign-up` and `All 50 match balls` (*"All 50 match balls"*) with `#efefea` surface cards, `#e4e4de` accents, and `after { content:"";background:currentColor;height:1.5px;position:absolute;bottom... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.portada> — `3 balls a day · no sign-up`)` uses `14px`, `50%`, `12px`, `16px` radii, `#e4e4de` highlights, and assets (3nv7-x9qmrpfu.css, 2ud8dty-w4gn-.css, 00esfrgi11p6i.css).
5. **Colophon & Global Directory Footer (<footer.boton-perfil> — `https://matchball.today/`)**:
   - DOM & Selectors: Landmark `<footer class="boton-perfil">` anchoring `Matchball · Football quiz: name ` footer links (`Play, it’s free · All 50 match balls`), copy *"3 balls a day · no sign-up"*, and `#e2e2dc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.boton-perfil> — `https://matchball.today/`)` aligns to `374px` extracted from `matchball-today` stylesheet with `10px` lateral canvas padding with `12px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Historic footballs fly past. Name the ball or its tournament and collect them all."*
- Copy Excerpt 2: *"3 balls a day · no sign-up"*
- Copy Excerpt 3: *"All 50 match balls"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`
- **Extracted Stylesheet Rules (`matchball-today`)**:
- `a.boton-perfil { -webkit-tap-highlight-color:transparent;background:0 0;border:0 }`
- `.cabecera-coleccion { position:relative }`
- `after { content:"";background:currentColor;height:1.5px;position:absolute;bottom... }`
- `.cabecera .logo { font-size:22px }`
- `.cabecera .nav a { padding:0 4px }`
- **Per-Selector Transition Rules**:
- **Selector `.panel-cargando .panel-cifras`**: `transition: opacity .2s` extracted from `matchball-today` stylesheet.
- **Selector `.resultado [data-entra]`**: `transition: opacity .22s ease-out` extracted from `matchball-today` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `matchball-today` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.fondo-campo>` and `<main.portada>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `matchball-today`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
