---
title: "UI Prompt Blueprint: zarcerog-com"
date: 2026-11-15
target: "[[overview|zarcerog-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#e8b3a9` canvas, `#241417` ink, `#f4e6cb` accent)"
---

# UI Design System & Master Generation Blueprint: zarcerog-com

> **Nicolás Zarcero — Box Office** (https://zarcerog.com) — Two shows tonight: a portfolio in five acts, with an intermission; and a picture about a church that is running late. Nicolás Zarcero, en...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/zarcerog-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Nicolás Zarcero — Box Office** (`https://zarcerog.com`). Two shows tonight: a portfolio in five acts, with an intermission; and a picture about a church that is running late. Nicolás Zarcero, en...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#e8b3a9` canvas, `#241417` ink, `#f4e6cb` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e8b3a9` (`var(--pink)` in `:root`) paired with `#241417` primary typography and `#f4e6cb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jost` for display copy (`Nicolás Zarcero : box office. Two sh`) with `Jost Fallback` and `Courier Prime`.
  - **Calibrated Spatial Grid & Motion**: Combines `14ch` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.2,.7,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/zarcerog-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `14ch` extracted from `zarcerog-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 14ch`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-aspect-ratio:1)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e8b3a9` | `var(--pink)` in `:root` |
| **Primary Typography Ink** | `#86192a` | `var(--burgundy)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c9a24a` | `var(--gold)` in `:root` |
| **Interactive Accent / Highlight** | `#f4e6cb` | `var(--cream)` in `:root` |
| **Secondary / Muted Copy** | `#f2c230` | `var(--yellow)` in `:root` |
| **Structural Hairline Border** | `#241417` | `var(--ink)` in `:root` |
| **Variable Token (`--red`)** | `#d8262e` | `var(--red)` in `:root` |
| **Variable Token (`--sub`)** | `#f7d23e` | `var(--sub)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bx-sans` | `var(--f-sans,Jost), Jost, Futura, "Helvetica Neue", sans-serif` | Typography / Scale Token |
| `--bx-type` | `var(--f-type,"Courier Prime"), "Courier Prime", "Courier New", monospace` | Typography / Scale Token |
| `--bx-marquee` | `var(--f-marquee,Limelight), Limelight, var(--f-serif,"Bodoni Moda"), serif` | Design System Custom Token |
| `--bx-anton` | `var(--f-anton,Anton), Anton, Impact, "Arial Narrow", sans-serif` | Design System Custom Token |
| `--pink` | `#e8b3a9` | Typography Ink Token |
| `--burgundy` | `#86192a` | Color / Atmospheric Token |
| `--gold` | `#c9a24a` | Color / Atmospheric Token |
| `--cream` | `#f4e6cb` | Color / Atmospheric Token |
| `--yellow` | `#f2c230` | Color / Atmospheric Token |
| `--ink` | `#241417` | Typography Ink Token |
| `--red` | `#d8262e` | Color / Atmospheric Token |
| `--sub` | `#f7d23e` | Color / Atmospheric Token |
| `--px` | `0` | Design System Custom Token |
| `--py` | `0` | Design System Custom Token |
| `--tx` | `0` | Design System Custom Token |
| `--ty` | `0` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Jost`.
- **Primary Body Stack**: `Jost Fallback`.
- **Technical / Metadata Stack**: `Courier Prime`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.5,0,.3,1)`, `cubic-bezier(.4,0,.8,.4)`.

### Per-Element Transition & Choreography Rules
- **Selector `.bx-layer`**: `transition: transform .9s cubic-bezier(.2,.7,.2,1)` extracted from `zarcerog-com` stylesheet.
- **Selector `.bx-pupils`**: `transition: transform .25s ease-out` extracted from `zarcerog-com` stylesheet.
- **Selector `.bx-clerk`**: `transition: transform .6s` extracted from `zarcerog-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<nav.bx-layer>` and `<main.bx-root>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<main.bx-root>` and `<main.bx-root>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Nicolás Zarcero — Box Office               │
│ ====================================================================== │
│ [ <nav.bx-layer>           | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.bx-root>                                       |   │
│ | H1: Nicolás Zarcero : box office. Two shows tonight —...         |   │
│ | Substrate: #e8b3a9    | Ink: #241417    | Accent: #f4e6cb        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.bx-root>            ) max-w: 14ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The Zarcero Theatre presents |  | The Zarcero Theatre          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<nav.bx-layer>] -> [<main.bx-root>] -> [<main.bx-root>] |           │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bx-foot>      ) | https://zarcerog.com               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.bx-layer> — `zarcerog-com`)**:
   - Landmark `<nav class="bx-layer bx-layer--tickets">` hosting `Nicolás Zarcero — Box Office` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="1.6.1"`), and stylesheet rule `body { background:e8b3a9;margin:0 }`.
2. **Hero Stage & Focal Lead (<main.bx-root> — `Nicolás Zarcero : box office. Two `)**:
   - Landmark `<main class="bx-root">` presenting display lead `Nicolás Zarcero : box office. Two shows tonight —...` and copy excerpt *"The Zarcero Theatre presents A Portfolio in Five Acts with an int"* over `#e8b3a9` canvas and `#241417` ink.
