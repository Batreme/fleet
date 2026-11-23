---
title: "UI Prompt Blueprint: www-nereo-io"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-nereo-io"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#15191f` canvas, `#ffffff` ink, `#ffd23f` accent)"
---

# UI Design System & Master Generation Blueprint: www-nereo-io

> **Nereo — AI Video Generator for Creators & Marketers** (https://www.nereo.io/) — Generate stunning 4K videos with AI. Create professional videos from text prompts with realistic physics and native audio. Start free today.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Nereo — AI Video Generator for Creators & Marketers** (`https://www.nereo.io/`). Generate stunning 4K videos with AI. Create professional videos from text prompts with realistic physics and native audio. Start free today.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#15191f` canvas, `#ffffff` ink, `#ffd23f` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#15191f` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffd23f` accents.
  - **Grounded Typographic Hierarchy**: Pairs `__Unbounded_73c992` for display copy (`AI Video Generator for Creators & Ma`) with `__Outfit_a80a2d` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: 24px`, padding `2rem`) with `cubic-bezier(.8,0,1,1)` easing and Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `80rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `999px`, `.3125rem`, `.375rem`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1200px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:no-preference)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#15191f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `nav` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#171717` | `var(--sd-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#ffd23f` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#2b8fea` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#262626` | `var(--sd-line)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sidebar-background` | `var(--background)` | Canvas / Surface Token |
| `--sidebar-foreground` | `var(--foreground)` | Typography Ink Token |
| `--sidebar-primary` | `var(--primary)` | Brand / Palette Token |
| `--sidebar-primary-foreground` | `var(--primary-foreground)` | Typography Ink Token |
| `--sidebar-accent` | `var(--background)` | Brand / Palette Token |
| `--sidebar-accent-foreground` | `var(--primary)` | Typography Ink Token |
| `--sidebar-border` | `var(--border)` | Elevation / Border Token |
| `--sidebar-ring` | `var(--ring)` | Elevation / Border Token |
| `--font-heading` | `var(--font-sans)` | Typography Ink Token |
| `--background` | `262 76% 95%` | Canvas / Surface Token |
| `--foreground` | `262 5% 10%` | Typography Ink Token |
| `--card` | `262 50% 90%` | Dimension / Scale Token |
| `--card-foreground` | `262 5% 10%` | Typography Ink Token |
| `--popover` | `262 76% 95%` | Dimension / Scale Token |
| `--popover-foreground` | `262 95% 10%` | Typography Ink Token |
| `--primary` | `210 75% 50%` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `__Unbounded_73c992`.
- **Primary Body Stack**: `__Outfit_a80a2d`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 68px`, `font-weight: 700`, `letter-spacing: -0.9px`); CSS variables `--font-display: var(--font-sans)`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 26px`, `line-height: 32px`, `font-weight: 700`, `letter-spacing: 0.52px`); rule `h2` (`font-size: 1.875rem`, `line-height: 2.25rem`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--removed-body-scroll-bar-size: 0px`; rule `p` (`line-height: 1.625`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: 60px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: cubic-bezier(.8,0,1,1)` extracted from `www-nereo-io` stylesheet.
- **Selector `.transition-\[color\2c text-shadow\]`**: `transition: cubic-bezier(.8,0,1,1)` extracted from `www-nereo-io` stylesheet.
- **Selector `grid-template-rows\2c opacity\2c...`**: `transition: cubic-bezier(.8,0,1,1)` extracted from `www-nereo-io` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.8,0,1,1)`)**: Governs interactive state transitions across `<nav.gap-6>` and `<section.gap-4>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Nereo — AI Video Generator for Creators &  │
│ ====================================================================== │
│ [ <nav.gap-6> (1248x40px)             | Nereo · Home · AI Anime Shor ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative> (w=1440px)                          | │
│ | H1: AI Video Generator for Creators & Marketers                    | │
│ | Substrate: #15191f | Ink: #ffffff | Accent: #ffd23f                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.gap-4>) max-w: 80rem                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Nereo Agent Describe the vid |  | Seedance 2.5 One continuous  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.border-nl-rule>) — Seedance 2.0 Audio an   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.antialiased>) | https://www.nereo.io/                │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.gap-6>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.relative>) — 390px Vertical Lead              | │
│ | H1: AI Video Generator for Creators & Marketers                    | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.gap-4>) — 1-Col Stack                     | │
│ | [ Item 1: Nereo Agent Describe the video. The agent writes...    ] | │
│ | [ Item 2: Seedance 2.5 One continuous 30-second take, nativ...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.border-nl-rule>) — 1-Col (Seedance 2.0 Audio) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.antialiased>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.gap-6> — `www-nereo-io`)**:
   - Landmark `<nav class="gap-6 hidden">` (`1248x40px`) hosting `Nereo — AI Video Generator for Creat` navigation (`Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `AI Video Generator for Creators & `)**:
   - Landmark `<section class="relative overflow-hidden">` presenting display lead `AI Video Generator for Creators & Marketers` and copy excerpt *"Turn a prompt, a photo or a reference into a finished video. Veo "* over `#15191f` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.gap-4> — `Nereo Agent Describe the video. Th`)**:
   - Landmark `<section class="gap-4 border-nl-rule">` rendering section `Nereo Agent Describe the video. The agent writes...` with copy *"Start creating free"*, asset references (`e4af272ccee01ff0-s.p.woff2`, `logo.png`, `322e14d06135256b.css`, `a7f88efd924ba4d6.css`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.border-nl-rule> — `Seedance 2.5 One continuous 30-sec`)**:
   - Landmark `<section class="gap-4 border-nl-rule">` framing `Seedance 2.5 One continuous 30-second take, nativ...` and `Seedance 2.0 Audio and video generated together,...` (*"Describe the video. The agent writes the shots, generates them an"*) with `#171717` surface cards, `#ffd23f` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.antialiased> — `https://www.nereo.io/`)**:
   - Landmark `<footer class="antialiased">` anchoring `Nereo — AI Video Generator for C` footer links (`Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`), copy *"LUMA NOOK — A Daily Tea Ritual"*, and `#262626` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-nereo-io (Nereo — AI Video Generator for Creators & Marketers)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-nereo-io` (**Nereo — AI Video Generator for Creators & Marketers** — `https://www.nereo.io/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#15191f` canvas, `#ffffff` ink, `#ffd23f` accent).
