---
title: "UI Prompt Blueprint: www-jarnket-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-jarnket-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f5` / `#2563eb`)"
---

# UI Design System & Master Generation Blueprint: www-jarnket-com

> **JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane** (https://www.jarnket.com/) — Software engineer in Vientiane, Laos and WorldSkills ASEAN 2025 Web Technologies Expert, building fast, accessible React and Next.js inte...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane** (`https://www.jarnket.com/`). Software engineer in Vientiane, Laos and WorldSkills ASEAN 2025 Web Technologies Expert, building fast, accessible React and Next.js inte...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f5` / `#2563eb`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f5f5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1a1a1a` primary typography and `#2563eb` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Chakra Petch` for display copy (`JARN KET`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1376px` container bounds (`gap: .125rem`, padding `.125rem`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1376px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `.125rem` lateral canvas padding with `.125rem` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1376px`, `gap: .125rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.125rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1a` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f4f5f7` | `var(--jk-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#2563eb` | `var(--site-accent)` in `:root` |
| **Secondary / Muted Copy** | `#62666e` | `var(--jk-muted)` in `:root` |
| **Structural Hairline Border** | `#d7d9dc` | `var(--jk-line)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `0 0% 96%` | Canvas / Surface Token |
| `--foreground` | `0 0% 10%` | Typography Ink Token |
| `--card` | `0 0% 98%` | Dimension / Scale Token |
| `--card-foreground` | `0 0% 10%` | Typography Ink Token |
| `--popover` | `0 0% 98%` | Dimension / Scale Token |
| `--popover-foreground` | `0 0% 10%` | Typography Ink Token |
| `--primary` | `0 0% 10%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 96%` | Typography Ink Token |
| `--secondary` | `0 0% 92%` | Brand / Palette Token |
| `--secondary-foreground` | `0 0% 10%` | Typography Ink Token |
| `--muted` | `0 0% 91%` | Dimension / Scale Token |
| `--muted-foreground` | `0 0% 40%` | Typography Ink Token |
| `--accent` | `0 0% 90%` | Brand / Palette Token |
| `--accent-foreground` | `0 0% 10%` | Typography Ink Token |
| `--destructive` | `0 72% 48%` | Dimension / Scale Token |
| `--destructive-foreground` | `0 0% 96%` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Chakra Petch`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 151.176px`, `line-height: 123.965px`, `font-weight: 600`, `letter-spacing: -3.02353px`); CSS variables `--font-display: "Chakra Petch", "Chakra Petch Fallback"`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 129.6px`, `line-height: 111.456px`, `font-weight: 600`, `letter-spacing: -1.944px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .001ms!important` extracted from `www-jarnket-com` stylesheet.
- **Selector `.transition`**: `transition: .15s` extracted from `www-jarnket-com` stylesheet.
- **Selector `border-color\]`**: `transition: .15s` extracted from `www-jarnket-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.jk-flood>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — JarnKet · Ketsadaphone Boutpanyda, web eng │
│ ====================================================================== │
│ [ <header.inset-x-0> (1440x73px)      | Index · Work · Field notes · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative> (w=1440px)                          | │
│ | H1: JARN KET                                                       | │
│ | Substrate: #f5f5f5 | Ink: #1a1a1a | Accent: #2563eb                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.jk-flood>) max-w: 1376px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | J A R N K E T                |  | T o o l k i t                | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.relative:nth(2)>) — UI & Styling           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.jk-flood>   ) | https://www.jarnket.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .125rem)    │
│ ====================================================================== │
│ [ HEADER BAR (<header.inset-x-0>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.relative>) — 390px Vertical Lead              | │
│ | H1: JARN KET                                                       | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.jk-flood>) — 1-Col Stack                  | │
│ | [ Item 1: J A R N K E T                                          ] | │
│ | [ Item 2: T o o l k i t                                          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.relative:nth(2)) — 1-Col (UI & Styling)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.jk-flood>   ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-jarnket-com`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x73px`) hosting `JarnKet · Ketsadaphone Boutpanyda, w` navigation (`Index · Work · Field notes · Gallery · GitHub`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`), and stylesheet rule `._8NX9hq_className { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `JARN KET`)**:
   - Landmark `<section class="relative">` presenting display lead `JARN KET` and copy excerpt *"Ketsadaphone Boutpanyda — building fast, accessible interfaces wi"* over `#f5f5f5` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.jk-flood> — `J A R N K E T`)**:
   - Landmark `<section class="jk-flood pb-28">` rendering section `J A R N K E T` with copy *"Web Technologies Expert @ WorldSkills ASEAN 2025"*, asset references (`1ccf8ef962b3f693-s.p.2xt4dxqx4hw9...`, `797e433ab948586e-s.p.1v5bejj26fx9...`, `8457265da2739722-s.p.00okbctd204v...`, `caa3a2e1cccd8315-s.p.0zr6hhvz-h9n...`), and grid rule `._8NX9hq_variable { --font-geist:"Geist", "Geist Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative:nth(2)> — `T o o l k i t`)**:
   - Landmark `<section class="relative">` framing `T o o l k i t` and `UI & Styling` (*"Software Engineer @BCEL Bank Software Engineer @BCEL Bank, Web Te"*) with `#f4f5f7` surface cards, `#2563eb` accents, and `.z61v7q_className { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.jk-flood> — `https://www.jarnket.com/`)**:
   - Landmark `<footer class="jk-flood relative">` anchoring `JarnKet · Ketsadaphone Boutpanyd` footer links (`Index · Work · Field notes · Gallery · GitHub`), copy *"Software Engineer @BCEL Bank"*, and `#d7d9dc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-jarnket-com (JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-jarnket-com` (**JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane** — `https://www.jarnket.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f5` / `#2563eb`).
