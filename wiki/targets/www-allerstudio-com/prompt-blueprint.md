---
title: "UI Prompt Blueprint: www-allerstudio-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-allerstudio-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f9fafb` / `#787878`)"
---

# UI Design System & Master Generation Blueprint: www-allerstudio-com

> **ALLER Studio — Product design and development studio** (https://www.allerstudio.com/) — Product design and development studio for Web3, AI, fintech, and gaming.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ALLER Studio — Product design and development studio** (`https://www.allerstudio.com/`). Product design and development studio for Web3, AI, fintech, and gaming.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f9fafb` / `#787878`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f9fafb` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#121212` primary typography and `#787878` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Rajdhani` for display copy (`Product design and development studi`) with `Inter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 4px`, padding `var(--btn-px)`) with `cubic-bezier(.16,1,.3,1)` easing and Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (live computed `main` `max-width`).
- **Canvas Lateral Padding & Spacing**: `var(--btn-px)` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `3.35544e+07px`, `50%`, `16px`, `44px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--btn-px)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9fafb` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#121212` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f7f8` | `var(--color-surface-bg-2)` in `:root` |
| **Interactive Accent / Highlight** | `#787878` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#787878` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dadee2` | `var(--color-border)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--duration-quick` | `.15s` | Motion / Easing Token |
| `--duration-fast` | `.25s` | Motion / Easing Token |
| `--duration-medium` | `.35s` | Motion / Easing Token |
| `--duration-very-slow` | `.5s` | Motion / Easing Token |
| `--ease-smooth-out` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--ease-bounce` | `cubic-bezier(.34, 1.35, .64, 1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.37, 0, .63, 1)` | Motion / Easing Token |
| `--active` | `0` | Design System Custom Token |
| `--font-sans` | `var(--font-inter), "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Rajdhani`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 56px`, `font-weight: 600`); CSS variables `--text-5xl: 3rem`, `--text-5xl--line-height: 1`, `--font-display: var(--font-rajdhani), "Arial Narrow", sans-serif`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 56px`, `font-weight: 600`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.37,0,.63,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `._3N0scq_progress`**: `transition: stroke-dashoffset var(--travel) var(--ease-in-out)` extracted from `www-allerstudio-com` stylesheet.
- **Selector `scq_board[data-resetting] ._3N0sc...`**: `transition: opacity .5s var(--ease-in-out)` extracted from `www-allerstudio-com` stylesheet.
- **Selector `._3N0scq_nodeOn`**: `transition: opacity .35s var(--ease-out), transform .5s var(--ease-out)` extracted from `www-allerstudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.header-in>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ALLER Studio — Product design and developm │
│ ====================================================================== │
│ [ <header.header-in> (954x64px)       | Services · Case Studies · St ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.pt-40> (w=1440px)                             | │
│ | H1: Product design and development studio for Web3, A...           | │
│ | Substrate: #f9fafb | Ink: #121212 | Accent: #787878                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Technology can be complex. T |  | Complex flows                | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.pt-20>) — Low user trust                   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-42>       ) | https://www.allerstudio.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.header-in>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.pt-40>) — 390px Vertical Lead                 | │
│ | H1: Product design and development studio for Web3, A...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.relative>) — 1-Col Stack                  | │
│ | [ Item 1: Technology can be complex. The experience should...    ] | │
│ | [ Item 2: Complex flows                                          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.pt-20>) — 1-Col (Low user trust)            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-42>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header-in> — `www-allerstudio-com`)**:
   - Landmark `<header class="header-in top-4">` (`954x64px`) hosting `ALLER Studio — Product design and de` navigation (`Services · Case Studies · Studio · Insights · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `._3N0scq_board { width:954px;height:594px;transform:scale(var(--s,1));transform-origin:0... }`.
2. **Hero Stage & Focal Lead (<section.pt-40> — `Product design and development stu`)**:
   - Landmark `<section class="pt-40 relative">` presenting display lead `Product design and development studio for Web3, A...` and copy excerpt *"Lima · 9:23 PM UTC-5"* over `#f9fafb` canvas and `#121212` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Technology can be complex. The exp`)**:
   - Landmark `<section class="relative px-4">` rendering section `Technology can be complex. The experience should...` with copy *"Not made for the moment."*, asset references (`3206eb66b875a5b3-s.p.3gjg6tthudz5...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `a079e02bba5bf7ab-s.p.2yv0x3fl1lx-...`, `a10c617c9026098c-s.p.1a-q6cj6za4e...`), and grid rule `._3N0scq_svg { pointer-events:none;position:absolute;inset:0;overflow:visible }`.
