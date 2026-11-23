---
title: "UI Prompt Blueprint: ethiack-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "ethiack-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0b191b` / `#ff8000`)"
---

# UI Design System & Master Generation Blueprint: ethiack-com

> **Ethiack** (https://ethiack.com/) — Ethiack is the Adversarial Exposure Validation platform. Hackian continuously tests your attack surface, validates exploitability with pr...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Ethiack** (`https://ethiack.com/`). Ethiack is the Adversarial Exposure Validation platform. Hackian continuously tests your attack surface, validates exploitability with pr...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0b191b` / `#ff8000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0b191b` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff8000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `fk-grotesk-light` for display copy (`AI Offensive Security. Proven, Conti`) with `fk-grotesk-regular` and `fk-grotesk-mono-medium`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: .3vw`, padding `1.2vw`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `1.2vw` lateral canvas padding with `.3vw` grid gap.
- **Border Radius Scale**: `3.75px`, `8px`, `12px`, `14px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .3vw`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.2vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (max-width:410px)`, `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:743px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b191b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff8000` | `.fn-date-picker .pika-button:hover { background: #ff8000 }` |
| **Secondary / Muted Copy** | `#82988b` | `var(--color-muted-green-300)` in `:root` |
| **Structural Hairline Border** | `#23403f` | `var(--line)` in `:root` |
| **Variable Token (`--color-geral-yellow`)** | `#ffdea6` | `var(--color-geral-yellow)` in `:root` |
| **Variable Token (`--color-geral-red`)** | `#7c2329` | `var(--color-geral-red)` in `:root` |
| **Variable Token (`--color-semantic-informative-800`)** | `#1e40af` | `var(--color-semantic-informative-800)` in `:root` |
| **Variable Token (`--color-semantic-informative-200`)** | `#bfdbfe` | `var(--color-semantic-informative-200)` in `:root` |
| **Variable Token (`--color-semantic-danger-200`)** | `#fec8cc` | `var(--color-semantic-danger-200)` in `:root` |
| **Variable Token (`--color-semantic-danger-500`)** | `#de2d3b` | `var(--color-semantic-danger-500)` in `:root` |
| **Variable Token (`--color-semantic-danger-600`)** | `#d12332` | `var(--color-semantic-danger-600)` in `:root` |
| **Variable Token (`--color-semantic-warning-600`)** | `#fbbf24` | `var(--color-semantic-warning-600)` in `:root` |
| **Variable Token (`--color-infection-detected`)** | `#ff0015` | `var(--color-infection-detected)` in `:root` |
| **Variable Token (`--color-infection-identified`)** | `#ff9900` | `var(--color-infection-identified)` in `:root` |
| **Variable Token (`--color-muted-green-50`)** | `#e8ecea` | `var(--color-muted-green-50)` in `:root` |
| **Variable Token (`--color-muted-green-100`)** | `#cdd5d0` | `var(--color-muted-green-100)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-geral-black` | `#000` | Canvas / Surface Token |
| `--color-geral-white` | `#fff` | Canvas / Surface Token |
| `--color-geral-yellow` | `#ffdea6` | Brand / Palette Token |
| `--color-geral-red` | `#7c2329` | Brand / Palette Token |
| `--color-semantic-informative-800` | `#1e40af` | Brand / Palette Token |
| `--color-semantic-informative-200` | `#bfdbfe` | Brand / Palette Token |
| `--color-semantic-danger-200` | `#fec8cc` | Brand / Palette Token |
| `--color-semantic-danger-500` | `#de2d3b` | Brand / Palette Token |
| `--color-semantic-danger-600` | `#d12332` | Brand / Palette Token |
| `--color-semantic-warning-600` | `#fbbf24` | Brand / Palette Token |
| `--color-infection-detected` | `#ff0015` | Brand / Palette Token |
| `--color-infection-identified` | `#f90` | Brand / Palette Token |
| `--color-muted-green-50` | `#e8ecea` | Brand / Palette Token |
| `--color-muted-green-100` | `#cdd5d0` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `fk-grotesk-light`.
- **Primary Body Stack**: `fk-grotesk-regular`.
- **Technical / Metadata Stack**: `fk-grotesk-mono-medium`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 58.05px`, `line-height: 58.05px`, `font-weight: 400`, `letter-spacing: -2.322px`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 33.45px`, `line-height: 36.795px`, `font-weight: 400`, `letter-spacing: -1.0035px`); rule `h2` (`font-size: 44px`, `line-height: 1.02`, `letter-spacing: -.03em`, `font-weight: 600`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: clamp(64px,55.81px + 100vw *...`, `line-height: 1em`, `letter-spacing: -.1em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.1px`); CSS variables `--mono: 'FK Grotesk Mono','fk-grotesk-mono',ui-monospace,monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.215,.61,.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `ter-target .hs-email input:-webki...`**: `transition: background-color 9999s ease-in-out 0s` extracted from `ethiack-com` stylesheet.
- **Selector `error-msg) .hs-email input:-webki...`**: `transition: background-color 9999s ease-in-out 0s` extracted from `ethiack-com` stylesheet.
- **Selector `a-v-fc6eb133] .newsletter-target...`**: `transition: transform .5s cubic-bezier(.23,1,.32,1),opacity .5s cubic-bezi...` extracted from `ethiack-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<main.main:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Ethiack                                    │
│ ====================================================================== │
│ [ <header.lenis> (1440x900px)         | Try Ethiack                  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.main> (w=1440px)                                 | │
│ | H1: AI Offensive Security. Proven, Continuous.                     | │
│ | Substrate: #0b191b | Ink: #ffffff | Accent: #ff8000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.main:nth(2)>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Autonomous. Relentless. Cont |  | Pentesting without schedules | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.main:nth(3)>) — Complete visibility o         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.scene-contai) | https://ethiack.com/                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .3vw)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.lenis>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.main>) — 390px Vertical Lead                     | │
│ | H1: AI Offensive Security. Proven, Continuous.                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.main:nth(2)>) — 1-Col Stack                  | │
│ | [ Item 1: Autonomous. Relentless. Continuous.                    ] | │
│ | [ Item 2: Pentesting without schedules, snapshots, or manua...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.main:nth(3)>) — 1-Col (Complete visibilit)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.scene-contai) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `ethiack-com`)**:
   - Landmark `<header class="lenis">` (`1440x900px`) hosting `Ethiack` navigation (`Try Ethiack`), DOM attributes (`data-hubspot-styled-components`, `data-onloadfired="true"`, `data-website-id="9c5e0156-7850-40b6-91..."`, `data-onload`), and stylesheet rule `p em { font-size:2.1vw }`.
2. **Hero Stage & Focal Lead (<main.main> — `AI Offensive Security. Proven, Con`)**:
   - Landmark `<main class="main">` presenting display lead `AI Offensive Security. Proven, Continuous.` and copy excerpt *"We use cookies to personalise content and ads, to provide social "* over `#0b191b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.main:nth(2)> — `Autonomous. Relentless. Continuous`)**:
   - Landmark `<main class="main">` rendering section `Autonomous. Relentless. Continuous.` with copy *"Annual pentests give you a snapshot. Results arrive late, ranked "*, asset references (`analytics-browser-gtm-2.12.2-min....`, `cc.js`, `uwt.js`, `uc.js`), and grid rule `focus-within { background-color:var(--newsletter-form-focusBgColor,rgb(from var(--color... }`.
4. **Interactive Detail & Feature Matrix (<main.main:nth(3)> — `Pentesting without schedules, snap`)**:
   - Landmark `<main class="main">` framing `Pentesting without schedules, snapshots, or manua...` and `Complete visibility of your attack surface and su...` (*"R i s k v a l i d a t e d !"*) with `#000000` surface cards, `#ff8000` accents, and `.newsletter-target form { align-items:center;display:flex;flex-direction:row;justify-content:space... }`.
5. **Colophon & Global Directory Footer (<footer.scene-container> — `https://ethiack.com/`)**:
   - Landmark `<footer class="scene-container">` anchoring `Ethiack` footer links (`Try Ethiack`), copy *"X S S i n D a s h b o a r d"*, and `#23403f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ethiack-com (Ethiack)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ethiack-com` (**Ethiack** — `https://ethiack.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b191b` / `#ff8000`).
- **Identity & Domain Context**: Ethiack is the Adversarial Exposure Validation platform. Hackian continuously tests your attack surface, validates exploitability with pr...
- **Primary Substrate**: `#0b191b` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ff8000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0b191b` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff8000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `fk-grotesk-light` for display copy (`AI Offensive Security. Proven, Conti`) with `fk-grotesk-regular` and `fk-grotesk-mono-medium`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: .3vw`, padding `1.2vw`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ethiack-com` in your global stylesheet:

:root {
  /* Ethiack (ethiack-com) — Live-Grounded CSS Variables */
  --color-black: #000; /* Canvas / Surface Token (ethiack-com) */
  --color-white: #fff; /* Canvas / Surface Token (ethiack-com) */
  --color-geral-black: #000; /* Canvas / Surface Token (ethiack-com) */
  --color-geral-white: #fff; /* Canvas / Surface Token (ethiack-com) */
  --color-geral-yellow: #ffdea6; /* Brand / Palette Token (ethiack-com) */
  --color-geral-red: #7c2329; /* Brand / Palette Token (ethiack-com) */
  --color-semantic-informative-800: #1e40af; /* Brand / Palette Token (ethiack-com) */
  --color-semantic-informative-200: #bfdbfe; /* Brand / Palette Token (ethiack-com) */
  --color-semantic-danger-200: #fec8cc; /* Brand / Palette Token (ethiack-com) */
  --color-semantic-danger-500: #de2d3b; /* Brand / Palette Token (ethiack-com) */
  --color-semantic-danger-600: #d12332; /* Brand / Palette Token (ethiack-com) */
  --color-semantic-warning-600: #fbbf24; /* Brand / Palette Token (ethiack-com) */
  --color-infection-detected: #ff0015; /* Brand / Palette Token (ethiack-com) */
  --color-infection-identified: #f90; /* Brand / Palette Token (ethiack-com) */
  --color-muted-green-50: #e8ecea; /* Brand / Palette Token (ethiack-com) */
  --color-muted-green-100: #cdd5d0; /* Brand / Palette Token (ethiack-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0b191b` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ff8000` — grounded in `.fn-date-picker .pika-button:hover { background: #ff8000 }`
- **Secondary / Muted Copy**: `#82988b` — grounded in `var(--color-muted-green-300)` in `:root`
- **Structural Hairline Border**: `#23403f` — grounded in `var(--line)` in `:root`
- **Variable Token (`--color-geral-yellow`)**: `#ffdea6` — grounded in `var(--color-geral-yellow)` in `:root`
- **Variable Token (`--color-geral-red`)**: `#7c2329` — grounded in `var(--color-geral-red)` in `:root`
- **Variable Token (`--color-semantic-informative-800`)**: `#1e40af` — grounded in `var(--color-semantic-informative-800)` in `:root`
- **Variable Token (`--color-semantic-informative-200`)**: `#bfdbfe` — grounded in `var(--color-semantic-informative-200)` in `:root`
- **Variable Token (`--color-semantic-danger-200`)**: `#fec8cc` — grounded in `var(--color-semantic-danger-200)` in `:root`
- **Variable Token (`--color-semantic-danger-500`)**: `#de2d3b` — grounded in `var(--color-semantic-danger-500)` in `:root`
- **Variable Token (`--color-semantic-danger-600`)**: `#d12332` — grounded in `var(--color-semantic-danger-600)` in `:root`
- **Variable Token (`--color-semantic-warning-600`)**: `#fbbf24` — grounded in `var(--color-semantic-warning-600)` in `:root`
- **Variable Token (`--color-infection-detected`)**: `#ff0015` — grounded in `var(--color-infection-detected)` in `:root`
- **Variable Token (`--color-infection-identified`)**: `#ff9900` — grounded in `var(--color-infection-identified)` in `:root`
- **Variable Token (`--color-muted-green-50`)**: `#e8ecea` — grounded in `var(--color-muted-green-50)` in `:root`
- **Variable Token (`--color-muted-green-100`)**: `#cdd5d0` — grounded in `var(--color-muted-green-100)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `1.2vw` lateral canvas padding with `.3vw` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .3vw`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.2vw` horizontal padding
- **Media Queries**: `@media only screen and (max-width:410px)`, `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:743px)`
- **Corner Radii**: `3.75px`, `8px`, `12px`, `14px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `fk-grotesk-light`
- **Body Font Stack**: `fk-grotesk-regular`
- **Monospace / Technical Font Stack**: `fk-grotesk-mono-medium`
- **H1 Display Rule**: live computed `h1` (`font-size: 58.05px`, `line-height: 58.05px`, `font-weight: 400`, `letter-spacing: -2.322px`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 33.45px`, `line-height: 36.795px`, `font-weight: 400`, `letter-spacing: -1.0035px`); rule `h2` (`font-size: 44px`, `line-height: 1.02`, `letter-spacing: -.03em`, `font-weight: 600`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: clamp(64px,55.81px + 100vw *...`, `line-height: 1em`, `letter-spacing: -.1em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.1px`); CSS variables `--mono: 'FK Grotesk Mono','fk-grotesk-mono',ui-monospace,monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ethiack-com` (`Ethiack`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `ethiack-com`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` (`1440x900px`) hosting `Ethiack` navigation (`Try Ethiack`), DOM attributes (`data-hubspot-styled-components`, `data-onloadfired="true"`, `data-website-id="9c5e0156-7850-40b6-91..."`, `data-onload`), and stylesheet rule `p em { font-size:2.1vw }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `ethiack-com`)` (`ethiack-com`) adapts across `@media only screen and (max-width:410px)`, `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:743px)` with `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.215,.61,.355,1)` transitions and links `Try Ethiack`.
2. **Hero Stage & Focal Lead (<main.main> — `AI Offensive Security. Proven, Con`)**:
   - DOM & Selectors: Landmark `<main class="main">` presenting display lead `AI Offensive Security. Proven, Continuous.` and copy excerpt *"We use cookies to personalise content and ads, to provide social "* over `#0b191b` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#0b191b` background with `#ffffff` headline `AI Offensive Security. Proven, Continuous.`.
3. **Primary Showcase & Content Grid (<main.main:nth(2)> — `Autonomous. Relentless. Continuous`)**:
   - DOM & Selectors: Landmark `<main class="main">` rendering section `Autonomous. Relentless. Continuous.` with copy *"Annual pentests give you a snapshot. Results arrive late, ranked "*, asset references (`analytics-browser-gtm-2.12.2-min....`, `cc.js`, `uwt.js`, `uc.js`), and grid rule `focus-within { background-color:var(--newsletter-form-focusBgColor,rgb(from var(--color... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.main:nth(2)> — `Autonomous. Relentless. Continuous`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .3vw`) on desktop and Single-column vertical stack at `390px` viewport width with `1.2vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.main:nth(3)> — `Pentesting without schedules, snap`)**:
   - DOM & Selectors: Landmark `<main class="main">` framing `Pentesting without schedules, snapshots, or manua...` and `Complete visibility of your attack surface and su...` (*"R i s k v a l i d a t e d !"*) with `#000000` surface cards, `#ff8000` accents, and `.newsletter-target form { align-items:center;display:flex;flex-direction:row;justify-content:space... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.main:nth(3)> — `Pentesting without schedules, snap`)` uses `3.75px`, `8px`, `12px`, `14px` radii, `#ff8000` highlights, and assets (analytics-browser-gtm-2.12.2-min...., cc.js, uwt.js).
