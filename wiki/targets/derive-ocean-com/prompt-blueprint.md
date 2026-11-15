---
title: "UI Prompt Blueprint: derive-ocean-com"
date: 2026-11-15
target: "[[overview|derive-ocean-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f6eedf` / `#5a4531`)"
---

# UI Design System & Master Generation Blueprint: derive-ocean-com

> **Dérive — a contemplative game: a rowing boat on an endless ocean** (https://derive-ocean.com/) — Ramez sur un océan sans fin, observez baleines et bancs de poissons, remplissez le carnet d’une naturaliste. Un jeu contemplatif gratuit,...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/derive-ocean-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Dérive — a contemplative game: a rowing boat on an endless ocean** (`https://derive-ocean.com/`). Ramez sur un océan sans fin, observez baleines et bancs de poissons, remplissez le carnet d’une naturaliste. Un jeu contemplatif gratuit,...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f6eedf` / `#5a4531`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f6eedf` (`var(--sea-text)` in `:root`) paired with `#2a241d` primary typography and `#5a4531` accents.
  - **Extracted Typographic Hierarchy**: Pairs `EB Garamond` for display copy (`Dérive`) with `La Belle Aurore` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `560px` container bounds (`gap: 12px`, padding `10px`) with `cubic-bezier(.22,1,.36,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/derive-ocean-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `560px` extracted from `derive-ocean-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `12px`, `22px`, `6px`, `16px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:560px)`, `@media (min-width:561px)`, `@media (max-height:500px) and (orientation:landscape)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f6eedf` | `var(--sea-text)` in `:root` |
| **Primary Typography Ink** | `#f3eada` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d9c9aa` | `var(--paper-deep)` in `:root` |
| **Interactive Accent / Highlight** | `#5a4531` | `var(--binding)` in `:root` |
| **Secondary / Muted Copy** | `#2a241d` | `var(--ink)` in `:root` |
| **Structural Hairline Border** | `#3e3326` | `var(--ink-soft)` in `:root` |
| **Variable Token (`--sea-shadow`)** | `#06222899` | `var(--sea-shadow)` in `:root` |
| **Variable Token (`--sea-button`)** | `#08262a29` | `var(--sea-button)` in `:root` |
| **Variable Token (`--sea-line`)** | `#f6eedf52` | `var(--sea-line)` in `:root` |
| **Variable Token (`--sea-dim`)** | `#0412148c` | `var(--sea-dim)` in `:root` |
| **Variable Token (`--paper-gutter`)** | `#5e482a2e` | `var(--paper-gutter)` in `:root` |
| **Variable Token (`--ink-muted`)** | `#5e4e3b` | `var(--ink-muted)` in `:root` |
| **Variable Token (`--ink-faint`)** | `#7a6a55` | `var(--ink-faint)` in `:root` |
| **Variable Token (`--rule`)** | `#5e4e3b4d` | `var(--rule)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-text` | `"EB Garamond", "Iowan Old Style", Georgia, serif` | Typography Ink Token |
| `--font-hand` | `"La Belle Aurore", "Snell Roundhand", cursive` | Typography / Scale Token |
| `--sea-text` | `#f6eedf` | Typography Ink Token |
| `--sea-shadow` | `0 1px 8px #06222899` | Elevation / Border Token |
| `--sea-button` | `#08262a29` | Color / Atmospheric Token |
| `--sea-line` | `#f6eedf52` | Color / Atmospheric Token |
| `--sea-dim` | `#0412148c` | Color / Atmospheric Token |
| `--paper` | `#f3eada` | Canvas / Surface Token |
| `--paper-deep` | `#d9c9aa` | Canvas / Surface Token |
| `--paper-gutter` | `#5e482a2e` | Canvas / Surface Token |
| `--binding` | `#5a4531` | Color / Atmospheric Token |
| `--ink` | `#2a241d` | Typography Ink Token |
| `--ink-soft` | `#3e3326` | Typography Ink Token |
| `--ink-muted` | `#5e4e3b` | Typography Ink Token |
| `--ink-faint` | `#7a6a55` | Typography Ink Token |
| `--rule` | `#5e4e3b4d` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `EB Garamond`.
- **Primary Body Stack**: `La Belle Aurore`.
- **Technical / Metadata Stack**: `SF Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 136px`, `line-height: .95`, `letter-spacing: -.01em`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 34px`, `font-weight: 400`).
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.45`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `18px`, `15px`, `16px`, `20px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.5,0,.9,.4)`, `cubic-bezier(.34,1.56,.64,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.plate-name`**: `transition: opacity .25s` extracted from `derive-ocean-com` stylesheet.
- **Selector `.bubble`**: `transition: opacity .3s,transform .3s` extracted from `derive-ocean-com` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `derive-ocean-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.intro-menu>` and `<div.hud-camera>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Dérive — a contemplative game: a rowing bo │
│ ====================================================================== │
│ [ <nav.intro-menu>         | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.hud-settings>                                   |   │
│ | H1: Dérive                                                       |   │
│ | Substrate: #f6eedf    | Ink: #2a241d    | Accent: #5a4531        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.hud-camera>          ) max-w: 560px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | A rowing boat, an endless oc |  | Sign in to find your game    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<nav.intro-menu>] -> [<div.hud-settings>] -> [<div.hud-camera>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.tools>        ) | https://derive-ocean.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.intro-menu> — `derive-ocean-com`)**:
   - Landmark `<nav class="intro-menu">` hosting `Dérive — a contemplative game: a row` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-carte="d"`, `data-carte-v="Xyo-u2Gt"`, `data-paper="162430"`, `data-teach="photo"`), and stylesheet rule `html { scroll-padding-top:env(safe-area-inset-top,0px) }`.
