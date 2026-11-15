---
title: "UI Prompt Blueprint: chanpan-com-ar"
date: 2026-11-15
target: "[[overview|chanpan-com-ar]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#C1BBAE` canvas, `#17130D` ink, `#F15A24` accent)"
---

# UI Design System & Master Generation Blueprint: chanpan-com-ar

> **ChanPan · AI Video Production, Commercials & Creative Studio — Argentina** (https://chanpan.com.ar) — AI-driven video production, commercials, branded content, branding and 2D/3D animation. A creative studio from Corrientes, Argentina, wor...

![Desktop Viewport Capture (1440x25422)](file:///root/projects/fleet/wiki/targets/chanpan-com-ar/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ChanPan · AI Video Production, Commercials & Creative Studio — Argentina** (`https://chanpan.com.ar`). AI-driven video production, commercials, branded content, branding and 2D/3D animation. A creative studio from Corrientes, Argentina, wor...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#C1BBAE` canvas, `#17130D` ink, `#F15A24` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#C1BBAE` (`var(--bg)` in `:root`) paired with `#17130D` primary typography and `#F15A24` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`ChanPan — AI video production and cr`) with `Inter` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `24ch` container bounds (`gap: 26px`, padding `4px`) with `cubic-bezier(.7,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/chanpan-com-ar/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×25422px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `24ch` extracted from `chanpan-com-ar` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `26px` grid gap.
- **Border Radius Scale**: `999px`, `50%`, `12px`, `14px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24ch`, `gap: 26px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#C1BBAE` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#17130D` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#524B3D` | `var(--ink-soft)` in `:root` |
| **Interactive Accent / Highlight** | `#F15A24` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#A8360C` | `var(--brand-text)` in `:root` |
| **Structural Hairline Border** | `#EEE9DE` | `var(--paper)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#C1BBAE` | Canvas / Surface Token |
| `--ink` | `#17130D` | Typography Ink Token |
| `--ink-soft` | `#524B3D` | Typography Ink Token |
| `--brand` | `#F15A24` | Brand / Palette Token |
| `--brand-text` | `#A8360C` | Typography Ink Token |
| `--paper` | `#EEE9DE` | Canvas / Surface Token |
| `--line` | `rgba(23,19,13,.16)` | Color / Atmospheric Token |
| `--display` | `'Archivo',sans-serif` | Dimension / Scale Token |
| `--body` | `'Inter',system-ui,sans-serif` | Dimension / Scale Token |
| `--mono` | `'JetBrains Mono',ui-monospace,monospace` | Typography / Scale Token |
| `--mx` | `clamp(22px,5.5vw,88px)` | Dimension / Scale Token |
| `--band-bottom` | `0px` | Dimension / Scale Token |
| `--chanpan-com-ar-bg` | `#C1BBAE` | Canvas Substrate (from `var(--bg)` in `:root`) |
| `--chanpan-com-ar-ink` | `#17130D` | Primary Typography Ink (stylesheet-derived) |
| `--chanpan-com-ar-surface` | `#524B3D` | Surface Substrate (stylesheet-derived) |
| `--chanpan-com-ar-accent` | `#F15A24` | Interactive Accent (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--display: 'Archivo',sans-serif`.
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(26px,3.2vw,42px)`, `font-weight: 800`).
- **Body Copy**: CSS variables `--body: 'Inter',system-ui,sans-serif`; rule `body` (`line-height: 1.6`).
- **Metadata & Navigation Labels**: CSS variables `--mono: 'JetBrains Mono',ui-monospace,monospace`; rule `small` (`font-size: 9.5px`, `letter-spacing: .14em`, `font-weight: 600`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#pre`**: `transition: opacity .8s ease, transform .9s cubic-bezier(.7,0,.2,1)` extracted from `chanpan-com-ar` stylesheet.
- **Selector `.pre-iso--fill`**: `transition: clip-path .35s ease` extracted from `chanpan-com-ar` stylesheet.
- **Selector `#canvas`**: `transition: opacity .8s ease` extracted from `chanpan-com-ar` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,0,.2,1)`)**: Governs interactive state transitions across `<header.hd>` and `<section.drive>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.drive>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ChanPan · AI Video Production, Commercials │
│ ====================================================================== │
│ [ <header.hd>              | Home · Demo Reel · Services · Work · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: ChanPan — AI video production and creative studio            |   │
│ | Substrate: #C1BBAE    | Ink: #17130D    | Accent: #F15A24        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.drive>           ) max-w: 24ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | First, perspective.          |  | Our terrain.                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 26px  ) | │
│ | [<header.hd>] -> [<section.hero>] -> [<section.drive>] |             │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ft>           ) | https://chanpan.com.ar             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hd> — `chanpan-com-ar`)**:
   - Landmark `<header class="hd">` hosting `ChanPan · AI Video Production, Comme` navigation (`Home · Demo Reel · Services · Work · Contact`), DOM attributes (`data-clip="s1-loop"`, `data-clip="s2-scrub"`, `data-scrub`, `data-clip="s3-scrub"`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.hero> — `ChanPan — AI video production and `)**:
   - Landmark `<section class="hero">` presenting display lead `ChanPan — AI video production and creative studio` and copy excerpt *"Message us on WhatsApp"* over `#C1BBAE` canvas and `#17130D` ink.
3. **Primary Showcase & Content Grid (<section.drive> — `First, perspective.`)**:
   - Landmark `<section class="drive">` rendering section `First, perspective.` with copy *"Corrientes, Argentina"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `body.is-loading { overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.drive> — `Our terrain.`)**:
   - Landmark `<section class="drive">` framing `Our terrain.` and `Twenty years climbing.` (*"Production company"*) with `#524B3D` surface cards, `#F15A24` accents, and `button { font:inherit;color:inherit }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://chanpan.com.ar`)**:
   - Landmark `<footer class="ft">` anchoring `ChanPan · AI Video Production, C` footer links (`Home · Demo Reel · Services · Work · Contact`), copy *"AI · Film · Design"*, and `#EEE9DE` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: chanpan-com-ar (ChanPan · AI Video Production, Commercials & Creative Studio — Argentina)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `chanpan-com-ar` (**ChanPan · AI Video Production, Commercials & Creative Studio — Argentina** — `https://chanpan.com.ar`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#C1BBAE` canvas, `#17130D` ink, `#F15A24` accent).
- **Identity & Domain Context**: AI-driven video production, commercials, branded content, branding and 2D/3D animation. A creative studio from Corrientes, Argentina, wor...
- **Primary Substrate**: `#C1BBAE` (`var(--bg)` in `:root`), **Primary Ink**: `#17130D`, **Accent / Highlight**: `#F15A24`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#C1BBAE` (`var(--bg)` in `:root`) paired with `#17130D` primary typography and `#F15A24` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`ChanPan — AI video production and cr`) with `Inter` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `24ch` container bounds (`gap: 26px`, padding `4px`) with `cubic-bezier(.7,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `chanpan-com-ar` in your global stylesheet:

:root {
  /* ChanPan · AI Video Production, Commercials & Creative Studio — Argentina (chanpan-com-ar) — Ground-Truth Extracted CSS Variables */
  --bg: #C1BBAE; /* Canvas / Surface Token (chanpan-com-ar) */
  --ink: #17130D; /* Typography Ink Token (chanpan-com-ar) */
  --ink-soft: #524B3D; /* Typography Ink Token (chanpan-com-ar) */
  --brand: #F15A24; /* Brand / Palette Token (chanpan-com-ar) */
  --brand-text: #A8360C; /* Typography Ink Token (chanpan-com-ar) */
  --paper: #EEE9DE; /* Canvas / Surface Token (chanpan-com-ar) */
  --line: rgba(23,19,13,.16); /* Color / Atmospheric Token (chanpan-com-ar) */
  --display: 'Archivo',sans-serif; /* Dimension / Scale Token (chanpan-com-ar) */
  --body: 'Inter',system-ui,sans-serif; /* Dimension / Scale Token (chanpan-com-ar) */
  --mono: 'JetBrains Mono',ui-monospace,monospace; /* Typography / Scale Token (chanpan-com-ar) */
  --mx: clamp(22px,5.5vw,88px); /* Dimension / Scale Token (chanpan-com-ar) */
  --band-bottom: 0px; /* Dimension / Scale Token (chanpan-com-ar) */
  --chanpan-com-ar-bg: #C1BBAE; /* Canvas Substrate (from `var(--bg)` in `:root`) (chanpan-com-ar) */
  --chanpan-com-ar-ink: #17130D; /* Primary Typography Ink (stylesheet-derived) (chanpan-com-ar) */
  --chanpan-com-ar-surface: #524B3D; /* Surface Substrate (stylesheet-derived) (chanpan-com-ar) */
  --chanpan-com-ar-accent: #F15A24; /* Interactive Accent (stylesheet-derived) (chanpan-com-ar) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#C1BBAE` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#17130D` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#524B3D` — grounded in `var(--ink-soft)` in `:root`
- **Interactive Accent / Highlight**: `#F15A24` — grounded in `var(--brand)` in `:root`
- **Secondary / Muted Copy**: `#A8360C` — grounded in `var(--brand-text)` in `:root`
- **Structural Hairline Border**: `#EEE9DE` — grounded in `var(--paper)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×25422px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `24ch` extracted from `chanpan-com-ar` stylesheet
- **Padding & Gutters**: `4px` lateral canvas padding with `26px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24ch`, `gap: 26px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `999px`, `50%`, `12px`, `14px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: CSS variables `--display: 'Archivo',sans-serif`
- **H2 Section Rule**: rule `h2` (`font-size: clamp(26px,3.2vw,42px)`, `font-weight: 800`)
- **Body Copy Rule**: CSS variables `--body: 'Inter',system-ui,sans-serif`; rule `body` (`line-height: 1.6`)
- **Metadata & Index Rule**: CSS variables `--mono: 'JetBrains Mono',ui-monospace,monospace`; rule `small` (`font-size: 9.5px`, `letter-spacing: .14em`, `font-weight: 600`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `chanpan-com-ar` (`ChanPan · AI Video Production, Commercials & Creative Studio — Argentina`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hd> — `chanpan-com-ar`)**:
   - DOM & Selectors: Landmark `<header class="hd">` hosting `ChanPan · AI Video Production, Comme` navigation (`Home · Demo Reel · Services · Work · Contact`), DOM attributes (`data-clip="s1-loop"`, `data-clip="s2-scrub"`, `data-scrub`, `data-clip="s3-scrub"`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hd> — `chanpan-com-ar`)` (`chanpan-com-ar`) adapts across `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)` transitions and links `Home · Demo Reel · Services · Work · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `ChanPan — AI video production and `)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `ChanPan — AI video production and creative studio` and copy excerpt *"Message us on WhatsApp"* over `#C1BBAE` canvas and `#17130D` ink.
   - Responsive Contract: Hero stage (`1440×25422px` desktop / `390×2400px` mobile) sets `#C1BBAE` background with `#17130D` headline `ChanPan — AI video production and creative studio`.
3. **Primary Showcase & Content Grid (<section.drive> — `First, perspective.`)**:
   - DOM & Selectors: Landmark `<section class="drive">` rendering section `First, perspective.` with copy *"Corrientes, Argentina"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `body.is-loading { overflow:hidden }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.drive> — `First, perspective.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24ch`, `gap: 26px`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.drive> — `Our terrain.`)**:
   - DOM & Selectors: Landmark `<section class="drive">` framing `Our terrain.` and `Twenty years climbing.` (*"Production company"*) with `#524B3D` surface cards, `#F15A24` accents, and `button { font:inherit;color:inherit }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.drive> — `Our terrain.`)` uses `999px`, `50%`, `12px`, `14px` radii, `#F15A24` highlights, and assets (favicon.svg, favicon-32.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.ft> — `https://chanpan.com.ar`)**:
   - DOM & Selectors: Landmark `<footer class="ft">` anchoring `ChanPan · AI Video Production, C` footer links (`Home · Demo Reel · Services · Work · Contact`), copy *"AI · Film · Design"*, and `#EEE9DE` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ft> — `https://chanpan.com.ar`)` aligns to `24ch` extracted from `chanpan-com-ar` stylesheet with `4px` lateral canvas padding with `26px` grid gap and attributes (data-clip="s1-loop", data-clip="s2-scrub", data-scrub).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Message us on WhatsApp"*
- Copy Excerpt 2: *"Corrientes, Argentina"*
- Copy Excerpt 3: *"Production company"*
- Copy Excerpt 4: *"AI · Film · Design"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)`
- **Extracted Stylesheet Rules (`chanpan-com-ar`)**:
- `html { -webkit-text-size-adjust:100% }`
- `body.is-loading { overflow:hidden }`
- `button { font:inherit;color:inherit }`
- `.sr { position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0... }`
- `.eyebrow b { color:var(--ink);font-weight:600 }`
- **Per-Selector Transition Rules**:
- **Selector `#pre`**: `transition: opacity .8s ease, transform .9s cubic-bezier(.7,0,.2,1)` extracted from `chanpan-com-ar` stylesheet.
- **Selector `.pre-iso--fill`**: `transition: clip-path .35s ease` extracted from `chanpan-com-ar` stylesheet.
- **Selector `#canvas`**: `transition: opacity .8s ease` extracted from `chanpan-com-ar` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,0,.2,1)`)**: Governs interactive state transitions across `<header.hd>` and `<section.drive>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.drive>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `chanpan-com-ar`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
