---
title: "UI Prompt Blueprint: www-worksruthi-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-worksruthi-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f3f3e9` / `#e33529`)"
---

# UI Design System & Master Generation Blueprint: www-worksruthi-com

> **meet Sruthi. a copywriter, marketer and artist with chutzpah.** (https://www.worksruthi.com/) — you've built something good and nobody's talking about it yet? i write and design the art that helps capitalists sell their stuff. loudly.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **meet Sruthi. a copywriter, marketer and artist with chutzpah.** (`https://www.worksruthi.com/`). you've built something good and nobody's talking about it yet? i write and design the art that helps capitalists sell their stuff. loudly.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f3f3e9` / `#e33529`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f3f3e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1c1b1a` primary typography and `#e33529` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Impact` for display copy (`SRUTHI`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: var(--gap-block)`, padding `40px`) with `cubic-bezier(.4,0,1,1)` easing and GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `var(--gap-block)` grid gap.
- **Border Radius Scale**: `.25rem`, `50%`, `16px`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: var(--gap-block)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f3e9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1c1b1a` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e33529` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#e33529` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#e33529` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#808080` | `.f-col .lead { border-bottom: #808080 }` |
| **Variable Token (`--cherub`)** | `#f4ced3` | `var(--cherub)` in `:root` |
| **Variable Token (`--sail`)** | `#afd8fb` | `var(--sail)` in `:root` |
| **Variable Token (`--cobalt`)** | `#2b52d9` | `var(--cobalt)` in `:root` |
| **Variable Token (`--marigold`)** | `#f2a900` | `var(--marigold)` in `:root` |
| **Variable Token (`--grey`)** | `#6b6862` | `var(--grey)` in `:root` |
| **Variable Token (`--grey-soft`)** | `#a09c92` | `var(--grey-soft)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-display` | `"Impact", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-bayon` | `"Bayon", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-sans` | `"Geist", "Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono", "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--font-helvetica` | `"Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--spring` | `#f3f3e9` | Elevation / Border Token |
| `--ink` | `#1c1b1a` | Typography Ink Token |
| `--cinnabar` | `#e33529` | Color / Atmospheric Token |
| `--cherub` | `#f4ced3` | Color / Atmospheric Token |
| `--sail` | `#afd8fb` | Color / Atmospheric Token |
| `--cobalt` | `#2b52d9` | Color / Atmospheric Token |
| `--marigold` | `#f2a900` | Color / Atmospheric Token |
| `--grey` | `#6b6862` | Color / Atmospheric Token |
| `--grey-soft` | `#a09c92` | Color / Atmospheric Token |
| `--cream` | `var(--spring)` | Design System Custom Token |
| `--red` | `var(--cinnabar)` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Impact`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 161.973px`, `line-height: 126.339px`, `font-weight: 400`); CSS variables `--font-display: "Impact", "Arial Narrow", sans-serif`, `--h1: calc(clamp(72px, calc(28.17px + 11.24vw), 190px) * var(--vp-scale))`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 46px`, `line-height: 46px`, `font-weight: 400`); CSS variables `--h2: calc(clamp(62px, calc(28.57px + 8.57vw), 152px) * var(--vp-scale))`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono", "SF Mono", Menlo, monospace`, `--lh-small: 1.14`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-worksruthi-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-worksruthi-com` stylesheet.
- **Selector `.ease-in`**: `transition: var(--ease-in)` extracted from `www-worksruthi-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.pl-lock>` and `<section.bq>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — meet Sruthi. a copywriter, marketer and ar │
│ ====================================================================== │
│ [ <header.pl-lock> (1440x64px)        | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: SRUTHI                                                         | │
│ | Substrate: #f3f3e9 | Ink: #1c1b1a | Accent: #e33529                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bq>) max-w: 96rem                          | │
│ | +------------------------------+  +------------------------------+ | │
│ | | sruthi                       |  | MY WEBSITE IS NOW ON AWWWARD | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.sfold>) — MY WEBSITE IS NOW ON             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://www.worksruthi.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--ga)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.pl-lock>        ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: SRUTHI                                                         | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bq>) — 1-Col Stack                        | │
│ | [ Item 1: sruthi                                                 ] | │
│ | [ Item 2: MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.sfold>) — 1-Col (MY WEBSITE IS NOW )        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.pl-lock> — `www-worksruthi-com`)**:
   - Landmark `<header class="pl-lock">` (`1440x64px`) hosting `meet Sruthi. a copywriter, marketer ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --vp-100:0px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `SRUTHI`)**:
   - Landmark `<section class="hero in">` presenting display lead `SRUTHI` and copy excerpt *"handmade with 🫀 and 🧠 and"* over `#f3f3e9` canvas and `#1c1b1a` ink.
