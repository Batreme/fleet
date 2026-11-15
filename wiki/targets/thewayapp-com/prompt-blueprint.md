---
title: "UI Prompt Blueprint: thewayapp-com"
date: 2026-11-15
target: "[[overview|thewayapp-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#e8f2f0` / `#e6f2f0`)"
---

# UI Design System & Master Generation Blueprint: thewayapp-com

> **The Way App - Meditation that lasts a lifetime — The Way** (https://thewayapp.com) — A long-term path of deep meditation training, guided by Zen Master Henry Shukman

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/thewayapp-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Way App - Meditation that lasts a lifetime — The Way** (`https://thewayapp.com`). A long-term path of deep meditation training, guided by Zen Master Henry Shukman
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#e8f2f0` / `#e6f2f0`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e8f2f0` (`var(--color-evergreen-light)` in `:root`) paired with `#122e28` primary typography and `#e6f2f0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `nunito` for display copy (`The end of your search. The start of`) with `nunito Fallback` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--width-content)` container bounds (`gap: 1.25rem`, padding `var(--space-32)`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/thewayapp-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--width-content)` extracted from `thewayapp-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--space-32)` lateral canvas padding with `1.25rem` grid gap.
- **Border Radius Scale**: `var(--radius-sm)`, `10px`, `24px`, `18px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--width-content)`, `gap: 1.25rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-32)` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:768px)`, `@media screen and (min-width:769px)`, `@media screen and (min-width:670px)and (max-width:850px)`, `@media screen and (min-width:769px)and (max-width:850px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e8f2f0` | `var(--color-evergreen-light)` in `:root` |
| **Primary Typography Ink** | `#1c5349` | `var(--color-evergreen-default)` in `:root` |
| **Elevated Surface / Card Substrate** | `#122e28` | `var(--color-evergreen-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#e6f2f0` | `var(--color-deepsea-light)` in `:root` |
| **Secondary / Muted Copy** | `#267768` | `var(--color-deepsea-default)` in `:root` |
| **Structural Hairline Border** | `#1a5249` | `var(--color-deepsea-dark)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--max-width-module-variation-content-wrapper` | `1320px!important` | Layout / Spatial Grid Token |
| `--width-module-variation-content-wrapper` | `91.6667vw!important` | Layout / Spatial Grid Token |
| `--font-sans` | `"nunito","nunito Fallback"` | Typography / Scale Token |
| `--_press-x` | `1` | Design System Custom Token |
| `--_press-y` | `0.3` | Design System Custom Token |
| `--_press-deg` | `0.5deg` | Design System Custom Token |
| `--media-width-cap` | `90vw` | Layout / Spatial Grid Token |
| `--media-height` | `min(calc(var(--media-width-cap) * 9 / 16),80vh)` | Layout / Spatial Grid Token |
| `--_card-radius` | `10px 8px 16px 17px/18px 17px 11px 15px` | Elevation / Border Token |
| `--logo-height-mobile` | `2.5rem` | Layout / Spatial Grid Token |
| `--blob-media-bleed` | `1.25` | Design System Custom Token |
| `--hero-height` | `clamp(480px,70vh,760px)` | Layout / Spatial Grid Token |
| `--hero-media-basis` | `min(var(--hero-height),50vw)` | Dimension / Scale Token |
| `--blob-corner-scale` | `1.2` | Design System Custom Token |
| `--parallax-y` | `0px` | Dimension / Scale Token |
| `--blob-shoulder` | `0.85` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `nunito`.
- **Primary Body Stack**: `nunito Fallback`.
- **Technical / Metadata Stack**: `SF Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80px`, `10px`, `12px`, `14px`, `18px`).
- **Section Heading (`H2`)**: CSS variables `--color-subtitle: var(--color-evergreen-default)`, `--color-card-subtitle: var(--color-obsidian-dark)`.
- **Body Copy**: CSS variables `--color-body-text: var(--color-evergreen-default)`; rule `p` (`line-height: 1.2`).
- **Metadata & Navigation Labels**: CSS variables `--color-caption: var(--color-evergreen-default)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.898,0,.669,1)`, `cubic-bezier(.5,0,.5,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.Default_youtubePlayButton__ETkvO`**: `transition: opacity .2s` extracted from `thewayapp-com` stylesheet.
- **Selector `.NavGroup_link__0kay2`**: `transition: color .2s var(--easeOutQuad,ease)` extracted from `thewayapp-com` stylesheet.
- **Selector `.NavigationOverlay_socialLink__az...`**: `transition: background-color .25s var(--easeOutQuad,ease)` extracted from `thewayapp-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.Header_header__gtmFw>` and `<article.StaticNarrative_root__V_9OR>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Way App - Meditation that lasts a life │
│ ====================================================================== │
│ [ <header.Header_header__g | Skip to content                        ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.StaticNarrative_root__V_9OR>                |   │
│ | H1: The end of your search. The start of your journey.           |   │
│ | Substrate: #e8f2f0    | Ink: #122e28    | Accent: #e6f2f0        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.StaticNarrative_r) max-w: var(--width-co |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | One way forward              |  | Meet your teacher: Henry Shu | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1.25re) | │
│ | [<header.Header_hea] -> [<article.StaticNar] -> [<article.StaticNar] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.type-ui-micro>) | https://thewayapp.com              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.Header_header__gtmFw> — `thewayapp-com`)**:
   - Landmark `<header class="Header_header__gtmFw theme-light">` hosting `The Way App - Meditation that lasts ` navigation (`Skip to content`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.Default_embedWrapper__PB5mt { width:100% }`.
