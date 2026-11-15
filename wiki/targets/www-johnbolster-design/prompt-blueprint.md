---
title: "UI Prompt Blueprint: www-johnbolster-design"
date: 2026-11-15
target: "[[overview|www-johnbolster-design]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ECEAE2` / `#D3D0C6`)"
---

# UI Design System & Master Generation Blueprint: www-johnbolster-design

> **John Bolster · Brand Identity Designer and Art Director, Saratoga Spring...** (https://www.johnbolster.design/) — Independent brand identity designer and art director in Saratoga Springs, NY. Brand strategy, identity, print and web for businesses, hig...

![Desktop Viewport Capture (1440x24580)](file:///root/projects/fleet/wiki/targets/www-johnbolster-design/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **John Bolster · Brand Identity Designer and Art Director, Saratoga Spring...** (`https://www.johnbolster.design/`). Independent brand identity designer and art director in Saratoga Springs, NY. Brand strategy, identity, print and web for businesses, hig...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ECEAE2` / `#D3D0C6`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ECEAE2` (`var(--bg)` in `:root`) paired with `#121413` primary typography and `#D3D0C6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Serif Display` for display copy (`About John Bolster`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `34ch` container bounds (`gap: 12px`, padding `var(--gut)`) with `cubic-bezier(.7,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-johnbolster-design/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×24580px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `34ch` extracted from `www-johnbolster-design` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--gut)` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `2px`, `50%`, `999px`, `10px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34ch`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px)and (max-height:780px)`, `@media (max-width:400px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ECEAE2` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#121413` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5E6360` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#D3D0C6` | `var(--hair)` in `:root` |
| **Secondary / Muted Copy** | `#2234E0` | `var(--line)` in `:root` |
| **Structural Hairline Border** | `#F47920` | `var(--orange)` in `:root` |
| **Variable Token (`--black`)** | `#0A0A0A` | `var(--black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#ECEAE2` | Canvas / Surface Token |
| `--ink` | `#121413` | Typography Ink Token |
| `--muted` | `#5E6360` | Color / Atmospheric Token |
| `--hair` | `#D3D0C6` | Color / Atmospheric Token |
| `--line` | `#2234E0` | Color / Atmospheric Token |
| `--orange` | `#F47920` | Color / Atmospheric Token |
| `--black` | `#0A0A0A` | Canvas / Surface Token |
| `--display` | `"BebasPro","Bebas Neue","Arial Narrow",Impact,sans-serif` | Design System Custom Token |
| `--body` | `"Geist",ui-sans-serif,system-ui,sans-serif` | Dimension / Scale Token |
| `--mono` | `"Geist Mono",ui-monospace,Menlo,monospace` | Typography / Scale Token |
| `--serif` | `"DM Serif Display",Georgia,serif` | Typography / Scale Token |
| `--gut` | `max(16px, env(safe-area-inset-left, 0px))` | Dimension / Scale Token |
| `--gutR` | `max(16px, env(safe-area-inset-right, 0px))` | Dimension / Scale Token |
| `--fp` | `1` | Design System Custom Token |
| `--sc` | `var(--ink)` | Design System Custom Token |
| `--on` | `clamp(0, calc((var(--fp) * 1.7 - var(--li,0) * .22) * 15 - var(--i)), 1)` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DM Serif Display`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--display: "BebasPro","Bebas Neue","Arial Narrow",Impact,sans-serif`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `11px`, `clamp(15px,1.15vw,18px)`, `14px`, `22px`).
- **Body Copy**: CSS variables `--body: "Geist",ui-sans-serif,system-ui,sans-serif`; rule `p` (`font-size: clamp(15px,1.15vw,18px)`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: CSS variables `--mono: "Geist Mono",ui-monospace,Menlo,monospace`; rule `.mono` (`font-size: 12px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.3,1.6,.4,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.burger i:after`**: `transition: transform .5s cubic-bezier(.7,0,.2,1)` extracted from `www-johnbolster-design` stylesheet.
- **Selector `#menu`**: `transition: clip-path .9s cubic-bezier(.7,0,.2,1)` extracted from `www-johnbolster-design` stylesheet.
- **Selector `#menu a`**: `transition: transform .9s cubic-bezier(.7,0,.2,1)` extracted from `www-johnbolster-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,0,.2,1)`)**: Governs interactive state transitions across `<header.bar>` and `<section.st>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — John Bolster · Brand Identity Designer and │
│ ====================================================================== │
│ [ <header.bar>             | 01 About · 02 Journey · 03 What I do · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.st>                                         |   │
│ | H1: About John Bolster                                           |   │
│ | Substrate: #ECEAE2    | Ink: #121413    | Accent: #D3D0C6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.st>              ) max-w: 34ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Services                     |  | Selected work                | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.bar>] -> [<section.st>] -> [<section.st>] |                 │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.burger>       ) | https://www.johnbolster.design/    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.bar> — `www-johnbolster-design`)**:
   - Landmark `<header class="bar">` hosting `John Bolster · Brand Identity Design` navigation (`01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`), DOM attributes (`data-sdkn="@vercel/analytics"`, `data-sdkv="2.0.1"`, `data-go="hero"`, `data-go="about"`), and stylesheet rule `html { background:var(--bg) }`.
2. **Hero Stage & Focal Lead (<section.st> — `About John Bolster`)**:
   - Landmark `<section class="st">` presenting display lead `About John Bolster` and copy excerpt *"John Bolster is an independent brand identity designer and art di"* over `#ECEAE2` canvas and `#121413` ink.
3. **Primary Showcase & Content Grid (<section.st> — `Services`)**:
   - Landmark `<section class="st">` rendering section `Services` with copy *"Brand Strategy: Positioning and differentiation, Audience definit"*, asset references (`favicon-32.png`, `icon-512.png`, `apple-touch-icon.png`, `bebas-neue-pro-semiexp-bold.woff2`), and grid rule `body::-webkit-scrollbar { display:none;width:0;height:0 }`.
4. **Interactive Detail & Feature Matrix (<section.st> — `Selected work`)**:
   - Landmark `<section class="st">` framing `Selected work` and `Contact` (*"Brand Identity: Logo design, Typography and color systems, Guidel"*) with `#5E6360` surface cards, `#D3D0C6` accents, and `img { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.burger> — `https://www.johnbolster.design/`)**:
   - Landmark `<footer class="burger">` anchoring `John Bolster · Brand Identity De` footer links (`01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`), copy *"Art Direction: Campaign concepts, Art direction and imagery"*, and `#F47920` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-johnbolster-design (John Bolster · Brand Identity Designer and Art Director, Saratoga Spring...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-johnbolster-design` (**John Bolster · Brand Identity Designer and Art Director, Saratoga Spring...** — `https://www.johnbolster.design/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ECEAE2` / `#D3D0C6`).
- **Identity & Domain Context**: Independent brand identity designer and art director in Saratoga Springs, NY. Brand strategy, identity, print and web for businesses, hig...
- **Primary Substrate**: `#ECEAE2` (`var(--bg)` in `:root`), **Primary Ink**: `#121413`, **Accent / Highlight**: `#D3D0C6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ECEAE2` (`var(--bg)` in `:root`) paired with `#121413` primary typography and `#D3D0C6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Serif Display` for display copy (`About John Bolster`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `34ch` container bounds (`gap: 12px`, padding `var(--gut)`) with `cubic-bezier(.7,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-johnbolster-design` in your global stylesheet:

:root {
  /* John Bolster · Brand Identity Designer and Art Director, Saratoga Spring... (www-johnbolster-design) — Ground-Truth Extracted CSS Variables */
  --bg: #ECEAE2; /* Canvas / Surface Token (www-johnbolster-design) */
  --ink: #121413; /* Typography Ink Token (www-johnbolster-design) */
  --muted: #5E6360; /* Color / Atmospheric Token (www-johnbolster-design) */
  --hair: #D3D0C6; /* Color / Atmospheric Token (www-johnbolster-design) */
  --line: #2234E0; /* Color / Atmospheric Token (www-johnbolster-design) */
  --orange: #F47920; /* Color / Atmospheric Token (www-johnbolster-design) */
  --black: #0A0A0A; /* Canvas / Surface Token (www-johnbolster-design) */
  --display: "BebasPro","Bebas Neue","Arial Narrow",Impact,sans-serif; /* Design System Custom Token (www-johnbolster-design) */
  --body: "Geist",ui-sans-serif,system-ui,sans-serif; /* Dimension / Scale Token (www-johnbolster-design) */
  --mono: "Geist Mono",ui-monospace,Menlo,monospace; /* Typography / Scale Token (www-johnbolster-design) */
  --serif: "DM Serif Display",Georgia,serif; /* Typography / Scale Token (www-johnbolster-design) */
  --gut: max(16px, env(safe-area-inset-left, 0px)); /* Dimension / Scale Token (www-johnbolster-design) */
  --gutR: max(16px, env(safe-area-inset-right, 0px)); /* Dimension / Scale Token (www-johnbolster-design) */
  --fp: 1; /* Design System Custom Token (www-johnbolster-design) */
  --sc: var(--ink); /* Design System Custom Token (www-johnbolster-design) */
  --on: clamp(0, calc((var(--fp) * 1.7 - var(--li,0) * .22) * 15 - var(--i)), 1); /* Design System Custom Token (www-johnbolster-design) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ECEAE2` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#121413` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#5E6360` — grounded in `var(--muted)` in `:root`
- **Interactive Accent / Highlight**: `#D3D0C6` — grounded in `var(--hair)` in `:root`
- **Secondary / Muted Copy**: `#2234E0` — grounded in `var(--line)` in `:root`
- **Structural Hairline Border**: `#F47920` — grounded in `var(--orange)` in `:root`
- **Variable Token (`--black`)**: `#0A0A0A` — grounded in `var(--black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×24580px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `34ch` extracted from `www-johnbolster-design` stylesheet
- **Padding & Gutters**: `var(--gut)` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34ch`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding
- **Media Queries**: `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px)and (max-height:780px)`, `@media (max-width:400px)`
- **Corner Radii**: `2px`, `50%`, `999px`, `10px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DM Serif Display`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: CSS variables `--display: "BebasPro","Bebas Neue","Arial Narrow",Impact,sans-serif`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `11px`, `clamp(15px,1.15vw,18px)`, `14px`, `22px`)
- **Body Copy Rule**: CSS variables `--body: "Geist",ui-sans-serif,system-ui,sans-serif`; rule `p` (`font-size: clamp(15px,1.15vw,18px)`, `line-height: 1.5`)
- **Metadata & Index Rule**: CSS variables `--mono: "Geist Mono",ui-monospace,Menlo,monospace`; rule `.mono` (`font-size: 12px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-johnbolster-design` (`John Bolster · Brand Identity Designer and Art Director, Saratoga Spring...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.bar> — `www-johnbolster-design`)**:
   - DOM & Selectors: Landmark `<header class="bar">` hosting `John Bolster · Brand Identity Design` navigation (`01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`), DOM attributes (`data-sdkn="@vercel/analytics"`, `data-sdkv="2.0.1"`, `data-go="hero"`, `data-go="about"`), and stylesheet rule `html { background:var(--bg) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.bar> — `www-johnbolster-design`)` (`www-johnbolster-design`) adapts across `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px)and (max-height:780px)`, `@media (max-width:400px)` with `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.3,1.6,.4,1)` transitions and links `01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`.
2. **Hero Stage & Focal Lead (<section.st> — `About John Bolster`)**:
   - DOM & Selectors: Landmark `<section class="st">` presenting display lead `About John Bolster` and copy excerpt *"John Bolster is an independent brand identity designer and art di"* over `#ECEAE2` canvas and `#121413` ink.
   - Responsive Contract: Hero stage (`1440×24580px` desktop / `390×2400px` mobile) sets `#ECEAE2` background with `#121413` headline `About John Bolster`.
3. **Primary Showcase & Content Grid (<section.st> — `Services`)**:
   - DOM & Selectors: Landmark `<section class="st">` rendering section `Services` with copy *"Brand Strategy: Positioning and differentiation, Audience definit"*, asset references (`favicon-32.png`, `icon-512.png`, `apple-touch-icon.png`, `bebas-neue-pro-semiexp-bold.woff2`), and grid rule `body::-webkit-scrollbar { display:none;width:0;height:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.st> — `Services`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34ch`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.st> — `Selected work`)**:
   - DOM & Selectors: Landmark `<section class="st">` framing `Selected work` and `Contact` (*"Brand Identity: Logo design, Typography and color systems, Guidel"*) with `#5E6360` surface cards, `#D3D0C6` accents, and `img { max-width:100%;display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.st> — `Selected work`)` uses `2px`, `50%`, `999px`, `10px` radii, `#D3D0C6` highlights, and assets (favicon-32.png, icon-512.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.burger> — `https://www.johnbolster.design/`)**:
   - DOM & Selectors: Landmark `<footer class="burger">` anchoring `John Bolster · Brand Identity De` footer links (`01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`), copy *"Art Direction: Campaign concepts, Art direction and imagery"*, and `#F47920` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.burger> — `https://www.johnbolster.design/`)` aligns to `34ch` extracted from `www-johnbolster-design` stylesheet with `var(--gut)` lateral canvas padding with `12px` grid gap and attributes (data-sdkn="@vercel/analytics", data-sdkv="2.0.1", data-go="hero").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"John Bolster is an independent brand identity designer and art director based in S..."*
- Copy Excerpt 2: *"Brand Strategy: Positioning and differentiation, Audience definition, Voice, missi..."*
- Copy Excerpt 3: *"Brand Identity: Logo design, Typography and color systems, Guidelines and brand pl..."*
- Copy Excerpt 4: *"Art Direction: Campaign concepts, Art direction and imagery"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.3,1.6,.4,1)`
- **Extracted Stylesheet Rules (`www-johnbolster-design`)**:
- `html { background:var(--bg) }`
- `body::-webkit-scrollbar { display:none;width:0;height:0 }`
- `img { max-width:100%;display:block }`
- `button { font:inherit;color:inherit;background:none;border:0;padding:0;cursor:poi... }`
- `focus-visible { outline:2px solid var(--line);outline-offset:4px;border-radius:2px }`
- **Per-Selector Transition Rules**:
- **Selector `.burger i:after`**: `transition: transform .5s cubic-bezier(.7,0,.2,1)` extracted from `www-johnbolster-design` stylesheet.
- **Selector `#menu`**: `transition: clip-path .9s cubic-bezier(.7,0,.2,1)` extracted from `www-johnbolster-design` stylesheet.
- **Selector `#menu a`**: `transition: transform .9s cubic-bezier(.7,0,.2,1)` extracted from `www-johnbolster-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,0,.2,1)`)**: Governs interactive state transitions across `<header.bar>` and `<section.st>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-johnbolster-design`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
