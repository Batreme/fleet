---
title: "UI Prompt Blueprint: thesovietflip-com"
date: 2026-11-15
target: "[[overview|thesovietflip-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#0f0f0c` canvas, `#fff0d3` ink, `#fff0d3` accent)"
---

# UI Design System & Master Generation Blueprint: thesovietflip-com

> **The Soviet Flip** (https://thesovietflip.com/) — A visual historical research project about the Cold War, Israel, the USSR, and the rise of modern Palestinian identity, with archival sou...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/thesovietflip-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Soviet Flip** (`https://thesovietflip.com/`). A visual historical research project about the Cold War, Israel, the USSR, and the rise of modern Palestinian identity, with archival sou...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#0f0f0c` canvas, `#fff0d3` ink, `#fff0d3` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0f0f0c` (`var(--ink)` in `:root`) paired with `#fff0d3` primary typography and `#fff0d3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jost` for display copy (`The Soviet Flip`) with `Stalinist One` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `65px` container bounds (`gap: 8px`, padding `10px`) with `cubic-bezier(.2,.8,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/thesovietflip-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `65px` extracted from `thesovietflip-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `18px`, `50%`, `4px`, `28px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 65px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=480px)`, `@media (width<=600px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0f0f0c` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#ebe5d6` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#903c32` | `var(--red)` in `:root` |
| **Interactive Accent / Highlight** | `#fff0d3` | `:hover { color: #fff0d3 }` |
| **Secondary / Muted Copy** | `#dba181` | `:first-child { color: #dba181 }` |
| **Structural Hairline Border** | `#b5634f` | `::-webkit-slider-runnable-track { background: #b5634f }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0f0f0c` | Typography Ink Token |
| `--paper` | `#ebe5d6` | Canvas / Surface Token |
| `--red` | `#903c32` | Color / Atmospheric Token |
| `--site-cursor` | `url(/cursors/arrow.png),auto` | Design System Custom Token |
| `--link-cursor` | `url(/cursors/magnifier.png),pointer` | Typography Ink Token |
| `--map-heading-font` | `"Russo One",sans-serif` | Typography Ink Token |
| `--map-heading-weight` | `400` | Typography Ink Token |
| `--map-body-font` | `"Jost",sans-serif` | Typography / Scale Token |
| `--drawer-side` | `1` | Design System Custom Token |
| `--drawer-progress` | `0` | Design System Custom Token |
| `--peek` | `0px` | Dimension / Scale Token |
| `--ribbon-tail` | `24px` | Dimension / Scale Token |
| `--bookmark-width` | `88px!important` | Layout / Spatial Grid Token |
| `--listener-shift` | `18px` | Dimension / Scale Token |
| `--progress` | `0%` | Dimension / Scale Token |
| `--initial-transform` | `none` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Jost`.
- **Primary Body Stack**: `Stalinist One`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`).
- **Body Copy**: CSS variables `--map-body-font: "Jost",sans-serif`; rule `p` (`line-height: 1.2!important`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.45,0,.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `:after`**: `transition: .01ms!important` extracted from `thesovietflip-com` stylesheet.
- **Selector `.story-map-drawer[data-astro-cid-...`**: `transition: transform .38s cubic-bezier(.2,.8,.2,1)` extracted from `thesovietflip-com` stylesheet.
- **Selector `-drawer[data-astro-cid-ikck2sju]....`**: `transition: .32s` extracted from `thesovietflip-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.motion-enabled>` and `<section.reading-block>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.reading-view>` and `<section.reading-block>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Soviet Flip                            │
│ ====================================================================== │
│ [ <header.motion-enabled>  | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.reading-view>                               |   │
│ | H1: The Soviet Flip                                              |   │
│ | Substrate: #0f0f0c    | Ink: #fff0d3    | Accent: #fff0d3        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.reading-block>   ) max-w: 65px           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | האזנה רציפה                  |  | info@thesovietflip.com       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<header.motion-ena] -> [<section.reading-v] -> [<section.reading-b] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.book-turning-p) | https://thesovietflip.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.motion-enabled> — `thesovietflip-com`)**:
   - Landmark `<header class="motion-enabled">` hosting `The Soviet Flip` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-astro-transition-scope="astro-yztbsuuz-1"`, `data-astro-cid-ju4pidww`, `data-astro-rerun`, `data-astro-exec`), and stylesheet rule `root { color-scheme:dark;--ink:0f0f0c;--paper:ebe5d6;--red:903c32 }`.
2. **Hero Stage & Focal Lead (<section.reading-view> — `The Soviet Flip`)**:
   - Landmark `<section class="reading-view">` presenting display lead `The Soviet Flip` and copy excerpt *"For source corrections, archival material, licensing questions, o"* over `#0f0f0c` canvas and `#fff0d3` ink.
