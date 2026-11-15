---
title: "UI Prompt Blueprint: degacsid-com"
date: 2026-11-15
target: "degacsid-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fffcf9` / `#E55655`)"
---

# UI Design System & Master Generation Blueprint: degacsid-com

> **DEGACSID** (https://degacsid.com/) — The Only Creative Partner You'll Need. Full Service Creative Agency that handles everything from strategy, conception, design, execution,...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **DEGACSID** (`https://degacsid.com/`). The Only Creative Partner You'll Need. Full Service Creative Agency that handles everything from strategy, conception, design, execution,...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fffcf9` / `#E55655`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fffcf9` (`body { background: #fffcf9 }`) paired with `#E55655` primary typography and `#E55655` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Return of the Boss` for display copy (`DEGACSID`) with `Crimson Text` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `none (full-bleed `100%` viewport stage)` container bounds (`gap: 12px`, padding `10px`) with `cubic-bezier(0.5,0,0.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `none (full-bleed `100%` viewport stage)` extracted from `degacsid-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: no `@media` queries in static stylesheet (fluid viewport scaling).

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fffcf9` | `body { background: #fffcf9 }` |
| **Primary Typography Ink** | `#FFF4E7` | `.navkkwuna-mi .navkkwuna-lbl { color: #FFF4E7 }` |
| **Elevated Surface / Card Substrate** | `#E55655` | `.navkkwuna-mi .navkkwuna-arw { color: #E55655 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--crt-safe` | `31px` | Dimension / Scale Token |
| `--degacsid-com-bg` | `#fffcf9` | Canvas Substrate (from `body { background: #fffcf9 }`) |
| `--degacsid-com-ink` | `#E55655` | Primary Typography Ink (stylesheet-derived) |
| `--degacsid-com-surface` | `#E55655` | Surface Substrate (stylesheet-derived) |
| `--degacsid-com-accent` | `#E55655` | Interactive Accent (stylesheet-derived) |
| `--degacsid-com-muted` | `#E55655` | Secondary Ink (stylesheet-derived) |
| `--degacsid-com-border` | `#E55655` | Structural Border (stylesheet-derived) |
| `--degacsid-com-container` | `none` | Container Bound (stylesheet-derived) |
| `--degacsid-com-gap` | `12px` | Grid Gutter (stylesheet-derived) |
| `--degacsid-com-pad` | `10px` | Lateral Padding (stylesheet-derived) |
| `--degacsid-com-ease` | `cubic-bezier(0.5,0,0.2,1)` | Primary Easing Function |
| `--degacsid-com-radius` | `50%` | Corner Radius (stylesheet-derived) |
| `--degacsid-com-fs-base` | `11px` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Return of the Boss`.
- **Primary Body Stack**: `Crimson Text`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.5,0,0.2,1)`, `cubic-bezier(0.2,0.8,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.navkkwuna-mi .navkkwuna-lbl`**: `transition: color .13s ease` extracted from `degacsid-com` stylesheet.
- **Selector `.navkkwuna-mi .navkkwuna-arw`**: `transition: opacity .15s ease, transform .15s ease` extracted from `degacsid-com` stylesheet.
- **Selector `style]`**: `transition: opacity 260ms` extracted from `degacsid-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.5,0,0.2,1)`)**: Governs interactive state transitions across `<header.cls-1>` and `<div.navkkwuna-lbl>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — DEGACSID                                   │
│ ====================================================================== │
│ [ <header.cls-1>           | ▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STU ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.navkkwuna-mi>                                   |   │
│ | H1: DEGACSID                                                     |   │
│ | Substrate: #fffcf9    | Ink: #E55655    | Accent: #E55655        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.navkkwuna-lbl>       ) max-w: none (full-ble |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.cls-1>] -> [<div.navkkwuna-mi>] -> [<div.navkkwuna-lbl] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer>              ) | https://degacsid.com/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.cls-1> — `degacsid-com`)**:
   - Landmark `<header class="cls-1">` hosting `DEGACSID` navigation (`▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`), DOM attributes (`data-name="Layer 1"`), and stylesheet rule `font-face { font-family:Return of the Boss;src:url(/fonts/ReturnOfTheBoss.ttf) forma... }`.
2. **Hero Stage & Focal Lead (<div.navkkwuna-mi> — `DEGACSID`)**:
   - Landmark `<div class="navkkwuna-mi">` presenting display lead `DEGACSID` and copy excerpt *"← Back to the room"* over `#fffcf9` canvas and `#E55655` ink.
3. **Primary Showcase & Content Grid (<div.navkkwuna-lbl> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="navkkwuna-lbl">` rendering section `Featured Work & Interactive Showcase` with copy *"DEGACSID"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `main-D5gnYzr4.js`), and grid rule `root { margin:0;padding:0;width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<div.navkkwuna-arw> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="navkkwuna-arw">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#E55655` surface cards, `#E55655` accents, and `body { background:fffcf9;overflow:hidden;-webkit-font-smoothing:antialiased }`.
5. **Colophon & Global Directory Footer (<footer> — `https://degacsid.com/`)**:
   - Landmark `<footer>` landmark anchoring `DEGACSID` footer links (`▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`), copy *"Technical Architecture & Narrative"*, and `#E55655` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: degacsid-com (DEGACSID)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `degacsid-com` (**DEGACSID** — `https://degacsid.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fffcf9` / `#E55655`).
- **Identity & Domain Context**: The Only Creative Partner You'll Need. Full Service Creative Agency that handles everything from strategy, conception, design, execution,...
- **Primary Substrate**: `#fffcf9` (`body { background: #fffcf9 }`), **Primary Ink**: `#E55655`, **Accent / Highlight**: `#E55655`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fffcf9` (`body { background: #fffcf9 }`) paired with `#E55655` primary typography and `#E55655` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Return of the Boss` for display copy (`DEGACSID`) with `Crimson Text` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `none (full-bleed `100%` viewport stage)` container bounds (`gap: 12px`, padding `10px`) with `cubic-bezier(0.5,0,0.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `degacsid-com` in your global stylesheet:

:root {
  /* DEGACSID (degacsid-com) — Ground-Truth Extracted CSS Variables */
  --crt-safe: 31px; /* Dimension / Scale Token (degacsid-com) */
  --degacsid-com-bg: #fffcf9; /* Canvas Substrate (from `body { background: #fffcf9 }`) (degacsid-com) */
  --degacsid-com-ink: #E55655; /* Primary Typography Ink (stylesheet-derived) (degacsid-com) */
  --degacsid-com-surface: #E55655; /* Surface Substrate (stylesheet-derived) (degacsid-com) */
  --degacsid-com-accent: #E55655; /* Interactive Accent (stylesheet-derived) (degacsid-com) */
  --degacsid-com-muted: #E55655; /* Secondary Ink (stylesheet-derived) (degacsid-com) */
  --degacsid-com-border: #E55655; /* Structural Border (stylesheet-derived) (degacsid-com) */
  --degacsid-com-container: none; /* Container Bound (stylesheet-derived) (degacsid-com) */
  --degacsid-com-gap: 12px; /* Grid Gutter (stylesheet-derived) (degacsid-com) */
  --degacsid-com-pad: 10px; /* Lateral Padding (stylesheet-derived) (degacsid-com) */
  --degacsid-com-ease: cubic-bezier(0.5,0,0.2,1); /* Primary Easing Function (degacsid-com) */
  --degacsid-com-radius: 50%; /* Corner Radius (stylesheet-derived) (degacsid-com) */
  --degacsid-com-fs-base: 11px; /* Observed Font Size Token (degacsid-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fffcf9` — grounded in `body { background: #fffcf9 }`
- **Primary Typography Ink**: `#FFF4E7` — grounded in `.navkkwuna-mi .navkkwuna-lbl { color: #FFF4E7 }`
- **Elevated Surface / Card Substrate**: `#E55655` — grounded in `.navkkwuna-mi .navkkwuna-arw { color: #E55655 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `none (full-bleed `100%` viewport stage)` extracted from `degacsid-com` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: no `@media` queries in static stylesheet (fluid viewport scaling)
- **Corner Radii**: `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Return of the Boss`
- **Body Font Stack**: `Crimson Text`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `degacsid-com` (`DEGACSID`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.cls-1> — `degacsid-com`)**:
   - DOM & Selectors: Landmark `<header class="cls-1">` hosting `DEGACSID` navigation (`▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`), DOM attributes (`data-name="Layer 1"`), and stylesheet rule `font-face { font-family:Return of the Boss;src:url(/fonts/ReturnOfTheBoss.ttf) forma... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.cls-1> — `degacsid-com`)` (`degacsid-com`) adapts across no `@media` queries in static stylesheet (fluid viewport scaling) with `cubic-bezier(0.5,0,0.2,1)`, `cubic-bezier(0.2,0.8,0.2,1)` transitions and links `▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`.
2. **Hero Stage & Focal Lead (<div.navkkwuna-mi> — `DEGACSID`)**:
   - DOM & Selectors: Landmark `<div class="navkkwuna-mi">` presenting display lead `DEGACSID` and copy excerpt *"← Back to the room"* over `#fffcf9` canvas and `#E55655` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fffcf9` background with `#E55655` headline `DEGACSID`.
3. **Primary Showcase & Content Grid (<div.navkkwuna-lbl> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<div class="navkkwuna-lbl">` rendering section `Featured Work & Interactive Showcase` with copy *"DEGACSID"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `main-D5gnYzr4.js`), and grid rule `root { margin:0;padding:0;width:100%;height:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.navkkwuna-lbl> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.navkkwuna-arw> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<div class="navkkwuna-arw">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#E55655` surface cards, `#E55655` accents, and `body { background:fffcf9;overflow:hidden;-webkit-font-smoothing:antialiased }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.navkkwuna-arw> — `Technical Architecture & Narrative`)` uses `50%`, `2px` radii, `#E55655` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer> — `https://degacsid.com/`)**:
   - DOM & Selectors: Landmark `<footer>` landmark anchoring `DEGACSID` footer links (`▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`), copy *"Technical Architecture & Narrative"*, and `#E55655` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer> — `https://degacsid.com/`)` aligns to `none (full-bleed `100%` viewport stage)` extracted from `degacsid-com` stylesheet with `10px` lateral canvas padding with `12px` grid gap and attributes (data-name="Layer 1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"← Back to the room"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.5,0,0.2,1)`, `cubic-bezier(0.2,0.8,0.2,1)`
- **Extracted Stylesheet Rules (`degacsid-com`)**:
- `font-face { font-family:Return of the Boss;src:url(/fonts/ReturnOfTheBoss.ttf) forma... }`
- `root { margin:0;padding:0;width:100%;height:100% }`
- `body { background:fffcf9;overflow:hidden;-webkit-font-smoothing:antialiased }`
- `canvas { display:block }`
- `button { font:inherit }`
- **Per-Selector Transition Rules**:
- **Selector `.navkkwuna-mi .navkkwuna-lbl`**: `transition: color .13s ease` extracted from `degacsid-com` stylesheet.
- **Selector `.navkkwuna-mi .navkkwuna-arw`**: `transition: opacity .15s ease, transform .15s ease` extracted from `degacsid-com` stylesheet.
- **Selector `style]`**: `transition: opacity 260ms` extracted from `degacsid-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.5,0,0.2,1)`)**: Governs interactive state transitions across `<header.cls-1>` and `<div.navkkwuna-lbl>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `degacsid-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
