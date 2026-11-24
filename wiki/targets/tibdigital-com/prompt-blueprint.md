---
title: "UI Prompt Blueprint: tibdigital-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "tibdigital-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: wheel
desktop_keyframes: 2
subpages_crawled: 0
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0c10` / `#00ff84`)"
---

# UI Design System & Master Generation Blueprint: tibdigital-com

> **TIB Digital · Built by humans. Powered by AI.** (https://tibdigital.com) — TIB Digital is an Austin and Hong Kong studio building AI-powered web, mobile and platform software for founders and agencies. Built by h...

![Desktop Journey Filmstrip (1280x1656)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x1744)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **TIB Digital · Built by humans. Powered by AI.** (`https://tibdigital.com`). TIB Digital is an Austin and Hong Kong studio building AI-powered web, mobile and platform software for founders and agencies. Built by h...
- **Final Redirected URL**: [https://www.tibdigital.com/](https://www.tibdigital.com/)
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0c10` / `#00ff84`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0a0c10` (live computed `meta-theme-color` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#00ff84` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Geist` for display copy (`Built by Humans. Powered by AI. Made`) with `Geist Fallback` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: .35rem`, padding `1px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×1656px` (`assets/desktop-journey.webp`, `2` keyframes up to `y=750px` / doc `11408px`), Mobile `390×1744px` (`assets/mobile-journey.webp`, `2` keyframes).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `1px` lateral canvas padding with `.35rem` grid gap.
- **Border Radius Scale**: `50%`, `.25rem`, `.625rem`, `3rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: .35rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0c10` | live computed `meta-theme-color` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | `var(--text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#00ff84` | `var(--color-gradient-green)` in `:root` |
| **Secondary / Muted Copy** | `#e9eceb` | `var(--pl-ink)` in `:root` |
| **Structural Hairline Border** | `#008000` | `.border-green { border-color: #008000 }` |
| **Variable Token (`--pl-dark`)** | `#0b0c10` | `var(--pl-dark)` in `:root` |
| **Variable Token (`--pl-green`)** | `#00ff85` | `var(--pl-green)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pl-dark` | `#0b0c10` | Canvas / Surface Token |
| `--pl-green` | `#00ff85` | Color / Atmospheric Token |
| `--pl-ink` | `#e9eceb` | Typography Ink Token |
| `--font-geist-sans` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--font-geist-mono` | `"Geist Mono", "Geist Mono Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-geist-sans)` | Typography / Scale Token |
| `--font-mono` | `var(--font-geist-mono)` | Typography / Scale Token |
| `--color-black` | `#0a0c10` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-5xl` | `64rem` | Layout / Spatial Grid Token |
| `--container-7xl` | `80rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist Fallback`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: 2.5rem`, `line-height: calc(var(--spacing) *...`, `letter-spacing: -.06em`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `,.h2` (`font-size: 2rem`, `line-height: calc(var(--spacing) * 9)`, `letter-spacing: -.06em`, `font-weight: var(--font-we...`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `,.paragraph` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: -.04em`).
- **Metadata & Navigation Labels**: CSS variables `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`, `--font-mono: var(--font-geist-mono)`, `--text-xs: .75rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `tibdigital-com` stylesheet.
- **Selector `.swiper-fade.swiper-free-mode .sw...`**: `transition: ease-out` extracted from `tibdigital-com` stylesheet.
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `tibdigital-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.text-light>` and `<section.bg-grey-light>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `wheel` (max document height `11408px`, deepest scrollY reached `750px` across `2` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `WebGL/Canvas`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — TIB Digital · Built by humans. Powered by  │
│ ====================================================================== │
│ [ <header.text-light> (1440px)        | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative> (w=1440px)                          | │
│ | H1: Built by Humans. Powered by AI. Made for what's n...           | │
│ | Substrate: #0a0c10 | Ink: #ffffff | Accent: #00ff84                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-grey-light>) max-w: 96rem               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | First prototype <24 hrs      |  | Design systems that ship     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.text-rich-black>) — AI agents in producti  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.text-light> ) | https://tibdigital.com               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .35rem)     │
│ ====================================================================== │
│ [ HEADER BAR (<header.text-light>     ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.relative>) — 390px Vertical Lead              | │
│ | H1: Built by Humans. Powered by AI. Made for what's n...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bg-grey-light) — 1-Col Stack              | │
│ | [ Item 1: First prototype <24 hrs                                ] | │
│ | [ Item 2: Design systems that ship                               ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.text-rich-black) — 1-Col (AI agents in produ) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.text-light> ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.text-light> — `tibdigital-com`)**:
   - Landmark `<header class="text-light top-0">` (`1440px`) hosting `TIB Digital · Built by humans. Power` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-lg="sheen-grad"`), and stylesheet rule `root { --pl-dark:0b0c10;--pl-green:00ff85;--pl-ink:e9eceb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Built by Humans. Powered by AI. Ma`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Built by Humans. Powered by AI. Made for what's n...` and copy excerpt *"IRONING OUT DIGITAL PRODUCTS"* over `#0a0c10` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.bg-grey-light> — `First prototype <24 hrs`)**:
   - Landmark `<section class="bg-grey-light relative">` rendering section `First prototype <24 hrs` with copy *"Built by Humans. Powered by AI. Made for what's next."*, asset references (`07a39a8a4660cc7c-s.p.0r6juujl39pe...`, `605ce01b664af129-s.p.0wgildi0cnwt...`, `24e2077-fs8_m.css`, `235q64u4xcxu9.css`), and grid rule `.pl-glow-mount { pointer-events:none;position:absolute;inset:0 }`.
4. **Interactive Detail & Feature Matrix (<section.text-rich-black> — `Design systems that ship`)**:
   - Landmark `<section class="bg-grey-light text-rich-black">` framing `Design systems that ship` and `AI agents in production` (*"NO WRINKLES. NO SHORTCUTS."*) with `#000000` surface cards, `#00ff84` accents, and `.pl-glow { pointer-events:none;width:100%;height:100%;display:block;position:absolu... }`.
5. **Colophon & Global Directory Footer (<footer.text-light> — `https://tibdigital.com`)**:
   - Landmark `<footer class="text-light relative">` anchoring `TIB Digital · Built by humans. P` footer links (`Overview · Index · Archive · About · Contact`), copy *"TIB Digital combines human creativity and advanced AI to bui"*, and `#008000` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Viewport` · sticky/fixed elements: `0`
- **Step 02** (`y=750px`, `33%`): Active landmark `Hero` · sticky/fixed elements: `3`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tibdigital-com (TIB Digital · Built by humans. Powered by AI.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tibdigital-com` (**TIB Digital · Built by humans. Powered by AI.** — `https://tibdigital.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0c10` / `#00ff84`).
- **Identity & Domain Context**: TIB Digital is an Austin and Hong Kong studio building AI-powered web, mobile and platform software for founders and agencies. Built by h...
- **Primary Substrate**: `#0a0c10` (live computed `meta-theme-color` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#00ff84`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0a0c10` (live computed `meta-theme-color` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#00ff84` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Geist` for display copy (`Built by Humans. Powered by AI. Made`) with `Geist Fallback` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: .35rem`, padding `1px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tibdigital-com` in your global stylesheet:

:root {
  /* TIB Digital · Built by humans. Powered by AI. (tibdigital-com) — Live-Grounded CSS Variables */
  --pl-dark: #0b0c10; /* Canvas / Surface Token (tibdigital-com) */
  --pl-green: #00ff85; /* Color / Atmospheric Token (tibdigital-com) */
  --pl-ink: #e9eceb; /* Typography Ink Token (tibdigital-com) */
  --font-geist-sans: "Geist", "Geist Fallback"; /* Typography / Scale Token (tibdigital-com) */
  --font-geist-mono: "Geist Mono", "Geist Mono Fallback"; /* Typography / Scale Token (tibdigital-com) */
  --font-sans: var(--font-geist-sans); /* Typography / Scale Token (tibdigital-com) */
  --font-mono: var(--font-geist-mono); /* Typography / Scale Token (tibdigital-com) */
  --color-black: #0a0c10; /* Canvas / Surface Token (tibdigital-com) */
  --color-white: #fff; /* Canvas / Surface Token (tibdigital-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (tibdigital-com) */
  --container-sm: 24rem; /* Layout / Spatial Grid Token (tibdigital-com) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (tibdigital-com) */
  --container-xl: 36rem; /* Layout / Spatial Grid Token (tibdigital-com) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (tibdigital-com) */
  --container-5xl: 64rem; /* Layout / Spatial Grid Token (tibdigital-com) */
  --container-7xl: 80rem; /* Layout / Spatial Grid Token (tibdigital-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0a0c10` — grounded in live computed `meta-theme-color` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in `var(--text)` in `:root`
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `.bg-black { background-color: black }` (`#000000`)
- **Interactive Accent / Highlight**: `#00ff84` — grounded in `var(--color-gradient-green)` in `:root`
- **Secondary / Muted Copy**: `#e9eceb` — grounded in `var(--pl-ink)` in `:root`
- **Structural Hairline Border**: `#008000` — grounded in `.border-green { border-color: #008000 }`
- **Variable Token (`--pl-dark`)**: `#0b0c10` — grounded in `var(--pl-dark)` in `:root`
- **Variable Token (`--pl-green`)**: `#00ff85` — grounded in `var(--pl-green)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×1656px` (full-page live capture (1656px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×1744px` (full-page live capture (1744px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `1px` lateral canvas padding with `.35rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: .35rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `50%`, `.25rem`, `.625rem`, `3rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: rule `,.h1` (`font-size: 2.5rem`, `line-height: calc(var(--spacing) *...`, `letter-spacing: -.06em`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `,.h2` (`font-size: 2rem`, `line-height: calc(var(--spacing) * 9)`, `letter-spacing: -.06em`, `font-weight: var(--font-we...`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `,.paragraph` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: -.04em`)
- **Metadata & Index Rule**: CSS variables `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`, `--font-mono: var(--font-geist-mono)`, `--text-xs: .75rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tibdigital-com` (`TIB Digital · Built by humans. Powered by AI.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.text-light> — `tibdigital-com`)**:
   - DOM & Selectors: Landmark `<header class="text-light top-0">` (`1440px`) hosting `TIB Digital · Built by humans. Power` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-lg="sheen-grad"`), and stylesheet rule `root { --pl-dark:0b0c10;--pl-green:00ff85;--pl-ink:e9eceb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.text-light> — `tibdigital-com`)` (`tibdigital-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.relative> — `Built by Humans. Powered by AI. Ma`)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` presenting display lead `Built by Humans. Powered by AI. Made for what's n...` and copy excerpt *"IRONING OUT DIGITAL PRODUCTS"* over `#0a0c10` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×1656px` desktop / `390×1744px` mobile) sets `#0a0c10` background with `#ffffff` headline `Built by Humans. Powered by AI. Made for what's n...`.
3. **Primary Showcase & Content Grid (<section.bg-grey-light> — `First prototype <24 hrs`)**:
   - DOM & Selectors: Landmark `<section class="bg-grey-light relative">` rendering section `First prototype <24 hrs` with copy *"Built by Humans. Powered by AI. Made for what's next."*, asset references (`07a39a8a4660cc7c-s.p.0r6juujl39pe...`, `605ce01b664af129-s.p.0wgildi0cnwt...`, `24e2077-fs8_m.css`, `235q64u4xcxu9.css`), and grid rule `.pl-glow-mount { pointer-events:none;position:absolute;inset:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-grey-light> — `First prototype <24 hrs`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: .35rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.text-rich-black> — `Design systems that ship`)**:
   - DOM & Selectors: Landmark `<section class="bg-grey-light text-rich-black">` framing `Design systems that ship` and `AI agents in production` (*"NO WRINKLES. NO SHORTCUTS."*) with `#000000` surface cards, `#00ff84` accents, and `.pl-glow { pointer-events:none;width:100%;height:100%;display:block;position:absolu... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.text-rich-black> — `Design systems that ship`)` uses `50%`, `.25rem`, `.625rem`, `3rem` radii, `#00ff84` highlights, and assets (07a39a8a4660cc7c-s.p.0r6juujl39pe..., 605ce01b664af129-s.p.0wgildi0cnwt..., 24e2077-fs8_m.css).
5. **Colophon & Global Directory Footer (<footer.text-light> — `https://tibdigital.com`)**:
   - DOM & Selectors: Landmark `<footer class="text-light relative">` anchoring `TIB Digital · Built by humans. P` footer links (`Overview · Index · Archive · About · Contact`), copy *"TIB Digital combines human creativity and advanced AI to bui"*, and `#008000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.text-light> — `https://tibdigital.com`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `1px` lateral canvas padding with `.35rem` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"IRONING OUT DIGITAL PRODUCTS"*
- Copy Excerpt 2: *"Built by Humans. Powered by AI. Made for what's next."*
- Copy Excerpt 3: *"NO WRINKLES. NO SHORTCUTS."*
- Copy Excerpt 4: *"TIB Digital combines human creativity and advanced AI to build products that stand..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`tibdigital-com`)**:
- `root { --pl-dark:0b0c10;--pl-green:00ff85;--pl-ink:e9eceb }`
- `.pl-glow-mount { pointer-events:none;position:absolute;inset:0 }`
- `.pl-glow { pointer-events:none;width:100%;height:100%;display:block;position:absolu... }`
- `.pl-wordmark { opacity:0;will-change:opacity, transform;line-height:0 }`
- `.pl-logo { transform-origin:50%;will-change:transform;width:clamp(14rem,46vw,29rem)... }`
- **Per-Selector Transition Rules**:
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `tibdigital-com` stylesheet.
- **Selector `.swiper-fade.swiper-free-mode .sw...`**: `transition: ease-out` extracted from `tibdigital-com` stylesheet.
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `tibdigital-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.text-light>` and `<section.bg-grey-light>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `wheel` vertical progression up to `11408px` across 2 distinct viewport chapters using Lenis, WebGL/Canvas.
- **Vertical Chapter Sequence**: Viewport (0%) -> Hero (33%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tibdigital-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Viewport | `0` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `750px` | `33%` | Hero | `3` | [desktop-step-02.webp](assets/desktop-step-02.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `8466px` | `100%` | Footer | [mobile-step-02.webp](assets/mobile-step-02.webp) |

