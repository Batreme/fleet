---
title: "UI Prompt Blueprint: tej-as_story"
date: 2026-11-15
target: "[[overview|tej-as_story]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0708` / `#4a4441`)"
---

# UI Design System & Master Generation Blueprint: tej-as_story

> **The testimony and autobiography of Tejas Kumar** (https://tej.as/story) — Tejas Kumar died at 4 and was revived, got about 19 days of school a year, and is now an AI engineer at IBM. His full testimony, in 39 ch...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/tej-as_story/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The testimony and autobiography of Tejas Kumar** (`https://tej.as/story`). Tejas Kumar died at 4 and was revived, got about 19 days of school a year, and is now an AI engineer at IBM. His full testimony, in 39 ch...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0708` / `#4a4441`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0a0708` (`var(--void)` in `:root`) paired with `#f2efe9` primary typography and `#4a4441` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jost` for display copy (`The thread .`) with `Switzer` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .375rem`, padding `.5rem`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/tej-as_story/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `tej-as_story` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `.375rem` grid gap.
- **Border Radius Scale**: `.25rem`, `1rem`, `2px`, `var(--r-1)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .375rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=640px)`, `@media (width>=768px)`, `@media (width>=1024px)`, `@media (width>=1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0708` | `var(--void)` in `:root` |
| **Primary Typography Ink** | `#161012` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2a2426` | `var(--rule-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#4a4441` | `var(--rule-dark-lit)` in `:root` |
| **Secondary / Muted Copy** | `#f2efe9` | `var(--bone)` in `:root` |
| **Structural Hairline Border** | `#a39b98` | `var(--ash)` in `:root` |
| **Variable Token (`--ash-dim`)** | `#8c8481` | `var(--ash-dim)` in `:root` |
| **Variable Token (`--paper`)** | `#f4f1ea` | `var(--paper)` in `:root` |
| **Variable Token (`--paper-2`)** | `#e8e4da` | `var(--paper-2)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent` | `var(--on-red)` | Brand / Palette Token |
| `--fg-2` | `var(--on-red-2)` | Typography Ink Token |
| `--fg-3` | `var(--on-red-2)` | Typography Ink Token |
| `--fg` | `var(--on-red)` | Typography Ink Token |
| `--focus` | `var(--on-red)` | Design System Custom Token |
| `--gold-fg` | `var(--gold)` | Typography Ink Token |
| `--mark` | `var(--gold)` | Design System Custom Token |
| `--void` | `#0a0708` | Color / Atmospheric Token |
| `--ink` | `#161012` | Typography Ink Token |
| `--rule-dark` | `#2a2426` | Canvas / Surface Token |
| `--rule-dark-lit` | `#4a4441` | Canvas / Surface Token |
| `--bone` | `#f2efe9` | Color / Atmospheric Token |
| `--ash` | `#a39b98` | Color / Atmospheric Token |
| `--ash-dim` | `#8c8481` | Color / Atmospheric Token |
| `--paper` | `#f4f1ea` | Canvas / Surface Token |
| `--paper-2` | `#e8e4da` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Jost`.
- **Primary Body Stack**: `Switzer`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Jost", "Futura", "Century Gothic", "Trebuchet MS", system-ui, sans-serif`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`).
- **Body Copy**: CSS variables `--font-body: "Switzer", "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif`, `--t-body: clamp(1.125rem, 1.3vw, 1.3125rem)`, `--lh-body: 1.62`.
- **Metadata & Navigation Labels**: CSS variables `--fg-label: color-mix(in srgb, var(--fg-2) 72%, var(--fg))`, `--font-mono: "Geist Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--t-small: clamp(.9375rem, 1vw, 1rem)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: .15s` extracted from `tej-as_story` stylesheet.
- **Selector `.transition-colors`**: `transition: .15s` extracted from `tej-as_story` stylesheet.
- **Selector `.transition-opacity`**: `transition: .15s` extracted from `tej-as_story` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.summary>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The testimony and autobiography of Tejas K │
│ ====================================================================== │
│ [ <header.topbar>          | Speaking · Story · Podcast · Blog · Bo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: The thread .                                                 |   │
│ | Substrate: #0a0708    | Ink: #f2efe9    | Accent: #4a4441        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.summary>         ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The short version.           |  | Contents                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .375re) | │
│ | [<header.topbar>] -> [<section.relative>] -> [<section.summary>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-t>     ) | https://tej.as/story               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.topbar> — `tej-as_story`)**:
   - Landmark `<header class="topbar">` hosting `The testimony and autobiography of T` navigation (`Speaking · Story · Podcast · Blog · Book Fluent React`), DOM attributes (`data-theme="light"`, `data-track="Nav Click"`, `data-track-label="Wordmark"`, `data-track-href="/"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `The thread .`)**:
   - Landmark `<section class="relative isolate">` presenting display lead `The thread .` and copy excerpt *"More Speaking Talks, topics and fees Calendar Where I'll be next "* over `#0a0708` canvas and `#f2efe9` ink.
3. **Primary Showcase & Content Grid (<section.summary> — `The short version.`)**:
   - Landmark `<section class="summary">` rendering section `The short version.` with copy *"Speaking Talks, topics and fees"*, asset references (`favicon.svg`, `story`, `array.js`, `jost-var.woff2`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.border-t> — `Contents`)**:
   - Landmark `<section class="border-t border-hairline">` framing `Contents` and `Before` (*"Talks, topics and fees"*) with `#2a2426` surface cards, `#4a4441` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://tej.as/story`)**:
   - Landmark `<footer class="border-t border-hairline">` anchoring `The testimony and autobiography ` footer links (`Speaking · Story · Podcast · Blog · Book Fluent React`), copy *"Calendar Where I'll be next"*, and `#a39b98` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tej-as_story (The testimony and autobiography of Tejas Kumar)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tej-as_story` (**The testimony and autobiography of Tejas Kumar** — `https://tej.as/story`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0708` / `#4a4441`).
- **Identity & Domain Context**: Tejas Kumar died at 4 and was revived, got about 19 days of school a year, and is now an AI engineer at IBM. His full testimony, in 39 ch...
- **Primary Substrate**: `#0a0708` (`var(--void)` in `:root`), **Primary Ink**: `#f2efe9`, **Accent / Highlight**: `#4a4441`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0a0708` (`var(--void)` in `:root`) paired with `#f2efe9` primary typography and `#4a4441` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jost` for display copy (`The thread .`) with `Switzer` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .375rem`, padding `.5rem`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tej-as_story` in your global stylesheet:

:root {
  /* The testimony and autobiography of Tejas Kumar (tej-as_story) — Ground-Truth Extracted CSS Variables */
  --accent: var(--on-red); /* Brand / Palette Token (tej-as_story) */
  --fg-2: var(--on-red-2); /* Typography Ink Token (tej-as_story) */
  --fg-3: var(--on-red-2); /* Typography Ink Token (tej-as_story) */
  --fg: var(--on-red); /* Typography Ink Token (tej-as_story) */
  --focus: var(--on-red); /* Design System Custom Token (tej-as_story) */
  --gold-fg: var(--gold); /* Typography Ink Token (tej-as_story) */
  --mark: var(--gold); /* Design System Custom Token (tej-as_story) */
  --void: #0a0708; /* Color / Atmospheric Token (tej-as_story) */
  --ink: #161012; /* Typography Ink Token (tej-as_story) */
  --rule-dark: #2a2426; /* Canvas / Surface Token (tej-as_story) */
  --rule-dark-lit: #4a4441; /* Canvas / Surface Token (tej-as_story) */
  --bone: #f2efe9; /* Color / Atmospheric Token (tej-as_story) */
  --ash: #a39b98; /* Color / Atmospheric Token (tej-as_story) */
  --ash-dim: #8c8481; /* Color / Atmospheric Token (tej-as_story) */
  --paper: #f4f1ea; /* Canvas / Surface Token (tej-as_story) */
  --paper-2: #e8e4da; /* Canvas / Surface Token (tej-as_story) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0a0708` — grounded in `var(--void)` in `:root`
- **Primary Typography Ink**: `#161012` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#2a2426` — grounded in `var(--rule-dark)` in `:root`
- **Interactive Accent / Highlight**: `#4a4441` — grounded in `var(--rule-dark-lit)` in `:root`
- **Secondary / Muted Copy**: `#f2efe9` — grounded in `var(--bone)` in `:root`
- **Structural Hairline Border**: `#a39b98` — grounded in `var(--ash)` in `:root`
- **Variable Token (`--ash-dim`)**: `#8c8481` — grounded in `var(--ash-dim)` in `:root`
- **Variable Token (`--paper`)**: `#f4f1ea` — grounded in `var(--paper)` in `:root`
- **Variable Token (`--paper-2`)**: `#e8e4da` — grounded in `var(--paper-2)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `tej-as_story` stylesheet
- **Padding & Gutters**: `.5rem` lateral canvas padding with `.375rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .375rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (width>=640px)`, `@media (width>=768px)`, `@media (width>=1024px)`, `@media (width>=1280px)`
- **Corner Radii**: `.25rem`, `1rem`, `2px`, `var(--r-1)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Switzer`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: CSS variables `--font-display: "Jost", "Futura", "Century Gothic", "Trebuchet MS", system-ui, sans-serif`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Body Copy Rule**: CSS variables `--font-body: "Switzer", "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif`, `--t-body: clamp(1.125rem, 1.3vw, 1.3125rem)`, `--lh-body: 1.62`
- **Metadata & Index Rule**: CSS variables `--fg-label: color-mix(in srgb, var(--fg-2) 72%, var(--fg))`, `--font-mono: "Geist Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--t-small: clamp(.9375rem, 1vw, 1rem)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tej-as_story` (`The testimony and autobiography of Tejas Kumar`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.topbar> — `tej-as_story`)**:
   - DOM & Selectors: Landmark `<header class="topbar">` hosting `The testimony and autobiography of T` navigation (`Speaking · Story · Podcast · Blog · Book Fluent React`), DOM attributes (`data-theme="light"`, `data-track="Nav Click"`, `data-track-label="Wordmark"`, `data-track-href="/"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.topbar> — `tej-as_story`)` (`tej-as_story`) adapts across `@media (width>=640px)`, `@media (width>=768px)`, `@media (width>=1024px)`, `@media (width>=1280px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Speaking · Story · Podcast · Blog · Book Fluent React`.
2. **Hero Stage & Focal Lead (<section.relative> — `The thread .`)**:
   - DOM & Selectors: Landmark `<section class="relative isolate">` presenting display lead `The thread .` and copy excerpt *"More Speaking Talks, topics and fees Calendar Where I'll be next "* over `#0a0708` canvas and `#f2efe9` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0a0708` background with `#f2efe9` headline `The thread .`.
3. **Primary Showcase & Content Grid (<section.summary> — `The short version.`)**:
   - DOM & Selectors: Landmark `<section class="summary">` rendering section `The short version.` with copy *"Speaking Talks, topics and fees"*, asset references (`favicon.svg`, `story`, `array.js`, `jost-var.woff2`), and grid rule `body { line-height:inherit;margin:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.summary> — `The short version.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .375rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.border-t> — `Contents`)**:
   - DOM & Selectors: Landmark `<section class="border-t border-hairline">` framing `Contents` and `Before` (*"Talks, topics and fees"*) with `#2a2426` surface cards, `#4a4441` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.border-t> — `Contents`)` uses `.25rem`, `1rem`, `2px`, `var(--r-1)` radii, `#4a4441` highlights, and assets (favicon.svg, story, array.js).
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://tej.as/story`)**:
   - DOM & Selectors: Landmark `<footer class="border-t border-hairline">` anchoring `The testimony and autobiography ` footer links (`Speaking · Story · Podcast · Blog · Book Fluent React`), copy *"Calendar Where I'll be next"*, and `#a39b98` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.border-t> — `https://tej.as/story`)` aligns to `640px` extracted from `tej-as_story` stylesheet with `.5rem` lateral canvas padding with `.375rem` grid gap and attributes (data-theme="light", data-track="Nav Click", data-track-label="Wordmark").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"More Speaking Talks, topics and fees Calendar Where I'll be next Workshops I teach..."*
- Copy Excerpt 2: *"Speaking Talks, topics and fees"*
- Copy Excerpt 3: *"Talks, topics and fees"*
- Copy Excerpt 4: *"Calendar Where I'll be next"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`tej-as_story`)**:
- `after { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { line-height:inherit;margin:0 }`
- `strong { font-weight:bolder }`
- `pre { font-family:var(--font-mono);font-feature-settings:normal;font-variation... }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: .15s` extracted from `tej-as_story` stylesheet.
- **Selector `.transition-colors`**: `transition: .15s` extracted from `tej-as_story` stylesheet.
- **Selector `.transition-opacity`**: `transition: .15s` extracted from `tej-as_story` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.summary>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tej-as_story`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
