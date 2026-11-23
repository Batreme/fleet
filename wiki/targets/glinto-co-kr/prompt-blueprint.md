---
title: "UI Prompt Blueprint: glinto-co-kr"
date: 2026-11-23
captured_at: 2026-11-23
target: "glinto-co-kr"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff5c34`)"
---

# UI Design System & Master Generation Blueprint: glinto-co-kr

> **Glinto — Creative studio** (https://glinto.co.kr) — Glinto is a creative studio where one team takes brand strategy and identity, film and photography, design, and web and app development f...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Glinto — Creative studio** (`https://glinto.co.kr`). Glinto is a creative studio where one team takes brand strategy and identity, film and photography, design, and web and app development f...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff5c34`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0f131f` primary typography and `#ff5c34` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Pretendard Variable` for display copy (`Everything your brand needs, from on`) with `Pretendard Variable` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `105rem` container bounds (`gap: var(--spacing-1)`, padding `var(--spacing-1)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `105rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--spacing-1)` lateral canvas padding with `var(--spacing-1)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--pixel-radius)`, `.5rem`, `.75rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 105rem`, `gap: var(--spacing-1)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f131f` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fdeceb` | `var(--danger-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ff5c34` | `var(--accent-500)` in `:root` |
| **Secondary / Muted Copy** | `#626880` | `var(--mock-muted)` in `:root` |
| **Structural Hairline Border** | `#626880` | hairline divider derived from `var(--mock-muted)` in `:root` |
| **Variable Token (`--accent-50`)** | `#fff3ee` | `var(--accent-50)` in `:root` |
| **Variable Token (`--accent-100`)** | `#ffe4d9` | `var(--accent-100)` in `:root` |
| **Variable Token (`--accent-200`)** | `#ffc7b0` | `var(--accent-200)` in `:root` |
| **Variable Token (`--accent-300`)** | `#ffa47d` | `var(--accent-300)` in `:root` |
| **Variable Token (`--accent-400`)** | `#ff7f54` | `var(--accent-400)` in `:root` |
| **Variable Token (`--accent-600`)** | `#e8451f` | `var(--accent-600)` in `:root` |
| **Variable Token (`--accent-700`)** | `#c13215` | `var(--accent-700)` in `:root` |
| **Variable Token (`--accent-800`)** | `#922712` | `var(--accent-800)` in `:root` |
| **Variable Token (`--accent-900`)** | `#611a0c` | `var(--accent-900)` in `:root` |
| **Variable Token (`--neutral-50`)** | `#fbf9f7` | `var(--neutral-50)` in `:root` |
| **Variable Token (`--neutral-100`)** | `#f5f1ed` | `var(--neutral-100)` in `:root` |
| **Variable Token (`--neutral-200`)** | `#e8e1da` | `var(--neutral-200)` in `:root` |
| **Variable Token (`--neutral-300`)** | `#d6ccc2` | `var(--neutral-300)` in `:root` |
| **Variable Token (`--neutral-400`)** | `#b3a79c` | `var(--neutral-400)` in `:root` |
| **Variable Token (`--neutral-500`)** | `#8f8177` | `var(--neutral-500)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent-50` | `#fff3ee` | Brand / Palette Token |
| `--accent-100` | `#ffe4d9` | Brand / Palette Token |
| `--accent-200` | `#ffc7b0` | Brand / Palette Token |
| `--accent-300` | `#ffa47d` | Brand / Palette Token |
| `--accent-400` | `#ff7f54` | Brand / Palette Token |
| `--accent-500` | `#ff5c34` | Brand / Palette Token |
| `--accent-600` | `#e8451f` | Brand / Palette Token |
| `--accent-700` | `#c13215` | Brand / Palette Token |
| `--accent-800` | `#922712` | Brand / Palette Token |
| `--accent-900` | `#611a0c` | Brand / Palette Token |
| `--neutral-50` | `#fbf9f7` | Color / Atmospheric Token |
| `--neutral-100` | `#f5f1ed` | Color / Atmospheric Token |
| `--neutral-200` | `#e8e1da` | Color / Atmospheric Token |
| `--neutral-300` | `#d6ccc2` | Color / Atmospheric Token |
| `--neutral-400` | `#b3a79c` | Color / Atmospheric Token |
| `--neutral-500` | `#8f8177` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Pretendard Variable`.
- **Primary Body Stack**: `Pretendard Variable`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--fs-xl: 1.25rem`, `--fs-h1: 1.625rem`, `--fs-display-sans: 2.125rem`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 60px`, `font-weight: 600`, `letter-spacing: -0.6px`); CSS variables `--fs-lg: 1.125rem`, `--fs-h2: 1.375rem`, `--tracking-h2: -.01em`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--fs-base: 1rem`, `--fs-body-s: .8125rem`, `--fs-body-m: .875rem`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--label-ink-start: var(--lime-cream-start)`, `--label-ink-end: var(--lime-cream-end)`, `--fs-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `glinto-co-kr` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `glinto-co-kr` stylesheet.
- **Selector `.transition-\[clip-path\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `glinto-co-kr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.site-header-wrap>` and `<section.pt-24>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Glinto — Creative studio                   │
│ ====================================================================== │
│ [ <header.site-header-wr (1440x64px)  | About · Services · Glinto.de ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.antialiased> (w=1440px)                       | │
│ | H1: Everything your brand needs, from one team                     | │
│ | Substrate: #ffffff | Ink: #0f131f | Accent: #ff5c34                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.pt-24>) max-w: 105rem                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Solutions shaped by how your |  | Launch & care                | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.pt-24:nth(2)>) — Experience with brand     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mt-24>      ) | https://glinto.co.kr                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--sp)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.site-header-wrap) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.antialiased>) — 390px Vertical Lead           | │
│ | H1: Everything your brand needs, from one team                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.pt-24>) — 1-Col Stack                     | │
│ | [ Item 1: Solutions shaped by how your brand runs                ] | │
│ | [ Item 2: Launch & care                                          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.pt-24:nth(2)>) — 1-Col (Experience with br) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mt-24>      ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header-wrap> — `glinto-co-kr`)**:
   - Landmark `<header class="site-header-wrap top-0">` (`1440x64px`) hosting `Glinto — Creative studio` navigation (`About · Services · Glinto.dev · Works · Contact`), DOM attributes (`data-theme="light"`, `data-reveal-ready`, `data-progress-ready`, `data-precedence="next"`), and stylesheet rule `sans_efc253b3-module__w1i8Da__cla... { font-family:DM Sans,DM Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Everything your brand needs, from `)**:
   - Landmark `<section class="antialiased">` presenting display lead `Everything your brand needs, from one team` and copy excerpt *"Creative studio for identity, visuals, and code."* over `#ffffff` canvas and `#0f131f` ink.
