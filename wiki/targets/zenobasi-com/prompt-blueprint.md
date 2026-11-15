---
title: "UI Prompt Blueprint: zenobasi-com"
date: 2026-11-15
target: "zenobasi-com"
status: analyzed
capture: specimen
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000`)"
---

# UI Design System & Master Generation Blueprint: zenobasi-com

> **Zen Obasi — Art Director** (https://zenobasi.com) — Art director and visual strategist working across identity, campaign and editorial for brands worldwide.

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Zen Obasi — Art Director** (`https://zenobasi.com`). Art director and visual strategist working across identity, campaign and editorial for brands worldwide.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--base-100)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Google Sans Flex` for display copy (`Zen Obasi, Art Director`) with `Google Sans Flex` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 18rem`, padding `var(--edge)`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `600px` extracted from `zenobasi-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--edge)` lateral canvas padding with `18rem` grid gap.
- **Border Radius Scale**: `.5rem`, `.375rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 18rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--edge)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`, `@media (hover:none) and (pointer:coarse),(max-width:1024px)`, `@media (max-width:1000px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--base-100)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--base-300)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0c0c0c` | `.background { background-color: #0c0c0c }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-100` | `#fff` | Color / Atmospheric Token |
| `--base-200` | `rgb(255 255 255/0.5)` | Color / Atmospheric Token |
| `--base-300` | `#000` | Color / Atmospheric Token |
| `--edge` | `clamp(2rem,3.5vw,3rem)` | Dimension / Scale Token |
| `--section-gap` | `18rem` | Layout / Spatial Grid Token |
| `--text-small` | `0.7rem` | Typography Ink Token |
| `--text-large` | `clamp(16px,3.5vw,24px)` | Typography Ink Token |
| `--side-reach` | `3.5em` | Dimension / Scale Token |
| `--font-sans` | `"Google Sans Flex"` | Typography / Scale Token |
| `--backdrop` | `0 0 0` | Design System Custom Token |
| `--digit-h` | `1.1em` | Dimension / Scale Token |
| `--fill-mobile` | `0.75` | Design System Custom Token |
| `--fill-desktop` | `0.45` | Design System Custom Token |
| `--zenobasi-com-bg` | `#fff` | Canvas Substrate (from `var(--base-100)` in `:root`) |
| `--zenobasi-com-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--zenobasi-com-surface` | `#0c0c0c` | Surface Substrate (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Google Sans Flex`.
- **Primary Body Stack**: `Google Sans Flex`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-large)`, `var(--text-small)`, `clamp(1.5rem,7vw,2rem)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-large)`, `var(--text-small)`, `clamp(1.5rem,7vw,2rem)`).
- **Body Copy**: rule `,p` (`font-size: var(--text-small)`, `line-height: 1.35`, `font-weight: 400`).
- **Metadata & Navigation Labels**: CSS variables `--text-small: 0.7rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.menu-toggle`**: `transition: color .35s ease` extracted from `zenobasi-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Zen Obasi — Art Director                   │
│ ====================================================================== │
│ [ <nav.lenis>              | Index Index · Work Work · About About  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.background>                                    |   │
│ | H1: Zen Obasi, Art Director                                      |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.container>          ) max-w: 600px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Zen Obasi Zen Obasi          |  | Art Direction / Visual Ident | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 18rem ) | │
│ | [<nav.lenis>] -> [<main.background>] -> [<main.container>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer-pinned>) | https://zenobasi.com               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.lenis> — `zenobasi-com`)**:
   - Landmark `<nav class="lenis">` hosting `Zen Obasi — Art Director` navigation (`Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/css/5f4..."`, `data-engine="three.js r186"`, `data-copy="lines"`), and stylesheet rule `html { overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<main.background> — `Zen Obasi, Art Director`)**:
   - Landmark `<main class="background">` presenting display lead `Zen Obasi, Art Director` and copy excerpt *"Zen Obasi Zen Obasi"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.container> — `Zen Obasi Zen Obasi`)**:
   - Landmark `<main class="container">` rendering section `Zen Obasi Zen Obasi` with copy *"Art Direction / Visual Identity"*, asset references (`2adbc45882a5a7c5.p.woff2`, `webpack-b827b2449ca92f38.js`, `4bd1b696-228d6cc6681fc189.js`, `826-cff36fe3db5d20f7.js`), and grid rule `body { font-family:var(--font-sans),sans-serif;background-color:var(--base-300)... }`.