- **Identity & Domain Context**: Software engineer in Vientiane, Laos and WorldSkills ASEAN 2025 Web Technologies Expert, building fast, accessible React and Next.js inte...
- **Primary Substrate**: `#f5f5f5` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1a1a1a`, **Accent / Highlight**: `#2563eb`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f5f5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1a1a1a` primary typography and `#2563eb` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Chakra Petch` for display copy (`JARN KET`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1376px` container bounds (`gap: .125rem`, padding `.125rem`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-jarnket-com` in your global stylesheet:

:root {
  /* JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane (www-jarnket-com) — Live-Grounded CSS Variables */
  --background: 0 0% 96%; /* Canvas / Surface Token (www-jarnket-com) */
  --foreground: 0 0% 10%; /* Typography Ink Token (www-jarnket-com) */
  --card: 0 0% 98%; /* Dimension / Scale Token (www-jarnket-com) */
  --card-foreground: 0 0% 10%; /* Typography Ink Token (www-jarnket-com) */
  --popover: 0 0% 98%; /* Dimension / Scale Token (www-jarnket-com) */
  --popover-foreground: 0 0% 10%; /* Typography Ink Token (www-jarnket-com) */
  --primary: 0 0% 10%; /* Brand / Palette Token (www-jarnket-com) */
  --primary-foreground: 0 0% 96%; /* Typography Ink Token (www-jarnket-com) */
  --secondary: 0 0% 92%; /* Brand / Palette Token (www-jarnket-com) */
  --secondary-foreground: 0 0% 10%; /* Typography Ink Token (www-jarnket-com) */
  --muted: 0 0% 91%; /* Dimension / Scale Token (www-jarnket-com) */
  --muted-foreground: 0 0% 40%; /* Typography Ink Token (www-jarnket-com) */
  --accent: 0 0% 90%; /* Brand / Palette Token (www-jarnket-com) */
  --accent-foreground: 0 0% 10%; /* Typography Ink Token (www-jarnket-com) */
  --destructive: 0 72% 48%; /* Dimension / Scale Token (www-jarnket-com) */
  --destructive-foreground: 0 0% 96%; /* Typography Ink Token (www-jarnket-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5f5f5` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1a1a1a` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f4f5f7` — grounded in `var(--jk-bg)` in `:root`
- **Interactive Accent / Highlight**: `#2563eb` — grounded in `var(--site-accent)` in `:root`
- **Secondary / Muted Copy**: `#62666e` — grounded in `var(--jk-muted)` in `:root`
- **Structural Hairline Border**: `#d7d9dc` — grounded in `var(--jk-line)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1376px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `.125rem` lateral canvas padding with `.125rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1376px`, `gap: .125rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.125rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Chakra Petch`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 151.176px`, `line-height: 123.965px`, `font-weight: 600`, `letter-spacing: -3.02353px`); CSS variables `--font-display: "Chakra Petch", "Chakra Petch Fallback"`
- **H2 Section Rule**: live computed `h2` (`font-size: 129.6px`, `line-height: 111.456px`, `font-weight: 600`, `letter-spacing: -1.944px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-jarnket-com` (`JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-jarnket-com`)**:
   - DOM & Selectors: Landmark `<header class="inset-x-0 top-0">` (`1440x73px`) hosting `JarnKet · Ketsadaphone Boutpanyda, w` navigation (`Index · Work · Field notes · Gallery · GitHub`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`), and stylesheet rule `._8NX9hq_className { font-family:Geist,Geist Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.inset-x-0> — `www-jarnket-com`)` (`www-jarnket-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Index · Work · Field notes · Gallery · GitHub`.
2. **Hero Stage & Focal Lead (<section.relative> — `JARN KET`)**:
   - DOM & Selectors: Landmark `<section class="relative">` presenting display lead `JARN KET` and copy excerpt *"Ketsadaphone Boutpanyda — building fast, accessible interfaces wi"* over `#f5f5f5` canvas and `#1a1a1a` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#f5f5f5` background with `#1a1a1a` headline `JARN KET`.
3. **Primary Showcase & Content Grid (<section.jk-flood> — `J A R N K E T`)**:
   - DOM & Selectors: Landmark `<section class="jk-flood pb-28">` rendering section `J A R N K E T` with copy *"Web Technologies Expert @ WorldSkills ASEAN 2025"*, asset references (`1ccf8ef962b3f693-s.p.2xt4dxqx4hw9...`, `797e433ab948586e-s.p.1v5bejj26fx9...`, `8457265da2739722-s.p.00okbctd204v...`, `caa3a2e1cccd8315-s.p.0zr6hhvz-h9n...`), and grid rule `._8NX9hq_variable { --font-geist:"Geist", "Geist Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.jk-flood> — `J A R N K E T`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1376px`, `gap: .125rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.125rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative:nth(2)> — `T o o l k i t`)**:
   - DOM & Selectors: Landmark `<section class="relative">` framing `T o o l k i t` and `UI & Styling` (*"Software Engineer @BCEL Bank Software Engineer @BCEL Bank, Web Te"*) with `#f4f5f7` surface cards, `#2563eb` accents, and `.z61v7q_className { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative:nth(2)> — `T o o l k i t`)` uses `.3125rem`, `.375rem`, `.25rem`, `2px` radii, `#2563eb` highlights, and assets (1ccf8ef962b3f693-s.p.2xt4dxqx4hw9..., 797e433ab948586e-s.p.1v5bejj26fx9..., 8457265da2739722-s.p.00okbctd204v...).
5. **Colophon & Global Directory Footer (<footer.jk-flood> — `https://www.jarnket.com/`)**:
   - DOM & Selectors: Landmark `<footer class="jk-flood relative">` anchoring `JarnKet · Ketsadaphone Boutpanyd` footer links (`Index · Work · Field notes · Gallery · GitHub`), copy *"Software Engineer @BCEL Bank"*, and `#d7d9dc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.jk-flood> — `https://www.jarnket.com/`)` aligns to `1376px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `.125rem` lateral canvas padding with `.125rem` grid gap and attributes (data-precedence="next", data-href="/_next/static/immutab...", data-sdkn="@vercel/analytics/react").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Ketsadaphone Boutpanyda — building fast, accessible interfaces with React & Next.j..."*
- Copy Excerpt 2: *"Web Technologies Expert @ WorldSkills ASEAN 2025"*
- Copy Excerpt 3: *"Software Engineer @BCEL Bank Software Engineer @BCEL Bank, Web Techologies Expert..."*
- Copy Excerpt 4: *"Software Engineer @BCEL Bank"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`www-jarnket-com`)**:
- `._8NX9hq_className { font-family:Geist,Geist Fallback;font-style:normal }`
- `._8NX9hq_variable { --font-geist:"Geist", "Geist Fallback" }`
- `.z61v7q_className { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`
- `.z61v7q_variable { --font-geist-mono:"Geist Mono", "Geist Mono Fallback" }`
- `after { box-sizing:border-box;border:0 solid e5e7eb }`
- **Per-Selector Transition Rules**:
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .001ms!important` extracted from `www-jarnket-com` stylesheet.
- **Selector `.transition`**: `transition: .15s` extracted from `www-jarnket-com` stylesheet.
- **Selector `border-color\]`**: `transition: .15s` extracted from `www-jarnket-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.jk-flood>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-jarnket-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
