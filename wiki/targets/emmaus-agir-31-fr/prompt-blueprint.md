---
title: "UI Prompt Blueprint: emmaus-agir-31-fr"
date: 2026-11-15
target: "[[overview|emmaus-agir-31-fr]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f1ece1` / `#5f5d57`)"
---

# UI Design System & Master Generation Blueprint: emmaus-agir-31-fr

> **Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour** (https://emmaus-agir-31.fr/) — Donnez une seconde vie à vos objets. Emmaüs A.G.I.R. collecte, trie et revend vos dons dans six boutiques solidaires à Toulouse et autour...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour** (`https://emmaus-agir-31.fr/`). Donnez une seconde vie à vos objets. Emmaüs A.G.I.R. collecte, trie et revend vos dons dans six boutiques solidaires à Toulouse et autour...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f1ece1` / `#5f5d57`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1ece1` (`var(--fond)` in `:root`) paired with `#1b1b1b` primary typography and `#5f5d57` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bricolage Grotesque` for display copy (`S e c o n d e v i e , s e c o n d e `) with `Bricolage Grotesque Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `38ch` container bounds (`gap: .7rem`, padding `var(--gutter)`) with `cubic-bezier(0.16,1,0.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `38ch` extracted from `emmaus-agir-31-fr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--gutter)` lateral canvas padding with `.7rem` grid gap.
- **Border Radius Scale**: `var(--radius-pill)`, `8px`, `50%`, `6px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 38ch`, `gap: .7rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--gutter)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:640px)`, `@media (max-width:1024px)`, `@media (max-width:1024px)and (orientation:portrait)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1ece1` | `var(--fond)` in `:root` |
| **Primary Typography Ink** | `#e7e1d3` | `var(--fond-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1b1b1b` | `var(--gris)` in `:root` |
| **Interactive Accent / Highlight** | `#5f5d57` | `var(--gris-doux)` in `:root` |
| **Secondary / Muted Copy** | `#ebc017` | `var(--jaune)` in `:root` |
| **Structural Hairline Border** | `#33669b` | `var(--bleu)` in `:root` |
| **Variable Token (`--vert`)** | `#43744e` | `var(--vert)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fond` | `#f1ece1` | Color / Atmospheric Token |
| `--fond-2` | `#e7e1d3` | Color / Atmospheric Token |
| `--gris` | `#1b1b1b` | Color / Atmospheric Token |
| `--gris-doux` | `#5f5d57` | Color / Atmospheric Token |
| `--ligne` | `rgba(27,27,27,0.18)` | Color / Atmospheric Token |
| `--jaune` | `#ebc017` | Color / Atmospheric Token |
| `--bleu` | `#33669b` | Color / Atmospheric Token |
| `--vert` | `#43744e` | Color / Atmospheric Token |
| `--ink` | `var(--gris)` | Typography Ink Token |
| `--header-h` | `clamp(56px,8vw,88px)` | Layout / Spatial Grid Token |
| `--radius-pill` | `999px` | Elevation / Border Token |
| `--tap` | `44px` | Dimension / Scale Token |
| `--z-flower` | `2` | Elevation / Border Token |
| `--z-guide` | `3` | Elevation / Border Token |
| `--z-scene` | `4` | Elevation / Border Token |
| `--z-scene-raised` | `5` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Bricolage Grotesque`.
- **Primary Body Stack**: `Bricolage Grotesque Fallback`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--fs-display: clamp(3.2rem,0.8rem + 7.2vw,11.5rem)`.
- **Section Heading (`H2`)**: CSS variables `--fs-h2: clamp(2.5rem,1.3rem + 4.6vw,6.5rem)`; rule `.h2` (`font-size: clamp(1.5rem,8dvh,2.6rem)`).
- **Body Copy**: CSS variables `--fs-body: clamp(1rem,0.95rem + 0.2vw,1.125rem)`; rule `p` (`font-size: var(--fs-lead)`, `line-height: 1.45`).
- **Metadata & Navigation Labels**: CSS variables `--fs-small: 0.9375rem`, `--fs-label: clamp(0.75rem,0.72rem + 0.12vw,0.8125rem)`; rule `.label` (`font-size: .6875rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.16,1,0.3,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(0.34,1.8,0.64,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: .01ms!important` extracted from `emmaus-agir-31-fr` stylesheet.
- **Selector `.btn`**: `transition: color .45s var(--ease-out)` extracted from `emmaus-agir-31-fr` stylesheet.
- **Selector `.btn:before`**: `transition: scale .6s var(--ease-out)` extracted from `emmaus-agir-31-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.16,1,0.3,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.activites>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Emmaüs A.G.I.R. — Boutiques solidaires à T │
│ ====================================================================== │
│ [ <header.header>          | 0 1 Accueil Accueil · 05 61 63 14 94 · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: S e c o n d e v i e , s e c o n d e c h a n c e .            |   │
│ | Substrate: #f1ece1    | Ink: #1b1b1b    | Accent: #5f5d57        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.activites>       ) max-w: 38ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Le parcours d’un don.        |  | Réception des dons           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .7rem ) | │
│ | [<header.header>] -> [<section.hero>] -> [<section.activites] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://emmaus-agir-31.fr/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `emmaus-agir-31-fr`)**:
   - Landmark `<header class="header">` hosting `Emmaüs A.G.I.R. — Boutiques solidair` navigation (`0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.__className_2a1a39 { font-family:Bricolage Grotesque,Bricolage Grotesque Fallback;font-style:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `S e c o n d e v i e , s e c o n d `)**:
   - Landmark `<section class="hero">` presenting display lead `S e c o n d e v i e , s e c o n d e c h a n c e .` and copy excerpt *"Chargement du site"* over `#f1ece1` canvas and `#1b1b1b` ink.
3. **Primary Showcase & Content Grid (<section.activites> — `Le parcours d’un don.`)**:
   - Landmark `<section class="activites">` rendering section `Le parcours d’un don.` with copy *"0 1 Accueil Accueil"*, asset references (`logo.svg`, `favicon.ico`, `favicon-32x32.png`, `apple-icon-180x180.png`), and grid rule `.__className_ae301a { font-family:"Instrument Serif","Instrument Serif Fallback";font-weight:400 }`.
4. **Interactive Detail & Feature Matrix (<article.activites__text> — `Réception des dons`)**:
   - Landmark `<article class="activites__text is-active">` framing `Réception des dons` and `Tri par catégorie` (*"0 2 Activités Activités"*) with `#1b1b1b` surface cards, `#5f5d57` accents, and `before { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://emmaus-agir-31.fr/`)**:
   - Landmark `<footer class="footer">` anchoring `Emmaüs A.G.I.R. — Boutiques soli` footer links (`0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`), copy *"Activités Activités"*, and `#33669b` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: emmaus-agir-31-fr (Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `emmaus-agir-31-fr` (**Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour** — `https://emmaus-agir-31.fr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f1ece1` / `#5f5d57`).
- **Identity & Domain Context**: Donnez une seconde vie à vos objets. Emmaüs A.G.I.R. collecte, trie et revend vos dons dans six boutiques solidaires à Toulouse et autour...
- **Primary Substrate**: `#f1ece1` (`var(--fond)` in `:root`), **Primary Ink**: `#1b1b1b`, **Accent / Highlight**: `#5f5d57`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1ece1` (`var(--fond)` in `:root`) paired with `#1b1b1b` primary typography and `#5f5d57` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bricolage Grotesque` for display copy (`S e c o n d e v i e , s e c o n d e `) with `Bricolage Grotesque Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `38ch` container bounds (`gap: .7rem`, padding `var(--gutter)`) with `cubic-bezier(0.16,1,0.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `emmaus-agir-31-fr` in your global stylesheet:

:root {
  /* Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour (emmaus-agir-31-fr) — Ground-Truth Extracted CSS Variables */
  --fond: #f1ece1; /* Color / Atmospheric Token (emmaus-agir-31-fr) */
  --fond-2: #e7e1d3; /* Color / Atmospheric Token (emmaus-agir-31-fr) */
  --gris: #1b1b1b; /* Color / Atmospheric Token (emmaus-agir-31-fr) */
  --gris-doux: #5f5d57; /* Color / Atmospheric Token (emmaus-agir-31-fr) */
  --ligne: rgba(27,27,27,0.18); /* Color / Atmospheric Token (emmaus-agir-31-fr) */
  --jaune: #ebc017; /* Color / Atmospheric Token (emmaus-agir-31-fr) */
  --bleu: #33669b; /* Color / Atmospheric Token (emmaus-agir-31-fr) */
  --vert: #43744e; /* Color / Atmospheric Token (emmaus-agir-31-fr) */
  --ink: var(--gris); /* Typography Ink Token (emmaus-agir-31-fr) */
  --header-h: clamp(56px,8vw,88px); /* Layout / Spatial Grid Token (emmaus-agir-31-fr) */
  --radius-pill: 999px; /* Elevation / Border Token (emmaus-agir-31-fr) */
  --tap: 44px; /* Dimension / Scale Token (emmaus-agir-31-fr) */
  --z-flower: 2; /* Elevation / Border Token (emmaus-agir-31-fr) */
  --z-guide: 3; /* Elevation / Border Token (emmaus-agir-31-fr) */
  --z-scene: 4; /* Elevation / Border Token (emmaus-agir-31-fr) */
  --z-scene-raised: 5; /* Elevation / Border Token (emmaus-agir-31-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f1ece1` — grounded in `var(--fond)` in `:root`
- **Primary Typography Ink**: `#e7e1d3` — grounded in `var(--fond-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#1b1b1b` — grounded in `var(--gris)` in `:root`
- **Interactive Accent / Highlight**: `#5f5d57` — grounded in `var(--gris-doux)` in `:root`
- **Secondary / Muted Copy**: `#ebc017` — grounded in `var(--jaune)` in `:root`
- **Structural Hairline Border**: `#33669b` — grounded in `var(--bleu)` in `:root`
- **Variable Token (`--vert`)**: `#43744e` — grounded in `var(--vert)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `38ch` extracted from `emmaus-agir-31-fr` stylesheet
- **Padding & Gutters**: `var(--gutter)` lateral canvas padding with `.7rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 38ch`, `gap: .7rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--gutter)` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:640px)`, `@media (max-width:1024px)`, `@media (max-width:1024px)and (orientation:portrait)`
- **Corner Radii**: `var(--radius-pill)`, `8px`, `50%`, `6px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Bricolage Grotesque`
- **Body Font Stack**: `Bricolage Grotesque Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--fs-display: clamp(3.2rem,0.8rem + 7.2vw,11.5rem)`
- **H2 Section Rule**: CSS variables `--fs-h2: clamp(2.5rem,1.3rem + 4.6vw,6.5rem)`; rule `.h2` (`font-size: clamp(1.5rem,8dvh,2.6rem)`)
- **Body Copy Rule**: CSS variables `--fs-body: clamp(1rem,0.95rem + 0.2vw,1.125rem)`; rule `p` (`font-size: var(--fs-lead)`, `line-height: 1.45`)
- **Metadata & Index Rule**: CSS variables `--fs-small: 0.9375rem`, `--fs-label: clamp(0.75rem,0.72rem + 0.12vw,0.8125rem)`; rule `.label` (`font-size: .6875rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `emmaus-agir-31-fr` (`Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `emmaus-agir-31-fr`)**:
   - DOM & Selectors: Landmark `<header class="header">` hosting `Emmaüs A.G.I.R. — Boutiques solidair` navigation (`0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.__className_2a1a39 { font-family:Bricolage Grotesque,Bricolage Grotesque Fallback;font-style:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `emmaus-agir-31-fr`)` (`emmaus-agir-31-fr`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:640px)`, `@media (max-width:1024px)`, `@media (max-width:1024px)and (orientation:portrait)` with `cubic-bezier(0.16,1,0.3,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(0.34,1.8,0.64,1)` transitions and links `0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`.
2. **Hero Stage & Focal Lead (<section.hero> — `S e c o n d e v i e , s e c o n d `)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `S e c o n d e v i e , s e c o n d e c h a n c e .` and copy excerpt *"Chargement du site"* over `#f1ece1` canvas and `#1b1b1b` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f1ece1` background with `#1b1b1b` headline `S e c o n d e v i e , s e c o n d e c h a n c e .`.
3. **Primary Showcase & Content Grid (<section.activites> — `Le parcours d’un don.`)**:
   - DOM & Selectors: Landmark `<section class="activites">` rendering section `Le parcours d’un don.` with copy *"0 1 Accueil Accueil"*, asset references (`logo.svg`, `favicon.ico`, `favicon-32x32.png`, `apple-icon-180x180.png`), and grid rule `.__className_ae301a { font-family:"Instrument Serif","Instrument Serif Fallback";font-weight:400 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.activites> — `Le parcours d’un don.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 38ch`, `gap: .7rem`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--gutter)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.activites__text> — `Réception des dons`)**:
   - DOM & Selectors: Landmark `<article class="activites__text is-active">` framing `Réception des dons` and `Tri par catégorie` (*"0 2 Activités Activités"*) with `#1b1b1b` surface cards, `#5f5d57` accents, and `before { box-sizing:border-box }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.activites__text> — `Réception des dons`)` uses `var(--radius-pill)`, `8px`, `50%`, `6px` radii, `#5f5d57` highlights, and assets (logo.svg, favicon.ico, favicon-32x32.png).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://emmaus-agir-31.fr/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Emmaüs A.G.I.R. — Boutiques soli` footer links (`0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`), copy *"Activités Activités"*, and `#33669b` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://emmaus-agir-31.fr/`)` aligns to `38ch` extracted from `emmaus-agir-31-fr` stylesheet with `var(--gutter)` lateral canvas padding with `.7rem` grid gap and attributes (data-next-head, data-next-font="size-adjust", data-next-font="size-adjust").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Chargement du site"*
- Copy Excerpt 2: *"0 1 Accueil Accueil"*
- Copy Excerpt 3: *"0 2 Activités Activités"*
- Copy Excerpt 4: *"Activités Activités"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.16,1,0.3,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(0.34,1.8,0.64,1)`
- **Extracted Stylesheet Rules (`emmaus-agir-31-fr`)**:
- `.__className_2a1a39 { font-family:Bricolage Grotesque,Bricolage Grotesque Fallback;font-style:... }`
- `.__className_ae301a { font-family:"Instrument Serif","Instrument Serif Fallback";font-weight:400 }`
- `before { box-sizing:border-box }`
- `html { text-size-adjust:100%;background:var(--fond);color:var(--ink) }`
- `html.lenis body { height:auto }`
- **Per-Selector Transition Rules**:
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: .01ms!important` extracted from `emmaus-agir-31-fr` stylesheet.
- **Selector `.btn`**: `transition: color .45s var(--ease-out)` extracted from `emmaus-agir-31-fr` stylesheet.
- **Selector `.btn:before`**: `transition: scale .6s var(--ease-out)` extracted from `emmaus-agir-31-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.16,1,0.3,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.activites>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `emmaus-agir-31-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
