---
title: "UI Prompt Blueprint: dream-with-ai-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "dream-with-ai-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0b` / `#a04a2a`)"
---

# UI Design System & Master Generation Blueprint: dream-with-ai-com

> **Dream with AI** (https://dream-with-ai.com) — Can an AI feel anything? If it could, what would it dream? Every night an AI dreams up a whole new world, with its own visuals and sounds...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Dream with AI** (`https://dream-with-ai.com`). Can an AI feel anything? If it could, what would it dream? Every night an AI dreams up a whole new world, with its own visuals and sounds...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0b` / `#a04a2a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0b0b0b` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#e4e0d6` primary typography and `#a04a2a` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Cormorant Garamond` for display copy (`Dream with AI`) with `Georgia` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 6px`, padding `6px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` viewport stage).
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `6px` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:640px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0b0b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#e4e0d6` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1a1a1a` | `.case-row select { background: #1a1a1a }` |
| **Interactive Accent / Highlight** | `#a04a2a` | `var(--dxlAccent)` in `:root` |
| **Secondary / Muted Copy** | `#1c120d` | `var(--ink)` in `:root` |
| **Structural Hairline Border** | `#494949` | `.case-row select { border: #494949 }` |
| **Variable Token (`--paper`)** | `#d6cebe` | `var(--paper)` in `:root` |
| **Variable Token (`--dxlFg`)** | `#d9d9d9` | `var(--dxlFg)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dxl-bg` | `var(--dxlBg)` | Canvas / Surface Token |
| `--dxl-fg` | `var(--dxlFg)` | Typography Ink Token |
| `--dxl-accent` | `var(--dxlAccent)` | Brand / Palette Token |
| `--paper` | `#d6cebe` | Canvas / Surface Token |
| `--ink` | `#1c120d` | Typography Ink Token |
| `--rust` | `#a04a2a` | Color / Atmospheric Token |
| `--dxl-mark-font` | `500 11px/1 "JetBrains Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--dxl-mark-tracking` | `.08em` | Typography / Scale Token |
| `--dxl-mark-case` | `uppercase` | Design System Custom Token |
| `--dxl-mark-fg` | `var(--ink)` | Typography Ink Token |
| `--dxl-mark-bg` | `none` | Canvas / Surface Token |
| `--dxlBg` | `#0b0b0b` | Canvas / Surface Token |
| `--dxlFg` | `#d9d9d9` | Typography Ink Token |
| `--dxlAccent` | `#a04a2a` | Brand / Palette Token |
| `--wash` | `#0b0b0b` | Color / Atmospheric Token |
| `--text` | `#e4e0d6` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cormorant Garamond`.
- **Primary Body Stack**: `Georgia`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 92px`, `line-height: 87.4px`, `font-weight: 400`, `letter-spacing: -0.92px`); rule `h1` (`letter-spacing: -.01em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 54px`, `line-height: 51.3px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 17px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: 11px`, `font-weight: 500`, `letter-spacing: 0.88px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.dxl-mark[data-astro-cid-n6wkilw4]`**: `transition: opacity .2s` extracted from `dream-with-ai-com` stylesheet.
- **Selector `.hint`**: `transition: opacity 1.6s` extracted from `dream-with-ai-com` stylesheet.
- **Selector `.menu.leaving .plate`**: `transition: transform 1.6s ease-in-out` extracted from `dream-with-ai-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.noir>` and `<div.paper:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Dream with AI                              │
│ ====================================================================== │
│ [ <header.noir> (1440px)              | DEPT® LABS · BY DEPT® LABS   ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.paper> (w=1440px)                                 | │
│ | H1: Dream with AI                                                  | │
│ | Substrate: #0b0b0b | Ink: #e4e0d6 | Accent: #a04a2a                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.paper:nth(2)>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Every night I dream up a new |  | Close your eyes · hold       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<div.paper:nth(3)>) — An art piece by x09,          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.cue>        ) | https://dream-with-ai.com            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.noir>           ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<div.paper>) — 390px Vertical Lead                     | │
│ | H1: Dream with AI                                                  | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<div.paper:nth(2)>) — 1-Col Stack                  | │
│ | [ Item 1: Every night I dream up a new world. This is what       ] | │
│ | [ Item 2: Close your eyes · hold                                 ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<div.paper:nth(3)>) — 1-Col (An art piece by x0)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.cue>        ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.noir> — `dream-with-ai-com`)**:
   - Landmark `<header class="noir">` (`1440px`) hosting `Dream with AI` navigation (`DEPT® LABS · BY DEPT® LABS`), DOM attributes (`data-engine="three.js r180"`, `data-engine="three.js r180"`, `data-track="Start"`, `data-track-with="camera"`), and stylesheet rule `root { --paper: d6cebe;--ink: 1c120d;--rust: a04a2a }`.
2. **Hero Stage & Focal Lead (<div.paper> — `Dream with AI`)**:
   - Landmark `<div class="paper">` presenting display lead `Dream with AI` and copy excerpt *"Every night I dream up a new world. This is what I see, when nobo"* over `#0b0b0b` canvas and `#e4e0d6` ink.
3. **Primary Showcase & Content Grid (<div.paper:nth(2)> — `Every night I dream up a new world`)**:
   - Landmark `<div class="paper">` rendering section `Every night I dream up a new world. This is what` with copy *"Close your eyes · hold"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `sitemap-index.xml`, `script.js`), and grid rule `body { margin:0;height:100%;overflow:hidden;background:var(--paper) }`.
