---
title: "UI Prompt Blueprint: michellekayewashington-com"
date: 2026-11-15
target: "[[overview|michellekayewashington-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fffdf8` canvas, `#120a09` ink, `#2b201d` accent)"
---

# UI Design System & Master Generation Blueprint: michellekayewashington-com

> **Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC** (https://michellekayewashington.com/) — Michelle Kaye is a contemporary artist in Charleston, SC, exploring humanity’s relationship with the natural world. See Against the Grain...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/michellekayewashington-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC** (`https://michellekayewashington.com/`). Michelle Kaye is a contemporary artist in Charleston, SC, exploring humanity’s relationship with the natural world. See Against the Grain...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fffdf8` canvas, `#120a09` ink, `#2b201d` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fffdf8` (`var(--paper)` in `:root`) paired with `#120a09` primary typography and `#2b201d` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cormorant` for display copy (`Michelle Kaye`) with `Cormorant` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `30ch` container bounds (`gap: 0.35rem`, padding `0.5rem`) with `cubic-bezier(0.22,1,0.36,1)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/michellekayewashington-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `30ch` extracted from `michellekayewashington-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0.5rem` lateral canvas padding with `0.35rem` grid gap.
- **Border Radius Scale**: `50%`, `999px`, `1px`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 30ch`, `gap: 0.35rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 599px)`, `@media (max-height: 480px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 899px), (max-width: 999px) and (max-height: 5...`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fffdf8` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#f6f0e8` | `var(--paper-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#120a09` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#2b201d` | `var(--ink-2)` in `:root` |
| **Secondary / Muted Copy** | `#9a675c` | `var(--rose)` in `:root` |
| **Structural Hairline Border** | `#c68f81` | `var(--rose-2)` in `:root` |
| **Variable Token (`--tan`)** | `#b7a397` | `var(--tan)` in `:root` |
| **Variable Token (`--muted`)** | `#7a6560` | `var(--muted)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#fffdf8` | Canvas / Surface Token |
| `--paper-2` | `#f6f0e8` | Canvas / Surface Token |
| `--ink` | `#120a09` | Typography Ink Token |
| `--ink-2` | `#2b201d` | Typography Ink Token |
| `--rose` | `#9a675c` | Color / Atmospheric Token |
| `--rose-2` | `#c68f81` | Color / Atmospheric Token |
| `--tan` | `#b7a397` | Color / Atmospheric Token |
| `--rule` | `rgb(18 10 9 / 14%)` | Color / Atmospheric Token |
| `--fg` | `var(--ink)` | Typography Ink Token |
| `--bg` | `var(--paper)` | Canvas / Surface Token |
| `--muted` | `#7a6560` | Color / Atmospheric Token |
| `--nav-w` | `clamp(190px, 15vw, 300px)` | Layout / Spatial Grid Token |
| `--pad` | `clamp(1.25rem, 3.2vw, 4rem)` | Layout / Spatial Grid Token |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--ease-io` | `cubic-bezier(0.65, 0, 0.35, 1)` | Motion / Easing Token |
| `--serif` | `"Cormorant", Georgia, "Times New Roman", serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cormorant`.
- **Primary Body Stack**: `Cormorant`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`).
- **Body Copy**: rule `body` (`font-size: clamp(17px, 1.05vw + 10px, 21px)`, `line-height: 1.45`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `body`**: `transition: background-color 0.9s var(--ease), color 0.9s var(--ease)` extracted from `michellekayewashington-com` stylesheet.
- **Selector `.nav-index a`**: `transition: color 0.3s var(--ease)` extracted from `michellekayewashington-com` stylesheet.
- **Selector `.nav-label::after`**: `transition: transform 0.45s var(--ease)` extracted from `michellekayewashington-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.shell>` and `<section.home>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Michelle Kaye — Fine Arts · Contemporary A │
│ ====================================================================== │
│ [ <header.shell>           | 01 Michelle · 02 Gallery · 03 Socials  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home>                                       |   │
│ | H1: Michelle Kaye                                                |   │
│ | Substrate: #fffdf8    | Ink: #120a09    | Accent: #2b201d        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home>            ) max-w: 30ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | About the Artist             |  | Questions for the Artist?    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0.35re) | │
│ | [<header.shell>] -> [<section.home>] -> [<section.home>] |           │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mkl-cam>      ) | https://michellekayewashington.com │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.shell> — `michellekayewashington-com`)**:
   - Landmark `<header class="shell">` hosting `Michelle Kaye — Fine Arts · Contempo` navigation (`01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`), DOM attributes (`data-page="index"`, `data-ready="index"`, `data-shell`, `data-nav="index"`), and stylesheet rule `html { --room-title: var(--fg); }`.
2. **Hero Stage & Focal Lead (<section.home> — `Michelle Kaye`)**:
   - Landmark `<section class="home">` presenting display lead `Michelle Kaye` and copy excerpt *"Michelle Kaye Fine Arts"* over `#fffdf8` canvas and `#120a09` ink.
3. **Primary Showcase & Content Grid (<section.home> — `About the Artist`)**:
   - Landmark `<section class="home">` rendering section `About the Artist` with copy *"Drummond Studio Gallery"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `after { box-sizing: border-box; }`.
4. **Interactive Detail & Feature Matrix (<section.home> — `Questions for the Artist?`)**:
   - Landmark `<section class="home">` framing `Questions for the Artist?` and `Leaving this site` (*"Charleston City Paper"*) with `#120a09` surface cards, `#2b201d` accents, and `body { margin: 0; height: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.mkl-cam> — `https://michellekayewashington.com/`)**:
   - Landmark `<footer class="mkl-cam">` anchoring `Michelle Kaye — Fine Arts · Cont` footer links (`01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`), copy *"Charleston Magazine"*, and `#c68f81` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: michellekayewashington-com (Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `michellekayewashington-com` (**Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC** — `https://michellekayewashington.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fffdf8` canvas, `#120a09` ink, `#2b201d` accent).
- **Identity & Domain Context**: Michelle Kaye is a contemporary artist in Charleston, SC, exploring humanity’s relationship with the natural world. See Against the Grain...
- **Primary Substrate**: `#fffdf8` (`var(--paper)` in `:root`), **Primary Ink**: `#120a09`, **Accent / Highlight**: `#2b201d`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fffdf8` (`var(--paper)` in `:root`) paired with `#120a09` primary typography and `#2b201d` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cormorant` for display copy (`Michelle Kaye`) with `Cormorant` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `30ch` container bounds (`gap: 0.35rem`, padding `0.5rem`) with `cubic-bezier(0.22,1,0.36,1)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `michellekayewashington-com` in your global stylesheet:

:root {
  /* Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC (michellekayewashington-com) — Ground-Truth Extracted CSS Variables */
  --paper: #fffdf8; /* Canvas / Surface Token (michellekayewashington-com) */
  --paper-2: #f6f0e8; /* Canvas / Surface Token (michellekayewashington-com) */
  --ink: #120a09; /* Typography Ink Token (michellekayewashington-com) */
  --ink-2: #2b201d; /* Typography Ink Token (michellekayewashington-com) */
  --rose: #9a675c; /* Color / Atmospheric Token (michellekayewashington-com) */
  --rose-2: #c68f81; /* Color / Atmospheric Token (michellekayewashington-com) */
  --tan: #b7a397; /* Color / Atmospheric Token (michellekayewashington-com) */
  --rule: rgb(18 10 9 / 14%); /* Color / Atmospheric Token (michellekayewashington-com) */
  --fg: var(--ink); /* Typography Ink Token (michellekayewashington-com) */
  --bg: var(--paper); /* Canvas / Surface Token (michellekayewashington-com) */
  --muted: #7a6560; /* Color / Atmospheric Token (michellekayewashington-com) */
  --nav-w: clamp(190px, 15vw, 300px); /* Layout / Spatial Grid Token (michellekayewashington-com) */
  --pad: clamp(1.25rem, 3.2vw, 4rem); /* Layout / Spatial Grid Token (michellekayewashington-com) */
  --ease: cubic-bezier(0.22, 1, 0.36, 1); /* Motion / Easing Token (michellekayewashington-com) */
  --ease-io: cubic-bezier(0.65, 0, 0.35, 1); /* Motion / Easing Token (michellekayewashington-com) */
  --serif: "Cormorant", Georgia, "Times New Roman", serif; /* Typography / Scale Token (michellekayewashington-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fffdf8` — grounded in `var(--paper)` in `:root`
- **Primary Typography Ink**: `#f6f0e8` — grounded in `var(--paper-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#120a09` — grounded in `var(--ink)` in `:root`
- **Interactive Accent / Highlight**: `#2b201d` — grounded in `var(--ink-2)` in `:root`
- **Secondary / Muted Copy**: `#9a675c` — grounded in `var(--rose)` in `:root`
- **Structural Hairline Border**: `#c68f81` — grounded in `var(--rose-2)` in `:root`
- **Variable Token (`--tan`)**: `#b7a397` — grounded in `var(--tan)` in `:root`
- **Variable Token (`--muted`)**: `#7a6560` — grounded in `var(--muted)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `30ch` extracted from `michellekayewashington-com` stylesheet
- **Padding & Gutters**: `0.5rem` lateral canvas padding with `0.35rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 30ch`, `gap: 0.35rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding
- **Media Queries**: `@media (max-width: 599px)`, `@media (max-height: 480px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 899px), (max-width: 999px) and (max-height: 5...`
- **Corner Radii**: `50%`, `999px`, `1px`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cormorant`
- **Body Font Stack**: `Cormorant`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`)
- **Body Copy Rule**: rule `body` (`font-size: clamp(17px, 1.05vw + 10px, 21px)`, `line-height: 1.45`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `michellekayewashington-com` (`Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.shell> — `michellekayewashington-com`)**:
   - DOM & Selectors: Landmark `<header class="shell">` hosting `Michelle Kaye — Fine Arts · Contempo` navigation (`01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`), DOM attributes (`data-page="index"`, `data-ready="index"`, `data-shell`, `data-nav="index"`), and stylesheet rule `html { --room-title: var(--fg); }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.shell> — `michellekayewashington-com`)` (`michellekayewashington-com`) adapts across `@media (max-width: 599px)`, `@media (max-height: 480px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 899px), (max-width: 999px) and (max-height: 5...` with `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`.
2. **Hero Stage & Focal Lead (<section.home> — `Michelle Kaye`)**:
   - DOM & Selectors: Landmark `<section class="home">` presenting display lead `Michelle Kaye` and copy excerpt *"Michelle Kaye Fine Arts"* over `#fffdf8` canvas and `#120a09` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fffdf8` background with `#120a09` headline `Michelle Kaye`.
3. **Primary Showcase & Content Grid (<section.home> — `About the Artist`)**:
   - DOM & Selectors: Landmark `<section class="home">` rendering section `About the Artist` with copy *"Drummond Studio Gallery"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `after { box-sizing: border-box; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home> — `About the Artist`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 30ch`, `gap: 0.35rem`) on desktop and Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home> — `Questions for the Artist?`)**:
   - DOM & Selectors: Landmark `<section class="home">` framing `Questions for the Artist?` and `Leaving this site` (*"Charleston City Paper"*) with `#120a09` surface cards, `#2b201d` accents, and `body { margin: 0; height: 100%; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home> — `Questions for the Artist?`)` uses `50%`, `999px`, `1px`, `4px` radii, `#2b201d` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.mkl-cam> — `https://michellekayewashington.com/`)**:
   - DOM & Selectors: Landmark `<footer class="mkl-cam">` anchoring `Michelle Kaye — Fine Arts · Cont` footer links (`01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`), copy *"Charleston Magazine"*, and `#c68f81` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mkl-cam> — `https://michellekayewashington.com/`)` aligns to `30ch` extracted from `michellekayewashington-com` stylesheet with `0.5rem` lateral canvas padding with `0.35rem` grid gap and attributes (data-page="index", data-ready="index", data-shell).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Michelle Kaye Fine Arts"*
- Copy Excerpt 2: *"Drummond Studio Gallery"*
- Copy Excerpt 3: *"Charleston City Paper"*
- Copy Excerpt 4: *"Charleston Magazine"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`michellekayewashington-com`)**:
- `html { --room-title: var(--fg); }`
- `after { box-sizing: border-box; }`
- `body { margin: 0; height: 100%; }`
- `img { display: block; max-width: 100%; height: auto; }`
- `button { font: inherit; color: inherit; }`
- **Per-Selector Transition Rules**:
- **Selector `body`**: `transition: background-color 0.9s var(--ease), color 0.9s var(--ease)` extracted from `michellekayewashington-com` stylesheet.
- **Selector `.nav-index a`**: `transition: color 0.3s var(--ease)` extracted from `michellekayewashington-com` stylesheet.
- **Selector `.nav-label::after`**: `transition: transform 0.45s var(--ease)` extracted from `michellekayewashington-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.shell>` and `<section.home>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `michellekayewashington-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
