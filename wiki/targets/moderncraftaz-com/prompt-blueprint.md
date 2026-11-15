---
title: "UI Prompt Blueprint: moderncraftaz-com"
date: 2026-11-15
target: "[[overview|moderncraftaz-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#4831B0` canvas, `#FFFFFF` ink, `#7a00df` accent)"
---

# UI Design System & Master Generation Blueprint: moderncraftaz-com

> **Select A Location · AllHaus** (https://moderncraftaz.com/) — Crafting exceptional residences with unmatched service in Arizona, Montana, and beyond.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/moderncraftaz-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Select A Location · AllHaus** (`https://moderncraftaz.com/`). Crafting exceptional residences with unmatched service in Arizona, Montana, and beyond.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#4831B0` canvas, `#FFFFFF` ink, `#7a00df` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#4831B0` (`var(--oxynav-brand-color)` in `:root`) paired with `#FFFFFF` primary typography and `#7a00df` accents.
  - **Extracted Typographic Hierarchy**: Pairs `didot-01` for display copy (`Unparallelled Service For Exceptiona`) with `didot-02` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `479px` container bounds (`gap: 3rem`, padding `4rem`) with `cubic-bezier(0.455,0.03,0.515,0.955)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/moderncraftaz-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `479px` extracted from `moderncraftaz-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4rem` lateral canvas padding with `3rem` grid gap.
- **Border Radius Scale**: `100%`, `50%`, `2px`, `0px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 479px`, `gap: 3rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:479px)`, `@media (max-width:1280px)`, `@media (max-width:991px)`, `@media (max-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4831B0` | `var(--oxynav-brand-color)` in `:root` |
| **Primary Typography Ink** | `#FFFFFF` | `var(--oxynav-neutral-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#EFEDF4` | `var(--oxynav-activehover-color)` in `:root` |
| **Interactive Accent / Highlight** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Secondary / Muted Copy** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Structural Hairline Border** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sk-color` | `currentColor` | Brand / Palette Token |
| `--sk-size` | `100%` | Layout / Spatial Grid Token |
| `--sk-wander-distance` | `calc(var(--sk-size) * 0.75)` | Design System Custom Token |
| `--oxynav-brand-color` | `#4831B0` | Brand / Palette Token |
| `--oxynav-neutral-color` | `#FFFFFF` | Brand / Palette Token |
| `--oxynav-activehover-color` | `#EFEDF4` | Brand / Palette Token |
| `--oxynav-background-color` | `#4831B0` | Canvas / Surface Token |
| `--oxynav-border-radius` | `0px` | Layout / Spatial Grid Token |
| `--oxynav-other-spacing` | `8px` | Layout / Spatial Grid Token |
| `--oxynav-transition-duration` | `0.3s` | Layout / Spatial Grid Token |
| `--oxynav-transition-timing-function` | `cubic-bezier(.84,.05,.31,.93)` | Layout / Spatial Grid Token |
| `--oxynav-animation-name` | `none` | Layout / Spatial Grid Token |
| `--extras-hide-accordion` | `block` | Design System Custom Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `didot-01`.
- **Primary Body Stack**: `didot-02`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `54px`, `48px`, `40px`, `24px`, `64px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `54px`, `48px`, `40px`, `24px`, `64px`).
- **Body Copy**: rule `body` (`font-size: 16px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.455,0.03,0.515,0.955)`, `cubic-bezier(.84,.05,.31,.93)`, `cubic-bezier(.49,.78,.46,1.34)`.

### Per-Element Transition & Choreography Rules
- **Selector `.oxy-preloader`**: `transition: 1s` extracted from `moderncraftaz-com` stylesheet.
- **Selector `-nav-menu .oxy-nav-menu-list li.m...`**: `transition: ease-in-out` extracted from `moderncraftaz-com` stylesheet.
- **Selector `.oxy-nav-menu .menu-item .sub-menu`**: `transition: ease-in-out` extracted from `moderncraftaz-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.455,0.03,0.515,0.955)`)**: Governs interactive state transitions across `<header.yoast-schema-graph>` and `<section.ct-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Select A Location · AllHaus                │
│ ====================================================================== │
│ [ <header.yoast-schema-gra | AZ AZ AZ · CO CO CO · MT MT MT         ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.ct-section>                                 |   │
│ | H1: Unparallelled Service For Exceptional Homes                  |   │
│ | Substrate: #4831B0    | Ink: #FFFFFF    | Accent: #7a00df        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.ct-section>      ) max-w: 479px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Code Snippet ma-customfonts  |  | moderncraftaz-com Interactiv | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3rem  ) | │
│ | [<header.yoast-sche] -> [<section.ct-sectio] -> [<section.ct-sectio] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page>         ) | https://moderncraftaz.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.yoast-schema-graph> — `moderncraftaz-com`)**:
   - Landmark `<header class="yoast-schema-graph">` hosting `Select A Location · AllHaus` navigation (`AZ AZ AZ · CO CO CO · MT MT MT`), DOM attributes (`data-again="always_show"`, `data-wait="load"`, `data-wait-sec="2"`, `data-nosnippet`), and stylesheet rule `section-2-27 > .ct-section-inner-... { max-width:100%;padding-top:0;padding-right:0;padding-bottom:0;padding-le... }`.