2. **Hero Stage & Focal Lead (<div.hud-settings> — `Dérive`)**:
   - Landmark `<div class="hud-settings">` presenting display lead `Dérive` and copy excerpt *"A rowing boat, an endless ocean, and what swims beneath."* over `#f6eedf` canvas and `#2a241d` ink.
3. **Primary Showcase & Content Grid (<div.hud-camera> — `A rowing boat, an endless ocean, a`)**:
   - Landmark `<div class="hud-camera">` rendering section `A rowing boat, an endless ocean, and what swims ` with copy *"Sign in to find your game"*, asset references (`favicon-32.png`, `favicon-48.png`, `apple-touch-icon.png`, `en-BwLAseLg.js`), and grid rule `body { background:var(--deep);overscroll-behavior:none;height:100%;margin:0;ove... }`.
4. **Interactive Detail & Feature Matrix (<div.hud-carnet> — `Sign in to find your game`)**:
   - Landmark `<div class="hud-carnet">` framing `Sign in to find your game` and `Touch and hold the sea, or the arrows or WASD, t` (*"Touch and hold the sea, or the arrows or WASD, to row About The m"*) with `#d9c9aa` surface cards, `#5a4531` accents, and `root { height:100% }`.
5. **Colophon & Global Directory Footer (<footer.tools> — `https://derive-ocean.com/`)**:
   - Landmark `<footer class="tools">` anchoring `Dérive — a contemplative game: a` footer links (`Overview · Index · Archive · About · Contact`), copy *"Touch and hold the sea, or the arrows or WASD, to row"*, and `#3e3326` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: derive-ocean-com (Dérive — a contemplative game: a rowing boat on an endless ocean)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `derive-ocean-com` (**Dérive — a contemplative game: a rowing boat on an endless ocean** — `https://derive-ocean.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f6eedf` / `#5a4531`).
