---
title: "UI Prompt Blueprint: overworldaudio-com"
date: 2026-11-15
target: "[[overview|overworldaudio-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#e9ecee` / `#6e8799`)"
---

# UI Design System & Master Generation Blueprint: overworldaudio-com

> **Overworld Audio** (https://overworldaudio.com/) — Audio co-development for games and interactive experiences, from prototype to final mix.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/overworldaudio-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Overworld Audio** (`https://overworldaudio.com/`). Audio co-development for games and interactive experiences, from prototype to final mix.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#e9ecee` / `#6e8799`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e9ecee` (`var(--off-white)` in `:root`) paired with `#13151f` primary typography and `#6e8799` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IvarHeadline` for display copy (`Building unforgettable sonic experie`) with `PPFrama` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `768px` container bounds (`gap: .75rem`, padding `.875rem`) with `cubic-bezier(.14,1,.34,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/overworldaudio-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `768px` extracted from `overworldaudio-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.875rem` lateral canvas padding with `.75rem` grid gap.
- **Border Radius Scale**: `.21875rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: .75rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.875rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:768px)`, `@media (max-width:1000px)`, `@media (max-width:400px)`, `@media (min-width:1530px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e9ecee` | `var(--off-white)` in `:root` |
| **Primary Typography Ink** | `#13151f` | `var(--off-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#aab9c7` | `var(--color-secondary)` in `:root` |
| **Interactive Accent / Highlight** | `#6e8799` | `var(--gray)` in `:root` |
| **Secondary / Muted Copy** | `#4c5e6b` | `var(--dark-gray)` in `:root` |
| **Structural Hairline Border** | `#1a1a1a` | `var(--surface)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--nav-align-col` | `6` | Layout / Spatial Grid Token |
| `--off-white` | `#e9ecee` | Canvas / Surface Token |
| `--off-black` | `#13151f` | Canvas / Surface Token |
| `--color-secondary` | `#aab9c7` | Brand / Palette Token |
| `--gray` | `#6e8799` | Color / Atmospheric Token |
| `--dark-gray` | `#4c5e6b` | Canvas / Surface Token |
| `--expo-out` | `cubic-bezier(.14,1,.34,1)` | Motion / Timing Token |
| `--quint-out` | `cubic-bezier(.23,1,.32,1)` | Motion / Timing Token |
| `--z-sound-toggle` | `100` | Elevation / Border Token |
| `--chrome-bottom` | `2.6rem` | Dimension / Scale Token |
| `--gl-bleed` | `0px` | Dimension / Scale Token |
| `--border` | `hsla(0,0%,91%,.1)` | Elevation / Border Token |
| `--surface` | `#1a1a1a` | Canvas / Surface Token |
| `--grid-cols` | `12` | Layout / Spatial Grid Token |
| `--grid-gutter` | `1rem` | Layout / Spatial Grid Token |
| `--grid-max-width` | `calc(100% - 4.9rem)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `IvarHeadline`.
- **Primary Body Stack**: `PPFrama`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.h1` (`font-size: 2.375rem`).
- **Section Heading (`H2`)**: rule `,.h2` (`line-height: .95`, `font-weight: 500`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.5625rem`, `.75rem`, `1.875rem`, `16px`, `clamp(16px,1.11111vw,20px)`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.5625rem`, `.75rem`, `1.875rem`, `16px`, `clamp(16px,1.11111vw,20px)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.14,1,.34,1)`, `cubic-bezier(.23,1,.32,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.fade[data-v-3f1fbcc8]`**: `transition: opacity var(--fade-duration) linear var(--fade-delay),visibili...` extracted from `overworldaudio-com` stylesheet.
- **Selector `.btn-link[data-v-05faef33]`**: `transition: color .3s ease` extracted from `overworldaudio-com` stylesheet.
- **Selector `media(hover:hover)`**: `transition: transform .8s var(--expo-out),opacity .8s var(--expo-out)` extracted from `overworldaudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.14,1,.34,1)`)**: Governs interactive state transitions across `<nav.nav-bar>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Overworld Audio                            │
│ ====================================================================== │
│ [ <nav.nav-bar>            | Projects Projects · Studio Studio · Co ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Building unforgettable sonic experiences                     |   │
│ | Substrate: #e9ecee    | Ink: #13151f    | Accent: #6e8799        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero>            ) max-w: 768px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Enter with sound Enter with  |  | Enter without sound          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .75rem) | │
│ | [<nav.nav-bar>] -> [<section.hero>] -> [<section.hero>] |            │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.is-visible>   ) | https://overworldaudio.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.nav-bar> — `overworldaudio-com`)**:
   - Landmark `<nav class="nav-bar">` hosting `Overworld Audio` navigation (`Projects Projects · Studio Studio · Contact Contact`), DOM attributes (`data-v-a6ea98c7`, `data-v-3f1fbcc8`, `data-v-71a6f60d`, `data-v-05faef33`), and stylesheet rule `hover { color:var(--off-black) }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building unforgettable sonic exper`)**:
   - Landmark `<section class="hero">` presenting display lead `Building unforgettable sonic experiences` and copy excerpt *"Enter with sound Enter with sound"* over `#e9ecee` canvas and `#13151f` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Enter with sound Enter with sound`)**:
   - Landmark `<section class="hero">` rendering section `Enter with sound Enter with sound` with copy *"Enter without sound"*, asset references (`entry.B6zjpOmH.css`, `CmsText.BXNuEsZZ.css`, `IvarHeadline-Regular.woff2`, `PPFrama-Regular.woff2`), and grid rule `last-child { left:0;opacity:0;position:absolute;top:0;transform:translateY(120%);widt... }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Enter without sound`)**:
   - Landmark `<section class="hero">` framing `Enter without sound` and `Drag or scroll to navigate. Click markers to exp` (*"Drag or scroll to navigate. Click markers to explore. Drag to nav"*) with `#aab9c7` surface cards, `#6e8799` accents, and `first-child { opacity:0;transform:translateY(-120%) }`.
