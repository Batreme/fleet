---
title: "UI Prompt Blueprint: fontsight-xyz"
date: 2026-11-15
target: "[[overview|fontsight-xyz]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffd84a` / `#ff5a36`)"
---

# UI Design System & Master Generation Blueprint: fontsight-xyz

> **Fontsight: What Font Is That? Font Finder for Chrome** (https://fontsight.xyz/) — What font is that? Point at any text to see the typeface that actually rendered, who made it, and the CSS to use it. A free font finder f...

![Desktop Viewport Capture (1440x11776)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Fontsight: What Font Is That? Font Finder for Chrome** (`https://fontsight.xyz/`). What font is that? Point at any text to see the typeface that actually rendered, who made it, and the CSS to use it. A free font finder f...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffd84a` / `#ff5a36`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffd84a` (`var(--yellow)` in `:root`) paired with `#0b0b0c` primary typography and `#ff5a36` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bricolage Grotesque` for display copy (`What font is that? W h a t f o n t i`) with `Inter` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1360px` container bounds (`gap: 10px`, padding `7px`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×11776px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1360px` extracted from `fontsight-xyz` stylesheet.
- **Canvas Lateral Padding & Spacing**: `7px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `8px`, `999px`, `7px`, `18px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=900px)`, `@media (width<=1100px)`, `@media (width<=760px)`, `@media (width<=820px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffd84a` | `var(--yellow)` in `:root` |
| **Primary Typography Ink** | `#2e44ff` | `var(--blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff9acd` | `var(--pink)` in `:root` |
| **Interactive Accent / Highlight** | `#ff5a36` | `var(--tomato)` in `:root` |
| **Secondary / Muted Copy** | `#0b0b0c` | `var(--ink)` in `:root` |
| **Structural Hairline Border** | `#fffdf6` | `var(--paper)` in `:root` |
| **Variable Token (`--ink-2`)** | `#0b0b0cad` | `var(--ink-2)` in `:root` |
| **Variable Token (`--paper-2`)** | `#fffdf6db` | `var(--paper-2)` in `:root` |
| **Variable Token (`--card`)** | `#1c1c1b` | `var(--card)` in `:root` |
| **Variable Token (`--card-well`)** | `#262625` | `var(--card-well)` in `:root` |
| **Variable Token (`--card-row`)** | `#2b2b2a` | `var(--card-row)` in `:root` |
| **Variable Token (`--card-line`)** | `#f4f4f11a` | `var(--card-line)` in `:root` |
| **Variable Token (`--card-ink`)** | `#f4f4f1` | `var(--card-ink)` in `:root` |
| **Variable Token (`--card-soft`)** | `#9b9a94` | `var(--card-soft)` in `:root` |
| **Variable Token (`--warn`)** | `#f2b544` | `var(--warn)` in `:root` |
| **Variable Token (`--go`)** | `#5be38a` | `var(--go)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--yellow` | `#ffd84a` | Color / Atmospheric Token |
| `--blue` | `#2e44ff` | Color / Atmospheric Token |
| `--pink` | `#ff9acd` | Typography Ink Token |
| `--tomato` | `#ff5a36` | Color / Atmospheric Token |
| `--ink` | `#0b0b0c` | Typography Ink Token |
| `--paper` | `#fffdf6` | Canvas / Surface Token |
| `--ink-2` | `#0b0b0cad` | Typography Ink Token |
| `--paper-2` | `#fffdf6db` | Canvas / Surface Token |
| `--card` | `#1c1c1b` | Color / Atmospheric Token |
| `--card-well` | `#262625` | Color / Atmospheric Token |
| `--card-row` | `#2b2b2a` | Color / Atmospheric Token |
| `--card-line` | `#f4f4f11a` | Color / Atmospheric Token |
| `--card-ink` | `#f4f4f1` | Typography Ink Token |
| `--card-soft` | `#9b9a94` | Color / Atmospheric Token |
| `--warn` | `#f2b544` | Color / Atmospheric Token |
| `--go` | `#5be38a` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Bricolage Grotesque`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--display: "Bricolage Grotesque", "Inter", system-ui, sans-serif`.
- **Section Heading (`H2`)**: rule `.h2` (`font-size: clamp(44px,6.4vw,104px)`).
- **Body Copy**: rule `p` (`font-size: 15.5px`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: CSS variables `--mono: "Geist Mono", ui-monospace, "SF Mono", Menlo, monospace`; rule `small` (`letter-spacing: normal`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.34,1.56,.64,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn`**: `transition: transform .4s var(--spring), box-shadow .4s var(--ease)` extracted from `fontsight-xyz` stylesheet.
- **Selector `.nav-links .nav-page`**: `transition: transform .35s var(--spring), background .2s` extracted from `fontsight-xyz` stylesheet.
- **Selector `.shuffle`**: `transition: opacity .6s var(--ease), transform .8s var(--ease)` extracted from `fontsight-xyz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.demo>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Fontsight: What Font Is That? Font Finder  │
│ ====================================================================== │
│ [ <header.nav>             | How it works · Fallbacks · Try on · Te ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: What font is that? W h a t f o n t i s t h a t ?             |   │
│ | Substrate: #ffd84a    | Ink: #0b0b0c    | Accent: #ff5a36        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.demo>            ) max-w: 1360px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Point. Click. Copy.          |  | Soup tastes better in a seri | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.nav>] -> [<section.hero>] -> [<section.demo>] |             │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://fontsight.xyz/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `fontsight-xyz`)**:
   - Landmark `<header class="nav wrap">` hosting `Fontsight: What Font Is That? Font F` navigation (`How it works · Fallbacks · Try on · Test drive · Foundries`), DOM attributes (`data-browser="chrome"`, `data-site="GQEJOPOH"`, `data-noinspect`, `data-store`), and stylesheet rule `img { max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.hero> — `What font is that? W h a t f o n t`)**:
   - Landmark `<section class="hero">` presenting display lead `What font is that? W h a t f o n t i s t h a t ?` and copy excerpt *"Free alternatives ↗"* over `#ffd84a` canvas and `#0b0b0c` ink.
3. **Primary Showcase & Content Grid (<section.demo> — `Point. Click. Copy.`)**:
   - Landmark `<section class="demo">` rendering section `Point. Click. Copy.` with copy *"Add to Chrome Brave"*, asset references (`bricolage-grotesque-latin-standar...`, `inter-latin-opsz-normal.BwkfbSeq....`, `favicon.ico`, `favicon.svg`), and grid rule `html { scroll-behavior:smooth;background:var(--ink);overscroll-behavior-y:none }`.
4. **Interactive Detail & Feature Matrix (<section.fallback> — `Soup tastes better in a serif.`)**:
   - Landmark `<section class="fallback">` framing `Soup tastes better in a serif.` and `Asked for Söhne . Got Arial .` (*"What font is that?"*) with `#ff9acd` surface cards, `#ff5a36` accents, and `selection { background:var(--ink);color:var(--yellow) }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://fontsight.xyz/`)**:
   - Landmark `<footer class="footer">` anchoring `Fontsight: What Font Is That? Fo` footer links (`How it works · Fallbacks · Try on · Test drive · Foundries`), copy *"Bricolage Grotesque ExtraBold"*, and `#fffdf6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: fontsight-xyz (Fontsight: What Font Is That? Font Finder for Chrome)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `fontsight-xyz` (**Fontsight: What Font Is That? Font Finder for Chrome** — `https://fontsight.xyz/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffd84a` / `#ff5a36`).
- **Identity & Domain Context**: What font is that? Point at any text to see the typeface that actually rendered, who made it, and the CSS to use it. A free font finder f...
- **Primary Substrate**: `#ffd84a` (`var(--yellow)` in `:root`), **Primary Ink**: `#0b0b0c`, **Accent / Highlight**: `#ff5a36`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffd84a` (`var(--yellow)` in `:root`) paired with `#0b0b0c` primary typography and `#ff5a36` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bricolage Grotesque` for display copy (`What font is that? W h a t f o n t i`) with `Inter` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1360px` container bounds (`gap: 10px`, padding `7px`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `fontsight-xyz` in your global stylesheet:

:root {
  /* Fontsight: What Font Is That? Font Finder for Chrome (fontsight-xyz) — Ground-Truth Extracted CSS Variables */
  --yellow: #ffd84a; /* Color / Atmospheric Token (fontsight-xyz) */
  --blue: #2e44ff; /* Color / Atmospheric Token (fontsight-xyz) */
  --pink: #ff9acd; /* Typography Ink Token (fontsight-xyz) */
  --tomato: #ff5a36; /* Color / Atmospheric Token (fontsight-xyz) */
  --ink: #0b0b0c; /* Typography Ink Token (fontsight-xyz) */
  --paper: #fffdf6; /* Canvas / Surface Token (fontsight-xyz) */
  --ink-2: #0b0b0cad; /* Typography Ink Token (fontsight-xyz) */
  --paper-2: #fffdf6db; /* Canvas / Surface Token (fontsight-xyz) */
  --card: #1c1c1b; /* Color / Atmospheric Token (fontsight-xyz) */
  --card-well: #262625; /* Color / Atmospheric Token (fontsight-xyz) */
  --card-row: #2b2b2a; /* Color / Atmospheric Token (fontsight-xyz) */
  --card-line: #f4f4f11a; /* Color / Atmospheric Token (fontsight-xyz) */
  --card-ink: #f4f4f1; /* Typography Ink Token (fontsight-xyz) */
  --card-soft: #9b9a94; /* Color / Atmospheric Token (fontsight-xyz) */
  --warn: #f2b544; /* Color / Atmospheric Token (fontsight-xyz) */
  --go: #5be38a; /* Color / Atmospheric Token (fontsight-xyz) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffd84a` — grounded in `var(--yellow)` in `:root`
- **Primary Typography Ink**: `#2e44ff` — grounded in `var(--blue)` in `:root`
- **Elevated Surface / Card Substrate**: `#ff9acd` — grounded in `var(--pink)` in `:root`
- **Interactive Accent / Highlight**: `#ff5a36` — grounded in `var(--tomato)` in `:root`
- **Secondary / Muted Copy**: `#0b0b0c` — grounded in `var(--ink)` in `:root`
- **Structural Hairline Border**: `#fffdf6` — grounded in `var(--paper)` in `:root`
- **Variable Token (`--ink-2`)**: `#0b0b0cad` — grounded in `var(--ink-2)` in `:root`
- **Variable Token (`--paper-2`)**: `#fffdf6db` — grounded in `var(--paper-2)` in `:root`
- **Variable Token (`--card`)**: `#1c1c1b` — grounded in `var(--card)` in `:root`
- **Variable Token (`--card-well`)**: `#262625` — grounded in `var(--card-well)` in `:root`
- **Variable Token (`--card-row`)**: `#2b2b2a` — grounded in `var(--card-row)` in `:root`
- **Variable Token (`--card-line`)**: `#f4f4f11a` — grounded in `var(--card-line)` in `:root`
- **Variable Token (`--card-ink`)**: `#f4f4f1` — grounded in `var(--card-ink)` in `:root`
- **Variable Token (`--card-soft`)**: `#9b9a94` — grounded in `var(--card-soft)` in `:root`
- **Variable Token (`--warn`)**: `#f2b544` — grounded in `var(--warn)` in `:root`
- **Variable Token (`--go`)**: `#5be38a` — grounded in `var(--go)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×11776px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1360px` extracted from `fontsight-xyz` stylesheet
- **Padding & Gutters**: `7px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding
- **Media Queries**: `@media (width>=900px)`, `@media (width<=1100px)`, `@media (width<=760px)`, `@media (width<=820px)`
- **Corner Radii**: `8px`, `999px`, `7px`, `18px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Bricolage Grotesque`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: CSS variables `--display: "Bricolage Grotesque", "Inter", system-ui, sans-serif`
- **H2 Section Rule**: rule `.h2` (`font-size: clamp(44px,6.4vw,104px)`)
- **Body Copy Rule**: rule `p` (`font-size: 15.5px`, `line-height: 1.5`)
- **Metadata & Index Rule**: CSS variables `--mono: "Geist Mono", ui-monospace, "SF Mono", Menlo, monospace`; rule `small` (`letter-spacing: normal`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `fontsight-xyz` (`Fontsight: What Font Is That? Font Finder for Chrome`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `fontsight-xyz`)**:
   - DOM & Selectors: Landmark `<header class="nav wrap">` hosting `Fontsight: What Font Is That? Font F` navigation (`How it works · Fallbacks · Try on · Test drive · Foundries`), DOM attributes (`data-browser="chrome"`, `data-site="GQEJOPOH"`, `data-noinspect`, `data-store`), and stylesheet rule `img { max-width:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `fontsight-xyz`)` (`fontsight-xyz`) adapts across `@media (width>=900px)`, `@media (width<=1100px)`, `@media (width<=760px)`, `@media (width<=820px)` with `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.34,1.56,.64,1)` transitions and links `How it works · Fallbacks · Try on · Test drive · Foundries`.
2. **Hero Stage & Focal Lead (<section.hero> — `What font is that? W h a t f o n t`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `What font is that? W h a t f o n t i s t h a t ?` and copy excerpt *"Free alternatives ↗"* over `#ffd84a` canvas and `#0b0b0c` ink.
   - Responsive Contract: Hero stage (`1440×11776px` desktop / `390×2400px` mobile) sets `#ffd84a` background with `#0b0b0c` headline `What font is that? W h a t f o n t i s t h a t ?`.
3. **Primary Showcase & Content Grid (<section.demo> — `Point. Click. Copy.`)**:
   - DOM & Selectors: Landmark `<section class="demo">` rendering section `Point. Click. Copy.` with copy *"Add to Chrome Brave"*, asset references (`bricolage-grotesque-latin-standar...`, `inter-latin-opsz-normal.BwkfbSeq....`, `favicon.ico`, `favicon.svg`), and grid rule `html { scroll-behavior:smooth;background:var(--ink);overscroll-behavior-y:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.demo> — `Point. Click. Copy.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `7px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.fallback> — `Soup tastes better in a serif.`)**:
   - DOM & Selectors: Landmark `<section class="fallback">` framing `Soup tastes better in a serif.` and `Asked for Söhne . Got Arial .` (*"What font is that?"*) with `#ff9acd` surface cards, `#ff5a36` accents, and `selection { background:var(--ink);color:var(--yellow) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.fallback> — `Soup tastes better in a serif.`)` uses `8px`, `999px`, `7px`, `18px` radii, `#ff5a36` highlights, and assets (bricolage-grotesque-latin-standar..., inter-latin-opsz-normal.BwkfbSeq...., favicon.ico).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://fontsight.xyz/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Fontsight: What Font Is That? Fo` footer links (`How it works · Fallbacks · Try on · Test drive · Foundries`), copy *"Bricolage Grotesque ExtraBold"*, and `#fffdf6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://fontsight.xyz/`)` aligns to `1360px` extracted from `fontsight-xyz` stylesheet with `7px` lateral canvas padding with `10px` grid gap and attributes (data-browser="chrome", data-site="GQEJOPOH", data-noinspect).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Free alternatives ↗"*
- Copy Excerpt 2: *"Add to Chrome Brave"*
- Copy Excerpt 3: *"What font is that?"*
- Copy Excerpt 4: *"Bricolage Grotesque ExtraBold"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.34,1.56,.64,1)`
- **Extracted Stylesheet Rules (`fontsight-xyz`)**:
- `img { max-width:100% }`
- `html { scroll-behavior:smooth;background:var(--ink);overscroll-behavior-y:none }`
- `selection { background:var(--ink);color:var(--yellow) }`
- `focus-visible { outline:3px solid var(--ink);outline-offset:3px;border-radius:8px }`
- `.sr { clip:rect(0 0 0 0);white-space:nowrap;width:1px;height:1px;position:abso... }`
- **Per-Selector Transition Rules**:
- **Selector `.btn`**: `transition: transform .4s var(--spring), box-shadow .4s var(--ease)` extracted from `fontsight-xyz` stylesheet.
- **Selector `.nav-links .nav-page`**: `transition: transform .35s var(--spring), background .2s` extracted from `fontsight-xyz` stylesheet.
- **Selector `.shuffle`**: `transition: opacity .6s var(--ease), transform .8s var(--ease)` extracted from `fontsight-xyz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.demo>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `fontsight-xyz`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
