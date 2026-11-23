---
title: "UI Prompt Blueprint: almirakho-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "almirakho-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#fafafa` canvas, `#0a0a0a` ink, `#2ec97a` accent)"
---

# UI Design System & Master Generation Blueprint: almirakho-com

> **Almira Kho - Photographer and Director** (https://almirakho.com/) — Almira Kho is a photographer and director based in Paris/London. Specialized in music industry and fashion. Film and digital.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Almira Kho - Photographer and Director** (`https://almirakho.com/`). Almira Kho is a photographer and director based in Paris/London. Specialized in music industry and fashion. Film and digital.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fafafa` canvas, `#0a0a0a` ink, `#2ec97a` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fafafa` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0a0a0a` primary typography and `#2ec97a` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Archivo` for display copy (`ALMIRA KHO`) with `Archivo` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 20px`, padding `20px`) with `cubic-bezier(.455,.03,.515,.955)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `var(--vp-radius)`, `var(--vp-button-radius)`, `var(--vp-radius-xs)`, `var(--vp-timeline-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (width<=900px)`, `@media screen and (width<=420px)`, `@media screen and (hover:hover) and (pointer:fine)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fafafa` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a0a0a` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `body::-moz-selection { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#2ec97a` | `var(--vp-primary-hover)` in `:root` |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |
| **Variable Token (`--color-red`)** | `#e45050` | `var(--color-red)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vw` | `100vw` | Layout / Spatial Grid Token |
| `--vh` | `100vh` | Layout / Spatial Grid Token |
| `--ivh` | `100dvh` | Layout / Spatial Grid Token |
| `--rem` | `1px` | Dimension / Scale Token |
| `--main-font-name` | `"Archivo"` | Typography / Scale Token |
| `--display-font-name` | `"Archivo"` | Typography / Scale Token |
| `--main-font` | `var(--main-font-name), "Helvetica Neue", "Arial", sans-serif` | Typography / Scale Token |
| `--display-font` | `var(--display-font-name), "Helvetica Neue", "Arial", sans-serif` | Typography / Scale Token |
| `--color-black` | `#0a0a0a` | Canvas / Surface Token |
| `--color-white` | `#fafafa` | Canvas / Surface Token |
| `--color-white-50` | `#ffffff80` | Canvas / Surface Token |
| `--color-white-5` | `#ffffff0d` | Canvas / Surface Token |
| `--color-red` | `#e45050` | Brand / Palette Token |
| `--grid-margin` | `20rem` | Layout / Spatial Grid Token |
| `--grid-gutter` | `20rem` | Layout / Spatial Grid Token |
| `--grid-column` | `calc(var(--vw)/10 - var(--grid-gutter)*9/10 - var(--grid-margin)*2/10)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Archivo`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 13px`, `line-height: 13px`, `font-weight: 500`); CSS variables `--display-font-name: "Archivo"`, `--display-font: var(--display-font-name), "Helvetica Neue", "Arial", sans-serif`.
- **Section Heading (`H2`)**: observed font-size ladder: `13px`, `16px`, `40px`, `16rem`, `var(--rem)`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 500`); rule `,p` (`font-size: inherit`, `letter-spacing: inherit`, `font-weight: inherit`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 13px`, `line-height: 13px`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.455,.03,.515,.955)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.fade-leave-active`**: `transition: opacity .35s` extracted from `almirakho-com` stylesheet.
- **Selector `.project-enter-active`**: `transition: opacity .65s .2s,transform .65s cubic-bezier(.455,.03,.515,.955) .2s` extracted from `almirakho-com` stylesheet.
- **Selector `.project-leave-active`**: `transition: opacity .45s,transform .45s` extracted from `almirakho-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.455,.03,.515,.955)`)**: Governs interactive state transitions across `<header.header>` and `<main.home-link>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Almira Kho - Photographer and Director     │
│ ====================================================================== │
│ [ <header.header> (1440x76px)         | Almira Kho · About · IG      ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.header> (w=1440px)                               | │
│ | H1: ALMIRA KHO                                                     | │
│ | Substrate: #fafafa | Ink: #0a0a0a | Accent: #2ec97a                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.home-link>) max-w: 1440px                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Almira Kho                   |  | almirakho-com Interactive Ma | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.router-link-active>) — almirakho-com Archive  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.router-link-) | https://almirakho.com/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.header>) — 390px Vertical Lead                   | │
│ | H1: ALMIRA KHO                                                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.home-link>) — 1-Col Stack                    | │
│ | [ Item 1: Almira Kho                                             ] | │
│ | [ Item 2: almirakho-com Interactive Matrix                       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.router-link-active) — 1-Col (almirakho-com Arch) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.router-link-) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `almirakho-com`)**:
   - Landmark `<header class="header">` (`1440x76px`) hosting `Almira Kho - Photographer and Direct` navigation (`Almira Kho · About · IG`), DOM attributes (`data-scroll="top"`, `data-v-app`, `data-v-edc13355`, `data-v-83432065`), and stylesheet rule `html { font-family:var(--main-font);letter-spacing:0;text-transform:uppercase;f... }`.
2. **Hero Stage & Focal Lead (<main.header> — `ALMIRA KHO`)**:
   - Landmark `<main class="header">` presenting display lead `ALMIRA KHO` and copy excerpt *"Photographer and director based in Paris/London. Specialized in m"* over `#fafafa` canvas and `#0a0a0a` ink.