5. **Colophon & Global Directory Footer (<footer.is-visible> — `https://overworldaudio.com/`)**:
   - Landmark `<footer class="is-visible">` anchoring `Overworld Audio` footer links (`Projects Projects · Studio Studio · Contact Contact`), copy *"Drag or scroll to navigate. Click markers to explore."*, and `#1a1a1a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: overworldaudio-com (Overworld Audio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `overworldaudio-com` (**Overworld Audio** — `https://overworldaudio.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e9ecee` / `#6e8799`).
- **Identity & Domain Context**: Audio co-development for games and interactive experiences, from prototype to final mix.
- **Primary Substrate**: `#e9ecee` (`var(--off-white)` in `:root`), **Primary Ink**: `#13151f`, **Accent / Highlight**: `#6e8799`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e9ecee` (`var(--off-white)` in `:root`) paired with `#13151f` primary typography and `#6e8799` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IvarHeadline` for display copy (`Building unforgettable sonic experie`) with `PPFrama` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `768px` container bounds (`gap: .75rem`, padding `.875rem`) with `cubic-bezier(.14,1,.34,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `overworldaudio-com` in your global stylesheet:

:root {
  /* Overworld Audio (overworldaudio-com) — Ground-Truth Extracted CSS Variables */
  --nav-align-col: 6; /* Layout / Spatial Grid Token (overworldaudio-com) */
  --off-white: #e9ecee; /* Canvas / Surface Token (overworldaudio-com) */
  --off-black: #13151f; /* Canvas / Surface Token (overworldaudio-com) */
  --color-secondary: #aab9c7; /* Brand / Palette Token (overworldaudio-com) */
  --gray: #6e8799; /* Color / Atmospheric Token (overworldaudio-com) */
  --dark-gray: #4c5e6b; /* Canvas / Surface Token (overworldaudio-com) */
  --expo-out: cubic-bezier(.14,1,.34,1); /* Motion / Timing Token (overworldaudio-com) */
  --quint-out: cubic-bezier(.23,1,.32,1); /* Motion / Timing Token (overworldaudio-com) */
  --z-sound-toggle: 100; /* Elevation / Border Token (overworldaudio-com) */
  --chrome-bottom: 2.6rem; /* Dimension / Scale Token (overworldaudio-com) */
  --gl-bleed: 0px; /* Dimension / Scale Token (overworldaudio-com) */
  --border: hsla(0,0%,91%,.1); /* Elevation / Border Token (overworldaudio-com) */
  --surface: #1a1a1a; /* Canvas / Surface Token (overworldaudio-com) */
  --grid-cols: 12; /* Layout / Spatial Grid Token (overworldaudio-com) */
  --grid-gutter: 1rem; /* Layout / Spatial Grid Token (overworldaudio-com) */
  --grid-max-width: calc(100% - 4.9rem); /* Layout / Spatial Grid Token (overworldaudio-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e9ecee` — grounded in `var(--off-white)` in `:root`
- **Primary Typography Ink**: `#13151f` — grounded in `var(--off-black)` in `:root`
- **Elevated Surface / Card Substrate**: `#aab9c7` — grounded in `var(--color-secondary)` in `:root`
- **Interactive Accent / Highlight**: `#6e8799` — grounded in `var(--gray)` in `:root`
- **Secondary / Muted Copy**: `#4c5e6b` — grounded in `var(--dark-gray)` in `:root`
- **Structural Hairline Border**: `#1a1a1a` — grounded in `var(--surface)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `768px` extracted from `overworldaudio-com` stylesheet
- **Padding & Gutters**: `.875rem` lateral canvas padding with `.75rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: .75rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.875rem` horizontal padding
- **Media Queries**: `@media (max-width:768px)`, `@media (max-width:1000px)`, `@media (max-width:400px)`, `@media (min-width:1530px)`
- **Corner Radii**: `.21875rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `IvarHeadline`
- **Body Font Stack**: `PPFrama`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `.h1` (`font-size: 2.375rem`)
- **H2 Section Rule**: rule `,.h2` (`line-height: .95`, `font-weight: 500`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.5625rem`, `.75rem`, `1.875rem`, `16px`, `clamp(16px,1.11111vw,20px)`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.5625rem`, `.75rem`, `1.875rem`, `16px`, `clamp(16px,1.11111vw,20px)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `overworldaudio-com` (`Overworld Audio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.nav-bar> — `overworldaudio-com`)**:
   - DOM & Selectors: Landmark `<nav class="nav-bar">` hosting `Overworld Audio` navigation (`Projects Projects · Studio Studio · Contact Contact`), DOM attributes (`data-v-a6ea98c7`, `data-v-3f1fbcc8`, `data-v-71a6f60d`, `data-v-05faef33`), and stylesheet rule `hover { color:var(--off-black) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.nav-bar> — `overworldaudio-com`)` (`overworldaudio-com`) adapts across `@media (max-width:768px)`, `@media (max-width:1000px)`, `@media (max-width:400px)`, `@media (min-width:1530px)` with `cubic-bezier(.14,1,.34,1)`, `cubic-bezier(.23,1,.32,1)` transitions and links `Projects Projects · Studio Studio · Contact Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building unforgettable sonic exper`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Building unforgettable sonic experiences` and copy excerpt *"Enter with sound Enter with sound"* over `#e9ecee` canvas and `#13151f` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#e9ecee` background with `#13151f` headline `Building unforgettable sonic experiences`.
3. **Primary Showcase & Content Grid (<section.hero> — `Enter with sound Enter with sound`)**:
   - DOM & Selectors: Landmark `<section class="hero">` rendering section `Enter with sound Enter with sound` with copy *"Enter without sound"*, asset references (`entry.B6zjpOmH.css`, `CmsText.BXNuEsZZ.css`, `IvarHeadline-Regular.woff2`, `PPFrama-Regular.woff2`), and grid rule `last-child { left:0;opacity:0;position:absolute;top:0;transform:translateY(120%);widt... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero> — `Enter with sound Enter with sound`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: .75rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.875rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Enter without sound`)**:
   - DOM & Selectors: Landmark `<section class="hero">` framing `Enter without sound` and `Drag or scroll to navigate. Click markers to exp` (*"Drag or scroll to navigate. Click markers to explore. Drag to nav"*) with `#aab9c7` surface cards, `#6e8799` accents, and `first-child { opacity:0;transform:translateY(-120%) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero> — `Enter without sound`)` uses `.21875rem` radii, `#6e8799` highlights, and assets (entry.B6zjpOmH.css, CmsText.BXNuEsZZ.css, IvarHeadline-Regular.woff2).
5. **Colophon & Global Directory Footer (<footer.is-visible> — `https://overworldaudio.com/`)**:
   - DOM & Selectors: Landmark `<footer class="is-visible">` anchoring `Overworld Audio` footer links (`Projects Projects · Studio Studio · Contact Contact`), copy *"Drag or scroll to navigate. Click markers to explore."*, and `#1a1a1a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.is-visible> — `https://overworldaudio.com/`)` aligns to `768px` extracted from `overworldaudio-com` stylesheet with `.875rem` lateral canvas padding with `.75rem` grid gap and attributes (data-v-a6ea98c7, data-v-3f1fbcc8, data-v-71a6f60d).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Enter with sound Enter with sound"*
- Copy Excerpt 2: *"Enter without sound"*
- Copy Excerpt 3: *"Drag or scroll to navigate. Click markers to explore. Drag to navigate. Tap marker..."*
- Copy Excerpt 4: *"Drag or scroll to navigate. Click markers to explore."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.14,1,.34,1)`, `cubic-bezier(.23,1,.32,1)`
- **Extracted Stylesheet Rules (`overworldaudio-com`)**:
- `hover { color:var(--off-black) }`
- `last-child { left:0;opacity:0;position:absolute;top:0;transform:translateY(120%);widt... }`
- `first-child { opacity:0;transform:translateY(-120%) }`
- `.text-link__underline { opacity:.75 }`
- `before { background:url(../textures/grain-bg.webp) repeat 0 0/300px 300px;content... }`
- **Per-Selector Transition Rules**:
- **Selector `.fade[data-v-3f1fbcc8]`**: `transition: opacity var(--fade-duration) linear var(--fade-delay),visibili...` extracted from `overworldaudio-com` stylesheet.
- **Selector `.btn-link[data-v-05faef33]`**: `transition: color .3s ease` extracted from `overworldaudio-com` stylesheet.
- **Selector `media(hover:hover)`**: `transition: transform .8s var(--expo-out),opacity .8s var(--expo-out)` extracted from `overworldaudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.14,1,.34,1)`)**: Governs interactive state transitions across `<nav.nav-bar>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `overworldaudio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