2. **Hero Stage & Focal Lead (<section.ct-section> — `Unparallelled Service For Exceptio`)**:
   - Landmark `<section class="ct-section">` presenting display lead `Unparallelled Service For Exceptional Homes` and copy excerpt *"Code Snippet ma-customfonts 3.4.2"* over `#4831B0` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.ct-section> — `Code Snippet ma-customfonts 3.4.2`)**:
   - Landmark `<section class="ct-section">` rendering section `Code Snippet ma-customfonts 3.4.2` with copy *"Unparallelled Service For Exceptional Homes"*, asset references (`recaptcha__en.js`, `cdn.jsdelivr.net`, `embed`, `ma-customfonts.css`), and grid rule `section-2-27 { background-image:linear-gradient(180deg,rgba(77,37,93,0.5),rgba(77,37,93... }`.
4. **Interactive Detail & Feature Matrix (<section.ct-section> — `moderncraftaz-com Interactive Matr`)**:
   - Landmark `<section class="ct-section">` framing `moderncraftaz-com Interactive Matrix` and `moderncraftaz-com Archive & Directory` (*"Code Snippet ma-customfonts 3.4.2"*) with `#EFEDF4` surface cards, `#7a00df` accents, and `div_block-5-27 { width:100%;flex-direction:row;display:flex;align-items:center;justify-co... }`.
5. **Colophon & Global Directory Footer (<footer.page> — `https://moderncraftaz.com/`)**:
   - Landmark `<footer class="page">` anchoring `Select A Location · AllHaus` footer links (`AZ AZ AZ · CO CO CO · MT MT MT`), copy *"moderncraftaz-com Interactive Matrix"*, and `#007cba` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: moderncraftaz-com (Select A Location · AllHaus)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `moderncraftaz-com` (**Select A Location · AllHaus** — `https://moderncraftaz.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#4831B0` canvas, `#FFFFFF` ink, `#7a00df` accent).
