---
title: "UI Prompt Blueprint: findra-art"
date: 2026-11-15
target: "[[overview|findra-art]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f7` accent)"
---

# UI Design System & Master Generation Blueprint: findra-art

> **Findra: the AI character feed** (https://findra.art/) — Who is rising among AI characters on TikTok, Instagram, X and YouTube: what they look like, their legends and where to follow them.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/findra-art/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Findra: the AI character feed** (`https://findra.art/`). Who is rising among AI characters on TikTok, Instagram, X and YouTube: what they look like, their legends and where to follow them.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f7` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f5f5f7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Breaking`) with `Geist Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(0,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/findra-art/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `findra-art` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-2xl)`, `2147483647px`, `var(--radius-lg)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:63rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#09090b` | `var(--background)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f5f7` | `var(--foreground)` in `:root` |
| **Secondary / Muted Copy** | `#a1a1aa` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#141417` | `var(--surface)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--font-anton` | `"Anton", "Anton Fallback"` | Typography / Scale Token |
| `--font-permanent-marker` | `"Permanent Marker", "Permanent Marker Fallback"` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-anton), Impact, "Arial Narrow", sans-serif`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `findra-art` stylesheet.
- **Selector `scale\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `findra-art` stylesheet.
- **Selector `scale\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `findra-art` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<article.group>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.border-foreground>` and `<article.group>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Findra: the AI character feed              │
│ ====================================================================== │
│ [ <header.sticky>          | Feed · Magazine · Wire · Leaderboard · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.border-foreground>                          |   │
│ | H1: Breaking                                                     |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #f5f5f7        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.group>           ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Who’s rising                 |  | The week on Findra           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.sticky>] -> [<section.border-fo] -> [<article.group>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.text-muted>   ) | https://findra.art/                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sticky> — `findra-art`)**:
   - Landmark `<header class="sticky top-0">` hosting `Findra: the AI character feed` navigation (`Feed · Magazine · Wire · Leaderboard · 40 Under 40`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="1.6.1"`, `data-test="skip-to-content"`), and stylesheet rule `.u8MhCG_className { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.border-foreground> — `Breaking`)**:
   - Landmark `<section class="border-foreground flex">` presenting display lead `Breaking` and copy excerpt *"Don Nuger’s Instagram account is unavailable"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.group> — `Who’s rising`)**:
   - Landmark `<article class="group relative">` rendering section `Who’s rising` with copy *"The account could not be read on November 13 or this morning. It "*, asset references (`60143a72b8d6b7a7338339c64f9bcd8bb...`, `3f38907974d4f61e778b2b56d301ade05...`, `3qago8bg0x8_-.css`, `30qn3skk62nz8.js`), and grid rule `.u8MhCG_variable { --font-geist:"Geist", "Geist Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.border-border> — `The week on Findra`)**:
   - Landmark `<section class="border-border flex">` framing `The week on Findra` and `Latest story` (*"AI characters and the audiences they are building on TikTok, Inst"*) with `#09090b` surface cards, `#f5f5f7` accents, and `.mJqafq_className { font-family:Anton,Anton Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.text-muted> — `https://findra.art/`)**:
   - Landmark `<footer class="text-muted mx-auto">` anchoring `Findra: the AI character feed` footer links (`Feed · Magazine · Wire · Leaderboard · 40 Under 40`), copy *"adventurous ai cat character"*, and `#141417` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: findra-art (Findra: the AI character feed)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `findra-art` (**Findra: the AI character feed** — `https://findra.art/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f7` accent).
- **Identity & Domain Context**: Who is rising among AI characters on TikTok, Instagram, X and YouTube: what they look like, their legends and where to follow them.
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#f5f5f7`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f5f5f7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Breaking`) with `Geist Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(0,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `findra-art` in your global stylesheet:

:root {
  /* Findra: the AI character feed (findra-art) — Ground-Truth Extracted CSS Variables */
  --font-geist: "Geist", "Geist Fallback"; /* Typography / Scale Token (findra-art) */
  --font-anton: "Anton", "Anton Fallback"; /* Typography / Scale Token (findra-art) */
  --font-permanent-marker: "Permanent Marker", "Permanent Marker Fallback"; /* Typography / Scale Token (findra-art) */
  --color-black: #000; /* Canvas / Surface Token (findra-art) */
  --color-white: #fff; /* Canvas / Surface Token (findra-art) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (findra-art) */
  --container-xl: 36rem; /* Layout / Spatial Grid Token (findra-art) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (findra-art) */
  --container-6xl: 72rem; /* Layout / Spatial Grid Token (findra-art) */
  --text-xs: .75rem; /* Typography Ink Token (findra-art) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (findra-art) */
  --text-sm: .875rem; /* Typography Ink Token (findra-art) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (findra-art) */
  --text-base: 1rem; /* Typography Ink Token (findra-art) */
  --text-base--line-height: calc(1.5 / 1); /* Typography Ink Token (findra-art) */
  --text-lg: 1.125rem; /* Typography Ink Token (findra-art) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#09090b` — grounded in `var(--background)` in `:root`
- **Interactive Accent / Highlight**: `#f5f5f7` — grounded in `var(--foreground)` in `:root`
- **Secondary / Muted Copy**: `#a1a1aa` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#141417` — grounded in `var(--surface)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `findra-art` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:63rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `var(--radius-2xl)`, `2147483647px`, `var(--radius-lg)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--font-display: var(--font-anton), Impact, "Arial Narrow", sans-serif`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `findra-art` (`Findra: the AI character feed`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sticky> — `findra-art`)**:
   - DOM & Selectors: Landmark `<header class="sticky top-0">` hosting `Findra: the AI character feed` navigation (`Feed · Magazine · Wire · Leaderboard · 40 Under 40`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="1.6.1"`, `data-test="skip-to-content"`), and stylesheet rule `.u8MhCG_className { font-family:Geist,Geist Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sticky> — `findra-art`)` (`findra-art`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:63rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Feed · Magazine · Wire · Leaderboard · 40 Under 40`.
2. **Hero Stage & Focal Lead (<section.border-foreground> — `Breaking`)**:
   - DOM & Selectors: Landmark `<section class="border-foreground flex">` presenting display lead `Breaking` and copy excerpt *"Don Nuger’s Instagram account is unavailable"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Breaking`.
3. **Primary Showcase & Content Grid (<article.group> — `Who’s rising`)**:
   - DOM & Selectors: Landmark `<article class="group relative">` rendering section `Who’s rising` with copy *"The account could not be read on November 13 or this morning. It "*, asset references (`60143a72b8d6b7a7338339c64f9bcd8bb...`, `3f38907974d4f61e778b2b56d301ade05...`, `3qago8bg0x8_-.css`, `30qn3skk62nz8.js`), and grid rule `.u8MhCG_variable { --font-geist:"Geist", "Geist Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.group> — `Who’s rising`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.border-border> — `The week on Findra`)**:
   - DOM & Selectors: Landmark `<section class="border-border flex">` framing `The week on Findra` and `Latest story` (*"AI characters and the audiences they are building on TikTok, Inst"*) with `#09090b` surface cards, `#f5f5f7` accents, and `.mJqafq_className { font-family:Anton,Anton Fallback;font-style:normal;font-weight:400 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.border-border> — `The week on Findra`)` uses `.25rem`, `var(--radius-2xl)`, `2147483647px`, `var(--radius-lg)` radii, `#f5f5f7` highlights, and assets (60143a72b8d6b7a7338339c64f9bcd8bb..., 3f38907974d4f61e778b2b56d301ade05..., 3qago8bg0x8_-.css).
5. **Colophon & Global Directory Footer (<footer.text-muted> — `https://findra.art/`)**:
   - DOM & Selectors: Landmark `<footer class="text-muted mx-auto">` anchoring `Findra: the AI character feed` footer links (`Feed · Magazine · Wire · Leaderboard · 40 Under 40`), copy *"adventurous ai cat character"*, and `#141417` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.text-muted> — `https://findra.art/`)` aligns to `40rem` extracted from `findra-art` stylesheet with `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-precedence="next", data-sdkn="@vercel/analytics/react", data-sdkv="1.6.1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Don Nuger’s Instagram account is unavailable"*
- Copy Excerpt 2: *"The account could not be read on November 13 or this morning. It is the only accou..."*
- Copy Excerpt 3: *"AI characters and the audiences they are building on TikTok, Instagram, X and YouT..."*
- Copy Excerpt 4: *"adventurous ai cat character"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`findra-art`)**:
- `.u8MhCG_className { font-family:Geist,Geist Fallback;font-style:normal }`
- `.u8MhCG_variable { --font-geist:"Geist", "Geist Fallback" }`
- `.mJqafq_className { font-family:Anton,Anton Fallback;font-style:normal;font-weight:400 }`
- `.mJqafq_variable { --font-anton:"Anton", "Anton Fallback" }`
- `.XWwCSG_className { font-family:Permanent Marker,Permanent Marker Fallback;font-style:normal... }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `findra-art` stylesheet.
- **Selector `scale\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `findra-art` stylesheet.
- **Selector `scale\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `findra-art` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<article.group>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.border-foreground>` and `<article.group>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `findra-art`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
