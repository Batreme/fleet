---
title: "UI Prompt Blueprint: members-play-lacoste-com_ace-breaker-rg"
date: 2026-11-23
captured_at: 2026-11-23
target: "members-play-lacoste-com_ace-breaker-rg"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fcd757`)"
---

# UI Design System & Master Generation Blueprint: members-play-lacoste-com_ace-breaker-rg

> **Lacoste - Ace breaker** (https://members-play.lacoste.com/ace-breaker-rg) — Play and break as many bricks as you can

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Lacoste - Ace breaker** (`https://members-play.lacoste.com/ace-breaker-rg`). Play and break as many bricks as you can
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fcd757`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#f3f2e1` primary typography and `#fcd757` accents.
  - **Grounded Typographic Hierarchy**: Pairs `MonaSans` for display copy (`Lacoste - Ace breaker`) with `MonaSans` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 20px`, padding `40px`) with `cubic-bezier(.25,.46,.45,.94)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (live computed `main` `max-width`).
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `var(--a07d8100)`, `50%`, `8px`, `30px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 375px) and (max-width: 1024px)`, `@media (min-width: 1024px) and (max-width: 1900px)`, `@media (min-width: 1901px)`, `@media (max-width: 699px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f3f2e1` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#00503c` | `:after { background: #00503c }` |
| **Interactive Accent / Highlight** | `#fcd757` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#3f8964` | `domi-gpc-label .right-container... { color: #3f8964 }` |
| **Structural Hairline Border** | `#7a7a2c` | `var(--border-color)` in `:root` (`rgba(245, 245, 88, .5)`) |
| **Variable Token (`--color-green`)** | `#008a20` | `var(--color-green)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-text` | `calc((22px) * var(--h-demult, 1))` | Typography Ink Token |
| `--color-main` | `#00503c` | Brand / Palette Token |
| `--color-accent` | `#fcd757` | Brand / Palette Token |
| `--color-green` | `#008A20` | Brand / Palette Token |
| `--padding` | `calc(var(--base-text))` | Layout / Spatial Grid Token |
| `--font-btn` | `MonaSans, Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-title` | `MonaSans, Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-text` | `MonaSans, Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--logo-size` | `calc((50px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--cta-text` | `calc((22.5px) * var(--h-demult, 1))` | Typography Ink Token |
| `--home-title` | `calc((45px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--prize-title` | `calc((45px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--prize-text` | `calc((22px) * var(--h-demult, 1))` | Typography Ink Token |
| `--padding-header` | `calc((10px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--size` | `calc((400px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--prize-mult` | `calc((24px) * var(--h-demult, 1))` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `MonaSans`.
- **Primary Body Stack**: `MonaSans`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--title)`, `line-height: 1.1`, `letter-spacing: -.06em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.5em`, `font-weight: bold`).
- **Body Copy**: live computed `body` (`font-size: 50px`, `line-height: 52.5px`, `font-weight: 500`); rule `p` (`font-size: 20px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 18.9px`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.55,0,.1,1)`, `cubic-bezier(.19,1,.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.base-cta[data-v-bd309550]`**: `transition: border-color .3s cubic-bezier(.25,.46,.45,.94),transform .3s c...` extracted from `members-play-lacoste-com_ace-breaker-rg` stylesheet.
- **Selector `.base-cta.is-result[data-v-bd309550]`**: `transition: border .3s cubic-bezier(.25,.46,.45,.94),transform .3s cubic-b...` extracted from `members-play-lacoste-com_ace-breaker-rg` stylesheet.
- **Selector `.base-cta.is-inv[data-v-bd309550]`**: `transition: border .3s cubic-bezier(.25,.46,.45,.94),transform .3s cubic-b...` extracted from `members-play-lacoste-com_ace-breaker-rg` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.46,.45,.94)`)**: Governs interactive state transitions across `<header.app-header>` and `<main.ui:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Lacoste - Ace breaker                      │
│ ====================================================================== │
│ [ <header.app-header> (1440x88px)     | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.ui> (w=1440px)                                   | │
│ | H1: Lacoste - Ace breaker                                          | │
│ | Substrate: #000000 | Ink: #f3f2e1 | Accent: #fcd757                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.ui:nth(2)>) max-w: 1440px                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.ui:nth(3)>) — Global Directory & Co           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.icons-sprite) | https://members-play.lacoste.com/ac  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.app-header>     ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.ui>) — 390px Vertical Lead                       | │
│ | H1: Lacoste - Ace breaker                                          | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.ui:nth(2)>) — 1-Col Stack                    | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.ui:nth(3)>) — 1-Col (Global Directory &)       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.icons-sprite) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.app-header> — `members-play-lacoste-com_ace-breaker-rg`)**:
   - Landmark `<header class="app-header visible">` (`1440x88px`) hosting `Lacoste - Ace breaker` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-name="Layer 1"`, `data-nosnippet="true"`, `data-lang-dir="ltr"`, `data-v-app`), and stylesheet rule `path { fill:fcd757 }`.
2. **Hero Stage & Focal Lead (<main.ui> — `Lacoste - Ace breaker`)**:
   - Landmark `<main class="ui">` presenting display lead `Lacoste - Ace breaker` and copy excerpt *"United Kingdom (EN)"* over `#000000` canvas and `#f3f2e1` ink.
