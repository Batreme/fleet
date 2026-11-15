---
title: "UI Prompt Blueprint: mindofakira-com"
date: 2026-11-15
target: "mindofakira-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0c0b0f` / `#8f8b98`)"
---

# UI Design System & Master Generation Blueprint: mindofakira-com

> **Mind of Akira** (http://mindofakira.com) — Mind of Akira: graphic designer working where streetwear, gaming culture and music meet. Branding, apparel, cover art, type and streaming...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Mind of Akira** (`http://mindofakira.com`). Mind of Akira: graphic designer working where streetwear, gaming culture and music meet. Branding, apparel, cover art, type and streaming...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0c0b0f` / `#8f8b98`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0c0b0f` (`var(--bg)` in `:root`) paired with `#f4f3ff` primary typography and `#8f8b98` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Mind of Akira`) with `JetBrains Mono` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `760px` container bounds (`gap: 12px`, padding `var(--gut)`) with `cubic-bezier(.2,.7,.1,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `760px` extracted from `mindofakira-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--gut)` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `50%`, `99px`, `3px`, `10px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 760px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 760px)`, `@media (max-width: 480px)`, `@media (max-width: 800px)`, `@media (max-width: 560px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0c0b0f` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#15131a` | `var(--bg-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ecebe4` | `var(--fg)` in `:root` |
| **Interactive Accent / Highlight** | `#8f8b98` | `var(--muted)` in `:root` |
| **Secondary / Muted Copy** | `#5b6bff` | `var(--accent)` in `:root` |
| **Structural Hairline Border** | `#f4f3ff` | `var(--accent-ink)` in `:root` |
| **Variable Token (`--vinyl`)** | `#050407` | `var(--vinyl)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0c0b0f` | Canvas / Surface Token |
| `--bg-2` | `#15131a` | Canvas / Surface Token |
| `--fg` | `#ecebe4` | Typography Ink Token |
| `--muted` | `#8f8b98` | Color / Atmospheric Token |
| `--line` | `rgba(236, 235, 228, 0.14)` | Color / Atmospheric Token |
| `--accent` | `#5b6bff` | Brand / Palette Token |
| `--accent-ink` | `#f4f3ff` | Typography Ink Token |
| `--vinyl` | `#050407` | Color / Atmospheric Token |
| `--f-display` | `"Archivo", "Arial Black", "Helvetica Neue", Arial, sans-serif` | Dimension / Scale Token |
| `--f-body` | `"Archivo", "Helvetica Neue", Arial, sans-serif` | Dimension / Scale Token |
| `--f-mono` | `"JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace` | Typography / Scale Token |
| `--s-1` | `clamp(0.75rem, 0.7rem + 0.2vw, 0.8125rem)` | Dimension / Scale Token |
| `--s0` | `clamp(1rem, 0.95rem + 0.25vw, 1.125rem)` | Dimension / Scale Token |
| `--s1` | `clamp(1.375rem, 1.1rem + 1.2vw, 2rem)` | Dimension / Scale Token |
| `--s2` | `clamp(2rem, 1.3rem + 3.2vw, 4rem)` | Dimension / Scale Token |
| `--s3` | `clamp(3.2rem, 1rem + 10vw, 11rem)` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `JetBrains Mono`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--f-display: "Archivo", "Arial Black", "Helvetica Neue", Arial, sans-serif`; rule `h1` (`font-size: var(--s1)`, `line-height: 1.15`, `letter-spacing: -0.01em`, `font-weight: 500`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--s1)`, `letter-spacing: -0.01em`, `font-weight: 700`).
- **Body Copy**: CSS variables `--f-body: "Archivo", "Helvetica Neue", Arial, sans-serif`; rule `body` (`font-size: var(--s0)`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: CSS variables `--f-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace`; rule `.mono` (`font-size: var(--s-1)`, `letter-spacing: 0.04em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.3,1.6,.5,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `body`**: `transition: background-color .5s var(--ease), color .5s var(--ease)` extracted from `mindofakira-com` stylesheet.
- **Selector `.gate`**: `transition: clip-path 1.1s cubic-bezier(.2,.7,.1,1)` extracted from `mindofakira-com` stylesheet.
- **Selector `.nav a::after`**: `transition: transform .4s var(--ease)` extracted from `mindofakira-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.1,1)`)**: Governs interactive state transitions across `<header.top>` and `<section.intro>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Mind of Akira                              │
│ ====================================================================== │
│ [ <header.top>             | Work · About · Services · Contact      ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Mind of Akira                                                |   │
│ | Substrate: #0c0b0f    | Ink: #f4f3ff    | Accent: #8f8b98        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.intro>           ) max-w: 760px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Visuals for streetwear, gami |  | Photoshop and Illustrator, c | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.top>] -> [<section.hero>] -> [<section.intro>] |            │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.foot>         ) | http://mindofakira.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.top> — `mindofakira-com`)**:
   - Landmark `<header class="top">` hosting `Mind of Akira` navigation (`Work · About · Services · Contact`), DOM attributes (`data-cursor="Play"`, `data-cursor="Enter"`, `data-cursor="Go"`, `data-cursor="Go"`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Mind of Akira`)**:
   - Landmark `<section class="hero">` presenting display lead `Mind of Akira` and copy excerpt *"MOA-001 Side A / Side B ℗ 2026"* over `#0c0b0f` canvas and `#f4f3ff` ink.
3. **Primary Showcase & Content Grid (<section.intro> — `Visuals for streetwear, gaming and`)**:
   - Landmark `<section class="intro wrap">` rendering section `Visuals for streetwear, gaming and music that fee...` with copy *"Best experienced with sound on"*, asset references (`favicon.svg`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }`.
4. **Interactive Detail & Feature Matrix (<article.tape-note> — `Photoshop and Illustrator, cracked`)**:
   - Landmark `<article class="tape-note">` framing `Photoshop and Illustrator, cracked open.` and `Mind of Akira starts.` (*"Enter with sound ♪"*) with `#ecebe4` surface cards, `#8f8b98` accents, and `canvas { max-width: 100%; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `http://mindofakira.com`)**:
   - Landmark `<footer class="foot wrap">` anchoring `Mind of Akira` footer links (`Work · About · Services · Contact`), copy *"Enter without sound"*, and `#f4f3ff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: mindofakira-com (Mind of Akira)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `mindofakira-com` (**Mind of Akira** — `http://mindofakira.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0c0b0f` / `#8f8b98`).
- **Identity & Domain Context**: Mind of Akira: graphic designer working where streetwear, gaming culture and music meet. Branding, apparel, cover art, type and streaming...
- **Primary Substrate**: `#0c0b0f` (`var(--bg)` in `:root`), **Primary Ink**: `#f4f3ff`, **Accent / Highlight**: `#8f8b98`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0c0b0f` (`var(--bg)` in `:root`) paired with `#f4f3ff` primary typography and `#8f8b98` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Mind of Akira`) with `JetBrains Mono` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `760px` container bounds (`gap: 12px`, padding `var(--gut)`) with `cubic-bezier(.2,.7,.1,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `mindofakira-com` in your global stylesheet:

:root {
  /* Mind of Akira (mindofakira-com) — Ground-Truth Extracted CSS Variables */
  --bg: #0c0b0f; /* Canvas / Surface Token (mindofakira-com) */
  --bg-2: #15131a; /* Canvas / Surface Token (mindofakira-com) */
  --fg: #ecebe4; /* Typography Ink Token (mindofakira-com) */
  --muted: #8f8b98; /* Color / Atmospheric Token (mindofakira-com) */
  --line: rgba(236, 235, 228, 0.14); /* Color / Atmospheric Token (mindofakira-com) */
  --accent: #5b6bff; /* Brand / Palette Token (mindofakira-com) */
  --accent-ink: #f4f3ff; /* Typography Ink Token (mindofakira-com) */
  --vinyl: #050407; /* Color / Atmospheric Token (mindofakira-com) */
  --f-display: "Archivo", "Arial Black", "Helvetica Neue", Arial, sans-serif; /* Dimension / Scale Token (mindofakira-com) */
  --f-body: "Archivo", "Helvetica Neue", Arial, sans-serif; /* Dimension / Scale Token (mindofakira-com) */
  --f-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace; /* Typography / Scale Token (mindofakira-com) */
  --s-1: clamp(0.75rem, 0.7rem + 0.2vw, 0.8125rem); /* Dimension / Scale Token (mindofakira-com) */
  --s0: clamp(1rem, 0.95rem + 0.25vw, 1.125rem); /* Dimension / Scale Token (mindofakira-com) */
  --s1: clamp(1.375rem, 1.1rem + 1.2vw, 2rem); /* Dimension / Scale Token (mindofakira-com) */
  --s2: clamp(2rem, 1.3rem + 3.2vw, 4rem); /* Dimension / Scale Token (mindofakira-com) */
  --s3: clamp(3.2rem, 1rem + 10vw, 11rem); /* Dimension / Scale Token (mindofakira-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0c0b0f` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#15131a` — grounded in `var(--bg-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#ecebe4` — grounded in `var(--fg)` in `:root`
- **Interactive Accent / Highlight**: `#8f8b98` — grounded in `var(--muted)` in `:root`
- **Secondary / Muted Copy**: `#5b6bff` — grounded in `var(--accent)` in `:root`
- **Structural Hairline Border**: `#f4f3ff` — grounded in `var(--accent-ink)` in `:root`
- **Variable Token (`--vinyl`)**: `#050407` — grounded in `var(--vinyl)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `760px` extracted from `mindofakira-com` stylesheet
- **Padding & Gutters**: `var(--gut)` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 760px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding
- **Media Queries**: `@media (max-width: 760px)`, `@media (max-width: 480px)`, `@media (max-width: 800px)`, `@media (max-width: 560px)`
- **Corner Radii**: `50%`, `99px`, `3px`, `10px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: CSS variables `--f-display: "Archivo", "Arial Black", "Helvetica Neue", Arial, sans-serif`; rule `h1` (`font-size: var(--s1)`, `line-height: 1.15`, `letter-spacing: -0.01em`, `font-weight: 500`)
- **H2 Section Rule**: rule `h2` (`font-size: var(--s1)`, `letter-spacing: -0.01em`, `font-weight: 700`)
- **Body Copy Rule**: CSS variables `--f-body: "Archivo", "Helvetica Neue", Arial, sans-serif`; rule `body` (`font-size: var(--s0)`, `line-height: 1.5`)
- **Metadata & Index Rule**: CSS variables `--f-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace`; rule `.mono` (`font-size: var(--s-1)`, `letter-spacing: 0.04em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `mindofakira-com` (`Mind of Akira`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.top> — `mindofakira-com`)**:
   - DOM & Selectors: Landmark `<header class="top">` hosting `Mind of Akira` navigation (`Work · About · Services · Contact`), DOM attributes (`data-cursor="Play"`, `data-cursor="Enter"`, `data-cursor="Go"`, `data-cursor="Go"`), and stylesheet rule `after { box-sizing: border-box; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.top> — `mindofakira-com`)` (`mindofakira-com`) adapts across `@media (max-width: 760px)`, `@media (max-width: 480px)`, `@media (max-width: 800px)`, `@media (max-width: 560px)` with `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.3,1.6,.5,1)` transitions and links `Work · About · Services · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Mind of Akira`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Mind of Akira` and copy excerpt *"MOA-001 Side A / Side B ℗ 2026"* over `#0c0b0f` canvas and `#f4f3ff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0c0b0f` background with `#f4f3ff` headline `Mind of Akira`.
3. **Primary Showcase & Content Grid (<section.intro> — `Visuals for streetwear, gaming and`)**:
   - DOM & Selectors: Landmark `<section class="intro wrap">` rendering section `Visuals for streetwear, gaming and music that fee...` with copy *"Best experienced with sound on"*, asset references (`favicon.svg`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.intro> — `Visuals for streetwear, gaming and`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 760px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.tape-note> — `Photoshop and Illustrator, cracked`)**:
   - DOM & Selectors: Landmark `<article class="tape-note">` framing `Photoshop and Illustrator, cracked open.` and `Mind of Akira starts.` (*"Enter with sound ♪"*) with `#ecebe4` surface cards, `#8f8b98` accents, and `canvas { max-width: 100%; display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.tape-note> — `Photoshop and Illustrator, cracked`)` uses `50%`, `99px`, `3px`, `10px` radii, `#8f8b98` highlights, and assets (favicon.svg, fonts.googleapis.com, fonts.gstatic.com).
5. **Colophon & Global Directory Footer (<footer.foot> — `http://mindofakira.com`)**:
   - DOM & Selectors: Landmark `<footer class="foot wrap">` anchoring `Mind of Akira` footer links (`Work · About · Services · Contact`), copy *"Enter without sound"*, and `#f4f3ff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.foot> — `http://mindofakira.com`)` aligns to `760px` extracted from `mindofakira-com` stylesheet with `var(--gut)` lateral canvas padding with `12px` grid gap and attributes (data-cursor="Play", data-cursor="Enter", data-cursor="Go").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"MOA-001 Side A / Side B ℗ 2026"*
- Copy Excerpt 2: *"Best experienced with sound on"*
- Copy Excerpt 3: *"Enter with sound ♪"*
- Copy Excerpt 4: *"Enter without sound"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.3,1.6,.5,1)`
- **Extracted Stylesheet Rules (`mindofakira-com`)**:
- `after { box-sizing: border-box; }`
- `html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }`
- `canvas { max-width: 100%; display: block; }`
- `button { font: inherit; color: inherit; }`
- `selection { background: var(--accent); color: var(--accent-ink); }`
- **Per-Selector Transition Rules**:
- **Selector `body`**: `transition: background-color .5s var(--ease), color .5s var(--ease)` extracted from `mindofakira-com` stylesheet.
- **Selector `.gate`**: `transition: clip-path 1.1s cubic-bezier(.2,.7,.1,1)` extracted from `mindofakira-com` stylesheet.
- **Selector `.nav a::after`**: `transition: transform .4s var(--ease)` extracted from `mindofakira-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.1,1)`)**: Governs interactive state transitions across `<header.top>` and `<section.intro>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `mindofakira-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
