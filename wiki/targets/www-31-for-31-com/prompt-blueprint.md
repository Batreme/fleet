---
title: "UI Prompt Blueprint: www-31-for-31-com"
date: 2026-11-15
target: "[[overview|www-31-for-31-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#8d8a80`)"
---

# UI Design System & Master Generation Blueprint: www-31-for-31-com

> **31 for 31 · One scary movie for every night of October** (https://www.31-for-31.com/) — Thirty one horror movies, one for each night of October. Rate them, find where to stream them, and scroll through the whole tape.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-31-for-31-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **31 for 31 · One scary movie for every night of October** (`https://www.31-for-31.com/`). Thirty one horror movies, one for each night of October. Rate them, find where to stream them, and scroll through the whole tape.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#8d8a80`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#07090c` (`var(--bg)` in `:root`) paired with `#e8e4d8` primary typography and `#8d8a80` accents.
  - **Extracted Typographic Hierarchy**: Pairs `OC Blimp` for display copy (`Rope`) with `Zombie Punks` and `Saans Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `720px` container bounds (`gap: 14px`, padding `6px`) with `cubic-bezier(.2,.8,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-31-for-31-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `720px` extracted from `www-31-for-31-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `14px` grid gap.
- **Border Radius Scale**: `4px`, `50%`, `8px`, `1px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 720px`, `gap: 14px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 720px)`, `@media (max-height: 820px) and (min-width: 721px)`, `@media (hover: none), (pointer: coarse), (max-width: 720px)`, `@media (max-width: 860px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#07090c` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#0d1218` | `var(--bg-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e8e4d8` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#8d8a80` | `var(--muted)` in `:root` |
| **Secondary / Muted Copy** | `#4dff8c` | `var(--green)` in `:root` |
| **Structural Hairline Border** | `#1f8f4e` | `var(--green-dim)` in `:root` |
| **Variable Token (`--orange`)** | `#ff6a1a` | `var(--orange)` in `:root` |
| **Variable Token (`--red`)** | `#ff2d55` | `var(--red)` in `:root` |
| **Variable Token (`--cyan`)** | `#2ee6ff` | `var(--cyan)` in `:root` |
| **Variable Token (`--block-a`)** | `#b8321f` | `var(--block-a)` in `:root` |
| **Variable Token (`--block-b`)** | `#1f3d2b` | `var(--block-b)` in `:root` |
| **Variable Token (`--block-c`)** | `#2a1f45` | `var(--block-c)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#07090c` | Canvas / Surface Token |
| `--bg-2` | `#0d1218` | Canvas / Surface Token |
| `--ink` | `#e8e4d8` | Typography Ink Token |
| `--muted` | `#8d8a80` | Color / Atmospheric Token |
| `--green` | `#4dff8c` | Color / Atmospheric Token |
| `--green-dim` | `#1f8f4e` | Color / Atmospheric Token |
| `--orange` | `#ff6a1a` | Color / Atmospheric Token |
| `--red` | `#ff2d55` | Color / Atmospheric Token |
| `--cyan` | `#2ee6ff` | Color / Atmospheric Token |
| `--block-a` | `#b8321f` | Color / Atmospheric Token |
| `--block-b` | `#1f3d2b` | Color / Atmospheric Token |
| `--block-c` | `#2a1f45` | Color / Atmospheric Token |
| `--font-spooky` | `"Creepster", "Impact", cursive` | Typography / Scale Token |
| `--font-blimp` | `"OC Blimp", "Creepster", "Impact", cursive` | Typography / Scale Token |
| `--font-osd` | `"Saans Mono", ui-monospace, "SF Mono", Menlo, "Courier New", monospace` | Typography / Scale Token |
| `--font-body` | `"Saans", system-ui, -apple-system, "Helvetica Neue", sans-serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `OC Blimp`.
- **Primary Body Stack**: `Zombie Punks`.
- **Technical / Metadata Stack**: `Saans Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.title` (`line-height: 0`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(28px, 3.4vw, 52px)`, `line-height: 1`, `font-weight: 400`).
- **Body Copy**: CSS variables `--font-body: "Saans", system-ui, -apple-system, "Helvetica Neue", sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 15px`, `letter-spacing: .3em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.75,.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.osd-bl .snd-ico`**: `transition: transform .2s` extracted from `www-31-for-31-com` stylesheet.
- **Selector `.deck-links`**: `transition: grid-template-columns .45s cubic-bezier(.2,.8,.2,1)` extracted from `www-31-for-31-com` stylesheet.
- **Selector `.deck-links-in`**: `transition: padding-left .45s cubic-bezier(.2,.8,.2,1), opacity .25s` extracted from `www-31-for-31-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.film>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — 31 for 31 · One scary movie for every nigh │
│ ====================================================================== │
│ [ <header.topbar>          | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Rope                                                         |   │
│ | Substrate: #07090c    | Ink: #e8e4d8    | Accent: #8d8a80        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.film>            ) max-w: 720px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Mandy                        |  | Wes Craven's New Nightmare   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 14px  ) | │
│ | [<header.topbar>] -> [<section.hero>] -> [<section.film>] |          │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://www.31-for-31.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.topbar> — `www-31-for-31-com`)**:
   - Landmark `<header class="topbar">` hosting `31 for 31 · One scary movie for ever` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound-toggle`, `data-view="scroll"`, `data-label="Scroll"`, `data-view="gallery"`), and stylesheet rule `focus { outline: none; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Rope`)**:
   - Landmark `<section class="hero">` presenting display lead `Rope` and copy excerpt *"One scary movie for every night of October. Thirty one tapes, rew"* over `#07090c` canvas and `#e8e4d8` ink.