4. **Interactive Detail & Feature Matrix (<main.menu-toggle> — `Art Direction / Visual Identity`)**:
   - Landmark `<main class="menu-toggle">` framing `Art Direction / Visual Identity` and `Accepting Briefs for S/S 2027` (*"Accepting Briefs for S/S 2027"*) with `#0c0c0c` surface cards, `#000` accents, and `selection { background-color:var(--base-100);color:var(--base-300) }`.
5. **Colophon & Global Directory Footer (<footer.footer-pinned> — `https://zenobasi.com`)**:
   - Landmark `<footer class="footer-pinned footer-simple">` anchoring `Zen Obasi — Art Director` footer links (`Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`), copy *"Art Direction / Visual Identity"*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: zenobasi-com (Zen Obasi — Art Director)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `zenobasi-com` (**Zen Obasi — Art Director** — `https://zenobasi.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000`).
- **Identity & Domain Context**: Art director and visual strategist working across identity, campaign and editorial for brands worldwide.
- **Primary Substrate**: `#fff` (`var(--base-100)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--base-100)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Google Sans Flex` for display copy (`Zen Obasi, Art Director`) with `Google Sans Flex` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 18rem`, padding `var(--edge)`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `zenobasi-com` in your global stylesheet:

:root {
  /* Zen Obasi — Art Director (zenobasi-com) — Ground-Truth Extracted CSS Variables */
  --base-100: #fff; /* Color / Atmospheric Token (zenobasi-com) */
  --base-200: rgb(255 255 255/0.5); /* Color / Atmospheric Token (zenobasi-com) */
  --base-300: #000; /* Color / Atmospheric Token (zenobasi-com) */
  --edge: clamp(2rem,3.5vw,3rem); /* Dimension / Scale Token (zenobasi-com) */
  --section-gap: 18rem; /* Layout / Spatial Grid Token (zenobasi-com) */
  --text-small: 0.7rem; /* Typography Ink Token (zenobasi-com) */
  --text-large: clamp(16px,3.5vw,24px); /* Typography Ink Token (zenobasi-com) */
  --side-reach: 3.5em; /* Dimension / Scale Token (zenobasi-com) */
  --font-sans: "Google Sans Flex"; /* Typography / Scale Token (zenobasi-com) */
  --backdrop: 0 0 0; /* Design System Custom Token (zenobasi-com) */
  --digit-h: 1.1em; /* Dimension / Scale Token (zenobasi-com) */
  --fill-mobile: 0.75; /* Design System Custom Token (zenobasi-com) */
  --fill-desktop: 0.45; /* Design System Custom Token (zenobasi-com) */
  --zenobasi-com-bg: #fff; /* Canvas Substrate (from `var(--base-100)` in `:root`) (zenobasi-com) */
  --zenobasi-com-ink: #000; /* Primary Typography Ink (stylesheet-derived) (zenobasi-com) */
  --zenobasi-com-surface: #0c0c0c; /* Surface Substrate (stylesheet-derived) (zenobasi-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--base-100)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--base-300)` in `:root`
- **Elevated Surface / Card Substrate**: `#0c0c0c` — grounded in `.background { background-color: #0c0c0c }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `600px` extracted from `zenobasi-com` stylesheet
- **Padding & Gutters**: `var(--edge)` lateral canvas padding with `18rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 18rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--edge)` horizontal padding
- **Media Queries**: `@media (max-width:600px)`, `@media (hover:none) and (pointer:coarse),(max-width:1024px)`, `@media (max-width:1000px)`
- **Corner Radii**: `.5rem`, `.375rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Google Sans Flex`
- **Body Font Stack**: `Google Sans Flex`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-large)`, `var(--text-small)`, `clamp(1.5rem,7vw,2rem)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-large)`, `var(--text-small)`, `clamp(1.5rem,7vw,2rem)`)
- **Body Copy Rule**: rule `,p` (`font-size: var(--text-small)`, `line-height: 1.35`, `font-weight: 400`)
- **Metadata & Index Rule**: CSS variables `--text-small: 0.7rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `zenobasi-com` (`Zen Obasi — Art Director`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.lenis> — `zenobasi-com`)**:
   - DOM & Selectors: Landmark `<nav class="lenis">` hosting `Zen Obasi — Art Director` navigation (`Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/css/5f4..."`, `data-engine="three.js r186"`, `data-copy="lines"`), and stylesheet rule `html { overflow-x:clip }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.lenis> — `zenobasi-com`)` (`zenobasi-com`) adapts across `@media (max-width:600px)`, `@media (hover:none) and (pointer:coarse),(max-width:1024px)`, `@media (max-width:1000px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`.
