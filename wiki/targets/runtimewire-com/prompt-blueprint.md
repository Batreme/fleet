---
title: "UI Prompt Blueprint: runtimewire-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "runtimewire-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 2
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f9fafb` canvas, `#171a26` ink, `#cb3610` accent)"
---

# UI Design System & Master Generation Blueprint: runtimewire-com

> **RuntimeWire: Breaking tech news. Before everyone else.** (https://runtimewire.com) — Breaking tech news. Before everyone else. Independent investigations, original reporting and a continuous news feed covering startups and...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **RuntimeWire: Breaking tech news. Before everyone else.** (`https://runtimewire.com`). Breaking tech news. Before everyone else. Independent investigations, original reporting and a continuous news feed covering startups and...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f9fafb` canvas, `#171a26` ink, `#cb3610` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f9fafb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#171a26` primary typography and `#cb3610` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Newsreader` for display copy (`Nvidia's board reinstated Jensen Hua`) with `Inter` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 32px`, padding `1px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=12146px` / doc `13383px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `1px` lateral canvas padding with `32px` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 32px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9fafb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171a26` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffa500` | `.bg-orange-500 { background-color: orange }` (`#ffa500`) |
| **Interactive Accent / Highlight** | `#cb3610` | `.a11y-signup .bg-primary { background-color: #cb3610 }` |
| **Secondary / Muted Copy** | `#8a93a6` | `.rw-nojs-footer { color: #8a93a6 }` |
| **Structural Hairline Border** | `#7fe0a8` | `50 { border-color: #7fe0a8 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rw-static-asset-revision` | `20260900` | Design System Custom Token |
| `--background` | `230 18% 6%` | Canvas / Surface Token |
| `--foreground` | `210 20% 96%` | Typography Ink Token |
| `--border` | `230 14% 14%` | Elevation / Border Token |
| `--input` | `230 14% 14%` | Dimension / Scale Token |
| `--ring` | `13 100% 56%` | Elevation / Border Token |
| `--card` | `230 18% 8%` | Dimension / Scale Token |
| `--card-foreground` | `210 20% 96%` | Typography Ink Token |
| `--card-border` | `230 14% 14%` | Elevation / Border Token |
| `--popover` | `230 18% 8%` | Dimension / Scale Token |
| `--popover-foreground` | `210 20% 96%` | Typography Ink Token |
| `--popover-border` | `230 14% 14%` | Elevation / Border Token |
| `--primary` | `13 100% 56%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |
| `--primary-readable` | `13 100% 56%` | Brand / Palette Token |
| `--secondary` | `230 14% 12%` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Newsreader`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44.64px`, `line-height: 46.4256px`, `font-weight: 600`, `letter-spacing: -0.53568px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.028em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 43.2px`, `line-height: 45.792px`, `font-weight: 600`, `letter-spacing: -0.5184px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`letter-spacing: .09em`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`; rule `p` (`line-height: var(--leading-relaxed)`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 15.6px`, `font-weight: 600`, `letter-spacing: 0.12px`); CSS variables `--app-font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace`, `--font-mono: var(--app-font-mono)`, `--text-xs: .75rem`; rule `small` (`font-size: 12px`, `line-height: 1.45`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `runtimewire-com` stylesheet.
- **Selector `.\!transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))!impor...` extracted from `runtimewire-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `runtimewire-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.public-site-header>` and `<article.gap-4>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `13383px`, deepest scrollY reached `12146px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe (`PRO`)**: Triggered visual change (pixel diff `10.039`, captured in `assets/state-nav.webp`); revealed links: SIGN IN, Today, Top, Latest, Investigations, AI.
- **Hover Physics (`primary_cta` · `SUBSCRIBE`)**: `color`: `rgb(249, 250, 251)` -> `rgb(255, 255, 255)`; `backgroundColor`: `rgb(23, 26, 38)` -> `rgb(255, 79, 31)`; `borderColor`: `rgb(23, 26, 38)` -> `rgb(255, 79, 31)` (`transition-duration: 0.15s`, `timing: cubic-bezier(0.4, 0, 0.2, 1)`).
- **Hover Physics (`first_card` · `FEATURED Nvidia's board reinstate...`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Theme Toggle Probe (`Dark mode`)**: Toggled body background `rgb(249, 250, 251)` -> `rgb(13, 13, 18)` and ink `rgb(23, 26, 38)` -> `rgb(243, 245, 247)`.
- **Route Transition Architecture**: First internal navigation (`/article/nvidia-s-board-reinstated-jensen-huang-on-sunday-sec-filing-shows-as-its-spy`) measured as `direct` in `938ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — RuntimeWire: Breaking tech news. Before ev │
│ ====================================================================== │
│ [ <header.public-site-he (1440x114px) | Investigations · Stories · A ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.border-border> (w=1440px)                     | │
│ | H1: Nvidia's board reinstated Jensen Huang on Sunday,...           | │
│ | Substrate: #f9fafb | Ink: #171a26 | Accent: #cb3610                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.gap-4>) max-w: 96rem                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | OX Security finds prompt inj |  | Editor’s picks               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.border-border>) — INVESTIGATIONS           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-borde) | https://runtimewire.com              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 32px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.public-site-head) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.border-border>) — 390px Vertical Lead         | │
│ | H1: Nvidia's board reinstated Jensen Huang on Sunday,...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.gap-4>) — 1-Col Stack                     | │
│ | [ Item 1: OX Security finds prompt injection or tool poison...   ] | │
│ | [ Item 2: Editor’s picks                                         ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.border-border>) — 1-Col (INVESTIGATIONS)    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-borde) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.public-site-header> — `runtimewire-com`)**:
   - Landmark `<header class="public-site-header backdrop-blur-md">` (`1440x114px`) hosting `RuntimeWire: Breaking tech news. Bef` navigation (`Investigations · Stories · AI · Startups · Venture`), DOM attributes (`data-testid="skip-to-content"`, `data-anim="static"`, `data-testid="header-search-button"`, `data-testid="theme-switch"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.border-border> — `Nvidia's board reinstated Jensen H`)**:
   - Landmark `<section class="border-border relative">` presenting display lead `Nvidia's board reinstated Jensen Huang on Sunday,...` and copy excerpt *"An SEC filing dates the board's action to November 22nd, a day be"* over `#f9fafb` canvas and `#171a26` ink.
