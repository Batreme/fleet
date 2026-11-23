---
title: "UI Prompt Blueprint: www-aaronbrimhall-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-aaronbrimhall-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#fe019a`)"
---

# UI Design System & Master Generation Blueprint: www-aaronbrimhall-com

> **Aaron Brimhall · Action & Automotive Photographer** (https://www.aaronbrimhall.com/) — Action and automotive photography by Aaron Brimhall: dynamic compositions, high-octane shoots and globe-trotting adventures. Fun fuels cr...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Aaron Brimhall · Action & Automotive Photographer** (`https://www.aaronbrimhall.com/`). Action and automotive photography by Aaron Brimhall: dynamic compositions, high-octane shoots and globe-trotting adventures. Fun fuels cr...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#fe019a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#101010` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#fe019a` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter Variablefont Opsz Wght` for display copy (`Aaron Brimhall · Action & Automotive`) with `IBM Plex Mono` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `0%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#101010` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#fe019a` | `.ab-ab-cta-arrow { color: #fe019a }` |
| **Secondary / Muted Copy** | `#333333` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#101010` | Canvas / Surface Token |
| `--pink` | `#fe019a` | Typography Ink Token |
| `--font-family` | `"IBM Plex Mono",sans-serif` | Typography / Scale Token |
| `--ab-pink` | `#fe019a` | Typography Ink Token |
| `--ab-black` | `#101010` | Canvas / Surface Token |
| `--ab-ease-osmo` | `cubic-bezier(0.625, 0.05, 0, 1)` | Motion / Easing Token |
| `--ab-ease-out` | `cubic-bezier(0.19, 1, 0.22, 1)` | Motion / Easing Token |
| `--ab-edge` | `24px` | Dimension / Scale Token |
| `--ab-nav-ride` | `0.45s cubic-bezier(0.19, 1, 0.22, 1)` | Layout / Spatial Grid Token |
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--ab-ldx-aw` | `max(96px,min(clamp(140px,44vw,210px),35.16dvh))` | Dimension / Scale Token |
| `--tr-cover` | `#101010` | Color / Atmospheric Token |
| `--hs-e` | `var(--ab-edge,24px)` | Dimension / Scale Token |
| `--hs-trim` | `4px` | Dimension / Scale Token |
| `--vf-i` | `clamp(24px,4vw,64px)` | Dimension / Scale Token |
| `--vf-t` | `max(var(--vf-i),60px)` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter Variablefont Opsz Wght`.
- **Primary Body Stack**: `IBM Plex Mono`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: observed font-size ladder: `100px`, `38px`, `14px`, `11px`, `2em`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 100px`, `line-height: 95px`, `font-weight: 200`, `letter-spacing: 1px`).
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `.paragraph` (`letter-spacing: .01em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.19,1,0.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-aaronbrimhall-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-aaronbrimhall-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-aaronbrimhall-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<nav.ab-cs-socials>` and `<section.hero-section_wrapper>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Barba.js Page Transition Router, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Aaron Brimhall · Action & Automotive Photo │
│ ====================================================================== │
│ [ <nav.ab-cs-socials> (317x177px)     | INSTAGRAM ↗ · TIKTOK ↗ · BEH ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero_section> (w=1440px)                      | │
│ | H1: Aaron Brimhall · Action & Automotive Photographe               | │
│ | Substrate: #101010 | Ink: #ffffff | Accent: #fe019a                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero-section_wrap) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.gallery_section>) — Global Directory & Co  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-ibmplexmo) | https://www.aaronbrimhall.com/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.ab-cs-socials>     ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero_section>) — 390px Vertical Lead          | │
│ | H1: Aaron Brimhall · Action & Automotive Photographe               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.hero-section_) — 1-Col Stack              | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.gallery_section) — 1-Col (Global Directory &) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-ibmplexmo) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.ab-cs-socials> — `www-aaronbrimhall-com`)**:
   - Landmark `<nav class="ab-cs-socials">` (`317x177px`) hosting `Aaron Brimhall · Action & Automotive` navigation (`INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`), DOM attributes (`data-wf-domain="www.aaronbrimhall.com"`, `data-wf-page="6941d6f273b44a2836ceae0d"`, `data-wf-site="6941d6f273b44a2836ceae16"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero_section> — `Aaron Brimhall · Action & Automoti`)**:
   - Landmark `<section class="hero_section ab-hx-short">` presenting display lead `Aaron Brimhall · Action & Automotive Photographe` and copy excerpt *"TRANSMISSION RECEIVED"* over `#101010` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.hero-section_wrapper> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="hero-section_wrapper">` rendering section `Featured Work & Interactive Showcase` with copy *"SIGNAL LOST — TRY AGAIN"*, asset references (`cdn.prod.website-files.com`, `aaron-brimhall-site-09-25-f01e7c4...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.gallery_section> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="gallery_section">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"I M A G E G E N E R A T O R →"*) with `#222222` surface cards, `#fe019a` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-ibmplexmono-n6-active> — `https://www.aaronbrimhall.com/`)**:
   - Landmark `<footer class="wf-ibmplexmono-n6-active">` anchoring `Aaron Brimhall · Action & Automo` footer links (`INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`), copy *"I M A G E G E N E R A T O R"*, and `#3898ec` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-aaronbrimhall-com (Aaron Brimhall · Action & Automotive Photographer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-aaronbrimhall-com` (**Aaron Brimhall · Action & Automotive Photographer** — `https://www.aaronbrimhall.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#fe019a`).
- **Identity & Domain Context**: Action and automotive photography by Aaron Brimhall: dynamic compositions, high-octane shoots and globe-trotting adventures. Fun fuels cr...
- **Primary Substrate**: `#101010` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#fe019a`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#101010` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#fe019a` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter Variablefont Opsz Wght` for display copy (`Aaron Brimhall · Action & Automotive`) with `IBM Plex Mono` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-aaronbrimhall-com` in your global stylesheet:

:root {
  /* Aaron Brimhall · Action & Automotive Photographer (www-aaronbrimhall-com) — Live-Grounded CSS Variables */
  --black: #101010; /* Canvas / Surface Token (www-aaronbrimhall-com) */
  --pink: #fe019a; /* Typography Ink Token (www-aaronbrimhall-com) */
  --font-family: "IBM Plex Mono",sans-serif; /* Typography / Scale Token (www-aaronbrimhall-com) */
  --ab-pink: #fe019a; /* Typography Ink Token (www-aaronbrimhall-com) */
  --ab-black: #101010; /* Canvas / Surface Token (www-aaronbrimhall-com) */
  --ab-ease-osmo: cubic-bezier(0.625, 0.05, 0, 1); /* Motion / Easing Token (www-aaronbrimhall-com) */
  --ab-ease-out: cubic-bezier(0.19, 1, 0.22, 1); /* Motion / Easing Token (www-aaronbrimhall-com) */
  --ab-edge: 24px; /* Dimension / Scale Token (www-aaronbrimhall-com) */
  --ab-nav-ride: 0.45s cubic-bezier(0.19, 1, 0.22, 1); /* Layout / Spatial Grid Token (www-aaronbrimhall-com) */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-aaronbrimhall-com) */
  --ab-ldx-aw: max(96px,min(clamp(140px,44vw,210px),35.16dvh)); /* Dimension / Scale Token (www-aaronbrimhall-com) */
  --tr-cover: #101010; /* Color / Atmospheric Token (www-aaronbrimhall-com) */
  --hs-e: var(--ab-edge,24px); /* Dimension / Scale Token (www-aaronbrimhall-com) */
  --hs-trim: 4px; /* Dimension / Scale Token (www-aaronbrimhall-com) */
  --vf-i: clamp(24px,4vw,64px); /* Dimension / Scale Token (www-aaronbrimhall-com) */
  --vf-t: max(var(--vf-i),60px); /* Dimension / Scale Token (www-aaronbrimhall-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#101010` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#222222` — grounded in `.w-slider-nav-invert>div.w-active { background-color: #222222 }`
- **Interactive Accent / Highlight**: `#fe019a` — grounded in `.ab-ab-cta-arrow { color: #fe019a }`
- **Secondary / Muted Copy**: `#333333` — grounded in live computed `nav` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#3898ec` — grounded in `.w-select:focus { border-color: #3898ec }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `0%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter Variablefont Opsz Wght`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: observed font-size ladder: `100px`, `38px`, `14px`, `11px`, `2em`
- **H2 Section Rule**: live computed `h2` (`font-size: 100px`, `line-height: 95px`, `font-weight: 200`, `letter-spacing: 1px`)
- **Body Copy Rule**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `.paragraph` (`letter-spacing: .01em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-aaronbrimhall-com` (`Aaron Brimhall · Action & Automotive Photographer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.ab-cs-socials> — `www-aaronbrimhall-com`)**:
   - DOM & Selectors: Landmark `<nav class="ab-cs-socials">` (`317x177px`) hosting `Aaron Brimhall · Action & Automotive` navigation (`INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`), DOM attributes (`data-wf-domain="www.aaronbrimhall.com"`, `data-wf-page="6941d6f273b44a2836ceae0d"`, `data-wf-site="6941d6f273b44a2836ceae16"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.ab-cs-socials> — `www-aaronbrimhall-com`)` (`www-aaronbrimhall-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.19,1,0.22,1)` transitions and links `INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`.
2. **Hero Stage & Focal Lead (<section.hero_section> — `Aaron Brimhall · Action & Automoti`)**:
   - DOM & Selectors: Landmark `<section class="hero_section ab-hx-short">` presenting display lead `Aaron Brimhall · Action & Automotive Photographe` and copy excerpt *"TRANSMISSION RECEIVED"* over `#101010` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#101010` background with `#ffffff` headline `Aaron Brimhall · Action & Automotive Photographe`.
3. **Primary Showcase & Content Grid (<section.hero-section_wrapper> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="hero-section_wrapper">` rendering section `Featured Work & Interactive Showcase` with copy *"SIGNAL LOST — TRY AGAIN"*, asset references (`cdn.prod.website-files.com`, `aaron-brimhall-site-09-25-f01e7c4...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero-section_wrapper> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.gallery_section> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="gallery_section">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"I M A G E G E N E R A T O R →"*) with `#222222` surface cards, `#fe019a` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.gallery_section> — `Technical Architecture & Narrative`)` uses `3px`, `100%`, `50%`, `0%` radii, `#fe019a` highlights, and assets (cdn.prod.website-files.com, aaron-brimhall-site-09-25-f01e7c4..., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.wf-ibmplexmono-n6-active> — `https://www.aaronbrimhall.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wf-ibmplexmono-n6-active">` anchoring `Aaron Brimhall · Action & Automo` footer links (`INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`), copy *"I M A G E G E N E R A T O R"*, and `#3898ec` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-ibmplexmono-n6-active> — `https://www.aaronbrimhall.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.aaronbrimhall.com", data-wf-page="6941d6f273b44a2836ceae0d", data-wf-site="6941d6f273b44a2836ceae16").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"TRANSMISSION RECEIVED"*
- Copy Excerpt 2: *"SIGNAL LOST — TRY AGAIN"*
- Copy Excerpt 3: *"I M A G E G E N E R A T O R →"*
- Copy Excerpt 4: *"I M A G E G E N E R A T O R"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.19,1,0.22,1)`
- **Extracted Stylesheet Rules (`www-aaronbrimhall-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-aaronbrimhall-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-aaronbrimhall-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-aaronbrimhall-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<nav.ab-cs-socials>` and `<section.hero-section_wrapper>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Barba.js Page Transition Router, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-aaronbrimhall-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