3. **Primary Showcase & Content Grid (<section.pt-24> — `Solutions shaped by how your brand`)**:
   - Landmark `<section class="pt-24">` rendering section `Solutions shaped by how your brand runs` with copy *"Engineering Build it"*, asset references (`2f7d2945a32bc936-s.p.0q9pvfn3wr_3...`, `5c285b27cdda1fe8-s.p.0lsanbtneewq...`, `0k1f2nt08p6_n.css`, `3b84er6uv62xn.css`), and grid rule `sans_efc253b3-module__w1i8Da__var... { --font-dm-sans:"DM Sans", "DM Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.pt-24:nth(2)> — `Launch & care`)**:
   - Landmark `<section class="pt-24">` framing `Launch & care` and `Experience with brands across industries` (*"From brand strategy to design, media and development, specialists"*) with `#fdeceb` surface cards, `#ff5c34` accents, and `f_kr_611a1780-module__N7vmma__cla... { font-family:Noto Serif KR,Noto Serif KR Fallback;font-style:normal;font-... }`.
5. **Colophon & Global Directory Footer (<footer.mt-24> — `https://glinto.co.kr`)**:
   - Landmark `<footer class="mt-24">` anchoring `Glinto — Creative studio` footer links (`About · Services · Glinto.dev · Works · Contact`), copy *"Start small with the one service you need right now."*, and `#626880` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: glinto-co-kr (Glinto — Creative studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `glinto-co-kr` (**Glinto — Creative studio** — `https://glinto.co.kr`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff5c34`).
- **Identity & Domain Context**: Glinto is a creative studio where one team takes brand strategy and identity, film and photography, design, and web and app development f...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0f131f`, **Accent / Highlight**: `#ff5c34`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0f131f` primary typography and `#ff5c34` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Pretendard Variable` for display copy (`Everything your brand needs, from on`) with `Pretendard Variable` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `105rem` container bounds (`gap: var(--spacing-1)`, padding `var(--spacing-1)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `glinto-co-kr` in your global stylesheet:

:root {
  /* Glinto — Creative studio (glinto-co-kr) — Live-Grounded CSS Variables */
  --accent-50: #fff3ee; /* Brand / Palette Token (glinto-co-kr) */
  --accent-100: #ffe4d9; /* Brand / Palette Token (glinto-co-kr) */
  --accent-200: #ffc7b0; /* Brand / Palette Token (glinto-co-kr) */
  --accent-300: #ffa47d; /* Brand / Palette Token (glinto-co-kr) */
  --accent-400: #ff7f54; /* Brand / Palette Token (glinto-co-kr) */
  --accent-500: #ff5c34; /* Brand / Palette Token (glinto-co-kr) */
  --accent-600: #e8451f; /* Brand / Palette Token (glinto-co-kr) */
  --accent-700: #c13215; /* Brand / Palette Token (glinto-co-kr) */
  --accent-800: #922712; /* Brand / Palette Token (glinto-co-kr) */
  --accent-900: #611a0c; /* Brand / Palette Token (glinto-co-kr) */
  --neutral-50: #fbf9f7; /* Color / Atmospheric Token (glinto-co-kr) */
  --neutral-100: #f5f1ed; /* Color / Atmospheric Token (glinto-co-kr) */
  --neutral-200: #e8e1da; /* Color / Atmospheric Token (glinto-co-kr) */
  --neutral-300: #d6ccc2; /* Color / Atmospheric Token (glinto-co-kr) */
  --neutral-400: #b3a79c; /* Color / Atmospheric Token (glinto-co-kr) */
  --neutral-500: #8f8177; /* Color / Atmospheric Token (glinto-co-kr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0f131f` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#fdeceb` — grounded in `var(--danger-bg)` in `:root`
- **Interactive Accent / Highlight**: `#ff5c34` — grounded in `var(--accent-500)` in `:root`
- **Secondary / Muted Copy**: `#626880` — grounded in `var(--mock-muted)` in `:root`
- **Structural Hairline Border**: `#626880` — grounded in hairline divider derived from `var(--mock-muted)` in `:root`
- **Variable Token (`--accent-50`)**: `#fff3ee` — grounded in `var(--accent-50)` in `:root`
- **Variable Token (`--accent-100`)**: `#ffe4d9` — grounded in `var(--accent-100)` in `:root`
- **Variable Token (`--accent-200`)**: `#ffc7b0` — grounded in `var(--accent-200)` in `:root`
- **Variable Token (`--accent-300`)**: `#ffa47d` — grounded in `var(--accent-300)` in `:root`
- **Variable Token (`--accent-400`)**: `#ff7f54` — grounded in `var(--accent-400)` in `:root`
- **Variable Token (`--accent-600`)**: `#e8451f` — grounded in `var(--accent-600)` in `:root`
- **Variable Token (`--accent-700`)**: `#c13215` — grounded in `var(--accent-700)` in `:root`
- **Variable Token (`--accent-800`)**: `#922712` — grounded in `var(--accent-800)` in `:root`
- **Variable Token (`--accent-900`)**: `#611a0c` — grounded in `var(--accent-900)` in `:root`
- **Variable Token (`--neutral-50`)**: `#fbf9f7` — grounded in `var(--neutral-50)` in `:root`
- **Variable Token (`--neutral-100`)**: `#f5f1ed` — grounded in `var(--neutral-100)` in `:root`
- **Variable Token (`--neutral-200`)**: `#e8e1da` — grounded in `var(--neutral-200)` in `:root`
- **Variable Token (`--neutral-300`)**: `#d6ccc2` — grounded in `var(--neutral-300)` in `:root`
- **Variable Token (`--neutral-400`)**: `#b3a79c` — grounded in `var(--neutral-400)` in `:root`
- **Variable Token (`--neutral-500`)**: `#8f8177` — grounded in `var(--neutral-500)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `105rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--spacing-1)` lateral canvas padding with `var(--spacing-1)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 105rem`, `gap: var(--spacing-1)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `var(--pixel-radius)`, `.5rem`, `.75rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Pretendard Variable`
- **Body Font Stack**: `Pretendard Variable`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--fs-xl: 1.25rem`, `--fs-h1: 1.625rem`, `--fs-display-sans: 2.125rem`
- **H2 Section Rule**: live computed `h2` (`font-size: 40px`, `line-height: 60px`, `font-weight: 600`, `letter-spacing: -0.6px`); CSS variables `--fs-lg: 1.125rem`, `--fs-h2: 1.375rem`, `--tracking-h2: -.01em`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--fs-base: 1rem`, `--fs-body-s: .8125rem`, `--fs-body-m: .875rem`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--label-ink-start: var(--lime-cream-start)`, `--label-ink-end: var(--lime-cream-end)`, `--fs-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `glinto-co-kr` (`Glinto — Creative studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header-wrap> — `glinto-co-kr`)**:
   - DOM & Selectors: Landmark `<header class="site-header-wrap top-0">` (`1440x64px`) hosting `Glinto — Creative studio` navigation (`About · Services · Glinto.dev · Works · Contact`), DOM attributes (`data-theme="light"`, `data-reveal-ready`, `data-progress-ready`, `data-precedence="next"`), and stylesheet rule `sans_efc253b3-module__w1i8Da__cla... { font-family:DM Sans,DM Sans Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header-wrap> — `glinto-co-kr`)` (`glinto-co-kr`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `About · Services · Glinto.dev · Works · Contact`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Everything your brand needs, from `)**:
   - DOM & Selectors: Landmark `<section class="antialiased">` presenting display lead `Everything your brand needs, from one team` and copy excerpt *"Creative studio for identity, visuals, and code."* over `#ffffff` canvas and `#0f131f` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#0f131f` headline `Everything your brand needs, from one team`.
3. **Primary Showcase & Content Grid (<section.pt-24> — `Solutions shaped by how your brand`)**:
   - DOM & Selectors: Landmark `<section class="pt-24">` rendering section `Solutions shaped by how your brand runs` with copy *"Engineering Build it"*, asset references (`2f7d2945a32bc936-s.p.0q9pvfn3wr_3...`, `5c285b27cdda1fe8-s.p.0lsanbtneewq...`, `0k1f2nt08p6_n.css`, `3b84er6uv62xn.css`), and grid rule `sans_efc253b3-module__w1i8Da__var... { --font-dm-sans:"DM Sans", "DM Sans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.pt-24> — `Solutions shaped by how your brand`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 105rem`, `gap: var(--spacing-1)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.pt-24:nth(2)> — `Launch & care`)**:
   - DOM & Selectors: Landmark `<section class="pt-24">` framing `Launch & care` and `Experience with brands across industries` (*"From brand strategy to design, media and development, specialists"*) with `#fdeceb` surface cards, `#ff5c34` accents, and `f_kr_611a1780-module__N7vmma__cla... { font-family:Noto Serif KR,Noto Serif KR Fallback;font-style:normal;font-... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.pt-24:nth(2)> — `Launch & care`)` uses `.25rem`, `var(--pixel-radius)`, `.5rem`, `.75rem` radii, `#ff5c34` highlights, and assets (2f7d2945a32bc936-s.p.0q9pvfn3wr_3..., 5c285b27cdda1fe8-s.p.0lsanbtneewq..., 0k1f2nt08p6_n.css).
5. **Colophon & Global Directory Footer (<footer.mt-24> — `https://glinto.co.kr`)**:
   - DOM & Selectors: Landmark `<footer class="mt-24">` anchoring `Glinto — Creative studio` footer links (`About · Services · Glinto.dev · Works · Contact`), copy *"Start small with the one service you need right now."*, and `#626880` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mt-24> — `https://glinto.co.kr`)` aligns to `105rem` (non-`@media` desktop container stylesheet rule) with `var(--spacing-1)` lateral canvas padding with `var(--spacing-1)` grid gap and attributes (data-theme="light", data-reveal-ready, data-progress-ready).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Creative studio for identity, visuals, and code."*
- Copy Excerpt 2: *"Engineering Build it"*
- Copy Excerpt 3: *"From brand strategy to design, media and development, specialists in each field wo..."*
- Copy Excerpt 4: *"Start small with the one service you need right now."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`glinto-co-kr`)**:
- `sans_efc253b3-module__w1i8Da__cla... { font-family:DM Sans,DM Sans Fallback;font-style:normal }`
- `sans_efc253b3-module__w1i8Da__var... { --font-dm-sans:"DM Sans", "DM Sans Fallback" }`
- `f_kr_611a1780-module__N7vmma__cla... { font-family:Noto Serif KR,Noto Serif KR Fallback;font-style:normal;font-... }`
- `mono_dee0ec74-module__m2KSdq__cla... { font-family:JetBrains Mono,JetBrains Mono Fallback;font-style:normal }`
- `rbit_fbf1de06-module__6Zwo7q__cla... { font-family:Orbit,Orbit Fallback;font-style:normal;font-weight:400 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `glinto-co-kr` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `glinto-co-kr` stylesheet.
- **Selector `.transition-\[clip-path\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `glinto-co-kr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.site-header-wrap>` and `<section.pt-24>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `glinto-co-kr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
