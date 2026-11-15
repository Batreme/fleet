---
title: "UI Prompt Blueprint: sinedogma-com-tr"
date: 2026-11-15
target: "sinedogma-com-tr"
status: analyzed
capture: dom
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#d9d9d9` accent)"
---

# UI Design System & Master Generation Blueprint: sinedogma-com-tr

> **sinedogma** (https://sinedogma.com.tr/) — sinedogma ve dogma yayın: dijital arşiv, dergiler, kitaplar, haberler ve satış noktaları.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **sinedogma** (`https://sinedogma.com.tr/`). sinedogma ve dogma yayın: dijital arşiv, dergiler, kitaplar, haberler ve satış noktaları.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#d9d9d9` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--paper)` in `:root`) paired with `#000` primary typography and `#d9d9d9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `EB Garamond Local` for display copy (`iki yayın tek dolaşım`) with `Garamond` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--reading)` container bounds (`gap: 24px`, padding `34px`) with `cubic-bezier(.22,.61,.36,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6895px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--reading)` extracted from `sinedogma-com-tr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `34px` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `50%`, `999px`, `7px`, `5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--reading)`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `34px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 860px)`, `@media (max-width: 600px)`, `@media (max-width: 700px)`, `@media (max-width:600px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#111` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6f6f6f` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#d9d9d9` | `var(--line)` in `:root` |
| **Secondary / Muted Copy** | `#f5f5f3` | `var(--soft)` in `:root` |
| **Structural Hairline Border** | `#000` | `var(--w2w-start-background-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#fff` | Canvas / Surface Token |
| `--ink` | `#111` | Typography Ink Token |
| `--muted` | `#6f6f6f` | Color / Atmospheric Token |
| `--line` | `#d9d9d9` | Color / Atmospheric Token |
| `--soft` | `#f5f5f3` | Color / Atmospheric Token |
| `--max` | `1080px` | Dimension / Scale Token |
| `--reading` | `680px` | Dimension / Scale Token |
| `--motion-fast` | `160ms` | Motion / Easing Token |
| `--motion-base` | `220ms` | Motion / Easing Token |
| `--motion-slow` | `300ms` | Motion / Easing Token |
| `--motion-ease` | `cubic-bezier(.22,.61,.36,1)` | Motion / Easing Token |
| `--mobile-gutter` | `16px` | Layout / Spatial Grid Token |
| `--mobile-radius` | `0px` | Elevation / Border Token |
| `--circulation-progress` | `0` | Design System Custom Token |
| `--garamond-tracking` | `0em` | Typography / Scale Token |
| `--garamond-heading-tracking` | `-0.025em` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `EB Garamond Local`.
- **Primary Body Stack**: `Garamond`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-weight: 400`).
- **Body Copy**: rule `p` (`font-size: 15px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: .72rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.2,.75,.25,1)`, `cubic-bezier(.2,.72,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.text-button`**: `transition: background .15s ease, color .15s ease, transform .15s ease` extracted from `sinedogma-com-tr` stylesheet.
- **Selector `.about-copy a`**: `transition: background-color 160ms ease, color 160ms ease, text-decoration...` extracted from `sinedogma-com-tr` stylesheet.
- **Selector `.carousel-next`**: `transition: var(--motion-base)` extracted from `sinedogma-com-tr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.61,.36,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.section>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.section>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — sinedogma                                  │
│ ====================================================================== │
│ [ <header.site-header>     | haberler · satış noktaları · hakkımızd ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: iki yayın tek dolaşım                                        |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #d9d9d9        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: var(--reading) |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | sinedogma dijital arşiv      |  | “bu ben değilim” yönetmenler | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px  ) | │
│ | [<header.site-heade] -> [<section.hero>] -> [<section.section>] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://sinedogma.com.tr/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `sinedogma-com-tr`)**:
   - Landmark `<header class="site-header">` hosting `sinedogma` navigation (`haberler · satış noktaları · hakkımızda`), DOM attributes (`data-path="/"`, `data-path="/haberler"`, `data-path="/satis-noktalari"`, `data-path="/hakkimizda"`), and stylesheet rule `root { --paper: fff; --ink: 111; --muted: 6f6f6f; --line: d9d9d9; --soft: f5f5f3; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `iki yayın tek dolaşım`)**:
   - Landmark `<section class="hero shell">` presenting display lead `iki yayın tek dolaşım` and copy excerpt *"yazı gönder / kitap dosyası gönder yazı / kitap gönder"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.section> — `sinedogma dijital arşiv`)**:
   - Landmark `<section class="section shell">` rendering section `sinedogma dijital arşiv` with copy *"yazı gönder / kitap dosyası gönder"*, asset references (`EBGaramond-VariableFont_wght.woff2`, `favicon-32x32.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `html { scroll-behavior: smooth; }`.
4. **Interactive Detail & Feature Matrix (<article.article-card> — `“bu ben değilim” yönetmenleri ile `)**:
   - Landmark `<article class="article-card">` framing `“bu ben değilim” yönetmenleri ile bir söyleşi` and `+1 belgesel: jim’le tanışmak "kısa incelemesi"` (*"yazı / kitap gönder"*) with `#6f6f6f` surface cards, `#d9d9d9` accents, and `input { font: inherit; text-transform: lowercase; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://sinedogma.com.tr/`)**:
   - Landmark `<footer class="site-footer">` anchoring `sinedogma` footer links (`haberler · satış noktaları · hakkımızda`), copy *"sinedogma · güz 2026 güz 2026 beş sayı antoloji koleksiyonu "*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: sinedogma-com-tr (sinedogma)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `sinedogma-com-tr` (**sinedogma** — `https://sinedogma.com.tr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#d9d9d9` accent).
- **Identity & Domain Context**: sinedogma ve dogma yayın: dijital arşiv, dergiler, kitaplar, haberler ve satış noktaları.
- **Primary Substrate**: `#fff` (`var(--paper)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#d9d9d9`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--paper)` in `:root`) paired with `#000` primary typography and `#d9d9d9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `EB Garamond Local` for display copy (`iki yayın tek dolaşım`) with `Garamond` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--reading)` container bounds (`gap: 24px`, padding `34px`) with `cubic-bezier(.22,.61,.36,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `sinedogma-com-tr` in your global stylesheet:

:root {
  /* sinedogma (sinedogma-com-tr) — Ground-Truth Extracted CSS Variables */
  --paper: #fff; /* Canvas / Surface Token (sinedogma-com-tr) */
  --ink: #111; /* Typography Ink Token (sinedogma-com-tr) */
  --muted: #6f6f6f; /* Color / Atmospheric Token (sinedogma-com-tr) */
  --line: #d9d9d9; /* Color / Atmospheric Token (sinedogma-com-tr) */
  --soft: #f5f5f3; /* Color / Atmospheric Token (sinedogma-com-tr) */
  --max: 1080px; /* Dimension / Scale Token (sinedogma-com-tr) */
  --reading: 680px; /* Dimension / Scale Token (sinedogma-com-tr) */
  --motion-fast: 160ms; /* Motion / Easing Token (sinedogma-com-tr) */
  --motion-base: 220ms; /* Motion / Easing Token (sinedogma-com-tr) */
  --motion-slow: 300ms; /* Motion / Easing Token (sinedogma-com-tr) */
  --motion-ease: cubic-bezier(.22,.61,.36,1); /* Motion / Easing Token (sinedogma-com-tr) */
  --mobile-gutter: 16px; /* Layout / Spatial Grid Token (sinedogma-com-tr) */
  --mobile-radius: 0px; /* Elevation / Border Token (sinedogma-com-tr) */
  --circulation-progress: 0; /* Design System Custom Token (sinedogma-com-tr) */
  --garamond-tracking: 0em; /* Typography / Scale Token (sinedogma-com-tr) */
  --garamond-heading-tracking: -0.025em; /* Typography Ink Token (sinedogma-com-tr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--paper)` in `:root`
- **Primary Typography Ink**: `#111` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#6f6f6f` — grounded in `var(--muted)` in `:root`
- **Interactive Accent / Highlight**: `#d9d9d9` — grounded in `var(--line)` in `:root`
- **Secondary / Muted Copy**: `#f5f5f3` — grounded in `var(--soft)` in `:root`
- **Structural Hairline Border**: `#000` — grounded in `var(--w2w-start-background-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6895px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--reading)` extracted from `sinedogma-com-tr` stylesheet
- **Padding & Gutters**: `34px` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--reading)`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `34px` horizontal padding
- **Media Queries**: `@media (max-width: 860px)`, `@media (max-width: 600px)`, `@media (max-width: 700px)`, `@media (max-width:600px)`
- **Corner Radii**: `50%`, `999px`, `7px`, `5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `EB Garamond Local`
- **Body Font Stack**: `Garamond`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-weight: 400`)
- **Body Copy Rule**: rule `p` (`font-size: 15px`)
- **Metadata & Index Rule**: rule `small` (`font-size: .72rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `sinedogma-com-tr` (`sinedogma`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `sinedogma-com-tr`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` hosting `sinedogma` navigation (`haberler · satış noktaları · hakkımızda`), DOM attributes (`data-path="/"`, `data-path="/haberler"`, `data-path="/satis-noktalari"`, `data-path="/hakkimizda"`), and stylesheet rule `root { --paper: fff; --ink: 111; --muted: 6f6f6f; --line: d9d9d9; --soft: f5f5f3; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `sinedogma-com-tr`)` (`sinedogma-com-tr`) adapts across `@media (max-width: 860px)`, `@media (max-width: 600px)`, `@media (max-width: 700px)`, `@media (max-width:600px)` with `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.2,.75,.25,1)`, `cubic-bezier(.2,.72,.2,1)` transitions and links `haberler · satış noktaları · hakkımızda`.
2. **Hero Stage & Focal Lead (<section.hero> — `iki yayın tek dolaşım`)**:
   - DOM & Selectors: Landmark `<section class="hero shell">` presenting display lead `iki yayın tek dolaşım` and copy excerpt *"yazı gönder / kitap dosyası gönder yazı / kitap gönder"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×6895px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `iki yayın tek dolaşım`.
3. **Primary Showcase & Content Grid (<section.section> — `sinedogma dijital arşiv`)**:
   - DOM & Selectors: Landmark `<section class="section shell">` rendering section `sinedogma dijital arşiv` with copy *"yazı gönder / kitap dosyası gönder"*, asset references (`EBGaramond-VariableFont_wght.woff2`, `favicon-32x32.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `html { scroll-behavior: smooth; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `sinedogma dijital arşiv`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--reading)`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `34px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.article-card> — `“bu ben değilim” yönetmenleri ile `)**:
   - DOM & Selectors: Landmark `<article class="article-card">` framing `“bu ben değilim” yönetmenleri ile bir söyleşi` and `+1 belgesel: jim’le tanışmak "kısa incelemesi"` (*"yazı / kitap gönder"*) with `#6f6f6f` surface cards, `#d9d9d9` accents, and `input { font: inherit; text-transform: lowercase; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.article-card> — `“bu ben değilim” yönetmenleri ile `)` uses `50%`, `999px`, `7px`, `5px` radii, `#d9d9d9` highlights, and assets (EBGaramond-VariableFont_wght.woff2, favicon-32x32.png, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://sinedogma.com.tr/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `sinedogma` footer links (`haberler · satış noktaları · hakkımızda`), copy *"sinedogma · güz 2026 güz 2026 beş sayı antoloji koleksiyonu "*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://sinedogma.com.tr/`)` aligns to `var(--reading)` extracted from `sinedogma-com-tr` stylesheet with `34px` lateral canvas padding with `24px` grid gap and attributes (data-path="/", data-path="/haberler", data-path="/satis-noktalari").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"yazı gönder / kitap dosyası gönder yazı / kitap gönder"*
- Copy Excerpt 2: *"yazı gönder / kitap dosyası gönder"*
- Copy Excerpt 3: *"yazı / kitap gönder"*
- Copy Excerpt 4: *"sinedogma · güz 2026 güz 2026 beş sayı antoloji koleksiyonu özel sayı incele ↗"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.2,.75,.25,1)`, `cubic-bezier(.2,.72,.2,1)`
- **Extracted Stylesheet Rules (`sinedogma-com-tr`)**:
- `root { --paper: fff; --ink: 111; --muted: 6f6f6f; --line: d9d9d9; --soft: f5f5f3; }`
- `html { scroll-behavior: smooth; }`
- `input { font: inherit; text-transform: lowercase; }`
- `.shell { width: min(calc(100% - 40px), var(--max)); margin-inline: auto; }`
- `.header-inner { display: flex; align-items: center; justify-content: space-between; }`
- **Per-Selector Transition Rules**:
- **Selector `.text-button`**: `transition: background .15s ease, color .15s ease, transform .15s ease` extracted from `sinedogma-com-tr` stylesheet.
- **Selector `.about-copy a`**: `transition: background-color 160ms ease, color 160ms ease, text-decoration...` extracted from `sinedogma-com-tr` stylesheet.
- **Selector `.carousel-next`**: `transition: var(--motion-base)` extracted from `sinedogma-com-tr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.61,.36,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.section>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.section>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `sinedogma-com-tr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