3. **Primary Showcase & Content Grid (<section.film> — `Mandy`)**:
   - Landmark `<section class="film">` rendering section `Mandy` with copy *"1948 DIR. ALFRED HITCHCOCK"*, asset references (`apple-touch-icon.png`, `Saans-Regular.woff`, `SaansMono-Regular.woff`, `style.css`), and grid rule `focus-visible { outline: 2px solid var(--green); outline-offset: 3px; box-shadow: 0 0 0... }`.
4. **Interactive Detail & Feature Matrix (<section.film> — `Wes Craven's New Nightmare`)**:
   - Landmark `<section class="film">` framing `Wes Craven's New Nightmare` and `Candyman` (*"DIR. ALFRED HITCHCOCK"*) with `#e8e4d8` surface cards, `#8d8a80` accents, and `.stream a:focus-visible { outline-offset: 2px; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.31-for-31.com/`)**:
   - Landmark `<footer class="footer">` anchoring `31 for 31 · One scary movie for ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Two college friends strangle a classmate, hide the body in a"*, and `#1f8f4e` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-31-for-31-com (31 for 31 · One scary movie for every night of October)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-31-for-31-com` (**31 for 31 · One scary movie for every night of October** — `https://www.31-for-31.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#8d8a80`).
- **Identity & Domain Context**: Thirty one horror movies, one for each night of October. Rate them, find where to stream them, and scroll through the whole tape.
- **Primary Substrate**: `#07090c` (`var(--bg)` in `:root`), **Primary Ink**: `#e8e4d8`, **Accent / Highlight**: `#8d8a80`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#07090c` (`var(--bg)` in `:root`) paired with `#e8e4d8` primary typography and `#8d8a80` accents.
  - **Extracted Typographic Hierarchy**: Pairs `OC Blimp` for display copy (`Rope`) with `Zombie Punks` and `Saans Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `720px` container bounds (`gap: 14px`, padding `6px`) with `cubic-bezier(.2,.8,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-31-for-31-com` in your global stylesheet:

:root {
  /* 31 for 31 · One scary movie for every night of October (www-31-for-31-com) — Ground-Truth Extracted CSS Variables */
  --bg: #07090c; /* Canvas / Surface Token (www-31-for-31-com) */
  --bg-2: #0d1218; /* Canvas / Surface Token (www-31-for-31-com) */
  --ink: #e8e4d8; /* Typography Ink Token (www-31-for-31-com) */
  --muted: #8d8a80; /* Color / Atmospheric Token (www-31-for-31-com) */
  --green: #4dff8c; /* Color / Atmospheric Token (www-31-for-31-com) */
  --green-dim: #1f8f4e; /* Color / Atmospheric Token (www-31-for-31-com) */
  --orange: #ff6a1a; /* Color / Atmospheric Token (www-31-for-31-com) */
  --red: #ff2d55; /* Color / Atmospheric Token (www-31-for-31-com) */
  --cyan: #2ee6ff; /* Color / Atmospheric Token (www-31-for-31-com) */
  --block-a: #b8321f; /* Color / Atmospheric Token (www-31-for-31-com) */
  --block-b: #1f3d2b; /* Color / Atmospheric Token (www-31-for-31-com) */
  --block-c: #2a1f45; /* Color / Atmospheric Token (www-31-for-31-com) */
  --font-spooky: "Creepster", "Impact", cursive; /* Typography / Scale Token (www-31-for-31-com) */
  --font-blimp: "OC Blimp", "Creepster", "Impact", cursive; /* Typography / Scale Token (www-31-for-31-com) */
  --font-osd: "Saans Mono", ui-monospace, "SF Mono", Menlo, "Courier New", monospace; /* Typography / Scale Token (www-31-for-31-com) */
  --font-body: "Saans", system-ui, -apple-system, "Helvetica Neue", sans-serif; /* Typography / Scale Token (www-31-for-31-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#07090c` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#0d1218` — grounded in `var(--bg-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#e8e4d8` — grounded in `var(--ink)` in `:root`
- **Interactive Accent / Highlight**: `#8d8a80` — grounded in `var(--muted)` in `:root`
- **Secondary / Muted Copy**: `#4dff8c` — grounded in `var(--green)` in `:root`
- **Structural Hairline Border**: `#1f8f4e` — grounded in `var(--green-dim)` in `:root`
- **Variable Token (`--orange`)**: `#ff6a1a` — grounded in `var(--orange)` in `:root`
- **Variable Token (`--red`)**: `#ff2d55` — grounded in `var(--red)` in `:root`
- **Variable Token (`--cyan`)**: `#2ee6ff` — grounded in `var(--cyan)` in `:root`
- **Variable Token (`--block-a`)**: `#b8321f` — grounded in `var(--block-a)` in `:root`
- **Variable Token (`--block-b`)**: `#1f3d2b` — grounded in `var(--block-b)` in `:root`
- **Variable Token (`--block-c`)**: `#2a1f45` — grounded in `var(--block-c)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `720px` extracted from `www-31-for-31-com` stylesheet
- **Padding & Gutters**: `6px` lateral canvas padding with `14px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 720px`, `gap: 14px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (max-width: 720px)`, `@media (max-height: 820px) and (min-width: 721px)`, `@media (hover: none), (pointer: coarse), (max-width: 720px)`, `@media (max-width: 860px)`
- **Corner Radii**: `4px`, `50%`, `8px`, `1px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `OC Blimp`
- **Body Font Stack**: `Zombie Punks`
- **Monospace / Technical Font Stack**: `Saans Mono`
- **H1 Display Rule**: rule `.title` (`line-height: 0`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(28px, 3.4vw, 52px)`, `line-height: 1`, `font-weight: 400`)
- **Body Copy Rule**: CSS variables `--font-body: "Saans", system-ui, -apple-system, "Helvetica Neue", sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`)
- **Metadata & Index Rule**: rule `small` (`font-size: 15px`, `letter-spacing: .3em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-31-for-31-com` (`31 for 31 · One scary movie for every night of October`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.topbar> — `www-31-for-31-com`)**:
   - DOM & Selectors: Landmark `<header class="topbar">` hosting `31 for 31 · One scary movie for ever` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound-toggle`, `data-view="scroll"`, `data-label="Scroll"`, `data-view="gallery"`), and stylesheet rule `focus { outline: none; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.topbar> — `www-31-for-31-com`)` (`www-31-for-31-com`) adapts across `@media (max-width: 720px)`, `@media (max-height: 820px) and (min-width: 721px)`, `@media (hover: none), (pointer: coarse), (max-width: 720px)`, `@media (max-width: 860px)` with `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.75,.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Rope`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Rope` and copy excerpt *"One scary movie for every night of October. Thirty one tapes, rew"* over `#07090c` canvas and `#e8e4d8` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#07090c` background with `#e8e4d8` headline `Rope`.
3. **Primary Showcase & Content Grid (<section.film> — `Mandy`)**:
   - DOM & Selectors: Landmark `<section class="film">` rendering section `Mandy` with copy *"1948 DIR. ALFRED HITCHCOCK"*, asset references (`apple-touch-icon.png`, `Saans-Regular.woff`, `SaansMono-Regular.woff`, `style.css`), and grid rule `focus-visible { outline: 2px solid var(--green); outline-offset: 3px; box-shadow: 0 0 0... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.film> — `Mandy`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 720px`, `gap: 14px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.film> — `Wes Craven's New Nightmare`)**:
   - DOM & Selectors: Landmark `<section class="film">` framing `Wes Craven's New Nightmare` and `Candyman` (*"DIR. ALFRED HITCHCOCK"*) with `#e8e4d8` surface cards, `#8d8a80` accents, and `.stream a:focus-visible { outline-offset: 2px; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.film> — `Wes Craven's New Nightmare`)` uses `4px`, `50%`, `8px`, `1px` radii, `#8d8a80` highlights, and assets (apple-touch-icon.png, Saans-Regular.woff, SaansMono-Regular.woff).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.31-for-31.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `31 for 31 · One scary movie for ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Two college friends strangle a classmate, hide the body in a"*, and `#1f8f4e` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://www.31-for-31.com/`)` aligns to `720px` extracted from `www-31-for-31-com` stylesheet with `6px` lateral canvas padding with `14px` grid gap and attributes (data-sound-toggle, data-view="scroll", data-label="Scroll").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"One scary movie for every night of October. Thirty one tapes, rewound and ready. S..."*
- Copy Excerpt 2: *"1948 DIR. ALFRED HITCHCOCK"*
- Copy Excerpt 3: *"DIR. ALFRED HITCHCOCK"*
- Copy Excerpt 4: *"Two college friends strangle a classmate, hide the body in a chest, then host a di..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.75,.25,1)`
- **Extracted Stylesheet Rules (`www-31-for-31-com`)**:
- `focus { outline: none; }`
- `focus-visible { outline: 2px solid var(--green); outline-offset: 3px; box-shadow: 0 0 0... }`
- `.stream a:focus-visible { outline-offset: 2px; }`
- `html { background: var(--bg); color: var(--ink); scroll-behavior: auto; overflo... }`
- `html.lenis body { height: auto; }`
- **Per-Selector Transition Rules**:
- **Selector `.osd-bl .snd-ico`**: `transition: transform .2s` extracted from `www-31-for-31-com` stylesheet.
- **Selector `.deck-links`**: `transition: grid-template-columns .45s cubic-bezier(.2,.8,.2,1)` extracted from `www-31-for-31-com` stylesheet.
- **Selector `.deck-links-in`**: `transition: padding-left .45s cubic-bezier(.2,.8,.2,1), opacity .25s` extracted from `www-31-for-31-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.film>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-31-for-31-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
