---
title: "UI Prompt Blueprint: www-huxleysaga-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-huxleysaga-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0000`)"
---

# UI Design System & Master Generation Blueprint: www-huxleysaga-com

> **Huxley · Home** (https://www.huxleysaga.com/) — The HUXLEY® saga is an original sci-fi universe created by renowned concept artist Ben Mauro. Explore all the books, products, artwork an...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Huxley · Home** (`https://www.huxleysaga.com/`). The HUXLEY® saga is an original sci-fi universe created by renowned concept artist Ben Mauro. Explore all the books, products, artwork an...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `NB Architekt Light` for display copy (`10.23.26`) with `NB Architekt Regular` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1416px` container bounds (`gap: 12px`, padding `var(--layout-margin)`) with `cubic-bezier(.596,.003,0,1.033)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1416px` (live computed `main` `max-width`).
- **Canvas Lateral Padding & Spacing**: `var(--layout-margin)` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1416px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--layout-margin)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:950px)`, `@media (max-width:949px)`, `@media (max-width:949px)and (min-width:950px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1a1a1a` | `.page-showcase .showcase-box--h { background: #1a1a1a }` |
| **Interactive Accent / Highlight** | `#ff0000` | `:root .--red { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#666666` | `:root .--grey2 { color: #666666 }` |
| **Structural Hairline Border** | `#ffffff` | `.cta>span { border-bottom: #ffffff }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `#fff` | Canvas / Surface Token |
| `--white-0` | `hsla(0,0%,100%,0)` | Canvas / Surface Token |
| `--white-5` | `hsla(0,0%,100%,.05)` | Canvas / Surface Token |
| `--white-10` | `hsla(0,0%,100%,.1)` | Canvas / Surface Token |
| `--white-15` | `hsla(0,0%,100%,.15)` | Canvas / Surface Token |
| `--white-20` | `hsla(0,0%,100%,.2)` | Canvas / Surface Token |
| `--white-25` | `hsla(0,0%,100%,.25)` | Canvas / Surface Token |
| `--white-30` | `hsla(0,0%,100%,.3)` | Canvas / Surface Token |
| `--white-35` | `hsla(0,0%,100%,.35)` | Canvas / Surface Token |
| `--white-40` | `hsla(0,0%,100%,.4)` | Canvas / Surface Token |
| `--white-45` | `hsla(0,0%,100%,.45)` | Canvas / Surface Token |
| `--white-50` | `hsla(0,0%,100%,.5)` | Canvas / Surface Token |
| `--white-55` | `hsla(0,0%,100%,.55)` | Canvas / Surface Token |
| `--white-60` | `hsla(0,0%,100%,.6)` | Canvas / Surface Token |
| `--white-65` | `hsla(0,0%,100%,.65)` | Canvas / Surface Token |
| `--white-70` | `hsla(0,0%,100%,.7)` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `NB Architekt Light`.
- **Primary Body Stack**: `NB Architekt Regular`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78.3014px`, `line-height: 70.4712px`, `font-weight: 300`, `letter-spacing: 1.6px`); rule `,h1` (`font-size: clamp(80px,80px + 0vw,80px)`, `line-height: 90%`, `letter-spacing: 1.6px`, `font-weight: 300`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 400`, `letter-spacing: 1.2px`); rule `,h2` (`font-size: clamp(32px,32px + 0vw,32px)`, `line-height: 100%`, `letter-spacing: 1.92px`, `font-weight: 300`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `,p` (`letter-spacing: 12%`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.596,.003,0,1.033)`, `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.fade-enter-active`**: `transition: opacity var(--d-fast) steps(3)` extracted from `www-huxleysaga-com` stylesheet.
- **Selector `.fade-leave-active`**: `transition: opacity var(--d-fast) steps(3)` extracted from `www-huxleysaga-com` stylesheet.
- **Selector `.page-enter-active`**: `transition: opacity var(--d-medium) var(--ease-in-out-quint)` extracted from `www-huxleysaga-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.596,.003,0,1.033)`)**: Governs interactive state transitions across `<header.e-nav>` and `<section.s-small-header>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Huxley · Home                              │
│ ====================================================================== │
│ [ <header.e-nav> (1440x39px)          | H o m e · S t o r y · P r o  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.s-banner-hero> (w=1416px)                     | │
│ | H1: 10.23.26                                                       | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #ff0000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.s-small-header>) max-w: 1416px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | The HUXLEY® saga             |  | An original sci-fi universe  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.s-featured>) — STORY                       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.e-footer>   ) | https://www.huxleysaga.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.e-nav>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.s-banner-hero>) — 390px Vertical Lead         | │
│ | H1: 10.23.26                                                       | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.s-small-heade) — 1-Col Stack              | │
│ | [ Item 1: The HUXLEY® saga                                       ] | │
│ | [ Item 2: An original sci-fi universe created by renowned c...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.s-featured>) — 1-Col (STORY)                | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.e-footer>   ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.e-nav> — `www-huxleysaga-com`)**:
   - Landmark `<header class="e-nav">` (`1440x39px`) hosting `Huxley · Home` navigation (`H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`), DOM attributes (`data-hid="gtm"`, `data-hid="gtm-noscript"`, `data-hid="no-js-style"`, `data-v-db217464`), and stylesheet rule `root { --white:fff }`.
