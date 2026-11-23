---
title: "UI Prompt Blueprint: annnimate-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "annnimate-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#b3fca0` / `#ca4417`)"
---

# UI Design System & Master Generation Blueprint: annnimate-com

> **GSAP Motion Components for React & Vue · Annnimate** (https://annnimate.com) — Production GSAP motion components for React and Vue. Every component is built to the standard we ship for real brands. By Good Fella.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **GSAP Motion Components for React & Vue · Annnimate** (`https://annnimate.com`). Production GSAP motion components for React and Vue. Every component is built to the standard we ship for real brands. By Good Fella.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#b3fca0` / `#ca4417`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#b3fca0` (live computed `meta-theme-color` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ca4417` accents.
  - **Grounded Typographic Hierarchy**: Pairs `geistSans` for display copy (`Give any site award‑level animation `) with `geistSans Fallback` and `geistMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 12px`, padding `22px`) with `cubic-bezier(.7,0,.16,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `22px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `16px`, `.25rem`, `var(--adm-radius)`, `var(--adm-radius-md)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `22px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:767px)`, `@media (max-width:479px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#b3fca0` | live computed `meta-theme-color` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | `var(--foreground)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f2f2ef` | `var(--ga-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ca4417` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#696869` | `var(--foreground-muted)` in `:root` |
| **Structural Hairline Border** | `#d4d4d4` | `var(--surface-border)` in `:root` |
| **Variable Token (`--ga-tile`)** | `#fafaf8` | `var(--ga-tile)` in `:root` |
| **Variable Token (`--ga-tile-2`)** | `#e8e8e4` | `var(--ga-tile-2)` in `:root` |
| **Variable Token (`--ga-fg`)** | `#141314` | `var(--ga-fg)` in `:root` |
| **Variable Token (`--ga-fg-soft`)** | `#9a9a96` | `var(--ga-fg-soft)` in `:root` |
| **Variable Token (`--ga-focus`)** | `#101010` | `var(--ga-focus)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist-sans` | `"geistSans", "geistSans Fallback"` | Typography / Scale Token |
| `--font-geist-mono` | `"geistMono", "geistMono Fallback"` | Typography / Scale Token |
| `--font-aktiv` | `"aktivGrotesk", "aktivGrotesk Fallback"` | Typography / Scale Token |
| `--font-handwritten` | `"shadowsIntoLight", "shadowsIntoLight Fallback"` | Typography / Scale Token |
| `--ga-bg` | `#f2f2ef` | Canvas / Surface Token |
| `--ga-tile` | `#fafaf8` | Color / Atmospheric Token |
| `--ga-tile-2` | `#e8e8e4` | Color / Atmospheric Token |
| `--ga-ink` | `#fafaf8` | Typography Ink Token |
| `--ga-fg` | `#141314` | Typography Ink Token |
| `--ga-fg-soft` | `#9a9a96` | Typography Ink Token |
| `--ga-fg-dim` | `#9a9a96` | Typography Ink Token |
| `--ga-focus` | `#1010104d` | Color / Atmospheric Token |
| `--ga-margin` | `clamp(20px, 2.8vw, 48px)` | Layout / Spatial Grid Token |
| `--ga-gutter` | `clamp(12px, 1.4vw, 24px)` | Layout / Spatial Grid Token |
| `--ga-label` | `clamp(18px, 1.4vw, 28px)` | Dimension / Scale Token |
| `--angle` | `0deg` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `geistSans`.
- **Primary Body Stack**: `geistSans Fallback`.
- **Technical / Metadata Stack**: `geistMono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `,.h1` (`font-size: var(--font-size-4xl)`, `line-height: 1.2`, `letter-spacing: -.04em`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `,.h2` (`font-size: var(--font-size-2xl)`, `line-height: 1.2`, `letter-spacing: -.03em`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-size-base: clamp(1rem,.95rem + .25vw,1.125rem)`.
- **Metadata & Navigation Labels**: CSS variables `--font-geist-mono: "geistMono", "geistMono Fallback"`, `--ga-label: clamp(18px, 1.4vw, 28px)`, `--font-mono: var(--font-geist-mono),"SF Mono",Monaco,"Cascadia Code",monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.7,0,.16,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.macc_trigger_crisp`**: `transition: background-color .3s cubic-bezier(.7,0,.16,1)` extracted from `annnimate-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `annnimate-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `annnimate-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,0,.16,1)`)**: Governs interactive state transitions across `<header.v2-header>` and `<section.pt-64>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — GSAP Motion Components for React & Vue · A │
│ ====================================================================== │
│ [ <header.v2-header> (1440px)         | Library Library · Kits Kits  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.bg-background> (w=1440px)                     | │
│ | H1: Give any site award‑level animation in minutes.                | │
│ | Substrate: #b3fca0 | Ink: #000000 | Accent: #ca4417                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.pt-64>) max-w: 96rem                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Try it before you copy it.   |  | Client-ready the moment you  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.py-64>) — Motion that wins the             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.annnimate-fo) | https://annnimate.com                │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.v2-header>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.bg-background>) — 390px Vertical Lead         | │
│ | H1: Give any site award‑level animation in minutes.                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.pt-64>) — 1-Col Stack                     | │
│ | [ Item 1: Try it before you copy it.                             ] | │
│ | [ Item 2: Client-ready the moment you paste it.                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.py-64>) — 1-Col (Motion that wins t)        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.annnimate-fo) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.v2-header> — `annnimate-com`)**:
   - Landmark `<header class="v2-header inset-x-0">` (`1440px`) hosting `GSAP Motion Components for React & V` navigation (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.QRhTIa_className { font-family:geistSans,geistSans Fallback }`.