- **Identity & Domain Context**: Generate stunning 4K videos with AI. Create professional videos from text prompts with realistic physics and native audio. Start free today.
- **Primary Substrate**: `#15191f` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ffd23f`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#15191f` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffd23f` accents.
  - **Grounded Typographic Hierarchy**: Pairs `__Unbounded_73c992` for display copy (`AI Video Generator for Creators & Ma`) with `__Outfit_a80a2d` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: 24px`, padding `2rem`) with `cubic-bezier(.8,0,1,1)` easing and Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-nereo-io` in your global stylesheet:

:root {
  /* Nereo — AI Video Generator for Creators & Marketers (www-nereo-io) — Live-Grounded CSS Variables */
  --sidebar-background: var(--background); /* Canvas / Surface Token (www-nereo-io) */
  --sidebar-foreground: var(--foreground); /* Typography Ink Token (www-nereo-io) */
  --sidebar-primary: var(--primary); /* Brand / Palette Token (www-nereo-io) */
  --sidebar-primary-foreground: var(--primary-foreground); /* Typography Ink Token (www-nereo-io) */
  --sidebar-accent: var(--background); /* Brand / Palette Token (www-nereo-io) */
  --sidebar-accent-foreground: var(--primary); /* Typography Ink Token (www-nereo-io) */
  --sidebar-border: var(--border); /* Elevation / Border Token (www-nereo-io) */
  --sidebar-ring: var(--ring); /* Elevation / Border Token (www-nereo-io) */
  --font-heading: var(--font-sans); /* Typography Ink Token (www-nereo-io) */
  --background: 262 76% 95%; /* Canvas / Surface Token (www-nereo-io) */
  --foreground: 262 5% 10%; /* Typography Ink Token (www-nereo-io) */
  --card: 262 50% 90%; /* Dimension / Scale Token (www-nereo-io) */
  --card-foreground: 262 5% 10%; /* Typography Ink Token (www-nereo-io) */
  --popover: 262 76% 95%; /* Dimension / Scale Token (www-nereo-io) */
  --popover-foreground: 262 95% 10%; /* Typography Ink Token (www-nereo-io) */
  --primary: 210 75% 50%; /* Brand / Palette Token (www-nereo-io) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#15191f` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `nav` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#171717` — grounded in `var(--sd-paper)` in `:root`