- **Identity & Domain Context**: Ramez sur un océan sans fin, observez baleines et bancs de poissons, remplissez le carnet d’une naturaliste. Un jeu contemplatif gratuit,...
- **Primary Substrate**: `#f6eedf` (`var(--sea-text)` in `:root`), **Primary Ink**: `#2a241d`, **Accent / Highlight**: `#5a4531`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f6eedf` (`var(--sea-text)` in `:root`) paired with `#2a241d` primary typography and `#5a4531` accents.
  - **Extracted Typographic Hierarchy**: Pairs `EB Garamond` for display copy (`Dérive`) with `La Belle Aurore` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `560px` container bounds (`gap: 12px`, padding `10px`) with `cubic-bezier(.22,1,.36,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `derive-ocean-com` in your global stylesheet:

:root {
  /* Dérive — a contemplative game: a rowing boat on an endless ocean (derive-ocean-com) — Ground-Truth Extracted CSS Variables */
  --font-text: "EB Garamond", "Iowan Old Style", Georgia, serif; /* Typography Ink Token (derive-ocean-com) */
  --font-hand: "La Belle Aurore", "Snell Roundhand", cursive; /* Typography / Scale Token (derive-ocean-com) */
  --sea-text: #f6eedf; /* Typography Ink Token (derive-ocean-com) */
  --sea-shadow: 0 1px 8px #06222899; /* Elevation / Border Token (derive-ocean-com) */
  --sea-button: #08262a29; /* Color / Atmospheric Token (derive-ocean-com) */
  --sea-line: #f6eedf52; /* Color / Atmospheric Token (derive-ocean-com) */
  --sea-dim: #0412148c; /* Color / Atmospheric Token (derive-ocean-com) */
  --paper: #f3eada; /* Canvas / Surface Token (derive-ocean-com) */
  --paper-deep: #d9c9aa; /* Canvas / Surface Token (derive-ocean-com) */
  --paper-gutter: #5e482a2e; /* Canvas / Surface Token (derive-ocean-com) */
  --binding: #5a4531; /* Color / Atmospheric Token (derive-ocean-com) */
  --ink: #2a241d; /* Typography Ink Token (derive-ocean-com) */
  --ink-soft: #3e3326; /* Typography Ink Token (derive-ocean-com) */
  --ink-muted: #5e4e3b; /* Typography Ink Token (derive-ocean-com) */
  --ink-faint: #7a6a55; /* Typography Ink Token (derive-ocean-com) */
  --rule: #5e4e3b4d; /* Color / Atmospheric Token (derive-ocean-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f6eedf` — grounded in `var(--sea-text)` in `:root`