- **Identity & Domain Context**: Crafting exceptional residences with unmatched service in Arizona, Montana, and beyond.
- **Primary Substrate**: `#4831B0` (`var(--oxynav-brand-color)` in `:root`), **Primary Ink**: `#FFFFFF`, **Accent / Highlight**: `#7a00df`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#4831B0` (`var(--oxynav-brand-color)` in `:root`) paired with `#FFFFFF` primary typography and `#7a00df` accents.
  - **Extracted Typographic Hierarchy**: Pairs `didot-01` for display copy (`Unparallelled Service For Exceptiona`) with `didot-02` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `479px` container bounds (`gap: 3rem`, padding `4rem`) with `cubic-bezier(0.455,0.03,0.515,0.955)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `moderncraftaz-com` in your global stylesheet:

:root {
  /* Select A Location · AllHaus (moderncraftaz-com) — Ground-Truth Extracted CSS Variables */
  --sk-color: currentColor; /* Brand / Palette Token (moderncraftaz-com) */
  --sk-size: 100%; /* Layout / Spatial Grid Token (moderncraftaz-com) */
  --sk-wander-distance: calc(var(--sk-size) * 0.75); /* Design System Custom Token (moderncraftaz-com) */
  --oxynav-brand-color: #4831B0; /* Brand / Palette Token (moderncraftaz-com) */
  --oxynav-neutral-color: #FFFFFF; /* Brand / Palette Token (moderncraftaz-com) */
  --oxynav-activehover-color: #EFEDF4; /* Brand / Palette Token (moderncraftaz-com) */
  --oxynav-background-color: #4831B0; /* Canvas / Surface Token (moderncraftaz-com) */
  --oxynav-border-radius: 0px; /* Layout / Spatial Grid Token (moderncraftaz-com) */
  --oxynav-other-spacing: 8px; /* Layout / Spatial Grid Token (moderncraftaz-com) */
  --oxynav-transition-duration: 0.3s; /* Layout / Spatial Grid Token (moderncraftaz-com) */
  --oxynav-transition-timing-function: cubic-bezier(.84,.05,.31,.93); /* Layout / Spatial Grid Token (moderncraftaz-com) */
  --oxynav-animation-name: none; /* Layout / Spatial Grid Token (moderncraftaz-com) */
  --extras-hide-accordion: block; /* Design System Custom Token (moderncraftaz-com) */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (moderncraftaz-com) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (moderncraftaz-com) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (moderncraftaz-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#4831B0` — grounded in `var(--oxynav-brand-color)` in `:root`
- **Primary Typography Ink**: `#FFFFFF` — grounded in `var(--oxynav-neutral-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#EFEDF4` — grounded in `var(--oxynav-activehover-color)` in `:root`
- **Interactive Accent / Highlight**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Secondary / Muted Copy**: `#ddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Structural Hairline Border**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `479px` extracted from `moderncraftaz-com` stylesheet
- **Padding & Gutters**: `4rem` lateral canvas padding with `3rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 479px`, `gap: 3rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4rem` horizontal padding
- **Media Queries**: `@media (max-width:479px)`, `@media (max-width:1280px)`, `@media (max-width:991px)`, `@media (max-width:767px)`
- **Corner Radii**: `100%`, `50%`, `2px`, `0px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `didot-01`
- **Body Font Stack**: `didot-02`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `54px`, `48px`, `40px`, `24px`, `64px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `54px`, `48px`, `40px`, `24px`, `64px`)
- **Body Copy Rule**: rule `body` (`font-size: 16px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `moderncraftaz-com` (`Select A Location · AllHaus`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.yoast-schema-graph> — `moderncraftaz-com`)**:
   - DOM & Selectors: Landmark `<header class="yoast-schema-graph">` hosting `Select A Location · AllHaus` navigation (`AZ AZ AZ · CO CO CO · MT MT MT`), DOM attributes (`data-again="always_show"`, `data-wait="load"`, `data-wait-sec="2"`, `data-nosnippet`), and stylesheet rule `section-2-27 > .ct-section-inner-... { max-width:100%;padding-top:0;padding-right:0;padding-bottom:0;padding-le... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.yoast-schema-graph> — `moderncraftaz-com`)` (`moderncraftaz-com`) adapts across `@media (max-width:479px)`, `@media (max-width:1280px)`, `@media (max-width:991px)`, `@media (max-width:767px)` with `cubic-bezier(0.455,0.03,0.515,0.955)`, `cubic-bezier(.84,.05,.31,.93)`, `cubic-bezier(.49,.78,.46,1.34)` transitions and links `AZ AZ AZ · CO CO CO · MT MT MT`.
