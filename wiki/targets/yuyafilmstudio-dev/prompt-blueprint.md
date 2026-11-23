---
title: "UI Prompt Blueprint: yuyafilmstudio-dev"
date: 2026-11-23
captured_at: 2026-11-23
target: "yuyafilmstudio-dev"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0a` / `#dddddd`)"
---

# UI Design System & Master Generation Blueprint: yuyafilmstudio-dev

> **YUYA FILM STUDIO** (https://yuyafilmstudio.dev/) — Walk through YUYA FILM STUDIO — a working film company built from Yuya's real Video OS, projects and footage.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **YUYA FILM STUDIO** (`https://yuyafilmstudio.dev/`). Walk through YUYA FILM STUDIO — a working film company built from Yuya's real Video OS, projects and footage.
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0a` / `#dddddd`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0b0b0a` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f2ede4` primary typography and `#dddddd` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`YUYA FILM STUDIO`) with `Inter` and `Courier Prime`.
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 10px`, padding `2px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1400px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `2px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `3px`, `50%`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1000px)`, `@media (max-width:640px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:720px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0b0a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f2ede4` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0f0e0c` | `.bf-route li:before { background: #0f0e0c }` |
| **Interactive Accent / Highlight** | `#dddddd` | `.vf-shots button { color: #dddddd }` |
| **Secondary / Muted Copy** | `#a39e94` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#5c5a56` | `kbd { border: #5c5a56 }` |
| **Variable Token (`--gold`)** | `#c9a96e` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-dim`)** | `#8c7650` | `var(--gold-dim)` in `:root` |
| **Variable Token (`--rec`)** | `#e0402f` | `var(--rec)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0b0b0a` | Typography Ink Token |
| `--paper` | `#f2ede4` | Canvas / Surface Token |
| `--muted` | `#a39e94` | Color / Atmospheric Token |
| `--gold` | `#c9a96e` | Color / Atmospheric Token |
| `--gold-dim` | `#8c7650` | Color / Atmospheric Token |
| `--rec` | `#e0402f` | Color / Atmospheric Token |
| `--serif` | `"Cormorant Garamond", "Baskerville", Georgia, serif` | Typography / Scale Token |
| `--sans` | `"Inter", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--mono` | `"Courier Prime", "Courier New", monospace` | Typography / Scale Token |
| `--yuyafilmstudio-d-bg` | `#0b0b0a` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--yuyafilmstudio-d-ink` | `#f2ede4` | Primary Typography Ink (computed-derived) |
| `--yuyafilmstudio-d-surface` | `#0f0e0c` | Surface Substrate (computed-derived) |
| `--yuyafilmstudio-d-accent` | `#dddddd` | Interactive Accent (computed-derived) |
| `--yuyafilmstudio-d-muted` | `#a39e94` | Secondary Ink (computed-derived) |
| `--yuyafilmstudio-d-border` | `#5c5a56` | Structural Border (computed-derived) |
| `--yuyafilmstudio-d-container` | `1400px` | Container Bound (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `Courier Prime`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44px`, `line-height: 46.64px`, `font-weight: 500`, `letter-spacing: 5.28px`); rule `h1` (`font-size: clamp(30px,3.5vw,44px)`, `line-height: 1.06`, `letter-spacing: .12em`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 9.5px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: 3.04px`); rule `h2` (`font-size: 9.5px`, `letter-spacing: .32em`, `font-weight: 500`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 21px`, `line-height: 1.38`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 11.5px`, `line-height: normal`, `font-weight: 600`, `letter-spacing: 3.91px`); CSS variables `--mono: "Courier Prime", "Courier New", monospace`; rule `small` (`font-size: 11px`, `letter-spacing: .01em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn-enter`**: `transition: background .3s,color .3s,opacity .3s` extracted from `yuyafilmstudio-dev` stylesheet.
- **Selector `#loader`**: `transition: background 1.6s ease` extracted from `yuyafilmstudio-dev` stylesheet.
- **Selector `.bf-dot`**: `transition: background .6s` extracted from `yuyafilmstudio-dev` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.bf-top>` and `<section.bf-controls>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — YUYA FILM STUDIO                           │
│ ====================================================================== │
│ [ <header.bf-top> (1120x47px)         | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.bf-id> (w=1440px)                             | │
│ | H1: YUYA FILM STUDIO                                               | │
│ | Substrate: #0b0b0a | Ink: #f2ede4 | Accent: #dddddd                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bf-controls>) max-w: 1400px                | │
│ | +------------------------------+  +------------------------------+ | │
│ | | MOVE                         |  | EXPLORE                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.bf-map>) — OBJECTS                         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bf-foot>    ) | https://yuyafilmstudio.dev/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.bf-top>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.bf-id>) — 390px Vertical Lead                 | │
│ | H1: YUYA FILM STUDIO                                               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bf-controls>) — 1-Col Stack               | │
│ | [ Item 1: MOVE                                                   ] | │
│ | [ Item 2: EXPLORE                                                ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.bf-map>) — 1-Col (OBJECTS)                  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bf-foot>    ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.bf-top> — `yuyafilmstudio-dev`)**:
   - Landmark `<header class="bf-top">` (`1120x47px`) hosting `YUYA FILM STUDIO` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sdkn="@vercel/analytics"`, `data-sdkv="2.0.1"`, `data-engine="three.js r180"`, `data-k="KeyV"`), and stylesheet rule `gl { position:fixed;inset:0;width:100vw;height:100vh;display:block;outline:none }`.
2. **Hero Stage & Focal Lead (<section.bf-id> — `YUYA FILM STUDIO`)**:
   - Landmark `<section class="bf-id">` presenting display lead `YUYA FILM STUDIO` and copy excerpt *"Explore the studio, interact with the production process, and fol"* over `#0b0b0a` canvas and `#f2ede4` ink.
