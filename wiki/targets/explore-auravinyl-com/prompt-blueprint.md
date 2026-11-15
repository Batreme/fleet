---
title: "UI Prompt Blueprint: explore-auravinyl-com"
date: 2026-11-15
target: "[[overview|explore-auravinyl-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#1e1e1e`)"
---

# UI Design System & Master Generation Blueprint: explore-auravinyl-com

> **Aura Vinyl Color Explorer** (https://explore.auravinyl.com) — Explore over 500 colors across matte, satin, and gloss finishes from Aura Premium Vinyl. Find vinyl wrap ideas and inspiration.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/explore-auravinyl-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Aura Vinyl Color Explorer** (`https://explore.auravinyl.com`). Explore over 500 colors across matte, satin, and gloss finishes from Aura Premium Vinyl. Find vinyl wrap ideas and inspiration.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#1e1e1e`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0a0a0a` (`var(--bg)` in `:root`) paired with `#404040` primary typography and `#1e1e1e` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Arctic Fire`) with `Geist Mono` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `900px` container bounds (`gap: 12px`, padding `20px`) with `cubic-bezier(.215,.61,.355,1)` easing and Barba.js Page Transition Router, HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/explore-auravinyl-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `900px` extracted from `explore-auravinyl-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `6px`, `var(--radius-pill)`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 900px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:901px)`, `@media (max-width:560px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#161616` | `var(--bg-raised)` in `:root` |
| **Elevated Surface / Card Substrate** | `#050505` | `var(--bg-sunken)` in `:root` |
| **Interactive Accent / Highlight** | `#1e1e1e` | `var(--raised)` in `:root` |
| **Secondary / Muted Copy** | `#262626` | `var(--line)` in `:root` |
| **Structural Hairline Border** | `#404040` | `var(--line-steel)` in `:root` |
| **Variable Token (`--line-strong`)** | `#6b6b6b` | `var(--line-strong)` in `:root` |
| **Variable Token (`--text`)** | `#f5f5f5` | `var(--text)` in `:root` |
| **Variable Token (`--text-2`)** | `#a3a3a3` | `var(--text-2)` in `:root` |
| **Variable Token (`--text-3`)** | `#808080` | `var(--text-3)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--enter-at` | `1100ms` | Motion / Timing Token |
| `--enter-from` | `48px 0` | Dimension / Scale Token |
| `--enter-order` | `1` | Design System Custom Token |
| `--ease-pull` | `cubic-bezier(.215, .61, .355, 1)` | Motion / Easing Token |
| `--ease-pull-back` | `cubic-bezier(.645, .045, .355, 1)` | Motion / Easing Token |
| `--under` | `0px` | Dimension / Scale Token |
| `--bg` | `#0a0a0a` | Canvas / Surface Token |
| `--bg-raised` | `#161616` | Canvas / Surface Token |
| `--bg-sunken` | `#050505` | Canvas / Surface Token |
| `--raised` | `#1e1e1e` | Color / Atmospheric Token |
| `--line` | `#262626` | Color / Atmospheric Token |
| `--line-steel` | `#404040` | Color / Atmospheric Token |
| `--line-strong` | `#6b6b6b` | Color / Atmospheric Token |
| `--text` | `#f5f5f5` | Typography Ink Token |
| `--text-2` | `#a3a3a3` | Typography Ink Token |
| `--text-3` | `#808080` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Geist Mono`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.title` (`font-size: 18px`, `line-height: 1.1`, `letter-spacing: -.02em`, `font-weight: 800`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `18px`, `12px`, `10px`, `16px`).
- **Body Copy**: rule `.body` (`font-size: 13px`, `line-height: 1.5`, `font-weight: 500`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: "Geist Mono", ui-monospace, monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.FormDialog`**: `transition: opacity var(--dur-fast) var(--ease-standard),visibility 0s lin...` extracted from `explore-auravinyl-com` stylesheet.
- **Selector `.FormDialog.on`**: `transition: opacity var(--dur-fast) var(--ease-standard),visibility 0s` extracted from `explore-auravinyl-com` stylesheet.
- **Selector `.FormDialog .panel`**: `transition: transform var(--dur-fast) var(--ease-standard)` extracted from `explore-auravinyl-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.head>` and `<section.card>`.
- **Runtime Interaction Engine**: Integrates Barba.js Page Transition Router, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Aura Vinyl Color Explorer                  │
│ ====================================================================== │
│ [ <header.head>            | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.mbar>                                       |   │
│ | H1: Arctic Fire                                                  |   │
│ | Substrate: #0a0a0a    | Ink: #404040    | Accent: #1e1e1e        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.card>            ) max-w: 900px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | No color                     |  | Reference                    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.head>] -> [<section.mbar>] -> [<section.card>] |            │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shell>        ) | https://explore.auravinyl.com      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.head> — `explore-auravinyl-com`)**:
   - Landmark `<header class="head">` hosting `Aura Vinyl Color Explorer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-perma="ultra-gloss-laguna-blue"`, `data-perma="ultra-gloss-white-pri..."`, `data-perma="ultra-gloss-laguna-blue"`), and stylesheet rule `.FormDialog.on { visibility:visible;opacity:1;pointer-events:auto;transition:opacity var(... }`.
2. **Hero Stage & Focal Lead (<section.mbar> — `Arctic Fire`)**:
   - Landmark `<section class="mbar">` presenting display lead `Arctic Fire` and copy excerpt *"Please enable javascript"* over `#0a0a0a` canvas and `#404040` ink.
3. **Primary Showcase & Content Grid (<section.card> — `No color`)**:
   - Landmark `<section class="card">` rendering section `No color` with copy *"Paint Metallic 190"*, asset references (`favicon.svg`, `180.png`, `152.png`, `167.png`), and grid rule `.FormDialog { padding:10px }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Reference`)**:
   - Landmark `<section class="sec">` framing `Reference` and `Material` (*"White Prismatic Chrome"*) with `#050505` surface cards, `#1e1e1e` accents, and `.FormDialog .backdrop { position:absolute;inset:0;background:rgba(5,5,5,.8) }`.
5. **Colophon & Global Directory Footer (<footer.shell> — `https://explore.auravinyl.com`)**:
   - Landmark `<footer class="shell">` anchoring `Aura Vinyl Color Explorer` footer links (`Overview · Index · Archive · About · Contact`), copy *"Ultra Gloss / Chrome"*, and `#404040` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: explore-auravinyl-com (Aura Vinyl Color Explorer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `explore-auravinyl-com` (**Aura Vinyl Color Explorer** — `https://explore.auravinyl.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#1e1e1e`).
- **Identity & Domain Context**: Explore over 500 colors across matte, satin, and gloss finishes from Aura Premium Vinyl. Find vinyl wrap ideas and inspiration.
- **Primary Substrate**: `#0a0a0a` (`var(--bg)` in `:root`), **Primary Ink**: `#404040`, **Accent / Highlight**: `#1e1e1e`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0a0a0a` (`var(--bg)` in `:root`) paired with `#404040` primary typography and `#1e1e1e` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Arctic Fire`) with `Geist Mono` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `900px` container bounds (`gap: 12px`, padding `20px`) with `cubic-bezier(.215,.61,.355,1)` easing and Barba.js Page Transition Router, HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `explore-auravinyl-com` in your global stylesheet:

:root {
  /* Aura Vinyl Color Explorer (explore-auravinyl-com) — Ground-Truth Extracted CSS Variables */
  --enter-at: 1100ms; /* Motion / Timing Token (explore-auravinyl-com) */
  --enter-from: 48px 0; /* Dimension / Scale Token (explore-auravinyl-com) */
  --enter-order: 1; /* Design System Custom Token (explore-auravinyl-com) */
  --ease-pull: cubic-bezier(.215, .61, .355, 1); /* Motion / Easing Token (explore-auravinyl-com) */
  --ease-pull-back: cubic-bezier(.645, .045, .355, 1); /* Motion / Easing Token (explore-auravinyl-com) */
  --under: 0px; /* Dimension / Scale Token (explore-auravinyl-com) */
  --bg: #0a0a0a; /* Canvas / Surface Token (explore-auravinyl-com) */
  --bg-raised: #161616; /* Canvas / Surface Token (explore-auravinyl-com) */
  --bg-sunken: #050505; /* Canvas / Surface Token (explore-auravinyl-com) */
  --raised: #1e1e1e; /* Color / Atmospheric Token (explore-auravinyl-com) */
  --line: #262626; /* Color / Atmospheric Token (explore-auravinyl-com) */
  --line-steel: #404040; /* Color / Atmospheric Token (explore-auravinyl-com) */
  --line-strong: #6b6b6b; /* Color / Atmospheric Token (explore-auravinyl-com) */
  --text: #f5f5f5; /* Typography Ink Token (explore-auravinyl-com) */
  --text-2: #a3a3a3; /* Typography Ink Token (explore-auravinyl-com) */
  --text-3: #808080; /* Typography Ink Token (explore-auravinyl-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0a0a0a` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#161616` — grounded in `var(--bg-raised)` in `:root`
- **Elevated Surface / Card Substrate**: `#050505` — grounded in `var(--bg-sunken)` in `:root`
- **Interactive Accent / Highlight**: `#1e1e1e` — grounded in `var(--raised)` in `:root`
- **Secondary / Muted Copy**: `#262626` — grounded in `var(--line)` in `:root`
- **Structural Hairline Border**: `#404040` — grounded in `var(--line-steel)` in `:root`
- **Variable Token (`--line-strong`)**: `#6b6b6b` — grounded in `var(--line-strong)` in `:root`
- **Variable Token (`--text`)**: `#f5f5f5` — grounded in `var(--text)` in `:root`
- **Variable Token (`--text-2`)**: `#a3a3a3` — grounded in `var(--text-2)` in `:root`
- **Variable Token (`--text-3`)**: `#808080` — grounded in `var(--text-3)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `900px` extracted from `explore-auravinyl-com` stylesheet
- **Padding & Gutters**: `20px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 900px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:901px)`, `@media (max-width:560px)`
- **Corner Radii**: `6px`, `var(--radius-pill)`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: rule `.title` (`font-size: 18px`, `line-height: 1.1`, `letter-spacing: -.02em`, `font-weight: 800`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `18px`, `12px`, `10px`, `16px`)
- **Body Copy Rule**: rule `.body` (`font-size: 13px`, `line-height: 1.5`, `font-weight: 500`)
- **Metadata & Index Rule**: CSS variables `--font-mono: "Geist Mono", ui-monospace, monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `explore-auravinyl-com` (`Aura Vinyl Color Explorer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.head> — `explore-auravinyl-com`)**:
   - DOM & Selectors: Landmark `<header class="head">` hosting `Aura Vinyl Color Explorer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-perma="ultra-gloss-laguna-blue"`, `data-perma="ultra-gloss-white-pri..."`, `data-perma="ultra-gloss-laguna-blue"`), and stylesheet rule `.FormDialog.on { visibility:visible;opacity:1;pointer-events:auto;transition:opacity var(... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.head> — `explore-auravinyl-com`)` (`explore-auravinyl-com`) adapts across `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:901px)`, `@media (max-width:560px)` with `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.mbar> — `Arctic Fire`)**:
   - DOM & Selectors: Landmark `<section class="mbar">` presenting display lead `Arctic Fire` and copy excerpt *"Please enable javascript"* over `#0a0a0a` canvas and `#404040` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0a0a0a` background with `#404040` headline `Arctic Fire`.
3. **Primary Showcase & Content Grid (<section.card> — `No color`)**:
   - DOM & Selectors: Landmark `<section class="card">` rendering section `No color` with copy *"Paint Metallic 190"*, asset references (`favicon.svg`, `180.png`, `152.png`, `167.png`), and grid rule `.FormDialog { padding:10px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.card> — `No color`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 900px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Reference`)**:
   - DOM & Selectors: Landmark `<section class="sec">` framing `Reference` and `Material` (*"White Prismatic Chrome"*) with `#050505` surface cards, `#1e1e1e` accents, and `.FormDialog .backdrop { position:absolute;inset:0;background:rgba(5,5,5,.8) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sec> — `Reference`)` uses `6px`, `var(--radius-pill)`, `50%`, `2px` radii, `#1e1e1e` highlights, and assets (favicon.svg, 180.png, 152.png).
5. **Colophon & Global Directory Footer (<footer.shell> — `https://explore.auravinyl.com`)**:
   - DOM & Selectors: Landmark `<footer class="shell">` anchoring `Aura Vinyl Color Explorer` footer links (`Overview · Index · Archive · About · Contact`), copy *"Ultra Gloss / Chrome"*, and `#404040` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shell> — `https://explore.auravinyl.com`)` aligns to `900px` extracted from `explore-auravinyl-com` stylesheet with `20px` lateral canvas padding with `12px` grid gap and attributes (data-perma="ultra-gloss-laguna-blue", data-perma="ultra-gloss-white-pri...", data-perma="ultra-gloss-laguna-blue").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Please enable javascript"*
- Copy Excerpt 2: *"Paint Metallic 190"*
- Copy Excerpt 3: *"White Prismatic Chrome"*
- Copy Excerpt 4: *"Ultra Gloss / Chrome"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`explore-auravinyl-com`)**:
- `.FormDialog.on { visibility:visible;opacity:1;pointer-events:auto;transition:opacity var(... }`
- `.FormDialog { padding:10px }`
- `.FormDialog .backdrop { position:absolute;inset:0;background:rgba(5,5,5,.8) }`
- `.FormDialog .trap { position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(5... }`
- `.FormDialog .panel { max-width:none;padding:20px }`
- **Per-Selector Transition Rules**:
- **Selector `.FormDialog`**: `transition: opacity var(--dur-fast) var(--ease-standard),visibility 0s lin...` extracted from `explore-auravinyl-com` stylesheet.
- **Selector `.FormDialog.on`**: `transition: opacity var(--dur-fast) var(--ease-standard),visibility 0s` extracted from `explore-auravinyl-com` stylesheet.
- **Selector `.FormDialog .panel`**: `transition: transform var(--dur-fast) var(--ease-standard)` extracted from `explore-auravinyl-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.head>` and `<section.card>`.
- **Runtime Interaction Engine**: Integrates Barba.js Page Transition Router, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `explore-auravinyl-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