3. **Primary Showcase & Content Grid (<section.bq> — `sruthi`)**:
   - Landmark `<section class="bq">` rendering section `sruthi` with copy *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3 MY WEBSITE"*, asset references (`Impact.woff2`, `0_vr5kr4-0c-u.css`, `3y62y2uuds32t.css`, `1mlftcslf095m.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.sfold> — `MY WEBSITE IS NOW ON AWWWARDS??!! `)**:
   - Landmark `<section class="sfold">` framing `MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE ` and `MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE ` (*"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3"*) with `#e33529` surface cards, `#e33529` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.worksruthi.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `meet Sruthi. a copywriter, marke` footer links (`Overview · Index · Archive · About · Contact`), copy *"a copywriter/marketer/artist with chutzpah. a c o p y w r i "*, and `#808080` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-worksruthi-com (meet Sruthi. a copywriter, marketer and artist with chutzpah.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-worksruthi-com` (**meet Sruthi. a copywriter, marketer and artist with chutzpah.** — `https://www.worksruthi.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f3f3e9` / `#e33529`).
- **Identity & Domain Context**: you've built something good and nobody's talking about it yet? i write and design the art that helps capitalists sell their stuff. loudly.
- **Primary Substrate**: `#f3f3e9` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1c1b1a`, **Accent / Highlight**: `#e33529`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f3f3e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1c1b1a` primary typography and `#e33529` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Impact` for display copy (`SRUTHI`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: var(--gap-block)`, padding `40px`) with `cubic-bezier(.4,0,1,1)` easing and GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-worksruthi-com` in your global stylesheet:

:root {
  /* meet Sruthi. a copywriter, marketer and artist with chutzpah. (www-worksruthi-com) — Live-Grounded CSS Variables */
  --font-display: "Impact", "Arial Narrow", sans-serif; /* Typography / Scale Token (www-worksruthi-com) */
  --font-bayon: "Bayon", "Arial Narrow", sans-serif; /* Typography / Scale Token (www-worksruthi-com) */
  --font-sans: "Geist", "Helvetica Neue", Helvetica, Arial, sans-serif; /* Typography / Scale Token (www-worksruthi-com) */
  --font-mono: "Geist Mono", "SF Mono", Menlo, monospace; /* Typography / Scale Token (www-worksruthi-com) */
  --font-helvetica: "Helvetica Neue", Helvetica, Arial, sans-serif; /* Typography / Scale Token (www-worksruthi-com) */
  --spring: #f3f3e9; /* Elevation / Border Token (www-worksruthi-com) */
  --ink: #1c1b1a; /* Typography Ink Token (www-worksruthi-com) */
  --cinnabar: #e33529; /* Color / Atmospheric Token (www-worksruthi-com) */
  --cherub: #f4ced3; /* Color / Atmospheric Token (www-worksruthi-com) */
  --sail: #afd8fb; /* Color / Atmospheric Token (www-worksruthi-com) */
  --cobalt: #2b52d9; /* Color / Atmospheric Token (www-worksruthi-com) */
  --marigold: #f2a900; /* Color / Atmospheric Token (www-worksruthi-com) */
  --grey: #6b6862; /* Color / Atmospheric Token (www-worksruthi-com) */
  --grey-soft: #a09c92; /* Color / Atmospheric Token (www-worksruthi-com) */
  --cream: var(--spring); /* Design System Custom Token (www-worksruthi-com) */
  --red: var(--cinnabar); /* Design System Custom Token (www-worksruthi-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f3f3e9` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1c1b1a` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e33529` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#e33529` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#e33529` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#808080` — grounded in `.f-col .lead { border-bottom: #808080 }`
- **Variable Token (`--cherub`)**: `#f4ced3` — grounded in `var(--cherub)` in `:root`
- **Variable Token (`--sail`)**: `#afd8fb` — grounded in `var(--sail)` in `:root`
- **Variable Token (`--cobalt`)**: `#2b52d9` — grounded in `var(--cobalt)` in `:root`
- **Variable Token (`--marigold`)**: `#f2a900` — grounded in `var(--marigold)` in `:root`
- **Variable Token (`--grey`)**: `#6b6862` — grounded in `var(--grey)` in `:root`
- **Variable Token (`--grey-soft`)**: `#a09c92` — grounded in `var(--grey-soft)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `40px` lateral canvas padding with `var(--gap-block)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: var(--gap-block)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `50%`, `16px`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Impact`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 161.973px`, `line-height: 126.339px`, `font-weight: 400`); CSS variables `--font-display: "Impact", "Arial Narrow", sans-serif`, `--h1: calc(clamp(72px, calc(28.17px + 11.24vw), 190px) * var(--vp-scale))`
- **H2 Section Rule**: live computed `h2` (`font-size: 46px`, `line-height: 46px`, `font-weight: 400`); CSS variables `--h2: calc(clamp(62px, calc(28.57px + 8.57vw), 152px) * var(--vp-scale))`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono", "SF Mono", Menlo, monospace`, `--lh-small: 1.14`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-worksruthi-com` (`meet Sruthi. a copywriter, marketer and artist with chutzpah.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.pl-lock> — `www-worksruthi-com`)**:
   - DOM & Selectors: Landmark `<header class="pl-lock">` (`1440x64px`) hosting `meet Sruthi. a copywriter, marketer ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --vp-100:0px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.pl-lock> — `www-worksruthi-com`)` (`www-worksruthi-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `SRUTHI`)**:
   - DOM & Selectors: Landmark `<section class="hero in">` presenting display lead `SRUTHI` and copy excerpt *"handmade with 🫀 and 🧠 and"* over `#f3f3e9` canvas and `#1c1b1a` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f3f3e9` background with `#1c1b1a` headline `SRUTHI`.
3. **Primary Showcase & Content Grid (<section.bq> — `sruthi`)**:
   - DOM & Selectors: Landmark `<section class="bq">` rendering section `sruthi` with copy *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3 MY WEBSITE"*, asset references (`Impact.woff2`, `0_vr5kr4-0c-u.css`, `3y62y2uuds32t.css`, `1mlftcslf095m.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bq> — `sruthi`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: var(--gap-block)`) on desktop and Single-column vertical stack at `390px` viewport width with `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sfold> — `MY WEBSITE IS NOW ON AWWWARDS??!! `)**:
   - DOM & Selectors: Landmark `<section class="sfold">` framing `MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE ` and `MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE ` (*"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3"*) with `#e33529` surface cards, `#e33529` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sfold> — `MY WEBSITE IS NOW ON AWWWARDS??!! `)` uses `.25rem`, `50%`, `16px`, `999px` radii, `#e33529` highlights, and assets (Impact.woff2, 0_vr5kr4-0c-u.css, 3y62y2uuds32t.css).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.worksruthi.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `meet Sruthi. a copywriter, marke` footer links (`Overview · Index · Archive · About · Contact`), copy *"a copywriter/marketer/artist with chutzpah. a c o p y w r i "*, and `#808080` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://www.worksruthi.com/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `40px` lateral canvas padding with `var(--gap-block)` grid gap and attributes (data-precedence="next", data-precedence="next", data-sdkn="@vercel/analytics/next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"handmade with 🫀 and 🧠 and"*
- Copy Excerpt 2: *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3 MY WEBSITE IS NOW ON AWWWAR..."*
- Copy Excerpt 3: *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3"*
- Copy Excerpt 4: *"a copywriter/marketer/artist with chutzpah. a c o p y w r i t e r / m a r k e t e..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-worksruthi-com`)**:
- `host { --vp-100:0px }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-worksruthi-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-worksruthi-com` stylesheet.
- **Selector `.ease-in`**: `transition: var(--ease-in)` extracted from `www-worksruthi-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.pl-lock>` and `<section.bq>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-worksruthi-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