2. **Hero Stage & Focal Lead (<main.background> — `Zen Obasi, Art Director`)**:
   - DOM & Selectors: Landmark `<main class="background">` presenting display lead `Zen Obasi, Art Director` and copy excerpt *"Zen Obasi Zen Obasi"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `Zen Obasi, Art Director`.
3. **Primary Showcase & Content Grid (<main.container> — `Zen Obasi Zen Obasi`)**:
   - DOM & Selectors: Landmark `<main class="container">` rendering section `Zen Obasi Zen Obasi` with copy *"Art Direction / Visual Identity"*, asset references (`2adbc45882a5a7c5.p.woff2`, `webpack-b827b2449ca92f38.js`, `4bd1b696-228d6cc6681fc189.js`, `826-cff36fe3db5d20f7.js`), and grid rule `body { font-family:var(--font-sans),sans-serif;background-color:var(--base-300)... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.container> — `Zen Obasi Zen Obasi`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 18rem`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--edge)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.menu-toggle> — `Art Direction / Visual Identity`)**:
   - DOM & Selectors: Landmark `<main class="menu-toggle">` framing `Art Direction / Visual Identity` and `Accepting Briefs for S/S 2027` (*"Accepting Briefs for S/S 2027"*) with `#0c0c0c` surface cards, `#000` accents, and `selection { background-color:var(--base-100);color:var(--base-300) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.menu-toggle> — `Art Direction / Visual Identity`)` uses `.5rem`, `.375rem` radii, `#000` highlights, and assets (2adbc45882a5a7c5.p.woff2, webpack-b827b2449ca92f38.js, 4bd1b696-228d6cc6681fc189.js).
5. **Colophon & Global Directory Footer (<footer.footer-pinned> — `https://zenobasi.com`)**:
   - DOM & Selectors: Landmark `<footer class="footer-pinned footer-simple">` anchoring `Zen Obasi — Art Director` footer links (`Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`), copy *"Art Direction / Visual Identity"*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer-pinned> — `https://zenobasi.com`)` aligns to `600px` extracted from `zenobasi-com` stylesheet with `var(--edge)` lateral canvas padding with `18rem` grid gap and attributes (data-precedence="next", data-href="/_next/static/css/5f4...", data-engine="three.js r186").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Zen Obasi Zen Obasi"*
- Copy Excerpt 2: *"Art Direction / Visual Identity"*
- Copy Excerpt 3: *"Accepting Briefs for S/S 2027"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`zenobasi-com`)**:
- `html { overflow-x:clip }`
- `body { font-family:var(--font-sans),sans-serif;background-color:var(--base-300)... }`
- `selection { background-color:var(--base-100);color:var(--base-300) }`
- `html.lenis body { height:auto }`
- `.lenis.lenis-stopped { overflow:hidden }`
- **Per-Selector Transition Rules**:
- **Selector `.menu-toggle`**: `transition: color .35s ease` extracted from `zenobasi-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `zenobasi-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
