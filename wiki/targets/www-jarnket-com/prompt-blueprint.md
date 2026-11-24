---
title: "UI Prompt Blueprint: www-jarnket-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-jarnket-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f5` / `#2563eb`)"
---

# UI Design System & Master Generation Blueprint: www-jarnket-com

> **JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane** (https://www.jarnket.com/) — Software engineer in Vientiane, Laos and WorldSkills ASEAN 2025 Web Technologies Expert, building fast, accessible React and Next.js inte...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane** (`https://www.jarnket.com/`). Software engineer in Vientiane, Laos and WorldSkills ASEAN 2025 Web Technologies Expert, building fast, accessible React and Next.js inte...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f5` / `#2563eb`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f5f5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1a1a1a` primary typography and `#2563eb` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Chakra Petch` for display copy (`JARN KET`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1376px` container bounds (`gap: .125rem`, padding `.125rem`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=9731px` / doc `10631px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
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
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `10631px`, deepest scrollY reached `9731px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Nav / Drawer Probe (`MENU`)**: Triggered visual change (pixel diff `101.203`, captured in `assets/state-nav.webp`); revealed links: INDEX, WORK, FIELD NOTES, GALLERY, GITHUB, Software Engineer @BC....
- **Hover Physics (`primary_cta` · `JK JARNKET — HOME`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Interactive Control Probe (`accordion` · `01 BANQUE POUR LE COMMERCE EXTERI...`)**: Triggered visual diff `35.673` (attr ` -> `, captured in `assets/state-interactive.webp`).
- **Theme Toggle Probe (`Switch to dark mode`)**: Toggled body background `rgb(245, 245, 245)` -> `rgb(10, 10, 10)` and ink `rgb(26, 26, 26)` -> `rgb(245, 245, 245)`.
- **Route Transition Architecture**: First internal navigation (`/blog`) measured as `direct` in `946ms`.

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
   - Landmark `<section class="relative">` framing `T o o l k i t` and `UI & Styling` (*"Web Techologies Expert @World Skills ASEAN 2025 Software Engineer"*) with `#f4f5f7` surface cards, `#2563eb` accents, and `.z61v7q_className { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.jk-flood> — `https://www.jarnket.com/`)**:
   - Landmark `<footer class="jk-flood relative">` anchoring `JarnKet · Ketsadaphone Boutpanyd` footer links (`Index · Work · Field notes · Gallery · GitHub`), copy *"Web Techologies Expert @World Skills ASEAN 2025"*, and `#d7d9dc` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `JARN KET` · sticky/fixed elements: `3`
- **Step 02** (`y=850px`, `9%`): Active landmark `Section @ 9%` · sticky/fixed elements: `2`
- **Step 03** (`y=2550px`, `26%`): Active landmark `TOOLKIT` · sticky/fixed elements: `1`
- **Step 04** (`y=4250px`, `44%`): Active landmark `LAOSWAY` · sticky/fixed elements: `1`
- **Step 05** (`y=5950px`, `61%`): Active landmark `VANGUARD AI` · sticky/fixed elements: `1`
- **Step 06** (`y=7650px`, `79%`): Active landmark `PHAPAY HACKATHON 2024` · sticky/fixed elements: `1`
- **Step 07** (`y=9350px`, `96%`): Active landmark `HAVE SOMETHING TO BUILD?` · sticky/fixed elements: `1`
- **Step 08** (`y=9731px`, `100%`): Active landmark `HAVE SOMETHING TO BUILD?` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/blog`)**: `https://www.jarnket.com/blog` — H1: `WRITING`, scrollHeight `2462px`, transition `direct` (`946ms`)
- **Detail Route (`/work/seemuehub`)**: `https://www.jarnket.com/work/seemuehub` — H1: `SEEMUEHUB (ສີມືຮັບ )`, scrollHeight `3642px`, transition `direct` (`652ms`)
- **Detail Route (`/work/laosway`)**: `https://www.jarnket.com/work/laosway` — H1: `LAOSWAY`, scrollHeight `3612px`, transition `direct` (`878ms`)

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
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
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
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f5f5f5` background with `#1a1a1a` headline `JARN KET`.
3. **Primary Showcase & Content Grid (<section.jk-flood> — `J A R N K E T`)**:
   - DOM & Selectors: Landmark `<section class="jk-flood pb-28">` rendering section `J A R N K E T` with copy *"Web Technologies Expert @ WorldSkills ASEAN 2025"*, asset references (`1ccf8ef962b3f693-s.p.2xt4dxqx4hw9...`, `797e433ab948586e-s.p.1v5bejj26fx9...`, `8457265da2739722-s.p.00okbctd204v...`, `caa3a2e1cccd8315-s.p.0zr6hhvz-h9n...`), and grid rule `._8NX9hq_variable { --font-geist:"Geist", "Geist Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.jk-flood> — `J A R N K E T`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1376px`, `gap: .125rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.125rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative:nth(2)> — `T o o l k i t`)**:
   - DOM & Selectors: Landmark `<section class="relative">` framing `T o o l k i t` and `UI & Styling` (*"Web Techologies Expert @World Skills ASEAN 2025 Software Engineer"*) with `#f4f5f7` surface cards, `#2563eb` accents, and `.z61v7q_className { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative:nth(2)> — `T o o l k i t`)` uses `.3125rem`, `.375rem`, `.25rem`, `2px` radii, `#2563eb` highlights, and assets (1ccf8ef962b3f693-s.p.2xt4dxqx4hw9..., 797e433ab948586e-s.p.1v5bejj26fx9..., 8457265da2739722-s.p.00okbctd204v...).
5. **Colophon & Global Directory Footer (<footer.jk-flood> — `https://www.jarnket.com/`)**:
   - DOM & Selectors: Landmark `<footer class="jk-flood relative">` anchoring `JarnKet · Ketsadaphone Boutpanyd` footer links (`Index · Work · Field notes · Gallery · GitHub`), copy *"Web Techologies Expert @World Skills ASEAN 2025"*, and `#d7d9dc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.jk-flood> — `https://www.jarnket.com/`)` aligns to `1376px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `.125rem` lateral canvas padding with `.125rem` grid gap and attributes (data-precedence="next", data-href="/_next/static/immutab...", data-sdkn="@vercel/analytics/react").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Ketsadaphone Boutpanyda — building fast, accessible interfaces with React & Next.j..."*
- Copy Excerpt 2: *"Web Technologies Expert @ WorldSkills ASEAN 2025"*
- Copy Excerpt 3: *"Web Techologies Expert @World Skills ASEAN 2025 Software Engineer @BCEL Bank, Web..."*
- Copy Excerpt 4: *"Web Techologies Expert @World Skills ASEAN 2025"*

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
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `10631px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: JARN KET (0%) -> Section @ 9% (9%) -> TOOLKIT (26%) -> LAOSWAY (44%) -> VANGUARD AI (61%) -> PHAPAY HACKATHON 2024 (79%) -> HAVE SOMETHING TO BUILD? (96%) -> HAVE SOMETHING TO BUILD? (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`MENU`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/blog` (listing, direct), `/work/seemuehub` (detail, direct), `/work/laosway` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-jarnket-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | JARN KET | `3` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `9%` | Section @ 9% | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `26%` | TOOLKIT | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `44%` | LAOSWAY | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5950px` | `61%` | VANGUARD AI | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `7650px` | `79%` | PHAPAY HACKATHON 2024 | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `9350px` | `96%` | HAVE SOMETHING TO BUILD? | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `9731px` | `100%` | HAVE SOMETHING TO BUILD? | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | JARN KET | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `5737px` | `50%` | LAOSWAY EVENTS | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `11474px` | `100%` | HAVE SOMETHING TO BUILD? | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`MENU`, diff `101.203`) | [state-nav.webp](assets/state-nav.webp) |
| `interactive_control` | Control `accordion` (`01 BANQUE POUR LE COMMERCE EX...`, diff `35.673`) | [state-interactive.webp](assets/state-interactive.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://www.jarnket.com/blog` | WRITING | `2462px` | `direct` (`946ms`) | [subpage-01-blog.webp](assets/subpage-01-blog.webp) |
| `2` | `detail` | `https://www.jarnket.com/work/seemuehub` | SEEMUEHUB (ສີມືຮັບ ) | `3642px` | `direct` (`652ms`) | [subpage-02-work-seemuehub.webp](assets/subpage-02-work-seemuehub.webp) |
| `3` | `detail` | `https://www.jarnket.com/work/laosway` | LAOSWAY | `3612px` | `direct` (`878ms`) | [subpage-03-work-laosway.webp](assets/subpage-03-work-laosway.webp) |