3. **Primary Showcase & Content Grid (<section.bf-controls> — `MOVE`)**:
   - Landmark `<section class="bf-controls">` rendering section `MOVE` with copy *"VISITOR ACCESS / STUDIO TOUR"*, asset references (`index-BGb4Src9.js`, `index-C-QYK-dA.css`, `script.js`), and grid rule `.hidden { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.bf-map> — `EXPLORE`)**:
   - Landmark `<section class="bf-map">` framing `EXPLORE` and `OBJECTS` (*"ENTER YUYA FILM STUDIO"*) with `#0f0e0c` surface cards, `#dddddd` accents, and `button { font-family:var(--sans);cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.bf-foot> — `https://yuyafilmstudio.dev/`)**:
   - Landmark `<footer class="bf-foot">` anchoring `YUYA FILM STUDIO` footer links (`Overview · Index · Archive · About · Contact`), copy *"Pulling stills from the ÉCLAT edit…"*, and `#5c5a56` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: yuyafilmstudio-dev (YUYA FILM STUDIO)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `yuyafilmstudio-dev` (**YUYA FILM STUDIO** — `https://yuyafilmstudio.dev/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0a` / `#dddddd`).
- **Identity & Domain Context**: Walk through YUYA FILM STUDIO — a working film company built from Yuya's real Video OS, projects and footage.
- **Primary Substrate**: `#0b0b0a` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f2ede4`, **Accent / Highlight**: `#dddddd`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0b0b0a` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f2ede4` primary typography and `#dddddd` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`YUYA FILM STUDIO`) with `Inter` and `Courier Prime`.
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 10px`, padding `2px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `yuyafilmstudio-dev` in your global stylesheet:

