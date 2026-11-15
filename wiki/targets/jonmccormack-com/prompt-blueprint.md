---
title: "UI Prompt Blueprint: jonmccormack-com"
date: 2026-11-15
target: "[[overview|jonmccormack-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#ffffff` ink, `#006ba1` accent)"
---

# UI Design System & Master Generation Blueprint: jonmccormack-com

> **Patterns - Jon McCormack** (https://jonmccormack.com/) — Explore the intriguing repeating patterns in nature that captivate the eye and remind us of the awe and beauty in the world.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/jonmccormack-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Patterns - Jon McCormack** (`https://jonmccormack.com/`). Explore the intriguing repeating patterns in nature that captivate the eye and remind us of the awe and beauty in the world.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#ffffff` ink, `#006ba1` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#7a00df` (`var(--wp-block-synced-color)` in `:root`) paired with `#ffffff` primary typography and `#006ba1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Aeonik Pro` for display copy (`A e r i a l P a t t e r n s`) with `Fira Code` and `Fira Code`.
  - **Calibrated Spatial Grid & Motion**: Combines `781px` container bounds (`gap: 1rem`, padding `0.875rem`) with `cubic-bezier(0.22,1,0.36,1)` easing and GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/jonmccormack-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `781px` extracted from `jonmccormack-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0.875rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `50%`, `9999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 781px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0.875rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (max-width: 781px)`, `@media (min-width: 769px)`, `@media only screen and (max-width: 768px)`, `@media only screen and (min-width: 769px) and (max-width: 1200px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Interactive Accent / Highlight** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Secondary / Muted Copy** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `::selection { color: white }` (`#ffffff`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gf-field-gap` | `1.5rem` | Layout / Spatial Grid Token |
| `--gf-input-padding` | `0.875rem 1rem` | Layout / Spatial Grid Token |
| `--gf-border-width` | `1px` | Layout / Spatial Grid Token |
| `--jm-shell-header` | `10vh` | Layout / Spatial Grid Token |
| `--jm-shell-content` | `80vh` | Dimension / Scale Token |
| `--jm-shell-footer` | `8vh` | Dimension / Scale Token |
| `--navigation-layout-justification-setting` | `flex-start` | Layout / Spatial Grid Token |
| `--navigation-layout-direction` | `row` | Layout / Spatial Grid Token |
| `--navigation-layout-wrap` | `wrap` | Layout / Spatial Grid Token |
| `--navigation-layout-justify` | `flex-start` | Layout / Spatial Grid Token |
| `--navigation-layout-align` | `center` | Layout / Spatial Grid Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Aeonik Pro`.
- **Primary Body Stack**: `Fira Code`.
- **Technical / Metadata Stack**: `Fira Code`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `footer li`**: `transition: all 0.3s ease-in-out` extracted from `jonmccormack-com` stylesheet.
- **Selector `.is-style-editorial-heading`**: `transition: all 0.3s ease-in-out` extracted from `jonmccormack-com` stylesheet.
- **Selector `.jm-attachment-modal .jm-attachme...`**: `transition: opacity 250ms ease, transform 350ms cubic-bezier(0.22, 1, 0.36...` extracted from `jonmccormack-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.wp-block-template-part>` and `<article.jm-patterns-landing__item>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Patterns - Jon McCormack                   │
│ ====================================================================== │
│ [ <header.wp-block-templat | Patterns · News · Book · Bio           ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.jm-patterns-landing__item>                  |   │
│ | H1: A e r i a l P a t t e r n s                                  |   │
│ | Substrate: #7a00df    | Ink: #ffffff    | Accent: #006ba1        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.jm-patterns-landi) max-w: 781px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | T i n y P a t t e r n s      |  | P o l a r P a t t e r n s    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem  ) | │
│ | [<header.wp-block-t] -> [<article.jm-patter] -> [<article.jm-patter] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wp-block-templ) | https://jonmccormack.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.wp-block-template-part> — `jonmccormack-com`)**:
   - Landmark `<header class="wp-block-template-part">` hosting `Patterns - Jon McCormack` navigation (`Patterns · News · Book · Bio`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-interactive="core/navigation"`, `data-wp-context="("overlayOpenedBy":("..."`, `data-wp-on--click="actions.openMenuOnClick"`), and stylesheet rule `html.jm-splash-viewed .jm-splash { display: none !important; }`.
2. **Hero Stage & Focal Lead (<article.jm-patterns-landing__item> — `A e r i a l P a t t e r n s`)**:
   - Landmark `<article class="jm-patterns-landing__item">` presenting display lead `A e r i a l P a t t e r n s` and copy excerpt *"A e r i a l P a t t e r n s"* over `#7a00df` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.jm-patterns-landing__item> — `T i n y P a t t e r n s`)**:
   - Landmark `<article class="jm-patterns-landing__item">` rendering section `T i n y P a t t e r n s` with copy *"T i n y P a t t e r n s"*, asset references (`cdnjs.cloudflare.com`, `www.googletagmanager.com`, `embed`, `splash.css`), and grid rule `textarea:focus { outline: none !important; box-shadow: none !important; }`.
4. **Interactive Detail & Feature Matrix (<article.jm-patterns-landing__item> — `P o l a r P a t t e r n s`)**:
   - Landmark `<article class="jm-patterns-landing__item">` framing `P o l a r P a t t e r n s` and `S m a l l P a t t e r n s` (*"P o l a r P a t t e r n s"*) with `#007cba` surface cards, `#006ba1` accents, and `selection { background: rgb(144, 144, 144); color: white; }`.
5. **Colophon & Global Directory Footer (<footer.wp-block-template-part> — `https://jonmccormack.com/`)**:
   - Landmark `<footer class="wp-block-template-part">` anchoring `Patterns - Jon McCormack` footer links (`Patterns · News · Book · Bio`), copy *"S m a l l P a t t e r n s"*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: jonmccormack-com (Patterns - Jon McCormack)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `jonmccormack-com` (**Patterns - Jon McCormack** — `https://jonmccormack.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#ffffff` ink, `#006ba1` accent).
- **Identity & Domain Context**: Explore the intriguing repeating patterns in nature that captivate the eye and remind us of the awe and beauty in the world.
- **Primary Substrate**: `#7a00df` (`var(--wp-block-synced-color)` in `:root`), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#006ba1`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#7a00df` (`var(--wp-block-synced-color)` in `:root`) paired with `#ffffff` primary typography and `#006ba1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Aeonik Pro` for display copy (`A e r i a l P a t t e r n s`) with `Fira Code` and `Fira Code`.
  - **Calibrated Spatial Grid & Motion**: Combines `781px` container bounds (`gap: 1rem`, padding `0.875rem`) with `cubic-bezier(0.22,1,0.36,1)` easing and GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `jonmccormack-com` in your global stylesheet:

:root {
  /* Patterns - Jon McCormack (jonmccormack-com) — Ground-Truth Extracted CSS Variables */
  --gf-field-gap: 1.5rem; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --gf-input-padding: 0.875rem 1rem; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --gf-border-width: 1px; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --jm-shell-header: 10vh; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --jm-shell-content: 80vh; /* Dimension / Scale Token (jonmccormack-com) */
  --jm-shell-footer: 8vh; /* Dimension / Scale Token (jonmccormack-com) */
  --navigation-layout-justification-setting: flex-start; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --navigation-layout-direction: row; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --navigation-layout-wrap: wrap; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --navigation-layout-justify: flex-start; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --navigation-layout-align: center; /* Layout / Spatial Grid Token (jonmccormack-com) */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (jonmccormack-com) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (jonmccormack-com) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (jonmccormack-com) */
  --wp-editor-canvas-background: #ddd; /* Canvas / Surface Token (jonmccormack-com) */
  --wp-admin-theme-color: #007cba; /* Brand / Palette Token (jonmccormack-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Primary Typography Ink**: `#ddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Elevated Surface / Card Substrate**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`
- **Interactive Accent / Highlight**: `#006ba1` — grounded in `var(--wp-admin-theme-color-darker-10)` in `:root`
- **Secondary / Muted Copy**: `#005a87` — grounded in `var(--wp-admin-theme-color-darker-20)` in `:root`
- **Structural Hairline Border**: `#ffffff` — grounded in `::selection { color: white }` (`#ffffff`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `781px` extracted from `jonmccormack-com` stylesheet
- **Padding & Gutters**: `0.875rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 781px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0.875rem` horizontal padding
- **Media Queries**: `@media only screen and (max-width: 781px)`, `@media (min-width: 769px)`, `@media only screen and (max-width: 768px)`, `@media only screen and (min-width: 769px) and (max-width: 1200px)`
- **Corner Radii**: `50%`, `9999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Aeonik Pro`
- **Body Font Stack**: `Fira Code`
- **Monospace / Technical Font Stack**: `Fira Code`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `jonmccormack-com` (`Patterns - Jon McCormack`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.wp-block-template-part> — `jonmccormack-com`)**:
   - DOM & Selectors: Landmark `<header class="wp-block-template-part">` hosting `Patterns - Jon McCormack` navigation (`Patterns · News · Book · Bio`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-interactive="core/navigation"`, `data-wp-context="("overlayOpenedBy":("..."`, `data-wp-on--click="actions.openMenuOnClick"`), and stylesheet rule `html.jm-splash-viewed .jm-splash { display: none !important; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.wp-block-template-part> — `jonmccormack-com`)` (`jonmccormack-com`) adapts across `@media only screen and (max-width: 781px)`, `@media (min-width: 769px)`, `@media only screen and (max-width: 768px)`, `@media only screen and (min-width: 769px) and (max-width: 1200px)` with `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Patterns · News · Book · Bio`.
2. **Hero Stage & Focal Lead (<article.jm-patterns-landing__item> — `A e r i a l P a t t e r n s`)**:
   - DOM & Selectors: Landmark `<article class="jm-patterns-landing__item">` presenting display lead `A e r i a l P a t t e r n s` and copy excerpt *"A e r i a l P a t t e r n s"* over `#7a00df` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#7a00df` background with `#ffffff` headline `A e r i a l P a t t e r n s`.
3. **Primary Showcase & Content Grid (<article.jm-patterns-landing__item> — `T i n y P a t t e r n s`)**:
   - DOM & Selectors: Landmark `<article class="jm-patterns-landing__item">` rendering section `T i n y P a t t e r n s` with copy *"T i n y P a t t e r n s"*, asset references (`cdnjs.cloudflare.com`, `www.googletagmanager.com`, `embed`, `splash.css`), and grid rule `textarea:focus { outline: none !important; box-shadow: none !important; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.jm-patterns-landing__item> — `T i n y P a t t e r n s`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 781px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `0.875rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.jm-patterns-landing__item> — `P o l a r P a t t e r n s`)**:
   - DOM & Selectors: Landmark `<article class="jm-patterns-landing__item">` framing `P o l a r P a t t e r n s` and `S m a l l P a t t e r n s` (*"P o l a r P a t t e r n s"*) with `#007cba` surface cards, `#006ba1` accents, and `selection { background: rgb(144, 144, 144); color: white; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.jm-patterns-landing__item> — `P o l a r P a t t e r n s`)` uses `50%`, `9999px` radii, `#006ba1` highlights, and assets (cdnjs.cloudflare.com, www.googletagmanager.com, embed).
5. **Colophon & Global Directory Footer (<footer.wp-block-template-part> — `https://jonmccormack.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wp-block-template-part">` anchoring `Patterns - Jon McCormack` footer links (`Patterns · News · Book · Bio`), copy *"S m a l l P a t t e r n s"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wp-block-template-part> — `https://jonmccormack.com/`)` aligns to `781px` extracted from `jonmccormack-com` stylesheet with `0.875rem` lateral canvas padding with `1rem` grid gap and attributes (data-wp-strategy="defer", data-wp-interactive="core/navigation", data-wp-context="("overlayOpenedBy":("...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A e r i a l P a t t e r n s"*
- Copy Excerpt 2: *"T i n y P a t t e r n s"*
- Copy Excerpt 3: *"P o l a r P a t t e r n s"*
- Copy Excerpt 4: *"S m a l l P a t t e r n s"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`jonmccormack-com`)**:
- `html.jm-splash-viewed .jm-splash { display: none !important; }`
- `textarea:focus { outline: none !important; box-shadow: none !important; }`
- `selection { background: rgb(144, 144, 144); color: white; }`
- `.wp-block-site-title a { letter-spacing: 0; font-size: clamp(1.95rem, 1.6vw, 2.8rem); }`
- `.wp-block-site-title a:hover { text-decoration: none; }`
- **Per-Selector Transition Rules**:
- **Selector `footer li`**: `transition: all 0.3s ease-in-out` extracted from `jonmccormack-com` stylesheet.
- **Selector `.is-style-editorial-heading`**: `transition: all 0.3s ease-in-out` extracted from `jonmccormack-com` stylesheet.
- **Selector `.jm-attachment-modal .jm-attachme...`**: `transition: opacity 250ms ease, transform 350ms cubic-bezier(0.22, 1, 0.36...` extracted from `jonmccormack-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.wp-block-template-part>` and `<article.jm-patterns-landing__item>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `jonmccormack-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
