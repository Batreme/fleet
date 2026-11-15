---
title: "UI Prompt Blueprint: rozaliabomawrites-com"
date: 2026-11-15
target: "[[overview|rozaliabomawrites-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#9ca3af`)"
---

# UI Design System & Master Generation Blueprint: rozaliabomawrites-com

> **Rozalia Boma — Multicultural Romance Author** (https://rozaliabomawrites.com/) — Official site of Rozalia Boma, author of multicultural YA romance. Books, diary entries, guestbook and newsletter.

![Desktop Viewport Capture (1440x6121)](file:///root/projects/fleet/wiki/targets/rozaliabomawrites-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Rozalia Boma — Multicultural Romance Author** (`https://rozaliabomawrites.com/`). Official site of Rozalia Boma, author of multicultural YA romance. Books, diary entries, guestbook and newsletter.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#9ca3af`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--w2w-start-background-color)` in `:root`) paired with `#fff` primary typography and `#9ca3af` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Gochi Hand Fallback` for display copy (`Rozalia Boma — writing multicultural`) with `Barlow Condensed` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .5rem`, padding `2rem`) with `cubic-bezier(.4,0,.6,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/rozaliabomawrites-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6121px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `rozaliabomawrites-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `var(--radius)`, `999px`, `14px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 640px)`, `@media (min-width: 1400px)`, `@media (min-width: 640px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--w2w-start-background-color)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--normal-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e5e7eb` | `:after { border-color: #e5e7eb }` |
| **Interactive Accent / Highlight** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Secondary / Muted Copy** | `#ffa500` | `.os-window--orange { border-color: orange }` (`#ffa500`) |
| **Structural Hairline Border** | `#93ceec` | `.os-window--babyblue { border-color: #93ceec }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `290 80% 92%` | Canvas / Surface Token |
| `--foreground` | `320 60% 18%` | Typography Ink Token |
| `--card` | `0 0% 100%` | Dimension / Scale Token |
| `--card-foreground` | `320 60% 18%` | Typography Ink Token |
| `--popover` | `0 0% 100%` | Dimension / Scale Token |
| `--popover-foreground` | `320 60% 18%` | Typography Ink Token |
| `--primary` | `330 95% 60%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |
| `--secondary` | `280 85% 78%` | Brand / Palette Token |
| `--secondary-foreground` | `320 60% 18%` | Typography Ink Token |
| `--muted` | `320 60% 95%` | Dimension / Scale Token |
| `--muted-foreground` | `320 25% 45%` | Typography Ink Token |
| `--accent` | `195 90% 75%` | Brand / Palette Token |
| `--accent-foreground` | `320 60% 18%` | Typography Ink Token |
| `--destructive` | `0 84% 60%` | Dimension / Scale Token |
| `--destructive-foreground` | `0 0% 100%` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Gochi Hand Fallback`.
- **Primary Body Stack**: `Barlow Condensed`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `6em`).
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -.02em`, `font-weight: 400`).
- **Body Copy**: rule `p` (`line-height: 1.65`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `6em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn-bubble`**: `transition: transform .12s ease,box-shadow .12s ease` extracted from `rozaliabomawrites-com` stylesheet.
- **Selector `.win98-btn`**: `transition: none` extracted from `rozaliabomawrites-com` stylesheet.
- **Selector `.y2k-textbox`**: `transition: transform .35s ease,box-shadow .35s ease` extracted from `rozaliabomawrites-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<nav.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Rozalia Boma — Multicultural Romance Autho │
│ ====================================================================== │
│ [ <nav.fixed>              | Home · Author · Books · Blog · Guestbo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.fixed>                                      |   │
│ | H1: Rozalia Boma — writing multicultural romances                |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #9ca3af        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | w r i t i n g m u l t i c u  |  | H i ! I ' m R o z a l i a B  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem ) | │
│ | [<nav.fixed>] -> [<section.fixed>] -> [<section.relative>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://rozaliabomawrites.com/     │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.fixed> — `rozaliabomawrites-com`)**:
   - Landmark `<nav class="fixed top-0">` hosting `Rozalia Boma — Multicultural Romance` navigation (`Home · Author · Books · Blog · Guestbook`), DOM attributes (`data-artifact-kind="dwl_content_hash"`, `data-artifact-id="db5c4db312500dfaed9e3..."`, `data-commit-sha="37366776bd44c18a989e4..."`, `data-context-token="v1.eyJwcm9qZWN0X2lkIj..."`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Rozalia Boma — writing multicultur`)**:
   - Landmark `<section class="fixed">` presenting display lead `Rozalia Boma — writing multicultural romances` and copy excerpt *"Rozalia Boma Writes is loading"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `w r i t i n g m u l t i c u l t u `)**:
   - Landmark `<section class="relative min-h-screen">` rendering section `w r i t i n g m u l t i c u l t u r a l r o m a n...` with copy *"Beware! Black Eastern European baddies on the rise!"*, asset references (`holo-sky-bg-C4iYYOxV.webp`, `fonts.googleapis.com`, `fonts.gstatic.com`, `sykz-yx0lLcxQaSIhS23-w.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `H i ! I ' m R o z a l i a B o m a `)**:
   - Landmark `<section class="relative w-full">` framing `H i ! I ' m R o z a l i a B o m a .` and `T h e B o o k` (*"w r i t i n g m u l t i c u l t u r a l"*) with `#e5e7eb` surface cards, `#9ca3af` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://rozaliabomawrites.com/`)**:
   - Landmark `<footer class="relative z-10">` anchoring `Rozalia Boma — Multicultural Rom` footer links (`Home · Author · Books · Blog · Guestbook`), copy *"m u l t i c u l t u r a l"*, and `#93ceec` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: rozaliabomawrites-com (Rozalia Boma — Multicultural Romance Author)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `rozaliabomawrites-com` (**Rozalia Boma — Multicultural Romance Author** — `https://rozaliabomawrites.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#9ca3af`).
- **Identity & Domain Context**: Official site of Rozalia Boma, author of multicultural YA romance. Books, diary entries, guestbook and newsletter.
- **Primary Substrate**: `#000` (`var(--w2w-start-background-color)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#9ca3af`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--w2w-start-background-color)` in `:root`) paired with `#fff` primary typography and `#9ca3af` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Gochi Hand Fallback` for display copy (`Rozalia Boma — writing multicultural`) with `Barlow Condensed` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .5rem`, padding `2rem`) with `cubic-bezier(.4,0,.6,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `rozaliabomawrites-com` in your global stylesheet:

:root {
  /* Rozalia Boma — Multicultural Romance Author (rozaliabomawrites-com) — Ground-Truth Extracted CSS Variables */
  --background: 290 80% 92%; /* Canvas / Surface Token (rozaliabomawrites-com) */
  --foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --card: 0 0% 100%; /* Dimension / Scale Token (rozaliabomawrites-com) */
  --card-foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --popover: 0 0% 100%; /* Dimension / Scale Token (rozaliabomawrites-com) */
  --popover-foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --primary: 330 95% 60%; /* Brand / Palette Token (rozaliabomawrites-com) */
  --primary-foreground: 0 0% 100%; /* Typography Ink Token (rozaliabomawrites-com) */
  --secondary: 280 85% 78%; /* Brand / Palette Token (rozaliabomawrites-com) */
  --secondary-foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --muted: 320 60% 95%; /* Dimension / Scale Token (rozaliabomawrites-com) */
  --muted-foreground: 320 25% 45%; /* Typography Ink Token (rozaliabomawrites-com) */
  --accent: 195 90% 75%; /* Brand / Palette Token (rozaliabomawrites-com) */
  --accent-foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --destructive: 0 84% 60%; /* Dimension / Scale Token (rozaliabomawrites-com) */
  --destructive-foreground: 0 0% 100%; /* Typography Ink Token (rozaliabomawrites-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--w2w-start-background-color)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--normal-bg)` in `:root`
- **Elevated Surface / Card Substrate**: `#e5e7eb` — grounded in `:after { border-color: #e5e7eb }`
- **Interactive Accent / Highlight**: `#9ca3af` — grounded in `textarea::-moz-placeholder { color: #9ca3af }`
- **Secondary / Muted Copy**: `#ffa500` — grounded in `.os-window--orange { border-color: orange }` (`#ffa500`)
- **Structural Hairline Border**: `#93ceec` — grounded in `.os-window--babyblue { border-color: #93ceec }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6121px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `rozaliabomawrites-com` stylesheet
- **Padding & Gutters**: `2rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (max-width: 640px)`, `@media (min-width: 1400px)`, `@media (min-width: 640px)`, `@media (min-width: 768px)`
- **Corner Radii**: `var(--radius)`, `999px`, `14px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Gochi Hand Fallback`
- **Body Font Stack**: `Barlow Condensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `6em`)
- **H2 Section Rule**: rule `h2` (`letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy Rule**: rule `p` (`line-height: 1.65`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `6em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `rozaliabomawrites-com` (`Rozalia Boma — Multicultural Romance Author`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.fixed> — `rozaliabomawrites-com`)**:
   - DOM & Selectors: Landmark `<nav class="fixed top-0">` hosting `Rozalia Boma — Multicultural Romance` navigation (`Home · Author · Books · Blog · Guestbook`), DOM attributes (`data-artifact-kind="dwl_content_hash"`, `data-artifact-id="db5c4db312500dfaed9e3..."`, `data-commit-sha="37366776bd44c18a989e4..."`, `data-context-token="v1.eyJwcm9qZWN0X2lkIj..."`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.fixed> — `rozaliabomawrites-com`)` (`rozaliabomawrites-com`) adapts across `@media (max-width: 640px)`, `@media (min-width: 1400px)`, `@media (min-width: 640px)`, `@media (min-width: 768px)` with `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `Home · Author · Books · Blog · Guestbook`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Rozalia Boma — writing multicultur`)**:
   - DOM & Selectors: Landmark `<section class="fixed">` presenting display lead `Rozalia Boma — writing multicultural romances` and copy excerpt *"Rozalia Boma Writes is loading"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×6121px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Rozalia Boma — writing multicultural romances`.
3. **Primary Showcase & Content Grid (<section.relative> — `w r i t i n g m u l t i c u l t u `)**:
   - DOM & Selectors: Landmark `<section class="relative min-h-screen">` rendering section `w r i t i n g m u l t i c u l t u r a l r o m a n...` with copy *"Beware! Black Eastern European baddies on the rise!"*, asset references (`holo-sky-bg-C4iYYOxV.webp`, `fonts.googleapis.com`, `fonts.gstatic.com`, `sykz-yx0lLcxQaSIhS23-w.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `w r i t i n g m u l t i c u l t u `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `H i ! I ' m R o z a l i a B o m a `)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` framing `H i ! I ' m R o z a l i a B o m a .` and `T h e B o o k` (*"w r i t i n g m u l t i c u l t u r a l"*) with `#e5e7eb` surface cards, `#9ca3af` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `H i ! I ' m R o z a l i a B o m a `)` uses `var(--radius)`, `999px`, `14px`, `8px` radii, `#9ca3af` highlights, and assets (holo-sky-bg-C4iYYOxV.webp, fonts.googleapis.com, fonts.gstatic.com).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://rozaliabomawrites.com/`)**:
   - DOM & Selectors: Landmark `<footer class="relative z-10">` anchoring `Rozalia Boma — Multicultural Rom` footer links (`Home · Author · Books · Blog · Guestbook`), copy *"m u l t i c u l t u r a l"*, and `#93ceec` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://rozaliabomawrites.com/`)` aligns to `640px` extracted from `rozaliabomawrites-com` stylesheet with `2rem` lateral canvas padding with `.5rem` grid gap and attributes (data-artifact-kind="dwl_content_hash", data-artifact-id="db5c4db312500dfaed9e3...", data-commit-sha="37366776bd44c18a989e4...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Rozalia Boma Writes is loading"*
- Copy Excerpt 2: *"Beware! Black Eastern European baddies on the rise!"*
- Copy Excerpt 3: *"w r i t i n g m u l t i c u l t u r a l"*
- Copy Excerpt 4: *"m u l t i c u l t u r a l"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`rozaliabomawrites-com`)**:
- `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.btn-bubble`**: `transition: transform .12s ease,box-shadow .12s ease` extracted from `rozaliabomawrites-com` stylesheet.
- **Selector `.win98-btn`**: `transition: none` extracted from `rozaliabomawrites-com` stylesheet.
- **Selector `.y2k-textbox`**: `transition: transform .35s ease,box-shadow .35s ease` extracted from `rozaliabomawrites-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<nav.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `rozaliabomawrites-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
