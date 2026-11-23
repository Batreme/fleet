---
title: "UI Prompt Blueprint: www-blumjeffrey-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-blumjeffrey-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#080808` canvas, `#f5f5f0` ink, `#378ef0` accent)"
---

# UI Design System & Master Generation Blueprint: www-blumjeffrey-com

> **Jeffrey Blum — AI Digital Creative Director** (https://www.blumjeffrey.com) — Jeffrey Blum is a New York-based AI Digital Creative Director building creative systems, intelligent workflows, brand platforms, and digi...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Jeffrey Blum — AI Digital Creative Director** (`https://www.blumjeffrey.com`). Jeffrey Blum is a New York-based AI Digital Creative Director building creative systems, intelligent workflows, brand platforms, and digi...
- **Final Redirected URL**: [https://blumjeffrey.com/](https://blumjeffrey.com/)
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#080808` canvas, `#f5f5f0` ink, `#378ef0` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#080808` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5f5f0` primary typography and `#378ef0` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Barlow Condensed` for display copy (`SHAPE VISION. BUILD SYSTEMS.`) with `Barlow` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1320px` container bounds (`gap: 32px`, padding `48px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1320px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `48px` lateral canvas padding with `32px` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 32px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1024px)`, `@media (max-width:640px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f0` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.wcs .cs-bg { background: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#378ef0` | `.home-v2 .damBtn { background: #378ef0 }` |
| **Secondary / Muted Copy** | `#888888` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2a2a2a` | `var(--border)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--motion-instant` | `.12s` | Motion / Easing Token |
| `--motion-fast` | `.2s` | Motion / Easing Token |
| `--motion-medium` | `.3s` | Motion / Easing Token |
| `--motion-slow` | `.4s` | Motion / Easing Token |
| `--motion-reveal` | `.8s` | Motion / Easing Token |
| `--motion-hero` | `.9s` | Motion / Easing Token |
| `--motion-counter` | `1.1s` | Motion / Easing Token |
| `--motion-marquee` | `28s` | Motion / Easing Token |
| `--ease-standard` | `ease` | Motion / Easing Token |
| `--ease-linear` | `linear` | Motion / Easing Token |
| `--ease-pulse` | `ease-in-out` | Motion / Easing Token |
| `--ease-expressive` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--motion-shift-xs` | `4px` | Motion / Easing Token |
| `--motion-shift-sm` | `8px` | Motion / Easing Token |
| `--motion-shift-md` | `20px` | Motion / Easing Token |
| `--motion-shift-lg` | `32px` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Barlow Condensed`.
- **Primary Body Stack**: `Barlow`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 138.24px`, `line-height: 121.651px`, `font-weight: 900`, `letter-spacing: -2.7648px`); rule `h1` (`font-size: clamp(64px,9.6vw,180px)`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 129.6px`, `line-height: 114.048px`, `font-weight: 900`, `letter-spacing: -2.592px`); rule `h2` (`font-size: clamp(64px,9vw,170px)`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 300`); rule `p` (`font-size: clamp(1.3rem,2.5vw,2rem)`, `line-height: 1.25`, `font-weight: 300`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 300`); rule `small` (`font-size: .6rem`, `letter-spacing: .22em`, `font-weight: 600`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,1.35,.5,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.wcs .cs-nav`**: `transition: background .4s,border-color .4s,-webkit-backdrop-filter .4s,ba...` extracted from `www-blumjeffrey-com` stylesheet.
- **Selector `.wcs .cs-x`**: `transition: background var(--motion-fast),color var(--motion-fast),border-...` extracted from `www-blumjeffrey-com` stylesheet.
- **Selector `.wcs .cs-x i`**: `transition: transform var(--motion-slow)var(--ease-expressive)` extracted from `www-blumjeffrey-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.cs-hero>` and `<section.home>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Jeffrey Blum — AI Digital Creative Directo │
│ ====================================================================== │
│ [ <header.cs-hero> (1440px)           | Work · Lab · Speaking · Abou ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.lenis-scrolling> (w=1440px)                   | │
│ | H1: SHAPE VISION. BUILD SYSTEMS.                                   | │
│ | Substrate: #080808 | Ink: #f5f5f0 | Accent: #378ef0                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home>) max-w: 1320px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Shape vision. Build systems. |  | Recent projects              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.clients-scene>) — M·A·C Design System      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ft>         ) | https://www.blumjeffrey.com          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 32px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.cs-hero>        ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.lenis-scrolling) — 390px Vertical Lead        | │
│ | H1: SHAPE VISION. BUILD SYSTEMS.                                   | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.home>) — 1-Col Stack                      | │
│ | [ Item 1: Shape vision. Build systems.                           ] | │
│ | [ Item 2: Recent projects                                        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.clients-scene>) — 1-Col (M·A·C Design Syste)  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ft>         ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.cs-hero> — `www-blumjeffrey-com`)**:
   - Landmark `<header class="cs-hero">` (`1440px`) hosting `Jeffrey Blum — AI Digital Creative D` navigation (`Work · Lab · Speaking · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-motion="gsap"`), and stylesheet rule `.wcs .disp { font-family:var(--fd);text-transform:uppercase;letter-spacing:-.02em;fon... }`.
2. **Hero Stage & Focal Lead (<section.lenis-scrolling> — `SHAPE VISION. BUILD SYSTEMS.`)**:
   - Landmark `<section class="lenis-scrolling">` presenting display lead `SHAPE VISION. BUILD SYSTEMS.` and copy excerpt *"AI DIGITAL CREATIVE DIRECTOR · NEW YORK"* over `#080808` canvas and `#f5f5f0` ink.
3. **Primary Showcase & Content Grid (<section.home> — `Shape vision. Build systems.`)**:
   - Landmark `<section class="home">` rendering section `Shape vision. Build systems.` with copy *"AI Digital Creative Director · New York"*, asset references (`235a0ef330592118-s.p.b3cd1641.woff2`, `303804218d80822e-s.p.9b40bd6c.woff2`, `4f530f52d514af96-s.p.52297690.woff2`, `81cef6a21128489e-s.p.6cf41120.woff2`), and grid rule `.wcs .mask .ln { padding-top:.06em;display:block;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.clients-scene> — `Recent projects`)**:
   - Landmark `<section class="clients-scene">` framing `Recent projects` and `M·A·C Design System` (*"Hey, Jeffrey here. I design digital experiences and the intellige"*) with `#000000` surface cards, `#378ef0` accents, and `.wcs .mask .ln>span { display:block }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://www.blumjeffrey.com`)**:
   - Landmark `<footer class="ft fixed">` anchoring `Jeffrey Blum — AI Digital Creati` footer links (`Work · Lab · Speaking · About · Contact`), copy *"From Swiss watchmakers to global beauty. Digital products, c"*, and `#2a2a2a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-blumjeffrey-com (Jeffrey Blum — AI Digital Creative Director)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-blumjeffrey-com` (**Jeffrey Blum — AI Digital Creative Director** — `https://www.blumjeffrey.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#080808` canvas, `#f5f5f0` ink, `#378ef0` accent).
- **Identity & Domain Context**: Jeffrey Blum is a New York-based AI Digital Creative Director building creative systems, intelligent workflows, brand platforms, and digi...
- **Primary Substrate**: `#080808` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f5f5f0`, **Accent / Highlight**: `#378ef0`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#080808` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5f5f0` primary typography and `#378ef0` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Barlow Condensed` for display copy (`SHAPE VISION. BUILD SYSTEMS.`) with `Barlow` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1320px` container bounds (`gap: 32px`, padding `48px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-blumjeffrey-com` in your global stylesheet:

:root {
  /* Jeffrey Blum — AI Digital Creative Director (www-blumjeffrey-com) — Live-Grounded CSS Variables */
  --motion-instant: .12s; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-fast: .2s; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-medium: .3s; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-slow: .4s; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-reveal: .8s; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-hero: .9s; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-counter: 1.1s; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-marquee: 28s; /* Motion / Easing Token (www-blumjeffrey-com) */
  --ease-standard: ease; /* Motion / Easing Token (www-blumjeffrey-com) */
  --ease-linear: linear; /* Motion / Easing Token (www-blumjeffrey-com) */
  --ease-pulse: ease-in-out; /* Motion / Easing Token (www-blumjeffrey-com) */
  --ease-expressive: cubic-bezier(.16,1,.3,1); /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-shift-xs: 4px; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-shift-sm: 8px; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-shift-md: 20px; /* Motion / Easing Token (www-blumjeffrey-com) */
  --motion-shift-lg: 32px; /* Motion / Easing Token (www-blumjeffrey-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#080808` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f5f5f0` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `.wcs .cs-bg { background: black }` (`#000000`)
- **Interactive Accent / Highlight**: `#378ef0` — grounded in `.home-v2 .damBtn { background: #378ef0 }`
- **Secondary / Muted Copy**: `#888888` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#2a2a2a` — grounded in `var(--border)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1320px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `48px` lateral canvas padding with `32px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 32px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding
- **Media Queries**: `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1024px)`, `@media (max-width:640px)`
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Barlow Condensed`
- **Body Font Stack**: `Barlow`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 138.24px`, `line-height: 121.651px`, `font-weight: 900`, `letter-spacing: -2.7648px`); rule `h1` (`font-size: clamp(64px,9.6vw,180px)`)
- **H2 Section Rule**: live computed `h2` (`font-size: 129.6px`, `line-height: 114.048px`, `font-weight: 900`, `letter-spacing: -2.592px`); rule `h2` (`font-size: clamp(64px,9vw,170px)`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 300`); rule `p` (`font-size: clamp(1.3rem,2.5vw,2rem)`, `line-height: 1.25`, `font-weight: 300`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 300`); rule `small` (`font-size: .6rem`, `letter-spacing: .22em`, `font-weight: 600`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-blumjeffrey-com` (`Jeffrey Blum — AI Digital Creative Director`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.cs-hero> — `www-blumjeffrey-com`)**:
   - DOM & Selectors: Landmark `<header class="cs-hero">` (`1440px`) hosting `Jeffrey Blum — AI Digital Creative D` navigation (`Work · Lab · Speaking · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-motion="gsap"`), and stylesheet rule `.wcs .disp { font-family:var(--fd);text-transform:uppercase;letter-spacing:-.02em;fon... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.cs-hero> — `www-blumjeffrey-com`)` (`www-blumjeffrey-com`) adapts across `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1024px)`, `@media (max-width:640px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,1.35,.5,1)` transitions and links `Work · Lab · Speaking · About · Contact`.
2. **Hero Stage & Focal Lead (<section.lenis-scrolling> — `SHAPE VISION. BUILD SYSTEMS.`)**:
   - DOM & Selectors: Landmark `<section class="lenis-scrolling">` presenting display lead `SHAPE VISION. BUILD SYSTEMS.` and copy excerpt *"AI DIGITAL CREATIVE DIRECTOR · NEW YORK"* over `#080808` canvas and `#f5f5f0` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#080808` background with `#f5f5f0` headline `SHAPE VISION. BUILD SYSTEMS.`.
3. **Primary Showcase & Content Grid (<section.home> — `Shape vision. Build systems.`)**:
   - DOM & Selectors: Landmark `<section class="home">` rendering section `Shape vision. Build systems.` with copy *"AI Digital Creative Director · New York"*, asset references (`235a0ef330592118-s.p.b3cd1641.woff2`, `303804218d80822e-s.p.9b40bd6c.woff2`, `4f530f52d514af96-s.p.52297690.woff2`, `81cef6a21128489e-s.p.6cf41120.woff2`), and grid rule `.wcs .mask .ln { padding-top:.06em;display:block;overflow:hidden }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home> — `Shape vision. Build systems.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 32px`) on desktop and Single-column vertical stack at `390px` viewport width with `48px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.clients-scene> — `Recent projects`)**:
   - DOM & Selectors: Landmark `<section class="clients-scene">` framing `Recent projects` and `M·A·C Design System` (*"Hey, Jeffrey here. I design digital experiences and the intellige"*) with `#000000` surface cards, `#378ef0` accents, and `.wcs .mask .ln>span { display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.clients-scene> — `Recent projects`)` uses `50%` radii, `#378ef0` highlights, and assets (235a0ef330592118-s.p.b3cd1641.woff2, 303804218d80822e-s.p.9b40bd6c.woff2, 4f530f52d514af96-s.p.52297690.woff2).
5. **Colophon & Global Directory Footer (<footer.ft> — `https://www.blumjeffrey.com`)**:
   - DOM & Selectors: Landmark `<footer class="ft fixed">` anchoring `Jeffrey Blum — AI Digital Creati` footer links (`Work · Lab · Speaking · About · Contact`), copy *"From Swiss watchmakers to global beauty. Digital products, c"*, and `#2a2a2a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ft> — `https://www.blumjeffrey.com`)` aligns to `1320px` (non-`@media` desktop container stylesheet rule) with `48px` lateral canvas padding with `32px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"AI DIGITAL CREATIVE DIRECTOR · NEW YORK"*
- Copy Excerpt 2: *"AI Digital Creative Director · New York"*
- Copy Excerpt 3: *"Hey, Jeffrey here. I design digital experiences and the intelligent systems behind..."*
- Copy Excerpt 4: *"From Swiss watchmakers to global beauty. Digital products, creative systems and AI..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,1.35,.5,1)`
- **Extracted Stylesheet Rules (`www-blumjeffrey-com`)**:
- `.wcs .disp { font-family:var(--fd);text-transform:uppercase;letter-spacing:-.02em;fon... }`
- `.wcs .mask .ln { padding-top:.06em;display:block;overflow:hidden }`
- `.wcs .mask .ln>span { display:block }`
- `.wcs .cs-media .hwrap { position:absolute;inset:0;overflow:hidden }`
- `.wcs .cs-media .hwrap.still video { object-fit:cover;width:100%;height:100%;display:block;position:absolute;... }`
- **Per-Selector Transition Rules**:
- **Selector `.wcs .cs-nav`**: `transition: background .4s,border-color .4s,-webkit-backdrop-filter .4s,ba...` extracted from `www-blumjeffrey-com` stylesheet.
- **Selector `.wcs .cs-x`**: `transition: background var(--motion-fast),color var(--motion-fast),border-...` extracted from `www-blumjeffrey-com` stylesheet.
- **Selector `.wcs .cs-x i`**: `transition: transform var(--motion-slow)var(--ease-expressive)` extracted from `www-blumjeffrey-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.cs-hero>` and `<section.home>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-blumjeffrey-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