3. **Primary Showcase & Content Grid (<main.home-link> — `Almira Kho`)**:
   - Landmark `<main class="home-link">` rendering section `Almira Kho` with copy *"ALMIRA KHO"*, asset references (`entry.BkXJSryM.css`, `Cg0QnzOv.js`, `B_9E_aBj.js`, `HclGiUj8.js`), and grid rule `body::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`.
4. **Interactive Detail & Feature Matrix (<main.router-link-active> — `almirakho-com Interactive Matrix`)**:
   - Landmark `<main class="router-link-active">` framing `almirakho-com Interactive Matrix` and `almirakho-com Archive & Directory` (*"Almira Kho"*) with `#ffffff` surface cards, `#2ec97a` accents, and `html::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`.
5. **Colophon & Global Directory Footer (<footer.router-link-exact-active> — `https://almirakho.com/`)**:
   - Landmark `<footer class="router-link-exact-active">` anchoring `Almira Kho - Photographer and Di` footer links (`Almira Kho · About · IG`), copy *"almirakho-com Interactive Matrix"*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: almirakho-com (Almira Kho - Photographer and Director)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `almirakho-com` (**Almira Kho - Photographer and Director** — `https://almirakho.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fafafa` canvas, `#0a0a0a` ink, `#2ec97a` accent).
- **Identity & Domain Context**: Almira Kho is a photographer and director based in Paris/London. Specialized in music industry and fashion. Film and digital.
- **Primary Substrate**: `#fafafa` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0a0a0a`, **Accent / Highlight**: `#2ec97a`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fafafa` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0a0a0a` primary typography and `#2ec97a` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Archivo` for display copy (`ALMIRA KHO`) with `Archivo` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 20px`, padding `20px`) with `cubic-bezier(.455,.03,.515,.955)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `almirakho-com` in your global stylesheet:

:root {
  /* Almira Kho - Photographer and Director (almirakho-com) — Live-Grounded CSS Variables */
  --vw: 100vw; /* Layout / Spatial Grid Token (almirakho-com) */
  --vh: 100vh; /* Layout / Spatial Grid Token (almirakho-com) */
  --ivh: 100dvh; /* Layout / Spatial Grid Token (almirakho-com) */
  --rem: 1px; /* Dimension / Scale Token (almirakho-com) */
  --main-font-name: "Archivo"; /* Typography / Scale Token (almirakho-com) */
  --display-font-name: "Archivo"; /* Typography / Scale Token (almirakho-com) */
  --main-font: var(--main-font-name), "Helvetica Neue", "Arial", sans-serif; /* Typography / Scale Token (almirakho-com) */
  --display-font: var(--display-font-name), "Helvetica Neue", "Arial", sans-serif; /* Typography / Scale Token (almirakho-com) */
  --color-black: #0a0a0a; /* Canvas / Surface Token (almirakho-com) */
  --color-white: #fafafa; /* Canvas / Surface Token (almirakho-com) */
  --color-white-50: #ffffff80; /* Canvas / Surface Token (almirakho-com) */
  --color-white-5: #ffffff0d; /* Canvas / Surface Token (almirakho-com) */
  --color-red: #e45050; /* Brand / Palette Token (almirakho-com) */
  --grid-margin: 20rem; /* Layout / Spatial Grid Token (almirakho-com) */
  --grid-gutter: 20rem; /* Layout / Spatial Grid Token (almirakho-com) */
  --grid-column: calc(var(--vw)/10 - var(--grid-gutter)*9/10 - var(--grid-margin)*2/10); /* Layout / Spatial Grid Token (almirakho-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fafafa` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0a0a0a` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `body::-moz-selection { background-color: white }` (`#ffffff`)
- **Interactive Accent / Highlight**: `#2ec97a` — grounded in `var(--vp-primary-hover)` in `:root`
- **Secondary / Muted Copy**: `#ffffff` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#ffffff` — grounded in hairline divider derived from live computed `p` `color` (`computed_styles.json`)
- **Variable Token (`--color-red`)**: `#e45050` — grounded in `var(--color-red)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `20px` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media screen and (width<=900px)`, `@media screen and (width<=420px)`, `@media screen and (hover:hover) and (pointer:fine)`
- **Corner Radii**: `var(--vp-radius)`, `var(--vp-button-radius)`, `var(--vp-radius-xs)`, `var(--vp-timeline-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 13px`, `line-height: 13px`, `font-weight: 500`); CSS variables `--display-font-name: "Archivo"`, `--display-font: var(--display-font-name), "Helvetica Neue", "Arial", sans-serif`
- **H2 Section Rule**: observed font-size ladder: `13px`, `16px`, `40px`, `16rem`, `var(--rem)`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 500`); rule `,p` (`font-size: inherit`, `letter-spacing: inherit`, `font-weight: inherit`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 13px`, `line-height: 13px`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `almirakho-com` (`Almira Kho - Photographer and Director`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `almirakho-com`)**:
   - DOM & Selectors: Landmark `<header class="header">` (`1440x76px`) hosting `Almira Kho - Photographer and Direct` navigation (`Almira Kho · About · IG`), DOM attributes (`data-scroll="top"`, `data-v-app`, `data-v-edc13355`, `data-v-83432065`), and stylesheet rule `html { font-family:var(--main-font);letter-spacing:0;text-transform:uppercase;f... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `almirakho-com`)` (`almirakho-com`) adapts across `@media screen and (width<=900px)`, `@media screen and (width<=420px)`, `@media screen and (hover:hover) and (pointer:fine)` with `cubic-bezier(.455,.03,.515,.955)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Almira Kho · About · IG`.
2. **Hero Stage & Focal Lead (<main.header> — `ALMIRA KHO`)**:
   - DOM & Selectors: Landmark `<main class="header">` presenting display lead `ALMIRA KHO` and copy excerpt *"Photographer and director based in Paris/London. Specialized in m"* over `#fafafa` canvas and `#0a0a0a` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×2400px` mobile) sets `#fafafa` background with `#0a0a0a` headline `ALMIRA KHO`.
3. **Primary Showcase & Content Grid (<main.home-link> — `Almira Kho`)**:
   - DOM & Selectors: Landmark `<main class="home-link">` rendering section `Almira Kho` with copy *"ALMIRA KHO"*, asset references (`entry.BkXJSryM.css`, `Cg0QnzOv.js`, `B_9E_aBj.js`, `HclGiUj8.js`), and grid rule `body::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.home-link> — `Almira Kho`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.router-link-active> — `almirakho-com Interactive Matrix`)**:
   - DOM & Selectors: Landmark `<main class="router-link-active">` framing `almirakho-com Interactive Matrix` and `almirakho-com Archive & Directory` (*"Almira Kho"*) with `#ffffff` surface cards, `#2ec97a` accents, and `html::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.router-link-active> — `almirakho-com Interactive Matrix`)` uses `var(--vp-radius)`, `var(--vp-button-radius)`, `var(--vp-radius-xs)`, `var(--vp-timeline-radius)` radii, `#2ec97a` highlights, and assets (entry.BkXJSryM.css, Cg0QnzOv.js, B_9E_aBj.js).
5. **Colophon & Global Directory Footer (<footer.router-link-exact-active> — `https://almirakho.com/`)**:
   - DOM & Selectors: Landmark `<footer class="router-link-exact-active">` anchoring `Almira Kho - Photographer and Di` footer links (`Almira Kho · About · IG`), copy *"almirakho-com Interactive Matrix"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.router-link-exact-active> — `https://almirakho.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `20px` lateral canvas padding with `20px` grid gap and attributes (data-scroll="top", data-v-app, data-v-edc13355).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Photographer and director based in Paris/London. Specialized in music industry and..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.455,.03,.515,.955)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`almirakho-com`)**:
- `html { font-family:var(--main-font);letter-spacing:0;text-transform:uppercase;f... }`
- `body::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`
- `html::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`
- `body::selection { background-color:var(--color-white);color:var(--color-black) }`
- `html::selection { background-color:var(--color-white);color:var(--color-black) }`
- **Per-Selector Transition Rules**:
- **Selector `.fade-leave-active`**: `transition: opacity .35s` extracted from `almirakho-com` stylesheet.
- **Selector `.project-enter-active`**: `transition: opacity .65s .2s,transform .65s cubic-bezier(.455,.03,.515,.955) .2s` extracted from `almirakho-com` stylesheet.
- **Selector `.project-leave-active`**: `transition: opacity .45s,transform .45s` extracted from `almirakho-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.455,.03,.515,.955)`)**: Governs interactive state transitions across `<header.header>` and `<main.home-link>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `almirakho-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