4. **Interactive Detail & Feature Matrix (<div.paper:nth(3)> — `Close your eyes · hold`)**:
   - Landmark `<div class="paper">` framing `Close your eyes · hold` and `An art piece by x09, brought to life by DEPT® LA` (*"An art piece by x09, brought to life by DEPT® LABS"*) with `#1a1a1a` surface cards, `#a04a2a` accents, and `lids { position:fixed;inset:0;width:100%;height:100%;display:block;touch-action... }`.
5. **Colophon & Global Directory Footer (<footer.cue> — `https://dream-with-ai.com`)**:
   - Landmark `<footer class="cue">` anchoring `Dream with AI` footer links (`DEPT® LABS · BY DEPT® LABS`), copy *"Every night an AI dreams a new world, engraved like Escher a"*, and `#494949` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dream-with-ai-com (Dream with AI)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dream-with-ai-com` (**Dream with AI** — `https://dream-with-ai.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0b` / `#a04a2a`).
- **Identity & Domain Context**: Can an AI feel anything? If it could, what would it dream? Every night an AI dreams up a whole new world, with its own visuals and sounds...
- **Primary Substrate**: `#0b0b0b` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#e4e0d6`, **Accent / Highlight**: `#a04a2a`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0b0b0b` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#e4e0d6` primary typography and `#a04a2a` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Cormorant Garamond` for display copy (`Dream with AI`) with `Georgia` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 6px`, padding `6px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dream-with-ai-com` in your global stylesheet:

:root {
  /* Dream with AI (dream-with-ai-com) — Live-Grounded CSS Variables */
  --dxl-bg: var(--dxlBg); /* Canvas / Surface Token (dream-with-ai-com) */
  --dxl-fg: var(--dxlFg); /* Typography Ink Token (dream-with-ai-com) */
  --dxl-accent: var(--dxlAccent); /* Brand / Palette Token (dream-with-ai-com) */
  --paper: #d6cebe; /* Canvas / Surface Token (dream-with-ai-com) */
  --ink: #1c120d; /* Typography Ink Token (dream-with-ai-com) */
  --rust: #a04a2a; /* Color / Atmospheric Token (dream-with-ai-com) */
  --dxl-mark-font: 500 11px/1 "JetBrains Mono", ui-monospace, monospace; /* Typography / Scale Token (dream-with-ai-com) */
  --dxl-mark-tracking: .08em; /* Typography / Scale Token (dream-with-ai-com) */
  --dxl-mark-case: uppercase; /* Design System Custom Token (dream-with-ai-com) */
  --dxl-mark-fg: var(--ink); /* Typography Ink Token (dream-with-ai-com) */
  --dxl-mark-bg: none; /* Canvas / Surface Token (dream-with-ai-com) */
  --dxlBg: #0b0b0b; /* Canvas / Surface Token (dream-with-ai-com) */
  --dxlFg: #d9d9d9; /* Typography Ink Token (dream-with-ai-com) */
  --dxlAccent: #a04a2a; /* Brand / Palette Token (dream-with-ai-com) */
  --wash: #0b0b0b; /* Color / Atmospheric Token (dream-with-ai-com) */
  --text: #e4e0d6; /* Typography Ink Token (dream-with-ai-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0b0b0b` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#e4e0d6` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#1a1a1a` — grounded in `.case-row select { background: #1a1a1a }`
- **Interactive Accent / Highlight**: `#a04a2a` — grounded in `var(--dxlAccent)` in `:root`
- **Secondary / Muted Copy**: `#1c120d` — grounded in `var(--ink)` in `:root`
- **Structural Hairline Border**: `#494949` — grounded in `.case-row select { border: #494949 }`
- **Variable Token (`--paper`)**: `#d6cebe` — grounded in `var(--paper)` in `:root`
- **Variable Token (`--dxlFg`)**: `#d9d9d9` — grounded in `var(--dxlFg)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` viewport stage)
- **Padding & Gutters**: `6px` lateral canvas padding with `6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:640px)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Georgia`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 92px`, `line-height: 87.4px`, `font-weight: 400`, `letter-spacing: -0.92px`); rule `h1` (`letter-spacing: -.01em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 54px`, `line-height: 51.3px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 17px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 11px`, `line-height: 11px`, `font-weight: 500`, `letter-spacing: 0.88px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dream-with-ai-com` (`Dream with AI`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.noir> — `dream-with-ai-com`)**:
   - DOM & Selectors: Landmark `<header class="noir">` (`1440px`) hosting `Dream with AI` navigation (`DEPT® LABS · BY DEPT® LABS`), DOM attributes (`data-engine="three.js r180"`, `data-engine="three.js r180"`, `data-track="Start"`, `data-track-with="camera"`), and stylesheet rule `root { --paper: d6cebe;--ink: 1c120d;--rust: a04a2a }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.noir> — `dream-with-ai-com`)` (`dream-with-ai-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:640px)` with `cubic-bezier(.2,.7,.2,1)` transitions and links `DEPT® LABS · BY DEPT® LABS`.
2. **Hero Stage & Focal Lead (<div.paper> — `Dream with AI`)**:
   - DOM & Selectors: Landmark `<div class="paper">` presenting display lead `Dream with AI` and copy excerpt *"Every night I dream up a new world. This is what I see, when nobo"* over `#0b0b0b` canvas and `#e4e0d6` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#0b0b0b` background with `#e4e0d6` headline `Dream with AI`.
