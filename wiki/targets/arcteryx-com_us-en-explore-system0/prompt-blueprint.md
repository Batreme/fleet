---
title: "UI Prompt Blueprint: arcteryx-com_us-en-explore-system0"
date: 2026-11-15
target: "[[overview|arcteryx-com_us-en-explore-system0]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fdfdfd` canvas, `#0c0c0c` ink, `#565656` accent)"
---

# UI Design System & Master Generation Blueprint: arcteryx-com_us-en-explore-system0

> **System 0 · Arc’teryx** (https://arcteryx.com/us/en/explore/system0) — System 0 is the Arc’teryx platform linking our products, services, and guest experience together in a committed, synchronized journey tow...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **System 0 · Arc’teryx** (`https://arcteryx.com/us/en/explore/system0`). System 0 is the Arc’teryx platform linking our products, services, and guest experience together in a committed, synchronized journey tow...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fdfdfd` canvas, `#0c0c0c` ink, `#565656` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fdfdfd` (`html { color: #fdfdfd }`) paired with `#0c0c0c` primary typography and `#565656` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Elan ITC Pro` for display copy (`The Revolution is Circular`) with `Helvetica Now Display` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1279px` container bounds (`gap: 16.5%`, padding `var(--dot-overlap-offset-horizontal)`) with `cubic-bezier(.42,0,.58,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1279px` extracted from `arcteryx-com_us-en-explore-system0` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--dot-overlap-offset-horizontal)` lateral canvas padding with `16.5%` grid gap.
- **Border Radius Scale**: `50%`, `3px`, `2.5px`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 16.5%`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--dot-overlap-offset-horizontal)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:no-preference)`, `@media only screen and (min-width:1280px)`, `@media only screen and (max-width:1279px)`, `@media only screen and (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fdfdfd` | `html { color: #fdfdfd }` |
| **Primary Typography Ink** | `#0c0c0c` | `html { background: #0c0c0c }` |
| **Elevated Surface / Card Substrate** | `#1f96db` | `-banner-sdk .onetrust-vendors-l... { color: #1f96db }` |
| **Interactive Accent / Highlight** | `#565656` | `#ot-sync-ntfy .ot-pc-footer-log... { color: #565656 }` |
| **Secondary / Muted Copy** | `#fff` | `#ot-sdk-btn.optanon-show-settings { color: #fff }` |
| **Structural Hairline Border** | `#468254` | `#ot-sdk-btn.optanon-show-settings { background-color: #468254 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dot-overlap-offset-horizontal` | `12px` | Dimension / Scale Token |
| `--dot-overlap-offset-vertical` | `14px` | Dimension / Scale Token |
| `--dot-overlap-offset-relative` | `calc( var(--dot-overlap-offset-horizontal) + .5% )` | Dimension / Scale Token |
| `--circle-size` | `var(--button-circle-small-size)` | Layout / Spatial Grid Token |
| `--circle-border-opacity` | `1` | Elevation / Border Token |
| `--circle-border-interact` | `.2` | Elevation / Border Token |
| `--circle-content-opacity` | `1` | Design System Custom Token |
| `--circle-content-interact` | `1` | Design System Custom Token |
| `--pill-background` | `rgb(26, 26, 26)` | Canvas / Surface Token |
| `--pill-color` | `rgb(253, 253, 253)` | Brand / Palette Token |
| `--pill-background-active` | `rgb(212, 212, 212)` | Canvas / Surface Token |
| `--pill-color-active` | `rgb(12, 12, 12)` | Brand / Palette Token |
| `--pill-background-hover` | `rgb(253, 253, 253)` | Canvas / Surface Token |
| `--pill-color-hover` | `rgb(12, 12, 12)` | Brand / Palette Token |
| `--pill-background-disabled` | `rgb(253, 253, 253)` | Canvas / Surface Token |
| `--pill-color-disabled` | `rgb(212, 212, 212)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Elan ITC Pro`.
- **Primary Body Stack**: `Helvetica Now Display`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-helvetica-now-display: "Helvetica Now Display", helvetica, sans-serif`, `--type-font-size-display-1: 34px`, `--type-font-size-display-2: 20px`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`).
- **Body Copy**: CSS variables `--type-font-size-body-1: 18px`, `--type-font-size-body-2: 14px`, `--type-line-height-body-1: 22px`; rule `,p` (`line-height: inherit`, `letter-spacing: inherit`, `font-weight: inherit`).
- **Metadata & Navigation Labels**: CSS variables `--type-letter-spacing-display-1: .4px`, `--type-letter-spacing-display-2: .4px`, `--type-letter-spacing-body-1: .25px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.42,0,.58,1)`, `cubic-bezier(.87,-.01,.16,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media(prefers-reduced-motion:no-p...`**: `transition: opacity .2s cubic-bezier(.42,0,.58,1)` extracted from `arcteryx-com_us-en-explore-system0` stylesheet.
- **Selector `media(prefers-reduced-motion:no-p...`**: `transition: fill .2s cubic-bezier(.42,0,.58,1),stroke-opacity .2s cubic-be...` extracted from `arcteryx-com_us-en-explore-system0` stylesheet.
- **Selector `media(prefers-reduced-motion:no-p...`**: `transition: opacity .2s cubic-bezier(.42,0,.58,1)` extracted from `arcteryx-com_us-en-explore-system0` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.42,0,.58,1)`)**: Governs interactive state transitions across `<header.onetrust-pc-dark-filter>` and `<section.ot-fade-in>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — System 0 · Arc’teryx                       │
│ ====================================================================== │
│ [ <header.onetrust-pc-dark | PROCESS · MISSION · SPERRO SV · ARC’TE ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.ot-hide>                                    |   │
│ | H1: The Revolution is Circular                                   |   │
│ | Substrate: #fdfdfd    | Ink: #0c0c0c    | Accent: #565656        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.ot-fade-in>      ) max-w: 1279px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Find preferred materials     |  | Design for durability        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16.5% ) | │
│ | [<header.onetrust-p] -> [<section.ot-hide>] -> [<section.ot-fade-i]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.otRelFont>    ) | https://arcteryx.com/us/en/explore │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.onetrust-pc-dark-filter> — `arcteryx-com_us-en-explore-system0`)**:
   - Landmark `<header class="onetrust-pc-dark-filter">` hosting `System 0 · Arc’teryx` navigation (`PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`), DOM attributes (`data-signup-tag="4467"`, `data-is-header-visible="true"`, `data-document-language="true"`, `data-language-detection="true"`), and stylesheet rule `._container_ybue0_1 { display:grid;width:100% }`.
