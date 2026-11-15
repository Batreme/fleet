---
title: "UI Prompt Blueprint: useguidely-co"
date: 2026-11-15
target: "[[overview|useguidely-co]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#1f1d1a` canvas, `#fff` ink, `#222` accent)"
---

# UI Design System & Master Generation Blueprint: useguidely-co

> **guidely - the hospitality of the future** (https://useguidely.co/) — A smart guest app that answers questions any hour, recommends what is good right now, plans the day and takes room orders, all from one l...

![Desktop Viewport Capture (1440x3643)](file:///root/projects/fleet/wiki/targets/useguidely-co/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **guidely - the hospitality of the future** (`https://useguidely.co/`). A smart guest app that answers questions any hour, recommends what is good right now, plans the day and takes room orders, all from one l...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#1f1d1a` canvas, `#fff` ink, `#222` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1f1d1a` (`var(--brand)` in `:root`) paired with `#fff` primary typography and `#222` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Satoshi` for display copy (`The smart app for your guests.`) with `PP Mori` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .125rem`, padding `.125rem`) with `cubic-bezier(0,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/useguidely-co/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×3643px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `useguidely-co` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.125rem` lateral canvas padding with `.125rem` grid gap.
- **Border Radius Scale**: `.25rem`, `1rem`, `1.5rem`, `.95rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.125rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1f1d1a` | `var(--brand)` in `:root` |
| **Primary Typography Ink** | `#9b7b4d` | `var(--accent)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--surface)` in `:root` |
| **Interactive Accent / Highlight** | `#222` | `var(--ink)` in `:root` |
| **Secondary / Muted Copy** | `#6f6f6f` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e5e7eb` | `:before { border: #e5e7eb }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand` | `#1f1d1a` | Brand / Palette Token |
| `--accent` | `#9b7b4d` | Brand / Palette Token |
| `--surface` | `#fff` | Canvas / Surface Token |
| `--ink` | `#222` | Typography Ink Token |
| `--muted` | `#6f6f6f` | Color / Atmospheric Token |
| `--line` | `rgba(0,0,0,.08)` | Color / Atmospheric Token |
| `--font-display` | `Georgia,"Times New Roman",serif` | Typography / Scale Token |
| `--vintage-filter` | `sepia(0.24) saturate(1.1) contrast(1.04) brightness(1.02)` | Design System Custom Token |
| `--hop` | `center 42%` | Dimension / Scale Token |
| `--font-name` | `system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-body` | `system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-mono` | `ui-monospace,SFMono-Regular,Menlo,monospace` | Typography / Scale Token |
| `--hero-ready` | `1` | Design System Custom Token |
| `--reveal-delay` | `0ms` | Motion / Easing Token |
| `--useguidely-co-bg` | `#1f1d1a` | Canvas Substrate (from `var(--brand)` in `:root`) |
| `--useguidely-co-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Satoshi`.
- **Primary Body Stack**: `PP Mori`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: Georgia,"Times New Roman",serif`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`).
- **Body Copy**: CSS variables `--font-body: system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif`.
- **Metadata & Navigation Labels**: CSS variables `--font-mono: ui-monospace,SFMono-Regular,Menlo,monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `useguidely-co` stylesheet.
- **Selector `.transition-\[padding\]`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `useguidely-co` stylesheet.
- **Selector `.transition-\[width\]`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `useguidely-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.relative>` and `<section.mt-12>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero-sec>` and `<section.mt-12>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — guidely - the hospitality of the future    │
│ ====================================================================== │
│ [ <header.relative>        | Home · About · Hotels & lodges · Featu ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero-sec>                                   |   │
│ | H1: The smart app for your guests.                               |   │
│ | Substrate: #1f1d1a    | Ink: #fff       | Accent: #222           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.mt-12>           ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | What is a smart app?         |  | B&Bs & guest houses          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .125re) | │
│ | [<header.relative>] -> [<section.hero-sec>] -> [<section.mt-12>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mt-16>        ) | https://useguidely.co/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.relative> — `useguidely-co`)**:
   - Landmark `<header class="relative mx-auto">` hosting `guidely - the hospitality of the fut` navigation (`Home · About · Hotels & lodges · Features · Pricing`), DOM attributes (`data-precedence="next"`, `data-foldout-prefetch`, `data-spark="true"`, `data-reveal="stagger"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.hero-sec> — `The smart app for your guests.`)**:
   - Landmark `<section class="hero-sec mx-auto">` presenting display lead `The smart app for your guests.` and copy excerpt *"Check-in, Wi-Fi, house details, local recommendations, guest ques"* over `#1f1d1a` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.mt-12> — `What is a smart app?`)**:
   - Landmark `<section class="mt-12">` rendering section `What is a smart app?` with copy *"Smart picks for right now"*, asset references (`logo.png`, `hero-cover-19.jpg`, `001c094435c96c6a.css`, `webpack-61e7ac9f112b97ad.js`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `B&Bs & guest houses`)**:
   - Landmark `<section class="mx-auto px-6">` framing `B&Bs & guest houses` and `Boutique hotels` (*"Experiences & activities"*) with `#fff` surface cards, `#222` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mt-16> — `https://useguidely.co/`)**:
   - Landmark `<footer class="mt-16">` anchoring `guidely - the hospitality of the` footer links (`Home · About · Hotels & lodges · Features · Pricing`), copy *"Room service ordering"*, and `#e5e7eb` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: useguidely-co (guidely - the hospitality of the future)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `useguidely-co` (**guidely - the hospitality of the future** — `https://useguidely.co/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#1f1d1a` canvas, `#fff` ink, `#222` accent).
- **Identity & Domain Context**: A smart guest app that answers questions any hour, recommends what is good right now, plans the day and takes room orders, all from one l...
- **Primary Substrate**: `#1f1d1a` (`var(--brand)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#222`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1f1d1a` (`var(--brand)` in `:root`) paired with `#fff` primary typography and `#222` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Satoshi` for display copy (`The smart app for your guests.`) with `PP Mori` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .125rem`, padding `.125rem`) with `cubic-bezier(0,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `useguidely-co` in your global stylesheet:

:root {
  /* guidely - the hospitality of the future (useguidely-co) — Ground-Truth Extracted CSS Variables */
  --brand: #1f1d1a; /* Brand / Palette Token (useguidely-co) */
  --accent: #9b7b4d; /* Brand / Palette Token (useguidely-co) */
  --surface: #fff; /* Canvas / Surface Token (useguidely-co) */
  --ink: #222; /* Typography Ink Token (useguidely-co) */
  --muted: #6f6f6f; /* Color / Atmospheric Token (useguidely-co) */
  --line: rgba(0,0,0,.08); /* Color / Atmospheric Token (useguidely-co) */
  --font-display: Georgia,"Times New Roman",serif; /* Typography / Scale Token (useguidely-co) */
  --vintage-filter: sepia(0.24) saturate(1.1) contrast(1.04) brightness(1.02); /* Design System Custom Token (useguidely-co) */
  --hop: center 42%; /* Dimension / Scale Token (useguidely-co) */
  --font-name: system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; /* Typography / Scale Token (useguidely-co) */
  --font-body: system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; /* Typography / Scale Token (useguidely-co) */
  --font-mono: ui-monospace,SFMono-Regular,Menlo,monospace; /* Typography / Scale Token (useguidely-co) */
  --hero-ready: 1; /* Design System Custom Token (useguidely-co) */
  --reveal-delay: 0ms; /* Motion / Easing Token (useguidely-co) */
  --useguidely-co-bg: #1f1d1a; /* Canvas Substrate (from `var(--brand)` in `:root`) (useguidely-co) */
  --useguidely-co-ink: #fff; /* Primary Typography Ink (stylesheet-derived) (useguidely-co) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#1f1d1a` — grounded in `var(--brand)` in `:root`
- **Primary Typography Ink**: `#9b7b4d` — grounded in `var(--accent)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--surface)` in `:root`
- **Interactive Accent / Highlight**: `#222` — grounded in `var(--ink)` in `:root`
- **Secondary / Muted Copy**: `#6f6f6f` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#e5e7eb` — grounded in `:before { border: #e5e7eb }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×3643px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `useguidely-co` stylesheet
- **Padding & Gutters**: `.125rem` lateral canvas padding with `.125rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.125rem` horizontal padding
- **Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`
- **Corner Radii**: `.25rem`, `1rem`, `1.5rem`, `.95rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `PP Mori`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-display: Georgia,"Times New Roman",serif`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Body Copy Rule**: CSS variables `--font-body: system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif`
- **Metadata & Index Rule**: CSS variables `--font-mono: ui-monospace,SFMono-Regular,Menlo,monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `useguidely-co` (`guidely - the hospitality of the future`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.relative> — `useguidely-co`)**:
   - DOM & Selectors: Landmark `<header class="relative mx-auto">` hosting `guidely - the hospitality of the fut` navigation (`Home · About · Hotels & lodges · Features · Pricing`), DOM attributes (`data-precedence="next"`, `data-foldout-prefetch`, `data-spark="true"`, `data-reveal="stagger"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.relative> — `useguidely-co`)` (`useguidely-co`) adapts across `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Home · About · Hotels & lodges · Features · Pricing`.
2. **Hero Stage & Focal Lead (<section.hero-sec> — `The smart app for your guests.`)**:
   - DOM & Selectors: Landmark `<section class="hero-sec mx-auto">` presenting display lead `The smart app for your guests.` and copy excerpt *"Check-in, Wi-Fi, house details, local recommendations, guest ques"* over `#1f1d1a` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×3643px` desktop / `390×2400px` mobile) sets `#1f1d1a` background with `#fff` headline `The smart app for your guests.`.
3. **Primary Showcase & Content Grid (<section.mt-12> — `What is a smart app?`)**:
   - DOM & Selectors: Landmark `<section class="mt-12">` rendering section `What is a smart app?` with copy *"Smart picks for right now"*, asset references (`logo.png`, `hero-cover-19.jpg`, `001c094435c96c6a.css`, `webpack-61e7ac9f112b97ad.js`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.mt-12> — `What is a smart app?`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.125rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `B&Bs & guest houses`)**:
   - DOM & Selectors: Landmark `<section class="mx-auto px-6">` framing `B&Bs & guest houses` and `Boutique hotels` (*"Experiences & activities"*) with `#fff` surface cards, `#222` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.mx-auto> — `B&Bs & guest houses`)` uses `.25rem`, `1rem`, `1.5rem`, `.95rem` radii, `#222` highlights, and assets (logo.png, hero-cover-19.jpg, 001c094435c96c6a.css).
5. **Colophon & Global Directory Footer (<footer.mt-16> — `https://useguidely.co/`)**:
   - DOM & Selectors: Landmark `<footer class="mt-16">` anchoring `guidely - the hospitality of the` footer links (`Home · About · Hotels & lodges · Features · Pricing`), copy *"Room service ordering"*, and `#e5e7eb` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mt-16> — `https://useguidely.co/`)` aligns to `640px` extracted from `useguidely-co` stylesheet with `.125rem` lateral canvas padding with `.125rem` grid gap and attributes (data-precedence="next", data-foldout-prefetch, data-spark="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Check-in, Wi-Fi, house details, local recommendations, guest questions, orders and..."*
- Copy Excerpt 2: *"Smart picks for right now"*
- Copy Excerpt 3: *"Experiences & activities"*
- Copy Excerpt 4: *"Room service ordering"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`useguidely-co`)**:
- `before { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `useguidely-co` stylesheet.
- **Selector `.transition-\[padding\]`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `useguidely-co` stylesheet.
- **Selector `.transition-\[width\]`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `useguidely-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.relative>` and `<section.mt-12>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero-sec>` and `<section.mt-12>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `useguidely-co`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