3. **Primary Showcase & Content Grid (<article.gap-4> — `OX Security finds prompt injection`)**:
   - Landmark `<article class="gap-4 flex">` rendering section `OX Security finds prompt injection or tool poison...` with copy *"The Daily Briefing"*, asset references (`investigations.xml`, `stories.xml`, `featured`, `favicon.ico`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.border-border> — `Editor’s picks`)**:
   - Landmark `<article class="gap-4 border-border">` framing `Editor’s picks` and `INVESTIGATIONS` (*"Published 41 minutes ago"*) with `#ffa500` surface cards, `#cb3610` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-border> — `https://runtimewire.com`)**:
   - Landmark `<footer class="border-border mt-20">` anchoring `RuntimeWire: Breaking tech news.` footer links (`Investigations · Stories · AI · Startups · Venture`), copy *"OX Security, co-founded by Neatsun Ziv, analyzed 542,207 com"*, and `#7fe0a8` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Nvidia's board reinstated Jensen Huang on Sunday,...` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `7%`): Active landmark `OX Security finds prompt injection or tool poison...` · sticky/fixed elements: `1`
- **Step 03** (`y=3400px`, `28%`): Active landmark `Listen when you’re too busy to read.` · sticky/fixed elements: `1`
- **Step 04** (`y=5100px`, `42%`): Active landmark `Cloudflare uses DNS probes to help decide when re...` · sticky/fixed elements: `1`
- **Step 05** (`y=7650px`, `63%`): Active landmark `Edmund McMillen says he had no idea AI music was...` · sticky/fixed elements: `1`
- **Step 06** (`y=9350px`, `77%`): Active landmark `MIT lab is running Ferveret's reactor-inspired co...` · sticky/fixed elements: `1`
- **Step 07** (`y=11900px`, `95%`): Active landmark `Join RuntimeWire — it’s free.` · sticky/fixed elements: `1`
- **Step 08** (`y=12146px`, `97%`): Active landmark `EXPLORE` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Detail Route (`/article/nvidia-s-board-reinstated-jensen-huang-on-sunday-sec-filing-shows-as-its-spy`)**: `https://runtimewire.com/article/nvidia-s-board-reinstated-jensen-huang-on-sunday-sec-filing-shows-as-its-spy?rw_from=featured` — H1: `Nvidia's board reinstated Jensen Huang on Sunday,...`, scrollHeight `3449px`, transition `direct` (`938ms`)
- **Detail Route (`/article/ox-security-says-22-of-flagged-mcp-servers-used-instructions-to-steer-ai-agents`)**: `https://runtimewire.com/article/ox-security-says-22-of-flagged-mcp-servers-used-instructions-to-steer-ai-agents?rw_from=featured` — H1: `OX Security finds prompt injection or tool poison...`, scrollHeight `3499px`, transition `direct` (`830ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: runtimewire-com (RuntimeWire: Breaking tech news. Before everyone else.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `runtimewire-com` (**RuntimeWire: Breaking tech news. Before everyone else.** — `https://runtimewire.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f9fafb` canvas, `#171a26` ink, `#cb3610` accent).
- **Identity & Domain Context**: Breaking tech news. Before everyone else. Independent investigations, original reporting and a continuous news feed covering startups and...
- **Primary Substrate**: `#f9fafb` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#171a26`, **Accent / Highlight**: `#cb3610`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f9fafb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#171a26` primary typography and `#cb3610` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Newsreader` for display copy (`Nvidia's board reinstated Jensen Hua`) with `Inter` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 32px`, padding `1px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `runtimewire-com` in your global stylesheet:

:root {
  /* RuntimeWire: Breaking tech news. Before everyone else. (runtimewire-com) — Live-Grounded CSS Variables */
  --rw-static-asset-revision: 20260900; /* Design System Custom Token (runtimewire-com) */
  --background: 230 18% 6%; /* Canvas / Surface Token (runtimewire-com) */
  --foreground: 210 20% 96%; /* Typography Ink Token (runtimewire-com) */
  --border: 230 14% 14%; /* Elevation / Border Token (runtimewire-com) */
  --input: 230 14% 14%; /* Dimension / Scale Token (runtimewire-com) */
  --ring: 13 100% 56%; /* Elevation / Border Token (runtimewire-com) */
  --card: 230 18% 8%; /* Dimension / Scale Token (runtimewire-com) */
  --card-foreground: 210 20% 96%; /* Typography Ink Token (runtimewire-com) */
  --card-border: 230 14% 14%; /* Elevation / Border Token (runtimewire-com) */
  --popover: 230 18% 8%; /* Dimension / Scale Token (runtimewire-com) */
  --popover-foreground: 210 20% 96%; /* Typography Ink Token (runtimewire-com) */
  --popover-border: 230 14% 14%; /* Elevation / Border Token (runtimewire-com) */
  --primary: 13 100% 56%; /* Brand / Palette Token (runtimewire-com) */
  --primary-foreground: 0 0% 100%; /* Typography Ink Token (runtimewire-com) */
  --primary-readable: 13 100% 56%; /* Brand / Palette Token (runtimewire-com) */
  --secondary: 230 14% 12%; /* Brand / Palette Token (runtimewire-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f9fafb` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#171a26` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffa500` — grounded in `.bg-orange-500 { background-color: orange }` (`#ffa500`)
- **Interactive Accent / Highlight**: `#cb3610` — grounded in `.a11y-signup .bg-primary { background-color: #cb3610 }`
- **Secondary / Muted Copy**: `#8a93a6` — grounded in `.rw-nojs-footer { color: #8a93a6 }`
- **Structural Hairline Border**: `#7fe0a8` — grounded in `50 { border-color: #7fe0a8 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `1px` lateral canvas padding with `32px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 32px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Newsreader`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 44.64px`, `line-height: 46.4256px`, `font-weight: 600`, `letter-spacing: -0.53568px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.028em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 43.2px`, `line-height: 45.792px`, `font-weight: 600`, `letter-spacing: -0.5184px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`letter-spacing: .09em`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 15.6px`, `font-weight: 600`, `letter-spacing: 0.12px`); CSS variables `--app-font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace`, `--font-mono: var(--app-font-mono)`, `--text-xs: .75rem`; rule `small` (`font-size: 12px`, `line-height: 1.45`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `runtimewire-com` (`RuntimeWire: Breaking tech news. Before everyone else.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.public-site-header> — `runtimewire-com`)**:
   - DOM & Selectors: Landmark `<header class="public-site-header backdrop-blur-md">` (`1440x114px`) hosting `RuntimeWire: Breaking tech news. Bef` navigation (`Investigations · Stories · AI · Startups · Venture`), DOM attributes (`data-testid="skip-to-content"`, `data-anim="static"`, `data-testid="header-search-button"`, `data-testid="theme-switch"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.public-site-header> — `runtimewire-com`)` (`runtimewire-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Investigations · Stories · AI · Startups · Venture`.
2. **Hero Stage & Focal Lead (<section.border-border> — `Nvidia's board reinstated Jensen H`)**:
   - DOM & Selectors: Landmark `<section class="border-border relative">` presenting display lead `Nvidia's board reinstated Jensen Huang on Sunday,...` and copy excerpt *"An SEC filing dates the board's action to November 22nd, a day be"* over `#f9fafb` canvas and `#171a26` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f9fafb` background with `#171a26` headline `Nvidia's board reinstated Jensen Huang on Sunday,...`.
3. **Primary Showcase & Content Grid (<article.gap-4> — `OX Security finds prompt injection`)**:
   - DOM & Selectors: Landmark `<article class="gap-4 flex">` rendering section `OX Security finds prompt injection or tool poison...` with copy *"The Daily Briefing"*, asset references (`investigations.xml`, `stories.xml`, `featured`, `favicon.ico`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.gap-4> — `OX Security finds prompt injection`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 32px`) on desktop and Single-column vertical stack at `390px` viewport width with `1px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.border-border> — `Editor’s picks`)**:
   - DOM & Selectors: Landmark `<article class="gap-4 border-border">` framing `Editor’s picks` and `INVESTIGATIONS` (*"Published 41 minutes ago"*) with `#ffa500` surface cards, `#cb3610` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.border-border> — `Editor’s picks`)` uses `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)` radii, `#cb3610` highlights, and assets (investigations.xml, stories.xml, featured).
5. **Colophon & Global Directory Footer (<footer.border-border> — `https://runtimewire.com`)**:
   - DOM & Selectors: Landmark `<footer class="border-border mt-20">` anchoring `RuntimeWire: Breaking tech news.` footer links (`Investigations · Stories · AI · Startups · Venture`), copy *"OX Security, co-founded by Neatsun Ziv, analyzed 542,207 com"*, and `#7fe0a8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.border-border> — `https://runtimewire.com`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `1px` lateral canvas padding with `32px` grid gap and attributes (data-testid="skip-to-content", data-anim="static", data-testid="header-search-button").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"An SEC filing dates the board's action to November 22nd, a day before Monday's ann..."*
- Copy Excerpt 2: *"The Daily Briefing"*
- Copy Excerpt 3: *"Published 41 minutes ago"*
- Copy Excerpt 4: *"OX Security, co-founded by Neatsun Ziv, analyzed 542,207 components and found agen..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`runtimewire-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `runtimewire-com` stylesheet.
- **Selector `.\!transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))!impor...` extracted from `runtimewire-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `runtimewire-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.public-site-header>` and `<article.gap-4>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `13383px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: Nvidia's board reinstated J... (0%) -> OX Security finds prompt in... (7%) -> Listen when you’re too busy... (28%) -> Cloudflare uses DNS probes... (42%) -> Edmund McMillen says he had... (63%) -> MIT lab is running Ferveret... (77%) -> Join RuntimeWire — it’s free. (95%) -> EXPLORE (97%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`PRO`) with Escape-to-close keyboard handling.
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color, backgroundColor, borderColor` with `0.15s cubic-bezier(0.4, 0, 0.2, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/article/nvidia-s-board-reinstated-jensen-huang-on-sunday-sec-filing-shows-as-its-spy` (detail, direct), `/article/ox-security-says-22-of-flagged-mcp-servers-used-instructions-to-steer-ai-agents` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `runtimewire-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Nvidia's board reinstated Jensen Huang on Sun... | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `7%` | OX Security finds prompt injection or tool po... | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `28%` | Listen when you’re too busy to read. | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5100px` | `42%` | Cloudflare uses DNS probes to help decide whe... | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `7650px` | `63%` | Edmund McMillen says he had no idea AI music... | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `9350px` | `77%` | MIT lab is running Ferveret's reactor-inspire... | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `11900px` | `95%` | Join RuntimeWire — it’s free. | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `12146px` | `97%` | EXPLORE | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Nvidia's board reinstated Jensen Huang on... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Alexandr Wang says the certified Riemann... | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | Found something worth covering? | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`PRO`, diff `10.039`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `2` | `detail` | `https://runtimewire.com/article/nvidia-s-board-reinstated-jensen-huang-on-sunday-sec-filing-shows-as-its-spy?rw_from=featured` | Nvidia's board reinstated Jensen Huan... | `3449px` | `direct` (`938ms`) | [subpage-02-article-nvidia-s-board-reinstated-je.webp](assets/subpage-02-article-nvidia-s-board-reinstated-je.webp) |
| `3` | `detail` | `https://runtimewire.com/article/ox-security-says-22-of-flagged-mcp-servers-used-instructions-to-steer-ai-agents?rw_from=featured` | OX Security finds prompt injection or... | `3499px` | `direct` (`830ms`) | [subpage-03-article-ox-security-says-22-of-flagg.webp](assets/subpage-03-article-ox-security-says-22-of-flagg.webp) |