2. **Hero Stage & Focal Lead (<section.bg-background> — `Give any site award‑level animatio`)**:
   - Landmark `<section class="bg-background pt-112">` presenting display lead `Give any site award‑level animation in minutes.` and copy excerpt *"Give any site award‑level"* over `#b3fca0` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.pt-64> — `Try it before you copy it.`)**:
   - Landmark `<section class="bg-background pt-64">` rendering section `Try it before you copy it.` with copy *"animation in minutes."*, asset references (`teaser-poster.jpg`, `edoardo_avatar.avif`, `lukas_avatar.avif`, `matthew_avatar.avif`), and grid rule `.QRhTIa_variable { --font-geist-sans:"geistSans", "geistSans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-64> — `Client-ready the moment you paste `)**:
   - Landmark `<section class="bg-background py-64">` framing `Client-ready the moment you paste it.` and `Motion that wins the pitch` (*"The same GSAP animations we build for Coca-Cola and Powerade, rea"*) with `#f2f2ef` surface cards, `#ca4417` accents, and `.mNpjDG_className { font-family:geistMono,geistMono Fallback }`.
5. **Colophon & Global Directory Footer (<footer.annnimate-footer> — `https://annnimate.com`)**:
   - Landmark `<footer class="annnimate-footer bg-background">` anchoring `GSAP Motion Components for React` footer links (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), copy *"Get access -25% Get access -25%"*, and `#d4d4d4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: annnimate-com (GSAP Motion Components for React & Vue · Annnimate)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `annnimate-com` (**GSAP Motion Components for React & Vue · Annnimate** — `https://annnimate.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#b3fca0` / `#ca4417`).
