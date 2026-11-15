---
title: "UI Prompt Blueprint: giga-ai"
date: 2026-11-15
target: "[[overview|giga-ai]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#161413` / `#fb2c36`)"
---

# UI Design System & Master Generation Blueprint: giga-ai

> **Giga: AI support agents that improve your metrics** (https://giga.ai/) — Giga builds enterprise AI agents for customer support that resolve complex conversations across chat, voice, and email. Deployed in weeks...

![Desktop Viewport Capture (1440x15714)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Giga: AI support agents that improve your metrics** (`https://giga.ai/`). Giga builds enterprise AI agents for customer support that resolve complex conversations across chat, voice, and email. Deployed in weeks...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#161413` / `#fb2c36`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#161413` (`var(--panel)` in `:root`) paired with `#fff` primary typography and `#fb2c36` accents.
  - **Extracted Typographic Hierarchy**: Pairs `InterVariable` for display copy (`We value your privacy`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: 8px`, padding `9px`) with `cubic-bezier(.16,.84,.32,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×15714px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1023px` extracted from `giga-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `8px`, `3px`, `12px`, `7px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1023px)`, `@media (prefers-reduced-motion:no-preference)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#161413` | `var(--panel)` in `:root` |
| **Primary Typography Ink** | `#0b0a09` | `var(--cinema-room)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--cinema-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Secondary / Muted Copy** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Structural Hairline Border** | `#00bb7f` | `var(--color-emerald-500)` in `:root` |
| **Variable Token (`--key-face`)** | `#3b3b3e` | `var(--key-face)` in `:root` |
| **Variable Token (`--key-face`)** | `#2a2a2d` | `var(--key-face)` in `:root` |
| **Variable Token (`--key-edge`)** | `#ffffff1f` | `var(--key-edge)` in `:root` |
| **Variable Token (`--key-lit`)** | `#ffffff14` | `var(--key-lit)` in `:root` |
| **Variable Token (`--key-ink`)** | `#e8edefe0` | `var(--key-ink)` in `:root` |
| **Variable Token (`--key-shadow`)** | `#00000080` | `var(--key-shadow)` in `:root` |
| **Variable Token (`--key-shadow`)** | `#0009` | `var(--key-shadow)` in `:root` |
| **Variable Token (`--key-ring`)** | `#e8edef99` | `var(--key-ring)` in `:root` |
| **Variable Token (`--okey-face`)** | `#f7732b` | `var(--okey-face)` in `:root` |
| **Variable Token (`--okey-face`)** | `#dd520c` | `var(--okey-face)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sans` | `"Geist", system-ui, sans-serif` | Typography / Scale Token |
| `--mono` | `"Geist Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--display` | `inter, interExt, "InterVariable", system-ui, sans-serif` | Dimension / Scale Token |
| `--text` | `inter, interExt, "InterVariable", system-ui, sans-serif` | Typography Ink Token |
| `--key-radius` | `8px` | Elevation / Border Token |
| `--key-face` | `linear-gradient(123.37deg, #3b3b3e 13.97%, #2a2a2d 87.5%)` | Color / Atmospheric Token |
| `--key-edge` | `#ffffff1f` | Color / Atmospheric Token |
| `--key-lit` | `inset 1px 1px 0 #ffffff14` | Color / Atmospheric Token |
| `--key-ink` | `#e8edefe0` | Typography Ink Token |
| `--key-shadow` | `4px 6px 5px #00000080, 2px 4px 2.5px #0009` | Elevation / Border Token |
| `--key-shadow-down` | `1px 2px 2px #00000080, 1px 1px 1px #0009` | Elevation / Border Token |
| `--key-hover` | `brightness(1.12)` | Design System Custom Token |
| `--key-ring` | `1.5px solid #e8edef99` | Elevation / Border Token |
| `--key-release` | `.15s cubic-bezier(.16,.84,.32,1)` | Motion / Easing Token |
| `--key-mono` | `400 11px/14px "Geist Mono", geistMono, monospace` | Typography / Scale Token |
| `--okey-face` | `linear-gradient(155.7deg, #f7732b 13.97%, #dd520c 87.5%)` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `InterVariable`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--display: inter, interExt, "InterVariable", system-ui, sans-serif`, `--text-4xl: 2rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 2rem`, `line-height: 1.1`, `letter-spacing: var(--tracking-display)`, `font-weight: 400`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--rx-body: 15px`; rule `p` (`font-size: 13.5px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: CSS variables `--mono: "Geist Mono", ui-monospace, monospace`, `--key-mono: 400 11px/14px "Geist Mono", geistMono, monospace`, `--font-mono-source: "geistMono", "geistMono Fallback"`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,.84,.32,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.26,.28,.12,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#footer) .banner-x`**: `transition: background-color .15s cubic-bezier(.16,.84,.32,1)` extracted from `giga-ai` stylesheet.
- **Selector `#footer) .item svg`**: `transition: transform .2s cubic-bezier(.16,.84,.32,1)` extracted from `giga-ai` stylesheet.
- **Selector `#footer) .logo`**: `transition: opacity .15s cubic-bezier(.16,.84,.32,1),background-color .15s...` extracted from `giga-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,.84,.32,1)`)**: Governs interactive state transitions across `<header.docked>` and `<section.hero-fixed>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Giga: AI support agents that improve your  │
│ ====================================================================== │
│ [ <header.docked>          | Platform overview · Build agents · Obs ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.banner-off>                                 |   │
│ | H1: We value your privacy                                        |   │
│ | Substrate: #161413    | Ink: #fff       | Accent: #fb2c36        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero-fixed>      ) max-w: 1023px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | No time to wait.             |  | DoorDash handles delivery is | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<header.docked>] -> [<section.banner-of] -> [<section.hero-fixe] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.giga-cc--gdpr>) | https://giga.ai/                   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.docked> — `giga-ai`)**:
   - Landmark `<header class="docked">` hosting `Giga: AI support agents that improve` navigation (`Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`), DOM attributes (`data-theme="dark"`, `data-consent-region="gdpr"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.part { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.banner-off> — `We value your privacy`)**:
   - Landmark `<section class="banner-off">` presenting display lead `We value your privacy` and copy excerpt *"We use cookies to run giga.ai, remember your preferences, measure"* over `#161413` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.hero-fixed> — `No time to wait.`)**:
   - Landmark `<section class="hero-fixed">` rendering section `No time to wait.` with copy *"Strictly necessary"*, asset references (`geist_mono_400_latin-s.p.2qleaeww...`, `geist_pixel_line-s.p.1gvmpev-r-ty...`, `geist_sans_400-s.p.18rrztdh9mmoo....`, `geist_sans_500-s.p.08803r3rti4jl....`), and grid rule `.part.on { visibility:visible }`.
4. **Interactive Detail & Feature Matrix (<section.armed> — `DoorDash handles delivery issues e`)**:
   - Landmark `<section class="armed">` framing `DoorDash handles delivery issues end to end with...` and `See what Giga would resolve at your company.` (*"Required for the site to work. Always active."*) with `#fff` surface cards, `#fb2c36` accents, and `.sh { opacity:var(--room);pointer-events:none;position:absolute }`.
5. **Colophon & Global Directory Footer (<footer.giga-cc--gdpr> — `https://giga.ai/`)**:
   - Landmark `<footer class="giga-cc--gdpr">` anchoring `Giga: AI support agents that imp` footer links (`Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`), copy *"Remembers choices like region and saved settings."*, and `#00bb7f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: giga-ai (Giga: AI support agents that improve your metrics)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `giga-ai` (**Giga: AI support agents that improve your metrics** — `https://giga.ai/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#161413` / `#fb2c36`).
- **Identity & Domain Context**: Giga builds enterprise AI agents for customer support that resolve complex conversations across chat, voice, and email. Deployed in weeks...
- **Primary Substrate**: `#161413` (`var(--panel)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#fb2c36`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#161413` (`var(--panel)` in `:root`) paired with `#fff` primary typography and `#fb2c36` accents.
  - **Extracted Typographic Hierarchy**: Pairs `InterVariable` for display copy (`We value your privacy`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: 8px`, padding `9px`) with `cubic-bezier(.16,.84,.32,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `giga-ai` in your global stylesheet:

:root {
  /* Giga: AI support agents that improve your metrics (giga-ai) — Ground-Truth Extracted CSS Variables */
  --sans: "Geist", system-ui, sans-serif; /* Typography / Scale Token (giga-ai) */
  --mono: "Geist Mono", ui-monospace, monospace; /* Typography / Scale Token (giga-ai) */
  --display: inter, interExt, "InterVariable", system-ui, sans-serif; /* Dimension / Scale Token (giga-ai) */
  --text: inter, interExt, "InterVariable", system-ui, sans-serif; /* Typography Ink Token (giga-ai) */
  --key-radius: 8px; /* Elevation / Border Token (giga-ai) */
  --key-face: linear-gradient(123.37deg, #3b3b3e 13.97%, #2a2a2d 87.5%); /* Color / Atmospheric Token (giga-ai) */
  --key-edge: #ffffff1f; /* Color / Atmospheric Token (giga-ai) */
  --key-lit: inset 1px 1px 0 #ffffff14; /* Color / Atmospheric Token (giga-ai) */
  --key-ink: #e8edefe0; /* Typography Ink Token (giga-ai) */
  --key-shadow: 4px 6px 5px #00000080, 2px 4px 2.5px #0009; /* Elevation / Border Token (giga-ai) */
  --key-shadow-down: 1px 2px 2px #00000080, 1px 1px 1px #0009; /* Elevation / Border Token (giga-ai) */
  --key-hover: brightness(1.12); /* Design System Custom Token (giga-ai) */
  --key-ring: 1.5px solid #e8edef99; /* Elevation / Border Token (giga-ai) */
  --key-release: .15s cubic-bezier(.16,.84,.32,1); /* Motion / Easing Token (giga-ai) */
  --key-mono: 400 11px/14px "Geist Mono", geistMono, monospace; /* Typography / Scale Token (giga-ai) */
  --okey-face: linear-gradient(155.7deg, #f7732b 13.97%, #dd520c 87.5%); /* Color / Atmospheric Token (giga-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#161413` — grounded in `var(--panel)` in `:root`
- **Primary Typography Ink**: `#0b0a09` — grounded in `var(--cinema-room)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--cinema-ink)` in `:root`
- **Interactive Accent / Highlight**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Secondary / Muted Copy**: `#fcbb00` — grounded in `var(--color-amber-400)` in `:root`
- **Structural Hairline Border**: `#00bb7f` — grounded in `var(--color-emerald-500)` in `:root`
- **Variable Token (`--key-face`)**: `#3b3b3e` — grounded in `var(--key-face)` in `:root`
- **Variable Token (`--key-face`)**: `#2a2a2d` — grounded in `var(--key-face)` in `:root`
- **Variable Token (`--key-edge`)**: `#ffffff1f` — grounded in `var(--key-edge)` in `:root`
- **Variable Token (`--key-lit`)**: `#ffffff14` — grounded in `var(--key-lit)` in `:root`
- **Variable Token (`--key-ink`)**: `#e8edefe0` — grounded in `var(--key-ink)` in `:root`
- **Variable Token (`--key-shadow`)**: `#00000080` — grounded in `var(--key-shadow)` in `:root`
- **Variable Token (`--key-shadow`)**: `#0009` — grounded in `var(--key-shadow)` in `:root`
- **Variable Token (`--key-ring`)**: `#e8edef99` — grounded in `var(--key-ring)` in `:root`
- **Variable Token (`--okey-face`)**: `#f7732b` — grounded in `var(--okey-face)` in `:root`
- **Variable Token (`--okey-face`)**: `#dd520c` — grounded in `var(--okey-face)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×15714px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1023px` extracted from `giga-ai` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1023px)`, `@media (prefers-reduced-motion:no-preference)`
- **Corner Radii**: `8px`, `3px`, `12px`, `7px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `InterVariable`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: CSS variables `--display: inter, interExt, "InterVariable", system-ui, sans-serif`, `--text-4xl: 2rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 2rem`, `line-height: 1.1`, `letter-spacing: var(--tracking-display)`, `font-weight: 400`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--rx-body: 15px`; rule `p` (`font-size: 13.5px`, `line-height: 20px`)
- **Metadata & Index Rule**: CSS variables `--mono: "Geist Mono", ui-monospace, monospace`, `--key-mono: 400 11px/14px "Geist Mono", geistMono, monospace`, `--font-mono-source: "geistMono", "geistMono Fallback"`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `giga-ai` (`Giga: AI support agents that improve your metrics`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.docked> — `giga-ai`)**:
   - DOM & Selectors: Landmark `<header class="docked">` hosting `Giga: AI support agents that improve` navigation (`Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`), DOM attributes (`data-theme="dark"`, `data-consent-region="gdpr"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.part { visibility:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.docked> — `giga-ai`)` (`giga-ai`) adapts across `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1023px)`, `@media (prefers-reduced-motion:no-preference)` with `cubic-bezier(.16,.84,.32,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.26,.28,.12,1)` transitions and links `Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`.
2. **Hero Stage & Focal Lead (<section.banner-off> — `We value your privacy`)**:
   - DOM & Selectors: Landmark `<section class="banner-off">` presenting display lead `We value your privacy` and copy excerpt *"We use cookies to run giga.ai, remember your preferences, measure"* over `#161413` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×15714px` desktop / `390×2400px` mobile) sets `#161413` background with `#fff` headline `We value your privacy`.
3. **Primary Showcase & Content Grid (<section.hero-fixed> — `No time to wait.`)**:
   - DOM & Selectors: Landmark `<section class="hero-fixed">` rendering section `No time to wait.` with copy *"Strictly necessary"*, asset references (`geist_mono_400_latin-s.p.2qleaeww...`, `geist_pixel_line-s.p.1gvmpev-r-ty...`, `geist_sans_400-s.p.18rrztdh9mmoo....`, `geist_sans_500-s.p.08803r3rti4jl....`), and grid rule `.part.on { visibility:visible }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero-fixed> — `No time to wait.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.armed> — `DoorDash handles delivery issues e`)**:
   - DOM & Selectors: Landmark `<section class="armed">` framing `DoorDash handles delivery issues end to end with...` and `See what Giga would resolve at your company.` (*"Required for the site to work. Always active."*) with `#fff` surface cards, `#fb2c36` accents, and `.sh { opacity:var(--room);pointer-events:none;position:absolute }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.armed> — `DoorDash handles delivery issues e`)` uses `8px`, `3px`, `12px`, `7px` radii, `#fb2c36` highlights, and assets (geist_mono_400_latin-s.p.2qleaeww..., geist_pixel_line-s.p.1gvmpev-r-ty..., geist_sans_400-s.p.18rrztdh9mmoo....).
5. **Colophon & Global Directory Footer (<footer.giga-cc--gdpr> — `https://giga.ai/`)**:
   - DOM & Selectors: Landmark `<footer class="giga-cc--gdpr">` anchoring `Giga: AI support agents that imp` footer links (`Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`), copy *"Remembers choices like region and saved settings."*, and `#00bb7f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.giga-cc--gdpr> — `https://giga.ai/`)` aligns to `1023px` extracted from `giga-ai` stylesheet with `9px` lateral canvas padding with `8px` grid gap and attributes (data-theme="dark", data-consent-region="gdpr", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies to run giga.ai, remember your preferences, measure performance, and..."*
- Copy Excerpt 2: *"Strictly necessary"*
- Copy Excerpt 3: *"Required for the site to work. Always active."*
- Copy Excerpt 4: *"Remembers choices like region and saved settings."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,.84,.32,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.26,.28,.12,1)`
- **Extracted Stylesheet Rules (`giga-ai`)**:
- `.part { visibility:hidden }`
- `.part.on { visibility:visible }`
- `.sh { opacity:var(--room);pointer-events:none;position:absolute }`
- `.chrome { width:1440px;height:86px;position:absolute;top:0;left:0 }`
- `.banner { -webkit-backdrop-filter:blur(24px);background:0000008c;width:1440px;heig... }`
- **Per-Selector Transition Rules**:
- **Selector `#footer) .banner-x`**: `transition: background-color .15s cubic-bezier(.16,.84,.32,1)` extracted from `giga-ai` stylesheet.
- **Selector `#footer) .item svg`**: `transition: transform .2s cubic-bezier(.16,.84,.32,1)` extracted from `giga-ai` stylesheet.
- **Selector `#footer) .logo`**: `transition: opacity .15s cubic-bezier(.16,.84,.32,1),background-color .15s...` extracted from `giga-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,.84,.32,1)`)**: Governs interactive state transitions across `<header.docked>` and `<section.hero-fixed>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `giga-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
