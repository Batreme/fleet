---
title: "UI Prompt Blueprint: departmentofemotions-com"
date: 2026-11-15
target: "departmentofemotions-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#212c24` canvas, `#fff` ink, `#e2e7db` accent)"
---

# UI Design System & Master Generation Blueprint: departmentofemotions-com

> **Department of Emotions** (https://departmentofemotions.com/) — Explore your emotions with an interactive feeling wheel, body-language examples, somatic sensations, and behavioral experiences.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Department of Emotions** (`https://departmentofemotions.com/`). Explore your emotions with an interactive feeling wheel, body-language examples, somatic sensations, and behavioral experiences.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#212c24` canvas, `#fff` ink, `#e2e7db` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#212c24` (`.privacy-page { color: #212c24 }`) paired with `#fff` primary typography and `#e2e7db` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Gilda Display` for display copy (`Isolated`) with `Segoe UI` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `648px` container bounds (`gap: 5px`, padding `64px`) with `cubic-bezier(.23,1,.32,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `648px` extracted from `departmentofemotions-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `64px` lateral canvas padding with `5px` grid gap.
- **Border Radius Scale**: `50%`, `1px`, `22px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 648px`, `gap: 5px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `64px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`, `@media (min-width:1101px),(orientation:landscape)`, `@media (min-width:1024px)and (max-width:1279px)`, `@media (min-width:1024px)and (max-width:1100px)and (orientation:...`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#212c24` | `.privacy-page { color: #212c24 }` |
| **Primary Typography Ink** | `#fff` | `html { background: #fff }` |
| **Elevated Surface / Card Substrate** | `#33443a` | `.explorer-loading { color: #33443a }` |
| **Interactive Accent / Highlight** | `#e2e7db` | `.explorer-page button:focus-vis... { background: #e2e7db }` |
| **Secondary / Muted Copy** | `#6f7f74` | `.explorer-page button:focus-vis... { border-color: #6f7f74 }` |
| **Structural Hairline Border** | `#292929` | `.explorer-label { fill: #292929 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `oklch(28% .022 154)` | Typography Ink Token |
| `--muted` | `oklch(49% .016 154)` | Color / Atmospheric Token |
| `--line` | `oklch(86% .012 125)` | Color / Atmospheric Token |
| `--paper` | `oklch(98% .008 105)` | Canvas / Surface Token |
| `--desktop-wheel-size` | `clamp(74vw, 120svh, 92vw)` | Layout / Spatial Grid Token |
| `--mobile-wheel-size` | `min(160vw, 820px)` | Layout / Spatial Grid Token |
| `--landscape-wheel-size` | `clamp(560px, 160svh, 92vw)` | Layout / Spatial Grid Token |
| `--lab-toolbar-height` | `0px` | Layout / Spatial Grid Token |
| `--phone-wheel-size` | `213.75vw` | Layout / Spatial Grid Token |
| `--wheel-muted-opacity` | `0.38` | Design System Custom Token |
| `--wheel-fade-duration` | `180ms` | Motion / Easing Token |
| `--departmentofemot-bg` | `#212c24` | Canvas Substrate (from `.privacy-page { color: #212c24 }`) |
| `--departmentofemot-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--departmentofemot-surface` | `#33443a` | Surface Substrate (stylesheet-derived) |
| `--departmentofemot-accent` | `#e2e7db` | Interactive Accent (stylesheet-derived) |
| `--departmentofemot-muted` | `#6f7f74` | Secondary Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Gilda Display`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 48px`, `line-height: 1.12`, `letter-spacing: -.6px`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 11px`, `letter-spacing: 1.4px`).
- **Body Copy**: rule `p` (`font-size: 14px`, `line-height: 1.7`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `11px`, `10px`, `46px`, `48px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.23,1,.32,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.explorer-sector`**: `transition: opacity var(--wheel-fade-duration, .18s) ease-out` extracted from `departmentofemotions-com` stylesheet.
- **Selector `.wheel-strokes`**: `transition: opacity var(--wheel-fade-duration, .18s) ease-out` extracted from `departmentofemotions-com` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none!important` extracted from `departmentofemotions-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<nav.lab-switcher>` and `<section.wheel-workspace>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.explorer-page>` and `<section.wheel-workspace>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Department of Emotions                     │
│ ====================================================================== │
│ [ <nav.lab-switcher>       | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.explorer-page>                              |   │
│ | H1: Isolated                                                     |   │
│ | Substrate: #212c24    | Ink: #fff       | Accent: #e2e7db        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.wheel-workspace> ) max-w: 648px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | How it may feel in the body  |  | Possible body language & beh | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 5px   ) | │
│ | [<nav.lab-switcher>] -> [<section.explorer-] -> [<section.wheel-wor] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sidebar-footer) | https://departmentofemotions.com/  │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.lab-switcher> — `departmentofemotions-com`)**:
   - Landmark `<nav class="lab-switcher">` hosting `Department of Emotions` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wheel="feelings"`, `data-moving="false"`, `data-sector-index="0"`, `data-emotion="Anger"`), and stylesheet rule `.privacy-page { max-width:648px;margin-inline:auto;padding:64px 24px;color:212c24;font:1... }`.
2. **Hero Stage & Focal Lead (<section.explorer-page> — `Isolated`)**:
   - Landmark `<section class="explorer-page">` presenting display lead `Isolated` and copy excerpt *"Skip to the emotion explorer"* over `#212c24` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.wheel-workspace> — `How it may feel in the body`)**:
   - Landmark `<section class="wheel-workspace">` rendering section `How it may feel in the body` with copy *"Feeling separated from other people or unable to take part in a s"*, asset references (`favicon.ico`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.privacy-brand { display:inline-flex;align-items:center;gap:5px;font-weight:650;font-size... }`.
4. **Interactive Detail & Feature Matrix (<section.experience-section> — `Possible body language & behaviors`)**:
   - Landmark `<section class="experience-section">` framing `Possible body language & behaviors` and `01 An empty or constricted feeling in the chest.` (*"01 An empty or constricted feeling in the chest."*) with `#33443a` surface cards, `#e2e7db` accents, and `.privacy-page h1 { margin:40px 0 24px;font:400 42px/1.2 Gilda Display,Georgia,serif }`.
5. **Colophon & Global Directory Footer (<footer.sidebar-footer> — `https://departmentofemotions.com/`)**:
   - Landmark `<footer class="sidebar-footer">` anchoring `Department of Emotions` footer links (`Overview · Index · Archive · About · Contact`), copy *"An empty or constricted feeling in the chest."*, and `#292929` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: departmentofemotions-com (Department of Emotions)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `departmentofemotions-com` (**Department of Emotions** — `https://departmentofemotions.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#212c24` canvas, `#fff` ink, `#e2e7db` accent).
- **Identity & Domain Context**: Explore your emotions with an interactive feeling wheel, body-language examples, somatic sensations, and behavioral experiences.
- **Primary Substrate**: `#212c24` (`.privacy-page { color: #212c24 }`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#e2e7db`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#212c24` (`.privacy-page { color: #212c24 }`) paired with `#fff` primary typography and `#e2e7db` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Gilda Display` for display copy (`Isolated`) with `Segoe UI` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `648px` container bounds (`gap: 5px`, padding `64px`) with `cubic-bezier(.23,1,.32,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `departmentofemotions-com` in your global stylesheet:

:root {
  /* Department of Emotions (departmentofemotions-com) — Ground-Truth Extracted CSS Variables */
  --ink: oklch(28% .022 154); /* Typography Ink Token (departmentofemotions-com) */
  --muted: oklch(49% .016 154); /* Color / Atmospheric Token (departmentofemotions-com) */
  --line: oklch(86% .012 125); /* Color / Atmospheric Token (departmentofemotions-com) */
  --paper: oklch(98% .008 105); /* Canvas / Surface Token (departmentofemotions-com) */
  --desktop-wheel-size: clamp(74vw, 120svh, 92vw); /* Layout / Spatial Grid Token (departmentofemotions-com) */
  --mobile-wheel-size: min(160vw, 820px); /* Layout / Spatial Grid Token (departmentofemotions-com) */
  --landscape-wheel-size: clamp(560px, 160svh, 92vw); /* Layout / Spatial Grid Token (departmentofemotions-com) */
  --lab-toolbar-height: 0px; /* Layout / Spatial Grid Token (departmentofemotions-com) */
  --phone-wheel-size: 213.75vw; /* Layout / Spatial Grid Token (departmentofemotions-com) */
  --wheel-muted-opacity: 0.38; /* Design System Custom Token (departmentofemotions-com) */
  --wheel-fade-duration: 180ms; /* Motion / Easing Token (departmentofemotions-com) */
  --departmentofemot-bg: #212c24; /* Canvas Substrate (from `.privacy-page { color: #212c24 }`) (departmentofemotions-com) */
  --departmentofemot-ink: #fff; /* Primary Typography Ink (stylesheet-derived) (departmentofemotions-com) */
  --departmentofemot-surface: #33443a; /* Surface Substrate (stylesheet-derived) (departmentofemotions-com) */
  --departmentofemot-accent: #e2e7db; /* Interactive Accent (stylesheet-derived) (departmentofemotions-com) */
  --departmentofemot-muted: #6f7f74; /* Secondary Ink (stylesheet-derived) (departmentofemotions-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#212c24` — grounded in `.privacy-page { color: #212c24 }`
- **Primary Typography Ink**: `#fff` — grounded in `html { background: #fff }`
- **Elevated Surface / Card Substrate**: `#33443a` — grounded in `.explorer-loading { color: #33443a }`
- **Interactive Accent / Highlight**: `#e2e7db` — grounded in `.explorer-page button:focus-vis... { background: #e2e7db }`
- **Secondary / Muted Copy**: `#6f7f74` — grounded in `.explorer-page button:focus-vis... { border-color: #6f7f74 }`
- **Structural Hairline Border**: `#292929` — grounded in `.explorer-label { fill: #292929 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `648px` extracted from `departmentofemotions-com` stylesheet
- **Padding & Gutters**: `64px` lateral canvas padding with `5px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 648px`, `gap: 5px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `64px` horizontal padding
- **Media Queries**: `@media (max-width:600px)`, `@media (min-width:1101px),(orientation:landscape)`, `@media (min-width:1024px)and (max-width:1279px)`, `@media (min-width:1024px)and (max-width:1100px)and (orientation:...`
- **Corner Radii**: `50%`, `1px`, `22px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Gilda Display`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 48px`, `line-height: 1.12`, `letter-spacing: -.6px`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: 11px`, `letter-spacing: 1.4px`)
- **Body Copy Rule**: rule `p` (`font-size: 14px`, `line-height: 1.7`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `11px`, `10px`, `46px`, `48px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `departmentofemotions-com` (`Department of Emotions`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.lab-switcher> — `departmentofemotions-com`)**:
   - DOM & Selectors: Landmark `<nav class="lab-switcher">` hosting `Department of Emotions` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wheel="feelings"`, `data-moving="false"`, `data-sector-index="0"`, `data-emotion="Anger"`), and stylesheet rule `.privacy-page { max-width:648px;margin-inline:auto;padding:64px 24px;color:212c24;font:1... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.lab-switcher> — `departmentofemotions-com`)` (`departmentofemotions-com`) adapts across `@media (max-width:600px)`, `@media (min-width:1101px),(orientation:landscape)`, `@media (min-width:1024px)and (max-width:1279px)`, `@media (min-width:1024px)and (max-width:1100px)and (orientation:...` with `cubic-bezier(.23,1,.32,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.explorer-page> — `Isolated`)**:
   - DOM & Selectors: Landmark `<section class="explorer-page">` presenting display lead `Isolated` and copy excerpt *"Skip to the emotion explorer"* over `#212c24` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#212c24` background with `#fff` headline `Isolated`.
3. **Primary Showcase & Content Grid (<section.wheel-workspace> — `How it may feel in the body`)**:
   - DOM & Selectors: Landmark `<section class="wheel-workspace">` rendering section `How it may feel in the body` with copy *"Feeling separated from other people or unable to take part in a s"*, asset references (`favicon.ico`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.privacy-brand { display:inline-flex;align-items:center;gap:5px;font-weight:650;font-size... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.wheel-workspace> — `How it may feel in the body`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 648px`, `gap: 5px`) on desktop and Single-column vertical stack at `390px` viewport width with `64px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.experience-section> — `Possible body language & behaviors`)**:
   - DOM & Selectors: Landmark `<section class="experience-section">` framing `Possible body language & behaviors` and `01 An empty or constricted feeling in the chest.` (*"01 An empty or constricted feeling in the chest."*) with `#33443a` surface cards, `#e2e7db` accents, and `.privacy-page h1 { margin:40px 0 24px;font:400 42px/1.2 Gilda Display,Georgia,serif }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.experience-section> — `Possible body language & behaviors`)` uses `50%`, `1px`, `22px` radii, `#e2e7db` highlights, and assets (favicon.ico, favicon-32.png, favicon.svg).
5. **Colophon & Global Directory Footer (<footer.sidebar-footer> — `https://departmentofemotions.com/`)**:
   - DOM & Selectors: Landmark `<footer class="sidebar-footer">` anchoring `Department of Emotions` footer links (`Overview · Index · Archive · About · Contact`), copy *"An empty or constricted feeling in the chest."*, and `#292929` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sidebar-footer> — `https://departmentofemotions.com/`)` aligns to `648px` extracted from `departmentofemotions-com` stylesheet with `64px` lateral canvas padding with `5px` grid gap and attributes (data-wheel="feelings", data-moving="false", data-sector-index="0").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to the emotion explorer"*
- Copy Excerpt 2: *"Feeling separated from other people or unable to take part in a shared connection."*
- Copy Excerpt 3: *"01 An empty or constricted feeling in the chest."*
- Copy Excerpt 4: *"An empty or constricted feeling in the chest."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.23,1,.32,1)`
- **Extracted Stylesheet Rules (`departmentofemotions-com`)**:
- `.privacy-page { max-width:648px;margin-inline:auto;padding:64px 24px;color:212c24;font:1... }`
- `.privacy-brand { display:inline-flex;align-items:center;gap:5px;font-weight:650;font-size... }`
- `.privacy-page h1 { margin:40px 0 24px;font:400 42px/1.2 Gilda Display,Georgia,serif }`
- `.privacy-page h2 { margin-top:32px;font-size:11px;letter-spacing:1.4px;text-transform:upper... }`
- `.privacy-page a { color:inherit;text-underline-offset:3px }`
- **Per-Selector Transition Rules**:
- **Selector `.explorer-sector`**: `transition: opacity var(--wheel-fade-duration, .18s) ease-out` extracted from `departmentofemotions-com` stylesheet.
- **Selector `.wheel-strokes`**: `transition: opacity var(--wheel-fade-duration, .18s) ease-out` extracted from `departmentofemotions-com` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none!important` extracted from `departmentofemotions-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<nav.lab-switcher>` and `<section.wheel-workspace>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.explorer-page>` and `<section.wheel-workspace>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `departmentofemotions-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