- **Identity & Domain Context**: Production GSAP motion components for React and Vue. Every component is built to the standard we ship for real brands. By Good Fella.
- **Primary Substrate**: `#b3fca0` (live computed `meta-theme-color` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ca4417`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#b3fca0` (live computed `meta-theme-color` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ca4417` accents.
  - **Grounded Typographic Hierarchy**: Pairs `geistSans` for display copy (`Give any site award‑level animation `) with `geistSans Fallback` and `geistMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 12px`, padding `22px`) with `cubic-bezier(.7,0,.16,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `annnimate-com` in your global stylesheet:

:root {
  /* GSAP Motion Components for React & Vue · Annnimate (annnimate-com) — Live-Grounded CSS Variables */
  --font-geist-sans: "geistSans", "geistSans Fallback"; /* Typography / Scale Token (annnimate-com) */
  --font-geist-mono: "geistMono", "geistMono Fallback"; /* Typography / Scale Token (annnimate-com) */
  --font-aktiv: "aktivGrotesk", "aktivGrotesk Fallback"; /* Typography / Scale Token (annnimate-com) */
  --font-handwritten: "shadowsIntoLight", "shadowsIntoLight Fallback"; /* Typography / Scale Token (annnimate-com) */
  --ga-bg: #f2f2ef; /* Canvas / Surface Token (annnimate-com) */
  --ga-tile: #fafaf8; /* Color / Atmospheric Token (annnimate-com) */
  --ga-tile-2: #e8e8e4; /* Color / Atmospheric Token (annnimate-com) */
  --ga-ink: #fafaf8; /* Typography Ink Token (annnimate-com) */
  --ga-fg: #141314; /* Typography Ink Token (annnimate-com) */
  --ga-fg-soft: #9a9a96; /* Typography Ink Token (annnimate-com) */
  --ga-fg-dim: #9a9a96; /* Typography Ink Token (annnimate-com) */
  --ga-focus: #1010104d; /* Color / Atmospheric Token (annnimate-com) */
  --ga-margin: clamp(20px, 2.8vw, 48px); /* Layout / Spatial Grid Token (annnimate-com) */
  --ga-gutter: clamp(12px, 1.4vw, 24px); /* Layout / Spatial Grid Token (annnimate-com) */
  --ga-label: clamp(18px, 1.4vw, 28px); /* Dimension / Scale Token (annnimate-com) */
  --angle: 0deg; /* Design System Custom Token (annnimate-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#b3fca0` — grounded in live computed `meta-theme-color` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in `var(--foreground)` in `:root`
- **Elevated Surface / Card Substrate**: `#f2f2ef` — grounded in `var(--ga-bg)` in `:root`
- **Interactive Accent / Highlight**: `#ca4417` — grounded in `var(--primary)` in `:root`
- **Secondary / Muted Copy**: `#696869` — grounded in `var(--foreground-muted)` in `:root`
- **Structural Hairline Border**: `#d4d4d4` — grounded in `var(--surface-border)` in `:root`
- **Variable Token (`--ga-tile`)**: `#fafaf8` — grounded in `var(--ga-tile)` in `:root`
- **Variable Token (`--ga-tile-2`)**: `#e8e8e4` — grounded in `var(--ga-tile-2)` in `:root`
- **Variable Token (`--ga-fg`)**: `#141314` — grounded in `var(--ga-fg)` in `:root`
- **Variable Token (`--ga-fg-soft`)**: `#9a9a96` — grounded in `var(--ga-fg-soft)` in `:root`
- **Variable Token (`--ga-focus`)**: `#101010` — grounded in `var(--ga-focus)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `22px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `22px` horizontal padding
- **Media Queries**: `@media (max-width:767px)`, `@media (max-width:479px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`
- **Corner Radii**: `16px`, `.25rem`, `var(--adm-radius)`, `var(--adm-radius-md)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `geistSans`
- **Body Font Stack**: `geistSans Fallback`
- **Monospace / Technical Font Stack**: `geistMono`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `,.h1` (`font-size: var(--font-size-4xl)`, `line-height: 1.2`, `letter-spacing: -.04em`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `,.h2` (`font-size: var(--font-size-2xl)`, `line-height: 1.2`, `letter-spacing: -.03em`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-size-base: clamp(1rem,.95rem + .25vw,1.125rem)`
- **Metadata & Index Rule**: CSS variables `--font-geist-mono: "geistMono", "geistMono Fallback"`, `--ga-label: clamp(18px, 1.4vw, 28px)`, `--font-mono: var(--font-geist-mono),"SF Mono",Monaco,"Cascadia Code",monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `annnimate-com` (`GSAP Motion Components for React & Vue · Annnimate`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.v2-header> — `annnimate-com`)**:
   - DOM & Selectors: Landmark `<header class="v2-header inset-x-0">` (`1440px`) hosting `GSAP Motion Components for React & V` navigation (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.QRhTIa_className { font-family:geistSans,geistSans Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.v2-header> — `annnimate-com`)` (`annnimate-com`) adapts across `@media (max-width:767px)`, `@media (max-width:479px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)` with `cubic-bezier(.7,0,.16,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`.
2. **Hero Stage & Focal Lead (<section.bg-background> — `Give any site award‑level animatio`)**:
   - DOM & Selectors: Landmark `<section class="bg-background pt-112">` presenting display lead `Give any site award‑level animation in minutes.` and copy excerpt *"Give any site award‑level"* over `#b3fca0` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#b3fca0` background with `#000000` headline `Give any site award‑level animation in minutes.`.
3. **Primary Showcase & Content Grid (<section.pt-64> — `Try it before you copy it.`)**:
   - DOM & Selectors: Landmark `<section class="bg-background pt-64">` rendering section `Try it before you copy it.` with copy *"animation in minutes."*, asset references (`teaser-poster.jpg`, `edoardo_avatar.avif`, `lukas_avatar.avif`, `matthew_avatar.avif`), and grid rule `.QRhTIa_variable { --font-geist-sans:"geistSans", "geistSans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.pt-64> — `Try it before you copy it.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `22px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-64> — `Client-ready the moment you paste `)**:
   - DOM & Selectors: Landmark `<section class="bg-background py-64">` framing `Client-ready the moment you paste it.` and `Motion that wins the pitch` (*"The same GSAP animations we build for Coca-Cola and Powerade, rea"*) with `#f2f2ef` surface cards, `#ca4417` accents, and `.mNpjDG_className { font-family:geistMono,geistMono Fallback }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-64> — `Client-ready the moment you paste `)` uses `16px`, `.25rem`, `var(--adm-radius)`, `var(--adm-radius-md)` radii, `#ca4417` highlights, and assets (teaser-poster.jpg, edoardo_avatar.avif, lukas_avatar.avif).
5. **Colophon & Global Directory Footer (<footer.annnimate-footer> — `https://annnimate.com`)**:
   - DOM & Selectors: Landmark `<footer class="annnimate-footer bg-background">` anchoring `GSAP Motion Components for React` footer links (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), copy *"Get access -25% Get access -25%"*, and `#d4d4d4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.annnimate-footer> — `https://annnimate.com`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `22px` lateral canvas padding with `12px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Give any site award‑level"*
- Copy Excerpt 2: *"animation in minutes."*
- Copy Excerpt 3: *"The same GSAP animations we build for Coca-Cola and Powerade, ready for React, Vue..."*
- Copy Excerpt 4: *"Get access -25% Get access -25%"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.7,0,.16,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`annnimate-com`)**:
- `.QRhTIa_className { font-family:geistSans,geistSans Fallback }`
- `.QRhTIa_variable { --font-geist-sans:"geistSans", "geistSans Fallback" }`
- `.mNpjDG_className { font-family:geistMono,geistMono Fallback }`
- `.mNpjDG_variable { --font-geist-mono:"geistMono", "geistMono Fallback" }`
- `.b-foHG_className { font-family:aktivGrotesk,aktivGrotesk Fallback }`
- **Per-Selector Transition Rules**:
- **Selector `.macc_trigger_crisp`**: `transition: background-color .3s cubic-bezier(.7,0,.16,1)` extracted from `annnimate-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `annnimate-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `annnimate-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,0,.16,1)`)**: Governs interactive state transitions across `<header.v2-header>` and `<section.pt-64>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `annnimate-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