5. **Colophon & Global Directory Footer (<footer.scene-container> — `https://ethiack.com/`)**:
   - DOM & Selectors: Landmark `<footer class="scene-container">` anchoring `Ethiack` footer links (`Try Ethiack`), copy *"X S S i n D a s h b o a r d"*, and `#23403f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.scene-container> — `https://ethiack.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `1.2vw` lateral canvas padding with `.3vw` grid gap and attributes (data-hubspot-styled-components, data-onloadfired="true", data-website-id="9c5e0156-7850-40b6-91...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies to personalise content and ads, to provide social media features an..."*
- Copy Excerpt 2: *"Annual pentests give you a snapshot. Results arrive late, ranked by CVSS, not by w..."*
- Copy Excerpt 3: *"R i s k v a l i d a t e d !"*
- Copy Excerpt 4: *"X S S i n D a s h b o a r d"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.215,.61,.355,1)`
- **Extracted Stylesheet Rules (`ethiack-com`)**:
- `p em { font-size:2.1vw }`
- `focus-within { background-color:var(--newsletter-form-focusBgColor,rgb(from var(--color... }`
- `.newsletter-target form { align-items:center;display:flex;flex-direction:row;justify-content:space... }`
- `.newsletter-target .hs-richtext { display:none }`
- `.newsletter-target .hs-email { width:100% }`
- **Per-Selector Transition Rules**:
- **Selector `ter-target .hs-email input:-webki...`**: `transition: background-color 9999s ease-in-out 0s` extracted from `ethiack-com` stylesheet.
- **Selector `error-msg) .hs-email input:-webki...`**: `transition: background-color 9999s ease-in-out 0s` extracted from `ethiack-com` stylesheet.
- **Selector `a-v-fc6eb133] .newsletter-target...`**: `transition: transform .5s cubic-bezier(.23,1,.32,1),opacity .5s cubic-bezi...` extracted from `ethiack-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<main.main:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ethiack-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
