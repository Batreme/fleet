---
title: "UI Prompt Blueprint: chanpan-com-ar"
date: 2026-11-23
captured_at: 2026-11-23
target: "chanpan-com-ar"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#c1bbae` canvas, `#17130d` ink, `#f15a24` accent)"
---

# UI Design System & Master Generation Blueprint: chanpan-com-ar

> **ChanPan · AI Video Production, Commercials & Creative Studio — Argentina** (https://chanpan.com.ar) — AI-driven video production, commercials, branded content, branding and 2D/3D animation. A creative studio from Corrientes, Argentina, wor...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ChanPan · AI Video Production, Commercials & Creative Studio — Argentina** (`https://chanpan.com.ar`). AI-driven video production, commercials, branded content, branding and 2D/3D animation. A creative studio from Corrientes, Argentina, wor...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#c1bbae` canvas, `#17130d` ink, `#f15a24` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#c1bbae` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#17130d` primary typography and `#f15a24` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Archivo` for display copy (`ChanPan — AI video production and cr`) with `Inter` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `79.2px`) with `cubic-bezier(.7,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `79.2px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `999px`, `50%`, `12px`, `14px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `79.2px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#c1bbae` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#17130d` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eee9de` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#f15a24` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#524b3d` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#a6a094` | `var(--line)` in `:root` (`rgba(23,19,13,.16)`) |
| **Variable Token (`--brand-text`)** | `#a8360c` | `var(--brand-text)` in `:root` |

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
| `--chanpan-com-ar-bg` | `#c1bbae` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--chanpan-com-ar-ink` | `#17130d` | Primary Typography Ink (computed-derived) |
| `--chanpan-com-ar-surface` | `#eee9de` | Surface Substrate (computed-derived) |
| `--chanpan-com-ar-accent` | `#f15a24` | Interactive Accent (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 32.64px`, `font-weight: 700`, `letter-spacing: -0.64px`); CSS variables `--display: 'Archivo',sans-serif`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 33.12px`, `line-height: 33.7824px`, `font-weight: 800`, `letter-spacing: -0.6624px`); rule `h2` (`font-size: clamp(26px,3.2vw,42px)`, `font-weight: 800`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--body: 'Inter',system-ui,sans-serif`; rule `body` (`line-height: 1.6`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--mono: 'JetBrains Mono',ui-monospace,monospace`; rule `small` (`font-size: 9.5px`, `letter-spacing: .14em`, `font-weight: 600`).

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

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ChanPan · AI Video Production, Commercials │
│ ====================================================================== │
│ [ <header.hd> (1440x89px)             | Home · Demo Reel · Services  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: ChanPan — AI video production and creative studio              | │
│ | Substrate: #c1bbae | Ink: #17130d | Accent: #f15a24                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.drive>) max-w: 1440px                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | First, perspective.          |  | Our terrain.                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.drive:nth(2)>) — Twenty years climbing     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ft>         ) | https://chanpan.com.ar               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.hd>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: ChanPan — AI video production and creative studio              | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.drive>) — 1-Col Stack                     | │
│ | [ Item 1: First, perspective.                                    ] | │
│ | [ Item 2: Our terrain.                                           ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.drive:nth(2)>) — 1-Col (Twenty years climb) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ft>         ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hd> — `chanpan-com-ar`)**:
   - Landmark `<header class="hd">` (`1440x89px`) hosting `ChanPan · AI Video Production, Comme` navigation (`Home · Demo Reel · Services · Work · Contact`), DOM attributes (`data-clip="s1-loop"`, `data-clip="s2-scrub"`, `data-scrub`, `data-clip="s3-scrub"`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.hero> — `ChanPan — AI video production and `)**:
   - Landmark `<section class="hero">` presenting display lead `ChanPan — AI video production and creative studio` and copy excerpt *"AI as a production tool, not a shortcut."* over `#c1bbae` canvas and `#17130d` ink.
3. **Primary Showcase & Content Grid (<section.drive> — `First, perspective.`)**:
   - Landmark `<section class="drive">` rendering section `First, perspective.` with copy *"Corrientes, Argentina"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `body.is-loading { overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.drive:nth(2)> — `Our terrain.`)**:
   - Landmark `<section class="drive">` framing `Our terrain.` and `Twenty years climbing.` (*"Production company"*) with `#eee9de` surface cards, `#f15a24` accents, and `button { font:inherit;color:inherit }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://chanpan.com.ar`)**:
   - Landmark `<footer class="ft">` anchoring `ChanPan · AI Video Production, C` footer links (`Home · Demo Reel · Services · Work · Contact`), copy *"AI · Film · Design"*, and `#a6a094` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: chanpan-com-ar (ChanPan · AI Video Production, Commercials & Creative Studio — Argentina)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `chanpan-com-ar` (**ChanPan · AI Video Production, Commercials & Creative Studio — Argentina** — `https://chanpan.com.ar`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#c1bbae` canvas, `#17130d` ink, `#f15a24` accent).
- **Identity & Domain Context**: AI-driven video production, commercials, branded content, branding and 2D/3D animation. A creative studio from Corrientes, Argentina, wor...
- **Primary Substrate**: `#c1bbae` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#17130d`, **Accent / Highlight**: `#f15a24`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#c1bbae` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#17130d` primary typography and `#f15a24` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Archivo` for display copy (`ChanPan — AI video production and cr`) with `Inter` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `79.2px`) with `cubic-bezier(.7,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `chanpan-com-ar` in your global stylesheet:

:root {
  /* ChanPan · AI Video Production, Commercials & Creative Studio — Argentina (chanpan-com-ar) — Live-Grounded CSS Variables */
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
  --chanpan-com-ar-bg: #c1bbae; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (chanpan-com-ar) */
  --chanpan-com-ar-ink: #17130d; /* Primary Typography Ink (computed-derived) (chanpan-com-ar) */
  --chanpan-com-ar-surface: #eee9de; /* Surface Substrate (computed-derived) (chanpan-com-ar) */
  --chanpan-com-ar-accent: #f15a24; /* Interactive Accent (computed-derived) (chanpan-com-ar) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#c1bbae` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#17130d` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#eee9de` — grounded in `var(--paper)` in `:root`
- **Interactive Accent / Highlight**: `#f15a24` — grounded in `var(--brand)` in `:root`
- **Secondary / Muted Copy**: `#524b3d` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#a6a094` — grounded in `var(--line)` in `:root` (`rgba(23,19,13,.16)`)
- **Variable Token (`--brand-text`)**: `#a8360c` — grounded in `var(--brand-text)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `79.2px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `79.2px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `999px`, `50%`, `12px`, `14px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 32px`, `line-height: 32.64px`, `font-weight: 700`, `letter-spacing: -0.64px`); CSS variables `--display: 'Archivo',sans-serif`
- **H2 Section Rule**: live computed `h2` (`font-size: 33.12px`, `line-height: 33.7824px`, `font-weight: 800`, `letter-spacing: -0.6624px`); rule `h2` (`font-size: clamp(26px,3.2vw,42px)`, `font-weight: 800`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--body: 'Inter',system-ui,sans-serif`; rule `body` (`line-height: 1.6`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--mono: 'JetBrains Mono',ui-monospace,monospace`; rule `small` (`font-size: 9.5px`, `letter-spacing: .14em`, `font-weight: 600`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `chanpan-com-ar` (`ChanPan · AI Video Production, Commercials & Creative Studio — Argentina`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hd> — `chanpan-com-ar`)**:
   - DOM & Selectors: Landmark `<header class="hd">` (`1440x89px`) hosting `ChanPan · AI Video Production, Comme` navigation (`Home · Demo Reel · Services · Work · Contact`), DOM attributes (`data-clip="s1-loop"`, `data-clip="s2-scrub"`, `data-scrub`, `data-clip="s3-scrub"`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hd> — `chanpan-com-ar`)` (`chanpan-com-ar`) adapts across `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)` transitions and links `Home · Demo Reel · Services · Work · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `ChanPan — AI video production and `)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `ChanPan — AI video production and creative studio` and copy excerpt *"AI as a production tool, not a shortcut."* over `#c1bbae` canvas and `#17130d` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#c1bbae` background with `#17130d` headline `ChanPan — AI video production and creative studio`.
3. **Primary Showcase & Content Grid (<section.drive> — `First, perspective.`)**:
   - DOM & Selectors: Landmark `<section class="drive">` rendering section `First, perspective.` with copy *"Corrientes, Argentina"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `body.is-loading { overflow:hidden }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.drive> — `First, perspective.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `79.2px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.drive:nth(2)> — `Our terrain.`)**:
   - DOM & Selectors: Landmark `<section class="drive">` framing `Our terrain.` and `Twenty years climbing.` (*"Production company"*) with `#eee9de` surface cards, `#f15a24` accents, and `button { font:inherit;color:inherit }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.drive:nth(2)> — `Our terrain.`)` uses `999px`, `50%`, `12px`, `14px` radii, `#f15a24` highlights, and assets (favicon.svg, favicon-32.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.ft> — `https://chanpan.com.ar`)**:
   - DOM & Selectors: Landmark `<footer class="ft">` anchoring `ChanPan · AI Video Production, C` footer links (`Home · Demo Reel · Services · Work · Contact`), copy *"AI · Film · Design"*, and `#a6a094` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ft> — `https://chanpan.com.ar`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `79.2px` lateral canvas padding with `16px` grid gap and attributes (data-clip="s1-loop", data-clip="s2-scrub", data-scrub).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"AI as a production tool, not a shortcut."*
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
