---
title: "UI Prompt Blueprint: crun-ai"
date: 2026-11-15
target: "[[overview|crun-ai]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#409eff` canvas, `#18222b` ink, `#213d5b` accent)"
---

# UI Design System & Master Generation Blueprint: crun-ai

> **One API for All Top AI Models – Cost-Effective AI API · Crun** (https://crun.ai) — One API to access all top AI models—video, image, audio, and text. Fast integration, 30–70% cost savings, high-performance, and developer...

![Desktop Viewport Capture (1440x7745)](file:///root/projects/fleet/wiki/targets/crun-ai/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **One API for All Top AI Models – Cost-Effective AI API · Crun** (`https://crun.ai`). One API to access all top AI models—video, image, audio, and text. Fast integration, 30–70% cost savings, high-performance, and developer...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#409eff` canvas, `#18222b` ink, `#213d5b` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#409eff` (`var(--el-color-primary)` in `:root`) paired with `#18222b` primary typography and `#213d5b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Poppins` for display copy (`Top AI Video, Image & Audio Models i`) with `Crisp Noto Sans Regular` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: 4px`, padding `14px`) with `cubic-bezier(.4,0,1,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/crun-ai/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7745px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `crun-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `14px` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `var(--el-notification-radius)`, `10px`, `9999px`, `9px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `14px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce),print`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#409eff` | `var(--el-color-primary)` in `:root` |
| **Primary Typography Ink** | `#3375b9` | `var(--el-color-primary-light-3)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2a598a` | `var(--el-color-primary-light-5)` in `:root` |
| **Interactive Accent / Highlight** | `#213d5b` | `var(--el-color-primary-light-7)` in `:root` |
| **Secondary / Muted Copy** | `#1d3043` | `var(--el-color-primary-light-8)` in `:root` |
| **Structural Hairline Border** | `#18222b` | `var(--el-color-primary-light-9)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--el-notification-width` | `330px` | Layout / Spatial Grid Token |
| `--el-notification-padding` | `14px 26px 14px 13px` | Layout / Spatial Grid Token |
| `--el-notification-radius` | `8px` | Elevation / Border Token |
| `--el-notification-shadow` | `var(--el-box-shadow-light)` | Elevation / Border Token |
| `--el-notification-border-color` | `var(--el-border-color-lighter)` | Brand / Palette Token |
| `--el-notification-icon-size` | `24px` | Layout / Spatial Grid Token |
| `--el-notification-close-font-size` | `var(--el-message-close-size,16px)` | Typography / Scale Token |
| `--el-notification-group-margin-left` | `13px` | Layout / Spatial Grid Token |
| `--el-notification-group-margin-right` | `8px` | Layout / Spatial Grid Token |
| `--el-notification-content-font-size` | `var(--el-font-size-base)` | Typography / Scale Token |
| `--el-notification-content-color` | `var(--el-text-color-regular)` | Brand / Palette Token |
| `--el-notification-title-font-size` | `16px` | Typography / Scale Token |
| `--el-notification-title-color` | `var(--el-text-color-primary)` | Brand / Palette Token |
| `--el-notification-close-color` | `var(--el-text-color-secondary)` | Brand / Palette Token |
| `--el-notification-close-hover-color` | `var(--el-text-color-regular)` | Brand / Palette Token |
| `--el-notification-icon-color` | `var(--el-color-primary)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Poppins`.
- **Primary Body Stack**: `Crisp Noto Sans Regular`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em!important`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5em!important`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--el-font-size-base: 14px`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.el-notification`**: `transition: opacity var(--el-transition-duration),transform var(--el-trans...` extracted from `crun-ai` stylesheet.
- **Selector `print`**: `transition: 1ms!important` extracted from `crun-ai` stylesheet.
- **Selector `80%`**: `transition: cubic-bezier(.4,0,1,1)` extracted from `crun-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.pt-10>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — One API for All Top AI Models – Cost-Effec │
│ ====================================================================== │
│ [ <header.fixed>           | AI Agent NEW · Seedance 2.5 HOT · Klin ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Top AI Video, Image & Audio Models in One API                |   │
│ | Substrate: #409eff    | Ink: #18222b    | Accent: #213d5b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.pt-10>           ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Popular AI API Models        |  | Nano Banana 2.1              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px   ) | │
│ | [<header.fixed>] -> [<section.relative>] -> [<section.pt-10>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.right-0>      ) | https://crun.ai                    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `crun-ai`)**:
   - Landmark `<header class="fixed left-0">` hosting `One API for All Top AI Models – Cost` navigation (`AI Agent NEW · Seedance 2.5 HOT · Kling 4.0 NEW · Seedance 2.0 · Seedance 2.0 Mini`), DOM attributes (`data-gtag`, `data-v-c988fe2b`, `data-v-b2c0d9f1`, `data-v-2f8ea121`), and stylesheet rule `.el-notification.right { right:16px }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Top AI Video, Image & Audio Models`)**:
   - Landmark `<section class="relative flex">` presenting display lead `Top AI Video, Image & Audio Models in One API` and copy excerpt *"Seedance 2.0 Mini video from $0.008/sec. Built for AI comic serie"* over `#409eff` canvas and `#18222b` ink.
3. **Primary Showcase & Content Grid (<section.pt-10> — `Popular AI API Models`)**:
   - Landmark `<section class="pt-10 relative">` rendering section `Popular AI API Models` with copy *"Seedance 2.0 Mini video from $0.008/sec."*, asset references (`entry.C15VBcyN.css`, `el-notification.D1R47t8o.css`, `index.ByFwvLCV.css`, `advantagesGrid.o3VIx7N9.css`), and grid rule `cation .el-notification__closeBtn... { color:var(--el-notification-close-hover-color) }`.
4. **Interactive Detail & Feature Matrix (<section.px-4> — `Nano Banana 2.1`)**:
   - Landmark `<section class="px-4 pt-8">` framing `Nano Banana 2.1` and `Seedance 2.5` (*"Built for AI comic series and short videos, with cost-effective g"*) with `#2a598a` surface cards, `#213d5b` accents, and `notification .el-notification--pr... { --el-notification-icon-color:var(--el-color-primary);color:var(--el-noti... }`.
5. **Colophon & Global Directory Footer (<footer.right-0> — `https://crun.ai`)**:
   - Landmark `<footer class="right-0">` anchoring `One API for All Top AI Models – ` footer links (`AI Agent NEW · Seedance 2.5 HOT · Kling 4.0 NEW · Seedance 2.0 · Seedance 2.0 Mini`), copy *"Video API Seedance 2.5 HOT Kling 4.0 NEW Seedance 2.0 Seedan"*, and `#18222b` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: crun-ai (One API for All Top AI Models – Cost-Effective AI API · Crun)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `crun-ai` (**One API for All Top AI Models – Cost-Effective AI API · Crun** — `https://crun.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#409eff` canvas, `#18222b` ink, `#213d5b` accent).
- **Identity & Domain Context**: One API to access all top AI models—video, image, audio, and text. Fast integration, 30–70% cost savings, high-performance, and developer...
- **Primary Substrate**: `#409eff` (`var(--el-color-primary)` in `:root`), **Primary Ink**: `#18222b`, **Accent / Highlight**: `#213d5b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#409eff` (`var(--el-color-primary)` in `:root`) paired with `#18222b` primary typography and `#213d5b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Poppins` for display copy (`Top AI Video, Image & Audio Models i`) with `Crisp Noto Sans Regular` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: 4px`, padding `14px`) with `cubic-bezier(.4,0,1,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `crun-ai` in your global stylesheet:

:root {
  /* One API for All Top AI Models – Cost-Effective AI API · Crun (crun-ai) — Ground-Truth Extracted CSS Variables */
  --el-notification-width: 330px; /* Layout / Spatial Grid Token (crun-ai) */
  --el-notification-padding: 14px 26px 14px 13px; /* Layout / Spatial Grid Token (crun-ai) */
  --el-notification-radius: 8px; /* Elevation / Border Token (crun-ai) */
  --el-notification-shadow: var(--el-box-shadow-light); /* Elevation / Border Token (crun-ai) */
  --el-notification-border-color: var(--el-border-color-lighter); /* Brand / Palette Token (crun-ai) */
  --el-notification-icon-size: 24px; /* Layout / Spatial Grid Token (crun-ai) */
  --el-notification-close-font-size: var(--el-message-close-size,16px); /* Typography / Scale Token (crun-ai) */
  --el-notification-group-margin-left: 13px; /* Layout / Spatial Grid Token (crun-ai) */
  --el-notification-group-margin-right: 8px; /* Layout / Spatial Grid Token (crun-ai) */
  --el-notification-content-font-size: var(--el-font-size-base); /* Typography / Scale Token (crun-ai) */
  --el-notification-content-color: var(--el-text-color-regular); /* Brand / Palette Token (crun-ai) */
  --el-notification-title-font-size: 16px; /* Typography / Scale Token (crun-ai) */
  --el-notification-title-color: var(--el-text-color-primary); /* Brand / Palette Token (crun-ai) */
  --el-notification-close-color: var(--el-text-color-secondary); /* Brand / Palette Token (crun-ai) */
  --el-notification-close-hover-color: var(--el-text-color-regular); /* Brand / Palette Token (crun-ai) */
  --el-notification-icon-color: var(--el-color-primary); /* Brand / Palette Token (crun-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#409eff` — grounded in `var(--el-color-primary)` in `:root`
- **Primary Typography Ink**: `#3375b9` — grounded in `var(--el-color-primary-light-3)` in `:root`
- **Elevated Surface / Card Substrate**: `#2a598a` — grounded in `var(--el-color-primary-light-5)` in `:root`
- **Interactive Accent / Highlight**: `#213d5b` — grounded in `var(--el-color-primary-light-7)` in `:root`
- **Secondary / Muted Copy**: `#1d3043` — grounded in `var(--el-color-primary-light-8)` in `:root`
- **Structural Hairline Border**: `#18222b` — grounded in `var(--el-color-primary-light-9)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7745px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `crun-ai` stylesheet
- **Padding & Gutters**: `14px` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `14px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce),print`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`
- **Corner Radii**: `var(--el-notification-radius)`, `10px`, `9999px`, `9px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Crisp Noto Sans Regular`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em!important`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5em!important`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--el-font-size-base: 14px`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `crun-ai` (`One API for All Top AI Models – Cost-Effective AI API · Crun`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `crun-ai`)**:
   - DOM & Selectors: Landmark `<header class="fixed left-0">` hosting `One API for All Top AI Models – Cost` navigation (`AI Agent NEW · Seedance 2.5 HOT · Kling 4.0 NEW · Seedance 2.0 · Seedance 2.0 Mini`), DOM attributes (`data-gtag`, `data-v-c988fe2b`, `data-v-b2c0d9f1`, `data-v-2f8ea121`), and stylesheet rule `.el-notification.right { right:16px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `crun-ai`)` (`crun-ai`) adapts across `@media (prefers-reduced-motion:reduce),print`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `AI Agent NEW · Seedance 2.5 HOT · Kling 4.0 NEW · Seedance 2.0 · Seedance 2.0 Mini`.
2. **Hero Stage & Focal Lead (<section.relative> — `Top AI Video, Image & Audio Models`)**:
   - DOM & Selectors: Landmark `<section class="relative flex">` presenting display lead `Top AI Video, Image & Audio Models in One API` and copy excerpt *"Seedance 2.0 Mini video from $0.008/sec. Built for AI comic serie"* over `#409eff` canvas and `#18222b` ink.
   - Responsive Contract: Hero stage (`1440×7745px` desktop / `390×2400px` mobile) sets `#409eff` background with `#18222b` headline `Top AI Video, Image & Audio Models in One API`.
3. **Primary Showcase & Content Grid (<section.pt-10> — `Popular AI API Models`)**:
   - DOM & Selectors: Landmark `<section class="pt-10 relative">` rendering section `Popular AI API Models` with copy *"Seedance 2.0 Mini video from $0.008/sec."*, asset references (`entry.C15VBcyN.css`, `el-notification.D1R47t8o.css`, `index.ByFwvLCV.css`, `advantagesGrid.o3VIx7N9.css`), and grid rule `cation .el-notification__closeBtn... { color:var(--el-notification-close-hover-color) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.pt-10> — `Popular AI API Models`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `14px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.px-4> — `Nano Banana 2.1`)**:
   - DOM & Selectors: Landmark `<section class="px-4 pt-8">` framing `Nano Banana 2.1` and `Seedance 2.5` (*"Built for AI comic series and short videos, with cost-effective g"*) with `#2a598a` surface cards, `#213d5b` accents, and `notification .el-notification--pr... { --el-notification-icon-color:var(--el-color-primary);color:var(--el-noti... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.px-4> — `Nano Banana 2.1`)` uses `var(--el-notification-radius)`, `10px`, `9999px`, `9px` radii, `#213d5b` highlights, and assets (entry.C15VBcyN.css, el-notification.D1R47t8o.css, index.ByFwvLCV.css).
5. **Colophon & Global Directory Footer (<footer.right-0> — `https://crun.ai`)**:
   - DOM & Selectors: Landmark `<footer class="right-0">` anchoring `One API for All Top AI Models – ` footer links (`AI Agent NEW · Seedance 2.5 HOT · Kling 4.0 NEW · Seedance 2.0 · Seedance 2.0 Mini`), copy *"Video API Seedance 2.5 HOT Kling 4.0 NEW Seedance 2.0 Seedan"*, and `#18222b` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.right-0> — `https://crun.ai`)` aligns to `640px` extracted from `crun-ai` stylesheet with `14px` lateral canvas padding with `4px` grid gap and attributes (data-gtag, data-v-c988fe2b, data-v-b2c0d9f1).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Seedance 2.0 Mini video from $0.008/sec. Built for AI comic series and short video..."*
- Copy Excerpt 2: *"Seedance 2.0 Mini video from $0.008/sec."*
- Copy Excerpt 3: *"Built for AI comic series and short videos, with cost-effective generation at as l..."*
- Copy Excerpt 4: *"Video API Seedance 2.5 HOT Kling 4.0 NEW Seedance 2.0 Seedance 2.0 Mini Grok Imagi..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`crun-ai`)**:
- `.el-notification.right { right:16px }`
- `cation .el-notification__closeBtn... { color:var(--el-notification-close-hover-color) }`
- `notification .el-notification--pr... { --el-notification-icon-color:var(--el-color-primary);color:var(--el-noti... }`
- `notification .el-notification--su... { --el-notification-icon-color:var(--el-color-success);color:var(--el-noti... }`
- `.el-notification .el-notification... { --el-notification-icon-color:var(--el-color-info);color:var(--el-notific... }`
- **Per-Selector Transition Rules**:
- **Selector `.el-notification`**: `transition: opacity var(--el-transition-duration),transform var(--el-trans...` extracted from `crun-ai` stylesheet.
- **Selector `print`**: `transition: 1ms!important` extracted from `crun-ai` stylesheet.
- **Selector `80%`**: `transition: cubic-bezier(.4,0,1,1)` extracted from `crun-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.pt-10>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `crun-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
