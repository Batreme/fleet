---
title: "UI Prompt Blueprint: tabletales-crz-studio"
date: 2026-11-15
target: "tabletales-crz-studio"
status: analyzed
capture: specimen
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#08335d` / `#c98f2e`)"
---

# UI Design System & Master Generation Blueprint: tabletales-crz-studio

> **Table Tales by CRZ.STUDIO · Board Game Collection & Play Log** (https://tabletales.crz.studio/) — Table Tales is a digital exhibition of board games as art: a curated collection and a living log of every night at the table. Designed an...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Table Tales by CRZ.STUDIO · Board Game Collection & Play Log** (`https://tabletales.crz.studio/`). Table Tales is a digital exhibition of board games as art: a curated collection and a living log of every night at the table. Designed an...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#08335d` / `#c98f2e`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#08335d` (`var(--color-blue)` in `:root`) paired with `#fdffff` primary typography and `#c98f2e` accents.
  - **Extracted Typographic Hierarchy**: Pairs `grotesk` for display copy (`T a b l e T a l e s`) with `grotesk Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1080px` container bounds (`gap: var(--space-xs)`, padding `var(--space-m)`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1080px` extracted from `tabletales-crz-studio` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--space-m)` lateral canvas padding with `var(--space-xs)` grid gap.
- **Border Radius Scale**: `1px`, `2px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1080px`, `gap: var(--space-xs)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-m)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1080px)`, `@media (max-width:700px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1200px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#08335d` | `var(--color-blue)` in `:root` |
| **Primary Typography Ink** | `#f7b538` | `var(--color-golden)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdffff` | `var(--color-azure)` in `:root` |
| **Interactive Accent / Highlight** | `#c98f2e` | `var(--color-ochre)` in `:root` |
| **Secondary / Muted Copy** | `#145a86` | `var(--color-teal)` in `:root` |
| **Structural Hairline Border** | `#010e1c` | `var(--color-night)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-blue` | `#08335d` | Brand / Palette Token |
| `--color-golden` | `#f7b538` | Brand / Palette Token |
| `--color-azure` | `#fdffff` | Brand / Palette Token |
| `--color-ochre` | `#c98f2e` | Brand / Palette Token |
| `--color-teal` | `#145a86` | Brand / Palette Token |
| `--color-night` | `#010e1c` | Brand / Palette Token |
| `--color-line-on-light` | `color-mix(in srgb, var(--color-blue) 22%, transparent)` | Canvas / Surface Token |
| `--color-line-on-dark` | `color-mix(in srgb, var(--color-azure) 22%, transparent)` | Canvas / Surface Token |
| `--color-muted-on-light` | `color-mix(in srgb, var(--color-blue) 62%, transparent)` | Canvas / Surface Token |
| `--color-muted-on-dark` | `color-mix(in srgb, var(--color-azure) 62%, transparent)` | Canvas / Surface Token |
| `--section-padding-inline` | `clamp(20px, 2.78vw, 64px)` | Layout / Spatial Grid Token |
| `--section-padding-block` | `clamp(72px, 8.33vw, 160px)` | Layout / Spatial Grid Token |
| `--measure-padding` | `clamp(0px, 18vw, 420px)` | Layout / Spatial Grid Token |
| `--space-2xs` | `4px` | Layout / Spatial Grid Token |
| `--space-xs` | `8px` | Layout / Spatial Grid Token |
| `--space-s` | `clamp(12px, 1.11vw, 16px)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `grotesk`.
- **Primary Body Stack**: `grotesk Fallback`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "display", "display Fallback"`.
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(56px,5.6vw,120px)`, `line-height: .92`, `letter-spacing: 0`, `font-weight: 400`).
- **Body Copy**: CSS variables `--text-body: clamp(16px, 1.25vw, 20px)`; rule `p` (`font-size: var(--text-body)`, `line-height: 1.35`).
- **Metadata & Navigation Labels**: CSS variables `--text-label: clamp(12px, .9vw, 14px)`, `--text-small: clamp(14px, 1.04vw, 16px)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms!important` extracted from `tabletales-crz-studio` stylesheet.
- **Selector `._8wxUTq_closeButton`**: `transition: color var(--duration-fast) var(--ease-out)` extracted from `tabletales-crz-studio` stylesheet.
- **Selector `._8wxUTq_closeButton span:after`**: `transition: transform var(--duration-base) var(--ease-out)` extracted from `tabletales-crz-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.LYh_OG_variable>` and `<section.uxasZq_variable>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Table Tales by CRZ.STUDIO · Board Game Col │
│ ====================================================================== │
│ [ <header.LYh_OG_variable> | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.q_m67W_hero>                                |   │
│ | H1: T a b l e T a l e s                                          |   │
│ | Substrate: #08335d    | Ink: #fdffff    | Accent: #c98f2e        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.uxasZq_variable> ) max-w: 1080px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Games               |  | The play log                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.LYh_OG_var] -> [<section.q_m67W_he] -> [<section.uxasZq_va] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.tUdqrq_footer>) | https://tabletales.crz.studio/     │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.LYh_OG_variable> — `tabletales-crz-studio`)**:
   - Landmark `<header class="LYh_OG_variable">` hosting `Table Tales by CRZ.STUDIO · Board Ga` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.YZMoQq_card:focus-visible { z-index:1;outline:2px solid var(--color-golden);outline-offset:-6px }`.
2. **Hero Stage & Focal Lead (<section.q_m67W_hero> — `T a b l e T a l e s`)**:
   - Landmark `<section class="q_m67W_hero">` presenting display lead `T a b l e T a l e s` and copy excerpt *"I n s t a g r a m I n s t a g r a m"* over `#08335d` canvas and `#fdffff` ink.
3. **Primary Showcase & Content Grid (<section.uxasZq_variable> — `Featured Games`)**:
   - Landmark `<section class="uxasZq_variable">` rendering section `Featured Games` with copy *"L i n k e d I n L i n k e d I n"*, asset references (`FoundersGrotesk_Bold-s.p.2z72oy2q...`, `FoundersGrotesk_BoldItalic-s.p.2h...`, `FoundersGrotesk_Light-s.p.03ydj7u...`, `FoundersGrotesk_LightItalic-s.p.2...`), and grid rule `.YZMoQq_paint { transform-origin:top;pointer-events:none;will-change:transform;position:... }`.
4. **Interactive Detail & Feature Matrix (<section.O43udq_featured> — `The play log`)**:
   - Landmark `<section class="O43udq_featured">` framing `The play log` and `C R Z . S T U D I O C R Z . S T U D I O` (*"C R Z . S T U D I O C R Z . S T U D I O"*) with `#fdffff` surface cards, `#c98f2e` accents, and `.YZMoQq_paint:first-child { background:var(--color-golden) }`.
5. **Colophon & Global Directory Footer (<footer.tUdqrq_footer> — `https://tabletales.crz.studio/`)**:
   - Landmark `<footer class="tUdqrq_footer">` anchoring `Table Tales by CRZ.STUDIO · Boar` footer links (`Overview · Index · Archive · About · Contact`), copy *"C R Z . S T U D I O"*, and `#010e1c` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tabletales-crz-studio (Table Tales by CRZ.STUDIO · Board Game Collection & Play Log)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tabletales-crz-studio` (**Table Tales by CRZ.STUDIO · Board Game Collection & Play Log** — `https://tabletales.crz.studio/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#08335d` / `#c98f2e`).
- **Identity & Domain Context**: Table Tales is a digital exhibition of board games as art: a curated collection and a living log of every night at the table. Designed an...
- **Primary Substrate**: `#08335d` (`var(--color-blue)` in `:root`), **Primary Ink**: `#fdffff`, **Accent / Highlight**: `#c98f2e`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#08335d` (`var(--color-blue)` in `:root`) paired with `#fdffff` primary typography and `#c98f2e` accents.
  - **Extracted Typographic Hierarchy**: Pairs `grotesk` for display copy (`T a b l e T a l e s`) with `grotesk Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1080px` container bounds (`gap: var(--space-xs)`, padding `var(--space-m)`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tabletales-crz-studio` in your global stylesheet:

:root {
  /* Table Tales by CRZ.STUDIO · Board Game Collection & Play Log (tabletales-crz-studio) — Ground-Truth Extracted CSS Variables */
  --color-blue: #08335d; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-golden: #f7b538; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-azure: #fdffff; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-ochre: #c98f2e; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-teal: #145a86; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-night: #010e1c; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-line-on-light: color-mix(in srgb, var(--color-blue) 22%, transparent); /* Canvas / Surface Token (tabletales-crz-studio) */
  --color-line-on-dark: color-mix(in srgb, var(--color-azure) 22%, transparent); /* Canvas / Surface Token (tabletales-crz-studio) */
  --color-muted-on-light: color-mix(in srgb, var(--color-blue) 62%, transparent); /* Canvas / Surface Token (tabletales-crz-studio) */
  --color-muted-on-dark: color-mix(in srgb, var(--color-azure) 62%, transparent); /* Canvas / Surface Token (tabletales-crz-studio) */
  --section-padding-inline: clamp(20px, 2.78vw, 64px); /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --section-padding-block: clamp(72px, 8.33vw, 160px); /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --measure-padding: clamp(0px, 18vw, 420px); /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --space-2xs: 4px; /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --space-xs: 8px; /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --space-s: clamp(12px, 1.11vw, 16px); /* Layout / Spatial Grid Token (tabletales-crz-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#08335d` — grounded in `var(--color-blue)` in `:root`
- **Primary Typography Ink**: `#f7b538` — grounded in `var(--color-golden)` in `:root`
- **Elevated Surface / Card Substrate**: `#fdffff` — grounded in `var(--color-azure)` in `:root`
- **Interactive Accent / Highlight**: `#c98f2e` — grounded in `var(--color-ochre)` in `:root`
- **Secondary / Muted Copy**: `#145a86` — grounded in `var(--color-teal)` in `:root`
- **Structural Hairline Border**: `#010e1c` — grounded in `var(--color-night)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1080px` extracted from `tabletales-crz-studio` stylesheet
- **Padding & Gutters**: `var(--space-m)` lateral canvas padding with `var(--space-xs)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1080px`, `gap: var(--space-xs)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-m)` horizontal padding
- **Media Queries**: `@media (max-width:1080px)`, `@media (max-width:700px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1200px)`
- **Corner Radii**: `1px`, `2px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `grotesk`
- **Body Font Stack**: `grotesk Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-display: "display", "display Fallback"`
- **H2 Section Rule**: rule `h2` (`font-size: clamp(56px,5.6vw,120px)`, `line-height: .92`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy Rule**: CSS variables `--text-body: clamp(16px, 1.25vw, 20px)`; rule `p` (`font-size: var(--text-body)`, `line-height: 1.35`)
- **Metadata & Index Rule**: CSS variables `--text-label: clamp(12px, .9vw, 14px)`, `--text-small: clamp(14px, 1.04vw, 16px)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tabletales-crz-studio` (`Table Tales by CRZ.STUDIO · Board Game Collection & Play Log`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.LYh_OG_variable> — `tabletales-crz-studio`)**:
   - DOM & Selectors: Landmark `<header class="LYh_OG_variable">` hosting `Table Tales by CRZ.STUDIO · Board Ga` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.YZMoQq_card:focus-visible { z-index:1;outline:2px solid var(--color-golden);outline-offset:-6px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.LYh_OG_variable> — `tabletales-crz-studio`)` (`tabletales-crz-studio`) adapts across `@media (max-width:1080px)`, `@media (max-width:700px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1200px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.q_m67W_hero> — `T a b l e T a l e s`)**:
   - DOM & Selectors: Landmark `<section class="q_m67W_hero">` presenting display lead `T a b l e T a l e s` and copy excerpt *"I n s t a g r a m I n s t a g r a m"* over `#08335d` canvas and `#fdffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#08335d` background with `#fdffff` headline `T a b l e T a l e s`.
3. **Primary Showcase & Content Grid (<section.uxasZq_variable> — `Featured Games`)**:
   - DOM & Selectors: Landmark `<section class="uxasZq_variable">` rendering section `Featured Games` with copy *"L i n k e d I n L i n k e d I n"*, asset references (`FoundersGrotesk_Bold-s.p.2z72oy2q...`, `FoundersGrotesk_BoldItalic-s.p.2h...`, `FoundersGrotesk_Light-s.p.03ydj7u...`, `FoundersGrotesk_LightItalic-s.p.2...`), and grid rule `.YZMoQq_paint { transform-origin:top;pointer-events:none;will-change:transform;position:... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.uxasZq_variable> — `Featured Games`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1080px`, `gap: var(--space-xs)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-m)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.O43udq_featured> — `The play log`)**:
   - DOM & Selectors: Landmark `<section class="O43udq_featured">` framing `The play log` and `C R Z . S T U D I O C R Z . S T U D I O` (*"C R Z . S T U D I O C R Z . S T U D I O"*) with `#fdffff` surface cards, `#c98f2e` accents, and `.YZMoQq_paint:first-child { background:var(--color-golden) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.O43udq_featured> — `The play log`)` uses `1px`, `2px`, `50%` radii, `#c98f2e` highlights, and assets (FoundersGrotesk_Bold-s.p.2z72oy2q..., FoundersGrotesk_BoldItalic-s.p.2h..., FoundersGrotesk_Light-s.p.03ydj7u...).
5. **Colophon & Global Directory Footer (<footer.tUdqrq_footer> — `https://tabletales.crz.studio/`)**:
   - DOM & Selectors: Landmark `<footer class="tUdqrq_footer">` anchoring `Table Tales by CRZ.STUDIO · Boar` footer links (`Overview · Index · Archive · About · Contact`), copy *"C R Z . S T U D I O"*, and `#010e1c` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.tUdqrq_footer> — `https://tabletales.crz.studio/`)` aligns to `1080px` extracted from `tabletales-crz-studio` stylesheet with `var(--space-m)` lateral canvas padding with `var(--space-xs)` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"I n s t a g r a m I n s t a g r a m"*
- Copy Excerpt 2: *"L i n k e d I n L i n k e d I n"*
- Copy Excerpt 3: *"C R Z . S T U D I O C R Z . S T U D I O"*
- Copy Excerpt 4: *"C R Z . S T U D I O"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)`
- **Extracted Stylesheet Rules (`tabletales-crz-studio`)**:
- `.YZMoQq_card:focus-visible { z-index:1;outline:2px solid var(--color-golden);outline-offset:-6px }`
- `.YZMoQq_paint { transform-origin:top;pointer-events:none;will-change:transform;position:... }`
- `.YZMoQq_paint:first-child { background:var(--color-golden) }`
- `.YZMoQq_image { aspect-ratio:1;width:100%;position:relative;overflow:hidden }`
- `.YZMoQq_image img { object-fit:cover }`
- **Per-Selector Transition Rules**:
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms!important` extracted from `tabletales-crz-studio` stylesheet.
- **Selector `._8wxUTq_closeButton`**: `transition: color var(--duration-fast) var(--ease-out)` extracted from `tabletales-crz-studio` stylesheet.
- **Selector `._8wxUTq_closeButton span:after`**: `transition: transform var(--duration-base) var(--ease-out)` extracted from `tabletales-crz-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.LYh_OG_variable>` and `<section.uxasZq_variable>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tabletales-crz-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