2. **Hero Stage & Focal Lead (<section.ot-hide> — `The Revolution is Circular`)**:
   - Landmark `<section class="ot-hide">` presenting display lead `The Revolution is Circular` and copy excerpt *"Our journey toward circularity"* over `#fdfdfd` canvas and `#0c0c0c` ink.
3. **Primary Showcase & Content Grid (<section.ot-fade-in> — `Find preferred materials`)**:
   - Landmark `<section class="ot-fade-in">` rendering section `Find preferred materials` with copy *"System 0™ is our platform linking our products, services, and gue"*, asset references (`Loading.zo8phPeo.css`, `footer-with-infinity-loop.BY7Pus-...`, `use-process-exit.mlCI1y1L.css`, `index.K17Bkq0c.css`), and grid rule `._asset_ybue0_9 { opacity:0;transition:opacity .2s cubic-bezier(.42,0,.58,1) }`.
4. **Interactive Detail & Feature Matrix (<section.ot-hide> — `Design for durability`)**:
   - Landmark `<section class="ot-hide ot-pc-scrollbar">` framing `Design for durability` and `Prioritize repairability` (*"we’re changing the way we create and support our products to prot"*) with `#1f96db` surface cards, `#565656` accents, and `._picture_ybue0_18 { display:contents }`.
