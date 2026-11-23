---
title: "UI Prompt Blueprint: www-butter-video"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-butter-video"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#00ffd0`)"
---

# UI Design System & Master Generation Blueprint: www-butter-video

> **Butter Video · Online Video Editor Engineered for Creativity** (https://www.butter.video/) — The first video editor and design platform built with creative code for creative teams. It's a whole new timeline.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Butter Video · Online Video Editor Engineered for Creativity** (`https://www.butter.video/`). The first video editor and design platform built with creative code for creative teams. It's a whole new timeline.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#00ffd0`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#0f0f0f` primary typography and `#00ffd0` accents.
  - **Grounded Typographic Hierarchy**: Pairs `DieGrotesk` for display copy (`Engineered for Creativity Engineered`) with `DieGrotesk` and `monospace)`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: .75rem`, padding `1.5rem`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1920px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `.75rem` grid gap.
- **Border Radius Scale**: `8px`, `1.6rem`, `50%`, `1rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: .75rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:900px)`, `@media (max-width:650px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width: 480px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f0f0f` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ededed` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00ffd0` | `var(--perf-gradient-primary)` in `:root` |
| **Secondary / Muted Copy** | `#718096` | `var(--perf-text-muted)` in `:root` |
| **Structural Hairline Border** | `#fdfdfd` | `.CreatorSlice_secondaryButton__... { border-color: #fdfdfd }` |
| **Variable Token (`--butter-white`)** | `#fafafa` | `var(--butter-white)` in `:root` |
| **Variable Token (`--butter-off-white`)** | `#f7f7f7` | `var(--butter-off-white)` in `:root` |
| **Variable Token (`--butter-black`)** | `#1e1e1e` | `var(--butter-black)` in `:root` |
| **Variable Token (`--butter-charcoal`)** | `#3c3c3c` | `var(--butter-charcoal)` in `:root` |
| **Variable Token (`--butter-dark-grey`)** | `#e2e2e2` | `var(--butter-dark-grey)` in `:root` |
| **Variable Token (`--butter-light`)** | `#ebebeb` | `var(--butter-light)` in `:root` |
| **Variable Token (`--butter-red`)** | `#ff3333` | `var(--butter-red)` in `:root` |
| **Variable Token (`--butter-blue`)** | `#4dc5e5` | `var(--butter-blue)` in `:root` |
| **Variable Token (`--butter-green`)** | `#63ad45` | `var(--butter-green)` in `:root` |
| **Variable Token (`--butter-yellow`)** | `#e9d352` | `var(--butter-yellow)` in `:root` |
| **Variable Token (`--butter-pink`)** | `#f9abff` | `var(--butter-pink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--butter-white` | `#FAFAFA` | Canvas / Surface Token |
| `--butter-off-white` | `#F7F7F7` | Canvas / Surface Token |
| `--butter-black` | `#1E1E1E` | Canvas / Surface Token |
| `--butter-true-black` | `#0F0F0F` | Canvas / Surface Token |
| `--butter-charcoal` | `#3C3C3C` | Color / Atmospheric Token |
| `--butter-light-grey` | `#EDEDED` | Canvas / Surface Token |
| `--butter-dark-grey` | `#E2E2E2` | Canvas / Surface Token |
| `--butter-light` | `#EBEBEB` | Canvas / Surface Token |
| `--butter-red` | `#FF3333` | Color / Atmospheric Token |
| `--butter-blue` | `#4DC5E5` | Color / Atmospheric Token |
| `--butter-green` | `#63AD45` | Color / Atmospheric Token |
| `--butter-yellow` | `#E9D352` | Color / Atmospheric Token |
| `--butter-pink` | `#F9ABFF` | Typography Ink Token |
| `--butter-font-primary` | `'DieGrotesk','DieGrotesk Fallback'` | Brand / Palette Token |
| `--butter-font-secondary` | `'ABCDiatype','ABCDiatype Fallback'` | Brand / Palette Token |
| `--butter-ease-out` | `cubic-bezier(0.200, 0.715, 0.205, 0.990)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DieGrotesk`.
- **Primary Body Stack**: `DieGrotesk`.
- **Technical / Metadata Stack**: `monospace)`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 107.568px`, `line-height: 106.708px`, `font-weight: 400`, `letter-spacing: 0.344219px`); rule `h1` (`font-size: clamp(5.6rem,6.6vw,12.5rem)`, `line-height: .92`, `letter-spacing: -1px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.4px`, `line-height: 58.588px`, `font-weight: 400`, `letter-spacing: 0.3624px`); rule `h2` (`font-size: clamp(3.2rem,6vw,7rem)`, `line-height: .94`, `letter-spacing: -.5px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); rule `p` (`font-size: clamp(1.05rem,1.5vw,1.25rem)`, `line-height: 1.45`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); rule `small` (`font-size: inherit`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`, `cubic-bezier(0.200,0.715,0.205,0.990)`.

### Per-Element Transition & Choreography Rules
- **Selector `.CreatorSlice_secondaryButton__I1S9a`**: `transition: transform .2s var(--butter-ease-out),background .2s var(--butt...` extracted from `www-butter-video` stylesheet.
- **Selector `.CreatorSlice_tabs__0DQZR button`**: `transition: background .2s var(--butter-ease-out),color .2s var(--butter-e...` extracted from `www-butter-video` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none` extracted from `www-butter-video` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Butter Video · Online Video Editor Enginee │
│ ====================================================================== │
│ [ <header.kbhUnc> (1440x88px)         | Product Product · Blocks Blo ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hsoZjO> (w=1440px)                            | │
│ | H1: Engineered for Creativity Engineered for Creativity            | │
│ | Substrate: #ffffff | Ink: #0f0f0f | Accent: #00ffd0                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.glnUmG>) max-w: 1920px                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Butter is the first video ed |  | Browse curated blocks for mo | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.lhNRew>) — Make blocks your own            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bdNowa>     ) | https://www.butter.video/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .75rem)     │
│ ====================================================================== │
│ [ HEADER BAR (<header.kbhUnc>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hsoZjO>) — 390px Vertical Lead                | │
│ | H1: Engineered for Creativity Engineered for Creativity            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.glnUmG>) — 1-Col Stack                    | │
│ | [ Item 1: Butter is the first video editor where creatives...    ] | │
│ | [ Item 2: Browse curated blocks for motion graphics, kineti...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.lhNRew>) — 1-Col (Make blocks your o)       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bdNowa>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.kbhUnc> — `www-butter-video`)**:
   - Landmark `<header class="kbhUnc">` (`1440x88px`) hosting `Butter Video · Online Video Editor E` navigation (`Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`), DOM attributes (`data-auth="out"`, `data-precedence="next"`, `data-precedence="next"`, `data-styled="active"`), and stylesheet rule `.CreatorSlice_inner__5XvuM { width:100%;max-width:1920px;margin-inline:auto }`.
2. **Hero Stage & Focal Lead (<section.hsoZjO> — `Engineered for Creativity Engineer`)**:
   - Landmark `<section class="hsoZjO">` presenting display lead `Engineered for Creativity Engineered for Creativity` and copy excerpt *"It's a whole new timeline."* over `#ffffff` canvas and `#0f0f0f` ink.
3. **Primary Showcase & Content Grid (<section.glnUmG> — `Butter is the first video editor w`)**:
   - Landmark `<section class="glnUmG">` rendering section `Butter is the first video editor where creatives...` with copy *"Co-Create Co-Create"*, asset references (`5fb8d156cdd6d753-s.p.woff2`, `da60608f2183158e-s.p.woff2`, `2836d44e2fdcb041.css`, `6294d87c4b6dbd81.css`), and grid rule `.CreatorSlice_surfacePage__D5FDj { background:var(--butter-white) }`.
4. **Interactive Detail & Feature Matrix (<section.lhNRew> — `Browse curated blocks for motion g`)**:
   - Landmark `<section class="lhNRew">` framing `Browse curated blocks for motion graphics, kineti...` and `Make blocks your own with intuitive dials, slider...` (*"Templates Templates"*) with `#ededed` surface cards, `#00ffd0` accents, and `.CreatorSlice_surfaceSubtle__v5RgA { background:var(--butter-off-white) }`.
5. **Colophon & Global Directory Footer (<footer.bdNowa> — `https://www.butter.video/`)**:
   - Landmark `<footer class="bdNowa">` anchoring `Butter Video · Online Video Edit` footer links (`Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`), copy *"Product Product Explore features Explore features"*, and `#fdfdfd` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-butter-video (Butter Video · Online Video Editor Engineered for Creativity)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-butter-video` (**Butter Video · Online Video Editor Engineered for Creativity** — `https://www.butter.video/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#00ffd0`).
- **Identity & Domain Context**: The first video editor and design platform built with creative code for creative teams. It's a whole new timeline.
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0f0f0f`, **Accent / Highlight**: `#00ffd0`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#0f0f0f` primary typography and `#00ffd0` accents.
  - **Grounded Typographic Hierarchy**: Pairs `DieGrotesk` for display copy (`Engineered for Creativity Engineered`) with `DieGrotesk` and `monospace)`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: .75rem`, padding `1.5rem`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-butter-video` in your global stylesheet:

:root {
  /* Butter Video · Online Video Editor Engineered for Creativity (www-butter-video) — Live-Grounded CSS Variables */
  --butter-white: #FAFAFA; /* Canvas / Surface Token (www-butter-video) */
  --butter-off-white: #F7F7F7; /* Canvas / Surface Token (www-butter-video) */
  --butter-black: #1E1E1E; /* Canvas / Surface Token (www-butter-video) */
  --butter-true-black: #0F0F0F; /* Canvas / Surface Token (www-butter-video) */
  --butter-charcoal: #3C3C3C; /* Color / Atmospheric Token (www-butter-video) */
  --butter-light-grey: #EDEDED; /* Canvas / Surface Token (www-butter-video) */
  --butter-dark-grey: #E2E2E2; /* Canvas / Surface Token (www-butter-video) */
  --butter-light: #EBEBEB; /* Canvas / Surface Token (www-butter-video) */
  --butter-red: #FF3333; /* Color / Atmospheric Token (www-butter-video) */
  --butter-blue: #4DC5E5; /* Color / Atmospheric Token (www-butter-video) */
  --butter-green: #63AD45; /* Color / Atmospheric Token (www-butter-video) */
  --butter-yellow: #E9D352; /* Color / Atmospheric Token (www-butter-video) */
  --butter-pink: #F9ABFF; /* Typography Ink Token (www-butter-video) */
  --butter-font-primary: 'DieGrotesk','DieGrotesk Fallback'; /* Brand / Palette Token (www-butter-video) */
  --butter-font-secondary: 'ABCDiatype','ABCDiatype Fallback'; /* Brand / Palette Token (www-butter-video) */
  --butter-ease-out: cubic-bezier(0.200, 0.715, 0.205, 0.990); /* Motion / Easing Token (www-butter-video) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0f0f0f` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ededed` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#00ffd0` — grounded in `var(--perf-gradient-primary)` in `:root`
- **Secondary / Muted Copy**: `#718096` — grounded in `var(--perf-text-muted)` in `:root`
- **Structural Hairline Border**: `#fdfdfd` — grounded in `.CreatorSlice_secondaryButton__... { border-color: #fdfdfd }`
- **Variable Token (`--butter-white`)**: `#fafafa` — grounded in `var(--butter-white)` in `:root`
- **Variable Token (`--butter-off-white`)**: `#f7f7f7` — grounded in `var(--butter-off-white)` in `:root`
- **Variable Token (`--butter-black`)**: `#1e1e1e` — grounded in `var(--butter-black)` in `:root`
- **Variable Token (`--butter-charcoal`)**: `#3c3c3c` — grounded in `var(--butter-charcoal)` in `:root`
- **Variable Token (`--butter-dark-grey`)**: `#e2e2e2` — grounded in `var(--butter-dark-grey)` in `:root`
- **Variable Token (`--butter-light`)**: `#ebebeb` — grounded in `var(--butter-light)` in `:root`
- **Variable Token (`--butter-red`)**: `#ff3333` — grounded in `var(--butter-red)` in `:root`
- **Variable Token (`--butter-blue`)**: `#4dc5e5` — grounded in `var(--butter-blue)` in `:root`
- **Variable Token (`--butter-green`)**: `#63ad45` — grounded in `var(--butter-green)` in `:root`
- **Variable Token (`--butter-yellow`)**: `#e9d352` — grounded in `var(--butter-yellow)` in `:root`
- **Variable Token (`--butter-pink`)**: `#f9abff` — grounded in `var(--butter-pink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1920px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `.75rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: .75rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media (max-width:900px)`, `@media (max-width:650px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width: 480px)`
- **Corner Radii**: `8px`, `1.6rem`, `50%`, `1rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DieGrotesk`
- **Body Font Stack**: `DieGrotesk`
- **Monospace / Technical Font Stack**: `monospace)`
- **H1 Display Rule**: live computed `h1` (`font-size: 107.568px`, `line-height: 106.708px`, `font-weight: 400`, `letter-spacing: 0.344219px`); rule `h1` (`font-size: clamp(5.6rem,6.6vw,12.5rem)`, `line-height: .92`, `letter-spacing: -1px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 60.4px`, `line-height: 58.588px`, `font-weight: 400`, `letter-spacing: 0.3624px`); rule `h2` (`font-size: clamp(3.2rem,6vw,7rem)`, `line-height: .94`, `letter-spacing: -.5px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); rule `p` (`font-size: clamp(1.05rem,1.5vw,1.25rem)`, `line-height: 1.45`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); rule `small` (`font-size: inherit`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-butter-video` (`Butter Video · Online Video Editor Engineered for Creativity`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.kbhUnc> — `www-butter-video`)**:
   - DOM & Selectors: Landmark `<header class="kbhUnc">` (`1440x88px`) hosting `Butter Video · Online Video Editor E` navigation (`Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`), DOM attributes (`data-auth="out"`, `data-precedence="next"`, `data-precedence="next"`, `data-styled="active"`), and stylesheet rule `.CreatorSlice_inner__5XvuM { width:100%;max-width:1920px;margin-inline:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.kbhUnc> — `www-butter-video`)` (`www-butter-video`) adapts across `@media (max-width:900px)`, `@media (max-width:650px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width: 480px)` with `cubic-bezier(0.25,0.1,0.25,1)`, `cubic-bezier(0.200,0.715,0.205,0.990)` transitions and links `Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`.
2. **Hero Stage & Focal Lead (<section.hsoZjO> — `Engineered for Creativity Engineer`)**:
   - DOM & Selectors: Landmark `<section class="hsoZjO">` presenting display lead `Engineered for Creativity Engineered for Creativity` and copy excerpt *"It's a whole new timeline."* over `#ffffff` canvas and `#0f0f0f` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#0f0f0f` headline `Engineered for Creativity Engineered for Creativity`.
3. **Primary Showcase & Content Grid (<section.glnUmG> — `Butter is the first video editor w`)**:
   - DOM & Selectors: Landmark `<section class="glnUmG">` rendering section `Butter is the first video editor where creatives...` with copy *"Co-Create Co-Create"*, asset references (`5fb8d156cdd6d753-s.p.woff2`, `da60608f2183158e-s.p.woff2`, `2836d44e2fdcb041.css`, `6294d87c4b6dbd81.css`), and grid rule `.CreatorSlice_surfacePage__D5FDj { background:var(--butter-white) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.glnUmG> — `Butter is the first video editor w`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: .75rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.lhNRew> — `Browse curated blocks for motion g`)**:
   - DOM & Selectors: Landmark `<section class="lhNRew">` framing `Browse curated blocks for motion graphics, kineti...` and `Make blocks your own with intuitive dials, slider...` (*"Templates Templates"*) with `#ededed` surface cards, `#00ffd0` accents, and `.CreatorSlice_surfaceSubtle__v5RgA { background:var(--butter-off-white) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.lhNRew> — `Browse curated blocks for motion g`)` uses `8px`, `1.6rem`, `50%`, `1rem` radii, `#00ffd0` highlights, and assets (5fb8d156cdd6d753-s.p.woff2, da60608f2183158e-s.p.woff2, 2836d44e2fdcb041.css).
5. **Colophon & Global Directory Footer (<footer.bdNowa> — `https://www.butter.video/`)**:
   - DOM & Selectors: Landmark `<footer class="bdNowa">` anchoring `Butter Video · Online Video Edit` footer links (`Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`), copy *"Product Product Explore features Explore features"*, and `#fdfdfd` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bdNowa> — `https://www.butter.video/`)` aligns to `1920px` (non-`@media` desktop container stylesheet rule) with `1.5rem` lateral canvas padding with `.75rem` grid gap and attributes (data-auth="out", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"It's a whole new timeline."*
- Copy Excerpt 2: *"Co-Create Co-Create"*
- Copy Excerpt 3: *"Templates Templates"*
- Copy Excerpt 4: *"Product Product Explore features Explore features"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`, `cubic-bezier(0.200,0.715,0.205,0.990)`
- **Extracted Stylesheet Rules (`www-butter-video`)**:
- `.CreatorSlice_inner__5XvuM { width:100%;max-width:1920px;margin-inline:auto }`
- `.CreatorSlice_surfacePage__D5FDj { background:var(--butter-white) }`
- `.CreatorSlice_surfaceSubtle__v5RgA { background:var(--butter-off-white) }`
- `.CreatorSlice_surfaceMuted__nLVRI { background:var(--butter-light-grey) }`
- `.CreatorSlice_surfaceInverse___5xY_ { background:var(--butter-true-black);color:var(--butter-white) }`
- **Per-Selector Transition Rules**:
- **Selector `.CreatorSlice_secondaryButton__I1S9a`**: `transition: transform .2s var(--butter-ease-out),background .2s var(--butt...` extracted from `www-butter-video` stylesheet.
- **Selector `.CreatorSlice_tabs__0DQZR button`**: `transition: background .2s var(--butter-ease-out),color .2s var(--butter-e...` extracted from `www-butter-video` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none` extracted from `www-butter-video` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-butter-video`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
