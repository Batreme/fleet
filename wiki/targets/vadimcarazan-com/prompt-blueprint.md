---
title: "UI Prompt Blueprint: vadimcarazan-com"
date: 2026-11-15
target: "[[overview|vadimcarazan-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0b` / `#000`)"
---

# UI Design System & Master Generation Blueprint: vadimcarazan-com

> **Vadim Carazan, Creative Director** (https://vadimcarazan.com/) — Vadim Carazan, creative director and founder of WeGrow. Fourteen years of brand identities, websites and products for founders.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/vadimcarazan-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Vadim Carazan, Creative Director** (`https://vadimcarazan.com/`). Vadim Carazan, creative director and founder of WeGrow. Fourteen years of brand identities, websites and products for founders.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0b` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0a0a0b` (`var(--bg)` in `:root`) paired with `#fff` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Serif` for display copy (`Let's make the next one yours.`) with `Inter Tight` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `440px` container bounds (`gap: 24px`, padding `6px`) with `cubic-bezier(0.22,1,0.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/vadimcarazan-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `440px` extracted from `vadimcarazan-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `999px`, `50%`, `22px`, `12px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 860px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width:600px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0b` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#f2f2f2` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `.start:hover { border-color: #fff }` |
| **Interactive Accent / Highlight** | `#000` | `.start:hover i { color: #000 }` |
| **Secondary / Muted Copy** | `#ff9b92` | `.c-err { color: #ff9b92 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0a0a0b` | Canvas / Surface Token |
| `--ink` | `#f2f2f2` | Typography Ink Token |
| `--mute` | `rgba(242, 242, 242, 0.55)` | Color / Atmospheric Token |
| `--line` | `rgba(255, 255, 255, 0.12)` | Color / Atmospheric Token |
| `--serif` | `"Editorial Old Italic", "Instrument Serif", "Times New Roman", serif` | Typography / Scale Token |
| `--sans` | `"Inter Tight", "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--pad` | `clamp(16px, 2vw, 32px)` | Layout / Spatial Grid Token |
| `--box-open` | `clamp(460px, 42vw, 780px)` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--bp` | `28px` | Dimension / Scale Token |
| `--hx` | `748.8px` | Dimension / Scale Token |
| `--hy` | `196.0px` | Dimension / Scale Token |
| `--hrx` | `203.9px` | Dimension / Scale Token |
| `--hry` | `272.8px` | Dimension / Scale Token |
| `--vadimcarazan-com-bg` | `#0a0a0b` | Canvas Substrate (from `var(--bg)` in `:root`) |
| `--vadimcarazan-com-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument Serif`.
- **Primary Body Stack**: `Inter Tight`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16.5px`, `14px`, `15vw`, `clamp(56px, 6vw, 96px)`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(32px, 3vw, 46px)`, `line-height: 1.02`, `letter-spacing: -0.01em`, `font-weight: 400`).
- **Body Copy**: rule `.body` (`font-size: 15px`, `line-height: 1.6`).
- **Metadata & Navigation Labels**: rule `.label` (`font-size: 12px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.col-nav a`**: `transition: background-size 0.35s var(--ease)` extracted from `vadimcarazan-com` stylesheet.
- **Selector `.hero`**: `transition: opacity 0.6s ease, transform 0.9s var(--ease)` extracted from `vadimcarazan-com` stylesheet.
- **Selector `.start`**: `transition: border-color 0.3s ease, background 0.3s ease` extracted from `vadimcarazan-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.view>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Vadim Carazan, Creative Director           │
│ ====================================================================== │
│ [ <header.topbar>          | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Let's make the next one yours.                               |   │
│ | Substrate: #0a0a0b    | Ink: #fff       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.view>            ) max-w: 440px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | A few to start with.         |  | I make brands for founders w | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px  ) | │
│ | [<header.topbar>] -> [<section.hero>] -> [<section.view>] |          │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.logo>         ) | https://vadimcarazan.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.topbar> — `vadimcarazan-com`)**:
   - Landmark `<header class="topbar">` hosting `Vadim Carazan, Creative Director` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r169"`, `data-go="about"`, `data-go="about"`, `data-go="selected"`), and stylesheet rule `c.hot { cursor: pointer; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Let's make the next one yours.`)**:
   - Landmark `<section class="hero">` presenting display lead `Let's make the next one yours.` and copy excerpt *"Creative Director, WeGrow"* over `#0a0a0b` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.view> — `A few to start with.`)**:
   - Landmark `<section class="view v-project">` rendering section `A few to start with.` with copy *"Cluj-Napoca, Romania ( 13:10 )"*, asset references (`track.js`, `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `button { font: inherit; color: inherit; background: none; border: 0; padding: 0;... }`.
4. **Interactive Detail & Feature Matrix (<section.view> — `I make brands for founders who are`)**:
   - Landmark `<section class="view v-selected">` framing `I make brands for founders who are building somet...` and `Tell me what you're building.` (*"Selected , Work , About , Contact"*) with `#fff` surface cards, `#000` accents, and `.logo { width: 48px; height: auto; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.logo> — `https://vadimcarazan.com/`)**:
   - Landmark `<footer class="logo">` anchoring `Vadim Carazan, Creative Director` footer links (`Overview · Index · Archive · About · Contact`), copy *"Fourteen years of brand identities, websites and products fo"*, and `#fff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: vadimcarazan-com (Vadim Carazan, Creative Director)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `vadimcarazan-com` (**Vadim Carazan, Creative Director** — `https://vadimcarazan.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0b` / `#000`).
- **Identity & Domain Context**: Vadim Carazan, creative director and founder of WeGrow. Fourteen years of brand identities, websites and products for founders.
- **Primary Substrate**: `#0a0a0b` (`var(--bg)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0a0a0b` (`var(--bg)` in `:root`) paired with `#fff` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Serif` for display copy (`Let's make the next one yours.`) with `Inter Tight` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `440px` container bounds (`gap: 24px`, padding `6px`) with `cubic-bezier(0.22,1,0.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `vadimcarazan-com` in your global stylesheet:

:root {
  /* Vadim Carazan, Creative Director (vadimcarazan-com) — Ground-Truth Extracted CSS Variables */
  --bg: #0a0a0b; /* Canvas / Surface Token (vadimcarazan-com) */
  --ink: #f2f2f2; /* Typography Ink Token (vadimcarazan-com) */
  --mute: rgba(242, 242, 242, 0.55); /* Color / Atmospheric Token (vadimcarazan-com) */
  --line: rgba(255, 255, 255, 0.12); /* Color / Atmospheric Token (vadimcarazan-com) */
  --serif: "Editorial Old Italic", "Instrument Serif", "Times New Roman", serif; /* Typography / Scale Token (vadimcarazan-com) */
  --sans: "Inter Tight", "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif; /* Typography / Scale Token (vadimcarazan-com) */
  --pad: clamp(16px, 2vw, 32px); /* Layout / Spatial Grid Token (vadimcarazan-com) */
  --box-open: clamp(460px, 42vw, 780px); /* Dimension / Scale Token (vadimcarazan-com) */
  --ease: cubic-bezier(0.22, 1, 0.36, 1); /* Motion / Easing Token (vadimcarazan-com) */
  --bp: 28px; /* Dimension / Scale Token (vadimcarazan-com) */
  --hx: 748.8px; /* Dimension / Scale Token (vadimcarazan-com) */
  --hy: 196.0px; /* Dimension / Scale Token (vadimcarazan-com) */
  --hrx: 203.9px; /* Dimension / Scale Token (vadimcarazan-com) */
  --hry: 272.8px; /* Dimension / Scale Token (vadimcarazan-com) */
  --vadimcarazan-com-bg: #0a0a0b; /* Canvas Substrate (from `var(--bg)` in `:root`) (vadimcarazan-com) */
  --vadimcarazan-com-ink: #fff; /* Primary Typography Ink (stylesheet-derived) (vadimcarazan-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0a0a0b` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#f2f2f2` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `.start:hover { border-color: #fff }`
- **Interactive Accent / Highlight**: `#000` — grounded in `.start:hover i { color: #000 }`
- **Secondary / Muted Copy**: `#ff9b92` — grounded in `.c-err { color: #ff9b92 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `440px` extracted from `vadimcarazan-com` stylesheet
- **Padding & Gutters**: `6px` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (max-width: 860px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width:600px)`
- **Corner Radii**: `999px`, `50%`, `22px`, `12px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16.5px`, `14px`, `15vw`, `clamp(56px, 6vw, 96px)`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(32px, 3vw, 46px)`, `line-height: 1.02`, `letter-spacing: -0.01em`, `font-weight: 400`)
- **Body Copy Rule**: rule `.body` (`font-size: 15px`, `line-height: 1.6`)
- **Metadata & Index Rule**: rule `.label` (`font-size: 12px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `vadimcarazan-com` (`Vadim Carazan, Creative Director`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.topbar> — `vadimcarazan-com`)**:
   - DOM & Selectors: Landmark `<header class="topbar">` hosting `Vadim Carazan, Creative Director` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r169"`, `data-go="about"`, `data-go="about"`, `data-go="selected"`), and stylesheet rule `c.hot { cursor: pointer; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.topbar> — `vadimcarazan-com`)` (`vadimcarazan-com`) adapts across `@media (max-width: 860px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width:600px)` with `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Let's make the next one yours.`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Let's make the next one yours.` and copy excerpt *"Creative Director, WeGrow"* over `#0a0a0b` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0a0a0b` background with `#fff` headline `Let's make the next one yours.`.
3. **Primary Showcase & Content Grid (<section.view> — `A few to start with.`)**:
   - DOM & Selectors: Landmark `<section class="view v-project">` rendering section `A few to start with.` with copy *"Cluj-Napoca, Romania ( 13:10 )"*, asset references (`track.js`, `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `button { font: inherit; color: inherit; background: none; border: 0; padding: 0;... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.view> — `A few to start with.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.view> — `I make brands for founders who are`)**:
   - DOM & Selectors: Landmark `<section class="view v-selected">` framing `I make brands for founders who are building somet...` and `Tell me what you're building.` (*"Selected , Work , About , Contact"*) with `#fff` surface cards, `#000` accents, and `.logo { width: 48px; height: auto; display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.view> — `I make brands for founders who are`)` uses `999px`, `50%`, `22px`, `12px` radii, `#000` highlights, and assets (track.js, favicon.ico, favicon-32.png).
5. **Colophon & Global Directory Footer (<footer.logo> — `https://vadimcarazan.com/`)**:
   - DOM & Selectors: Landmark `<footer class="logo">` anchoring `Vadim Carazan, Creative Director` footer links (`Overview · Index · Archive · About · Contact`), copy *"Fourteen years of brand identities, websites and products fo"*, and `#fff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.logo> — `https://vadimcarazan.com/`)` aligns to `440px` extracted from `vadimcarazan-com` stylesheet with `6px` lateral canvas padding with `24px` grid gap and attributes (data-engine="three.js r169", data-go="about", data-go="about").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Creative Director, WeGrow"*
- Copy Excerpt 2: *"Cluj-Napoca, Romania ( 13:10 )"*
- Copy Excerpt 3: *"Selected , Work , About , Contact"*
- Copy Excerpt 4: *"Fourteen years of brand identities, websites and products for founders, from first..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`vadimcarazan-com`)**:
- `c.hot { cursor: pointer; }`
- `button { font: inherit; color: inherit; background: none; border: 0; padding: 0;... }`
- `.logo { width: 48px; height: auto; display: block; }`
- `.mark { display: block; line-height: 0; }`
- `.col { display: flex; flex-direction: column; }`
- **Per-Selector Transition Rules**:
- **Selector `.col-nav a`**: `transition: background-size 0.35s var(--ease)` extracted from `vadimcarazan-com` stylesheet.
- **Selector `.hero`**: `transition: opacity 0.6s ease, transform 0.9s var(--ease)` extracted from `vadimcarazan-com` stylesheet.
- **Selector `.start`**: `transition: border-color 0.3s ease, background 0.3s ease` extracted from `vadimcarazan-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.view>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `vadimcarazan-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
