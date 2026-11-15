---
title: "UI Prompt Blueprint: pinreply-com"
date: 2026-11-15
target: "pinreply-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#101828` canvas, `#f8fafc` ink, `#e4e7ec` accent)"
---

# UI Design System & Master Generation Blueprint: pinreply-com

> **PinReply — Design feedback, in the right place** (https://pinreply.com/) — PinReply is a design feedback tool for visual comments on websites. Point to a change, share a review, and keep replies in context.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **PinReply — Design feedback, in the right place** (`https://pinreply.com/`). PinReply is a design feedback tool for visual comments on websites. Point to a change, share a review, and keep replies in context.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#101828` canvas, `#f8fafc` ink, `#e4e7ec` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#101828` (`var(--ink)` in `:root`) paired with `#f8fafc` primary typography and `#e4e7ec` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Website feedback. Without the back-a`) with `Inter` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `530px` container bounds (`gap: 28px`, padding `12px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×4025px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `530px` extracted from `pinreply-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `12px` lateral canvas padding with `28px` grid gap.
- **Border Radius Scale**: `10px`, `100px`, `50%`, `24px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 530px`, `gap: 28px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:900px)`, `@media (max-width:620px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#101828` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#344054` | `var(--secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#667085` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#e4e7ec` | `var(--line)` in `:root` |
| **Secondary / Muted Copy** | `#f8fafc` | `var(--canvas)` in `:root` |
| **Structural Hairline Border** | `#5b4cee` | `var(--brand)` in `:root` |
| **Variable Token (`--hover`)** | `#4938d1` | `var(--hover)` in `:root` |
| **Variable Token (`--soft`)** | `#f5f3ff` | `var(--soft)` in `:root` |
| **Variable Token (`--mint`)** | `#087c6f` | `var(--mint)` in `:root` |
| **Variable Token (`--mint-soft`)** | `#f0fdf9` | `var(--mint-soft)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#101828` | Typography Ink Token |
| `--secondary` | `#344054` | Brand / Palette Token |
| `--muted` | `#667085` | Color / Atmospheric Token |
| `--line` | `#e4e7ec` | Color / Atmospheric Token |
| `--canvas` | `#f8fafc` | Canvas / Surface Token |
| `--brand` | `#5b4cee` | Brand / Palette Token |
| `--hover` | `#4938d1` | Color / Atmospheric Token |
| `--soft` | `#f5f3ff` | Color / Atmospheric Token |
| `--mint` | `#087c6f` | Color / Atmospheric Token |
| `--mint-soft` | `#f0fdf9` | Color / Atmospheric Token |
| `--radius` | `18px` | Elevation / Border Token |
| `--pinreply-com-bg` | `#101828` | Canvas Substrate (from `var(--ink)` in `:root`) |
| `--pinreply-com-ink` | `#f8fafc` | Primary Typography Ink (stylesheet-derived) |
| `--pinreply-com-surface` | `#667085` | Surface Substrate (stylesheet-derived) |
| `--pinreply-com-accent` | `#e4e7ec` | Interactive Accent (stylesheet-derived) |
| `--pinreply-com-muted` | `#f8fafc` | Secondary Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 46px`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 36px`).
- **Body Copy**: rule `p` (`font-size: 14px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(42px,5.5vw,72px)`, `clamp(30px,4vw,44px)`, `22px`, `23px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.button`**: `transition: background .15s,border-color .15s` extracted from `pinreply-com` stylesheet.
- **Selector `:after`**: `transition: none!important` extracted from `pinreply-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.section>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — PinReply — Design feedback, in the right p │
│ ====================================================================== │
│ [ <header.header>          | How it works · For clients · FAQ · Add ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Website feedback. Without the back-and-forth.                |   │
│ | Substrate: #101828    | Ink: #f8fafc    | Accent: #e4e7ec        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: 530px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | 1 Spaces for everyday living |  | Point. Explain. Move forward | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 28px  ) | │
│ | [<header.header>] -> [<section.hero>] -> [<section.section>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://pinreply.com/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `pinreply-com`)**:
   - Landmark `<header class="header">` hosting `PinReply — Design feedback, in the r` navigation (`How it works · For clients · FAQ · Add to Chrome`), DOM attributes (`data-ads-conversion="add-to-chrome"`, `data-ads-conversion="add-to-chrome"`, `data-ads-conversion="add-to-chrome"`, `data-ads-choice="decline"`), and stylesheet rule `html { scroll-behavior:smooth;scroll-padding-top:100px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Website feedback. Without the back`)**:
   - Landmark `<section class="hero">` presenting display lead `Website feedback. Without the back-and-forth.` and copy excerpt *"Point to what needs changing. Add a visual comment. Keep client r"* over `#101828` canvas and `#f8fafc` ink.
3. **Primary Showcase & Content Grid (<section.section> — `1 Spaces for everyday living.`)**:
   - Landmark `<section class="section">` rendering section `1 Spaces for everyday living.` with copy *"For Chrome on desktop. Free at launch. No account or payment card"*, asset references (`favicon.png`, `site.css`, `ads.js`, `pinreply-mark.svg`), and grid rule `textarea { font:inherit }`.
4. **Interactive Detail & Feature Matrix (<article.card> — `Point. Explain. Move forward.`)**:
   - Landmark `<article class="card">` framing `Point. Explain. Move forward.` and `Pin the change` (*"Give the headline more room above the button."*) with `#667085` surface cards, `#e4e7ec` accents, and `summary { -webkit-tap-highlight-color:transparent }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://pinreply.com/`)**:
   - Landmark `<footer class="footer">` anchoring `PinReply — Design feedback, in t` footer links (`How it works · For clients · FAQ · Add to Chrome`), copy *"An example review, with demonstration content."*, and `#5b4cee` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: pinreply-com (PinReply — Design feedback, in the right place)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `pinreply-com` (**PinReply — Design feedback, in the right place** — `https://pinreply.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#101828` canvas, `#f8fafc` ink, `#e4e7ec` accent).
- **Identity & Domain Context**: PinReply is a design feedback tool for visual comments on websites. Point to a change, share a review, and keep replies in context.
- **Primary Substrate**: `#101828` (`var(--ink)` in `:root`), **Primary Ink**: `#f8fafc`, **Accent / Highlight**: `#e4e7ec`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#101828` (`var(--ink)` in `:root`) paired with `#f8fafc` primary typography and `#e4e7ec` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Website feedback. Without the back-a`) with `Inter` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `530px` container bounds (`gap: 28px`, padding `12px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `pinreply-com` in your global stylesheet:

:root {
  /* PinReply — Design feedback, in the right place (pinreply-com) — Ground-Truth Extracted CSS Variables */
  --ink: #101828; /* Typography Ink Token (pinreply-com) */
  --secondary: #344054; /* Brand / Palette Token (pinreply-com) */
  --muted: #667085; /* Color / Atmospheric Token (pinreply-com) */
  --line: #e4e7ec; /* Color / Atmospheric Token (pinreply-com) */
  --canvas: #f8fafc; /* Canvas / Surface Token (pinreply-com) */
  --brand: #5b4cee; /* Brand / Palette Token (pinreply-com) */
  --hover: #4938d1; /* Color / Atmospheric Token (pinreply-com) */
  --soft: #f5f3ff; /* Color / Atmospheric Token (pinreply-com) */
  --mint: #087c6f; /* Color / Atmospheric Token (pinreply-com) */
  --mint-soft: #f0fdf9; /* Color / Atmospheric Token (pinreply-com) */
  --radius: 18px; /* Elevation / Border Token (pinreply-com) */
  --pinreply-com-bg: #101828; /* Canvas Substrate (from `var(--ink)` in `:root`) (pinreply-com) */
  --pinreply-com-ink: #f8fafc; /* Primary Typography Ink (stylesheet-derived) (pinreply-com) */
  --pinreply-com-surface: #667085; /* Surface Substrate (stylesheet-derived) (pinreply-com) */
  --pinreply-com-accent: #e4e7ec; /* Interactive Accent (stylesheet-derived) (pinreply-com) */
  --pinreply-com-muted: #f8fafc; /* Secondary Ink (stylesheet-derived) (pinreply-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#101828` — grounded in `var(--ink)` in `:root`
- **Primary Typography Ink**: `#344054` — grounded in `var(--secondary)` in `:root`
- **Elevated Surface / Card Substrate**: `#667085` — grounded in `var(--muted)` in `:root`
- **Interactive Accent / Highlight**: `#e4e7ec` — grounded in `var(--line)` in `:root`
- **Secondary / Muted Copy**: `#f8fafc` — grounded in `var(--canvas)` in `:root`
- **Structural Hairline Border**: `#5b4cee` — grounded in `var(--brand)` in `:root`
- **Variable Token (`--hover`)**: `#4938d1` — grounded in `var(--hover)` in `:root`
- **Variable Token (`--soft`)**: `#f5f3ff` — grounded in `var(--soft)` in `:root`
- **Variable Token (`--mint`)**: `#087c6f` — grounded in `var(--mint)` in `:root`
- **Variable Token (`--mint-soft`)**: `#f0fdf9` — grounded in `var(--mint-soft)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×4025px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `530px` extracted from `pinreply-com` stylesheet
- **Padding & Gutters**: `12px` lateral canvas padding with `28px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 530px`, `gap: 28px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding
- **Media Queries**: `@media (max-width:900px)`, `@media (max-width:620px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px)`
- **Corner Radii**: `10px`, `100px`, `50%`, `24px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 46px`)
- **H2 Section Rule**: rule `h2` (`font-size: 36px`)
- **Body Copy Rule**: rule `p` (`font-size: 14px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(42px,5.5vw,72px)`, `clamp(30px,4vw,44px)`, `22px`, `23px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `pinreply-com` (`PinReply — Design feedback, in the right place`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `pinreply-com`)**:
   - DOM & Selectors: Landmark `<header class="header">` hosting `PinReply — Design feedback, in the r` navigation (`How it works · For clients · FAQ · Add to Chrome`), DOM attributes (`data-ads-conversion="add-to-chrome"`, `data-ads-conversion="add-to-chrome"`, `data-ads-conversion="add-to-chrome"`, `data-ads-choice="decline"`), and stylesheet rule `html { scroll-behavior:smooth;scroll-padding-top:100px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `pinreply-com`)` (`pinreply-com`) adapts across `@media (max-width:900px)`, `@media (max-width:620px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:760px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `How it works · For clients · FAQ · Add to Chrome`.
2. **Hero Stage & Focal Lead (<section.hero> — `Website feedback. Without the back`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Website feedback. Without the back-and-forth.` and copy excerpt *"Point to what needs changing. Add a visual comment. Keep client r"* over `#101828` canvas and `#f8fafc` ink.
   - Responsive Contract: Hero stage (`1440×4025px` desktop / `390×2400px` mobile) sets `#101828` background with `#f8fafc` headline `Website feedback. Without the back-and-forth.`.
3. **Primary Showcase & Content Grid (<section.section> — `1 Spaces for everyday living.`)**:
   - DOM & Selectors: Landmark `<section class="section">` rendering section `1 Spaces for everyday living.` with copy *"For Chrome on desktop. Free at launch. No account or payment card"*, asset references (`favicon.png`, `site.css`, `ads.js`, `pinreply-mark.svg`), and grid rule `textarea { font:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `1 Spaces for everyday living.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 530px`, `gap: 28px`) on desktop and Single-column vertical stack at `390px` viewport width with `12px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.card> — `Point. Explain. Move forward.`)**:
   - DOM & Selectors: Landmark `<article class="card">` framing `Point. Explain. Move forward.` and `Pin the change` (*"Give the headline more room above the button."*) with `#667085` surface cards, `#e4e7ec` accents, and `summary { -webkit-tap-highlight-color:transparent }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.card> — `Point. Explain. Move forward.`)` uses `10px`, `100px`, `50%`, `24px` radii, `#e4e7ec` highlights, and assets (favicon.png, site.css, ads.js).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://pinreply.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `PinReply — Design feedback, in t` footer links (`How it works · For clients · FAQ · Add to Chrome`), copy *"An example review, with demonstration content."*, and `#5b4cee` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://pinreply.com/`)` aligns to `530px` extracted from `pinreply-com` stylesheet with `12px` lateral canvas padding with `28px` grid gap and attributes (data-ads-conversion="add-to-chrome", data-ads-conversion="add-to-chrome", data-ads-conversion="add-to-chrome").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Point to what needs changing. Add a visual comment. Keep client replies and design..."*
- Copy Excerpt 2: *"For Chrome on desktop. Free at launch. No account or payment card needed."*
- Copy Excerpt 3: *"Give the headline more room above the button."*
- Copy Excerpt 4: *"An example review, with demonstration content."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`pinreply-com`)**:
- `html { scroll-behavior:smooth;scroll-padding-top:100px }`
- `textarea { font:inherit }`
- `summary { -webkit-tap-highlight-color:transparent }`
- `button { cursor:pointer }`
- `button:disabled { cursor:wait;opacity:.6 }`
- **Per-Selector Transition Rules**:
- **Selector `.button`**: `transition: background .15s,border-color .15s` extracted from `pinreply-com` stylesheet.
- **Selector `:after`**: `transition: none!important` extracted from `pinreply-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.section>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `pinreply-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