3. **Primary Showcase & Content Grid (<section.reading-block> — `האזנה רציפה`)**:
   - Landmark `<section class="reading-block">` rendering section `האזנה רציפה` with copy *"info@thesovietflip.com"*, asset references (`ae304b70d9495a89f84a.woff2`, `cca183354fd3fefb84fd.woff2`, `2b5199f9f43249f2ad78.webp`, `3118562a4483c1224195.webp`), and grid rule `html { scroll-behavior:smooth;background:var(--ink);-webkit-text-size-adjust:10... }`.
4. **Interactive Detail & Feature Matrix (<section.reading-block> — `info@thesovietflip.com`)**:
   - Landmark `<section class="reading-block">` framing `info@thesovietflip.com` and `© 2026 The Soviet Flip. All rights reserved. All` (*"© 2026 The Soviet Flip. All rights reserved. All content, researc"*) with `#903c32` surface cards, `#fff0d3` accents, and `body { color:var(--paper);background:var(--ink);margin:0;font-family:Assistant,... }`.
5. **Colophon & Global Directory Footer (<footer.book-turning-page> — `https://thesovietflip.com/`)**:
   - Landmark `<footer class="book-turning-page">` anchoring `The Soviet Flip` footer links (`Overview · Index · Archive · About · Contact`), copy *"S o v i e t F l i p"*, and `#b5634f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thesovietflip-com (The Soviet Flip)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thesovietflip-com` (**The Soviet Flip** — `https://thesovietflip.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0f0f0c` canvas, `#fff0d3` ink, `#fff0d3` accent).
- **Identity & Domain Context**: A visual historical research project about the Cold War, Israel, the USSR, and the rise of modern Palestinian identity, with archival sou...
- **Primary Substrate**: `#0f0f0c` (`var(--ink)` in `:root`), **Primary Ink**: `#fff0d3`, **Accent / Highlight**: `#fff0d3`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0f0f0c` (`var(--ink)` in `:root`) paired with `#fff0d3` primary typography and `#fff0d3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jost` for display copy (`The Soviet Flip`) with `Stalinist One` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `65px` container bounds (`gap: 8px`, padding `10px`) with `cubic-bezier(.2,.8,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thesovietflip-com` in your global stylesheet:

