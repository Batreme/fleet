---
title: "UI Prompt Blueprint: later-com_made-you-look"
date: 2026-11-15
target: "later-com_made-you-look"
status: analyzed
capture: specimen
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#fff6cc` ink, `#ffd200` accent)"
---

# UI Design System & Master Generation Blueprint: later-com_made-you-look

> **Made You Look: Campaigns so good you break the algorithm.** (https://later.com/made-you-look/) — Meet the creators shaping culture through bold ideas and obsessive craft—and see how brands partner with them to build standout influence...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Made You Look: Campaigns so good you break the algorithm.** (`https://later.com/made-you-look/`). Meet the creators shaping culture through bold ideas and obsessive craft—and see how brands partner with them to build standout influence...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#fff6cc` ink, `#ffd200` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000000` (`var(--primary-color)` in `:root`) paired with `#fff6cc` primary typography and `#ffd200` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Garamond` for display copy (`Campaigns so good you break the algo`) with `Mondwest` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `630px` container bounds (`gap: 8px`, padding `6px`) with `cubic-bezier(0.41,0.94,0.71,1.41)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×18396px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `630px` extracted from `later-com_made-you-look` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `5px`, `4px`, `16px`, `var(--switchHeight)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 630px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 640px)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (max-width:325px)`, `@media screen and (-ms-high-contrast:active)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--primary-color)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--w2w-start-background-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a075ff` | `var(--outline-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ffd200` | `var(--yellow)` in `:root` |
| **Secondary / Muted Copy** | `#ffe880` | `var(--yellow-secondary)` in `:root` |
| **Structural Hairline Border** | `#fff6cc` | `var(--yellow-20)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--primary-color` | `#000000` | Brand / Palette Token |
| `--text-color` | `#000000` | Typography Ink Token |
| `--squareDimension` | `25px` | Dimension / Scale Token |
| `--switchHeight` | `20px` | Layout / Spatial Grid Token |
| `--switchGutter` | `2px` | Layout / Spatial Grid Token |
| `--switchButtonDiameter` | `calc(var(--switchHeight) - var(--switchGutter) * 2)` | Dimension / Scale Token |
| `--td176b92ada598f8f` | `initial` | Design System Custom Token |
| `--td851cd75a8793667` | `initial` | Design System Custom Token |
| `--tc58f4bf5a9869b3e` | `initial` | Design System Custom Token |
| `--t3a480c2f814ef19c` | `initial` | Design System Custom Token |
| `--t77e217518bcd986b` | `initial` | Design System Custom Token |
| `--tc5e0863356bf5767` | `initial` | Design System Custom Token |
| `--t7a2234c5eadde886` | `initial` | Design System Custom Token |
| `--td340014d093b0821` | `initial` | Design System Custom Token |
| `--tf8c80baf678711b8` | `initial` | Design System Custom Token |
| `--t2986df03ecf88759` | `initial` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Garamond`.
- **Primary Body Stack**: `Mondwest`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--h1-2xl: 3.5rem`, `--h1-xl: 3.125rem`, `--h1-l: 2.5rem`; rule `h1` (`font-size: 5rem`).
- **Section Heading (`H2`)**: CSS variables `--h2: 2.125rem`, `--h2-s: 1.875rem`, `--text-2xl: 1.25rem`; rule `h2` (`font-size: 13px`, `line-height: 15px`, `font-weight: 500`).
- **Body Copy**: CSS variables `--font-body: Inter Tight,Helvetica Neue,Helvetica,Arial,sans-serif`, `--body-line-height: 1.5`, `--body-letter-spacing: 0.01em`; rule `.paragraph` (`font-size: 14px`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: 0.875rem`, `--heading-letter-spacing: 0.005em`, `--body-letter-spacing: 0.01em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.41,0.94,0.71,1.41)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.button`**: `transition: filter 150ms, background-color 150ms` extracted from `later-com_made-you-look` stylesheet.
- **Selector `.modal-container`**: `transition: width 150ms, height 150ms` extracted from `later-com_made-you-look` stylesheet.
- **Selector `.button-base-text`**: `transition: color 150ms` extracted from `later-com_made-you-look` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.41,0.94,0.71,1.41)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.NnFvv>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Made You Look: Campaigns so good you break │
│ ====================================================================== │
│ [ <header.lenis>           | halo perez-gallardo · Timothy Goodman  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.NnFvv>                                      |   │
│ | H1: Campaigns so good you break the algorithm.                   |   │
│ | Substrate: #000000    | Ink: #fff6cc    | Accent: #ffd200        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.NnFvv>           ) max-w: 630px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Made you look                |  | halo perez-gallardo          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<header.lenis>] -> [<section.NnFvv>] -> [<section.NnFvv>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.myl-header-cta) | https://later.com/made-you-look/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `later-com_made-you-look`)**:
   - Landmark `<header class="lenis">` hosting `Made You Look: Campaigns so good you` navigation (`halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`), DOM attributes (`data-root="true"`, `data-gatsby-head="true"`, `data-gatsby-head="true"`, `data-gatsby-head="true"`), and stylesheet rule `.button:hover { background-color: var(--primary-color); }`.
2. **Hero Stage & Focal Lead (<section.NnFvv> — `Campaigns so good you break the al`)**:
   - Landmark `<section class="NnFvv">` presenting display lead `Campaigns so good you break the algorithm.` and copy excerpt *"That’s what happens when brands stop chasing trends and start wor"* over `#000000` canvas and `#fff6cc` ink.
3. **Primary Showcase & Content Grid (<section.NnFvv> — `Made you look`)**:
   - Landmark `<section class="NnFvv">` rendering section `Made you look` with copy *"At Later, we help brands partner with those creators—bringing tog"*, asset references (`InterTight-VariableFont_wght.woff2`, `superx-extrabold.woff2`, `superx-semibold.woff2`, `rss.xml`), and grid rule `.button:hover span { color: ffffff; }`.
4. **Interactive Detail & Feature Matrix (<section.NnFvv> — `halo perez-gallardo`)**:
   - Landmark `<section class="NnFvv">` framing `halo perez-gallardo` and `Timothy Goodman` (*"Because breakthrough campaigns aren’t louder. They’re more credib"*) with `#a075ff` surface cards, `#ffd200` accents, and `.button-primary-text { font-size: 12px; font-weight: 700; }`.
5. **Colophon & Global Directory Footer (<footer.myl-header-cta> — `https://later.com/made-you-look/`)**:
   - Landmark `<footer class="myl-header-cta">` anchoring `Made You Look: Campaigns so good` footer links (`halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`), copy *"Learn more about Later's services"*, and `#fff6cc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: later-com_made-you-look (Made You Look: Campaigns so good you break the algorithm.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `later-com_made-you-look` (**Made You Look: Campaigns so good you break the algorithm.** — `https://later.com/made-you-look/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#fff6cc` ink, `#ffd200` accent).
- **Identity & Domain Context**: Meet the creators shaping culture through bold ideas and obsessive craft—and see how brands partner with them to build standout influence...
- **Primary Substrate**: `#000000` (`var(--primary-color)` in `:root`), **Primary Ink**: `#fff6cc`, **Accent / Highlight**: `#ffd200`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000000` (`var(--primary-color)` in `:root`) paired with `#fff6cc` primary typography and `#ffd200` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Garamond` for display copy (`Campaigns so good you break the algo`) with `Mondwest` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `630px` container bounds (`gap: 8px`, padding `6px`) with `cubic-bezier(0.41,0.94,0.71,1.41)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `later-com_made-you-look` in your global stylesheet:

:root {
  /* Made You Look: Campaigns so good you break the algorithm. (later-com_made-you-look) — Ground-Truth Extracted CSS Variables */
  --primary-color: #000000; /* Brand / Palette Token (later-com_made-you-look) */
  --text-color: #000000; /* Typography Ink Token (later-com_made-you-look) */
  --squareDimension: 25px; /* Dimension / Scale Token (later-com_made-you-look) */
  --switchHeight: 20px; /* Layout / Spatial Grid Token (later-com_made-you-look) */
  --switchGutter: 2px; /* Layout / Spatial Grid Token (later-com_made-you-look) */
  --switchButtonDiameter: calc(var(--switchHeight) - var(--switchGutter) * 2); /* Dimension / Scale Token (later-com_made-you-look) */
  --td176b92ada598f8f: initial; /* Design System Custom Token (later-com_made-you-look) */
  --td851cd75a8793667: initial; /* Design System Custom Token (later-com_made-you-look) */
  --tc58f4bf5a9869b3e: initial; /* Design System Custom Token (later-com_made-you-look) */
  --t3a480c2f814ef19c: initial; /* Design System Custom Token (later-com_made-you-look) */
  --t77e217518bcd986b: initial; /* Design System Custom Token (later-com_made-you-look) */
  --tc5e0863356bf5767: initial; /* Design System Custom Token (later-com_made-you-look) */
  --t7a2234c5eadde886: initial; /* Design System Custom Token (later-com_made-you-look) */
  --td340014d093b0821: initial; /* Design System Custom Token (later-com_made-you-look) */
  --tf8c80baf678711b8: initial; /* Design System Custom Token (later-com_made-you-look) */
  --t2986df03ecf88759: initial; /* Design System Custom Token (later-com_made-you-look) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in `var(--primary-color)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--w2w-start-background-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#a075ff` — grounded in `var(--outline-color)` in `:root`
- **Interactive Accent / Highlight**: `#ffd200` — grounded in `var(--yellow)` in `:root`
- **Secondary / Muted Copy**: `#ffe880` — grounded in `var(--yellow-secondary)` in `:root`
- **Structural Hairline Border**: `#fff6cc` — grounded in `var(--yellow-20)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×18396px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `630px` extracted from `later-com_made-you-look` stylesheet
- **Padding & Gutters**: `6px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 630px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (min-width: 640px)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (max-width:325px)`, `@media screen and (-ms-high-contrast:active)`
- **Corner Radii**: `5px`, `4px`, `16px`, `var(--switchHeight)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Garamond`
- **Body Font Stack**: `Mondwest`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--h1-2xl: 3.5rem`, `--h1-xl: 3.125rem`, `--h1-l: 2.5rem`; rule `h1` (`font-size: 5rem`)
- **H2 Section Rule**: CSS variables `--h2: 2.125rem`, `--h2-s: 1.875rem`, `--text-2xl: 1.25rem`; rule `h2` (`font-size: 13px`, `line-height: 15px`, `font-weight: 500`)
- **Body Copy Rule**: CSS variables `--font-body: Inter Tight,Helvetica Neue,Helvetica,Arial,sans-serif`, `--body-line-height: 1.5`, `--body-letter-spacing: 0.01em`; rule `.paragraph` (`font-size: 14px`)
- **Metadata & Index Rule**: CSS variables `--text-xs: 0.875rem`, `--heading-letter-spacing: 0.005em`, `--body-letter-spacing: 0.01em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `later-com_made-you-look` (`Made You Look: Campaigns so good you break the algorithm.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `later-com_made-you-look`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Made You Look: Campaigns so good you` navigation (`halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`), DOM attributes (`data-root="true"`, `data-gatsby-head="true"`, `data-gatsby-head="true"`, `data-gatsby-head="true"`), and stylesheet rule `.button:hover { background-color: var(--primary-color); }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `later-com_made-you-look`)` (`later-com_made-you-look`) adapts across `@media (min-width: 640px)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (max-width:325px)`, `@media screen and (-ms-high-contrast:active)` with `cubic-bezier(0.41,0.94,0.71,1.41)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`.
2. **Hero Stage & Focal Lead (<section.NnFvv> — `Campaigns so good you break the al`)**:
   - DOM & Selectors: Landmark `<section class="NnFvv">` presenting display lead `Campaigns so good you break the algorithm.` and copy excerpt *"That’s what happens when brands stop chasing trends and start wor"* over `#000000` canvas and `#fff6cc` ink.
   - Responsive Contract: Hero stage (`1440×18396px` desktop / `390×2400px` mobile) sets `#000000` background with `#fff6cc` headline `Campaigns so good you break the algorithm.`.
3. **Primary Showcase & Content Grid (<section.NnFvv> — `Made you look`)**:
   - DOM & Selectors: Landmark `<section class="NnFvv">` rendering section `Made you look` with copy *"At Later, we help brands partner with those creators—bringing tog"*, asset references (`InterTight-VariableFont_wght.woff2`, `superx-extrabold.woff2`, `superx-semibold.woff2`, `rss.xml`), and grid rule `.button:hover span { color: ffffff; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.NnFvv> — `Made you look`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 630px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.NnFvv> — `halo perez-gallardo`)**:
   - DOM & Selectors: Landmark `<section class="NnFvv">` framing `halo perez-gallardo` and `Timothy Goodman` (*"Because breakthrough campaigns aren’t louder. They’re more credib"*) with `#a075ff` surface cards, `#ffd200` accents, and `.button-primary-text { font-size: 12px; font-weight: 700; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.NnFvv> — `halo perez-gallardo`)` uses `5px`, `4px`, `16px`, `var(--switchHeight)` radii, `#ffd200` highlights, and assets (InterTight-VariableFont_wght.woff2, superx-extrabold.woff2, superx-semibold.woff2).
5. **Colophon & Global Directory Footer (<footer.myl-header-cta> — `https://later.com/made-you-look/`)**:
   - DOM & Selectors: Landmark `<footer class="myl-header-cta">` anchoring `Made You Look: Campaigns so good` footer links (`halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`), copy *"Learn more about Later's services"*, and `#fff6cc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.myl-header-cta> — `https://later.com/made-you-look/`)` aligns to `630px` extracted from `later-com_made-you-look` stylesheet with `6px` lateral canvas padding with `8px` grid gap and attributes (data-root="true", data-gatsby-head="true", data-gatsby-head="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"That’s what happens when brands stop chasing trends and start working with creator..."*
- Copy Excerpt 2: *"At Later, we help brands partner with those creators—bringing together trusted ins..."*
- Copy Excerpt 3: *"Because breakthrough campaigns aren’t louder. They’re more credible."*
- Copy Excerpt 4: *"Learn more about Later's services"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.41,0.94,0.71,1.41)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`later-com_made-you-look`)**:
- `.button:hover { background-color: var(--primary-color); }`
- `.button:hover span { color: ffffff; }`
- `.button-primary-text { font-size: 12px; font-weight: 700; }`
- `.button-secondary-text { font-size: 9px; font-weight: 400; }`
- `button:focus { outline: 2px solid rgba(51, 157, 255, 0.7); }`
- **Per-Selector Transition Rules**:
- **Selector `.button`**: `transition: filter 150ms, background-color 150ms` extracted from `later-com_made-you-look` stylesheet.
- **Selector `.modal-container`**: `transition: width 150ms, height 150ms` extracted from `later-com_made-you-look` stylesheet.
- **Selector `.button-base-text`**: `transition: color 150ms` extracted from `later-com_made-you-look` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.41,0.94,0.71,1.41)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.NnFvv>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `later-com_made-you-look`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
