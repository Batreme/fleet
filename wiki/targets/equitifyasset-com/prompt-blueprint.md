---
title: "UI Prompt Blueprint: equitifyasset-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "equitifyasset-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#fbfbfb` canvas, `#000000` ink, `#0000ee` accent)"
---

# UI Design System & Master Generation Blueprint: equitifyasset-com

> **EquitiFy Assets · Home** (https://equitifyasset.com/) — We source off-market commercial property, run the acquisition end to end, and hand you 100% ownership. No syndicates, no partners.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **EquitiFy Assets · Home** (`https://equitifyasset.com/`). We source off-market commercial property, run the acquisition end to end, and hand you 100% ownership. No syndicates, no partners.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fbfbfb` canvas, `#000000` ink, `#0000ee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fbfbfb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Aspekta Variable Variable` for display copy (`100%`) with `Aspekta Variable Variable Placeholder` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: 128px`, padding `36px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1920px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `36px` lateral canvas padding with `128px` grid gap.
- **Border Radius Scale**: `40px`, `10px`, `8px`, `15px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 128px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `36px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 1200px)`, `@media (min-width: 720px) and (max-width: 1199.98px)`, `@media (max-width: 719.98px)`, `@media (max-width:1199px) and (min-width:720px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fbfbfb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#c83e07` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `var(--border-color)` in `:root` |
| **Variable Token (`--token-f277370d-904c-4e87-88c6-49451f154e33`)** | `#d1ff00` | `var(--token-f277370d-904c-4e87-88c6-49451f154e33)` in `:root` |
| **Variable Token (`--token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f`)** | `#f4f4e8` | `var(--token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f)` in `:root` |
| **Variable Token (`--token-82d92470-f077-4c9d-9673-709d01132847`)** | `#534f4d` | `var(--token-82d92470-f077-4c9d-9673-709d01132847)` in `:root` |
| **Variable Token (`--token-1486dbb4-cc20-4852-a20d-db81362153cb`)** | `#bcbcbc` | `var(--token-1486dbb4-cc20-4852-a20d-db81362153cb)` in `:root` |
| **Variable Token (`--token-08d07ee3-fce8-41f2-9d02-9c41009dd49d`)** | `#3d3d3d` | `var(--token-08d07ee3-fce8-41f2-9d02-9c41009dd49d)` in `:root` |
| **Variable Token (`--token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284`)** | `#1c1e19` | `var(--token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284)` in `:root` |
| **Variable Token (`--token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3`)** | `#ffffed` | `var(--token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3)` in `:root` |
| **Variable Token (`--token-5e7f03a9-6226-4578-8399-febb83abe7c0`)** | `#050505` | `var(--token-5e7f03a9-6226-4578-8399-febb83abe7c0)` in `:root` |
| **Variable Token (`--token-b22324d1-617e-4b7c-9516-d41489048918`)** | `#9c9c9c` | `var(--token-b22324d1-617e-4b7c-9516-d41489048918)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-e5145d68-ee3f-43dc-8638-41389fb43644` | `#e2e2e2` | Color / Atmospheric Token |
| `--token-f277370d-904c-4e87-88c6-49451f154e33` | `#d1ff00` | Color / Atmospheric Token |
| `--token-d33926f3-e1ef-47a7-a2fc-872ea608e7c8` | `#000` | Color / Atmospheric Token |
| `--token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f` | `#f4f4e8` | Color / Atmospheric Token |
| `--token-82d92470-f077-4c9d-9673-709d01132847` | `#534f4d` | Color / Atmospheric Token |
| `--token-1486dbb4-cc20-4852-a20d-db81362153cb` | `#bcbcbc` | Color / Atmospheric Token |
| `--token-08d07ee3-fce8-41f2-9d02-9c41009dd49d` | `#3d3d3d` | Color / Atmospheric Token |
| `--token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284` | `#1c1e19` | Color / Atmospheric Token |
| `--token-27d215b1-9859-4ed9-910b-49be7f89fc94` | `#fbfbfb` | Color / Atmospheric Token |
| `--token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3` | `#ffffed` | Color / Atmospheric Token |
| `--token-19fadcaa-97dd-4766-8f90-eb9a72bcc235` | `#c83e07` | Color / Atmospheric Token |
| `--token-a5e091a2-859c-44ea-91df-ecdc98f39d88` | `#f4f4e8` | Color / Atmospheric Token |
| `--token-1f8b4914-6c8e-4506-b0ec-24a02142f4ba` | `#d1ff00` | Color / Atmospheric Token |
| `--token-5e7f03a9-6226-4578-8399-febb83abe7c0` | `#050505` | Color / Atmospheric Token |
| `--token-b5be0a90-9b43-4c58-8ca5-f5dd60fafe9f` | `#bcbcbc` | Color / Atmospheric Token |
| `--token-b22324d1-617e-4b7c-9516-d41489048918` | `#9c9c9c26` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Aspekta Variable Variable`.
- **Primary Body Stack**: `Aspekta Variable Variable Placeholder`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78.88px`, `line-height: 78.88px`, `font-weight: 400`, `letter-spacing: -2.3664px`); rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1em`, `letter-spacing: -.03em`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`, `letter-spacing: -1.92px`); rule `h2` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.1em`, `letter-spacing: -.04em`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.3em`, `letter-spacing: -.02em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.32,0.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `equitifyasset-com` stylesheet.
- **Selector `er-styles-preset-3w9o9k.rich-text...`**: `transition: color .4s cubic-bezier(.4,0,.2,1)` extracted from `equitifyasset-com` stylesheet.
- **Selector `er-styles-preset-cxxcqs.rich-text...`**: `transition: color .4s cubic-bezier(.4,0,.2,1)` extracted from `equitifyasset-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<div.framer-ebH8S>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — EquitiFy Assets · Home                     │
│ ====================================================================== │
│ [ <header.lenis> (1440px)             | Home · How We Work · Propert ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.lenis-autoToggle> (w=1440px)                      | │
│ | H1: 100%                                                           | │
│ | Substrate: #fbfbfb | Ink: #000000 | Accent: #0000ee                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.framer-ebH8S>) max-w: 1920px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Tax Benefits                 |  | W h e r e C a p i t a l B e  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<div.framer-7dSme>) — Exclusive Access              | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-UGi5s) | https://equitifyasset.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 128px)      │
│ ====================================================================== │
│ [ HEADER BAR (<header.lenis>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<div.lenis-autoToggle>) — 390px Vertical Lead          | │
│ | H1: 100%                                                           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<div.framer-ebH8S>) — 1-Col Stack                  | │
│ | [ Item 1: Tax Benefits                                           ] | │
│ | [ Item 2: W h e r e C a p i t a l B e c o m e s O w n e r s...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<div.framer-7dSme>) — 1-Col (Exclusive Access)       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-UGi5s) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `equitifyasset-com`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `EquitiFy Assets · Home` navigation (`Home · How We Work · Properties · about us · Contact Us`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<div.lenis-autoToggle> — `100%`)**:
   - Landmark `<div class="lenis-autoToggle">` presenting display lead `100%` and copy excerpt *"EquitiFy Assets sources off-market commercial properties built ar"* over `#fbfbfb` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.framer-ebH8S> — `Tax Benefits`)**:
   - Landmark `<div class="framer-ebH8S">` rendering section `Tax Benefits` with copy *"We run the deal end-to-end. You keep 100%."*, asset references (`suGqY6sVqYrEl8vVN4Ar3ufRvmw.png`, `p8gmopxLkGo6Ily14ZQSTHPOFo0.png`, `3TkAWwL2xbK4k3fwlVTZWqigw.png`, `script`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<div.framer-7dSme> — `W h e r e C a p i t a l B e c o m `)**:
   - Landmark `<div class="framer-7dSme">` framing `W h e r e C a p i t a l B e c o m e s O w n e r s...` and `Exclusive Access` (*"The best properties never reach a listing. Ours come through an o"*) with `#c83e07` surface cards, `#0000ee` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.framer-UGi5s> — `https://equitifyasset.com/`)**:
   - Landmark `<footer class="framer-UGi5s framer-m1Hmn">` anchoring `EquitiFy Assets · Home` footer links (`Home · How We Work · Properties · about us · Contact Us`), copy *"We buy the same properties we bring to you, in the same mark"*, and `#e2e2e2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: equitifyasset-com (EquitiFy Assets · Home)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `equitifyasset-com` (**EquitiFy Assets · Home** — `https://equitifyasset.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fbfbfb` canvas, `#000000` ink, `#0000ee` accent).