3. **Primary Showcase & Content Grid (<div.paper:nth(2)> — `Every night I dream up a new world`)**:
   - DOM & Selectors: Landmark `<div class="paper">` rendering section `Every night I dream up a new world. This is what` with copy *"Close your eyes · hold"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `sitemap-index.xml`, `script.js`), and grid rule `body { margin:0;height:100%;overflow:hidden;background:var(--paper) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.paper:nth(2)> — `Every night I dream up a new world`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 6px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.paper:nth(3)> — `Close your eyes · hold`)**:
   - DOM & Selectors: Landmark `<div class="paper">` framing `Close your eyes · hold` and `An art piece by x09, brought to life by DEPT® LA` (*"An art piece by x09, brought to life by DEPT® LABS"*) with `#1a1a1a` surface cards, `#a04a2a` accents, and `lids { position:fixed;inset:0;width:100%;height:100%;display:block;touch-action... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.paper:nth(3)> — `Close your eyes · hold`)` uses `0px` (sharp unrounded corners) radii, `#a04a2a` highlights, and assets (favicon.svg, apple-touch-icon.png, sitemap-index.xml).
5. **Colophon & Global Directory Footer (<footer.cue> — `https://dream-with-ai.com`)**:
   - DOM & Selectors: Landmark `<footer class="cue">` anchoring `Dream with AI` footer links (`DEPT® LABS · BY DEPT® LABS`), copy *"Every night an AI dreams a new world, engraved like Escher a"*, and `#494949` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.cue> — `https://dream-with-ai.com`)` aligns to `1440px` (full-bleed `100%` viewport stage) with `6px` lateral canvas padding with `6px` grid gap and attributes (data-engine="three.js r180", data-engine="three.js r180", data-track="Start").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Every night I dream up a new world. This is what I see, when nobody is asking me a..."*
- Copy Excerpt 2: *"Close your eyes · hold"*
- Copy Excerpt 3: *"An art piece by x09, brought to life by DEPT® LABS"*
- Copy Excerpt 4: *"Every night an AI dreams a new world, engraved like Escher and melted like Dalí, a..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.2,1)`
- **Extracted Stylesheet Rules (`dream-with-ai-com`)**:
- `root { --paper: d6cebe;--ink: 1c120d;--rust: a04a2a }`
- `body { margin:0;height:100%;overflow:hidden;background:var(--paper) }`
- `lids { position:fixed;inset:0;width:100%;height:100%;display:block;touch-action... }`
- `video { position:fixed;left:0;top:0;width:2px;height:2px;opacity:0;pointer-event... }`
- `.menu .plate { position:relative;max-width:620px;padding:38px 44px 30px }`
- **Per-Selector Transition Rules**:
- **Selector `.dxl-mark[data-astro-cid-n6wkilw4]`**: `transition: opacity .2s` extracted from `dream-with-ai-com` stylesheet.
- **Selector `.hint`**: `transition: opacity 1.6s` extracted from `dream-with-ai-com` stylesheet.
- **Selector `.menu.leaving .plate`**: `transition: transform 1.6s ease-in-out` extracted from `dream-with-ai-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.noir>` and `<div.paper:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dream-with-ai-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
