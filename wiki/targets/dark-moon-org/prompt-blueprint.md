---
title: "UI Prompt Blueprint: dark-moon-org"
date: 2026-11-15
target: "dark-moon-org"
status: analyzed
capture: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#dceaf4` ink, `#b9c7d6` accent)"
---

# UI Design System & Master Generation Blueprint: dark-moon-org

> **Darkmoon: Autonomous AI Penetration Testing Platform** (https://dark-moon.org/) — Darkmoon is an open-source, AI-powered autonomous penetration testing platform. 50 specialized AI agents covering web, cloud, identity, C...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Darkmoon: Autonomous AI Penetration Testing Platform** (`https://dark-moon.org/`). Darkmoon is an open-source, AI-powered autonomous penetration testing platform. 50 specialized AI agents covering web, cloud, identity, C...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#dceaf4` ink, `#b9c7d6` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--ed-bg)` in `:root`) paired with `#dceaf4` primary typography and `#b9c7d6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Title Fallback` for display copy (`Darkmoon, Autonomous AI Penetration `) with `Poppins` and `Google Sans Code`.
  - **Calibrated Spatial Grid & Motion**: Combines `767.98px` container bounds (`gap: 22px`, padding `16px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×17311px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `767.98px` extracted from `dark-moon-org` stylesheet.
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `22px` grid gap.
- **Border Radius Scale**: `var(--nb-r-btn)`, `var(--nb-r-card)`, `999px`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767.98px`, `gap: 22px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767.98px)`, `@media (pointer:coarse) and (max-width:1023px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--ed-bg)` in `:root` |
| **Primary Typography Ink** | `#0b0d13` | `var(--ed-pale)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dceaf4` | `var(--ed-fg)` in `:root` |
| **Interactive Accent / Highlight** | `#b9c7d6` | `var(--ed-soft)` in `:root` |
| **Secondary / Muted Copy** | `#8e9baa` | `var(--ed-mute)` in `:root` |
| **Structural Hairline Border** | `#87bfff` | `var(--ed-acc)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--nb-glow` | `59,38,204` | Design System Custom Token |
| `--nb-gx` | `10%` | Dimension / Scale Token |
| `--m-ink` | `var(--dm-offwhite)` | Typography Ink Token |
| `--m-moon-bg` | `transparent` | Canvas / Surface Token |
| `--m-moon` | `transparent` | Design System Custom Token |
| `--m-line-light` | `rgba(220,234,244,0.22)` | Canvas / Surface Token |
| `--m-rule-light` | `rgba(220,234,244,0.45)` | Canvas / Surface Token |
| `--gl-liquidgl` | `0` | Design System Custom Token |
| `--ed-bg` | `#000` | Canvas / Surface Token |
| `--ed-pale` | `#0b0d13` | Color / Atmospheric Token |
| `--ed-fg` | `#dceaf4` | Typography Ink Token |
| `--ed-soft` | `#b9c7d6` | Color / Atmospheric Token |
| `--ed-mute` | `#8e9baa` | Color / Atmospheric Token |
| `--ed-line` | `rgba(220,234,244,0.16)` | Color / Atmospheric Token |
| `--ed-acc` | `#87bfff` | Color / Atmospheric Token |
| `--ed-title` | `var(--font-display),"Space Mono",monospace` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DM Title Fallback`.
- **Primary Body Stack**: `Poppins`.
- **Technical / Metadata Stack**: `Google Sans Code`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--m-display: clamp(3.5rem,calc(2rem + 8.2vw),4.5rem)`, `--m-h1: clamp(2.25rem,calc(1.25rem + 5.13vw),2.75rem)`, `--dm-display: var(--m-display)`; rule `.h1` (`font-size: var(--m-h1)`, `line-height: .95`, `letter-spacing: -.02em`, `font-weight: 500`).
- **Section Heading (`H2`)**: CSS variables `--nb-sh2: #e4e8ec`; rule `h2` (`letter-spacing: -.01em!important`).
- **Body Copy**: CSS variables `--m-body: 1.0625rem`, `--dm-body: var(--m-body)`, `--text-base: 1rem`; rule `p` (`font-size: 12px!important`).
- **Metadata & Navigation Labels**: CSS variables `--cv-mono: var(--font-code),"Google Sans Code",monospace`, `--m-caption: 0.8125rem`, `--m-mono: 0.75rem`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.19,1,0.22,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.dm-pill`**: `transition: transform .12s ease,box-shadow .12s ease,background-color .15s...` extracted from `dark-moon-org` stylesheet.
- **Selector `adius)]"][class*="border-[var(--d...`**: `transition: transform .15s ease,box-shadow .15s ease` extracted from `dark-moon-org` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `dark-moon-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Darkmoon: Autonomous AI Penetration Testin │
│ ====================================================================== │
│ [ <header.fixed>           | Product · Pricing · Docs · Blog        ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.dm-hero>                                    |   │
│ | H1: Darkmoon, Autonomous AI Penetration Testing Platform         |   │
│ | Substrate: #000       | Ink: #dceaf4    | Accent: #b9c7d6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 767.98px       |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Attack surface camp_20260426 |  | Not a scanner. An autonomous | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 22px  ) | │
│ | [<header.fixed>] -> [<section.dm-hero>] -> [<section.relative>] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://dark-moon.org/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `dark-moon-org`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `Darkmoon: Autonomous AI Penetration ` navigation (`Product · Pricing · Docs · Blog`), DOM attributes (`data-route-lang="en"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.dm-pill:hover { transform:translate(-2px,-2px);box-shadow:5.1px 5.1px 0 var(--nb-sh-btn) }`.
2. **Hero Stage & Focal Lead (<section.dm-hero> — `Darkmoon, Autonomous AI Penetratio`)**:
   - Landmark `<section class="dm-hero w6">` presenting display lead `Darkmoon, Autonomous AI Penetration Testing Platform` and copy excerpt *"D D A A R R K K M M O O O O N N"* over `#000` canvas and `#dceaf4` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Attack surface camp_20260426_3d2f `)**:
   - Landmark `<section class="relative scroll-mt-24">` rendering section `Attack surface camp_20260426_3d2f · 26 Apr 2026` with copy *"Autonomous, continuous penetration testing"*, asset references (`eafabf029ad39a43-s.p.woff2`, `c15382663895c1a1.css`, `6e008cfa72251405.css`, `e824d722814de74c.css`), and grid rule `hover { box-shadow:5.1px 5.1px 0 rgba(0,0,0,.75) }`.
4. **Interactive Detail & Feature Matrix (<section.dc> — `Not a scanner. An autonomous secur`)**:
   - Landmark `<section class="dc dc--default">` framing `Not a scanner. An autonomous security conductor.` and `Darkmoon + Splunk: Send AI Pentest Findings to Yo...` (*"Autonomous, continuous"*) with `#dceaf4` surface cards, `#b9c7d6` accents, and `.dm-pill:active { transform:translate(4px,4px);box-shadow:0 0 0 var(--nb-sh-btn) }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://dark-moon.org/`)**:
   - Landmark `<footer class="relative bg-white">` anchoring `Darkmoon: Autonomous AI Penetrat` footer links (`Product · Pricing · Docs · Blog`), copy *"penetration testing"*, and `#87bfff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dark-moon-org (Darkmoon: Autonomous AI Penetration Testing Platform)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dark-moon-org` (**Darkmoon: Autonomous AI Penetration Testing Platform** — `https://dark-moon.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#dceaf4` ink, `#b9c7d6` accent).
- **Identity & Domain Context**: Darkmoon is an open-source, AI-powered autonomous penetration testing platform. 50 specialized AI agents covering web, cloud, identity, C...
- **Primary Substrate**: `#000` (`var(--ed-bg)` in `:root`), **Primary Ink**: `#dceaf4`, **Accent / Highlight**: `#b9c7d6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--ed-bg)` in `:root`) paired with `#dceaf4` primary typography and `#b9c7d6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Title Fallback` for display copy (`Darkmoon, Autonomous AI Penetration `) with `Poppins` and `Google Sans Code`.
  - **Calibrated Spatial Grid & Motion**: Combines `767.98px` container bounds (`gap: 22px`, padding `16px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dark-moon-org` in your global stylesheet:

:root {
  /* Darkmoon: Autonomous AI Penetration Testing Platform (dark-moon-org) — Ground-Truth Extracted CSS Variables */
  --nb-glow: 59,38,204; /* Design System Custom Token (dark-moon-org) */
  --nb-gx: 10%; /* Dimension / Scale Token (dark-moon-org) */
  --m-ink: var(--dm-offwhite); /* Typography Ink Token (dark-moon-org) */
  --m-moon-bg: transparent; /* Canvas / Surface Token (dark-moon-org) */
  --m-moon: transparent; /* Design System Custom Token (dark-moon-org) */
  --m-line-light: rgba(220,234,244,0.22); /* Canvas / Surface Token (dark-moon-org) */
  --m-rule-light: rgba(220,234,244,0.45); /* Canvas / Surface Token (dark-moon-org) */
  --gl-liquidgl: 0; /* Design System Custom Token (dark-moon-org) */
  --ed-bg: #000; /* Canvas / Surface Token (dark-moon-org) */
  --ed-pale: #0b0d13; /* Color / Atmospheric Token (dark-moon-org) */
  --ed-fg: #dceaf4; /* Typography Ink Token (dark-moon-org) */
  --ed-soft: #b9c7d6; /* Color / Atmospheric Token (dark-moon-org) */
  --ed-mute: #8e9baa; /* Color / Atmospheric Token (dark-moon-org) */
  --ed-line: rgba(220,234,244,0.16); /* Color / Atmospheric Token (dark-moon-org) */
  --ed-acc: #87bfff; /* Color / Atmospheric Token (dark-moon-org) */
  --ed-title: var(--font-display),"Space Mono",monospace; /* Design System Custom Token (dark-moon-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--ed-bg)` in `:root`
- **Primary Typography Ink**: `#0b0d13` — grounded in `var(--ed-pale)` in `:root`
- **Elevated Surface / Card Substrate**: `#dceaf4` — grounded in `var(--ed-fg)` in `:root`
- **Interactive Accent / Highlight**: `#b9c7d6` — grounded in `var(--ed-soft)` in `:root`
- **Secondary / Muted Copy**: `#8e9baa` — grounded in `var(--ed-mute)` in `:root`
- **Structural Hairline Border**: `#87bfff` — grounded in `var(--ed-acc)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×17311px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `767.98px` extracted from `dark-moon-org` stylesheet
- **Padding & Gutters**: `16px` lateral canvas padding with `22px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767.98px`, `gap: 22px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767.98px)`, `@media (pointer:coarse) and (max-width:1023px)`
- **Corner Radii**: `var(--nb-r-btn)`, `var(--nb-r-card)`, `999px`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DM Title Fallback`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `Google Sans Code`
- **H1 Display Rule**: CSS variables `--m-display: clamp(3.5rem,calc(2rem + 8.2vw),4.5rem)`, `--m-h1: clamp(2.25rem,calc(1.25rem + 5.13vw),2.75rem)`, `--dm-display: var(--m-display)`; rule `.h1` (`font-size: var(--m-h1)`, `line-height: .95`, `letter-spacing: -.02em`, `font-weight: 500`)
- **H2 Section Rule**: CSS variables `--nb-sh2: #000`; rule `h2` (`letter-spacing: -.01em!important`)
- **Body Copy Rule**: CSS variables `--m-body: 1.0625rem`, `--dm-body: var(--m-body)`, `--text-base: 1rem`; rule `p` (`font-size: 12px!important`)
- **Metadata & Index Rule**: CSS variables `--cv-mono: var(--font-code),"Google Sans Code",monospace`, `--m-caption: 0.8125rem`, `--m-mono: 0.75rem`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dark-moon-org` (`Darkmoon: Autonomous AI Penetration Testing Platform`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `dark-moon-org`)**:
   - DOM & Selectors: Landmark `<header class="fixed inset-x-0">` hosting `Darkmoon: Autonomous AI Penetration ` navigation (`Product · Pricing · Docs · Blog`), DOM attributes (`data-route-lang="en"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.dm-pill:hover { transform:translate(-2px,-2px);box-shadow:5.1px 5.1px 0 var(--nb-sh-btn) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `dark-moon-org`)` (`dark-moon-org`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767.98px)`, `@media (pointer:coarse) and (max-width:1023px)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.19,1,0.22,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Product · Pricing · Docs · Blog`.
2. **Hero Stage & Focal Lead (<section.dm-hero> — `Darkmoon, Autonomous AI Penetratio`)**:
   - DOM & Selectors: Landmark `<section class="dm-hero w6">` presenting display lead `Darkmoon, Autonomous AI Penetration Testing Platform` and copy excerpt *"D D A A R R K K M M O O O O N N"* over `#000` canvas and `#dceaf4` ink.
   - Responsive Contract: Hero stage (`1440×17311px` desktop / `390×2400px` mobile) sets `#000` background with `#dceaf4` headline `Darkmoon, Autonomous AI Penetration Testing Platform`.
3. **Primary Showcase & Content Grid (<section.relative> — `Attack surface camp_20260426_3d2f `)**:
   - DOM & Selectors: Landmark `<section class="relative scroll-mt-24">` rendering section `Attack surface camp_20260426_3d2f · 26 Apr 2026` with copy *"Autonomous, continuous penetration testing"*, asset references (`eafabf029ad39a43-s.p.woff2`, `c15382663895c1a1.css`, `6e008cfa72251405.css`, `e824d722814de74c.css`), and grid rule `hover { box-shadow:5.1px 5.1px 0 rgba(0,0,0,.75) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `Attack surface camp_20260426_3d2f `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767.98px`, `gap: 22px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.dc> — `Not a scanner. An autonomous secur`)**:
   - DOM & Selectors: Landmark `<section class="dc dc--default">` framing `Not a scanner. An autonomous security conductor.` and `Darkmoon + Splunk: Send AI Pentest Findings to Yo...` (*"Autonomous, continuous"*) with `#dceaf4` surface cards, `#b9c7d6` accents, and `.dm-pill:active { transform:translate(4px,4px);box-shadow:0 0 0 var(--nb-sh-btn) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.dc> — `Not a scanner. An autonomous secur`)` uses `var(--nb-r-btn)`, `var(--nb-r-card)`, `999px`, `3px` radii, `#b9c7d6` highlights, and assets (eafabf029ad39a43-s.p.woff2, c15382663895c1a1.css, 6e008cfa72251405.css).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://dark-moon.org/`)**:
   - DOM & Selectors: Landmark `<footer class="relative bg-white">` anchoring `Darkmoon: Autonomous AI Penetrat` footer links (`Product · Pricing · Docs · Blog`), copy *"penetration testing"*, and `#87bfff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://dark-moon.org/`)` aligns to `767.98px` extracted from `dark-moon-org` stylesheet with `16px` lateral canvas padding with `22px` grid gap and attributes (data-route-lang="en", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"D D A A R R K K M M O O O O N N"*
- Copy Excerpt 2: *"Autonomous, continuous penetration testing"*
- Copy Excerpt 3: *"Autonomous, continuous"*
- Copy Excerpt 4: *"penetration testing"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.19,1,0.22,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`dark-moon-org`)**:
- `.dm-pill:hover { transform:translate(-2px,-2px);box-shadow:5.1px 5.1px 0 var(--nb-sh-btn) }`
- `hover { box-shadow:5.1px 5.1px 0 rgba(0,0,0,.75) }`
- `.dm-pill:active { transform:translate(4px,4px);box-shadow:0 0 0 var(--nb-sh-btn) }`
- `span { border:1px solid var(--nb-line)!important;border-radius:0!important;box-... }`
- `last-of-type { box-shadow:var(--nb-s2) var(--nb-s2) 0 var(--nb-sh) }`
- **Per-Selector Transition Rules**:
- **Selector `.dm-pill`**: `transition: transform .12s ease,box-shadow .12s ease,background-color .15s...` extracted from `dark-moon-org` stylesheet.
- **Selector `adius)]"][class*="border-[var(--d...`**: `transition: transform .15s ease,box-shadow .15s ease` extracted from `dark-moon-org` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `dark-moon-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dark-moon-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
