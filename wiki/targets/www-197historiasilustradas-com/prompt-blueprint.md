---
title: "UI Prompt Blueprint: www-197historiasilustradas-com"
date: 2026-11-15
target: "www-197historiasilustradas-com"
status: analyzed
capture: specimen
archetype: "Light-Substrate Editorial & Modular Grid System (`#d4d4d4` canvas, `#000` ink, `#fff` accent)"
---

# UI Design System & Master Generation Blueprint: www-197historiasilustradas-com

> **197 Historias Ilustradas** (https://www.197historiasilustradas.com/) — 197 historias ilustradas es un proyecto que busca dar a conocer la vida de cada una de las personas detenidas desaparecidas nacidas en Ur...

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **197 Historias Ilustradas** (`https://www.197historiasilustradas.com/`). 197 historias ilustradas es un proyecto que busca dar a conocer la vida de cada una de las personas detenidas desaparecidas nacidas en Ur...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#d4d4d4` canvas, `#000` ink, `#fff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#d4d4d4` (`var(--color-neutral-300)` in `:root`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `font` for display copy (`197 Historias Ilustradas`) with `font Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: 8.5px`, padding `0px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1920px` extracted from `www-197historiasilustradas-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `8.5px` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 8.5px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:1920px)`, `@media screen and (max-width:1440px)`, `@media screen and (max-width:479px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d4d4d4` | `var(--color-neutral-300)` in `:root` |
| **Primary Typography Ink** | `#a1a1a1` | `var(--color-neutral-400)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--color-white)` in `:root` |
| **Secondary / Muted Copy** | `#171717` | `var(--foreground)` in `:root` |
| **Structural Hairline Border** | `#737373` | `var(--muted)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-neutral-300` | `#d4d4d4` | Brand / Palette Token |
| `--color-neutral-400` | `#a1a1a1` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-tighter` | `-.05em` | Typography / Scale Token |
| `--tracking-normal` | `0em` | Typography / Scale Token |
| `--leading-relaxed` | `1.625` | Typography / Scale Token |
| `--ease-in` | `cubic-bezier(.4,0,1,1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0,0,.2,1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `font`.
- **Primary Body Stack**: `font Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`).
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-197historiasilustradas-com` stylesheet.
- **Selector `.reveal-lines .line-mask:before`**: `transition: var(--reveal-duration)` extracted from `www-197historiasilustradas-com` stylesheet.
- **Selector `.reveal-lines .line-mask:after`**: `transition: var(--reveal-duration)` extracted from `www-197historiasilustradas-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.px-global>` and `<div.px-global>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — 197 Historias Ilustradas                   │
│ ====================================================================== │
│ [ <header.px-global>       | [ Grilla ] · [ Listado ] · [ Galería ] ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.is-ready>                                       |   │
│ | H1: 197 Historias Ilustradas                                     |   │
│ | Substrate: #d4d4d4    | Ink: #000       | Accent: #fff           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.px-global>           ) max-w: 1920px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | 197 Historias Ilustradas     |  | Historias Ilustradas         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8.5px ) | │
│ | [<header.px-global>] -> [<div.is-ready>] -> [<div.px-global>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.top-0>        ) | https://www.197historiasilustradas │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.px-global> — `www-197historiasilustradas-com`)**:
   - Landmark `<header class="px-global fixed">` hosting `197 Historias Ilustradas` navigation (`[ Grilla ] · [ Listado ] · [ Galería ]`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --color-neutral-300:lab(84.92% 0 -.0000119209);--color-neutral-400:lab(6... }`.
2. **Hero Stage & Focal Lead (<div.is-ready> — `197 Historias Ilustradas`)**:
   - Landmark `<div class="is-ready">` presenting display lead `197 Historias Ilustradas` and copy excerpt *"197 Historias Ilustradas"* over `#d4d4d4` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<div.px-global> — `197 Historias Ilustradas`)**:
   - Landmark `<div class="px-global">` rendering section `197 Historias Ilustradas` with copy *"Historias Ilustradas"*, asset references (`882aee3e7e5fa64f.css`, `3068344f6b59fc28.css`, `a6a883b7ec42f0a6.js`, `1c40893e27076bb9.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.fixed> — `Historias Ilustradas`)**:
   - Landmark `<div class="fixed">` framing `Historias Ilustradas` and `E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 ` (*"E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 8 0 , t a n t o U"*) with `#000` surface cards, `#fff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.top-0> — `https://www.197historiasilustradas.com/`)**:
   - Landmark `<footer class="top-0">` anchoring `197 Historias Ilustradas` footer links (`[ Grilla ] · [ Listado ] · [ Galería ]`), copy *"R e c o r d a r e s v o l v e r a d a r v i d a ; p o r q u "*, and `#737373` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-197historiasilustradas-com (197 Historias Ilustradas)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-197historiasilustradas-com` (**197 Historias Ilustradas** — `https://www.197historiasilustradas.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#d4d4d4` canvas, `#000` ink, `#fff` accent).
- **Identity & Domain Context**: 197 historias ilustradas es un proyecto que busca dar a conocer la vida de cada una de las personas detenidas desaparecidas nacidas en Ur...
- **Primary Substrate**: `#d4d4d4` (`var(--color-neutral-300)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#fff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#d4d4d4` (`var(--color-neutral-300)` in `:root`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `font` for display copy (`197 Historias Ilustradas`) with `font Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: 8.5px`, padding `0px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-197historiasilustradas-com` in your global stylesheet:

:root {
  /* 197 Historias Ilustradas (www-197historiasilustradas-com) — Ground-Truth Extracted CSS Variables */
  --color-neutral-300: #d4d4d4; /* Brand / Palette Token (www-197historiasilustradas-com) */
  --color-neutral-400: #a1a1a1; /* Brand / Palette Token (www-197historiasilustradas-com) */
  --color-black: #000; /* Canvas / Surface Token (www-197historiasilustradas-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-197historiasilustradas-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-197historiasilustradas-com) */
  --font-weight-bold: 700; /* Typography / Scale Token (www-197historiasilustradas-com) */
  --tracking-tighter: -.05em; /* Typography / Scale Token (www-197historiasilustradas-com) */
  --tracking-normal: 0em; /* Typography / Scale Token (www-197historiasilustradas-com) */
  --leading-relaxed: 1.625; /* Typography / Scale Token (www-197historiasilustradas-com) */
  --ease-in: cubic-bezier(.4,0,1,1); /* Motion / Easing Token (www-197historiasilustradas-com) */
  --ease-out: cubic-bezier(0,0,.2,1); /* Motion / Easing Token (www-197historiasilustradas-com) */
  --ease-in-out: cubic-bezier(.4,0,.2,1); /* Motion / Easing Token (www-197historiasilustradas-com) */
  --default-transition-duration: .15s; /* Motion / Easing Token (www-197historiasilustradas-com) */
  --default-transition-timing-function: cubic-bezier(.4,0,.2,1); /* Motion / Easing Token (www-197historiasilustradas-com) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (www-197historiasilustradas-com) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (www-197historiasilustradas-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#d4d4d4` — grounded in `var(--color-neutral-300)` in `:root`
- **Primary Typography Ink**: `#a1a1a1` — grounded in `var(--color-neutral-400)` in `:root`
- **Elevated Surface / Card Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Interactive Accent / Highlight**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Secondary / Muted Copy**: `#171717` — grounded in `var(--foreground)` in `:root`
- **Structural Hairline Border**: `#737373` — grounded in `var(--muted)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1920px` extracted from `www-197historiasilustradas-com` stylesheet
- **Padding & Gutters**: `0px` lateral canvas padding with `8.5px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 8.5px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media screen and (max-width:1920px)`, `@media screen and (max-width:1440px)`, `@media screen and (max-width:479px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `font`
- **Body Font Stack**: `font Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`)
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-197historiasilustradas-com` (`197 Historias Ilustradas`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.px-global> — `www-197historiasilustradas-com`)**:
   - DOM & Selectors: Landmark `<header class="px-global fixed">` hosting `197 Historias Ilustradas` navigation (`[ Grilla ] · [ Listado ] · [ Galería ]`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --color-neutral-300:lab(84.92% 0 -.0000119209);--color-neutral-400:lab(6... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.px-global> — `www-197historiasilustradas-com`)` (`www-197historiasilustradas-com`) adapts across `@media screen and (max-width:1920px)`, `@media screen and (max-width:1440px)`, `@media screen and (max-width:479px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `[ Grilla ] · [ Listado ] · [ Galería ]`.
2. **Hero Stage & Focal Lead (<div.is-ready> — `197 Historias Ilustradas`)**:
   - DOM & Selectors: Landmark `<div class="is-ready">` presenting display lead `197 Historias Ilustradas` and copy excerpt *"197 Historias Ilustradas"* over `#d4d4d4` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#d4d4d4` background with `#000` headline `197 Historias Ilustradas`.
3. **Primary Showcase & Content Grid (<div.px-global> — `197 Historias Ilustradas`)**:
   - DOM & Selectors: Landmark `<div class="px-global">` rendering section `197 Historias Ilustradas` with copy *"Historias Ilustradas"*, asset references (`882aee3e7e5fa64f.css`, `3068344f6b59fc28.css`, `a6a883b7ec42f0a6.js`, `1c40893e27076bb9.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.px-global> — `197 Historias Ilustradas`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 8.5px`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.fixed> — `Historias Ilustradas`)**:
   - DOM & Selectors: Landmark `<div class="fixed">` framing `Historias Ilustradas` and `E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 ` (*"E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 8 0 , t a n t o U"*) with `#000` surface cards, `#fff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.fixed> — `Historias Ilustradas`)` uses `0px` (sharp unrounded corners) radii, `#fff` highlights, and assets (882aee3e7e5fa64f.css, 3068344f6b59fc28.css, a6a883b7ec42f0a6.js).
5. **Colophon & Global Directory Footer (<footer.top-0> — `https://www.197historiasilustradas.com/`)**:
   - DOM & Selectors: Landmark `<footer class="top-0">` anchoring `197 Historias Ilustradas` footer links (`[ Grilla ] · [ Listado ] · [ Galería ]`), copy *"R e c o r d a r e s v o l v e r a d a r v i d a ; p o r q u "*, and `#737373` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.top-0> — `https://www.197historiasilustradas.com/`)` aligns to `1920px` extracted from `www-197historiasilustradas-com` stylesheet with `0px` lateral canvas padding with `8.5px` grid gap and attributes (data-precedence="next", data-precedence="next", data-sdkn="@vercel/analytics/next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"197 Historias Ilustradas"*
- Copy Excerpt 2: *"Historias Ilustradas"*
- Copy Excerpt 3: *"E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 8 0 , t a n t o U r u g u a y c o..."*
- Copy Excerpt 4: *"R e c o r d a r e s v o l v e r a d a r v i d a ; p o r q u e s o l o l o q u e n..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-197historiasilustradas-com`)**:
- `host { --color-neutral-300:lab(84.92% 0 -.0000119209);--color-neutral-400:lab(6... }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-197historiasilustradas-com` stylesheet.
- **Selector `.reveal-lines .line-mask:before`**: `transition: var(--reveal-duration)` extracted from `www-197historiasilustradas-com` stylesheet.
- **Selector `.reveal-lines .line-mask:after`**: `transition: var(--reveal-duration)` extracted from `www-197historiasilustradas-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.px-global>` and `<div.px-global>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-197historiasilustradas-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
