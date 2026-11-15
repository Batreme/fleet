---
title: "UI Prompt Blueprint: tigris-lorolabs-ai"
date: 2026-11-15
target: "[[overview|tigris-lorolabs-ai]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#4a0e1a` / `#c9a24a`)"
---

# UI Design System & Master Generation Blueprint: tigris-lorolabs-ai

> **TIGRIS · Instinct, in Its Rarest Form** (https://tigris.lorolabs.ai/) — Maison Tigris. Sculptural high jewellery in gold, rubies and diamonds. Discover the collection and explore a private viewing.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/tigris-lorolabs-ai/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **TIGRIS · Instinct, in Its Rarest Form** (`https://tigris.lorolabs.ai/`). Maison Tigris. Sculptural high jewellery in gold, rubies and diamonds. Discover the collection and explore a private viewing.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#4a0e1a` / `#c9a24a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#4a0e1a` (`var(--burgundy)` in `:root`) paired with `#f2d38a` primary typography and `#c9a24a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bodoni Moda` for display copy (`TIGRIS`) with `Space Grotesk` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `20ch` container bounds (`gap: 2.5rem`, padding `2rem`) with `cubic-bezier(.65,0,.35,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/tigris-lorolabs-ai/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `20ch` extracted from `tigris-lorolabs-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `2.5rem` grid gap.
- **Border Radius Scale**: `50%`, `2px`, `2rem`, `16px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 20ch`, `gap: 2.5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:768px)`, `@media (max-width:600px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4a0e1a` | `var(--burgundy)` in `:root` |
| **Primary Typography Ink** | `#24060e` | `var(--oxblood)` in `:root` |
| **Elevated Surface / Card Substrate** | `#120309` | `var(--void)` in `:root` |
| **Interactive Accent / Highlight** | `#c9a24a` | `var(--gold)` in `:root` |
| **Secondary / Muted Copy** | `#f2d38a` | `var(--gold-hi)` in `:root` |
| **Structural Hairline Border** | `#9b1b30` | `var(--ruby)` in `:root` |
| **Variable Token (`--cream`)** | `#f5e9d6` | `var(--cream)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--burgundy` | `#4a0e1a` | Color / Atmospheric Token |
| `--oxblood` | `#24060e` | Color / Atmospheric Token |
| `--void` | `#120309` | Color / Atmospheric Token |
| `--gold` | `#c9a24a` | Color / Atmospheric Token |
| `--gold-hi` | `#f2d38a` | Color / Atmospheric Token |
| `--ruby` | `#9b1b30` | Color / Atmospheric Token |
| `--cream` | `#f5e9d6` | Color / Atmospheric Token |
| `--serif` | `"Bodoni Moda", "Didot", serif` | Typography / Scale Token |
| `--grot` | `"Space Grotesk", system-ui, sans-serif` | Dimension / Scale Token |
| `--tigris-lorolabs--bg` | `#4a0e1a` | Canvas Substrate (from `var(--burgundy)` in `:root`) |
| `--tigris-lorolabs--ink` | `#f2d38a` | Primary Typography Ink (stylesheet-derived) |
| `--tigris-lorolabs--surface` | `#120309` | Surface Substrate (stylesheet-derived) |
| `--tigris-lorolabs--accent` | `#c9a24a` | Interactive Accent (stylesheet-derived) |
| `--tigris-lorolabs--muted` | `#f2d38a` | Secondary Ink (stylesheet-derived) |
| `--tigris-lorolabs--border` | `#9b1b30` | Structural Border (stylesheet-derived) |
| `--tigris-lorolabs--container` | `20ch` | Container Bound (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Bodoni Moda`.
- **Primary Body Stack**: `Space Grotesk`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(.9rem,1.4vw,1.2rem)`, `1rem`, `.72rem`, `.7rem`, `clamp(2.6rem,7vw,6rem)`).
- **Section Heading (`H2`)**: rule `.section-title` (`font-size: clamp(2.6rem,7svh,5rem)`).
- **Body Copy**: rule `p` (`font-size: .75rem`, `letter-spacing: .22em`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(.9rem,1.4vw,1.2rem)`, `1rem`, `.72rem`, `.7rem`, `clamp(2.6rem,7vw,6rem)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.nav__links a:after`**: `transition: transform .45s cubic-bezier(.65,0,.35,1)` extracted from `tigris-lorolabs-ai` stylesheet.
- **Selector `.variants__btn`**: `transition: background .4s ease,color .4s ease,border-color .4s ease` extracted from `tigris-lorolabs-ai` stylesheet.
- **Selector `.card`**: `transition: opacity .5s ease` extracted from `tigris-lorolabs-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.35,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.manifesto>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — TIGRIS · Instinct, in Its Rarest Form      │
│ ====================================================================== │
│ [ <header.nav>             | Collection · Heritage · Acquire        ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: TIGRIS                                                       |   │
│ | Substrate: #4a0e1a    | Ink: #f2d38a    | Accent: #c9a24a        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.manifesto>       ) max-w: 20ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The Stripes                  |  | Stripe                       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2.5rem) | │
│ | [<header.nav>] -> [<section.hero>] -> [<section.manifesto] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://tigris.lorolabs.ai/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `tigris-lorolabs-ai`)**:
   - Landmark `<header class="nav">` hosting `TIGRIS · Instinct, in Its Rarest For` navigation (`Collection · Heritage · Acquire`), DOM attributes (`data-hover`, `data-variant="gold"`, `data-variant="enamel"`, `data-variant="pave"`), and stylesheet rule `html { scrollbar-width:thin;scrollbar-color:var(--gold) var(--void);background:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `TIGRIS`)**:
   - Landmark `<section class="hero">` presenting display lead `TIGRIS` and copy excerpt *"Skip to the collection"* over `#4a0e1a` canvas and `#f2d38a` ink.
3. **Primary Showcase & Content Grid (<section.manifesto> — `The Stripes`)**:
   - Landmark `<section class="manifesto">` rendering section `The Stripes` with copy *"TIGRIS · Please enable JavaScript to enter the collection."*, asset references (`manifest.webmanifest`, `icon-192.png`, `bodoni-moda-latin-normal.woff2`, `space-grotesk-latin-normal.woff2`), and grid rule `html.lenis body { height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.stripes> — `Stripe`)**:
   - Landmark `<section class="stripes">` framing `Stripe` and `Stripe II` (*"Instinct, in its rarest form."*) with `#120309` surface cards, `#c9a24a` accents, and `.lenis.lenis-smooth { scroll-behavior:auto!important }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tigris.lorolabs.ai/`)**:
   - Landmark `<footer class="footer">` anchoring `TIGRIS · Instinct, in Its Rarest` footer links (`Collection · Heritage · Acquire`), copy *"Scroll to discover"*, and `#9b1b30` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tigris-lorolabs-ai (TIGRIS · Instinct, in Its Rarest Form)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tigris-lorolabs-ai` (**TIGRIS · Instinct, in Its Rarest Form** — `https://tigris.lorolabs.ai/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#4a0e1a` / `#c9a24a`).
- **Identity & Domain Context**: Maison Tigris. Sculptural high jewellery in gold, rubies and diamonds. Discover the collection and explore a private viewing.
- **Primary Substrate**: `#4a0e1a` (`var(--burgundy)` in `:root`), **Primary Ink**: `#f2d38a`, **Accent / Highlight**: `#c9a24a`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#4a0e1a` (`var(--burgundy)` in `:root`) paired with `#f2d38a` primary typography and `#c9a24a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bodoni Moda` for display copy (`TIGRIS`) with `Space Grotesk` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `20ch` container bounds (`gap: 2.5rem`, padding `2rem`) with `cubic-bezier(.65,0,.35,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tigris-lorolabs-ai` in your global stylesheet:

:root {
  /* TIGRIS · Instinct, in Its Rarest Form (tigris-lorolabs-ai) — Ground-Truth Extracted CSS Variables */
  --burgundy: #4a0e1a; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --oxblood: #24060e; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --void: #120309; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --gold: #c9a24a; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --gold-hi: #f2d38a; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --ruby: #9b1b30; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --cream: #f5e9d6; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --serif: "Bodoni Moda", "Didot", serif; /* Typography / Scale Token (tigris-lorolabs-ai) */
  --grot: "Space Grotesk", system-ui, sans-serif; /* Dimension / Scale Token (tigris-lorolabs-ai) */
  --tigris-lorolabs--bg: #4a0e1a; /* Canvas Substrate (from `var(--burgundy)` in `:root`) (tigris-lorolabs-ai) */
  --tigris-lorolabs--ink: #f2d38a; /* Primary Typography Ink (stylesheet-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--surface: #120309; /* Surface Substrate (stylesheet-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--accent: #c9a24a; /* Interactive Accent (stylesheet-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--muted: #f2d38a; /* Secondary Ink (stylesheet-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--border: #9b1b30; /* Structural Border (stylesheet-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--container: 20ch; /* Container Bound (stylesheet-derived) (tigris-lorolabs-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#4a0e1a` — grounded in `var(--burgundy)` in `:root`
- **Primary Typography Ink**: `#24060e` — grounded in `var(--oxblood)` in `:root`
- **Elevated Surface / Card Substrate**: `#120309` — grounded in `var(--void)` in `:root`
- **Interactive Accent / Highlight**: `#c9a24a` — grounded in `var(--gold)` in `:root`
- **Secondary / Muted Copy**: `#f2d38a` — grounded in `var(--gold-hi)` in `:root`
- **Structural Hairline Border**: `#9b1b30` — grounded in `var(--ruby)` in `:root`
- **Variable Token (`--cream`)**: `#f5e9d6` — grounded in `var(--cream)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `20ch` extracted from `tigris-lorolabs-ai` stylesheet
- **Padding & Gutters**: `2rem` lateral canvas padding with `2.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 20ch`, `gap: 2.5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (max-width:768px)`, `@media (max-width:600px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:767px)`
- **Corner Radii**: `50%`, `2px`, `2rem`, `16px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Bodoni Moda`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(.9rem,1.4vw,1.2rem)`, `1rem`, `.72rem`, `.7rem`, `clamp(2.6rem,7vw,6rem)`)
- **H2 Section Rule**: rule `.section-title` (`font-size: clamp(2.6rem,7svh,5rem)`)
- **Body Copy Rule**: rule `p` (`font-size: .75rem`, `letter-spacing: .22em`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(.9rem,1.4vw,1.2rem)`, `1rem`, `.72rem`, `.7rem`, `clamp(2.6rem,7vw,6rem)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tigris-lorolabs-ai` (`TIGRIS · Instinct, in Its Rarest Form`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `tigris-lorolabs-ai`)**:
   - DOM & Selectors: Landmark `<header class="nav">` hosting `TIGRIS · Instinct, in Its Rarest For` navigation (`Collection · Heritage · Acquire`), DOM attributes (`data-hover`, `data-variant="gold"`, `data-variant="enamel"`, `data-variant="pave"`), and stylesheet rule `html { scrollbar-width:thin;scrollbar-color:var(--gold) var(--void);background:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `tigris-lorolabs-ai`)` (`tigris-lorolabs-ai`) adapts across `@media (max-width:768px)`, `@media (max-width:600px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:767px)` with `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Collection · Heritage · Acquire`.
2. **Hero Stage & Focal Lead (<section.hero> — `TIGRIS`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `TIGRIS` and copy excerpt *"Skip to the collection"* over `#4a0e1a` canvas and `#f2d38a` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#4a0e1a` background with `#f2d38a` headline `TIGRIS`.
3. **Primary Showcase & Content Grid (<section.manifesto> — `The Stripes`)**:
   - DOM & Selectors: Landmark `<section class="manifesto">` rendering section `The Stripes` with copy *"TIGRIS · Please enable JavaScript to enter the collection."*, asset references (`manifest.webmanifest`, `icon-192.png`, `bodoni-moda-latin-normal.woff2`, `space-grotesk-latin-normal.woff2`), and grid rule `html.lenis body { height:auto }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.manifesto> — `The Stripes`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 20ch`, `gap: 2.5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.stripes> — `Stripe`)**:
   - DOM & Selectors: Landmark `<section class="stripes">` framing `Stripe` and `Stripe II` (*"Instinct, in its rarest form."*) with `#120309` surface cards, `#c9a24a` accents, and `.lenis.lenis-smooth { scroll-behavior:auto!important }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.stripes> — `Stripe`)` uses `50%`, `2px`, `2rem`, `16px` radii, `#c9a24a` highlights, and assets (manifest.webmanifest, icon-192.png, bodoni-moda-latin-normal.woff2).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tigris.lorolabs.ai/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `TIGRIS · Instinct, in Its Rarest` footer links (`Collection · Heritage · Acquire`), copy *"Scroll to discover"*, and `#9b1b30` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://tigris.lorolabs.ai/`)` aligns to `20ch` extracted from `tigris-lorolabs-ai` stylesheet with `2rem` lateral canvas padding with `2.5rem` grid gap and attributes (data-hover, data-variant="gold", data-variant="enamel").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to the collection"*
- Copy Excerpt 2: *"TIGRIS · Please enable JavaScript to enter the collection."*
- Copy Excerpt 3: *"Instinct, in its rarest form."*
- Copy Excerpt 4: *"Scroll to discover"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`tigris-lorolabs-ai`)**:
- `html { scrollbar-width:thin;scrollbar-color:var(--gold) var(--void);background:... }`
- `html.lenis body { height:auto }`
- `.lenis.lenis-smooth { scroll-behavior:auto!important }`
- `body { background:var(--void);color:var(--cream);font-family:var(--grot);font-w... }`
- `selection { background:var(--gold);color:var(--oxblood) }`
- **Per-Selector Transition Rules**:
- **Selector `.nav__links a:after`**: `transition: transform .45s cubic-bezier(.65,0,.35,1)` extracted from `tigris-lorolabs-ai` stylesheet.
- **Selector `.variants__btn`**: `transition: background .4s ease,color .4s ease,border-color .4s ease` extracted from `tigris-lorolabs-ai` stylesheet.
- **Selector `.card`**: `transition: opacity .5s ease` extracted from `tigris-lorolabs-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.35,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.manifesto>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tigris-lorolabs-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