4. **Interactive Detail & Feature Matrix (<section.pt-20> — `Complex flows`)**:
   - Landmark `<section class="pt-20 pb-4">` framing `Complex flows` and `Low user trust` (*"Built for what follows."*) with `#f6f7f8` surface cards, `#787878` accents, and `._3N0scq_progress { stroke-dasharray:1 1;stroke-dashoffset:1px;opacity:1;transition:stroke-d... }`.
5. **Colophon & Global Directory Footer (<footer.z-42> — `https://www.allerstudio.com/`)**:
   - Landmark `<footer class="z-42 bg-dark-950">` anchoring `ALLER Studio — Product design an` footer links (`Services · Case Studies · Studio · Insights · Contact`), copy *"Product strategy · UX/UI · Branding · Development"*, and `#dadee2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-allerstudio-com (ALLER Studio — Product design and development studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-allerstudio-com` (**ALLER Studio — Product design and development studio** — `https://www.allerstudio.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f9fafb` / `#787878`).
- **Identity & Domain Context**: Product design and development studio for Web3, AI, fintech, and gaming.
- **Primary Substrate**: `#f9fafb` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#121212`, **Accent / Highlight**: `#787878`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f9fafb` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#121212` primary typography and `#787878` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Rajdhani` for display copy (`Product design and development studi`) with `Inter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 4px`, padding `var(--btn-px)`) with `cubic-bezier(.16,1,.3,1)` easing and Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-allerstudio-com` in your global stylesheet:

:root {
  /* ALLER Studio — Product design and development studio (www-allerstudio-com) — Live-Grounded CSS Variables */
  --duration-quick: .15s; /* Motion / Easing Token (www-allerstudio-com) */
  --duration-fast: .25s; /* Motion / Easing Token (www-allerstudio-com) */
  --duration-medium: .35s; /* Motion / Easing Token (www-allerstudio-com) */
  --duration-very-slow: .5s; /* Motion / Easing Token (www-allerstudio-com) */
  --ease-smooth-out: cubic-bezier(.22, 1, .36, 1); /* Motion / Easing Token (www-allerstudio-com) */
  --ease-bounce: cubic-bezier(.34, 1.35, .64, 1); /* Motion / Easing Token (www-allerstudio-com) */
  --ease-out: cubic-bezier(.16, 1, .3, 1); /* Motion / Easing Token (www-allerstudio-com) */
  --ease-in-out: cubic-bezier(.37, 0, .63, 1); /* Motion / Easing Token (www-allerstudio-com) */
  --active: 0; /* Design System Custom Token (www-allerstudio-com) */
  --font-sans: var(--font-inter), "Helvetica Neue", Arial, sans-serif; /* Typography / Scale Token (www-allerstudio-com) */
  --color-black: #000; /* Canvas / Surface Token (www-allerstudio-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-allerstudio-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-allerstudio-com) */
  --text-xs: .75rem; /* Typography Ink Token (www-allerstudio-com) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (www-allerstudio-com) */
  --text-sm: .875rem; /* Typography Ink Token (www-allerstudio-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f9fafb` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#121212` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f6f7f8` — grounded in `var(--color-surface-bg-2)` in `:root`
- **Interactive Accent / Highlight**: `#787878` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#787878` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#dadee2` — grounded in `var(--color-border)` in `:root`
- **Variable Token (`--color-black`)**: `#000000` — grounded in `var(--color-black)` in `:root`
- **Variable Token (`--color-white`)**: `#ffffff` — grounded in `var(--color-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (live computed `main` `max-width`)
- **Padding & Gutters**: `var(--btn-px)` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--btn-px)` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `3.35544e+07px`, `50%`, `16px`, `44px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Rajdhani`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 48px`, `line-height: 56px`, `font-weight: 600`); CSS variables `--text-5xl: 3rem`, `--text-5xl--line-height: 1`, `--font-display: var(--font-rajdhani), "Arial Narrow", sans-serif`
- **H2 Section Rule**: live computed `h2` (`font-size: 48px`, `line-height: 56px`, `font-weight: 600`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-allerstudio-com` (`ALLER Studio — Product design and development studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header-in> — `www-allerstudio-com`)**:
   - DOM & Selectors: Landmark `<header class="header-in top-4">` (`954x64px`) hosting `ALLER Studio — Product design and de` navigation (`Services · Case Studies · Studio · Insights · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `._3N0scq_board { width:954px;height:594px;transform:scale(var(--s,1));transform-origin:0... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header-in> — `www-allerstudio-com`)` (`www-allerstudio-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.37,0,.63,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `Services · Case Studies · Studio · Insights · Contact`.
2. **Hero Stage & Focal Lead (<section.pt-40> — `Product design and development stu`)**:
   - DOM & Selectors: Landmark `<section class="pt-40 relative">` presenting display lead `Product design and development studio for Web3, A...` and copy excerpt *"Lima · 9:23 PM UTC-5"* over `#f9fafb` canvas and `#121212` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f9fafb` background with `#121212` headline `Product design and development studio for Web3, A...`.
3. **Primary Showcase & Content Grid (<section.relative> — `Technology can be complex. The exp`)**:
   - DOM & Selectors: Landmark `<section class="relative px-4">` rendering section `Technology can be complex. The experience should...` with copy *"Not made for the moment."*, asset references (`3206eb66b875a5b3-s.p.3gjg6tthudz5...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `a079e02bba5bf7ab-s.p.2yv0x3fl1lx-...`, `a10c617c9026098c-s.p.1a-q6cj6za4e...`), and grid rule `._3N0scq_svg { pointer-events:none;position:absolute;inset:0;overflow:visible }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `Technology can be complex. The exp`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--btn-px)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.pt-20> — `Complex flows`)**:
   - DOM & Selectors: Landmark `<section class="pt-20 pb-4">` framing `Complex flows` and `Low user trust` (*"Built for what follows."*) with `#f6f7f8` surface cards, `#787878` accents, and `._3N0scq_progress { stroke-dasharray:1 1;stroke-dashoffset:1px;opacity:1;transition:stroke-d... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.pt-20> — `Complex flows`)` uses `3.35544e+07px`, `50%`, `16px`, `44px` radii, `#787878` highlights, and assets (3206eb66b875a5b3-s.p.3gjg6tthudz5..., 83afe278b6a6bb3c-s.p.45535valc9rz..., a079e02bba5bf7ab-s.p.2yv0x3fl1lx-...).
5. **Colophon & Global Directory Footer (<footer.z-42> — `https://www.allerstudio.com/`)**:
   - DOM & Selectors: Landmark `<footer class="z-42 bg-dark-950">` anchoring `ALLER Studio — Product design an` footer links (`Services · Case Studies · Studio · Insights · Contact`), copy *"Product strategy · UX/UI · Branding · Development"*, and `#dadee2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.z-42> — `https://www.allerstudio.com/`)` aligns to `1440px` (live computed `main` `max-width`) with `var(--btn-px)` lateral canvas padding with `4px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Lima · 9:23 PM UTC-5"*
- Copy Excerpt 2: *"Not made for the moment."*
- Copy Excerpt 3: *"Built for what follows."*
- Copy Excerpt 4: *"Product strategy · UX/UI · Branding · Development"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.37,0,.63,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`www-allerstudio-com`)**:
- `._3N0scq_board { width:954px;height:594px;transform:scale(var(--s,1));transform-origin:0... }`
- `._3N0scq_svg { pointer-events:none;position:absolute;inset:0;overflow:visible }`
- `._3N0scq_progress { stroke-dasharray:1 1;stroke-dashoffset:1px;opacity:1;transition:stroke-d... }`
- `._3N0scq_node { z-index:2;width:24px;height:24px;position:absolute }`
- `._3N0scq_node img { width:100%;height:100%;position:absolute;inset:0 }`
- **Per-Selector Transition Rules**:
- **Selector `._3N0scq_progress`**: `transition: stroke-dashoffset var(--travel) var(--ease-in-out)` extracted from `www-allerstudio-com` stylesheet.
- **Selector `scq_board[data-resetting] ._3N0sc...`**: `transition: opacity .5s var(--ease-in-out)` extracted from `www-allerstudio-com` stylesheet.
- **Selector `._3N0scq_nodeOn`**: `transition: opacity .35s var(--ease-out), transform .5s var(--ease-out)` extracted from `www-allerstudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.header-in>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-allerstudio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
