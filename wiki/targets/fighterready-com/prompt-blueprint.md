---
title: "UI Prompt Blueprint: fighterready-com"
date: 2026-11-15
target: "[[overview|fighterready-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#080808` / `#2b2b2b`)"
---

# UI Design System & Master Generation Blueprint: fighterready-com

> **Fighter Ready — UK Combat Sports Matchmaking Platform** (https://fighterready.com/) — Matchmaking that decides whether a bout is safe. One traffic light on weight, age, experience and skill before a bout is agreed — with ha...

![Desktop Viewport Capture (1440x12742)](file:///root/projects/fleet/wiki/targets/fighterready-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Fighter Ready — UK Combat Sports Matchmaking Platform** (`https://fighterready.com/`). Matchmaking that decides whether a bout is safe. One traffic light on weight, age, experience and skill before a bout is agreed — with ha...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#080808` / `#2b2b2b`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#080808` (`var(--ink)` in `:root`) paired with `#b8b8b8` primary typography and `#2b2b2b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Barlow Condensed` for display copy (`FIGHTER READY`) with `Inter` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `34rem` container bounds (`gap: 1.25rem`, padding `.8rem`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/fighterready-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×12742px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `34rem` extracted from `fighterready-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.8rem` lateral canvas padding with `1.25rem` grid gap.
- **Border Radius Scale**: `1px`, `50%`, `1rem`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34rem`, `gap: 1.25rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.8rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 52rem)`, `@media (max-width: 1240px)`, `@media (max-width: 860px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#0d0d0d` | `var(--ink-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1a1a1a` | `var(--smoke)` in `:root` |
| **Interactive Accent / Highlight** | `#2b2b2b` | `var(--steel)` in `:root` |
| **Secondary / Muted Copy** | `#6a6a6a` | `var(--ash)` in `:root` |
| **Structural Hairline Border** | `#b8b8b8` | `var(--bone)` in `:root` |
| **Variable Token (`--white`)** | `#f2f2f2` | `var(--white)` in `:root` |
| **Variable Token (`--flame`)** | `#ff6a00` | `var(--flame)` in `:root` |
| **Variable Token (`--amber`)** | `#ffc000` | `var(--amber)` in `:root` |
| **Variable Token (`--gold`)** | `#f5c518` | `var(--gold)` in `:root` |
| **Variable Token (`--ember`)** | `#cc5500` | `var(--ember)` in `:root` |
| **Variable Token (`--green`)** | `#2cc55c` | `var(--green)` in `:root` |
| **Variable Token (`--red`)** | `#ef5350` | `var(--red)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#080808` | Typography Ink Token |
| `--ink-2` | `#0d0d0d` | Typography Ink Token |
| `--smoke` | `#1a1a1a` | Color / Atmospheric Token |
| `--steel` | `#2b2b2b` | Color / Atmospheric Token |
| `--ash` | `#6a6a6a` | Color / Atmospheric Token |
| `--bone` | `#b8b8b8` | Color / Atmospheric Token |
| `--white` | `#f2f2f2` | Canvas / Surface Token |
| `--flame` | `#ff6a00` | Color / Atmospheric Token |
| `--amber` | `#ffc000` | Color / Atmospheric Token |
| `--gold` | `#f5c518` | Color / Atmospheric Token |
| `--ember` | `#cc5500` | Color / Atmospheric Token |
| `--green` | `#2cc55c` | Color / Atmospheric Token |
| `--red` | `#ef5350` | Color / Atmospheric Token |
| `--display` | `"Barlow Condensed", "Arial Narrow", sans-serif` | Design System Custom Token |
| `--body` | `"Inter", system-ui, -apple-system, sans-serif` | Dimension / Scale Token |
| `--gutter` | `clamp(1.25rem, 4vw, 4rem)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Barlow Condensed`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--display: "Barlow Condensed", "Arial Narrow", sans-serif`.
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2rem,4vw,3rem)`).
- **Body Copy**: CSS variables `--body: "Inter", system-ui, -apple-system, sans-serif`; rule `p` (`font-size: .9rem`, `line-height: 1.75`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.625rem`, `.95rem`, `.5rem`, `.75rem`, `clamp(3.25rem,9.5vw,9.5rem)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.skip`**: `transition: top .2s var(--ease)` extracted from `fighterready-com` stylesheet.
- **Selector `.preloader`**: `transition: opacity .9s var(--ease),visibility .9s` extracted from `fighterready-com` stylesheet.
- **Selector `.preloader__bar span`**: `transition: width .35s var(--ease)` extracted from `fighterready-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.masthead>` and `<section.round>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Fighter Ready — UK Combat Sports Matchmaki │
│ ====================================================================== │
│ [ <header.masthead>        | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.round>                                      |   │
│ | H1: FIGHTER READY                                                |   │
│ | Substrate: #080808    | Ink: #b8b8b8    | Accent: #2b2b2b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.round>           ) max-w: 34rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | MATCHMAKING IS BROKEN.       |  | Hours lost                   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1.25re) | │
│ | [<header.masthead>] -> [<section.round>] -> [<section.round>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://fighterready.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.masthead> — `fighterready-com`)**:
   - Landmark `<header class="masthead">` hosting `Fighter Ready — UK Combat Sports Mat` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r170"`, `data-round="doors"`, `data-round="corridor"`, `data-round="ring"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.round> — `FIGHTER READY`)**:
   - Landmark `<section class="round">` presenting display lead `FIGHTER READY` and copy excerpt *"Skip to early access"* over `#080808` canvas and `#b8b8b8` ink.
3. **Primary Showcase & Content Grid (<section.round> — `MATCHMAKING IS BROKEN.`)**:
   - Landmark `<section class="round">` rendering section `MATCHMAKING IS BROKEN.` with copy *"FIGHTER READY COMBAT SPORTS MATCHMAKING"*, asset references (`favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`, `fonts.googleapis.com`), and grid rule `html { background:var(--ink);scroll-behavior:auto }`.
4. **Interactive Detail & Feature Matrix (<section.round> — `Hours lost`)**:
   - Landmark `<section class="round">` framing `Hours lost` and `Mismatches happen` (*"EVENTS & TICKETING"*) with `#1a1a1a` surface cards, `#2b2b2b` accents, and `body.is-locked { overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://fighterready.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Fighter Ready — UK Combat Sports` footer links (`Overview · Index · Archive · About · Contact`), copy *"ROUND 00 — OVERVIEW"*, and `#b8b8b8` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: fighterready-com (Fighter Ready — UK Combat Sports Matchmaking Platform)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `fighterready-com` (**Fighter Ready — UK Combat Sports Matchmaking Platform** — `https://fighterready.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080808` / `#2b2b2b`).
- **Identity & Domain Context**: Matchmaking that decides whether a bout is safe. One traffic light on weight, age, experience and skill before a bout is agreed — with ha...
- **Primary Substrate**: `#080808` (`var(--ink)` in `:root`), **Primary Ink**: `#b8b8b8`, **Accent / Highlight**: `#2b2b2b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#080808` (`var(--ink)` in `:root`) paired with `#b8b8b8` primary typography and `#2b2b2b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Barlow Condensed` for display copy (`FIGHTER READY`) with `Inter` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `34rem` container bounds (`gap: 1.25rem`, padding `.8rem`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `fighterready-com` in your global stylesheet:

:root {
  /* Fighter Ready — UK Combat Sports Matchmaking Platform (fighterready-com) — Ground-Truth Extracted CSS Variables */
  --ink: #080808; /* Typography Ink Token (fighterready-com) */
  --ink-2: #0d0d0d; /* Typography Ink Token (fighterready-com) */
  --smoke: #1a1a1a; /* Color / Atmospheric Token (fighterready-com) */
  --steel: #2b2b2b; /* Color / Atmospheric Token (fighterready-com) */
  --ash: #6a6a6a; /* Color / Atmospheric Token (fighterready-com) */
  --bone: #b8b8b8; /* Color / Atmospheric Token (fighterready-com) */
  --white: #f2f2f2; /* Canvas / Surface Token (fighterready-com) */
  --flame: #ff6a00; /* Color / Atmospheric Token (fighterready-com) */
  --amber: #ffc000; /* Color / Atmospheric Token (fighterready-com) */
  --gold: #f5c518; /* Color / Atmospheric Token (fighterready-com) */
  --ember: #cc5500; /* Color / Atmospheric Token (fighterready-com) */
  --green: #2cc55c; /* Color / Atmospheric Token (fighterready-com) */
  --red: #ef5350; /* Color / Atmospheric Token (fighterready-com) */
  --display: "Barlow Condensed", "Arial Narrow", sans-serif; /* Design System Custom Token (fighterready-com) */
  --body: "Inter", system-ui, -apple-system, sans-serif; /* Dimension / Scale Token (fighterready-com) */
  --gutter: clamp(1.25rem, 4vw, 4rem); /* Layout / Spatial Grid Token (fighterready-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#080808` — grounded in `var(--ink)` in `:root`
- **Primary Typography Ink**: `#0d0d0d` — grounded in `var(--ink-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#1a1a1a` — grounded in `var(--smoke)` in `:root`
- **Interactive Accent / Highlight**: `#2b2b2b` — grounded in `var(--steel)` in `:root`
- **Secondary / Muted Copy**: `#6a6a6a` — grounded in `var(--ash)` in `:root`
- **Structural Hairline Border**: `#b8b8b8` — grounded in `var(--bone)` in `:root`
- **Variable Token (`--white`)**: `#f2f2f2` — grounded in `var(--white)` in `:root`
- **Variable Token (`--flame`)**: `#ff6a00` — grounded in `var(--flame)` in `:root`
- **Variable Token (`--amber`)**: `#ffc000` — grounded in `var(--amber)` in `:root`
- **Variable Token (`--gold`)**: `#f5c518` — grounded in `var(--gold)` in `:root`
- **Variable Token (`--ember`)**: `#cc5500` — grounded in `var(--ember)` in `:root`
- **Variable Token (`--green`)**: `#2cc55c` — grounded in `var(--green)` in `:root`
- **Variable Token (`--red`)**: `#ef5350` — grounded in `var(--red)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×12742px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `34rem` extracted from `fighterready-com` stylesheet
- **Padding & Gutters**: `.8rem` lateral canvas padding with `1.25rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34rem`, `gap: 1.25rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.8rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 52rem)`, `@media (max-width: 1240px)`, `@media (max-width: 860px)`
- **Corner Radii**: `1px`, `50%`, `1rem`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Barlow Condensed`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--display: "Barlow Condensed", "Arial Narrow", sans-serif`
- **H2 Section Rule**: rule `h2` (`font-size: clamp(2rem,4vw,3rem)`)
- **Body Copy Rule**: CSS variables `--body: "Inter", system-ui, -apple-system, sans-serif`; rule `p` (`font-size: .9rem`, `line-height: 1.75`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.625rem`, `.95rem`, `.5rem`, `.75rem`, `clamp(3.25rem,9.5vw,9.5rem)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `fighterready-com` (`Fighter Ready — UK Combat Sports Matchmaking Platform`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.masthead> — `fighterready-com`)**:
   - DOM & Selectors: Landmark `<header class="masthead">` hosting `Fighter Ready — UK Combat Sports Mat` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r170"`, `data-round="doors"`, `data-round="corridor"`, `data-round="ring"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.masthead> — `fighterready-com`)` (`fighterready-com`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 52rem)`, `@media (max-width: 1240px)`, `@media (max-width: 860px)` with `cubic-bezier(.22,1,.36,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.round> — `FIGHTER READY`)**:
   - DOM & Selectors: Landmark `<section class="round">` presenting display lead `FIGHTER READY` and copy excerpt *"Skip to early access"* over `#080808` canvas and `#b8b8b8` ink.
   - Responsive Contract: Hero stage (`1440×12742px` desktop / `390×2400px` mobile) sets `#080808` background with `#b8b8b8` headline `FIGHTER READY`.
3. **Primary Showcase & Content Grid (<section.round> — `MATCHMAKING IS BROKEN.`)**:
   - DOM & Selectors: Landmark `<section class="round">` rendering section `MATCHMAKING IS BROKEN.` with copy *"FIGHTER READY COMBAT SPORTS MATCHMAKING"*, asset references (`favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`, `fonts.googleapis.com`), and grid rule `html { background:var(--ink);scroll-behavior:auto }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.round> — `MATCHMAKING IS BROKEN.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34rem`, `gap: 1.25rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.8rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.round> — `Hours lost`)**:
   - DOM & Selectors: Landmark `<section class="round">` framing `Hours lost` and `Mismatches happen` (*"EVENTS & TICKETING"*) with `#1a1a1a` surface cards, `#2b2b2b` accents, and `body.is-locked { overflow:hidden }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.round> — `Hours lost`)` uses `1px`, `50%`, `1rem`, `2px` radii, `#2b2b2b` highlights, and assets (favicon.ico, apple-touch-icon.png, site.webmanifest).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://fighterready.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Fighter Ready — UK Combat Sports` footer links (`Overview · Index · Archive · About · Contact`), copy *"ROUND 00 — OVERVIEW"*, and `#b8b8b8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://fighterready.com/`)` aligns to `34rem` extracted from `fighterready-com` stylesheet with `.8rem` lateral canvas padding with `1.25rem` grid gap and attributes (data-engine="three.js r170", data-round="doors", data-round="corridor").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to early access"*
- Copy Excerpt 2: *"FIGHTER READY COMBAT SPORTS MATCHMAKING"*
- Copy Excerpt 3: *"EVENTS & TICKETING"*
- Copy Excerpt 4: *"ROUND 00 — OVERVIEW"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`fighterready-com`)**:
- `after { box-sizing:border-box }`
- `html { background:var(--ink);scroll-behavior:auto }`
- `body.is-locked { overflow:hidden }`
- `focus-visible { outline:2px solid var(--flame);outline-offset:3px;border-radius:1px }`
- `.preloader.is-done { opacity:0;visibility:hidden }`
- **Per-Selector Transition Rules**:
- **Selector `.skip`**: `transition: top .2s var(--ease)` extracted from `fighterready-com` stylesheet.
- **Selector `.preloader`**: `transition: opacity .9s var(--ease),visibility .9s` extracted from `fighterready-com` stylesheet.
- **Selector `.preloader__bar span`**: `transition: width .35s var(--ease)` extracted from `fighterready-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.masthead>` and `<section.round>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `fighterready-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