:root {
  /* YUYA FILM STUDIO (yuyafilmstudio-dev) — Live-Grounded CSS Variables */
  --ink: #0b0b0a; /* Typography Ink Token (yuyafilmstudio-dev) */
  --paper: #f2ede4; /* Canvas / Surface Token (yuyafilmstudio-dev) */
  --muted: #a39e94; /* Color / Atmospheric Token (yuyafilmstudio-dev) */
  --gold: #c9a96e; /* Color / Atmospheric Token (yuyafilmstudio-dev) */
  --gold-dim: #8c7650; /* Color / Atmospheric Token (yuyafilmstudio-dev) */
  --rec: #e0402f; /* Color / Atmospheric Token (yuyafilmstudio-dev) */
  --serif: "Cormorant Garamond", "Baskerville", Georgia, serif; /* Typography / Scale Token (yuyafilmstudio-dev) */
  --sans: "Inter", "Helvetica Neue", Arial, sans-serif; /* Typography / Scale Token (yuyafilmstudio-dev) */
  --mono: "Courier Prime", "Courier New", monospace; /* Typography / Scale Token (yuyafilmstudio-dev) */
  --yuyafilmstudio-d-bg: #0b0b0a; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (yuyafilmstudio-dev) */
  --yuyafilmstudio-d-ink: #f2ede4; /* Primary Typography Ink (computed-derived) (yuyafilmstudio-dev) */
  --yuyafilmstudio-d-surface: #0f0e0c; /* Surface Substrate (computed-derived) (yuyafilmstudio-dev) */
  --yuyafilmstudio-d-accent: #dddddd; /* Interactive Accent (computed-derived) (yuyafilmstudio-dev) */
  --yuyafilmstudio-d-muted: #a39e94; /* Secondary Ink (computed-derived) (yuyafilmstudio-dev) */
  --yuyafilmstudio-d-border: #5c5a56; /* Structural Border (computed-derived) (yuyafilmstudio-dev) */
  --yuyafilmstudio-d-container: 1400px; /* Container Bound (computed-derived) (yuyafilmstudio-dev) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0b0b0a` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f2ede4` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#0f0e0c` — grounded in `.bf-route li:before { background: #0f0e0c }`
- **Interactive Accent / Highlight**: `#dddddd` — grounded in `.vf-shots button { color: #dddddd }`
- **Secondary / Muted Copy**: `#a39e94` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#5c5a56` — grounded in `kbd { border: #5c5a56 }`
- **Variable Token (`--gold`)**: `#c9a96e` — grounded in `var(--gold)` in `:root`
- **Variable Token (`--gold-dim`)**: `#8c7650` — grounded in `var(--gold-dim)` in `:root`
- **Variable Token (`--rec`)**: `#e0402f` — grounded in `var(--rec)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1400px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `2px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding
- **Media Queries**: `@media (max-width:1000px)`, `@media (max-width:640px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:720px)`
- **Corner Radii**: `3px`, `50%`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `Courier Prime`
- **H1 Display Rule**: live computed `h1` (`font-size: 44px`, `line-height: 46.64px`, `font-weight: 500`, `letter-spacing: 5.28px`); rule `h1` (`font-size: clamp(30px,3.5vw,44px)`, `line-height: 1.06`, `letter-spacing: .12em`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 9.5px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: 3.04px`); rule `h2` (`font-size: 9.5px`, `letter-spacing: .32em`, `font-weight: 500`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 21px`, `line-height: 1.38`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 11.5px`, `line-height: normal`, `font-weight: 600`, `letter-spacing: 3.91px`); CSS variables `--mono: "Courier Prime", "Courier New", monospace`; rule `small` (`font-size: 11px`, `letter-spacing: .01em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `yuyafilmstudio-dev` (`YUYA FILM STUDIO`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.bf-top> — `yuyafilmstudio-dev`)**:
   - DOM & Selectors: Landmark `<header class="bf-top">` (`1120x47px`) hosting `YUYA FILM STUDIO` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sdkn="@vercel/analytics"`, `data-sdkv="2.0.1"`, `data-engine="three.js r180"`, `data-k="KeyV"`), and stylesheet rule `gl { position:fixed;inset:0;width:100vw;height:100vh;display:block;outline:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.bf-top> — `yuyafilmstudio-dev`)` (`yuyafilmstudio-dev`) adapts across `@media (max-width:1000px)`, `@media (max-width:640px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:720px)` with `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.bf-id> — `YUYA FILM STUDIO`)**:
   - DOM & Selectors: Landmark `<section class="bf-id">` presenting display lead `YUYA FILM STUDIO` and copy excerpt *"Explore the studio, interact with the production process, and fol"* over `#0b0b0a` canvas and `#f2ede4` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#0b0b0a` background with `#f2ede4` headline `YUYA FILM STUDIO`.
3. **Primary Showcase & Content Grid (<section.bf-controls> — `MOVE`)**:
   - DOM & Selectors: Landmark `<section class="bf-controls">` rendering section `MOVE` with copy *"VISITOR ACCESS / STUDIO TOUR"*, asset references (`index-BGb4Src9.js`, `index-C-QYK-dA.css`, `script.js`), and grid rule `.hidden { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bf-controls> — `MOVE`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `2px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.bf-map> — `EXPLORE`)**:
   - DOM & Selectors: Landmark `<section class="bf-map">` framing `EXPLORE` and `OBJECTS` (*"ENTER YUYA FILM STUDIO"*) with `#0f0e0c` surface cards, `#dddddd` accents, and `button { font-family:var(--sans);cursor:pointer }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.bf-map> — `EXPLORE`)` uses `3px`, `50%`, `4px` radii, `#dddddd` highlights, and assets (index-BGb4Src9.js, index-C-QYK-dA.css, script.js).
5. **Colophon & Global Directory Footer (<footer.bf-foot> — `https://yuyafilmstudio.dev/`)**:
   - DOM & Selectors: Landmark `<footer class="bf-foot">` anchoring `YUYA FILM STUDIO` footer links (`Overview · Index · Archive · About · Contact`), copy *"Pulling stills from the ÉCLAT edit…"*, and `#5c5a56` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bf-foot> — `https://yuyafilmstudio.dev/`)` aligns to `1400px` (non-`@media` desktop container stylesheet rule) with `2px` lateral canvas padding with `10px` grid gap and attributes (data-sdkn="@vercel/analytics", data-sdkv="2.0.1", data-engine="three.js r180").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Explore the studio, interact with the production process, and follow a film from d..."*
- Copy Excerpt 2: *"VISITOR ACCESS / STUDIO TOUR"*
- Copy Excerpt 3: *"ENTER YUYA FILM STUDIO"*
- Copy Excerpt 4: *"Pulling stills from the ÉCLAT edit…"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`yuyafilmstudio-dev`)**:
- `gl { position:fixed;inset:0;width:100vw;height:100vh;display:block;outline:none }`
- `.hidden { display:none!important }`
- `button { font-family:var(--sans);cursor:pointer }`
- `.btn-enter:disabled { opacity:.25;cursor:default }`
- `hover { background:var(--gold);color:var(--ink) }`
- **Per-Selector Transition Rules**:
- **Selector `.btn-enter`**: `transition: background .3s,color .3s,opacity .3s` extracted from `yuyafilmstudio-dev` stylesheet.
- **Selector `#loader`**: `transition: background 1.6s ease` extracted from `yuyafilmstudio-dev` stylesheet.
- **Selector `.bf-dot`**: `transition: background .6s` extracted from `yuyafilmstudio-dev` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.bf-top>` and `<section.bf-controls>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `yuyafilmstudio-dev`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