2. **Hero Stage & Focal Lead (<section.s-banner-hero> — `10.23.26`)**:
   - Landmark `<section class="s-banner-hero">` presenting display lead `10.23.26` and copy excerpt *"A post-apocalyptic sci-fi universe"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.s-small-header> — `The HUXLEY® saga`)**:
   - Landmark `<section class="s-small-header">` rendering section `The HUXLEY® saga` with copy *"S c r o l l t o e x p l o r e"*, asset references (`gtm.js`, `entry.B21Z6f7r.css`, `SvgMask.Bd2uXaPf.css`, `LabelHighlight.DTuRQ1tQ.css`), and grid rule `root .--white { color:fff }`.
4. **Interactive Detail & Feature Matrix (<section.s-featured> — `An original sci-fi universe create`)**:
   - Landmark `<section class="s-featured">` framing `An original sci-fi universe created by renowned c...` and `STORY` (*"V I E W T H E O R A C L E"*) with `#1a1a1a` surface cards, `#ff0000` accents, and `root .--white-0 { color:fff0 }`.
5. **Colophon & Global Directory Footer (<footer.e-footer> — `https://www.huxleysaga.com/`)**:
   - Landmark `<footer class="e-footer layout-block">` anchoring `Huxley · Home` footer links (`H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`), copy *"V I E W H U X L E Y"*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-huxleysaga-com (Huxley · Home)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-huxleysaga-com` (**Huxley · Home** — `https://www.huxleysaga.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0000`).
- **Identity & Domain Context**: The HUXLEY® saga is an original sci-fi universe created by renowned concept artist Ben Mauro. Explore all the books, products, artwork an...
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `NB Architekt Light` for display copy (`10.23.26`) with `NB Architekt Regular` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1416px` container bounds (`gap: 12px`, padding `var(--layout-margin)`) with `cubic-bezier(.596,.003,0,1.033)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-huxleysaga-com` in your global stylesheet:

:root {
  /* Huxley · Home (www-huxleysaga-com) — Live-Grounded CSS Variables */
  --white: #fff; /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-0: hsla(0,0%,100%,0); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-5: hsla(0,0%,100%,.05); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-10: hsla(0,0%,100%,.1); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-15: hsla(0,0%,100%,.15); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-20: hsla(0,0%,100%,.2); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-25: hsla(0,0%,100%,.25); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-30: hsla(0,0%,100%,.3); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-35: hsla(0,0%,100%,.35); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-40: hsla(0,0%,100%,.4); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-45: hsla(0,0%,100%,.45); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-50: hsla(0,0%,100%,.5); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-55: hsla(0,0%,100%,.55); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-60: hsla(0,0%,100%,.6); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-65: hsla(0,0%,100%,.65); /* Canvas / Surface Token (www-huxleysaga-com) */
  --white-70: hsla(0,0%,100%,.7); /* Canvas / Surface Token (www-huxleysaga-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#1a1a1a` — grounded in `.page-showcase .showcase-box--h { background: #1a1a1a }`
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `:root .--red { color: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#666666` — grounded in `:root .--grey2 { color: #666666 }`
- **Structural Hairline Border**: `#ffffff` — grounded in `.cta>span { border-bottom: #ffffff }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1416px` (live computed `main` `max-width`)
- **Padding & Gutters**: `var(--layout-margin)` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1416px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--layout-margin)` horizontal padding
- **Media Queries**: `@media (min-width:950px)`, `@media (max-width:949px)`, `@media (max-width:949px)and (min-width:950px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `NB Architekt Light`
- **Body Font Stack**: `NB Architekt Regular`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 78.3014px`, `line-height: 70.4712px`, `font-weight: 300`, `letter-spacing: 1.6px`); rule `,h1` (`font-size: clamp(80px,80px + 0vw,80px)`, `line-height: 90%`, `letter-spacing: 1.6px`, `font-weight: 300`)
- **H2 Section Rule**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 400`, `letter-spacing: 1.2px`); rule `,h2` (`font-size: clamp(32px,32px + 0vw,32px)`, `line-height: 100%`, `letter-spacing: 1.92px`, `font-weight: 300`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `,p` (`letter-spacing: 12%`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-huxleysaga-com` (`Huxley · Home`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.e-nav> — `www-huxleysaga-com`)**:
   - DOM & Selectors: Landmark `<header class="e-nav">` (`1440x39px`) hosting `Huxley · Home` navigation (`H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`), DOM attributes (`data-hid="gtm"`, `data-hid="gtm-noscript"`, `data-hid="no-js-style"`, `data-v-db217464`), and stylesheet rule `root { --white:fff }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.e-nav> — `www-huxleysaga-com`)` (`www-huxleysaga-com`) adapts across `@media (min-width:950px)`, `@media (max-width:949px)`, `@media (max-width:949px)and (min-width:950px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.596,.003,0,1.033)`, `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)` transitions and links `H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`.
2. **Hero Stage & Focal Lead (<section.s-banner-hero> — `10.23.26`)**:
   - DOM & Selectors: Landmark `<section class="s-banner-hero">` presenting display lead `10.23.26` and copy excerpt *"A post-apocalyptic sci-fi universe"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#ffffff` headline `10.23.26`.
