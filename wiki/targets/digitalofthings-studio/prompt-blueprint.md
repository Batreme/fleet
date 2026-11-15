---
title: "UI Prompt Blueprint: digitalofthings-studio"
date: 2026-11-15
target: "digitalofthings-studio"
status: analyzed
capture: specimen
capture_desktop: specimen
capture_mobile: specimen
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000`)"
---

# UI Design System & Master Generation Blueprint: digitalofthings-studio

> **digital of things · user experience digital studio** (https://digitalofthings.studio/) — digital of things is an independent user experience digital studio based in Barcelona. We design and build websites, e-commerce and digit...

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **digital of things · user experience digital studio** (`https://digitalofthings.studio/`). digital of things is an independent user experience digital studio based in Barcelona. We design and build websites, e-commerce and digit...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`body { background-color: #fff }`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `FoundersGrotesk-Medium` for display copy (`User experience digital studio`) with `CenturyExpandedBT-Roman` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `720px` container bounds (`gap: 10px`, padding `2rem`) with `cubic-bezier(.4,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `720px` extracted from `digitalofthings-studio` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `10px`, `2px`, `9999px`, `5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 720px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=880px)`, `@media (width<=1149px)`, `@media (width>=1400px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `body { background-color: #fff }` |
| **Primary Typography Ink** | `#ff0` | `.debug-info { background-color: #ff0 }` |
| **Elevated Surface / Card Substrate** | `#ececec` | `body { background-color: #ececec }` |
| **Interactive Accent / Highlight** | `#000` | `.loading-container { background-color: #000 }` |
| **Secondary / Muted Copy** | `#0000` | `:before { border: #0000 }` |
| **Structural Hairline Border** | `#dbffad` | `content-stack-container .expose... { background: #dbffad }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mask-x` | `50%` | Dimension / Scale Token |
| `--mask-y` | `50%` | Dimension / Scale Token |
| `--mask-radius` | `0px` | Elevation / Border Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--tw-skew-x` | `0` | Design System Custom Token |
| `--tw-skew-y` | `0` | Design System Custom Token |
| `--tw-scale-x` | `1` | Design System Custom Token |
| `--tw-scale-y` | `1` | Design System Custom Token |
| `--tw-scroll-snap-strictness` | `proximity` | Design System Custom Token |
| `--tw-ring-offset-width` | `0px` | Layout / Spatial Grid Token |
| `--digitalofthings--bg` | `#fff` | Canvas Substrate (from `body { background-color: #fff }`) |
| `--digitalofthings--ink` | `#000` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `FoundersGrotesk-Medium`.
- **Primary Body Stack**: `CenturyExpandedBT-Roman`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.title` (`font-size: 15px`, `line-height: 19px`, `letter-spacing: -.15px`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 16px`, `line-height: 22px`, `letter-spacing: -.16px`).
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 20px`, `letter-spacing: -.15px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `17px`, `24px`, `clamp(32px,5.6vw,56px)`, `18px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `body`**: `transition: background-color 1s ease-in-out` extracted from `digitalofthings-studio` stylesheet.
- **Selector `m .stack-item-wrapper .expose-tit...`**: `transition: opacity .3s,transform .4s` extracted from `digitalofthings-studio` stylesheet.
- **Selector `.stack-item .stack-item-card`**: `transition: transform .2s,box-shadow .2s` extracted from `digitalofthings-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.js>` and `<section.antialiased>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — digital of things · user experience digita │
│ ====================================================================== │
│ [ <nav.js>                 | Projects · Pet Projects · Contact · Ea ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.has-bar>                                    |   │
│ | H1: User experience digital studio                               |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.antialiased>     ) max-w: 720px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | digital of things — user exp |  | Explore                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<nav.js>] -> [<section.has-bar>] -> [<section.antialias] |          │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.app-footer>   ) | https://digitalofthings.studio/    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.js> — `digitalofthings-studio`)**:
   - Landmark `<nav class="js">` hosting `digital of things · user experience ` navigation (`Projects · Pet Projects · Contact · Easter Eggs · Clients`), DOM attributes (`data-prefix`, `data-home-title="digital of things · u..."`, `data-ga="G-WW56TNJ6LL"`, `data-cf-beacon="("token": "fcd04126c7..."`), and stylesheet rule `.__className_8eaea4 { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.has-bar> — `User experience digital studio`)**:
   - Landmark `<section class="has-bar">` presenting display lead `User experience digital studio` and copy excerpt *"We use Google Analytics cookies to understand how the site is use"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.antialiased> — `digital of things — user experienc`)**:
   - Landmark `<section class="antialiased">` rendering section `digital of things — user experience digital studi...` with copy *"Explore our projects"*, asset references (`manifest.webmanifest`, `digitalofthings.studio`, `favicon.ico`, `icon-512.png`), and grid rule `.__className_8c25df { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
4. **Interactive Detail & Feature Matrix (<section.cookie-consent> — `Explore`)**:
   - Landmark `<section class="cookie-consent">` framing `Explore` and `Selected projects` (*"or know more about us"*) with `#ececec` surface cards, `#000` accents, and `html { scroll-behavior:smooth }`.
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://digitalofthings.studio/`)**:
   - Landmark `<footer class="app-footer">` anchoring `digital of things · user experie` footer links (`Projects · Pet Projects · Contact · Easter Eggs · Clients`), copy *"User experience digital studio"*, and `#dbffad` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: digitalofthings-studio (digital of things · user experience digital studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `digitalofthings-studio` (**digital of things · user experience digital studio** — `https://digitalofthings.studio/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000`).
- **Identity & Domain Context**: digital of things is an independent user experience digital studio based in Barcelona. We design and build websites, e-commerce and digit...
- **Primary Substrate**: `#fff` (`body { background-color: #fff }`), **Primary Ink**: `#000`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`body { background-color: #fff }`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `FoundersGrotesk-Medium` for display copy (`User experience digital studio`) with `CenturyExpandedBT-Roman` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `720px` container bounds (`gap: 10px`, padding `2rem`) with `cubic-bezier(.4,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `digitalofthings-studio` in your global stylesheet:

:root {
  /* digital of things · user experience digital studio (digitalofthings-studio) — Ground-Truth Extracted CSS Variables */
  --mask-x: 50%; /* Dimension / Scale Token (digitalofthings-studio) */
  --mask-y: 50%; /* Dimension / Scale Token (digitalofthings-studio) */
  --mask-radius: 0px; /* Elevation / Border Token (digitalofthings-studio) */
  --tw-border-spacing-x: 0; /* Layout / Spatial Grid Token (digitalofthings-studio) */
  --tw-border-spacing-y: 0; /* Layout / Spatial Grid Token (digitalofthings-studio) */
  --tw-translate-x: 0; /* Design System Custom Token (digitalofthings-studio) */
  --tw-translate-y: 0; /* Design System Custom Token (digitalofthings-studio) */
  --tw-rotate: 0; /* Design System Custom Token (digitalofthings-studio) */
  --tw-skew-x: 0; /* Design System Custom Token (digitalofthings-studio) */
  --tw-skew-y: 0; /* Design System Custom Token (digitalofthings-studio) */
  --tw-scale-x: 1; /* Design System Custom Token (digitalofthings-studio) */
  --tw-scale-y: 1; /* Design System Custom Token (digitalofthings-studio) */
  --tw-scroll-snap-strictness: proximity; /* Design System Custom Token (digitalofthings-studio) */
  --tw-ring-offset-width: 0px; /* Layout / Spatial Grid Token (digitalofthings-studio) */
  --digitalofthings--bg: #fff; /* Canvas Substrate (from `body { background-color: #fff }`) (digitalofthings-studio) */
  --digitalofthings--ink: #000; /* Primary Typography Ink (stylesheet-derived) (digitalofthings-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `body { background-color: #fff }`
- **Primary Typography Ink**: `#ff0` — grounded in `.debug-info { background-color: #ff0 }`
- **Elevated Surface / Card Substrate**: `#ececec` — grounded in `body { background-color: #ececec }`
- **Interactive Accent / Highlight**: `#000` — grounded in `.loading-container { background-color: #000 }`
- **Secondary / Muted Copy**: `#0000` — grounded in `:before { border: #0000 }`
- **Structural Hairline Border**: `#dbffad` — grounded in `content-stack-container .expose... { background: #dbffad }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `720px` extracted from `digitalofthings-studio` stylesheet
- **Padding & Gutters**: `2rem` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 720px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (width>=880px)`, `@media (width<=1149px)`, `@media (width>=1400px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `10px`, `2px`, `9999px`, `5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `FoundersGrotesk-Medium`
- **Body Font Stack**: `CenturyExpandedBT-Roman`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: rule `.title` (`font-size: 15px`, `line-height: 19px`, `letter-spacing: -.15px`)
- **H2 Section Rule**: rule `h2` (`font-size: 16px`, `line-height: 22px`, `letter-spacing: -.16px`)
- **Body Copy Rule**: rule `p` (`font-size: 15px`, `line-height: 20px`, `letter-spacing: -.15px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `17px`, `24px`, `clamp(32px,5.6vw,56px)`, `18px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `digitalofthings-studio` (`digital of things · user experience digital studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.js> — `digitalofthings-studio`)**:
   - DOM & Selectors: Landmark `<nav class="js">` hosting `digital of things · user experience ` navigation (`Projects · Pet Projects · Contact · Easter Eggs · Clients`), DOM attributes (`data-prefix`, `data-home-title="digital of things · u..."`, `data-ga="G-WW56TNJ6LL"`, `data-cf-beacon="("token": "fcd04126c7..."`), and stylesheet rule `.__className_8eaea4 { font-family:Geist,Geist Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.js> — `digitalofthings-studio`)` (`digitalofthings-studio`) adapts across `@media (width>=880px)`, `@media (width<=1149px)`, `@media (width>=1400px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `Projects · Pet Projects · Contact · Easter Eggs · Clients`.
2. **Hero Stage & Focal Lead (<section.has-bar> — `User experience digital studio`)**:
   - DOM & Selectors: Landmark `<section class="has-bar">` presenting display lead `User experience digital studio` and copy excerpt *"We use Google Analytics cookies to understand how the site is use"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `User experience digital studio`.
3. **Primary Showcase & Content Grid (<section.antialiased> — `digital of things — user experienc`)**:
   - DOM & Selectors: Landmark `<section class="antialiased">` rendering section `digital of things — user experience digital studi...` with copy *"Explore our projects"*, asset references (`manifest.webmanifest`, `digitalofthings.studio`, `favicon.ico`, `icon-512.png`), and grid rule `.__className_8c25df { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.antialiased> — `digital of things — user experienc`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 720px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.cookie-consent> — `Explore`)**:
   - DOM & Selectors: Landmark `<section class="cookie-consent">` framing `Explore` and `Selected projects` (*"or know more about us"*) with `#ececec` surface cards, `#000` accents, and `html { scroll-behavior:smooth }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.cookie-consent> — `Explore`)` uses `10px`, `2px`, `9999px`, `5px` radii, `#000` highlights, and assets (manifest.webmanifest, digitalofthings.studio, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://digitalofthings.studio/`)**:
   - DOM & Selectors: Landmark `<footer class="app-footer">` anchoring `digital of things · user experie` footer links (`Projects · Pet Projects · Contact · Easter Eggs · Clients`), copy *"User experience digital studio"*, and `#dbffad` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.app-footer> — `https://digitalofthings.studio/`)` aligns to `720px` extracted from `digitalofthings-studio` stylesheet with `2rem` lateral canvas padding with `10px` grid gap and attributes (data-prefix, data-home-title="digital of things · u...", data-ga="G-WW56TNJ6LL").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use Google Analytics cookies to understand how the site is used. They are only..."*
- Copy Excerpt 2: *"Explore our projects"*
- Copy Excerpt 3: *"or know more about us"*
- Copy Excerpt 4: *"User experience digital studio"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`digitalofthings-studio`)**:
- `.__className_8eaea4 { font-family:Geist,Geist Fallback;font-style:normal }`
- `.__className_8c25df { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`
- `html { scroll-behavior:smooth }`
- `.seo-content { max-width:720px;margin:0 auto;padding:2rem 1.5rem }`
- `.seo-content img { max-width:100%;height:auto;display:block }`
- **Per-Selector Transition Rules**:
- **Selector `body`**: `transition: background-color 1s ease-in-out` extracted from `digitalofthings-studio` stylesheet.
- **Selector `m .stack-item-wrapper .expose-tit...`**: `transition: opacity .3s,transform .4s` extracted from `digitalofthings-studio` stylesheet.
- **Selector `.stack-item .stack-item-card`**: `transition: transform .2s,box-shadow .2s` extracted from `digitalofthings-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.js>` and `<section.antialiased>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `digitalofthings-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
