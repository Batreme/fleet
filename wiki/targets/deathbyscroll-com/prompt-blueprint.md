---
title: "UI Prompt Blueprint: deathbyscroll-com"
date: 2026-11-15
target: "[[overview|deathbyscroll-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#111` / `#777`)"
---

# UI Design System & Master Generation Blueprint: deathbyscroll-com

> **Death by Scroll** (https://deathbyscroll.com) — Killer scroll animation. Perfect for product launches, microsites, and explainers. Create a cult-like devotion to your brand.

![Desktop Viewport Capture (1440x32360)](file:///root/projects/fleet/wiki/targets/deathbyscroll-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Death by Scroll** (`https://deathbyscroll.com`). Killer scroll animation. Perfect for product launches, microsites, and explainers. Create a cult-like devotion to your brand.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#111` / `#777`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#111` (`var(--color-off-black)` in `:root`) paired with `#f4efed` primary typography and `#777` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Aesteric` for display copy (`Death by Scroll. Killer scroll anima`) with `Girthy` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 1.5rem`, padding `.75rem`) with `cubic-bezier(0.2,1,0.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/deathbyscroll-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×32360px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `767px` extracted from `deathbyscroll-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.75rem` lateral canvas padding with `1.5rem` grid gap.
- **Border Radius Scale**: `6px`, `0px`, `1.25rem`, `var(--corner-fallback-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 1.5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:768px)`, `@media screen and (min-width:1600px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (min-width:1020px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111` | `var(--color-off-black)` in `:root` |
| **Primary Typography Ink** | `#282828` | `var(--color-medium-grey)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1e1e1e` | `var(--color-dark-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#777` | `var(--color-light-grey)` in `:root` |
| **Secondary / Muted Copy** | `#f4efed` | `var(--color-off-white)` in `:root` |
| **Structural Hairline Border** | `#e8e8e8` | `var(--color-highlight)` in `:root` |
| **Variable Token (`--color-red`)** | `#d52127` | `var(--color-red)` in `:root` |
| **Variable Token (`--color-purple`)** | `#ae5eff` | `var(--color-purple)` in `:root` |
| **Variable Token (`--color-red-muted`)** | `#ff5e5e` | `var(--color-red-muted)` in `:root` |
| **Variable Token (`--color-red-white`)** | `#fad2d2` | `var(--color-red-white)` in `:root` |
| **Variable Token (`--color-green`)** | `#4cc44c` | `var(--color-green)` in `:root` |
| **Variable Token (`--color-shadow-2`)** | `#212121` | `var(--color-shadow-2)` in `:root` |
| **Variable Token (`--color-shadow-3`)** | `#222` | `var(--color-shadow-3)` in `:root` |
| **Variable Token (`--color-brass`)** | `#f9de95` | `var(--color-brass)` in `:root` |
| **Variable Token (`--color-brass-dark`)** | `#e7b882` | `var(--color-brass-dark)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-off-black` | `#111` | Canvas / Surface Token |
| `--color-medium-grey` | `#282828` | Brand / Palette Token |
| `--color-dark-grey` | `#1e1e1e` | Canvas / Surface Token |
| `--color-light-grey` | `#777` | Canvas / Surface Token |
| `--color-off-white` | `#f4efed` | Canvas / Surface Token |
| `--color-highlight` | `#e8e8e8` | Canvas / Surface Token |
| `--color-red` | `#d52127` | Brand / Palette Token |
| `--color-purple` | `#ae5eff` | Brand / Palette Token |
| `--color-red-rgb` | `213,33,39` | Brand / Palette Token |
| `--color-red-muted` | `#ff5e5e` | Brand / Palette Token |
| `--color-red-white` | `#fad2d2` | Canvas / Surface Token |
| `--color-green` | `#4cc44c` | Brand / Palette Token |
| `--color-shadow-2` | `#212121` | Brand / Palette Token |
| `--color-shadow-3` | `#222` | Brand / Palette Token |
| `--color-brass` | `#f9de95` | Brand / Palette Token |
| `--color-brass-dark` | `#e7b882` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Aesteric`.
- **Primary Body Stack**: `Girthy`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-size--h1: 2.3125rem`, `--line-height--h1: 2.375rem`.
- **Section Heading (`H2`)**: CSS variables `--font-size--h2: 2.5rem`, `--line-height--h2: 3rem`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.2`, `letter-spacing: 2px`, `font-weight: 600`).
- **Body Copy**: CSS variables `--typeface-body: "Setanz",serif`, `--typeface-body-bold: "Satoshi Black",sans-serif`, `--line-height--body: 1.375rem`; rule `p` (`font-size: 1rem`, `line-height: 1.25rem`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `1em`, `80%`, `75%`, `100%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.2,1,0.3,1)`, `cubic-bezier(.2,1,.3,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `:root`**: `transition: var(--global-duration) var(--global-timing)` extracted from `deathbyscroll-com` stylesheet.
- **Selector `.outline-text span:after`**: `transition: opacity .3s ease` extracted from `deathbyscroll-com` stylesheet.
- **Selector `a svg`**: `transition: fill .5s cubic-bezier(0.2,1,0.3,1)` extracted from `deathbyscroll-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,1,0.3,1)`)**: Governs interactive state transitions across `<header.dxs-header>` and `<section.temple-scene>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Death by Scroll                            │
│ ====================================================================== │
│ [ <header.dxs-header>      | Summon us Summon us                    ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.guided-player>                              |   │
│ | H1: Death by Scroll. Killer scroll animation                     |   │
│ | Substrate: #111       | Ink: #f4efed    | Accent: #777           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.temple-scene>    ) max-w: 767px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Scene player                 |  | Don't just get people's atte | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1.5rem) | │
│ | [<header.dxs-header] -> [<section.guided-pl] -> [<section.temple-sc] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.dxs-footer>   ) | https://deathbyscroll.com          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.dxs-header> — `deathbyscroll-com`)**:
   - Landmark `<header class="dxs-header">` hosting `Death by Scroll` navigation (`Summon us Summon us`), DOM attributes (`data-open-accessibility="accessibility-toggle-..."`, `data-end-announce="Summon Us. The page n..."`, `data-guided="prev"`, `data-guided="playpause"`), and stylesheet rule `root { --font-size--h1:5.375rem;--font-size--h2:4rem;--line-height--h1:5.375rem... }`.
2. **Hero Stage & Focal Lead (<section.guided-player> — `Death by Scroll. Killer scroll ani`)**:
   - Landmark `<section class="guided-player">` presenting display lead `Death by Scroll. Killer scroll animation` and copy excerpt *"Accessibility options"* over `#111` canvas and `#f4efed` ink.
3. **Primary Showcase & Content Grid (<section.temple-scene> — `Scene player`)**:
   - Landmark `<section class="temple-scene">` rendering section `Scene player` with copy *"The Offering The Offering"*, asset references (`tg-girthyultra-webfont.woff2`, `Satoshi-Bold.woff2`, `styles.min.css`, `favicon.png`), and grid rule `html { -webkit-text-size-adjust:100%;line-height:1.15 }`.
4. **Interactive Detail & Feature Matrix (<section.heads-scene> — `Don't just get people's attention,`)**:
   - Landmark `<section class="heads-scene">` framing `Don't just get people's attention, get inside the...` and `Don't Don't just just get get people's people's a...` (*"Death Scrolls Death Scrolls"*) with `#1e1e1e` surface cards, `#777` accents, and `main { display:block }`.
5. **Colophon & Global Directory Footer (<footer.dxs-footer> — `https://deathbyscroll.com`)**:
   - Landmark `<footer class="dxs-footer">` anchoring `Death by Scroll` footer links (`Summon us Summon us`), copy *"Summon us Summon us"*, and `#e8e8e8` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: deathbyscroll-com (Death by Scroll)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `deathbyscroll-com` (**Death by Scroll** — `https://deathbyscroll.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#111` / `#777`).
- **Identity & Domain Context**: Killer scroll animation. Perfect for product launches, microsites, and explainers. Create a cult-like devotion to your brand.
- **Primary Substrate**: `#111` (`var(--color-off-black)` in `:root`), **Primary Ink**: `#f4efed`, **Accent / Highlight**: `#777`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#111` (`var(--color-off-black)` in `:root`) paired with `#f4efed` primary typography and `#777` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Aesteric` for display copy (`Death by Scroll. Killer scroll anima`) with `Girthy` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 1.5rem`, padding `.75rem`) with `cubic-bezier(0.2,1,0.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `deathbyscroll-com` in your global stylesheet:

:root {
  /* Death by Scroll (deathbyscroll-com) — Ground-Truth Extracted CSS Variables */
  --color-off-black: #111; /* Canvas / Surface Token (deathbyscroll-com) */
  --color-medium-grey: #282828; /* Brand / Palette Token (deathbyscroll-com) */
  --color-dark-grey: #1e1e1e; /* Canvas / Surface Token (deathbyscroll-com) */
  --color-light-grey: #777; /* Canvas / Surface Token (deathbyscroll-com) */
  --color-off-white: #f4efed; /* Canvas / Surface Token (deathbyscroll-com) */
  --color-highlight: #e8e8e8; /* Canvas / Surface Token (deathbyscroll-com) */
  --color-red: #d52127; /* Brand / Palette Token (deathbyscroll-com) */
  --color-purple: #ae5eff; /* Brand / Palette Token (deathbyscroll-com) */
  --color-red-rgb: 213,33,39; /* Brand / Palette Token (deathbyscroll-com) */
  --color-red-muted: #ff5e5e; /* Brand / Palette Token (deathbyscroll-com) */
  --color-red-white: #fad2d2; /* Canvas / Surface Token (deathbyscroll-com) */
  --color-green: #4cc44c; /* Brand / Palette Token (deathbyscroll-com) */
  --color-shadow-2: #212121; /* Brand / Palette Token (deathbyscroll-com) */
  --color-shadow-3: #222; /* Brand / Palette Token (deathbyscroll-com) */
  --color-brass: #f9de95; /* Brand / Palette Token (deathbyscroll-com) */
  --color-brass-dark: #e7b882; /* Canvas / Surface Token (deathbyscroll-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#111` — grounded in `var(--color-off-black)` in `:root`
- **Primary Typography Ink**: `#282828` — grounded in `var(--color-medium-grey)` in `:root`
- **Elevated Surface / Card Substrate**: `#1e1e1e` — grounded in `var(--color-dark-grey)` in `:root`
- **Interactive Accent / Highlight**: `#777` — grounded in `var(--color-light-grey)` in `:root`
- **Secondary / Muted Copy**: `#f4efed` — grounded in `var(--color-off-white)` in `:root`
- **Structural Hairline Border**: `#e8e8e8` — grounded in `var(--color-highlight)` in `:root`
- **Variable Token (`--color-red`)**: `#d52127` — grounded in `var(--color-red)` in `:root`
- **Variable Token (`--color-purple`)**: `#ae5eff` — grounded in `var(--color-purple)` in `:root`
- **Variable Token (`--color-red-muted`)**: `#ff5e5e` — grounded in `var(--color-red-muted)` in `:root`
- **Variable Token (`--color-red-white`)**: `#fad2d2` — grounded in `var(--color-red-white)` in `:root`
- **Variable Token (`--color-green`)**: `#4cc44c` — grounded in `var(--color-green)` in `:root`
- **Variable Token (`--color-shadow-2`)**: `#212121` — grounded in `var(--color-shadow-2)` in `:root`
- **Variable Token (`--color-shadow-3`)**: `#222` — grounded in `var(--color-shadow-3)` in `:root`
- **Variable Token (`--color-brass`)**: `#f9de95` — grounded in `var(--color-brass)` in `:root`
- **Variable Token (`--color-brass-dark`)**: `#e7b882` — grounded in `var(--color-brass-dark)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×32360px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `767px` extracted from `deathbyscroll-com` stylesheet
- **Padding & Gutters**: `.75rem` lateral canvas padding with `1.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 1.5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding
- **Media Queries**: `@media screen and (min-width:768px)`, `@media screen and (min-width:1600px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (min-width:1020px)`
- **Corner Radii**: `6px`, `0px`, `1.25rem`, `var(--corner-fallback-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Aesteric`
- **Body Font Stack**: `Girthy`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-size--h1: 2.3125rem`, `--line-height--h1: 2.375rem`
- **H2 Section Rule**: CSS variables `--font-size--h2: 2.5rem`, `--line-height--h2: 3rem`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.2`, `letter-spacing: 2px`, `font-weight: 600`)
- **Body Copy Rule**: CSS variables `--typeface-body: "Setanz",serif`, `--typeface-body-bold: "Satoshi Black",sans-serif`, `--line-height--body: 1.375rem`; rule `p` (`font-size: 1rem`, `line-height: 1.25rem`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `1em`, `80%`, `75%`, `100%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `deathbyscroll-com` (`Death by Scroll`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.dxs-header> — `deathbyscroll-com`)**:
   - DOM & Selectors: Landmark `<header class="dxs-header">` hosting `Death by Scroll` navigation (`Summon us Summon us`), DOM attributes (`data-open-accessibility="accessibility-toggle-..."`, `data-end-announce="Summon Us. The page n..."`, `data-guided="prev"`, `data-guided="playpause"`), and stylesheet rule `root { --font-size--h1:5.375rem;--font-size--h2:4rem;--line-height--h1:5.375rem... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.dxs-header> — `deathbyscroll-com`)` (`deathbyscroll-com`) adapts across `@media screen and (min-width:768px)`, `@media screen and (min-width:1600px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (min-width:1020px)` with `cubic-bezier(0.2,1,0.3,1)`, `cubic-bezier(.2,1,.3,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Summon us Summon us`.
2. **Hero Stage & Focal Lead (<section.guided-player> — `Death by Scroll. Killer scroll ani`)**:
   - DOM & Selectors: Landmark `<section class="guided-player">` presenting display lead `Death by Scroll. Killer scroll animation` and copy excerpt *"Accessibility options"* over `#111` canvas and `#f4efed` ink.
   - Responsive Contract: Hero stage (`1440×32360px` desktop / `390×2400px` mobile) sets `#111` background with `#f4efed` headline `Death by Scroll. Killer scroll animation`.
3. **Primary Showcase & Content Grid (<section.temple-scene> — `Scene player`)**:
   - DOM & Selectors: Landmark `<section class="temple-scene">` rendering section `Scene player` with copy *"The Offering The Offering"*, asset references (`tg-girthyultra-webfont.woff2`, `Satoshi-Bold.woff2`, `styles.min.css`, `favicon.png`), and grid rule `html { -webkit-text-size-adjust:100%;line-height:1.15 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.temple-scene> — `Scene player`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 1.5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.heads-scene> — `Don't just get people's attention,`)**:
   - DOM & Selectors: Landmark `<section class="heads-scene">` framing `Don't just get people's attention, get inside the...` and `Don't Don't just just get get people's people's a...` (*"Death Scrolls Death Scrolls"*) with `#1e1e1e` surface cards, `#777` accents, and `main { display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.heads-scene> — `Don't just get people's attention,`)` uses `6px`, `0px`, `1.25rem`, `var(--corner-fallback-radius)` radii, `#777` highlights, and assets (tg-girthyultra-webfont.woff2, Satoshi-Bold.woff2, styles.min.css).
5. **Colophon & Global Directory Footer (<footer.dxs-footer> — `https://deathbyscroll.com`)**:
   - DOM & Selectors: Landmark `<footer class="dxs-footer">` anchoring `Death by Scroll` footer links (`Summon us Summon us`), copy *"Summon us Summon us"*, and `#e8e8e8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.dxs-footer> — `https://deathbyscroll.com`)` aligns to `767px` extracted from `deathbyscroll-com` stylesheet with `.75rem` lateral canvas padding with `1.5rem` grid gap and attributes (data-open-accessibility="accessibility-toggle-...", data-end-announce="Summon Us. The page n...", data-guided="prev").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Accessibility options"*
- Copy Excerpt 2: *"The Offering The Offering"*
- Copy Excerpt 3: *"Death Scrolls Death Scrolls"*
- Copy Excerpt 4: *"Summon us Summon us"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.2,1,0.3,1)`, `cubic-bezier(.2,1,.3,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`deathbyscroll-com`)**:
- `root { --font-size--h1:5.375rem;--font-size--h2:4rem;--line-height--h1:5.375rem... }`
- `html { -webkit-text-size-adjust:100%;line-height:1.15 }`
- `main { display:block }`
- `pre { font-family:monospace,monospace;font-size:1em }`
- `strong { font-weight:bolder }`
- **Per-Selector Transition Rules**:
- **Selector `:root`**: `transition: var(--global-duration) var(--global-timing)` extracted from `deathbyscroll-com` stylesheet.
- **Selector `.outline-text span:after`**: `transition: opacity .3s ease` extracted from `deathbyscroll-com` stylesheet.
- **Selector `a svg`**: `transition: fill .5s cubic-bezier(0.2,1,0.3,1)` extracted from `deathbyscroll-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,1,0.3,1)`)**: Governs interactive state transitions across `<header.dxs-header>` and `<section.temple-scene>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `deathbyscroll-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