5. **Colophon & Global Directory Footer (<footer.otRelFont> — `https://arcteryx.com/us/en/explore/system0`)**:
   - Landmark `<footer class="otRelFont">` anchoring `System 0 · Arc’teryx` footer links (`PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`), copy *"I. Find preferred materials"*, and `#468254` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: arcteryx-com_us-en-explore-system0 (System 0 · Arc’teryx)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `arcteryx-com_us-en-explore-system0` (**System 0 · Arc’teryx** — `https://arcteryx.com/us/en/explore/system0`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fdfdfd` canvas, `#0c0c0c` ink, `#565656` accent).
- **Identity & Domain Context**: System 0 is the Arc’teryx platform linking our products, services, and guest experience together in a committed, synchronized journey tow...
- **Primary Substrate**: `#fdfdfd` (`html { color: #fdfdfd }`), **Primary Ink**: `#0c0c0c`, **Accent / Highlight**: `#565656`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fdfdfd` (`html { color: #fdfdfd }`) paired with `#0c0c0c` primary typography and `#565656` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Elan ITC Pro` for display copy (`The Revolution is Circular`) with `Helvetica Now Display` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1279px` container bounds (`gap: 16.5%`, padding `var(--dot-overlap-offset-horizontal)`) with `cubic-bezier(.42,0,.58,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `arcteryx-com_us-en-explore-system0` in your global stylesheet:

:root {
  /* System 0 · Arc’teryx (arcteryx-com_us-en-explore-system0) — Ground-Truth Extracted CSS Variables */
  --dot-overlap-offset-horizontal: 12px; /* Dimension / Scale Token (arcteryx-com_us-en-explore-system0) */
  --dot-overlap-offset-vertical: 14px; /* Dimension / Scale Token (arcteryx-com_us-en-explore-system0) */
  --dot-overlap-offset-relative: calc( var(--dot-overlap-offset-horizontal) + .5% ); /* Dimension / Scale Token (arcteryx-com_us-en-explore-system0) */
  --circle-size: var(--button-circle-small-size); /* Layout / Spatial Grid Token (arcteryx-com_us-en-explore-system0) */
  --circle-border-opacity: 1; /* Elevation / Border Token (arcteryx-com_us-en-explore-system0) */
  --circle-border-interact: .2; /* Elevation / Border Token (arcteryx-com_us-en-explore-system0) */
  --circle-content-opacity: 1; /* Design System Custom Token (arcteryx-com_us-en-explore-system0) */
  --circle-content-interact: 1; /* Design System Custom Token (arcteryx-com_us-en-explore-system0) */
  --pill-background: rgb(26, 26, 26); /* Canvas / Surface Token (arcteryx-com_us-en-explore-system0) */
  --pill-color: rgb(253, 253, 253); /* Brand / Palette Token (arcteryx-com_us-en-explore-system0) */
  --pill-background-active: rgb(212, 212, 212); /* Canvas / Surface Token (arcteryx-com_us-en-explore-system0) */
  --pill-color-active: rgb(12, 12, 12); /* Brand / Palette Token (arcteryx-com_us-en-explore-system0) */
  --pill-background-hover: rgb(253, 253, 253); /* Canvas / Surface Token (arcteryx-com_us-en-explore-system0) */
  --pill-color-hover: rgb(12, 12, 12); /* Brand / Palette Token (arcteryx-com_us-en-explore-system0) */
  --pill-background-disabled: rgb(253, 253, 253); /* Canvas / Surface Token (arcteryx-com_us-en-explore-system0) */
  --pill-color-disabled: rgb(212, 212, 212); /* Brand / Palette Token (arcteryx-com_us-en-explore-system0) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fdfdfd` — grounded in `html { color: #fdfdfd }`
- **Primary Typography Ink**: `#0c0c0c` — grounded in `html { background: #0c0c0c }`
- **Elevated Surface / Card Substrate**: `#1f96db` — grounded in `-banner-sdk .onetrust-vendors-l... { color: #1f96db }`
- **Interactive Accent / Highlight**: `#565656` — grounded in `#ot-sync-ntfy .ot-pc-footer-log... { color: #565656 }`
- **Secondary / Muted Copy**: `#fff` — grounded in `#ot-sdk-btn.optanon-show-settings { color: #fff }`
- **Structural Hairline Border**: `#468254` — grounded in `#ot-sdk-btn.optanon-show-settings { background-color: #468254 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1279px` extracted from `arcteryx-com_us-en-explore-system0` stylesheet
- **Padding & Gutters**: `var(--dot-overlap-offset-horizontal)` lateral canvas padding with `16.5%` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 16.5%`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--dot-overlap-offset-horizontal)` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:no-preference)`, `@media only screen and (min-width:1280px)`, `@media only screen and (max-width:1279px)`, `@media only screen and (min-width:768px)`
- **Corner Radii**: `50%`, `3px`, `2.5px`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Elan ITC Pro`
- **Body Font Stack**: `Helvetica Now Display`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-helvetica-now-display: "Helvetica Now Display", helvetica, sans-serif`, `--type-font-size-display-1: 34px`, `--type-font-size-display-2: 20px`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **H2 Section Rule**: rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy Rule**: CSS variables `--type-font-size-body-1: 18px`, `--type-font-size-body-2: 14px`, `--type-line-height-body-1: 22px`; rule `,p` (`line-height: inherit`, `letter-spacing: inherit`, `font-weight: inherit`)
- **Metadata & Index Rule**: CSS variables `--type-letter-spacing-display-1: .4px`, `--type-letter-spacing-display-2: .4px`, `--type-letter-spacing-body-1: .25px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `arcteryx-com_us-en-explore-system0` (`System 0 · Arc’teryx`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.onetrust-pc-dark-filter> — `arcteryx-com_us-en-explore-system0`)**:
   - DOM & Selectors: Landmark `<header class="onetrust-pc-dark-filter">` hosting `System 0 · Arc’teryx` navigation (`PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`), DOM attributes (`data-signup-tag="4467"`, `data-is-header-visible="true"`, `data-document-language="true"`, `data-language-detection="true"`), and stylesheet rule `._container_ybue0_1 { display:grid;width:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.onetrust-pc-dark-filter> — `arcteryx-com_us-en-explore-system0`)` (`arcteryx-com_us-en-explore-system0`) adapts across `@media (prefers-reduced-motion:no-preference)`, `@media only screen and (min-width:1280px)`, `@media only screen and (max-width:1279px)`, `@media only screen and (min-width:768px)` with `cubic-bezier(.42,0,.58,1)`, `cubic-bezier(.87,-.01,.16,1)` transitions and links `PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`.
2. **Hero Stage & Focal Lead (<section.ot-hide> — `The Revolution is Circular`)**:
   - DOM & Selectors: Landmark `<section class="ot-hide">` presenting display lead `The Revolution is Circular` and copy excerpt *"Our journey toward circularity"* over `#fdfdfd` canvas and `#0c0c0c` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fdfdfd` background with `#0c0c0c` headline `The Revolution is Circular`.
3. **Primary Showcase & Content Grid (<section.ot-fade-in> — `Find preferred materials`)**:
   - DOM & Selectors: Landmark `<section class="ot-fade-in">` rendering section `Find preferred materials` with copy *"System 0™ is our platform linking our products, services, and gue"*, asset references (`Loading.zo8phPeo.css`, `footer-with-infinity-loop.BY7Pus-...`, `use-process-exit.mlCI1y1L.css`, `index.K17Bkq0c.css`), and grid rule `._asset_ybue0_9 { opacity:0;transition:opacity .2s cubic-bezier(.42,0,.58,1) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.ot-fade-in> — `Find preferred materials`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 16.5%`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--dot-overlap-offset-horizontal)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.ot-hide> — `Design for durability`)**:
   - DOM & Selectors: Landmark `<section class="ot-hide ot-pc-scrollbar">` framing `Design for durability` and `Prioritize repairability` (*"we’re changing the way we create and support our products to prot"*) with `#1f96db` surface cards, `#565656` accents, and `._picture_ybue0_18 { display:contents }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.ot-hide> — `Design for durability`)` uses `50%`, `3px`, `2.5px`, `4px` radii, `#565656` highlights, and assets (Loading.zo8phPeo.css, footer-with-infinity-loop.BY7Pus-..., use-process-exit.mlCI1y1L.css).
5. **Colophon & Global Directory Footer (<footer.otRelFont> — `https://arcteryx.com/us/en/explore/system0`)**:
   - DOM & Selectors: Landmark `<footer class="otRelFont">` anchoring `System 0 · Arc’teryx` footer links (`PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`), copy *"I. Find preferred materials"*, and `#468254` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.otRelFont> — `https://arcteryx.com/us/en/explore/system0`)` aligns to `1279px` extracted from `arcteryx-com_us-en-explore-system0` stylesheet with `var(--dot-overlap-offset-horizontal)` lateral canvas padding with `16.5%` grid gap and attributes (data-signup-tag="4467", data-is-header-visible="true", data-document-language="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Our journey toward circularity"*
- Copy Excerpt 2: *"System 0™ is our platform linking our products, services, and guest experience tog..."*
- Copy Excerpt 3: *"we’re changing the way we create and support our products to protect the mountains..."*
- Copy Excerpt 4: *"I. Find preferred materials"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.42,0,.58,1)`, `cubic-bezier(.87,-.01,.16,1)`
- **Extracted Stylesheet Rules (`arcteryx-com_us-en-explore-system0`)**:
- `._container_ybue0_1 { display:grid;width:100% }`
- `._asset_ybue0_9 { opacity:0;transition:opacity .2s cubic-bezier(.42,0,.58,1) }`
- `._picture_ybue0_18 { display:contents }`
- `._container_zjxo5_1 { --dot-overlap-offset-horizontal: 20px;--dot-overlap-offset-vertical: 16px }`
- `._icon_zjxo5_16 { grid-area:1/1;aspect-ratio:var(--loop-aspect-ratio) }`
- **Per-Selector Transition Rules**:
- **Selector `media(prefers-reduced-motion:no-p...`**: `transition: opacity .2s cubic-bezier(.42,0,.58,1)` extracted from `arcteryx-com_us-en-explore-system0` stylesheet.
- **Selector `media(prefers-reduced-motion:no-p...`**: `transition: fill .2s cubic-bezier(.42,0,.58,1),stroke-opacity .2s cubic-be...` extracted from `arcteryx-com_us-en-explore-system0` stylesheet.
- **Selector `media(prefers-reduced-motion:no-p...`**: `transition: opacity .2s cubic-bezier(.42,0,.58,1)` extracted from `arcteryx-com_us-en-explore-system0` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.42,0,.58,1)`)**: Governs interactive state transitions across `<header.onetrust-pc-dark-filter>` and `<section.ot-fade-in>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `arcteryx-com_us-en-explore-system0`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
