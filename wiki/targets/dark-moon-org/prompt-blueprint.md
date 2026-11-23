---
title: "UI Prompt Blueprint: dark-moon-org"
date: 2026-11-23
captured_at: 2026-11-23
target: "dark-moon-org"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#f97316` accent)"
---

# UI Design System & Master Generation Blueprint: dark-moon-org

> **Darkmoon: Autonomous AI Penetration Testing Platform** (https://dark-moon.org/) — Darkmoon is an open-source, AI-powered autonomous penetration testing platform. 50 specialized AI agents covering web, cloud, identity, C...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Darkmoon: Autonomous AI Penetration Testing Platform** (`https://dark-moon.org/`). Darkmoon is an open-source, AI-powered autonomous penetration testing platform. 50 specialized AI agents covering web, cloud, identity, C...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#f97316` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#f97316` accents.
  - **Grounded Typographic Hierarchy**: Pairs `googleSans` for display copy (`Darkmoon, Autonomous AI Penetration `) with `Poppins` and `Google Sans Code`.
  - **Calibrated Spatial Grid & Motion**: Combines `1217px` container bounds (`gap: 2px`, padding `1px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1217px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `1px` lateral canvas padding with `2px` grid gap.
- **Border Radius Scale**: `27px`, `16px`, `22px`, `14px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: 2-column persistent left sidebar (`188px`, <nav.ml-1>) + `1429px` main content stage at `1440px` (`max-width: 1217px`, `gap: 2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with collapsed `<nav.ml-1>` drawer navigation and `1px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:767.98px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#151515` | `var(--dm-card)` in `:root` |
| **Interactive Accent / Highlight** | `#f97316` | `.dm-main .dm-badge--high:before { background: #f97316 }` |
| **Secondary / Muted Copy** | `#9a9aa6` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#5c6168` | `var(--dc-line)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--radius` | `15px` | Elevation / Border Token |
| `--background` | `#000` | Canvas / Surface Token |
| `--dm-gutter` | `clamp(.75rem,1.6vw,1.75rem)` | Layout / Spatial Grid Token |
| `--dm-inset` | `clamp(1rem,4.5vw,6rem)` | Dimension / Scale Token |
| `--dm-page-x` | `clamp(1rem,2.22vw,2.25rem)` | Dimension / Scale Token |
| `--dm-card` | `#151515` | Color / Atmospheric Token |
| `--dm-line` | `#ffffff42` | Color / Atmospheric Token |
| `--dm-card-line` | `#ffffff2e` | Color / Atmospheric Token |
| `--dm-card-radius` | `.5rem` | Elevation / Border Token |
| `--dm-card-gap` | `clamp(1rem,1.25vw,1.25rem)` | Layout / Spatial Grid Token |
| `--dm-section-top` | `clamp(1.5rem,2.22vw,2.25rem)` | Dimension / Scale Token |
| `--dm-section-bottom` | `clamp(6rem,17.8vw,17.75rem)` | Dimension / Scale Token |
| `--dm-stack-gap` | `clamp(4rem,13vw,13rem)` | Layout / Spatial Grid Token |
| `--dm-display` | `clamp(3.25rem,7.8vw,7.75rem)` | Dimension / Scale Token |
| `--dm-statement` | `clamp(1.75rem,3.33vw,3.35rem)` | Dimension / Scale Token |
| `--dm-h3` | `clamp(1.5rem,2.22vw,2.25rem)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `googleSans`.
- **Primary Body Stack**: `Poppins`.
- **Technical / Metadata Stack**: `Google Sans Code`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--dm-display: clamp(3.25rem,7.8vw,7.75rem)`, `--m-display: clamp(3.5rem,calc(2rem + 8.2vw),4.5rem)`, `--m-h1: clamp(2.25rem,calc(1.25rem + 5.13vw),2.75rem)`; rule `h1` (`font-size: min(var(--m-h1),calc((100vw -...`, `line-height: .95`, `letter-spacing: -.02em`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 28px`, `line-height: 30.8px`, `font-weight: 500`, `letter-spacing: -0.56px`); rule `h2` (`letter-spacing: -.01em`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--dm-body: clamp(1rem,1.11vw,1.125rem)`, `--dm-body-lh: 1.45`, `--text-base: 1rem`; rule `p` (`font-size: .9375rem`, `line-height: 1.4`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--dm-label: .78rem`, `--font-mono: var(--font-code)`, `--text-xs: .75rem`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `gl6):not(#gl7):not(#gl8):not(#gl9...`**: `transition: background-color .15s ease,color .15s ease,filter .15s ease!im...` extracted from `dark-moon-org` stylesheet.
- **Selector `l1):not(#gl2):not(#gl3) .mlab .cc...`**: `transition: opacity .3s,background-color .3s` extracted from `dark-moon-org` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `dark-moon-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.scroll-mt-24>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Sidebar (188px) + Main (1429px)            │
│ ====================================================================== │
│ +--[ SIDEBAR (188px) ]--+--[ MAIN CONTENT STAGE (1429px) ]-----------+ │
│ | <nav.ml-1>            | [ <header.inset-x-0 | Product · Attack p ] | │
│ | - Product             | ------------------------------------------ | │
│ | - Attack paths        | HERO STAGE: <section.dm-hero>              | │
│ | - Pricing             | H1: Darkmoon, Autonomous AI Penetration Te | │
│ | - Docs                | Bg:#000000 Ink:#ffffff Acc:#f97316         | │
│ | x=12 h=598px rail     | ------------------------------------------ | │
│ |                       | SHOWCASE: <section.scroll-mt-2 max:1217px  | │
│ |                       | [Attack surface cam] [Not a scanner. An ]  | │
│ |                       | DETAIL: <section.dc>                       | │
│ +-----------------------+--------------------------------------------+ │
│ [ FOOTER (<footer.relative>   ) | https://dark-moon.org/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Collapsed Sidebar + 1-Col Stack       │
│ ====================================================================== │
│ [ DRAWER (<nav.ml-1>            ) | <header.inset-x-0>                 │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.dm-hero>) — 390px Full-Width                  | │
│ | H1: Darkmoon, Autonomous AI Penetration Testing Platform           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.scroll-mt-24>) — 1-Col (gap: 2px)         | │
│ | [ Card 1: Attack surface camp_20260426_3d2f · 26 Apr 2026        ] | │
│ | [ Card 2: Not a scanner. An autonomous security conductor.       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.dc>) — 1-Col (Darkmoon + Splunk:)           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | Stacked 390px Colophon             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Persistent Left Sidebar Navigation (<nav.ml-1> — `188×598px` at `x=12`)**:
   - Fixed/sticky left rail `<nav class="ml-1 hidden">` (`188px` wide) paired with top bar `<header class="inset-x-0 top-0">` hosting `Darkmoon: Autonomous AI Penetr` navigation (`Product · Attack paths · Pricing · Docs · Blog`), DOM attributes (`data-route-lang="en"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and rule `gl-l { display:block }`.
2. **Hero Stage & Focal Lead (<section.dm-hero> — `Darkmoon, Autonomous AI Penetratio`)**:
   - Landmark `<section class="dm-hero w6">` inside `1429px` main stage presenting display lead `Darkmoon, Autonomous AI Penetration Testing Platform` and copy excerpt *"AUTONOMOUS, CONTINUOUS PENETRATION TESTING"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.scroll-mt-24> — `Attack surface camp_20260426_3d2f `)**:
   - Landmark `<section class="scroll-mt-24 overflow-clip">` rendering section `Attack surface camp_20260426_3d2f · 26 Apr 2026` with copy *"Autonomous, continuous penetration testing"*, asset references (`eafabf029ad39a43-s.p.woff2`, `3d4d48715202a72c.css`, `6e008cfa72251405.css`, `e824d722814de74c.css`), and grid rule `.gl-host { isolation:isolate }`.
4. **Interactive Detail & Feature Matrix (<section.dc> — `Not a scanner. An autonomous secur`)**:
   - Landmark `<section class="dc dc--default">` framing `Not a scanner. An autonomous security conductor.` and `Darkmoon + Splunk: Send AI Pentest Findings to Yo...` (*"Autonomous, continuous"*) with `#151515` surface cards, `#f97316` accents, and `.gl-host.gl-static { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://dark-moon.org/`)**:
   - Landmark `<footer class="relative bg-white">` anchoring `Darkmoon: Autonomous AI Penetrat` footer links (`Product · Attack paths · Pricing · Docs · Blog`), copy *"penetration testing"*, and `#5c6168` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dark-moon-org (Darkmoon: Autonomous AI Penetration Testing Platform)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dark-moon-org` (**Darkmoon: Autonomous AI Penetration Testing Platform** — `https://dark-moon.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#f97316` accent).
- **Identity & Domain Context**: Darkmoon is an open-source, AI-powered autonomous penetration testing platform. 50 specialized AI agents covering web, cloud, identity, C...
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#f97316`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#f97316` accents.
  - **Grounded Typographic Hierarchy**: Pairs `googleSans` for display copy (`Darkmoon, Autonomous AI Penetration `) with `Poppins` and `Google Sans Code`.
  - **Calibrated Spatial Grid & Motion**: Combines `1217px` container bounds (`gap: 2px`, padding `1px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dark-moon-org` in your global stylesheet:

:root {
  /* Darkmoon: Autonomous AI Penetration Testing Platform (dark-moon-org) — Live-Grounded CSS Variables */
  --radius: 15px; /* Elevation / Border Token (dark-moon-org) */
  --background: #000; /* Canvas / Surface Token (dark-moon-org) */
  --dm-gutter: clamp(.75rem,1.6vw,1.75rem); /* Layout / Spatial Grid Token (dark-moon-org) */
  --dm-inset: clamp(1rem,4.5vw,6rem); /* Dimension / Scale Token (dark-moon-org) */
  --dm-page-x: clamp(1rem,2.22vw,2.25rem); /* Dimension / Scale Token (dark-moon-org) */
  --dm-card: #151515; /* Color / Atmospheric Token (dark-moon-org) */
  --dm-line: #ffffff42; /* Color / Atmospheric Token (dark-moon-org) */
  --dm-card-line: #ffffff2e; /* Color / Atmospheric Token (dark-moon-org) */
  --dm-card-radius: .5rem; /* Elevation / Border Token (dark-moon-org) */
  --dm-card-gap: clamp(1rem,1.25vw,1.25rem); /* Layout / Spatial Grid Token (dark-moon-org) */
  --dm-section-top: clamp(1.5rem,2.22vw,2.25rem); /* Dimension / Scale Token (dark-moon-org) */
  --dm-section-bottom: clamp(6rem,17.8vw,17.75rem); /* Dimension / Scale Token (dark-moon-org) */
  --dm-stack-gap: clamp(4rem,13vw,13rem); /* Layout / Spatial Grid Token (dark-moon-org) */
  --dm-display: clamp(3.25rem,7.8vw,7.75rem); /* Dimension / Scale Token (dark-moon-org) */
  --dm-statement: clamp(1.75rem,3.33vw,3.35rem); /* Dimension / Scale Token (dark-moon-org) */
  --dm-h3: clamp(1.5rem,2.22vw,2.25rem); /* Typography / Scale Token (dark-moon-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#151515` — grounded in `var(--dm-card)` in `:root`
- **Interactive Accent / Highlight**: `#f97316` — grounded in `.dm-main .dm-badge--high:before { background: #f97316 }`
- **Secondary / Muted Copy**: `#9a9aa6` — grounded in `var(--muted-foreground)` in `:root`
- **Structural Hairline Border**: `#5c6168` — grounded in `var(--dc-line)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1217px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `1px` lateral canvas padding with `2px` grid gap
- **Desktop Grid**: 2-column persistent left sidebar (`188px`, <nav.ml-1>) + `1429px` main content stage at `1440px` (`max-width: 1217px`, `gap: 2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with collapsed `<nav.ml-1>` drawer navigation and `1px` horizontal padding
- **Media Queries**: `@media (max-width:767.98px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`
- **Corner Radii**: `27px`, `16px`, `22px`, `14px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `googleSans`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `Google Sans Code`
- **H1 Display Rule**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--dm-display: clamp(3.25rem,7.8vw,7.75rem)`, `--m-display: clamp(3.5rem,calc(2rem + 8.2vw),4.5rem)`, `--m-h1: clamp(2.25rem,calc(1.25rem + 5.13vw),2.75rem)`; rule `h1` (`font-size: min(var(--m-h1),calc((100vw -...`, `line-height: .95`, `letter-spacing: -.02em`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 28px`, `line-height: 30.8px`, `font-weight: 500`, `letter-spacing: -0.56px`); rule `h2` (`letter-spacing: -.01em`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--dm-body: clamp(1rem,1.11vw,1.125rem)`, `--dm-body-lh: 1.45`, `--text-base: 1rem`; rule `p` (`font-size: .9375rem`, `line-height: 1.4`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--dm-label: .78rem`, `--font-mono: var(--font-code)`, `--text-xs: .75rem`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dark-moon-org` (`Darkmoon: Autonomous AI Penetration Testing Platform`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Persistent Left Sidebar Navigation (<nav.ml-1> — `188×598px` at `x=12`)**:
   - DOM & Selectors: Fixed/sticky left rail `<nav class="ml-1 hidden">` (`188px` wide) paired with top bar `<header class="inset-x-0 top-0">` hosting `Darkmoon: Autonomous AI Penetr` navigation (`Product · Attack paths · Pricing · Docs · Blog`), DOM attributes (`data-route-lang="en"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and rule `gl-l { display:block }`.
   - Responsive Contract: Header `Persistent Left Sidebar Navigation (<nav.ml-1> — `188×598px` at `x=12`)` (`dark-moon-org`) adapts across `@media (max-width:767.98px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Product · Attack paths · Pricing · Docs · Blog`.
2. **Hero Stage & Focal Lead (<section.dm-hero> — `Darkmoon, Autonomous AI Penetratio`)**:
   - DOM & Selectors: Landmark `<section class="dm-hero w6">` inside `1429px` main stage presenting display lead `Darkmoon, Autonomous AI Penetration Testing Platform` and copy excerpt *"AUTONOMOUS, CONTINUOUS PENETRATION TESTING"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#ffffff` headline `Darkmoon, Autonomous AI Penetration Testing Platform`.
3. **Primary Showcase & Content Grid (<section.scroll-mt-24> — `Attack surface camp_20260426_3d2f `)**:
   - DOM & Selectors: Landmark `<section class="scroll-mt-24 overflow-clip">` rendering section `Attack surface camp_20260426_3d2f · 26 Apr 2026` with copy *"Autonomous, continuous penetration testing"*, asset references (`eafabf029ad39a43-s.p.woff2`, `3d4d48715202a72c.css`, `6e008cfa72251405.css`, `e824d722814de74c.css`), and grid rule `.gl-host { isolation:isolate }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.scroll-mt-24> — `Attack surface camp_20260426_3d2f `)` applies 2-column persistent left sidebar (`188px`, <nav.ml-1>) + `1429px` main content stage at `1440px` (`max-width: 1217px`, `gap: 2px`) on desktop and Single-column vertical stack at `390px` viewport width with collapsed `<nav.ml-1>` drawer navigation and `1px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.dc> — `Not a scanner. An autonomous secur`)**:
   - DOM & Selectors: Landmark `<section class="dc dc--default">` framing `Not a scanner. An autonomous security conductor.` and `Darkmoon + Splunk: Send AI Pentest Findings to Yo...` (*"Autonomous, continuous"*) with `#151515` surface cards, `#f97316` accents, and `.gl-host.gl-static { position:relative }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.dc> — `Not a scanner. An autonomous secur`)` uses `27px`, `16px`, `22px`, `14px` radii, `#f97316` highlights, and assets (eafabf029ad39a43-s.p.woff2, 3d4d48715202a72c.css, 6e008cfa72251405.css).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://dark-moon.org/`)**:
   - DOM & Selectors: Landmark `<footer class="relative bg-white">` anchoring `Darkmoon: Autonomous AI Penetrat` footer links (`Product · Attack paths · Pricing · Docs · Blog`), copy *"penetration testing"*, and `#5c6168` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://dark-moon.org/`)` aligns to `1217px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `1px` lateral canvas padding with `2px` grid gap and attributes (data-route-lang="en", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"AUTONOMOUS, CONTINUOUS PENETRATION TESTING"*
- Copy Excerpt 2: *"Autonomous, continuous penetration testing"*
- Copy Excerpt 3: *"Autonomous, continuous"*
- Copy Excerpt 4: *"penetration testing"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`dark-moon-org`)**:
- `gl-l { display:block }`
- `.gl-host { isolation:isolate }`
- `.gl-host.gl-static { position:relative }`
- `.gl-card { border-radius:22px!important }`
- `.gl-panel { border-radius:14px!important }`
- **Per-Selector Transition Rules**:
- **Selector `gl6):not(#gl7):not(#gl8):not(#gl9...`**: `transition: background-color .15s ease,color .15s ease,filter .15s ease!im...` extracted from `dark-moon-org` stylesheet.
- **Selector `l1):not(#gl2):not(#gl3) .mlab .cc...`**: `transition: opacity .3s,background-color .3s` extracted from `dark-moon-org` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `dark-moon-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.scroll-mt-24>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dark-moon-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