2. **Hero Stage & Focal Lead (<article.StaticNarrative_root__V_9OR> — `The end of your search. The start `)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` presenting display lead `The end of your search. The start of your journey.` and copy excerpt *"The end of your search."* over `#e8f2f0` canvas and `#122e28` ink.
3. **Primary Showcase & Content Grid (<article.StaticNarrative_root__V_9OR> — `One way forward`)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` rendering section `One way forward` with copy *"The start of your journey."*, asset references (`75aacf3429424351-s.p.woff2`, `df8e05a132a73a9c-s.p.woff2`, `95817d087ee99a00.css`, `6fc6cebf31cdec86.css`), and grid rule `.Default_embedWrapper__PB5mt iframe { width:100%!important;aspect-ratio:16/9;height:auto!important;display:block }`.
4. **Interactive Detail & Feature Matrix (<article.StaticNarrative_root__V_9OR> — `Meet your teacher: Henry Shukman`)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` framing `Meet your teacher: Henry Shukman` and `A path that deepens with every step` (*"Most meditation apps give you countless options. The Way offers o"*) with `#122e28` surface cards, `#e6f2f0` accents, and `.Default_embedHeading__mSaeS { -webkit-margin-start:0;margin-inline-start:0;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.type-ui-micro> — `https://thewayapp.com`)**:
   - Landmark `<footer class="type-ui-micro StaticNarrative_attribution__25nmb">` anchoring `The Way App - Meditation that la` footer links (`Skip to content`), copy *"I've finally been able to commit to daily meditation after y"*, and `#1a5249` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thewayapp-com (The Way App - Meditation that lasts a lifetime — The Way)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thewayapp-com` (**The Way App - Meditation that lasts a lifetime — The Way** — `https://thewayapp.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e8f2f0` / `#e6f2f0`).
- **Identity & Domain Context**: A long-term path of deep meditation training, guided by Zen Master Henry Shukman
- **Primary Substrate**: `#e8f2f0` (`var(--color-evergreen-light)` in `:root`), **Primary Ink**: `#122e28`, **Accent / Highlight**: `#e6f2f0`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e8f2f0` (`var(--color-evergreen-light)` in `:root`) paired with `#122e28` primary typography and `#e6f2f0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `nunito` for display copy (`The end of your search. The start of`) with `nunito Fallback` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--width-content)` container bounds (`gap: 1.25rem`, padding `var(--space-32)`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thewayapp-com` in your global stylesheet:

:root {
  /* The Way App - Meditation that lasts a lifetime — The Way (thewayapp-com) — Ground-Truth Extracted CSS Variables */
  --max-width-module-variation-content-wrapper: 1320px!important; /* Layout / Spatial Grid Token (thewayapp-com) */
  --width-module-variation-content-wrapper: 91.6667vw!important; /* Layout / Spatial Grid Token (thewayapp-com) */
  --font-sans: "nunito","nunito Fallback"; /* Typography / Scale Token (thewayapp-com) */
  --_press-x: 1; /* Design System Custom Token (thewayapp-com) */
  --_press-y: 0.3; /* Design System Custom Token (thewayapp-com) */
  --_press-deg: 0.5deg; /* Design System Custom Token (thewayapp-com) */
  --media-width-cap: 90vw; /* Layout / Spatial Grid Token (thewayapp-com) */
  --media-height: min(calc(var(--media-width-cap) * 9 / 16),80vh); /* Layout / Spatial Grid Token (thewayapp-com) */
  --_card-radius: 10px 8px 16px 17px/18px 17px 11px 15px; /* Elevation / Border Token (thewayapp-com) */
  --logo-height-mobile: 2.5rem; /* Layout / Spatial Grid Token (thewayapp-com) */
  --blob-media-bleed: 1.25; /* Design System Custom Token (thewayapp-com) */
  --hero-height: clamp(480px,70vh,760px); /* Layout / Spatial Grid Token (thewayapp-com) */
  --hero-media-basis: min(var(--hero-height),50vw); /* Dimension / Scale Token (thewayapp-com) */
  --blob-corner-scale: 1.2; /* Design System Custom Token (thewayapp-com) */
  --parallax-y: 0px; /* Dimension / Scale Token (thewayapp-com) */
  --blob-shoulder: 0.85; /* Design System Custom Token (thewayapp-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e8f2f0` — grounded in `var(--color-evergreen-light)` in `:root`
- **Primary Typography Ink**: `#1c5349` — grounded in `var(--color-evergreen-default)` in `:root`
- **Elevated Surface / Card Substrate**: `#122e28` — grounded in `var(--color-evergreen-dark)` in `:root`
- **Interactive Accent / Highlight**: `#e6f2f0` — grounded in `var(--color-deepsea-light)` in `:root`
- **Secondary / Muted Copy**: `#267768` — grounded in `var(--color-deepsea-default)` in `:root`
- **Structural Hairline Border**: `#1a5249` — grounded in `var(--color-deepsea-dark)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--width-content)` extracted from `thewayapp-com` stylesheet
- **Padding & Gutters**: `var(--space-32)` lateral canvas padding with `1.25rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--width-content)`, `gap: 1.25rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-32)` horizontal padding
- **Media Queries**: `@media screen and (max-width:768px)`, `@media screen and (min-width:769px)`, `@media screen and (min-width:670px)and (max-width:850px)`, `@media screen and (min-width:769px)and (max-width:850px)`
- **Corner Radii**: `var(--radius-sm)`, `10px`, `24px`, `18px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `nunito`
- **Body Font Stack**: `nunito Fallback`
- **Monospace / Technical Font Stack**: `SF Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80px`, `10px`, `12px`, `14px`, `18px`)
- **H2 Section Rule**: CSS variables `--color-subtitle: var(--color-evergreen-default)`, `--color-card-subtitle: var(--color-obsidian-dark)`
- **Body Copy Rule**: CSS variables `--color-body-text: var(--color-evergreen-default)`; rule `p` (`line-height: 1.2`)
- **Metadata & Index Rule**: CSS variables `--color-caption: var(--color-evergreen-default)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thewayapp-com` (`The Way App - Meditation that lasts a lifetime — The Way`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.Header_header__gtmFw> — `thewayapp-com`)**:
   - DOM & Selectors: Landmark `<header class="Header_header__gtmFw theme-light">` hosting `The Way App - Meditation that lasts ` navigation (`Skip to content`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.Default_embedWrapper__PB5mt { width:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.Header_header__gtmFw> — `thewayapp-com`)` (`thewayapp-com`) adapts across `@media screen and (max-width:768px)`, `@media screen and (min-width:769px)`, `@media screen and (min-width:670px)and (max-width:850px)`, `@media screen and (min-width:769px)and (max-width:850px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.898,0,.669,1)`, `cubic-bezier(.5,0,.5,1)` transitions and links `Skip to content`.
2. **Hero Stage & Focal Lead (<article.StaticNarrative_root__V_9OR> — `The end of your search. The start `)**:
   - DOM & Selectors: Landmark `<article class="StaticNarrative_root__V_9OR">` presenting display lead `The end of your search. The start of your journey.` and copy excerpt *"The end of your search."* over `#e8f2f0` canvas and `#122e28` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#e8f2f0` background with `#122e28` headline `The end of your search. The start of your journey.`.
3. **Primary Showcase & Content Grid (<article.StaticNarrative_root__V_9OR> — `One way forward`)**:
   - DOM & Selectors: Landmark `<article class="StaticNarrative_root__V_9OR">` rendering section `One way forward` with copy *"The start of your journey."*, asset references (`75aacf3429424351-s.p.woff2`, `df8e05a132a73a9c-s.p.woff2`, `95817d087ee99a00.css`, `6fc6cebf31cdec86.css`), and grid rule `.Default_embedWrapper__PB5mt iframe { width:100%!important;aspect-ratio:16/9;height:auto!important;display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.StaticNarrative_root__V_9OR> — `One way forward`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--width-content)`, `gap: 1.25rem`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-32)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.StaticNarrative_root__V_9OR> — `Meet your teacher: Henry Shukman`)**:
   - DOM & Selectors: Landmark `<article class="StaticNarrative_root__V_9OR">` framing `Meet your teacher: Henry Shukman` and `A path that deepens with every step` (*"Most meditation apps give you countless options. The Way offers o"*) with `#122e28` surface cards, `#e6f2f0` accents, and `.Default_embedHeading__mSaeS { -webkit-margin-start:0;margin-inline-start:0;max-width:100% }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.StaticNarrative_root__V_9OR> — `Meet your teacher: Henry Shukman`)` uses `var(--radius-sm)`, `10px`, `24px`, `18px` radii, `#e6f2f0` highlights, and assets (75aacf3429424351-s.p.woff2, df8e05a132a73a9c-s.p.woff2, 95817d087ee99a00.css).
5. **Colophon & Global Directory Footer (<footer.type-ui-micro> — `https://thewayapp.com`)**:
   - DOM & Selectors: Landmark `<footer class="type-ui-micro StaticNarrative_attribution__25nmb">` anchoring `The Way App - Meditation that la` footer links (`Skip to content`), copy *"I've finally been able to commit to daily meditation after y"*, and `#1a5249` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.type-ui-micro> — `https://thewayapp.com`)` aligns to `var(--width-content)` extracted from `thewayapp-com` stylesheet with `var(--space-32)` lateral canvas padding with `1.25rem` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The end of your search."*
- Copy Excerpt 2: *"The start of your journey."*
- Copy Excerpt 3: *"Most meditation apps give you countless options. The Way offers one single path. N..."*
- Copy Excerpt 4: *"I've finally been able to commit to daily meditation after years of trying. Life c..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.898,0,.669,1)`, `cubic-bezier(.5,0,.5,1)`
- **Extracted Stylesheet Rules (`thewayapp-com`)**:
- `.Default_embedWrapper__PB5mt { width:100% }`
- `.Default_embedWrapper__PB5mt iframe { width:100%!important;aspect-ratio:16/9;height:auto!important;display:block }`
- `.Default_embedHeading__mSaeS { -webkit-margin-start:0;margin-inline-start:0;max-width:100% }`
- `.Default_embedRoot__Jw9C0 { padding-inline:var(--space-32) }`
- `.Default_youtubeFacade__WwJms { position:relative;display:block;width:100%;aspect-ratio:16/9;padding:0;b... }`
- **Per-Selector Transition Rules**:
- **Selector `.Default_youtubePlayButton__ETkvO`**: `transition: opacity .2s` extracted from `thewayapp-com` stylesheet.
- **Selector `.NavGroup_link__0kay2`**: `transition: color .2s var(--easeOutQuad,ease)` extracted from `thewayapp-com` stylesheet.
- **Selector `.NavigationOverlay_socialLink__az...`**: `transition: background-color .25s var(--easeOutQuad,ease)` extracted from `thewayapp-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.Header_header__gtmFw>` and `<article.StaticNarrative_root__V_9OR>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thewayapp-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