- **Identity & Domain Context**: We source off-market commercial property, run the acquisition end to end, and hand you 100% ownership. No syndicates, no partners.
- **Primary Substrate**: `#fbfbfb` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0000ee`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fbfbfb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Aspekta Variable Variable` for display copy (`100%`) with `Aspekta Variable Variable Placeholder` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: 128px`, padding `36px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `equitifyasset-com` in your global stylesheet:

:root {
  /* EquitiFy Assets · Home (equitifyasset-com) — Live-Grounded CSS Variables */
  --token-e5145d68-ee3f-43dc-8638-41389fb43644: #e2e2e2; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-f277370d-904c-4e87-88c6-49451f154e33: #d1ff00; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-d33926f3-e1ef-47a7-a2fc-872ea608e7c8: #000; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f: #f4f4e8; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-82d92470-f077-4c9d-9673-709d01132847: #534f4d; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-1486dbb4-cc20-4852-a20d-db81362153cb: #bcbcbc; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-08d07ee3-fce8-41f2-9d02-9c41009dd49d: #3d3d3d; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284: #1c1e19; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-27d215b1-9859-4ed9-910b-49be7f89fc94: #fbfbfb; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3: #ffffed; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-19fadcaa-97dd-4766-8f90-eb9a72bcc235: #c83e07; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-a5e091a2-859c-44ea-91df-ecdc98f39d88: #f4f4e8; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-1f8b4914-6c8e-4506-b0ec-24a02142f4ba: #d1ff00; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-5e7f03a9-6226-4578-8399-febb83abe7c0: #050505; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-b5be0a90-9b43-4c58-8ca5-f5dd60fafe9f: #bcbcbc; /* Color / Atmospheric Token (equitifyasset-com) */
  --token-b22324d1-617e-4b7c-9516-d41489048918: #9c9c9c26; /* Color / Atmospheric Token (equitifyasset-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fbfbfb` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#c83e07` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e2e2e2` — grounded in `var(--border-color)` in `:root`
- **Variable Token (`--token-f277370d-904c-4e87-88c6-49451f154e33`)**: `#d1ff00` — grounded in `var(--token-f277370d-904c-4e87-88c6-49451f154e33)` in `:root`
- **Variable Token (`--token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f`)**: `#f4f4e8` — grounded in `var(--token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f)` in `:root`
- **Variable Token (`--token-82d92470-f077-4c9d-9673-709d01132847`)**: `#534f4d` — grounded in `var(--token-82d92470-f077-4c9d-9673-709d01132847)` in `:root`
- **Variable Token (`--token-1486dbb4-cc20-4852-a20d-db81362153cb`)**: `#bcbcbc` — grounded in `var(--token-1486dbb4-cc20-4852-a20d-db81362153cb)` in `:root`
- **Variable Token (`--token-08d07ee3-fce8-41f2-9d02-9c41009dd49d`)**: `#3d3d3d` — grounded in `var(--token-08d07ee3-fce8-41f2-9d02-9c41009dd49d)` in `:root`
- **Variable Token (`--token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284`)**: `#1c1e19` — grounded in `var(--token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284)` in `:root`
- **Variable Token (`--token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3`)**: `#ffffed` — grounded in `var(--token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3)` in `:root`
- **Variable Token (`--token-5e7f03a9-6226-4578-8399-febb83abe7c0`)**: `#050505` — grounded in `var(--token-5e7f03a9-6226-4578-8399-febb83abe7c0)` in `:root`
- **Variable Token (`--token-b22324d1-617e-4b7c-9516-d41489048918`)**: `#9c9c9c` — grounded in `var(--token-b22324d1-617e-4b7c-9516-d41489048918)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1920px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `36px` lateral canvas padding with `128px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 128px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `36px` horizontal padding
- **Media Queries**: `@media (min-width: 1200px)`, `@media (min-width: 720px) and (max-width: 1199.98px)`, `@media (max-width: 719.98px)`, `@media (max-width:1199px) and (min-width:720px)`
- **Corner Radii**: `40px`, `10px`, `8px`, `15px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Aspekta Variable Variable`
- **Body Font Stack**: `Aspekta Variable Variable Placeholder`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 78.88px`, `line-height: 78.88px`, `font-weight: 400`, `letter-spacing: -2.3664px`); rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1em`, `letter-spacing: -.03em`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`, `letter-spacing: -1.92px`); rule `h2` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.1em`, `letter-spacing: -.04em`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.3em`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `equitifyasset-com` (`EquitiFy Assets · Home`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `equitifyasset-com`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` (`1440px`) hosting `EquitiFy Assets · Home` navigation (`Home · How We Work · Properties · about us · Contact Us`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `equitifyasset-com`)` (`equitifyasset-com`) adapts across `@media (min-width: 1200px)`, `@media (min-width: 720px) and (max-width: 1199.98px)`, `@media (max-width: 719.98px)`, `@media (max-width:1199px) and (min-width:720px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.32,0.72,0,1)` transitions and links `Home · How We Work · Properties · about us · Contact Us`.
2. **Hero Stage & Focal Lead (<div.lenis-autoToggle> — `100%`)**:
   - DOM & Selectors: Landmark `<div class="lenis-autoToggle">` presenting display lead `100%` and copy excerpt *"EquitiFy Assets sources off-market commercial properties built ar"* over `#fbfbfb` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fbfbfb` background with `#000000` headline `100%`.
3. **Primary Showcase & Content Grid (<div.framer-ebH8S> — `Tax Benefits`)**:
   - DOM & Selectors: Landmark `<div class="framer-ebH8S">` rendering section `Tax Benefits` with copy *"We run the deal end-to-end. You keep 100%."*, asset references (`suGqY6sVqYrEl8vVN4Ar3ufRvmw.png`, `p8gmopxLkGo6Ily14ZQSTHPOFo0.png`, `3TkAWwL2xbK4k3fwlVTZWqigw.png`, `script`), and grid rule `.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.framer-ebH8S> — `Tax Benefits`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 128px`) on desktop and Single-column vertical stack at `390px` viewport width with `36px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.framer-7dSme> — `W h e r e C a p i t a l B e c o m `)**:
   - DOM & Selectors: Landmark `<div class="framer-7dSme">` framing `W h e r e C a p i t a l B e c o m e s O w n e r s...` and `Exclusive Access` (*"The best properties never reach a listing. Ours come through an o"*) with `#c83e07` surface cards, `#0000ee` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.framer-7dSme> — `W h e r e C a p i t a l B e c o m `)` uses `40px`, `10px`, `8px`, `15px` radii, `#0000ee` highlights, and assets (suGqY6sVqYrEl8vVN4Ar3ufRvmw.png, p8gmopxLkGo6Ily14ZQSTHPOFo0.png, 3TkAWwL2xbK4k3fwlVTZWqigw.png).