3. **Primary Showcase & Content Grid (<main.ui:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"Lacoste - Ace breaker"*, asset references (`gtm.js`, `loader.js`, `favicon.ico`, `favicon_dark.svg`), and grid rule `disabled { pointer-events:none;opacity:.5 }`.
4. **Interactive Detail & Feature Matrix (<main.ui:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#00503c` surface cards, `#fcd757` accents, and `hover { background:fff;transform:scale(1.05) }`.
5. **Colophon & Global Directory Footer (<footer.icons-spritesheet> — `https://members-play.lacoste.com/ace-breaker-rg`)**:
   - Landmark `<footer class="icons-spritesheet">` anchoring `Lacoste - Ace breaker` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#7a7a2c` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: members-play-lacoste-com_ace-breaker-rg (Lacoste - Ace breaker)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `members-play-lacoste-com_ace-breaker-rg` (**Lacoste - Ace breaker** — `https://members-play.lacoste.com/ace-breaker-rg`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fcd757`).
- **Identity & Domain Context**: Play and break as many bricks as you can
- **Primary Substrate**: `#000000` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f3f2e1`, **Accent / Highlight**: `#fcd757`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#f3f2e1` primary typography and `#fcd757` accents.
  - **Grounded Typographic Hierarchy**: Pairs `MonaSans` for display copy (`Lacoste - Ace breaker`) with `MonaSans` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 20px`, padding `40px`) with `cubic-bezier(.25,.46,.45,.94)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `members-play-lacoste-com_ace-breaker-rg` in your global stylesheet:

:root {
  /* Lacoste - Ace breaker (members-play-lacoste-com_ace-breaker-rg) — Live-Grounded CSS Variables */
  --base-text: calc((22px) * var(--h-demult, 1)); /* Typography Ink Token (members-play-lacoste-com_ace-breaker-rg) */
  --color-main: #00503c; /* Brand / Palette Token (members-play-lacoste-com_ace-breaker-rg) */
  --color-accent: #fcd757; /* Brand / Palette Token (members-play-lacoste-com_ace-breaker-rg) */
  --color-green: #008A20; /* Brand / Palette Token (members-play-lacoste-com_ace-breaker-rg) */
  --padding: calc(var(--base-text)); /* Layout / Spatial Grid Token (members-play-lacoste-com_ace-breaker-rg) */
  --font-btn: MonaSans, Arial, Helvetica, sans-serif; /* Typography / Scale Token (members-play-lacoste-com_ace-breaker-rg) */
  --font-title: MonaSans, Arial, Helvetica, sans-serif; /* Typography / Scale Token (members-play-lacoste-com_ace-breaker-rg) */
  --font-text: MonaSans, Arial, Helvetica, sans-serif; /* Typography Ink Token (members-play-lacoste-com_ace-breaker-rg) */
  --logo-size: calc((50px) * var(--h-demult, 1)); /* Layout / Spatial Grid Token (members-play-lacoste-com_ace-breaker-rg) */
  --cta-text: calc((22.5px) * var(--h-demult, 1)); /* Typography Ink Token (members-play-lacoste-com_ace-breaker-rg) */
  --home-title: calc((45px) * var(--h-demult, 1)); /* Dimension / Scale Token (members-play-lacoste-com_ace-breaker-rg) */
  --prize-title: calc((45px) * var(--h-demult, 1)); /* Dimension / Scale Token (members-play-lacoste-com_ace-breaker-rg) */
  --prize-text: calc((22px) * var(--h-demult, 1)); /* Typography Ink Token (members-play-lacoste-com_ace-breaker-rg) */
  --padding-header: calc((10px) * var(--h-demult, 1)); /* Layout / Spatial Grid Token (members-play-lacoste-com_ace-breaker-rg) */
  --size: calc((400px) * var(--h-demult, 1)); /* Layout / Spatial Grid Token (members-play-lacoste-com_ace-breaker-rg) */
  --prize-mult: calc((24px) * var(--h-demult, 1)); /* Dimension / Scale Token (members-play-lacoste-com_ace-breaker-rg) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f3f2e1` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#00503c` — grounded in `:after { background: #00503c }`
- **Interactive Accent / Highlight**: `#fcd757` — grounded in `var(--color-accent)` in `:root`
- **Secondary / Muted Copy**: `#3f8964` — grounded in `domi-gpc-label .right-container... { color: #3f8964 }`
- **Structural Hairline Border**: `#7a7a2c` — grounded in `var(--border-color)` in `:root` (`rgba(245, 245, 88, .5)`)
- **Variable Token (`--color-green`)**: `#008a20` — grounded in `var(--color-green)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (live computed `main` `max-width`)
- **Padding & Gutters**: `40px` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding
- **Media Queries**: `@media (min-width: 375px) and (max-width: 1024px)`, `@media (min-width: 1024px) and (max-width: 1900px)`, `@media (min-width: 1901px)`, `@media (max-width: 699px)`
- **Corner Radii**: `var(--a07d8100)`, `50%`, `8px`, `30px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `MonaSans`
- **Body Font Stack**: `MonaSans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: var(--title)`, `line-height: 1.1`, `letter-spacing: -.06em`)
- **H2 Section Rule**: rule `h2` (`font-size: 1.5em`, `font-weight: bold`)
- **Body Copy Rule**: live computed `body` (`font-size: 50px`, `line-height: 52.5px`, `font-weight: 500`); rule `p` (`font-size: 20px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 18px`, `line-height: 18.9px`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `members-play-lacoste-com_ace-breaker-rg` (`Lacoste - Ace breaker`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.app-header> — `members-play-lacoste-com_ace-breaker-rg`)**:
   - DOM & Selectors: Landmark `<header class="app-header visible">` (`1440x88px`) hosting `Lacoste - Ace breaker` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-name="Layer 1"`, `data-nosnippet="true"`, `data-lang-dir="ltr"`, `data-v-app`), and stylesheet rule `path { fill:fcd757 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.app-header> — `members-play-lacoste-com_ace-breaker-rg`)` (`members-play-lacoste-com_ace-breaker-rg`) adapts across `@media (min-width: 375px) and (max-width: 1024px)`, `@media (min-width: 1024px) and (max-width: 1900px)`, `@media (min-width: 1901px)`, `@media (max-width: 699px)` with `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.55,0,.1,1)`, `cubic-bezier(.19,1,.22,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.ui> — `Lacoste - Ace breaker`)**:
   - DOM & Selectors: Landmark `<main class="ui">` presenting display lead `Lacoste - Ace breaker` and copy excerpt *"United Kingdom (EN)"* over `#000000` canvas and `#f3f2e1` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#f3f2e1` headline `Lacoste - Ace breaker`.
3. **Primary Showcase & Content Grid (<main.ui:nth(2)> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"Lacoste - Ace breaker"*, asset references (`gtm.js`, `loader.js`, `favicon.ico`, `favicon_dark.svg`), and grid rule `disabled { pointer-events:none;opacity:.5 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.ui:nth(2)> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.ui:nth(3)> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#00503c` surface cards, `#fcd757` accents, and `hover { background:fff;transform:scale(1.05) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.ui:nth(3)> — `Technical Architecture & Narrative`)` uses `var(--a07d8100)`, `50%`, `8px`, `30px` radii, `#fcd757` highlights, and assets (gtm.js, loader.js, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.icons-spritesheet> — `https://members-play.lacoste.com/ace-breaker-rg`)**:
   - DOM & Selectors: Landmark `<footer class="icons-spritesheet">` anchoring `Lacoste - Ace breaker` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#7a7a2c` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.icons-spritesheet> — `https://members-play.lacoste.com/ace-breaker-rg`)` aligns to `1440px` (live computed `main` `max-width`) with `40px` lateral canvas padding with `20px` grid gap and attributes (data-name="Layer 1", data-nosnippet="true", data-lang-dir="ltr").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"United Kingdom (EN)"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.55,0,.1,1)`, `cubic-bezier(.19,1,.22,1)`
- **Extracted Stylesheet Rules (`members-play-lacoste-com_ace-breaker-rg`)**:
- `path { fill:fcd757 }`
- `disabled { pointer-events:none;opacity:.5 }`
- `hover { background:fff;transform:scale(1.05) }`
- `strong { color:fcd757 }`
- `.animated-title { font-family:var(--font-title);line-height:1.05;color:f3f2e1;text-transfo... }`
- **Per-Selector Transition Rules**:
- **Selector `.base-cta[data-v-bd309550]`**: `transition: border-color .3s cubic-bezier(.25,.46,.45,.94),transform .3s c...` extracted from `members-play-lacoste-com_ace-breaker-rg` stylesheet.
- **Selector `.base-cta.is-result[data-v-bd309550]`**: `transition: border .3s cubic-bezier(.25,.46,.45,.94),transform .3s cubic-b...` extracted from `members-play-lacoste-com_ace-breaker-rg` stylesheet.
- **Selector `.base-cta.is-inv[data-v-bd309550]`**: `transition: border .3s cubic-bezier(.25,.46,.45,.94),transform .3s cubic-b...` extracted from `members-play-lacoste-com_ace-breaker-rg` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.46,.45,.94)`)**: Governs interactive state transitions across `<header.app-header>` and `<main.ui:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `members-play-lacoste-com_ace-breaker-rg`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