3. **Primary Showcase & Content Grid (<main.bx-root> — `The Zarcero Theatre presents A Por`)**:
   - Landmark `<main class="bx-root">` rendering section `The Zarcero Theatre presents A Portfolio in Five` with copy *"The Zarcero Theatre"*, asset references (`52b5d5098cb87ddd-s.p.3r2y_bth_sjs...`, `5f440d3eea613716-s.p.1xmps1tcyqv3...`, `612bd71aa396cae6-s.p.0y-3ea_6ee5g...`, `81cef6a21128489e-s.p.2csanl8cs02r...`), and grid rule `.bx-sr { clip-path:inset(50%);white-space:nowrap;width:1px;height:1px;position:ab... }`.
4. **Interactive Detail & Feature Matrix (<main.bx-root> — `The Zarcero Theatre`)**:
   - Landmark `<main class="bx-root">` framing `The Zarcero Theatre` and `A Portfolio in Five Acts` (*"A Portfolio in Five Acts"*) with `#c9a24a` surface cards, `#f4e6cb` accents, and `.bx-layer { transition:transform .9s cubic-bezier(.2,.7,.2,1);position:absolute;inset:0 }`.
5. **Colophon & Global Directory Footer (<footer.bx-foot> — `https://zarcerog.com`)**:
   - Landmark `<footer class="bx-foot">` anchoring `Nicolás Zarcero — Box Office` footer links (`Overview · Index · Archive · About · Contact`), copy *"with an intermission · starring Nicolás Zarcero"*, and `#241417` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: zarcerog-com (Nicolás Zarcero — Box Office)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `zarcerog-com` (**Nicolás Zarcero — Box Office** — `https://zarcerog.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#e8b3a9` canvas, `#241417` ink, `#f4e6cb` accent).
- **Identity & Domain Context**: Two shows tonight: a portfolio in five acts, with an intermission; and a picture about a church that is running late. Nicolás Zarcero, en...
- **Primary Substrate**: `#e8b3a9` (`var(--pink)` in `:root`), **Primary Ink**: `#241417`, **Accent / Highlight**: `#f4e6cb`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e8b3a9` (`var(--pink)` in `:root`) paired with `#241417` primary typography and `#f4e6cb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jost` for display copy (`Nicolás Zarcero : box office. Two sh`) with `Jost Fallback` and `Courier Prime`.
  - **Calibrated Spatial Grid & Motion**: Combines `14ch` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.2,.7,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `zarcerog-com` in your global stylesheet:

