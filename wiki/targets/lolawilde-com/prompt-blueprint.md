---
title: "UI Prompt Blueprint: lolawilde-com"
date: 2026-11-15
target: "[[overview|lolawilde-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000000` ink, `#000000` accent)"
---

# UI Design System & Master Generation Blueprint: lolawilde-com

> **LOLA WILDE — Learning Me** (https://lolawilde.com/) — Learning Me, the new album by LOLA WILDE. Listen on Spotify and read the lyrics.

![Desktop Viewport Capture (1440x5252)](file:///root/projects/fleet/wiki/targets/lolawilde-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **LOLA WILDE — Learning Me** (`https://lolawilde.com/`). Learning Me, the new album by LOLA WILDE. Listen on Spotify and read the lyrics.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000000` ink, `#000000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0000` (`var(--encore-list-row-bg)` in `:root`) paired with `#000000` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`LOLA WILDE — Learning Me`) with `Archivo Black` and `SpotifyMixMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `507px` container bounds (`gap: 4px`, padding `32px`) with `cubic-bezier(0.3,0,0,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/lolawilde-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5252px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `507px` extracted from `lolawilde-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `32px` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `48px`, `4px`, `.25rem`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 507px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-height:550px)`, `@media (max-height:200px)`, `@media (max-height:130px)`, `@media (max-width:359px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `var(--encore-list-row-bg)` in `:root` |
| **Primary Typography Ink** | `#121212` | `var(--background-base)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1f1f1f` | `var(--background-highlight)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--background-press)` in `:root` |
| **Secondary / Muted Copy** | `#2a2a2a` | `var(--background-elevated-highlight)` in `:root` |
| **Structural Hairline Border** | `#191919` | `var(--background-elevated-press)` in `:root` |
| **Variable Token (`--encore-overlay-box-shadow`)** | `#0000004d` | `var(--encore-overlay-box-shadow)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--trans-x` | `0px` | Dimension / Scale Token |
| `--encore-shortest-1` | `50ms` | Motion / Timing Token |
| `--encore-shortest-2` | `100ms` | Motion / Timing Token |
| `--encore-shortest-3` | `150ms` | Motion / Timing Token |
| `--encore-shortest-4` | `200ms` | Motion / Timing Token |
| `--encore-short-1` | `250ms` | Motion / Timing Token |
| `--encore-short-2` | `300ms` | Motion / Timing Token |
| `--encore-productive` | `cubic-bezier(0.3,0,0,1)` | Motion / Timing Token |
| `--encore-productive-decelerate` | `cubic-bezier(0,0,0.2,1)` | Motion / Timing Token |
| `--encore-productive-accelerate` | `cubic-bezier(0.8,0,1,1)` | Motion / Timing Token |
| `--encore-productive-exit-duration` | `var(--encore-shortest-4)` | Motion / Easing Token |
| `--encore-opacity-disabled` | `0.3` | Design System Custom Token |
| `--encore-opacity-active` | `0.7` | Design System Custom Token |
| `--encore-border-radius-rounded` | `9999px` | Elevation / Border Token |
| `--encore-overlay-box-shadow` | `0 4px 12px 0 #0000004d` | Elevation / Border Token |
| `--encore-overlay-drop-shadow` | `0 4px 6px #0000004d` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Archivo Black`.
- **Technical / Metadata Stack**: `SpotifyMixMono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-link-standalone-display: block`, `--encore-overlay-trigger-display: block`, `--display: 'Archivo Black', 'Arial Black', sans-serif`.
- **Section Heading (`H2`)**: rule `.h2` (`font-size: clamp(2.1rem,4.6vw,3.8rem)`, `line-height: 1`, `letter-spacing: -.035em`, `font-weight: 800`).
- **Body Copy**: CSS variables `--text-base: #ffffff`; rule `body` (`font-size: 16px`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: CSS variables `--encore-text-size-smaller-3: 0.625rem`, `--encore-text-size-smaller-2: 0.75rem`, `--encore-text-size-smaller: 0.875rem`; rule `.meta` (`font-size: 14px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.3,0,0,1)`, `cubic-bezier(0,0,0.2,1)`, `cubic-bezier(0.8,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.PreSaveButton_preSaveButton__6lI...`**: `transition: transform .3s ease-in-out` extracted from `lolawilde-com` stylesheet.
- **Selector `tifyButton_saveOnSpotifyButton__Q...`**: `transition: transform .3s ease-in-out` extracted from `lolawilde-com` stylesheet.
- **Selector `raryCompact_addToLibraryButton__e...`**: `transition: transform .3s ease-in-out` extracted from `lolawilde-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.3,0,0,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.blk>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.blk>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — LOLA WILDE — Learning Me                   │
│ ====================================================================== │
│ [ <header.nav>             | Songs · Album · About · Shop · Press   ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: LOLA WILDE — Learning Me                                     |   │
│ | Substrate: #0000      | Ink: #000000    | Accent: #000000        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.blk>             ) max-w: 507px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Learning Me                  |  | The girl in the front row, l | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px   ) | │
│ | [<header.nav>] -> [<section.hero>] -> [<section.blk>] |              │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.pill>         ) | https://lolawilde.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `lolawilde-com`)**:
   - Landmark `<header class="nav">` hosting `LOLA WILDE — Learning Me` navigation (`Songs · Album · About · Shop · Press`), DOM attributes (`data-album-title`, `data-i="0"`, `data-i="1"`, `data-i="2"`), and stylesheet rule `.Error_wrapper__7m1Fk { display:flex;align-items:center;flex-direction:column }`.
2. **Hero Stage & Focal Lead (<section.hero> — `LOLA WILDE — Learning Me`)**:
   - Landmark `<section class="hero">` presenting display lead `LOLA WILDE — Learning Me` and copy excerpt *"Out now · New album"* over `#0000` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.blk> — `Learning Me`)**:
   - Landmark `<section class="blk">` rendering section `Learning Me` with copy *"01 Golden ▶ Play and sing along"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `.Error_title__KvfPv { font-size:48px;line-height:1;letter-spacing:-.04em;margin:40px 0 16px;fo... }`.
4. **Interactive Detail & Feature Matrix (<section.about-sec> — `The girl in the front row, learnin`)**:
   - Landmark `<section class="about-sec">` framing `The girl in the front row, learning who she is.` and `Lipstick Confessions on vinyl.` (*"▶ Play and sing along"*) with `#1f1f1f` surface cards, `#000000` accents, and `.Error_description__h_wjs { line-height:24px;max-width:507px;margin:0 0 40px;font-weight:200;display... }`.
5. **Colophon & Global Directory Footer (<footer.pill> — `https://lolawilde.com/`)**:
   - Landmark `<footer class="pill">` anchoring `LOLA WILDE — Learning Me` footer links (`Songs · Album · About · Shop · Press`), copy *"02 The Way You Said My Name ▶ Play and sing along"*, and `#191919` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: lolawilde-com (LOLA WILDE — Learning Me)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `lolawilde-com` (**LOLA WILDE — Learning Me** — `https://lolawilde.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000000` ink, `#000000` accent).
- **Identity & Domain Context**: Learning Me, the new album by LOLA WILDE. Listen on Spotify and read the lyrics.
- **Primary Substrate**: `#0000` (`var(--encore-list-row-bg)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#000000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0000` (`var(--encore-list-row-bg)` in `:root`) paired with `#000000` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`LOLA WILDE — Learning Me`) with `Archivo Black` and `SpotifyMixMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `507px` container bounds (`gap: 4px`, padding `32px`) with `cubic-bezier(0.3,0,0,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `lolawilde-com` in your global stylesheet:

:root {
  /* LOLA WILDE — Learning Me (lolawilde-com) — Ground-Truth Extracted CSS Variables */
  --trans-x: 0px; /* Dimension / Scale Token (lolawilde-com) */
  --encore-shortest-1: 50ms; /* Motion / Timing Token (lolawilde-com) */
  --encore-shortest-2: 100ms; /* Motion / Timing Token (lolawilde-com) */
  --encore-shortest-3: 150ms; /* Motion / Timing Token (lolawilde-com) */
  --encore-shortest-4: 200ms; /* Motion / Timing Token (lolawilde-com) */
  --encore-short-1: 250ms; /* Motion / Timing Token (lolawilde-com) */
  --encore-short-2: 300ms; /* Motion / Timing Token (lolawilde-com) */
  --encore-productive: cubic-bezier(0.3,0,0,1); /* Motion / Timing Token (lolawilde-com) */
  --encore-productive-decelerate: cubic-bezier(0,0,0.2,1); /* Motion / Timing Token (lolawilde-com) */
  --encore-productive-accelerate: cubic-bezier(0.8,0,1,1); /* Motion / Timing Token (lolawilde-com) */
  --encore-productive-exit-duration: var(--encore-shortest-4); /* Motion / Easing Token (lolawilde-com) */
  --encore-opacity-disabled: 0.3; /* Design System Custom Token (lolawilde-com) */
  --encore-opacity-active: 0.7; /* Design System Custom Token (lolawilde-com) */
  --encore-border-radius-rounded: 9999px; /* Elevation / Border Token (lolawilde-com) */
  --encore-overlay-box-shadow: 0 4px 12px 0 #0000004d; /* Elevation / Border Token (lolawilde-com) */
  --encore-overlay-drop-shadow: 0 4px 6px #0000004d; /* Elevation / Border Token (lolawilde-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0000` — grounded in `var(--encore-list-row-bg)` in `:root`
- **Primary Typography Ink**: `#121212` — grounded in `var(--background-base)` in `:root`
- **Elevated Surface / Card Substrate**: `#1f1f1f` — grounded in `var(--background-highlight)` in `:root`
- **Interactive Accent / Highlight**: `#000000` — grounded in `var(--background-press)` in `:root`
- **Secondary / Muted Copy**: `#2a2a2a` — grounded in `var(--background-elevated-highlight)` in `:root`
- **Structural Hairline Border**: `#191919` — grounded in `var(--background-elevated-press)` in `:root`
- **Variable Token (`--encore-overlay-box-shadow`)**: `#0000004d` — grounded in `var(--encore-overlay-box-shadow)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5252px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `507px` extracted from `lolawilde-com` stylesheet
- **Padding & Gutters**: `32px` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 507px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding
- **Media Queries**: `@media (max-height:550px)`, `@media (max-height:200px)`, `@media (max-height:130px)`, `@media (max-width:359px)`
- **Corner Radii**: `48px`, `4px`, `.25rem`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo Black`
- **Monospace / Technical Font Stack**: `SpotifyMixMono`
- **H1 Display Rule**: CSS variables `--text-link-standalone-display: block`, `--encore-overlay-trigger-display: block`, `--display: 'Archivo Black', 'Arial Black', sans-serif`
- **H2 Section Rule**: rule `.h2` (`font-size: clamp(2.1rem,4.6vw,3.8rem)`, `line-height: 1`, `letter-spacing: -.035em`, `font-weight: 800`)
- **Body Copy Rule**: CSS variables `--text-base: #0000`; rule `body` (`font-size: 16px`, `line-height: 1.5`)
- **Metadata & Index Rule**: CSS variables `--encore-text-size-smaller-3: 0.625rem`, `--encore-text-size-smaller-2: 0.75rem`, `--encore-text-size-smaller: 0.875rem`; rule `.meta` (`font-size: 14px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `lolawilde-com` (`LOLA WILDE — Learning Me`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `lolawilde-com`)**:
   - DOM & Selectors: Landmark `<header class="nav">` hosting `LOLA WILDE — Learning Me` navigation (`Songs · Album · About · Shop · Press`), DOM attributes (`data-album-title`, `data-i="0"`, `data-i="1"`, `data-i="2"`), and stylesheet rule `.Error_wrapper__7m1Fk { display:flex;align-items:center;flex-direction:column }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `lolawilde-com`)` (`lolawilde-com`) adapts across `@media (max-height:550px)`, `@media (max-height:200px)`, `@media (max-height:130px)`, `@media (max-width:359px)` with `cubic-bezier(0.3,0,0,1)`, `cubic-bezier(0,0,0.2,1)`, `cubic-bezier(0.8,0,1,1)` transitions and links `Songs · Album · About · Shop · Press`.
2. **Hero Stage & Focal Lead (<section.hero> — `LOLA WILDE — Learning Me`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `LOLA WILDE — Learning Me` and copy excerpt *"Out now · New album"* over `#0000` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×5252px` desktop / `390×2400px` mobile) sets `#0000` background with `#000000` headline `LOLA WILDE — Learning Me`.
3. **Primary Showcase & Content Grid (<section.blk> — `Learning Me`)**:
   - DOM & Selectors: Landmark `<section class="blk">` rendering section `Learning Me` with copy *"01 Golden ▶ Play and sing along"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `.Error_title__KvfPv { font-size:48px;line-height:1;letter-spacing:-.04em;margin:40px 0 16px;fo... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.blk> — `Learning Me`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 507px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `32px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.about-sec> — `The girl in the front row, learnin`)**:
   - DOM & Selectors: Landmark `<section class="about-sec">` framing `The girl in the front row, learning who she is.` and `Lipstick Confessions on vinyl.` (*"▶ Play and sing along"*) with `#1f1f1f` surface cards, `#000000` accents, and `.Error_description__h_wjs { line-height:24px;max-width:507px;margin:0 0 40px;font-weight:200;display... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.about-sec> — `The girl in the front row, learnin`)` uses `48px`, `4px`, `.25rem`, `50%` radii, `#000000` highlights, and assets (favicon.svg, favicon-32.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.pill> — `https://lolawilde.com/`)**:
   - DOM & Selectors: Landmark `<footer class="pill">` anchoring `LOLA WILDE — Learning Me` footer links (`Songs · Album · About · Shop · Press`), copy *"02 The Way You Said My Name ▶ Play and sing along"*, and `#191919` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.pill> — `https://lolawilde.com/`)` aligns to `507px` extracted from `lolawilde-com` stylesheet with `32px` lateral canvas padding with `4px` grid gap and attributes (data-album-title, data-i="0", data-i="1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Out now · New album"*
- Copy Excerpt 2: *"01 Golden ▶ Play and sing along"*
- Copy Excerpt 3: *"▶ Play and sing along"*
- Copy Excerpt 4: *"02 The Way You Said My Name ▶ Play and sing along"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.3,0,0,1)`, `cubic-bezier(0,0,0.2,1)`, `cubic-bezier(0.8,0,1,1)`
- **Extracted Stylesheet Rules (`lolawilde-com`)**:
- `.Error_wrapper__7m1Fk { display:flex;align-items:center;flex-direction:column }`
- `.Error_title__KvfPv { font-size:48px;line-height:1;letter-spacing:-.04em;margin:40px 0 16px;fo... }`
- `.Error_description__h_wjs { line-height:24px;max-width:507px;margin:0 0 40px;font-weight:200;display... }`
- `.Error_links__WY7mc { display:flex;flex-direction:column;align-items:center }`
- `.Error_links__WY7mc a { font-size:1em;font-weight:700;text-decoration:none }`
- **Per-Selector Transition Rules**:
- **Selector `.PreSaveButton_preSaveButton__6lI...`**: `transition: transform .3s ease-in-out` extracted from `lolawilde-com` stylesheet.
- **Selector `tifyButton_saveOnSpotifyButton__Q...`**: `transition: transform .3s ease-in-out` extracted from `lolawilde-com` stylesheet.
- **Selector `raryCompact_addToLibraryButton__e...`**: `transition: transform .3s ease-in-out` extracted from `lolawilde-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.3,0,0,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.blk>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.blk>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `lolawilde-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
