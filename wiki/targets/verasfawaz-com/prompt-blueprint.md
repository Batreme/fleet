---
title: "UI Prompt Blueprint: verasfawaz-com"
date: 2026-11-15
target: "[[overview|verasfawaz-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#202426` / `#24292b`)"
---

# UI Design System & Master Generation Blueprint: verasfawaz-com

> **Véras Fawaz** (https://verasfawaz.com) — Véras Fawaz © 1993 - 2026

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/verasfawaz-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Véras Fawaz** (`https://verasfawaz.com`). Véras Fawaz © 1993 - 2026
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#202426` / `#24292b`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#202426` (`var(--ui-ink)` in `:root`) paired with `#fff` primary typography and `#24292b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Studio Mono` for display copy (`Véras Fawaz`) with `Studio Sans` and `Studio Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `760px` container bounds (`gap: 4px`, padding `8px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/verasfawaz-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `760px` extracted from `verasfawaz-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `14%`, `2px`, `3px`, `65px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 760px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px),(pointer:coarse)`, `@media (max-width:700px)`, `@media (min-width:1000px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#202426` | `var(--ui-ink)` in `:root` |
| **Primary Typography Ink** | `#575e61` | `var(--ui-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f7f7f2` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#24292b` | `var(--panel-ink)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--detail-paper)` in `:root` |
| **Structural Hairline Border** | `#202020` | `var(--detail-ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--project-scroll-progress` | `inherit` | Design System Custom Token |
| `--window-milk` | `rgba(255,255,255,.68)` | Color / Atmospheric Token |
| `--media-vignette` | `1` | Design System Custom Token |
| `--media-text-opacity` | `1` | Typography Ink Token |
| `--media-arrow-opacity` | `1` | Design System Custom Token |
| `--project-header-fill` | `0!important` | Layout / Spatial Grid Token |
| `--type-sans` | `"Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--type-mono` | `"Studio Mono",monospace` | Typography / Scale Token |
| `--ui-font` | `var(--type-sans)` | Typography / Scale Token |
| `--ui-action` | `15px` | Dimension / Scale Token |
| `--ui-meta` | `12px` | Dimension / Scale Token |
| `--ui-title` | `32px` | Dimension / Scale Token |
| `--site-edge` | `32px` | Dimension / Scale Token |
| `--panel-pad` | `24px` | Layout / Spatial Grid Token |
| `--content-width` | `1000px` | Layout / Spatial Grid Token |
| `--ui-blur` | `24px` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Studio Mono`.
- **Primary Body Stack**: `Studio Sans`.
- **Technical / Metadata Stack**: `Studio Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--ui-title)`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 22px!important`, `line-height: 1.2!important`).
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: CSS variables `--type-mono: "Studio Mono",monospace`, `--ui-meta: 12px`, `--meta: 13px`; rule `small` (`letter-spacing: 0`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `e):not(#project-flow-unused)>head...`**: `transition: none!important` extracted from `verasfawaz-com` stylesheet.
- **Selector `rolling:has(#detail[open]) .vinyl...`**: `transition: none!important` extracted from `verasfawaz-com` stylesheet.
- **Selector `html.project-entry-reveal::after`**: `transition: opacity 320ms ease` extracted from `verasfawaz-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.studio-power-pending>` and `<section.studio-ui>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Véras Fawaz                                │
│ ====================================================================== │
│ [ <header.studio-power-pen | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.temporary-panel>                            |   │
│ | H1: Véras Fawaz                                                  |   │
│ | Substrate: #202426    | Ink: #fff       | Accent: #24292b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.studio-ui>       ) max-w: 760px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Skip to the archive          |  | Studio opnieuw laden         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px   ) | │
│ | [<header.studio-pow] -> [<section.temporary] -> [<section.studio-ui] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.context-footer) | https://verasfawaz.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.studio-power-pending> — `verasfawaz-com`)**:
   - Landmark `<header class="studio-power-pending">` hosting `Véras Fawaz` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-studio-ready="true"`, `data-arrival="waiting"`, `data-arrival-navigation="visible"`, `data-arrival-from="night"`), and stylesheet rule `before { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.temporary-panel> — `Véras Fawaz`)**:
   - Landmark `<section class="temporary-panel">` presenting display lead `Véras Fawaz` and copy excerpt *"Skip to the archive"* over `#202426` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.studio-ui> — `Skip to the archive`)**:
   - Landmark `<section class="studio-ui">` rendering section `Skip to the archive` with copy *"Studio opnieuw laden"*, asset references (`packs.js`, `wide-blackout.webp`, `startup-input-game-exit-20261018.js`, `apple-touch-icon.png`), and grid rule `header::after { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.compact-music-ui> — `Studio opnieuw laden`)**:
   - Landmark `<section class="compact-music-ui">` framing `Studio opnieuw laden` and `PLEASE TOUCH EVERYTHING` (*"PLEASE TOUCH EVERYTHING"*) with `#f7f7f2` surface cards, `#24292b` accents, and `header { background:none!important }`.