3. **Primary Showcase & Content Grid (<section.s-small-header> — `The HUXLEY® saga`)**:
   - DOM & Selectors: Landmark `<section class="s-small-header">` rendering section `The HUXLEY® saga` with copy *"S c r o l l t o e x p l o r e"*, asset references (`gtm.js`, `entry.B21Z6f7r.css`, `SvgMask.Bd2uXaPf.css`, `LabelHighlight.DTuRQ1tQ.css`), and grid rule `root .--white { color:fff }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.s-small-header> — `The HUXLEY® saga`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1416px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--layout-margin)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.s-featured> — `An original sci-fi universe create`)**:
   - DOM & Selectors: Landmark `<section class="s-featured">` framing `An original sci-fi universe created by renowned c...` and `STORY` (*"V I E W T H E O R A C L E"*) with `#1a1a1a` surface cards, `#ff0000` accents, and `root .--white-0 { color:fff0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.s-featured> — `An original sci-fi universe create`)` uses `0px` (sharp unrounded corners) radii, `#ff0000` highlights, and assets (gtm.js, entry.B21Z6f7r.css, SvgMask.Bd2uXaPf.css).
5. **Colophon & Global Directory Footer (<footer.e-footer> — `https://www.huxleysaga.com/`)**:
   - DOM & Selectors: Landmark `<footer class="e-footer layout-block">` anchoring `Huxley · Home` footer links (`H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`), copy *"V I E W H U X L E Y"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.e-footer> — `https://www.huxleysaga.com/`)` aligns to `1416px` (live computed `main` `max-width`) with `var(--layout-margin)` lateral canvas padding with `12px` grid gap and attributes (data-hid="gtm", data-hid="gtm-noscript", data-hid="no-js-style").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A post-apocalyptic sci-fi universe"*
- Copy Excerpt 2: *"S c r o l l t o e x p l o r e"*
- Copy Excerpt 3: *"V I E W T H E O R A C L E"*
- Copy Excerpt 4: *"V I E W H U X L E Y"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.596,.003,0,1.033)`, `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)`
- **Extracted Stylesheet Rules (`www-huxleysaga-com`)**:
- `root { --white:fff }`
- `root .--white { color:fff }`
- `root .--white-0 { color:fff0 }`
- `root .--white-5 { color:ffffff0d }`
- `root .--white-10 { color:ffffff1a }`
- **Per-Selector Transition Rules**:
- **Selector `.fade-enter-active`**: `transition: opacity var(--d-fast) steps(3)` extracted from `www-huxleysaga-com` stylesheet.
- **Selector `.fade-leave-active`**: `transition: opacity var(--d-fast) steps(3)` extracted from `www-huxleysaga-com` stylesheet.
- **Selector `.page-enter-active`**: `transition: opacity var(--d-medium) var(--ease-in-out-quint)` extracted from `www-huxleysaga-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.596,.003,0,1.033)`)**: Governs interactive state transitions across `<header.e-nav>` and `<section.s-small-header>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-huxleysaga-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
