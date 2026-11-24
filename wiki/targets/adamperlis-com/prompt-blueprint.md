---
title: "UI Prompt Blueprint: adamperlis-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "adamperlis-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 2
subpages_crawled: 3
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#efefeb`)"
---

# UI Design System & Master Generation Blueprint: adamperlis-com

> **Adam Perlis — I design and build apps** (https://adamperlis.com) — Founder of Academy, formerly Head of Design at TIME and Head of UX at AKQA. I help founders and teams design, build and ship their apps.

![Desktop Journey Filmstrip (1280x1656)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x1744)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Adam Perlis — I design and build apps** (`https://adamperlis.com`). Founder of Academy, formerly Head of Design at TIME and Head of UX at AKQA. I help founders and teams design, build and ship their apps.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#efefeb`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#161615` primary typography and `#efefeb` accents.
  - **Grounded Typographic Hierarchy**: Uses `SF Pro Display` across display (`Hello, I'm Adam. I design and build `) and body copy, paired with `Geist Mono Variable` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1408px` container bounds (`gap: 8px`, padding `16px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×1656px` (`assets/desktop-journey.webp`, `2` keyframes up to `y=11086px` / doc `11986px`), Mobile `390×1744px` (`assets/mobile-journey.webp`, `2` keyframes).
- **Master Container Bounds**: `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `3.35544e+07px`, `4px`, `.25rem`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#161615` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#efefeb` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#efefeb` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#8a8a85` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ebebe7` | `var(--color-rule)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-mono` | `"Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--container-5xl` | `64rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `SF Pro Display`.
- **Primary Body Stack**: `SF Pro Display`.
- **Technical / Metadata Stack**: `Geist Mono Variable`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--font-mono: "Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `adamperlis-com` stylesheet.
- **Selector `.metal-glass`**: `transition: background-color .45s var(--ease-out-quart), backdrop-filter ....` extracted from `adamperlis-com` stylesheet.
- **Selector `.metal-halo`**: `transition: opacity .45s var(--ease-out-quart)` extracted from `adamperlis-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<section.moment>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `11986px`, deepest scrollY reached `11086px` across `2` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Hover Physics (`primary_cta` · `Run ⏎`)**: `transform`: `matrix(1.0397, 0, 0, 1....` -> `matrix(1.039, 0, 0, 1.0...` (`transition-duration: 0.2s`, `timing: cubic-bezier(0, 0, 0.2, 1)`).
- **Interactive Control Probe (`carousel_next`)**: Tested `Next project` (diff `0.0`).
- **Route Transition Architecture**: First internal navigation (`/work/`) measured as `direct` in `1375ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Adam Perlis — I design and build apps      │
│ ====================================================================== │
│ [ <header.pointer-events (1440x52px)  | 01 Home · 02 Work · 03 Skill ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.wrap> (w=1440px)                              | │
│ | H1: Hello, I'm Adam. I design and build apps.                      | │
│ | Substrate: #ffffff | Ink: #161615 | Accent: #efefeb                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.moment>) max-w: 1408px                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | I design and build apps.     |  | He built me with Claude Code | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.place-items-cente) — # best with sound on  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wrap>       ) | https://adamperlis.com               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.pointer-events-n) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.wrap>) — 390px Vertical Lead                  | │
│ | H1: Hello, I'm Adam. I design and build apps.                      | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.moment>) — 1-Col Stack                    | │
│ | [ Item 1: I design and build apps.                               ] | │
│ | [ Item 2: He built me with Claude Code, Codex and a little       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.place-items-cen) — 1-Col (# best with sound ) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wrap>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `adamperlis-com`)**:
   - Landmark `<header class="pointer-events-none inset-x-0">` (`1440x52px`) hosting `Adam Perlis — I design and build app` navigation (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), DOM attributes (`data-paper-shader`, `data-intro`, `data-sound-toggle`, `data-sound-choice="on"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.wrap> — `Hello, I'm Adam. I design and buil`)**:
   - Landmark `<section class="wrap relative">` presenting display lead `Hello, I'm Adam. I design and build apps.` and copy excerpt *"I design and build apps."* over `#ffffff` canvas and `#161615` ink.
3. **Primary Showcase & Content Grid (<section.moment> — `I design and build apps.`)**:
   - Landmark `<section class="moment py-12">` rendering section `I design and build apps.` with copy *"He built me with Claude Code, Codex and a little bit of love. Mos"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.place-items-center> — `He built me with Claude Code, Code`)**:
   - Landmark `<section class="place-items-center grid">` framing `He built me with Claude Code, Codex and a little` and `# best with sound on` (*"# best with sound on"*) with `#efefeb` surface cards, `#efefeb` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://adamperlis.com`)**:
   - Landmark `<footer class="wrap gap-4">` anchoring `Adam Perlis — I design and build` footer links (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), copy *"Need to install the following packages:"*, and `#ebebe7` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Hero` · sticky/fixed elements: `1`
- **Step 02** (`y=11086px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/work/`)**: `https://adamperlis.com/work/` — H1: `Things I've launched, and what I'm building now.`, scrollHeight `6602px`, transition `direct` (`1375ms`)
- **Detail Route (`/work/walkie/`)**: `https://adamperlis.com/work/walkie/` — H1: `Walkie. Speak, and polished text lands in any app...`, scrollHeight `12810px`, transition `direct` (`462ms`)
- **About Route (`/about/`)**: `https://adamperlis.com/about/` — H1: `I've spent more than fifteen years leading design...`, scrollHeight `11776px`, transition `direct` (`675ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: adamperlis-com (Adam Perlis — I design and build apps)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `adamperlis-com` (**Adam Perlis — I design and build apps** — `https://adamperlis.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#efefeb`).
- **Identity & Domain Context**: Founder of Academy, formerly Head of Design at TIME and Head of UX at AKQA. I help founders and teams design, build and ship their apps.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#161615`, **Accent / Highlight**: `#efefeb`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#161615` primary typography and `#efefeb` accents.
  - **Grounded Typographic Hierarchy**: Uses `SF Pro Display` across display (`Hello, I'm Adam. I design and build `) and body copy, paired with `Geist Mono Variable` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1408px` container bounds (`gap: 8px`, padding `16px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `adamperlis-com` in your global stylesheet:

:root {
  /* Adam Perlis — I design and build apps (adamperlis-com) — Live-Grounded CSS Variables */
  --font-mono: "Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace; /* Typography / Scale Token (adamperlis-com) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (adamperlis-com) */
  --color-black: #000; /* Canvas / Surface Token (adamperlis-com) */
  --color-white: #fff; /* Canvas / Surface Token (adamperlis-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-sm: 24rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-lg: 32rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-xl: 36rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-2xl: 42rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-4xl: 56rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-5xl: 64rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-6xl: 72rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --text-xs: .75rem; /* Typography Ink Token (adamperlis-com) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (adamperlis-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#161615` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#efefeb` — grounded in live computed `a` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#efefeb` — grounded in live computed `a` `background-color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#8a8a85` — grounded in live computed `footer` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#ebebe7` — grounded in `var(--color-rule)` in `:root`
- **Variable Token (`--color-black`)**: `#000000` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×1656px` (full-page live capture (1656px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×1744px` (full-page live capture (1744px), `390px` standard mobile width).
- **Container Max-Width**: `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `16px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`
- **Corner Radii**: `3.35544e+07px`, `4px`, `.25rem`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `SF Pro Display`
- **Body Font Stack**: `SF Pro Display`
- **Monospace / Technical Font Stack**: `Geist Mono Variable`
- **H1 Display Rule**: live computed `h1` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: live computed `body` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--font-mono: "Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `adamperlis-com` (`Adam Perlis — I design and build apps`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `adamperlis-com`)**:
   - DOM & Selectors: Landmark `<header class="pointer-events-none inset-x-0">` (`1440x52px`) hosting `Adam Perlis — I design and build app` navigation (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), DOM attributes (`data-paper-shader`, `data-intro`, `data-sound-toggle`, `data-sound-choice="on"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.pointer-events-none> — `adamperlis-com`)` (`adamperlis-com`) adapts across `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`.
2. **Hero Stage & Focal Lead (<section.wrap> — `Hello, I'm Adam. I design and buil`)**:
   - DOM & Selectors: Landmark `<section class="wrap relative">` presenting display lead `Hello, I'm Adam. I design and build apps.` and copy excerpt *"I design and build apps."* over `#ffffff` canvas and `#161615` ink.
   - Responsive Contract: Hero stage (`1280×1656px` desktop / `390×1744px` mobile) sets `#ffffff` background with `#161615` headline `Hello, I'm Adam. I design and build apps.`.
3. **Primary Showcase & Content Grid (<section.moment> — `I design and build apps.`)**:
   - DOM & Selectors: Landmark `<section class="moment py-12">` rendering section `I design and build apps.` with copy *"He built me with Claude Code, Codex and a little bit of love. Mos"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.moment> — `I design and build apps.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.place-items-center> — `He built me with Claude Code, Code`)**:
   - DOM & Selectors: Landmark `<section class="place-items-center grid">` framing `He built me with Claude Code, Codex and a little` and `# best with sound on` (*"# best with sound on"*) with `#efefeb` surface cards, `#efefeb` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.place-items-center> — `He built me with Claude Code, Code`)` uses `3.35544e+07px`, `4px`, `.25rem`, `var(--radius-2xl)` radii, `#efefeb` highlights, and assets (favicon.ico, favicon-32.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://adamperlis.com`)**:
   - DOM & Selectors: Landmark `<footer class="wrap gap-4">` anchoring `Adam Perlis — I design and build` footer links (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), copy *"Need to install the following packages:"*, and `#ebebe7` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wrap> — `https://adamperlis.com`)` aligns to `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `16px` lateral canvas padding with `8px` grid gap and attributes (data-paper-shader, data-intro, data-sound-toggle).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"I design and build apps."*
- Copy Excerpt 2: *"He built me with Claude Code, Codex and a little bit of love. Mostly the first two."*
- Copy Excerpt 3: *"# best with sound on"*
- Copy Excerpt 4: *"Need to install the following packages:"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`adamperlis-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `adamperlis-com` stylesheet.
- **Selector `.metal-glass`**: `transition: background-color .45s var(--ease-out-quart), backdrop-filter ....` extracted from `adamperlis-com` stylesheet.
- **Selector `.metal-halo`**: `transition: opacity .45s var(--ease-out-quart)` extracted from `adamperlis-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<section.moment>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `11986px` across 2 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: Hero (0%) -> Footer (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `transform` with `0.2s cubic-bezier(0, 0, 0.2, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/work/` (listing, direct), `/work/walkie/` (detail, direct), `/about/` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `adamperlis-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Hero | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `11086px` | `100%` | Footer | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `8460px` | `100%` | Footer | [mobile-step-02.webp](assets/mobile-step-02.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://adamperlis.com/work/` | Things I've launched, and what I'm bu... | `6602px` | `direct` (`1375ms`) | [subpage-01-work.webp](assets/subpage-01-work.webp) |
| `2` | `detail` | `https://adamperlis.com/work/walkie/` | Walkie. Speak, and polished text land... | `12810px` | `direct` (`462ms`) | [subpage-02-work-walkie.webp](assets/subpage-02-work-walkie.webp) |
| `3` | `about` | `https://adamperlis.com/about/` | I've spent more than fifteen years le... | `11776px` | `direct` (`675ms`) | [subpage-03-about.webp](assets/subpage-03-about.webp) |