:root {
  /* The Soviet Flip (thesovietflip-com) — Ground-Truth Extracted CSS Variables */
  --ink: #0f0f0c; /* Typography Ink Token (thesovietflip-com) */
  --paper: #ebe5d6; /* Canvas / Surface Token (thesovietflip-com) */
  --red: #903c32; /* Color / Atmospheric Token (thesovietflip-com) */
  --site-cursor: url(/cursors/arrow.png),auto; /* Design System Custom Token (thesovietflip-com) */
  --link-cursor: url(/cursors/magnifier.png),pointer; /* Typography Ink Token (thesovietflip-com) */
  --map-heading-font: "Russo One",sans-serif; /* Typography Ink Token (thesovietflip-com) */
  --map-heading-weight: 400; /* Typography Ink Token (thesovietflip-com) */
  --map-body-font: "Jost",sans-serif; /* Typography / Scale Token (thesovietflip-com) */
  --drawer-side: 1; /* Design System Custom Token (thesovietflip-com) */
  --drawer-progress: 0; /* Design System Custom Token (thesovietflip-com) */
  --peek: 0px; /* Dimension / Scale Token (thesovietflip-com) */
  --ribbon-tail: 24px; /* Dimension / Scale Token (thesovietflip-com) */
  --bookmark-width: 88px!important; /* Layout / Spatial Grid Token (thesovietflip-com) */
  --listener-shift: 18px; /* Dimension / Scale Token (thesovietflip-com) */
  --progress: 0%; /* Dimension / Scale Token (thesovietflip-com) */
  --initial-transform: none; /* Design System Custom Token (thesovietflip-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0f0f0c` — grounded in `var(--ink)` in `:root`
- **Primary Typography Ink**: `#ebe5d6` — grounded in `var(--paper)` in `:root`
- **Elevated Surface / Card Substrate**: `#903c32` — grounded in `var(--red)` in `:root`
- **Interactive Accent / Highlight**: `#fff0d3` — grounded in `:hover { color: #fff0d3 }`
- **Secondary / Muted Copy**: `#dba181` — grounded in `:first-child { color: #dba181 }`
- **Structural Hairline Border**: `#b5634f` — grounded in `::-webkit-slider-runnable-track { background: #b5634f }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `65px` extracted from `thesovietflip-com` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 65px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=480px)`, `@media (width<=600px)`
- **Corner Radii**: `18px`, `50%`, `4px`, `28px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Stalinist One`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`)
- **Body Copy Rule**: CSS variables `--map-body-font: "Jost",sans-serif`; rule `p` (`line-height: 1.2!important`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thesovietflip-com` (`The Soviet Flip`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.motion-enabled> — `thesovietflip-com`)**:
   - DOM & Selectors: Landmark `<header class="motion-enabled">` hosting `The Soviet Flip` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-astro-transition-scope="astro-yztbsuuz-1"`, `data-astro-cid-ju4pidww`, `data-astro-rerun`, `data-astro-exec`), and stylesheet rule `root { color-scheme:dark;--ink:0f0f0c;--paper:ebe5d6;--red:903c32 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.motion-enabled> — `thesovietflip-com`)` (`thesovietflip-com`) adapts across `@media (prefers-reduced-motion)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=480px)`, `@media (width<=600px)` with `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.45,0,.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.reading-view> — `The Soviet Flip`)**:
   - DOM & Selectors: Landmark `<section class="reading-view">` presenting display lead `The Soviet Flip` and copy excerpt *"For source corrections, archival material, licensing questions, o"* over `#0f0f0c` canvas and `#fff0d3` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0f0f0c` background with `#fff0d3` headline `The Soviet Flip`.
3. **Primary Showcase & Content Grid (<section.reading-block> — `האזנה רציפה`)**:
   - DOM & Selectors: Landmark `<section class="reading-block">` rendering section `האזנה רציפה` with copy *"info@thesovietflip.com"*, asset references (`ae304b70d9495a89f84a.woff2`, `cca183354fd3fefb84fd.woff2`, `2b5199f9f43249f2ad78.webp`, `3118562a4483c1224195.webp`), and grid rule `html { scroll-behavior:smooth;background:var(--ink);-webkit-text-size-adjust:10... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.reading-block> — `האזנה רציפה`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 65px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.reading-block> — `info@thesovietflip.com`)**:
   - DOM & Selectors: Landmark `<section class="reading-block">` framing `info@thesovietflip.com` and `© 2026 The Soviet Flip. All rights reserved. All` (*"© 2026 The Soviet Flip. All rights reserved. All content, researc"*) with `#903c32` surface cards, `#fff0d3` accents, and `body { color:var(--paper);background:var(--ink);margin:0;font-family:Assistant,... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.reading-block> — `info@thesovietflip.com`)` uses `18px`, `50%`, `4px`, `28px` radii, `#fff0d3` highlights, and assets (ae304b70d9495a89f84a.woff2, cca183354fd3fefb84fd.woff2, 2b5199f9f43249f2ad78.webp).
5. **Colophon & Global Directory Footer (<footer.book-turning-page> — `https://thesovietflip.com/`)**:
   - DOM & Selectors: Landmark `<footer class="book-turning-page">` anchoring `The Soviet Flip` footer links (`Overview · Index · Archive · About · Contact`), copy *"S o v i e t F l i p"*, and `#b5634f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.book-turning-page> — `https://thesovietflip.com/`)` aligns to `65px` extracted from `thesovietflip-com` stylesheet with `10px` lateral canvas padding with `8px` grid gap and attributes (data-astro-transition-scope="astro-yztbsuuz-1", data-astro-cid-ju4pidww, data-astro-rerun).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"For source corrections, archival material, licensing questions, or additional info..."*
- Copy Excerpt 2: *"info@thesovietflip.com"*
- Copy Excerpt 3: *"© 2026 The Soviet Flip. All rights reserved. All content, research, text, design,..."*
- Copy Excerpt 4: *"S o v i e t F l i p"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.45,0,.25,1)`
- **Extracted Stylesheet Rules (`thesovietflip-com`)**:
- `root { color-scheme:dark;--ink:0f0f0c;--paper:ebe5d6;--red:903c32 }`
- `html { scroll-behavior:smooth;background:var(--ink);-webkit-text-size-adjust:10... }`
- `body { color:var(--paper);background:var(--ink);margin:0;font-family:Assistant,... }`
- `input { font:inherit }`
- `focus-visible { outline:2px solid var(--paper);outline-offset:6px }`
- **Per-Selector Transition Rules**:
- **Selector `:after`**: `transition: .01ms!important` extracted from `thesovietflip-com` stylesheet.
- **Selector `.story-map-drawer[data-astro-cid-...`**: `transition: transform .38s cubic-bezier(.2,.8,.2,1)` extracted from `thesovietflip-com` stylesheet.
- **Selector `-drawer[data-astro-cid-ikck2sju]....`**: `transition: .32s` extracted from `thesovietflip-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.motion-enabled>` and `<section.reading-block>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.reading-view>` and `<section.reading-block>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thesovietflip-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