5. **Colophon & Global Directory Footer (<footer.framer-UGi5s> — `https://equitifyasset.com/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-UGi5s framer-m1Hmn">` anchoring `EquitiFy Assets · Home` footer links (`Home · How We Work · Properties · about us · Contact Us`), copy *"We buy the same properties we bring to you, in the same mark"*, and `#e2e2e2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-UGi5s> — `https://equitifyasset.com/`)` aligns to `1920px` (non-`@media` desktop container stylesheet rule) with `36px` lateral canvas padding with `128px` grid gap and attributes (data-redirect-timezone="1", data-framer-generated-canonical, data-framer-font-css).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"EquitiFy Assets sources off-market commercial properties built around your vision."*
- Copy Excerpt 2: *"We run the deal end-to-end. You keep 100%."*
- Copy Excerpt 3: *"The best properties never reach a listing. Ours come through an ownership network..."*
- Copy Excerpt 4: *"We buy the same properties we bring to you, in the same markets, held to the stand..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.32,0.72,0,1)`
- **Extracted Stylesheet Rules (`equitifyasset-com`)**:
- `html.lenis body { height:auto }`
- `.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `.lenis.lenis-autoToggle { transition-property:overflow;transition-duration:1ms;transition-behavior... }`
- `.hidden-coh9ff { display:none!important }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `equitifyasset-com` stylesheet.
- **Selector `er-styles-preset-3w9o9k.rich-text...`**: `transition: color .4s cubic-bezier(.4,0,.2,1)` extracted from `equitifyasset-com` stylesheet.
- **Selector `er-styles-preset-cxxcqs.rich-text...`**: `transition: color .4s cubic-bezier(.4,0,.2,1)` extracted from `equitifyasset-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<div.framer-ebH8S>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `equitifyasset-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