:root {
  /* Nicolás Zarcero — Box Office (zarcerog-com) — Ground-Truth Extracted CSS Variables */
  --bx-sans: var(--f-sans,Jost), Jost, Futura, "Helvetica Neue", sans-serif; /* Typography / Scale Token (zarcerog-com) */
  --bx-type: var(--f-type,"Courier Prime"), "Courier Prime", "Courier New", monospace; /* Typography / Scale Token (zarcerog-com) */
  --bx-marquee: var(--f-marquee,Limelight), Limelight, var(--f-serif,"Bodoni Moda"), serif; /* Design System Custom Token (zarcerog-com) */
  --bx-anton: var(--f-anton,Anton), Anton, Impact, "Arial Narrow", sans-serif; /* Design System Custom Token (zarcerog-com) */
  --pink: #e8b3a9; /* Typography Ink Token (zarcerog-com) */
  --burgundy: #86192a; /* Color / Atmospheric Token (zarcerog-com) */
  --gold: #c9a24a; /* Color / Atmospheric Token (zarcerog-com) */
  --cream: #f4e6cb; /* Color / Atmospheric Token (zarcerog-com) */
  --yellow: #f2c230; /* Color / Atmospheric Token (zarcerog-com) */
  --ink: #241417; /* Typography Ink Token (zarcerog-com) */
  --red: #d8262e; /* Color / Atmospheric Token (zarcerog-com) */
  --sub: #f7d23e; /* Color / Atmospheric Token (zarcerog-com) */
  --px: 0; /* Design System Custom Token (zarcerog-com) */
  --py: 0; /* Design System Custom Token (zarcerog-com) */
  --tx: 0; /* Design System Custom Token (zarcerog-com) */
  --ty: 0; /* Design System Custom Token (zarcerog-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e8b3a9` — grounded in `var(--pink)` in `:root`
- **Primary Typography Ink**: `#86192a` — grounded in `var(--burgundy)` in `:root`
- **Elevated Surface / Card Substrate**: `#c9a24a` — grounded in `var(--gold)` in `:root`
- **Interactive Accent / Highlight**: `#f4e6cb` — grounded in `var(--cream)` in `:root`
- **Secondary / Muted Copy**: `#f2c230` — grounded in `var(--yellow)` in `:root`
- **Structural Hairline Border**: `#241417` — grounded in `var(--ink)` in `:root`
- **Variable Token (`--red`)**: `#d8262e` — grounded in `var(--red)` in `:root`
- **Variable Token (`--sub`)**: `#f7d23e` — grounded in `var(--sub)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `14ch` extracted from `zarcerog-com` stylesheet
- **Padding & Gutters**: `0px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 14ch`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media (max-aspect-ratio:1)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Jost Fallback`
- **Monospace / Technical Font Stack**: `Courier Prime`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `zarcerog-com` (`Nicolás Zarcero — Box Office`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.bx-layer> — `zarcerog-com`)**:
   - DOM & Selectors: Landmark `<nav class="bx-layer bx-layer--tickets">` hosting `Nicolás Zarcero — Box Office` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="1.6.1"`), and stylesheet rule `body { background:e8b3a9;margin:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.bx-layer> — `zarcerog-com`)` (`zarcerog-com`) adapts across `@media (max-aspect-ratio:1)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.5,0,.3,1)`, `cubic-bezier(.4,0,.8,.4)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.bx-root> — `Nicolás Zarcero : box office. Two `)**:
   - DOM & Selectors: Landmark `<main class="bx-root">` presenting display lead `Nicolás Zarcero : box office. Two shows tonight —...` and copy excerpt *"The Zarcero Theatre presents A Portfolio in Five Acts with an int"* over `#e8b3a9` canvas and `#241417` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#e8b3a9` background with `#241417` headline `Nicolás Zarcero : box office. Two shows tonight —...`.
3. **Primary Showcase & Content Grid (<main.bx-root> — `The Zarcero Theatre presents A Por`)**:
   - DOM & Selectors: Landmark `<main class="bx-root">` rendering section `The Zarcero Theatre presents A Portfolio in Five` with copy *"The Zarcero Theatre"*, asset references (`52b5d5098cb87ddd-s.p.3r2y_bth_sjs...`, `5f440d3eea613716-s.p.1xmps1tcyqv3...`, `612bd71aa396cae6-s.p.0y-3ea_6ee5g...`, `81cef6a21128489e-s.p.2csanl8cs02r...`), and grid rule `.bx-sr { clip-path:inset(50%);white-space:nowrap;width:1px;height:1px;position:ab... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.bx-root> — `The Zarcero Theatre presents A Por`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 14ch`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.bx-root> — `The Zarcero Theatre`)**:
   - DOM & Selectors: Landmark `<main class="bx-root">` framing `The Zarcero Theatre` and `A Portfolio in Five Acts` (*"A Portfolio in Five Acts"*) with `#c9a24a` surface cards, `#f4e6cb` accents, and `.bx-layer { transition:transform .9s cubic-bezier(.2,.7,.2,1);position:absolute;inset:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.bx-root> — `The Zarcero Theatre`)` uses `50%` radii, `#f4e6cb` highlights, and assets (52b5d5098cb87ddd-s.p.3r2y_bth_sjs..., 5f440d3eea613716-s.p.1xmps1tcyqv3..., 612bd71aa396cae6-s.p.0y-3ea_6ee5g...).
5. **Colophon & Global Directory Footer (<footer.bx-foot> — `https://zarcerog.com`)**:
   - DOM & Selectors: Landmark `<footer class="bx-foot">` anchoring `Nicolás Zarcero — Box Office` footer links (`Overview · Index · Archive · About · Contact`), copy *"with an intermission · starring Nicolás Zarcero"*, and `#241417` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bx-foot> — `https://zarcerog.com`)` aligns to `14ch` extracted from `zarcerog-com` stylesheet with `0px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-precedence="next", data-precedence="next", data-sdkn="@vercel/analytics/next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The Zarcero Theatre presents A Portfolio in Five Acts with an intermission · starr..."*
- Copy Excerpt 2: *"The Zarcero Theatre"*
- Copy Excerpt 3: *"A Portfolio in Five Acts"*
- Copy Excerpt 4: *"with an intermission · starring Nicolás Zarcero"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.5,0,.3,1)`, `cubic-bezier(.4,0,.8,.4)`
- **Extracted Stylesheet Rules (`zarcerog-com`)**:
- `body { background:e8b3a9;margin:0 }`
- `.bx-sr { clip-path:inset(50%);white-space:nowrap;width:1px;height:1px;position:ab... }`
- `.bx-layer { transition:transform .9s cubic-bezier(.2,.7,.2,1);position:absolute;inset:0 }`
- `.bx-layer--wall { transform:translate(calc(var(--px) * -0.35%), calc(var(--py) * -0.25%)) }`
- `.bx-layer--kiosk { transform:translate(calc(var(--px) * -0.8%), calc(var(--py) * -0.5%)) }`
- **Per-Selector Transition Rules**:
- **Selector `.bx-layer`**: `transition: transform .9s cubic-bezier(.2,.7,.2,1)` extracted from `zarcerog-com` stylesheet.
- **Selector `.bx-pupils`**: `transition: transform .25s ease-out` extracted from `zarcerog-com` stylesheet.
- **Selector `.bx-clerk`**: `transition: transform .6s` extracted from `zarcerog-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<nav.bx-layer>` and `<main.bx-root>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<main.bx-root>` and `<main.bx-root>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `zarcerog-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