2. **Hero Stage & Focal Lead (<section.ct-section> — `Unparallelled Service For Exceptio`)**:
   - DOM & Selectors: Landmark `<section class="ct-section">` presenting display lead `Unparallelled Service For Exceptional Homes` and copy excerpt *"Code Snippet ma-customfonts 3.4.2"* over `#4831B0` canvas and `#FFFFFF` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#4831B0` background with `#FFFFFF` headline `Unparallelled Service For Exceptional Homes`.
3. **Primary Showcase & Content Grid (<section.ct-section> — `Code Snippet ma-customfonts 3.4.2`)**:
   - DOM & Selectors: Landmark `<section class="ct-section">` rendering section `Code Snippet ma-customfonts 3.4.2` with copy *"Unparallelled Service For Exceptional Homes"*, asset references (`recaptcha__en.js`, `cdn.jsdelivr.net`, `embed`, `ma-customfonts.css`), and grid rule `section-2-27 { background-image:linear-gradient(180deg,rgba(77,37,93,0.5),rgba(77,37,93... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.ct-section> — `Code Snippet ma-customfonts 3.4.2`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 479px`, `gap: 3rem`) on desktop and Single-column vertical stack at `390px` viewport width with `4rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.ct-section> — `moderncraftaz-com Interactive Matr`)**:
   - DOM & Selectors: Landmark `<section class="ct-section">` framing `moderncraftaz-com Interactive Matrix` and `moderncraftaz-com Archive & Directory` (*"Code Snippet ma-customfonts 3.4.2"*) with `#EFEDF4` surface cards, `#7a00df` accents, and `div_block-5-27 { width:100%;flex-direction:row;display:flex;align-items:center;justify-co... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.ct-section> — `moderncraftaz-com Interactive Matr`)` uses `100%`, `50%`, `2px`, `0px` radii, `#7a00df` highlights, and assets (recaptcha__en.js, cdn.jsdelivr.net, embed).
5. **Colophon & Global Directory Footer (<footer.page> — `https://moderncraftaz.com/`)**:
   - DOM & Selectors: Landmark `<footer class="page">` anchoring `Select A Location · AllHaus` footer links (`AZ AZ AZ · CO CO CO · MT MT MT`), copy *"moderncraftaz-com Interactive Matrix"*, and `#007cba` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.page> — `https://moderncraftaz.com/`)` aligns to `479px` extracted from `moderncraftaz-com` stylesheet with `4rem` lateral canvas padding with `3rem` grid gap and attributes (data-again="always_show", data-wait="load", data-wait-sec="2").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Code Snippet ma-customfonts 3.4.2"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.455,0.03,0.515,0.955)`, `cubic-bezier(.84,.05,.31,.93)`, `cubic-bezier(.49,.78,.46,1.34)`
- **Extracted Stylesheet Rules (`moderncraftaz-com`)**:
- `section-2-27 > .ct-section-inner-... { max-width:100%;padding-top:0;padding-right:0;padding-bottom:0;padding-le... }`
- `section-2-27 { background-image:linear-gradient(180deg,rgba(77,37,93,0.5),rgba(77,37,93... }`
- `div_block-5-27 { width:100%;flex-direction:row;display:flex;align-items:center;justify-co... }`
- `div_block-6-27 { padding-top:9rem }`
- `div_block-7-27 { text-align:left;flex-direction:row;display:flex;width:100%;align-items:f... }`
- **Per-Selector Transition Rules**:
- **Selector `.oxy-preloader`**: `transition: 1s` extracted from `moderncraftaz-com` stylesheet.
- **Selector `-nav-menu .oxy-nav-menu-list li.m...`**: `transition: ease-in-out` extracted from `moderncraftaz-com` stylesheet.
- **Selector `.oxy-nav-menu .menu-item .sub-menu`**: `transition: ease-in-out` extracted from `moderncraftaz-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.455,0.03,0.515,0.955)`)**: Governs interactive state transitions across `<header.yoast-schema-graph>` and `<section.ct-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `moderncraftaz-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