- **Primary Typography Ink**: `#f3eada` — grounded in `var(--paper)` in `:root`
- **Elevated Surface / Card Substrate**: `#d9c9aa` — grounded in `var(--paper-deep)` in `:root`
- **Interactive Accent / Highlight**: `#5a4531` — grounded in `var(--binding)` in `:root`
- **Secondary / Muted Copy**: `#2a241d` — grounded in `var(--ink)` in `:root`
- **Structural Hairline Border**: `#3e3326` — grounded in `var(--ink-soft)` in `:root`
- **Variable Token (`--sea-shadow`)**: `#06222899` — grounded in `var(--sea-shadow)` in `:root`
- **Variable Token (`--sea-button`)**: `#08262a29` — grounded in `var(--sea-button)` in `:root`
- **Variable Token (`--sea-line`)**: `#f6eedf52` — grounded in `var(--sea-line)` in `:root`
- **Variable Token (`--sea-dim`)**: `#0412148c` — grounded in `var(--sea-dim)` in `:root`
- **Variable Token (`--paper-gutter`)**: `#5e482a2e` — grounded in `var(--paper-gutter)` in `:root`
- **Variable Token (`--ink-muted`)**: `#5e4e3b` — grounded in `var(--ink-muted)` in `:root`
- **Variable Token (`--ink-faint`)**: `#7a6a55` — grounded in `var(--ink-faint)` in `:root`
- **Variable Token (`--rule`)**: `#5e4e3b4d` — grounded in `var(--rule)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `560px` extracted from `derive-ocean-com` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:560px)`, `@media (min-width:561px)`, `@media (max-height:500px) and (orientation:landscape)`
- **Corner Radii**: `12px`, `22px`, `6px`, `16px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `EB Garamond`
- **Body Font Stack**: `La Belle Aurore`
- **Monospace / Technical Font Stack**: `SF Mono`
- **H1 Display Rule**: rule `h1` (`font-size: 136px`, `line-height: .95`, `letter-spacing: -.01em`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: 34px`, `font-weight: 400`)
- **Body Copy Rule**: rule `p` (`font-size: 16px`, `line-height: 1.45`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `18px`, `15px`, `16px`, `20px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `derive-ocean-com` (`Dérive — a contemplative game: a rowing boat on an endless ocean`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.intro-menu> — `derive-ocean-com`)**:
   - DOM & Selectors: Landmark `<nav class="intro-menu">` hosting `Dérive — a contemplative game: a row` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-carte="d"`, `data-carte-v="Xyo-u2Gt"`, `data-paper="162430"`, `data-teach="photo"`), and stylesheet rule `html { scroll-padding-top:env(safe-area-inset-top,0px) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.intro-menu> — `derive-ocean-com`)` (`derive-ocean-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:560px)`, `@media (min-width:561px)`, `@media (max-height:500px) and (orientation:landscape)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.5,0,.9,.4)`, `cubic-bezier(.34,1.56,.64,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<div.hud-settings> — `Dérive`)**:
   - DOM & Selectors: Landmark `<div class="hud-settings">` presenting display lead `Dérive` and copy excerpt *"A rowing boat, an endless ocean, and what swims beneath."* over `#f6eedf` canvas and `#2a241d` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f6eedf` background with `#2a241d` headline `Dérive`.
3. **Primary Showcase & Content Grid (<div.hud-camera> — `A rowing boat, an endless ocean, a`)**:
   - DOM & Selectors: Landmark `<div class="hud-camera">` rendering section `A rowing boat, an endless ocean, and what swims ` with copy *"Sign in to find your game"*, asset references (`favicon-32.png`, `favicon-48.png`, `apple-touch-icon.png`, `en-BwLAseLg.js`), and grid rule `body { background:var(--deep);overscroll-behavior:none;height:100%;margin:0;ove... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.hud-camera> — `A rowing boat, an endless ocean, a`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.hud-carnet> — `Sign in to find your game`)**:
   - DOM & Selectors: Landmark `<div class="hud-carnet">` framing `Sign in to find your game` and `Touch and hold the sea, or the arrows or WASD, t` (*"Touch and hold the sea, or the arrows or WASD, to row About The m"*) with `#d9c9aa` surface cards, `#5a4531` accents, and `root { height:100% }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.hud-carnet> — `Sign in to find your game`)` uses `12px`, `22px`, `6px`, `16px` radii, `#5a4531` highlights, and assets (favicon-32.png, favicon-48.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.tools> — `https://derive-ocean.com/`)**:
   - DOM & Selectors: Landmark `<footer class="tools">` anchoring `Dérive — a contemplative game: a` footer links (`Overview · Index · Archive · About · Contact`), copy *"Touch and hold the sea, or the arrows or WASD, to row"*, and `#3e3326` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.tools> — `https://derive-ocean.com/`)` aligns to `560px` extracted from `derive-ocean-com` stylesheet with `10px` lateral canvas padding with `12px` grid gap and attributes (data-carte="d", data-carte-v="Xyo-u2Gt", data-paper="162430").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A rowing boat, an endless ocean, and what swims beneath."*
- Copy Excerpt 2: *"Sign in to find your game"*
- Copy Excerpt 3: *"Touch and hold the sea, or the arrows or WASD, to row About The making of Legal no..."*
- Copy Excerpt 4: *"Touch and hold the sea, or the arrows or WASD, to row"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.5,0,.9,.4)`, `cubic-bezier(.34,1.56,.64,1)`
- **Extracted Stylesheet Rules (`derive-ocean-com`)**:
- `html { scroll-padding-top:env(safe-area-inset-top,0px) }`
- `body { background:var(--deep);overscroll-behavior:none;height:100%;margin:0;ove... }`
- `root { height:100% }`
- `canvas { touch-action:none;cursor:crosshair;width:100%;height:100%;display:block;... }`
- `button:focus-visible { outline:2px solid var(--tide);outline-offset:2px }`
- **Per-Selector Transition Rules**:
- **Selector `.plate-name`**: `transition: opacity .25s` extracted from `derive-ocean-com` stylesheet.
- **Selector `.bubble`**: `transition: opacity .3s,transform .3s` extracted from `derive-ocean-com` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `derive-ocean-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.intro-menu>` and `<div.hud-camera>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `derive-ocean-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