- **Interactive Accent / Highlight**: `#ffd23f` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#2b8fea` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#262626` — grounded in `var(--sd-line)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `80rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `2rem` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (min-width:1200px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:no-preference)`
- **Corner Radii**: `999px`, `.3125rem`, `.375rem`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `__Unbounded_73c992`
- **Body Font Stack**: `__Outfit_a80a2d`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 60px`, `line-height: 68px`, `font-weight: 700`, `letter-spacing: -0.9px`); CSS variables `--font-display: var(--font-sans)`
- **H2 Section Rule**: live computed `h2` (`font-size: 26px`, `line-height: 32px`, `font-weight: 700`, `letter-spacing: 0.52px`); rule `h2` (`font-size: 1.875rem`, `line-height: 2.25rem`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--removed-body-scroll-bar-size: 0px`; rule `p` (`line-height: 1.625`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: 60px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-nereo-io` (`Nereo — AI Video Generator for Creators & Marketers`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.gap-6> — `www-nereo-io`)**:
   - DOM & Selectors: Landmark `<nav class="gap-6 hidden">` (`1248x40px`) hosting `Nereo — AI Video Generator for Creat` navigation (`Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.gap-6> — `www-nereo-io`)` (`www-nereo-io`) adapts across `@media (min-width:1200px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:no-preference)` with `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`.
2. **Hero Stage & Focal Lead (<section.relative> — `AI Video Generator for Creators & `)**:
   - DOM & Selectors: Landmark `<section class="relative overflow-hidden">` presenting display lead `AI Video Generator for Creators & Marketers` and copy excerpt *"Turn a prompt, a photo or a reference into a finished video. Veo "* over `#15191f` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#15191f` background with `#ffffff` headline `AI Video Generator for Creators & Marketers`.
3. **Primary Showcase & Content Grid (<section.gap-4> — `Nereo Agent Describe the video. Th`)**:
   - DOM & Selectors: Landmark `<section class="gap-4 border-nl-rule">` rendering section `Nereo Agent Describe the video. The agent writes...` with copy *"Start creating free"*, asset references (`e4af272ccee01ff0-s.p.woff2`, `logo.png`, `322e14d06135256b.css`, `a7f88efd924ba4d6.css`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.gap-4> — `Nereo Agent Describe the video. Th`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.border-nl-rule> — `Seedance 2.5 One continuous 30-sec`)**:
   - DOM & Selectors: Landmark `<section class="gap-4 border-nl-rule">` framing `Seedance 2.5 One continuous 30-second take, nativ...` and `Seedance 2.0 Audio and video generated together,...` (*"Describe the video. The agent writes the shots, generates them an"*) with `#171717` surface cards, `#ffd23f` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.border-nl-rule> — `Seedance 2.5 One continuous 30-sec`)` uses `999px`, `.3125rem`, `.375rem`, `2px` radii, `#ffd23f` highlights, and assets (e4af272ccee01ff0-s.p.woff2, logo.png, 322e14d06135256b.css).
5. **Colophon & Global Directory Footer (<footer.antialiased> — `https://www.nereo.io/`)**:
   - DOM & Selectors: Landmark `<footer class="antialiased">` anchoring `Nereo — AI Video Generator for C` footer links (`Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`), copy *"LUMA NOOK — A Daily Tea Ritual"*, and `#262626` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.antialiased> — `https://www.nereo.io/`)` aligns to `80rem` (non-`@media` desktop container stylesheet rule) with `2rem` lateral canvas padding with `24px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Turn a prompt, a photo or a reference into a finished video. Veo 3.1, Seedance 2.5..."*
- Copy Excerpt 2: *"Start creating free"*
- Copy Excerpt 3: *"Describe the video. The agent writes the shots, generates them and cuts them toget..."*
- Copy Excerpt 4: *"LUMA NOOK — A Daily Tea Ritual"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`www-nereo-io`)**:
- `before { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: cubic-bezier(.8,0,1,1)` extracted from `www-nereo-io` stylesheet.
- **Selector `.transition-\[color\2c text-shadow\]`**: `transition: cubic-bezier(.8,0,1,1)` extracted from `www-nereo-io` stylesheet.
- **Selector `grid-template-rows\2c opacity\2c...`**: `transition: cubic-bezier(.8,0,1,1)` extracted from `www-nereo-io` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.8,0,1,1)`)**: Governs interactive state transitions across `<nav.gap-6>` and `<section.gap-4>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-nereo-io`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
