---
title: "UI Prompt Blueprint: kelvin-8b-com"
date: 2026-11-15
target: "[[overview|kelvin-8b-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#f1ede4` canvas, `#110d19` ink, `#2a5cff` accent)"
---

# UI Design System & Master Generation Blueprint: kelvin-8b-com

> **Kelvin — three nights of music, filmed in heat** (https://kelvin.8b.com/) — Kelvin is a three-night music festival filmed through thermal cameras and projected back into a former power station in Rotterdam. 23–25...

![Desktop Viewport Capture (1440x17000)](file:///root/projects/fleet/wiki/targets/kelvin-8b-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Kelvin — three nights of music, filmed in heat** (`https://kelvin.8b.com/`). Kelvin is a three-night music festival filmed through thermal cameras and projected back into a former power station in Rotterdam. 23–25...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f1ede4` canvas, `#110d19` ink, `#2a5cff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1ede4` (`var(--color-1)` in `:root`) paired with `#110d19` primary typography and `#2a5cff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Hubot Sans` for display copy (`Kelvin K E L V I N`) with `Kalnia` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `699px` container bounds (`gap: 0.4rem`, padding `1rem`) with `cubic-bezier(0.2,0.7,0.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/kelvin-8b-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×17000px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `699px` extracted from `kelvin-8b-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `0.4rem` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 699px`, `gap: 0.4rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:699px)`, `@media (max-width:899px)`, `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1ede4` | `var(--color-1)` in `:root` |
| **Primary Typography Ink** | `#110d19` | `var(--color-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2d18a8` | `var(--color-3)` in `:root` |
| **Interactive Accent / Highlight** | `#2a5cff` | `var(--color-4)` in `:root` |
| **Secondary / Muted Copy** | `#12c3e3` | `var(--color-5)` in `:root` |
| **Structural Hairline Border** | `#ffe000` | `var(--color-6)` in `:root` |
| **Variable Token (`--color-7`)** | `#ff7a00` | `var(--color-7)` in `:root` |
| **Variable Token (`--color-8`)** | `#ff2c46` | `var(--color-8)` in `:root` |
| **Variable Token (`--color-9`)** | `#ff42ad` | `var(--color-9)` in `:root` |
| **Variable Token (`--color-10`)** | `#5b5664` | `var(--color-10)` in `:root` |
| **Variable Token (`--color-11`)** | `#bcb6c6` | `var(--color-11)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-1` | `#f1ede4` | Brand / Palette Token |
| `--color-2` | `#110d19` | Brand / Palette Token |
| `--color-3` | `#2d18a8` | Brand / Palette Token |
| `--color-4` | `#2a5cff` | Brand / Palette Token |
| `--color-5` | `#12c3e3` | Brand / Palette Token |
| `--color-6` | `#ffe000` | Brand / Palette Token |
| `--color-7` | `#ff7a00` | Brand / Palette Token |
| `--color-8` | `#ff2c46` | Brand / Palette Token |
| `--color-9` | `#ff42ad` | Brand / Palette Token |
| `--color-10` | `#5b5664` | Brand / Palette Token |
| `--color-11` | `#bcb6c6` | Brand / Palette Token |
| `--font-1` | `"Hubot Sans", "Arial Narrow", Arial, sans-serif` | Typography / Scale Token |
| `--font-2` | `"Kalnia", Georgia, serif` | Typography / Scale Token |
| `--font-3` | `"Hubot Sans", "Kelvin Narrow", sans-serif` | Typography / Scale Token |
| `--space-1` | `clamp(16px, 3vw, 44px)` | Layout / Spatial Grid Token |
| `--space-2` | `clamp(88px, 11vw, 168px)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Hubot Sans`.
- **Primary Body Stack**: `Kalnia`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.2,0.7,0.2,1)`, `cubic-bezier(0.2,0.75,0.2,1)`, `cubic-bezier(0.5,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.m-btn-2`**: `transition: color 0.3s` extracted from `kelvin-8b-com` stylesheet.
- **Selector `.m-btn-2::before`**: `transition: transform 0.5s cubic-bezier(0.2,0.7,0.2,1)` extracted from `kelvin-8b-com` stylesheet.
- **Selector `.m-link`**: `transition: background-size 0.4s cubic-bezier(0.2,0.7,0.2,1)` extracted from `kelvin-8b-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,0.7,0.2,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.heat-defs>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Kelvin — three nights of music, filmed in  │
│ ====================================================================== │
│ [ <header.lenis>           | Lineup · Nights · Archive · Visit      ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.m-text>                                     |   │
│ | H1: Kelvin K E L V I N                                           |   │
│ | Substrate: #f1ede4    | Ink: #110d19    | Accent: #2a5cff        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.heat-defs>       ) max-w: 699px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Every set is filmed in heat. |  | Six in the frame, forty‑one  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0.4rem) | │
│ | [<header.lenis>] -> [<section.m-text>] -> [<section.heat-defs] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.m-text-3>     ) | https://kelvin.8b.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `kelvin-8b-com`)**:
   - Landmark `<header class="lenis">` hosting `Kelvin — three nights of music, film` navigation (`Lineup · Nights · Archive · Visit`), DOM attributes (`data-8b-contract="4"`, `data-8b-part="fonts"`, `data-8b-part="layers"`, `data-8b-part="tokens"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.m-text> — `Kelvin K E L V I N`)**:
   - Landmark `<section class="m-text">` presenting display lead `Kelvin K E L V I N` and copy excerpt *"Kelvin Sound in heat · 2027"* over `#f1ede4` canvas and `#110d19` ink.
3. **Primary Showcase & Content Grid (<section.heat-defs> — `Every set is filmed in heat. The r`)**:
   - Landmark `<section class="heat-defs">` rendering section `Every set is filmed in heat. The room paints itself.` with copy *"Sound in heat · 2027"*, asset references (`images.unsplash.com`, `cdn.jsdelivr.net`, `fonts.gstatic.com`, `pe0rMIiULYxOvxVLbVwhEtCaBg.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.nav__brand> — `Six in the frame, forty‑one in the`)**:
   - Landmark `<section class="nav__brand">` framing `Six in the frame, forty‑one in the hall` and `Also in the hall` (*"Centrale Noord · Rotterdam"*) with `#2d18a8` surface cards, `#2a5cff` accents, and `html.lenis body { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://kelvin.8b.com/`)**:
   - Landmark `<footer class="m-text-3">` anchoring `Kelvin — three nights of music, ` footer links (`Lineup · Nights · Archive · Visit`), copy *"2027 · three nights"*, and `#ffe000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: kelvin-8b-com (Kelvin — three nights of music, filmed in heat)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `kelvin-8b-com` (**Kelvin — three nights of music, filmed in heat** — `https://kelvin.8b.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f1ede4` canvas, `#110d19` ink, `#2a5cff` accent).
- **Identity & Domain Context**: Kelvin is a three-night music festival filmed through thermal cameras and projected back into a former power station in Rotterdam. 23–25...
- **Primary Substrate**: `#f1ede4` (`var(--color-1)` in `:root`), **Primary Ink**: `#110d19`, **Accent / Highlight**: `#2a5cff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1ede4` (`var(--color-1)` in `:root`) paired with `#110d19` primary typography and `#2a5cff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Hubot Sans` for display copy (`Kelvin K E L V I N`) with `Kalnia` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `699px` container bounds (`gap: 0.4rem`, padding `1rem`) with `cubic-bezier(0.2,0.7,0.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `kelvin-8b-com` in your global stylesheet:

:root {
  /* Kelvin — three nights of music, filmed in heat (kelvin-8b-com) — Ground-Truth Extracted CSS Variables */
  --color-1: #f1ede4; /* Brand / Palette Token (kelvin-8b-com) */
  --color-2: #110d19; /* Brand / Palette Token (kelvin-8b-com) */
  --color-3: #2d18a8; /* Brand / Palette Token (kelvin-8b-com) */
  --color-4: #2a5cff; /* Brand / Palette Token (kelvin-8b-com) */
  --color-5: #12c3e3; /* Brand / Palette Token (kelvin-8b-com) */
  --color-6: #ffe000; /* Brand / Palette Token (kelvin-8b-com) */
  --color-7: #ff7a00; /* Brand / Palette Token (kelvin-8b-com) */
  --color-8: #ff2c46; /* Brand / Palette Token (kelvin-8b-com) */
  --color-9: #ff42ad; /* Brand / Palette Token (kelvin-8b-com) */
  --color-10: #5b5664; /* Brand / Palette Token (kelvin-8b-com) */
  --color-11: #bcb6c6; /* Brand / Palette Token (kelvin-8b-com) */
  --font-1: "Hubot Sans", "Arial Narrow", Arial, sans-serif; /* Typography / Scale Token (kelvin-8b-com) */
  --font-2: "Kalnia", Georgia, serif; /* Typography / Scale Token (kelvin-8b-com) */
  --font-3: "Hubot Sans", "Kelvin Narrow", sans-serif; /* Typography / Scale Token (kelvin-8b-com) */
  --space-1: clamp(16px, 3vw, 44px); /* Layout / Spatial Grid Token (kelvin-8b-com) */
  --space-2: clamp(88px, 11vw, 168px); /* Layout / Spatial Grid Token (kelvin-8b-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f1ede4` — grounded in `var(--color-1)` in `:root`
- **Primary Typography Ink**: `#110d19` — grounded in `var(--color-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#2d18a8` — grounded in `var(--color-3)` in `:root`
- **Interactive Accent / Highlight**: `#2a5cff` — grounded in `var(--color-4)` in `:root`
- **Secondary / Muted Copy**: `#12c3e3` — grounded in `var(--color-5)` in `:root`
- **Structural Hairline Border**: `#ffe000` — grounded in `var(--color-6)` in `:root`
- **Variable Token (`--color-7`)**: `#ff7a00` — grounded in `var(--color-7)` in `:root`
- **Variable Token (`--color-8`)**: `#ff2c46` — grounded in `var(--color-8)` in `:root`
- **Variable Token (`--color-9`)**: `#ff42ad` — grounded in `var(--color-9)` in `:root`
- **Variable Token (`--color-10`)**: `#5b5664` — grounded in `var(--color-10)` in `:root`
- **Variable Token (`--color-11`)**: `#bcb6c6` — grounded in `var(--color-11)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×17000px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `699px` extracted from `kelvin-8b-com` stylesheet
- **Padding & Gutters**: `1rem` lateral canvas padding with `0.4rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 699px`, `gap: 0.4rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media (max-width:699px)`, `@media (max-width:899px)`, `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)`
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Hubot Sans`
- **Body Font Stack**: `Kalnia`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `kelvin-8b-com` (`Kelvin — three nights of music, filmed in heat`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `kelvin-8b-com`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Kelvin — three nights of music, film` navigation (`Lineup · Nights · Archive · Visit`), DOM attributes (`data-8b-contract="4"`, `data-8b-part="fonts"`, `data-8b-part="layers"`, `data-8b-part="tokens"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `kelvin-8b-com`)` (`kelvin-8b-com`) adapts across `@media (max-width:699px)`, `@media (max-width:899px)`, `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)` with `cubic-bezier(0.2,0.7,0.2,1)`, `cubic-bezier(0.2,0.75,0.2,1)`, `cubic-bezier(0.5,0,0.2,1)` transitions and links `Lineup · Nights · Archive · Visit`.
2. **Hero Stage & Focal Lead (<section.m-text> — `Kelvin K E L V I N`)**:
   - DOM & Selectors: Landmark `<section class="m-text">` presenting display lead `Kelvin K E L V I N` and copy excerpt *"Kelvin Sound in heat · 2027"* over `#f1ede4` canvas and `#110d19` ink.
   - Responsive Contract: Hero stage (`1440×17000px` desktop / `390×2400px` mobile) sets `#f1ede4` background with `#110d19` headline `Kelvin K E L V I N`.
3. **Primary Showcase & Content Grid (<section.heat-defs> — `Every set is filmed in heat. The r`)**:
   - DOM & Selectors: Landmark `<section class="heat-defs">` rendering section `Every set is filmed in heat. The room paints itself.` with copy *"Sound in heat · 2027"*, asset references (`images.unsplash.com`, `cdn.jsdelivr.net`, `fonts.gstatic.com`, `pe0rMIiULYxOvxVLbVwhEtCaBg.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.heat-defs> — `Every set is filmed in heat. The r`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 699px`, `gap: 0.4rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.nav__brand> — `Six in the frame, forty‑one in the`)**:
   - DOM & Selectors: Landmark `<section class="nav__brand">` framing `Six in the frame, forty‑one in the hall` and `Also in the hall` (*"Centrale Noord · Rotterdam"*) with `#2d18a8` surface cards, `#2a5cff` accents, and `html.lenis body { height:auto }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.nav__brand> — `Six in the frame, forty‑one in the`)` uses `50%` radii, `#2a5cff` highlights, and assets (images.unsplash.com, cdn.jsdelivr.net, fonts.gstatic.com).
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://kelvin.8b.com/`)**:
   - DOM & Selectors: Landmark `<footer class="m-text-3">` anchoring `Kelvin — three nights of music, ` footer links (`Lineup · Nights · Archive · Visit`), copy *"2027 · three nights"*, and `#ffe000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.m-text-3> — `https://kelvin.8b.com/`)` aligns to `699px` extracted from `kelvin-8b-com` stylesheet with `1rem` lateral canvas padding with `0.4rem` grid gap and attributes (data-8b-contract="4", data-8b-part="fonts", data-8b-part="layers").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Kelvin Sound in heat · 2027"*
- Copy Excerpt 2: *"Sound in heat · 2027"*
- Copy Excerpt 3: *"Centrale Noord · Rotterdam"*
- Copy Excerpt 4: *"2027 · three nights"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.2,0.7,0.2,1)`, `cubic-bezier(0.2,0.75,0.2,1)`, `cubic-bezier(0.5,0,0.2,1)`
- **Extracted Stylesheet Rules (`kelvin-8b-com`)**:
- `after { box-sizing:border-box }`
- `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`
- `html.lenis body { height:auto }`
- `.lenis.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- **Per-Selector Transition Rules**:
- **Selector `.m-btn-2`**: `transition: color 0.3s` extracted from `kelvin-8b-com` stylesheet.
- **Selector `.m-btn-2::before`**: `transition: transform 0.5s cubic-bezier(0.2,0.7,0.2,1)` extracted from `kelvin-8b-com` stylesheet.
- **Selector `.m-link`**: `transition: background-size 0.4s cubic-bezier(0.2,0.7,0.2,1)` extracted from `kelvin-8b-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,0.7,0.2,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.heat-defs>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `kelvin-8b-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
