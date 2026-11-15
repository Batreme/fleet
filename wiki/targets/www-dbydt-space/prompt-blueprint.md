---
title: "UI Prompt Blueprint: www-dbydt-space"
date: 2026-11-15
target: "[[overview|www-dbydt-space]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#EEEBE4` / `#000`)"
---

# UI Design System & Master Generation Blueprint: www-dbydt-space

> **Deebak Tamilmani · Design Portfolio** (https://www.dbydt.space) — Design portfolio of Deebak Tamilmani. Fragments of architecture and design projects, held as memory rather than archive, drawn in real ti...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-dbydt-space/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Deebak Tamilmani · Design Portfolio** (`https://www.dbydt.space`). Design portfolio of Deebak Tamilmani. Fragments of architecture and design projects, held as memory rather than archive, drawn in real ti...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#EEEBE4` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#EEEBE4` (`var(--project-surface)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Lay Grotesk` for display copy (`Deebak Tamilmani · Design Portfolio`) with `Geist Pixel` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `40ch` container bounds (`gap: 3px`, padding `8px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-dbydt-space/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40ch` extracted from `www-dbydt-space` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `3px` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: 3px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#EEEBE4` | `var(--project-surface)` in `:root` |
| **Primary Typography Ink** | `#2b2b2b` | `.project-content-text-legend { color: #2b2b2b }` |
| **Elevated Surface / Card Substrate** | `#6b675f` | `t-content-text p.project-conten... { color: #6b675f }` |
| **Interactive Accent / Highlight** | `#000` | `.bento-hello { background: #000 }` |
| **Secondary / Muted Copy** | `#fff` | SVG/DOM `fill="#fff"` attribute in `dom.html` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pg-annot-mark-thickness` | `1.5px` | Dimension / Scale Token |
| `--pg-annot-bracket-size` | `8px` | Layout / Spatial Grid Token |
| `--fullscreen-ruler-reveal-inset` | `0%` | Dimension / Scale Token |
| `--project-surface` | `#EEEBE4` | Canvas / Surface Token |
| `--scene-clip-left` | `100%` | Dimension / Scale Token |
| `--bhp-caption-row-height` | `44px` | Layout / Spatial Grid Token |
| `--bhp-caption-top-padding` | `16px` | Layout / Spatial Grid Token |
| `--card-slot` | `max(300px, 25%)` | Dimension / Scale Token |
| `--ruler-height` | `30px` | Layout / Spatial Grid Token |
| `--ruler-label-top` | `30px` | Dimension / Scale Token |
| `--bento-title-size` | `clamp(5rem, min(16vw, 15vh), 8rem)` | Layout / Spatial Grid Token |
| `--stack-unit` | `40px` | Dimension / Scale Token |
| `--frame-inset` | `24px` | Dimension / Scale Token |
| `--page-height` | `900px` | Layout / Spatial Grid Token |
| `--ruler-top` | `184px` | Dimension / Scale Token |
| `--ruler-right` | `364px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Lay Grotesk`.
- **Primary Body Stack**: `Geist Pixel`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `8px`, `11px`, `16px`, `clamp(1.05rem,.24rem + 1.9vw,2rem)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `8px`, `11px`, `16px`, `clamp(1.05rem,.24rem + 1.9vw,2rem)`).
- **Body Copy**: rule `p` (`font-size: 10px`, `line-height: 1.4`, `font-weight: 300`).
- **Metadata & Navigation Labels**: CSS variables `--bhp-caption-row-height: 44px`, `--bhp-caption-top-padding: 16px`, `--ruler-label-top: 30px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.pg-annot`**: `transition: opacity .3s ease` extracted from `www-dbydt-space` stylesheet.
- **Selector `.pg-annot-plus`**: `transition: opacity .3s ease` extracted from `www-dbydt-space` stylesheet.
- **Selector `.pg-annot-brackets`**: `transition: opacity .16s ease` extracted from `www-dbydt-space` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.bento-hello-scrub-scroller>` and `<main.bento-hello-page>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Deebak Tamilmani · Design Portfolio        │
│ ====================================================================== │
│ [ <header.bento-hello-scru | Hues of Al'Ula · A Street Within · Ola ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.lenis>                                         |   │
│ | H1: Deebak Tamilmani · Design Portfolio                          |   │
│ | Substrate: #EEEBE4    | Ink: #000       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.bento-hello-page>   ) max-w: 40ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Projects                     |  | Research                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3px   ) | │
│ | [<header.bento-hell] -> [<main.lenis>] -> [<main.bento-hello-] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bento-hello-sc) | https://www.dbydt.space            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.bento-hello-scrub-scroller> — `www-dbydt-space`)**:
   - Landmark `<header class="bento-hello-scrub-scroller">` hosting `Deebak Tamilmani · Design Portfolio` navigation (`Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`), DOM attributes (`data-website-id="8efd2acd-25e0-4014-bc..."`, `data-host-url="https://www.dbydt.space"`, `data-aspect="landscape"`, `data-engine="three.js r184 webgpu"`), and stylesheet rule `root { font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:eeebe4;bac... }`.
2. **Hero Stage & Focal Lead (<main.lenis> — `Deebak Tamilmani · Design Portfoli`)**:
   - Landmark `<main class="lenis">` presenting display lead `Deebak Tamilmani · Design Portfolio` and copy excerpt *"Over the years, I have worked on many projects. Some were built, "* over `#EEEBE4` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.bento-hello-page> — `Projects`)**:
   - Landmark `<main class="bento-hello-page">` rendering section `Projects` with copy *"Hues of Al'Ula is a farm dwelling in the Cultural Oasis of Al'Ula"*, asset references (`favicon.svg`, `favicon-512.png`, `favicon-180.png`, `GeistPixel-Square.woff2`), and grid rule `.app { width:100%;height:100%;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<main.bento-hello> — `Research`)**:
   - Landmark `<main class="bento-hello">` framing `Research` and `Experience and education` (*"A Street Within is an office for a real estate developer in Ahmed"*) with `#6b675f` surface cards, `#000` accents, and `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
5. **Colophon & Global Directory Footer (<footer.bento-hello-scene> — `https://www.dbydt.space`)**:
   - Landmark `<footer class="bento-hello-scene">` anchoring `Deebak Tamilmani · Design Portfo` footer links (`Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`), copy *"Olakh , the Marathi word for identity, reimagines the Pre-Em"*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-dbydt-space (Deebak Tamilmani · Design Portfolio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-dbydt-space` (**Deebak Tamilmani · Design Portfolio** — `https://www.dbydt.space`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#EEEBE4` / `#000`).
- **Identity & Domain Context**: Design portfolio of Deebak Tamilmani. Fragments of architecture and design projects, held as memory rather than archive, drawn in real ti...
- **Primary Substrate**: `#EEEBE4` (`var(--project-surface)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#EEEBE4` (`var(--project-surface)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Lay Grotesk` for display copy (`Deebak Tamilmani · Design Portfolio`) with `Geist Pixel` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `40ch` container bounds (`gap: 3px`, padding `8px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-dbydt-space` in your global stylesheet:

:root {
  /* Deebak Tamilmani · Design Portfolio (www-dbydt-space) — Ground-Truth Extracted CSS Variables */
  --pg-annot-mark-thickness: 1.5px; /* Dimension / Scale Token (www-dbydt-space) */
  --pg-annot-bracket-size: 8px; /* Layout / Spatial Grid Token (www-dbydt-space) */
  --fullscreen-ruler-reveal-inset: 0%; /* Dimension / Scale Token (www-dbydt-space) */
  --project-surface: #EEEBE4; /* Canvas / Surface Token (www-dbydt-space) */
  --scene-clip-left: 100%; /* Dimension / Scale Token (www-dbydt-space) */
  --bhp-caption-row-height: 44px; /* Layout / Spatial Grid Token (www-dbydt-space) */
  --bhp-caption-top-padding: 16px; /* Layout / Spatial Grid Token (www-dbydt-space) */
  --card-slot: max(300px, 25%); /* Dimension / Scale Token (www-dbydt-space) */
  --ruler-height: 30px; /* Layout / Spatial Grid Token (www-dbydt-space) */
  --ruler-label-top: 30px; /* Dimension / Scale Token (www-dbydt-space) */
  --bento-title-size: clamp(5rem, min(16vw, 15vh), 8rem); /* Layout / Spatial Grid Token (www-dbydt-space) */
  --stack-unit: 40px; /* Dimension / Scale Token (www-dbydt-space) */
  --frame-inset: 24px; /* Dimension / Scale Token (www-dbydt-space) */
  --page-height: 900px; /* Layout / Spatial Grid Token (www-dbydt-space) */
  --ruler-top: 184px; /* Dimension / Scale Token (www-dbydt-space) */
  --ruler-right: 364px; /* Dimension / Scale Token (www-dbydt-space) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#EEEBE4` — grounded in `var(--project-surface)` in `:root`
- **Primary Typography Ink**: `#2b2b2b` — grounded in `.project-content-text-legend { color: #2b2b2b }`
- **Elevated Surface / Card Substrate**: `#6b675f` — grounded in `t-content-text p.project-conten... { color: #6b675f }`
- **Interactive Accent / Highlight**: `#000` — grounded in `.bento-hello { background: #000 }`
- **Secondary / Muted Copy**: `#fff` — grounded in SVG/DOM `fill="#fff"` attribute in `dom.html`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40ch` extracted from `www-dbydt-space` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `3px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: 3px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Lay Grotesk`
- **Body Font Stack**: `Geist Pixel`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `8px`, `11px`, `16px`, `clamp(1.05rem,.24rem + 1.9vw,2rem)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `8px`, `11px`, `16px`, `clamp(1.05rem,.24rem + 1.9vw,2rem)`)
- **Body Copy Rule**: rule `p` (`font-size: 10px`, `line-height: 1.4`, `font-weight: 300`)
- **Metadata & Index Rule**: CSS variables `--bhp-caption-row-height: 44px`, `--bhp-caption-top-padding: 16px`, `--ruler-label-top: 30px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-dbydt-space` (`Deebak Tamilmani · Design Portfolio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.bento-hello-scrub-scroller> — `www-dbydt-space`)**:
   - DOM & Selectors: Landmark `<header class="bento-hello-scrub-scroller">` hosting `Deebak Tamilmani · Design Portfolio` navigation (`Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`), DOM attributes (`data-website-id="8efd2acd-25e0-4014-bc..."`, `data-host-url="https://www.dbydt.space"`, `data-aspect="landscape"`, `data-engine="three.js r184 webgpu"`), and stylesheet rule `root { font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:eeebe4;bac... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.bento-hello-scrub-scroller> — `www-dbydt-space`)` (`www-dbydt-space`) adapts across `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`.
2. **Hero Stage & Focal Lead (<main.lenis> — `Deebak Tamilmani · Design Portfoli`)**:
   - DOM & Selectors: Landmark `<main class="lenis">` presenting display lead `Deebak Tamilmani · Design Portfolio` and copy excerpt *"Over the years, I have worked on many projects. Some were built, "* over `#EEEBE4` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#EEEBE4` background with `#000` headline `Deebak Tamilmani · Design Portfolio`.
3. **Primary Showcase & Content Grid (<main.bento-hello-page> — `Projects`)**:
   - DOM & Selectors: Landmark `<main class="bento-hello-page">` rendering section `Projects` with copy *"Hues of Al'Ula is a farm dwelling in the Cultural Oasis of Al'Ula"*, asset references (`favicon.svg`, `favicon-512.png`, `favicon-180.png`, `GeistPixel-Square.woff2`), and grid rule `.app { width:100%;height:100%;margin:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.bento-hello-page> — `Projects`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: 3px`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.bento-hello> — `Research`)**:
   - DOM & Selectors: Landmark `<main class="bento-hello">` framing `Research` and `Experience and education` (*"A Street Within is an office for a real estate developer in Ahmed"*) with `#6b675f` surface cards, `#000` accents, and `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.bento-hello> — `Research`)` uses `50%` radii, `#000` highlights, and assets (favicon.svg, favicon-512.png, favicon-180.png).
5. **Colophon & Global Directory Footer (<footer.bento-hello-scene> — `https://www.dbydt.space`)**:
   - DOM & Selectors: Landmark `<footer class="bento-hello-scene">` anchoring `Deebak Tamilmani · Design Portfo` footer links (`Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`), copy *"Olakh , the Marathi word for identity, reimagines the Pre-Em"*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bento-hello-scene> — `https://www.dbydt.space`)` aligns to `40ch` extracted from `www-dbydt-space` stylesheet with `8px` lateral canvas padding with `3px` grid gap and attributes (data-website-id="8efd2acd-25e0-4014-bc...", data-host-url="https://www.dbydt.space", data-aspect="landscape").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Over the years, I have worked on many projects. Some were built, some were develop..."*
- Copy Excerpt 2: *"Hues of Al'Ula is a farm dwelling in the Cultural Oasis of Al'Ula, a landscape tha..."*
- Copy Excerpt 3: *"A Street Within is an office for a real estate developer in Ahmedabad, planned aro..."*
- Copy Excerpt 4: *"Olakh , the Marathi word for identity, reimagines the Pre-Embarkation Security Che..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-dbydt-space`)**:
- `root { font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:eeebe4;bac... }`
- `.app { width:100%;height:100%;margin:0 }`
- `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`
- `.nav-scroll-spacer { width:1px;pointer-events:none;visibility:hidden }`
- `html.lenis.lenis-smooth { scroll-behavior:auto!important }`
- **Per-Selector Transition Rules**:
- **Selector `.pg-annot`**: `transition: opacity .3s ease` extracted from `www-dbydt-space` stylesheet.
- **Selector `.pg-annot-plus`**: `transition: opacity .3s ease` extracted from `www-dbydt-space` stylesheet.
- **Selector `.pg-annot-brackets`**: `transition: opacity .16s ease` extracted from `www-dbydt-space` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.bento-hello-scrub-scroller>` and `<main.bento-hello-page>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-dbydt-space`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
