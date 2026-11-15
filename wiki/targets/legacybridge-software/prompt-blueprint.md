---
title: "UI Prompt Blueprint: legacybridge-software"
date: 2026-11-15
target: "legacybridge-software"
status: analyzed
capture: specimen
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#082a1c` canvas, `#ffffff` ink, `#94a3b8` accent)"
---

# UI Design System & Master Generation Blueprint: legacybridge-software

> **AI Document Entry for AS/400 & Legacy Systems · LegacyBridge** (https://legacybridge.software/) — An AI agent that reads invoices, orders and claims and keys them into AS/400 (IBM i), mainframe and other legacy systems. Human approval,...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **AI Document Entry for AS/400 & Legacy Systems · LegacyBridge** (`https://legacybridge.software/`). An AI agent that reads invoices, orders and claims and keys them into AS/400 (IBM i), mainframe and other legacy systems. Human approval,...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#082a1c` canvas, `#ffffff` ink, `#94a3b8` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#082a1c` (`var(--text-ink)` in `:root`) paired with `#ffffff` primary typography and `#94a3b8` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Stop retyping invoices, claims and o`) with `Geist Mono` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 16px`, padding `12px`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×19851px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `767px` extracted from `legacybridge-software` stylesheet.
- **Canvas Lateral Padding & Spacing**: `12px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `var(--radius-full)`, `1px`, `12px`, `var(--radius-16)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 767px)`, `@media (max-width: 1700px)`, `@media (max-width: 1599px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#082a1c` | `var(--text-ink)` in `:root` |
| **Primary Typography Ink** | `#64707a` | `var(--text-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--text-inverse)` in `:root` |
| **Interactive Accent / Highlight** | `#94a3b8` | `var(--text-inverse-muted)` in `:root` |
| **Secondary / Muted Copy** | `#cdff8c` | `var(--brand-accent)` in `:root` |
| **Structural Hairline Border** | `#f4f7f9` | `var(--surface-card)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ring-m` | `max(16px, calc(50vw - 704px))` | Elevation / Border Token |
| `--rot-h` | `58px` | Dimension / Scale Token |
| `--rot-step` | `88px` | Dimension / Scale Token |
| `--rot-nudge` | `-2px` | Dimension / Scale Token |
| `--rise` | `110px` | Dimension / Scale Token |
| `--rise-ease` | `cubic-bezier(0, 1, 0.4, 1)` | Motion / Easing Token |
| `--text-ink` | `#082a1c` | Typography Ink Token |
| `--text-muted` | `#64707a` | Typography Ink Token |
| `--text-inverse` | `#ffffff` | Typography Ink Token |
| `--text-inverse-muted` | `#94a3b8` | Typography Ink Token |
| `--brand-primary` | `#082a1c` | Brand / Palette Token |
| `--brand-secondary` | `#94a3b8` | Brand / Palette Token |
| `--brand-accent` | `#cdff8c` | Brand / Palette Token |
| `--surface-white` | `#ffffff` | Canvas / Surface Token |
| `--surface-page` | `#ffffff` | Canvas / Surface Token |
| `--surface-card` | `#f4f7f9` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist Mono`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.h1` (`letter-spacing: -0.05em`).
- **Section Heading (`H2`)**: rule `.h2` (`letter-spacing: -0.04em`).
- **Body Copy**: rule `body` (`letter-spacing: -0.04em`).
- **Metadata & Navigation Labels**: CSS variables `--mono: "Geist Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace`; rule `.caption` (`letter-spacing: -0.04em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(0,1,.4,1)`, `cubic-bezier(0,1,0.4,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.announce`**: `transition: transform .45s cubic-bezier(.16,1,.3,1)` extracted from `legacybridge-software` stylesheet.
- **Selector `media (prefers-reduced-motion: re...`**: `transition: none` extracted from `legacybridge-software` stylesheet.
- **Selector `.announce__link`**: `transition: opacity .25s ease` extracted from `legacybridge-software` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.compare-cards>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — AI Document Entry for AS/400 & Legacy Syst │
│ ====================================================================== │
│ [ <header.site-header>     | How it works · Solutions · Use cases · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Stop retyping invoices, claims and orders into AS...         |   │
│ | Substrate: #082a1c    | Ink: #ffffff    | Accent: #94a3b8        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.compare-cards>   ) max-w: 767px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Your AS/400 (IBM i) system i |  | Hours of processing & typing | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.site-heade] -> [<section.hero>] -> [<section.compare-c] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://legacybridge.software/     │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `legacybridge-software`)**:
   - Landmark `<header class="site-header">` hosting `AI Document Entry for AS/400 & Legac` navigation (`How it works · Solutions · Use cases · Blog · Why us`), DOM attributes (`data-lb-cta="header"`, `data-label="Book a demo"`, `data-label="Book"`, `data-contact-open="header"`), and stylesheet rule `.announce.is-tucked { transform: translateY(-100%); }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Stop retyping invoices, claims and`)**:
   - Landmark `<section class="hero">` presenting display lead `Stop retyping invoices, claims and orders into AS...` and copy excerpt *"legacy bridge is now part of scandiweb"* over `#082a1c` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.compare-cards> — `Your AS/400 (IBM i) system is not `)**:
   - Landmark `<section class="compare-cards">` rendering section `Your AS/400 (IBM i) system is not the problem. Th...` with copy *"Read the announcement Read more"*, asset references (`favicon.svg`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `.announce { transition: none; }`.
4. **Interactive Detail & Feature Matrix (<article.compare-cards__card> — `Hours of processing & typing`)**:
   - Landmark `<article class="compare-cards__card compare-cards__card--without">` framing `Hours of processing & typing` and `Seconds to approve` (*"Read the announcement"*) with `#ffffff` surface cards, `#94a3b8` accents, and `.announce.is-hidden { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://legacybridge.software/`)**:
   - Landmark `<footer class="site-footer is-offscreen">` anchoring `AI Document Entry for AS/400 & L` footer links (`How it works · Solutions · Use cases · Blog · Why us`), copy *"Document entry automation for AS/400 (IBM i)"*, and `#f4f7f9` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: legacybridge-software (AI Document Entry for AS/400 & Legacy Systems · LegacyBridge)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `legacybridge-software` (**AI Document Entry for AS/400 & Legacy Systems · LegacyBridge** — `https://legacybridge.software/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#082a1c` canvas, `#ffffff` ink, `#94a3b8` accent).
- **Identity & Domain Context**: An AI agent that reads invoices, orders and claims and keys them into AS/400 (IBM i), mainframe and other legacy systems. Human approval,...
- **Primary Substrate**: `#082a1c` (`var(--text-ink)` in `:root`), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#94a3b8`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#082a1c` (`var(--text-ink)` in `:root`) paired with `#ffffff` primary typography and `#94a3b8` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Stop retyping invoices, claims and o`) with `Geist Mono` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 16px`, padding `12px`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `legacybridge-software` in your global stylesheet:

:root {
  /* AI Document Entry for AS/400 & Legacy Systems · LegacyBridge (legacybridge-software) — Ground-Truth Extracted CSS Variables */
  --ring-m: max(16px, calc(50vw - 704px)); /* Elevation / Border Token (legacybridge-software) */
  --rot-h: 58px; /* Dimension / Scale Token (legacybridge-software) */
  --rot-step: 88px; /* Dimension / Scale Token (legacybridge-software) */
  --rot-nudge: -2px; /* Dimension / Scale Token (legacybridge-software) */
  --rise: 110px; /* Dimension / Scale Token (legacybridge-software) */
  --rise-ease: cubic-bezier(0, 1, 0.4, 1); /* Motion / Easing Token (legacybridge-software) */
  --text-ink: #082a1c; /* Typography Ink Token (legacybridge-software) */
  --text-muted: #64707a; /* Typography Ink Token (legacybridge-software) */
  --text-inverse: #ffffff; /* Typography Ink Token (legacybridge-software) */
  --text-inverse-muted: #94a3b8; /* Typography Ink Token (legacybridge-software) */
  --brand-primary: #082a1c; /* Brand / Palette Token (legacybridge-software) */
  --brand-secondary: #94a3b8; /* Brand / Palette Token (legacybridge-software) */
  --brand-accent: #cdff8c; /* Brand / Palette Token (legacybridge-software) */
  --surface-white: #ffffff; /* Canvas / Surface Token (legacybridge-software) */
  --surface-page: #ffffff; /* Canvas / Surface Token (legacybridge-software) */
  --surface-card: #f4f7f9; /* Canvas / Surface Token (legacybridge-software) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#082a1c` — grounded in `var(--text-ink)` in `:root`
- **Primary Typography Ink**: `#64707a` — grounded in `var(--text-muted)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `var(--text-inverse)` in `:root`
- **Interactive Accent / Highlight**: `#94a3b8` — grounded in `var(--text-inverse-muted)` in `:root`
- **Secondary / Muted Copy**: `#cdff8c` — grounded in `var(--brand-accent)` in `:root`
- **Structural Hairline Border**: `#f4f7f9` — grounded in `var(--surface-card)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×19851px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `767px` extracted from `legacybridge-software` stylesheet
- **Padding & Gutters**: `12px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 767px)`, `@media (max-width: 1700px)`, `@media (max-width: 1599px)`
- **Corner Radii**: `var(--radius-full)`, `1px`, `12px`, `var(--radius-16)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: rule `.h1` (`letter-spacing: -0.05em`)
- **H2 Section Rule**: rule `.h2` (`letter-spacing: -0.04em`)
- **Body Copy Rule**: rule `body` (`letter-spacing: -0.04em`)
- **Metadata & Index Rule**: CSS variables `--mono: "Geist Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace`; rule `.caption` (`letter-spacing: -0.04em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `legacybridge-software` (`AI Document Entry for AS/400 & Legacy Systems · LegacyBridge`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `legacybridge-software`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` hosting `AI Document Entry for AS/400 & Legac` navigation (`How it works · Solutions · Use cases · Blog · Why us`), DOM attributes (`data-lb-cta="header"`, `data-label="Book a demo"`, `data-label="Book"`, `data-contact-open="header"`), and stylesheet rule `.announce.is-tucked { transform: translateY(-100%); }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `legacybridge-software`)` (`legacybridge-software`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 767px)`, `@media (max-width: 1700px)`, `@media (max-width: 1599px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(0,1,.4,1)`, `cubic-bezier(0,1,0.4,1)` transitions and links `How it works · Solutions · Use cases · Blog · Why us`.
2. **Hero Stage & Focal Lead (<section.hero> — `Stop retyping invoices, claims and`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Stop retyping invoices, claims and orders into AS...` and copy excerpt *"legacy bridge is now part of scandiweb"* over `#082a1c` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×19851px` desktop / `390×2400px` mobile) sets `#082a1c` background with `#ffffff` headline `Stop retyping invoices, claims and orders into AS...`.
3. **Primary Showcase & Content Grid (<section.compare-cards> — `Your AS/400 (IBM i) system is not `)**:
   - DOM & Selectors: Landmark `<section class="compare-cards">` rendering section `Your AS/400 (IBM i) system is not the problem. Th...` with copy *"Read the announcement Read more"*, asset references (`favicon.svg`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `.announce { transition: none; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.compare-cards> — `Your AS/400 (IBM i) system is not `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `12px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.compare-cards__card> — `Hours of processing & typing`)**:
   - DOM & Selectors: Landmark `<article class="compare-cards__card compare-cards__card--without">` framing `Hours of processing & typing` and `Seconds to approve` (*"Read the announcement"*) with `#ffffff` surface cards, `#94a3b8` accents, and `.announce.is-hidden { display: none; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.compare-cards__card> — `Hours of processing & typing`)` uses `var(--radius-full)`, `1px`, `12px`, `var(--radius-16)` radii, `#94a3b8` highlights, and assets (favicon.svg, favicon-32.png, icon-192.png).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://legacybridge.software/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer is-offscreen">` anchoring `AI Document Entry for AS/400 & L` footer links (`How it works · Solutions · Use cases · Blog · Why us`), copy *"Document entry automation for AS/400 (IBM i)"*, and `#f4f7f9` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://legacybridge.software/`)` aligns to `767px` extracted from `legacybridge-software` stylesheet with `12px` lateral canvas padding with `16px` grid gap and attributes (data-lb-cta="header", data-label="Book a demo", data-label="Book").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"legacy bridge is now part of scandiweb"*
- Copy Excerpt 2: *"Read the announcement Read more"*
- Copy Excerpt 3: *"Read the announcement"*
- Copy Excerpt 4: *"Document entry automation for AS/400 (IBM i)"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(0,1,.4,1)`, `cubic-bezier(0,1,0.4,1)`
- **Extracted Stylesheet Rules (`legacybridge-software`)**:
- `.announce.is-tucked { transform: translateY(-100%); }`
- `.announce { transition: none; }`
- `.announce.is-hidden { display: none; }`
- `.announce__inner { display: flex; align-items: center; gap: 16px; }`
- `.announce__text { margin: 0; font: 600 16px/20px var(--font); letter-spacing: -0.04em; whi... }`
- **Per-Selector Transition Rules**:
- **Selector `.announce`**: `transition: transform .45s cubic-bezier(.16,1,.3,1)` extracted from `legacybridge-software` stylesheet.
- **Selector `media (prefers-reduced-motion: re...`**: `transition: none` extracted from `legacybridge-software` stylesheet.
- **Selector `.announce__link`**: `transition: opacity .25s ease` extracted from `legacybridge-software` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.compare-cards>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `legacybridge-software`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