5. **Colophon & Global Directory Footer (<footer.context-footer-ui> — `https://verasfawaz.com`)**:
   - Landmark `<footer class="context-footer-ui">` anchoring `Véras Fawaz` footer links (`Overview · Index · Archive · About · Contact`), copy *"View record & tracks"*, and `#202020` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: verasfawaz-com (Véras Fawaz)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `verasfawaz-com` (**Véras Fawaz** — `https://verasfawaz.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#202426` / `#24292b`).
- **Identity & Domain Context**: Véras Fawaz © 1993 - 2026
- **Primary Substrate**: `#202426` (`var(--ui-ink)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#24292b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#202426` (`var(--ui-ink)` in `:root`) paired with `#fff` primary typography and `#24292b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Studio Mono` for display copy (`Véras Fawaz`) with `Studio Sans` and `Studio Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `760px` container bounds (`gap: 4px`, padding `8px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `verasfawaz-com` in your global stylesheet:

:root {
  /* Véras Fawaz (verasfawaz-com) — Ground-Truth Extracted CSS Variables */
  --project-scroll-progress: inherit; /* Design System Custom Token (verasfawaz-com) */
  --window-milk: rgba(255,255,255,.68); /* Color / Atmospheric Token (verasfawaz-com) */
  --media-vignette: 1; /* Design System Custom Token (verasfawaz-com) */
  --media-text-opacity: 1; /* Typography Ink Token (verasfawaz-com) */
  --media-arrow-opacity: 1; /* Design System Custom Token (verasfawaz-com) */
  --project-header-fill: 0!important; /* Layout / Spatial Grid Token (verasfawaz-com) */
  --type-sans: "Helvetica Neue",Helvetica,Arial,sans-serif; /* Typography / Scale Token (verasfawaz-com) */
  --type-mono: "Studio Mono",monospace; /* Typography / Scale Token (verasfawaz-com) */
  --ui-font: var(--type-sans); /* Typography / Scale Token (verasfawaz-com) */
  --ui-action: 15px; /* Dimension / Scale Token (verasfawaz-com) */
  --ui-meta: 12px; /* Dimension / Scale Token (verasfawaz-com) */
  --ui-title: 32px; /* Dimension / Scale Token (verasfawaz-com) */
  --site-edge: 32px; /* Dimension / Scale Token (verasfawaz-com) */
  --panel-pad: 24px; /* Layout / Spatial Grid Token (verasfawaz-com) */
  --content-width: 1000px; /* Layout / Spatial Grid Token (verasfawaz-com) */
  --ui-blur: 24px; /* Elevation / Border Token (verasfawaz-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#202426` — grounded in `var(--ui-ink)` in `:root`
- **Primary Typography Ink**: `#575e61` — grounded in `var(--ui-muted)` in `:root`
- **Elevated Surface / Card Substrate**: `#f7f7f2` — grounded in `var(--paper)` in `:root`
- **Interactive Accent / Highlight**: `#24292b` — grounded in `var(--panel-ink)` in `:root`
- **Secondary / Muted Copy**: `#fff` — grounded in `var(--detail-paper)` in `:root`
- **Structural Hairline Border**: `#202020` — grounded in `var(--detail-ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `760px` extracted from `verasfawaz-com` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 760px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px),(pointer:coarse)`, `@media (max-width:700px)`, `@media (min-width:1000px)`
- **Corner Radii**: `14%`, `2px`, `3px`, `65px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Studio Mono`
- **Body Font Stack**: `Studio Sans`
- **Monospace / Technical Font Stack**: `Studio Mono`
- **H1 Display Rule**: rule `h1` (`font-size: var(--ui-title)`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: 22px!important`, `line-height: 1.2!important`)
- **Body Copy Rule**: rule `p` (`font-size: 16px`, `line-height: 1.5`)
- **Metadata & Index Rule**: CSS variables `--type-mono: "Studio Mono",monospace`, `--ui-meta: 12px`, `--meta: 13px`; rule `small` (`letter-spacing: 0`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `verasfawaz-com` (`Véras Fawaz`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.studio-power-pending> — `verasfawaz-com`)**:
   - DOM & Selectors: Landmark `<header class="studio-power-pending">` hosting `Véras Fawaz` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-studio-ready="true"`, `data-arrival="waiting"`, `data-arrival-navigation="visible"`, `data-arrival-from="night"`), and stylesheet rule `before { display:none!important }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.studio-power-pending> — `verasfawaz-com`)` (`verasfawaz-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px),(pointer:coarse)`, `@media (max-width:700px)`, `@media (min-width:1000px)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.temporary-panel> — `Véras Fawaz`)**:
   - DOM & Selectors: Landmark `<section class="temporary-panel">` presenting display lead `Véras Fawaz` and copy excerpt *"Skip to the archive"* over `#202426` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#202426` background with `#fff` headline `Véras Fawaz`.
3. **Primary Showcase & Content Grid (<section.studio-ui> — `Skip to the archive`)**:
   - DOM & Selectors: Landmark `<section class="studio-ui">` rendering section `Skip to the archive` with copy *"Studio opnieuw laden"*, asset references (`packs.js`, `wide-blackout.webp`, `startup-input-game-exit-20261018.js`, `apple-touch-icon.png`), and grid rule `header::after { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.studio-ui> — `Skip to the archive`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 760px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.compact-music-ui> — `Studio opnieuw laden`)**:
   - DOM & Selectors: Landmark `<section class="compact-music-ui">` framing `Studio opnieuw laden` and `PLEASE TOUCH EVERYTHING` (*"PLEASE TOUCH EVERYTHING"*) with `#f7f7f2` surface cards, `#24292b` accents, and `header { background:none!important }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.compact-music-ui> — `Studio opnieuw laden`)` uses `14%`, `2px`, `3px`, `65px` radii, `#24292b` highlights, and assets (packs.js, wide-blackout.webp, startup-input-game-exit-20261018.js).
5. **Colophon & Global Directory Footer (<footer.context-footer-ui> — `https://verasfawaz.com`)**:
   - DOM & Selectors: Landmark `<footer class="context-footer-ui">` anchoring `Véras Fawaz` footer links (`Overview · Index · Archive · About · Contact`), copy *"View record & tracks"*, and `#202020` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.context-footer-ui> — `https://verasfawaz.com`)` aligns to `760px` extracted from `verasfawaz-com` stylesheet with `8px` lateral canvas padding with `4px` grid gap and attributes (data-studio-ready="true", data-arrival="waiting", data-arrival-navigation="visible").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to the archive"*
- Copy Excerpt 2: *"Studio opnieuw laden"*
- Copy Excerpt 3: *"PLEASE TOUCH EVERYTHING"*
- Copy Excerpt 4: *"View record & tracks"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`verasfawaz-com`)**:
- `before { display:none!important }`
- `header::after { display:none!important }`
- `header { background:none!important }`
- `.vinyl-play-hint { opacity:calc(var(--context-chrome-opacity,1) * var(--media-text-opacity,... }`
- `html.project-entry-cover::after { content:"";position:fixed;inset:0;background:000;z-index:2147483646;poin... }`
- **Per-Selector Transition Rules**:
- **Selector `e):not(#project-flow-unused)>head...`**: `transition: none!important` extracted from `verasfawaz-com` stylesheet.
- **Selector `rolling:has(#detail[open]) .vinyl...`**: `transition: none!important` extracted from `verasfawaz-com` stylesheet.
- **Selector `html.project-entry-reveal::after`**: `transition: opacity 320ms ease` extracted from `verasfawaz-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.studio-power-pending>` and `<section.studio-ui>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `verasfawaz-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
