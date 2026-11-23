---
title: "UI Prompt Blueprint: www-unbelievablycrap-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-unbelievablycrap-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#e8271c`)"
---

# UI Design System & Master Generation Blueprint: www-unbelievablycrap-com

> **Liubomyr Ulytskyi - Digital Designer** (https://www.unbelievablycrap.com/) — Liubomyr Ulytskyi — Digital Designer, award-winning UI/UX Designer, art director, conceptualist.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Liubomyr Ulytskyi - Digital Designer** (`https://www.unbelievablycrap.com/`). Liubomyr Ulytskyi — Digital Designer, award-winning UI/UX Designer, art director, conceptualist.
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#e8271c`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#e8271c` accents.
  - **Grounded Typographic Hierarchy**: Pairs `PP Supply Sans` for display copy (`find your way out of here`) with `PP Supply Sans` and `PP Supply Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `6px`) with `cubic-bezier(.4,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 860px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width:720px)`, `@media (max-width: 720px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#393939` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#e8271c` | `.trk__btn:hover { color: #e8271c }` |
| **Secondary / Muted Copy** | `#393939` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#393939` | hairline divider derived from live computed `button` `color` (`computed_styles.json`) |
| **Variable Token (`--c-fog`)** | `#afafaf` | `var(--c-fog)` in `:root` |
| **Variable Token (`--c-slate`)** | `#6e6e6e` | `var(--c-slate)` in `:root` |
| **Variable Token (`--c-label`)** | `#636363` | `var(--c-label)` in `:root` |
| **Variable Token (`--c-fade`)** | `#c3c3c3` | `var(--c-fade)` in `:root` |
| **Variable Token (`--ui-grey`)** | `#c8c8c8` | `var(--ui-grey)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-mono` | `'PP Supply Mono',ui-monospace,'SF Mono','Roboto Mono',monospace` | Typography / Scale Token |
| `--c-white` | `#ffffff` | Canvas / Surface Token |
| `--c-fog` | `#afafaf` | Color / Atmospheric Token |
| `--c-slate` | `#6e6e6e` | Color / Atmospheric Token |
| `--c-label` | `#636363` | Color / Atmospheric Token |
| `--c-fade` | `#c3c3c3` | Color / Atmospheric Token |
| `--c-ink` | `#393939` | Typography Ink Token |
| `--hud-size` | `14px` | Layout / Spatial Grid Token |
| `--tracking` | `-0.04em` | Typography / Scale Token |
| `--ui-ink` | `#393939` | Typography Ink Token |
| `--ui-dim` | `rgba(57,57,57,.5)` | Color / Atmospheric Token |
| `--ui-red` | `#e8271c` | Color / Atmospheric Token |
| `--ui-grey` | `#c8c8c8` | Color / Atmospheric Token |
| `--ui-bar` | `#393939` | Color / Atmospheric Token |
| `--ui-10` | `10px` | Dimension / Scale Token |
| `--ui-14` | `14px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PP Supply Sans`.
- **Primary Body Stack**: `PP Supply Sans`.
- **Technical / Metadata Stack**: `PP Supply Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: observed font-size ladder: `128px`, `16px`, `10px`, `14px`, `var(--ui-10)`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 128px`, `line-height: 102px`, `font-weight: 400`, `letter-spacing: -5.12px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: var(--ui-10)`, `line-height: 10px`, `letter-spacing: -0.4px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-mono: 'PP Supply Mono',ui-monospace,'SF Mono','Roboto Mono',monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.16,.84,.32,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.hud`**: `transition: opacity .28s linear` extracted from `www-unbelievablycrap-com` stylesheet.
- **Selector `.ftr__bar`**: `transition: background .18s ease, color .18s ease` extracted from `www-unbelievablycrap-com` stylesheet.
- **Selector `.bar`**: `transition: transform var(--bar-out, 420ms) cubic-bezier(.4,0,.2,1)` extracted from `www-unbelievablycrap-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.ftr__nav>` and `<main.gate__bg>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Liubomyr Ulytskyi - Digital Designer       │
│ ====================================================================== │
│ [ <nav.ftr__nav> (181x10px)           | index · work · gallery · 404 ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.gate> (w=1440px)                                 | │
│ | H1: find your way out of here                                      | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #e8271c                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.gate__bg>) max-w: 1440px                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | CASE FILE: THE MAN BEHIND TH |  | The first mistake was assumi | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.gate__logo>) — He was 0looking for w          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bar>        ) | https://www.unbelievablycrap.com/    │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.ftr__nav>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.gate>) — 390px Vertical Lead                     | │
│ | H1: find your way out of here                                      | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.gate__bg>) — 1-Col Stack                     | │
│ | [ Item 1: CASE FILE: THE MAN BEHIND THE IMAGE                    ] | │
│ | [ Item 2: The first mistake was assuming Liubomyr was look       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.gate__logo>) — 1-Col (He was 0looking fo)      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bar>        ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.ftr__nav> — `www-unbelievablycrap-com`)**:
   - Landmark `<nav class="ftr__nav">` (`181x10px`) hosting `Liubomyr Ulytskyi - Digital Designer` navigation (`index · work · gallery · 404`), DOM attributes (`data-err-src="ERR_ART"`, `data-err-src="ERR_CARD"`, `data-mesh-var="FIGURE_LITE"`, `data-mesh-var="LOGO_MESH"`), and stylesheet rule `.ftr { position: fixed; inset: 0; z-index: 62; color: 000; pointer-events: none... }`.
2. **Hero Stage & Focal Lead (<main.gate> — `find your way out of here`)**:
   - Landmark `<main class="gate">` presenting display lead `find your way out of here` and copy excerpt *"CASE FILE: THE MAN BEHIND THE IMAGE"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.gate__bg> — `CASE FILE: THE MAN BEHIND THE IMAG`)**:
   - Landmark `<main class="gate__bg">` rendering section `CASE FILE: THE MAN BEHIND THE IMAGE` with copy *"The first mistake was assuming Liubomyr was looking for something"*, asset references (`favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`), and grid rule `.ftr.is-live { visibility: visible; }`.
4. **Interactive Detail & Feature Matrix (<main.gate__logo> — `The first mistake was assuming Liu`)**:
   - Landmark `<main class="gate__logo">` framing `The first mistake was assuming Liubomyr was look` and `He was 0looking for what 3was hiding.` (*"He was 0looking for what 3was hiding."*) with `#393939` surface cards, `#e8271c` accents, and `.ftr.is-open button { pointer-events: auto; }`.
5. **Colophon & Global Directory Footer (<footer.bar> — `https://www.unbelievablycrap.com/`)**:
   - Landmark `<footer class="bar">` anchoring `Liubomyr Ulytskyi - Digital Desi` footer links (`index · work · gallery · 404`), copy *"There’s a difference."*, and `#393939` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-unbelievablycrap-com (Liubomyr Ulytskyi - Digital Designer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-unbelievablycrap-com` (**Liubomyr Ulytskyi - Digital Designer** — `https://www.unbelievablycrap.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#e8271c`).
- **Identity & Domain Context**: Liubomyr Ulytskyi — Digital Designer, award-winning UI/UX Designer, art director, conceptualist.
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#e8271c`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#e8271c` accents.
  - **Grounded Typographic Hierarchy**: Pairs `PP Supply Sans` for display copy (`find your way out of here`) with `PP Supply Sans` and `PP Supply Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `6px`) with `cubic-bezier(.4,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-unbelievablycrap-com` in your global stylesheet:

:root {
  /* Liubomyr Ulytskyi - Digital Designer (www-unbelievablycrap-com) — Live-Grounded CSS Variables */
  --font-mono: 'PP Supply Mono',ui-monospace,'SF Mono','Roboto Mono',monospace; /* Typography / Scale Token (www-unbelievablycrap-com) */
  --c-white: #ffffff; /* Canvas / Surface Token (www-unbelievablycrap-com) */
  --c-fog: #afafaf; /* Color / Atmospheric Token (www-unbelievablycrap-com) */
  --c-slate: #6e6e6e; /* Color / Atmospheric Token (www-unbelievablycrap-com) */
  --c-label: #636363; /* Color / Atmospheric Token (www-unbelievablycrap-com) */
  --c-fade: #c3c3c3; /* Color / Atmospheric Token (www-unbelievablycrap-com) */
  --c-ink: #393939; /* Typography Ink Token (www-unbelievablycrap-com) */
  --hud-size: 14px; /* Layout / Spatial Grid Token (www-unbelievablycrap-com) */
  --tracking: -0.04em; /* Typography / Scale Token (www-unbelievablycrap-com) */
  --ui-ink: #393939; /* Typography Ink Token (www-unbelievablycrap-com) */
  --ui-dim: rgba(57,57,57,.5); /* Color / Atmospheric Token (www-unbelievablycrap-com) */
  --ui-red: #e8271c; /* Color / Atmospheric Token (www-unbelievablycrap-com) */
  --ui-grey: #c8c8c8; /* Color / Atmospheric Token (www-unbelievablycrap-com) */
  --ui-bar: #393939; /* Color / Atmospheric Token (www-unbelievablycrap-com) */
  --ui-10: 10px; /* Dimension / Scale Token (www-unbelievablycrap-com) */
  --ui-14: 14px; /* Dimension / Scale Token (www-unbelievablycrap-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#393939` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#e8271c` — grounded in `.trk__btn:hover { color: #e8271c }`
- **Secondary / Muted Copy**: `#393939` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#393939` — grounded in hairline divider derived from live computed `button` `color` (`computed_styles.json`)
- **Variable Token (`--c-fog`)**: `#afafaf` — grounded in `var(--c-fog)` in `:root`
- **Variable Token (`--c-slate`)**: `#6e6e6e` — grounded in `var(--c-slate)` in `:root`
- **Variable Token (`--c-label`)**: `#636363` — grounded in `var(--c-label)` in `:root`
- **Variable Token (`--c-fade`)**: `#c3c3c3` — grounded in `var(--c-fade)` in `:root`
- **Variable Token (`--ui-grey`)**: `#c8c8c8` — grounded in `var(--ui-grey)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `6px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (max-width: 860px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width:720px)`, `@media (max-width: 720px)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PP Supply Sans`
- **Body Font Stack**: `PP Supply Sans`
- **Monospace / Technical Font Stack**: `PP Supply Mono`
- **H1 Display Rule**: observed font-size ladder: `128px`, `16px`, `10px`, `14px`, `var(--ui-10)`
- **H2 Section Rule**: live computed `h2` (`font-size: 128px`, `line-height: 102px`, `font-weight: 400`, `letter-spacing: -5.12px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: var(--ui-10)`, `line-height: 10px`, `letter-spacing: -0.4px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-mono: 'PP Supply Mono',ui-monospace,'SF Mono','Roboto Mono',monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-unbelievablycrap-com` (`Liubomyr Ulytskyi - Digital Designer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.ftr__nav> — `www-unbelievablycrap-com`)**:
   - DOM & Selectors: Landmark `<nav class="ftr__nav">` (`181x10px`) hosting `Liubomyr Ulytskyi - Digital Designer` navigation (`index · work · gallery · 404`), DOM attributes (`data-err-src="ERR_ART"`, `data-err-src="ERR_CARD"`, `data-mesh-var="FIGURE_LITE"`, `data-mesh-var="LOGO_MESH"`), and stylesheet rule `.ftr { position: fixed; inset: 0; z-index: 62; color: 000; pointer-events: none... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.ftr__nav> — `www-unbelievablycrap-com`)` (`www-unbelievablycrap-com`) adapts across `@media (max-width: 860px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width:720px)`, `@media (max-width: 720px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.16,.84,.32,1)` transitions and links `index · work · gallery · 404`.
2. **Hero Stage & Focal Lead (<main.gate> — `find your way out of here`)**:
   - DOM & Selectors: Landmark `<main class="gate">` presenting display lead `find your way out of here` and copy excerpt *"CASE FILE: THE MAN BEHIND THE IMAGE"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#ffffff` headline `find your way out of here`.
3. **Primary Showcase & Content Grid (<main.gate__bg> — `CASE FILE: THE MAN BEHIND THE IMAG`)**:
   - DOM & Selectors: Landmark `<main class="gate__bg">` rendering section `CASE FILE: THE MAN BEHIND THE IMAGE` with copy *"The first mistake was assuming Liubomyr was looking for something"*, asset references (`favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`), and grid rule `.ftr.is-live { visibility: visible; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.gate__bg> — `CASE FILE: THE MAN BEHIND THE IMAG`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.gate__logo> — `The first mistake was assuming Liu`)**:
   - DOM & Selectors: Landmark `<main class="gate__logo">` framing `The first mistake was assuming Liubomyr was look` and `He was 0looking for what 3was hiding.` (*"He was 0looking for what 3was hiding."*) with `#393939` surface cards, `#e8271c` accents, and `.ftr.is-open button { pointer-events: auto; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.gate__logo> — `The first mistake was assuming Liu`)` uses `0px` (sharp unrounded corners) radii, `#e8271c` highlights, and assets (favicon.ico, favicon-32x32.png, favicon-16x16.png).
5. **Colophon & Global Directory Footer (<footer.bar> — `https://www.unbelievablycrap.com/`)**:
   - DOM & Selectors: Landmark `<footer class="bar">` anchoring `Liubomyr Ulytskyi - Digital Desi` footer links (`index · work · gallery · 404`), copy *"There’s a difference."*, and `#393939` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bar> — `https://www.unbelievablycrap.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `6px` lateral canvas padding with `16px` grid gap and attributes (data-err-src="ERR_ART", data-err-src="ERR_CARD", data-mesh-var="FIGURE_LITE").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"CASE FILE: THE MAN BEHIND THE IMAGE"*
- Copy Excerpt 2: *"The first mistake was assuming Liubomyr was looking for something."*
- Copy Excerpt 3: *"He was 0looking for what 3was hiding."*
- Copy Excerpt 4: *"There’s a difference."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.16,.84,.32,1)`
- **Extracted Stylesheet Rules (`www-unbelievablycrap-com`)**:
- `.ftr { position: fixed; inset: 0; z-index: 62; color: 000; pointer-events: none... }`
- `.ftr.is-live { visibility: visible; }`
- `.ftr.is-open button { pointer-events: auto; }`
- `.ftr__in { position: absolute; inset: 0; opacity: var(--ftr-a, 0); clip-path: path(... }`
- `.ftr__title > span { display: block; }`
- **Per-Selector Transition Rules**:
- **Selector `.hud`**: `transition: opacity .28s linear` extracted from `www-unbelievablycrap-com` stylesheet.
- **Selector `.ftr__bar`**: `transition: background .18s ease, color .18s ease` extracted from `www-unbelievablycrap-com` stylesheet.
- **Selector `.bar`**: `transition: transform var(--bar-out, 420ms) cubic-bezier(.4,0,.2,1)` extracted from `www-unbelievablycrap-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.ftr__nav>` and `<main.gate__bg>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-unbelievablycrap-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
