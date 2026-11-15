---
title: "UI Prompt Blueprint: www-agrumeafarm-it_en"
date: 2026-11-15
target: "[[overview|www-agrumeafarm-it_en]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#e94e1b` / `#f39200`)"
---

# UI Design System & Master Generation Blueprint: www-agrumeafarm-it_en

> **Agrumea Farm · Jams, pestos and flavours of Sicily** (https://www.agrumeafarm.it/en) — Agrumea Farm transforms Sicilian citrus fruits, other fruits and produce into artisanal jams, pestos and preserves with an authentic flavour

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-agrumeafarm-it_en/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Agrumea Farm · Jams, pestos and flavours of Sicily** (`https://www.agrumeafarm.it/en`). Agrumea Farm transforms Sicilian citrus fruits, other fruits and produce into artisanal jams, pestos and preserves with an authentic flavour
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#e94e1b` / `#f39200`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e94e1b` (`var(--color-orange)` in `:root`) paired with `#ffffff` primary typography and `#f39200` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ivystyle-sans` for display copy (`Agrumea Farm: Sicilian artisan marma`) with `ivymode` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1024px` container bounds (`gap: var(--space-xs)`, padding `18px`) with `cubic-bezier(.645,.045,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-agrumeafarm-it_en/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1024px` extracted from `www-agrumeafarm-it_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `18px` lateral canvas padding with `var(--space-xs)` grid gap.
- **Border Radius Scale**: `999px`, `14px`, `2px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: var(--space-xs)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `18px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1024px)`, `@media (max-width:480px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e94e1b` | `var(--color-orange)` in `:root` |
| **Primary Typography Ink** | `#762530` | `var(--color-border)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdf3eb` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#f39200` | `var(--color-yellow)` in `:root` |
| **Secondary / Muted Copy** | `#ffa500` | `:hover { color: orange }` (`#ffa500`) |
| **Structural Hairline Border** | `#ffffff` | `:hover { color: white }` (`#ffffff`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--jar-circle-rotation` | `0deg` | Design System Custom Token |
| `--jar-marquee-top` | `55%` | Dimension / Scale Token |
| `--jar-marquee-w` | `100vw` | Dimension / Scale Token |
| `--jar-marquee-h` | `560px` | Dimension / Scale Token |
| `--jar-marquee-angle` | `10deg` | Design System Custom Token |
| `--jar-item-w` | `200px` | Dimension / Scale Token |
| `--jar-item-h` | `320px` | Dimension / Scale Token |
| `--jar-shape-intro-opacity` | `0` | Design System Custom Token |
| `--jar-shape-intro-y` | `24px` | Dimension / Scale Token |
| `--jar-badge-intro-opacity` | `0` | Design System Custom Token |
| `--jar-badge-intro-y` | `12px` | Dimension / Scale Token |
| `--jar-badge-intro-rotation` | `-18deg` | Design System Custom Token |
| `--jar-parallax-x` | `0` | Design System Custom Token |
| `--jar-parallax-y` | `0` | Design System Custom Token |
| `--jar-badge-shift-x` | `-52%` | Dimension / Scale Token |
| `--color-orange` | `#e94e1b` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `ivystyle-sans`.
- **Primary Body Stack**: `ivymode`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-display: clamp(4rem, calc(2.9rem + 11vw) ,999999px)`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-base)`, `var(--text-small)`, `var(--text-medium)`, `var(--text-large)`, `.9em`).
- **Body Copy**: CSS variables `--text-base: 1rem`.
- **Metadata & Navigation Labels**: CSS variables `--text-small: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `jar-slider.is-flying-out[data-v-a...`**: `transition: opacity .42s var(--ease-soft),scale .42s var(--ease-soft)` extracted from `www-agrumeafarm-it_en` stylesheet.
- **Selector `.jar-slider__prompt[data-v-a006feed]`**: `transition: opacity .9s var(--ease-premium) .18s,transform .9s var(--ease-...` extracted from `www-agrumeafarm-it_en` stylesheet.
- **Selector `.site-footer__link[data-v-68ac8fad]`**: `transition: color .3s var(--ease-out-expo)` extracted from `www-agrumeafarm-it_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<header.is-initial>` and `<section.jar-slider>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Agrumea Farm · Jams, pestos and flavours o │
│ ====================================================================== │
│ [ <header.is-initial>      | IT · EN                                ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.jar-slider>                                 |   │
│ | H1: Agrumea Farm: Sicilian artisan marmalades, spread...         |   │
│ | Substrate: #e94e1b    | Ink: #ffffff    | Accent: #f39200        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.jar-slider>      ) max-w: 1024px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Agrumea Farm · Jams, pestos  |  | m m e e n n u u c c l l o o  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.is-initial] -> [<section.jar-slide] -> [<section.jar-slide] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-shell__le) | https://www.agrumeafarm.it/en      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.is-initial> — `www-agrumeafarm-it_en`)**:
   - Landmark `<header class="is-initial site-header">` hosting `Agrumea Farm · Jams, pestos and flav` navigation (`IT · EN`), DOM attributes (`data-v-aa931410`, `data-v-3a145d88`, `data-header-theme="dark"`, `data-header-logo="full"`), and stylesheet rule `active { cursor:grabbing }`.
2. **Hero Stage & Focal Lead (<section.jar-slider> — `Agrumea Farm: Sicilian artisan mar`)**:
   - Landmark `<section class="jar-slider">` presenting display lead `Agrumea Farm: Sicilian artisan marmalades, spread...` and copy excerpt *"Agrumea Farm · Jams, pestos and flavours of Sicily"* over `#e94e1b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.jar-slider> — `Agrumea Farm · Jams, pestos and fl`)**:
   - Landmark `<section class="jar-slider">` rendering section `Agrumea Farm · Jams, pestos and flavours of Sici` with copy *"m m e e n n u u c c l l o o s s e e"*, asset references (`use.typekit.net`, `p.typekit.net`, `yey3ruw.css`, `CmsHomePage.CpbPGEL3.css`), and grid rule `.tk-ivystyle-sans { font-family: "ivystyle-sans",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<section.jar-slider> — `m m e e n n u u c c l l o o s s e `)**:
   - Landmark `<section class="jar-slider">` framing `m m e e n n u u c c l l o o s s e e` and `c c l l o o s s e e` (*"c c l l o o s s e e"*) with `#fdf3eb` surface cards, `#f39200` accents, and `.tk-ivymode { font-family: "ivymode",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.site-shell__legal> — `https://www.agrumeafarm.it/en`)**:
   - Landmark `<footer class="site-shell__legal">` anchoring `Agrumea Farm · Jams, pestos and ` footer links (`IT · EN`), copy *"Scroll to discover"*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-agrumeafarm-it_en (Agrumea Farm · Jams, pestos and flavours of Sicily)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-agrumeafarm-it_en` (**Agrumea Farm · Jams, pestos and flavours of Sicily** — `https://www.agrumeafarm.it/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#e94e1b` / `#f39200`).
- **Identity & Domain Context**: Agrumea Farm transforms Sicilian citrus fruits, other fruits and produce into artisanal jams, pestos and preserves with an authentic flavour
- **Primary Substrate**: `#e94e1b` (`var(--color-orange)` in `:root`), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#f39200`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e94e1b` (`var(--color-orange)` in `:root`) paired with `#ffffff` primary typography and `#f39200` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ivystyle-sans` for display copy (`Agrumea Farm: Sicilian artisan marma`) with `ivymode` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1024px` container bounds (`gap: var(--space-xs)`, padding `18px`) with `cubic-bezier(.645,.045,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-agrumeafarm-it_en` in your global stylesheet:

:root {
  /* Agrumea Farm · Jams, pestos and flavours of Sicily (www-agrumeafarm-it_en) — Ground-Truth Extracted CSS Variables */
  --jar-circle-rotation: 0deg; /* Design System Custom Token (www-agrumeafarm-it_en) */
  --jar-marquee-top: 55%; /* Dimension / Scale Token (www-agrumeafarm-it_en) */
  --jar-marquee-w: 100vw; /* Dimension / Scale Token (www-agrumeafarm-it_en) */
  --jar-marquee-h: 560px; /* Dimension / Scale Token (www-agrumeafarm-it_en) */
  --jar-marquee-angle: 10deg; /* Design System Custom Token (www-agrumeafarm-it_en) */
  --jar-item-w: 200px; /* Dimension / Scale Token (www-agrumeafarm-it_en) */
  --jar-item-h: 320px; /* Dimension / Scale Token (www-agrumeafarm-it_en) */
  --jar-shape-intro-opacity: 0; /* Design System Custom Token (www-agrumeafarm-it_en) */
  --jar-shape-intro-y: 24px; /* Dimension / Scale Token (www-agrumeafarm-it_en) */
  --jar-badge-intro-opacity: 0; /* Design System Custom Token (www-agrumeafarm-it_en) */
  --jar-badge-intro-y: 12px; /* Dimension / Scale Token (www-agrumeafarm-it_en) */
  --jar-badge-intro-rotation: -18deg; /* Design System Custom Token (www-agrumeafarm-it_en) */
  --jar-parallax-x: 0; /* Design System Custom Token (www-agrumeafarm-it_en) */
  --jar-parallax-y: 0; /* Design System Custom Token (www-agrumeafarm-it_en) */
  --jar-badge-shift-x: -52%; /* Dimension / Scale Token (www-agrumeafarm-it_en) */
  --color-orange: #e94e1b; /* Brand / Palette Token (www-agrumeafarm-it_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e94e1b` — grounded in `var(--color-orange)` in `:root`
- **Primary Typography Ink**: `#762530` — grounded in `var(--color-border)` in `:root`
- **Elevated Surface / Card Substrate**: `#fdf3eb` — grounded in `var(--color-white)` in `:root`
- **Interactive Accent / Highlight**: `#f39200` — grounded in `var(--color-yellow)` in `:root`
- **Secondary / Muted Copy**: `#ffa500` — grounded in `:hover { color: orange }` (`#ffa500`)
- **Structural Hairline Border**: `#ffffff` — grounded in `:hover { color: white }` (`#ffffff`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1024px` extracted from `www-agrumeafarm-it_en` stylesheet
- **Padding & Gutters**: `18px` lateral canvas padding with `var(--space-xs)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: var(--space-xs)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `18px` horizontal padding
- **Media Queries**: `@media (max-width:1024px)`, `@media (max-width:480px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `999px`, `14px`, `2px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ivystyle-sans`
- **Body Font Stack**: `ivymode`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--text-display: clamp(4rem, calc(2.9rem + 11vw) ,999999px)`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-base)`, `var(--text-small)`, `var(--text-medium)`, `var(--text-large)`, `.9em`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`
- **Metadata & Index Rule**: CSS variables `--text-small: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-agrumeafarm-it_en` (`Agrumea Farm · Jams, pestos and flavours of Sicily`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.is-initial> — `www-agrumeafarm-it_en`)**:
   - DOM & Selectors: Landmark `<header class="is-initial site-header">` hosting `Agrumea Farm · Jams, pestos and flav` navigation (`IT · EN`), DOM attributes (`data-v-aa931410`, `data-v-3a145d88`, `data-header-theme="dark"`, `data-header-logo="full"`), and stylesheet rule `active { cursor:grabbing }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.is-initial> — `www-agrumeafarm-it_en`)` (`www-agrumeafarm-it_en`) adapts across `@media (max-width:1024px)`, `@media (max-width:480px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `IT · EN`.
2. **Hero Stage & Focal Lead (<section.jar-slider> — `Agrumea Farm: Sicilian artisan mar`)**:
   - DOM & Selectors: Landmark `<section class="jar-slider">` presenting display lead `Agrumea Farm: Sicilian artisan marmalades, spread...` and copy excerpt *"Agrumea Farm · Jams, pestos and flavours of Sicily"* over `#e94e1b` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#e94e1b` background with `#ffffff` headline `Agrumea Farm: Sicilian artisan marmalades, spread...`.
3. **Primary Showcase & Content Grid (<section.jar-slider> — `Agrumea Farm · Jams, pestos and fl`)**:
   - DOM & Selectors: Landmark `<section class="jar-slider">` rendering section `Agrumea Farm · Jams, pestos and flavours of Sici` with copy *"m m e e n n u u c c l l o o s s e e"*, asset references (`use.typekit.net`, `p.typekit.net`, `yey3ruw.css`, `CmsHomePage.CpbPGEL3.css`), and grid rule `.tk-ivystyle-sans { font-family: "ivystyle-sans",sans-serif; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.jar-slider> — `Agrumea Farm · Jams, pestos and fl`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: var(--space-xs)`) on desktop and Single-column vertical stack at `390px` viewport width with `18px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.jar-slider> — `m m e e n n u u c c l l o o s s e `)**:
   - DOM & Selectors: Landmark `<section class="jar-slider">` framing `m m e e n n u u c c l l o o s s e e` and `c c l l o o s s e e` (*"c c l l o o s s e e"*) with `#fdf3eb` surface cards, `#f39200` accents, and `.tk-ivymode { font-family: "ivymode",sans-serif; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.jar-slider> — `m m e e n n u u c c l l o o s s e `)` uses `999px`, `14px`, `2px`, `50%` radii, `#f39200` highlights, and assets (use.typekit.net, p.typekit.net, yey3ruw.css).
5. **Colophon & Global Directory Footer (<footer.site-shell__legal> — `https://www.agrumeafarm.it/en`)**:
   - DOM & Selectors: Landmark `<footer class="site-shell__legal">` anchoring `Agrumea Farm · Jams, pestos and ` footer links (`IT · EN`), copy *"Scroll to discover"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-shell__legal> — `https://www.agrumeafarm.it/en`)` aligns to `1024px` extracted from `www-agrumeafarm-it_en` stylesheet with `18px` lateral canvas padding with `var(--space-xs)` grid gap and attributes (data-v-aa931410, data-v-3a145d88, data-header-theme="dark").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Agrumea Farm · Jams, pestos and flavours of Sicily"*
- Copy Excerpt 2: *"m m e e n n u u c c l l o o s s e e"*
- Copy Excerpt 3: *"c c l l o o s s e e"*
- Copy Excerpt 4: *"Scroll to discover"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`www-agrumeafarm-it_en`)**:
- `active { cursor:grabbing }`
- `.tk-ivystyle-sans { font-family: "ivystyle-sans",sans-serif; }`
- `.tk-ivymode { font-family: "ivymode",sans-serif; }`
- `hover { color:var(--color-orange) }`
- `.site-legal { align-items:flex-start;flex-direction:column;gap:.35rem }`
- **Per-Selector Transition Rules**:
- **Selector `jar-slider.is-flying-out[data-v-a...`**: `transition: opacity .42s var(--ease-soft),scale .42s var(--ease-soft)` extracted from `www-agrumeafarm-it_en` stylesheet.
- **Selector `.jar-slider__prompt[data-v-a006feed]`**: `transition: opacity .9s var(--ease-premium) .18s,transform .9s var(--ease-...` extracted from `www-agrumeafarm-it_en` stylesheet.
- **Selector `.site-footer__link[data-v-68ac8fad]`**: `transition: color .3s var(--ease-out-expo)` extracted from `www-agrumeafarm-it_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<header.is-initial>` and `<section.jar-slider>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-agrumeafarm-it_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
