---
title: "UI Prompt Blueprint: www-kaviengcreative-com"
date: 2026-11-15
target: "[[overview|www-kaviengcreative-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#050505` canvas, `#f0efe9` ink, `#0a0a09` accent)"
---

# UI Design System & Master Generation Blueprint: www-kaviengcreative-com

> **Kavieng Cheng · Art Director and Creative** (https://www.kaviengcreative.com/) — Kavieng Cheng is a Hong Kong-based art director and creative working across advertising, product, fine art and photography.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Kavieng Cheng · Art Director and Creative** (`https://www.kaviengcreative.com/`). Kavieng Cheng is a Hong Kong-based art director and creative working across advertising, product, fine art and photography.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#050505` canvas, `#f0efe9` ink, `#0a0a09` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#050505` (`var(--archive-black)` in `:root`) paired with `#f0efe9` primary typography and `#0a0a09` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Heros` for display copy (`Kavieng Cheng`) with `Junicode` and `Junicode`.
  - **Calibrated Spatial Grid & Motion**: Combines `78px` container bounds (`gap: 16px`, padding `24px`) with `cubic-bezier(.16,1,.3,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `78px` extracted from `www-kaviengcreative-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `24px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `8px`, `50%`, `5px`, `6px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 78px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:700px)`, `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:380px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#050505` | `var(--archive-black)` in `:root` |
| **Primary Typography Ink** | `#f0efe9` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c9c8c3` | `var(--page-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#0a0a09` | `var(--hard-ink)` in `:root` |
| **Secondary / Muted Copy** | `#8a8a84` | `var(--graphite)` in `:root` |
| **Structural Hairline Border** | `#aaa9a2` | `var(--silver)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--archive-black` | `#050505` | Canvas / Surface Token |
| `--paper` | `#f0efe9` | Canvas / Surface Token |
| `--page-grey` | `#c9c8c3` | Color / Atmospheric Token |
| `--hard-ink` | `#0a0a09` | Typography Ink Token |
| `--graphite` | `#8a8a84` | Color / Atmospheric Token |
| `--silver` | `#aaa9a2` | Color / Atmospheric Token |
| `--rule-dark` | `rgba(10, 10, 9, .19)` | Canvas / Surface Token |
| `--rule-light` | `rgba(240, 239, 233, .19)` | Canvas / Surface Token |
| `--gutter` | `40px` | Layout / Spatial Grid Token |
| `--perspective-blur` | `0px` | Elevation / Border Token |
| `--www-kaviengcreat-bg` | `#050505` | Canvas Substrate (from `var(--archive-black)` in `:root`) |
| `--www-kaviengcreat-ink` | `#f0efe9` | Primary Typography Ink (stylesheet-derived) |
| `--www-kaviengcreat-surface` | `#c9c8c3` | Surface Substrate (stylesheet-derived) |
| `--www-kaviengcreat-accent` | `#0a0a09` | Interactive Accent (stylesheet-derived) |
| `--www-kaviengcreat-muted` | `#8a8a84` | Secondary Ink (stylesheet-derived) |
| `--www-kaviengcreat-border` | `#aaa9a2` | Structural Border (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Heros`.
- **Primary Body Stack**: `Junicode`.
- **Technical / Metadata Stack**: `Junicode`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: -.055em`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `18px`, `13px`, `11px`, `15px`).
- **Body Copy**: rule `p` (`letter-spacing: -.006em`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `18px`, `13px`, `11px`, `15px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,1,.4,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.tile:before`**: `transition: opacity .36s cubic-bezier(.16,1,.3,1)` extracted from `www-kaviengcreative-com` stylesheet.
- **Selector `.tile img`**: `transition: filter .36s cubic-bezier(.16,1,.3,1)` extracted from `www-kaviengcreative-com` stylesheet.
- **Selector `.focus-reticle`**: `transition: opacity .18s ease` extracted from `www-kaviengcreative-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.archive-header>` and `<section.view-shell>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.view-shell>` and `<section.view-shell>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Kavieng Cheng · Art Director and Creative  │
│ ====================================================================== │
│ [ <header.archive-header>  | Archive · About · Awards · Press · Pri ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.view-shell>                                 |   │
│ | H1: Kavieng Cheng                                                |   │
│ | Substrate: #050505    | Ink: #f0efe9    | Accent: #0a0a09        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.view-shell>      ) max-w: 78px           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Art director + creative      |  | Kavieng Cheng Art director + | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.archive-he] -> [<section.view-shel] -> [<section.view-shel] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.loader__hint> ) | https://www.kaviengcreative.com/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.archive-header> — `www-kaviengcreative-com`)**:
   - Landmark `<header class="archive-header">` hosting `Kavieng Cheng · Art Director and Cre` navigation (`Archive · About · Awards · Press · Private`), DOM attributes (`data-route="archive"`, `data-route="archive"`, `data-route="about"`, `data-route="awards"`), and stylesheet rule `app { width:100%;height:100%;margin:0;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.view-shell> — `Kavieng Cheng`)**:
   - Landmark `<section class="view-shell">` presenting display lead `Kavieng Cheng` and copy excerpt *"Art director + creative"* over `#050505` canvas and `#f0efe9` ink.
3. **Primary Showcase & Content Grid (<section.view-shell> — `Art director + creative`)**:
   - Landmark `<section class="view-shell">` rendering section `Art director + creative` with copy *"Kavieng Cheng Art director + creative"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `main-C5DSeFRy.js`), and grid rule `html { background:var(--archive-black) }`.
4. **Interactive Detail & Feature Matrix (<section.view-shell> — `Kavieng Cheng Art director + creat`)**:
   - Landmark `<section class="view-shell">` framing `Kavieng Cheng Art director + creative` and `The UN-billed Space` (*"The UN-billed Space"*) with `#c9c8c3` surface cards, `#0a0a09` accents, and `body { background:var(--archive-black);color:var(--paper);font-family:Heros,Ari... }`.
5. **Colophon & Global Directory Footer (<footer.loader__hint> — `https://www.kaviengcreative.com/`)**:
   - Landmark `<footer class="loader__hint">` anchoring `Kavieng Cheng · Art Director and` footer links (`Archive · About · Awards · Press · Private`), copy *"The Touch Annual Report"*, and `#aaa9a2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-kaviengcreative-com (Kavieng Cheng · Art Director and Creative)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-kaviengcreative-com` (**Kavieng Cheng · Art Director and Creative** — `https://www.kaviengcreative.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#050505` canvas, `#f0efe9` ink, `#0a0a09` accent).
- **Identity & Domain Context**: Kavieng Cheng is a Hong Kong-based art director and creative working across advertising, product, fine art and photography.
- **Primary Substrate**: `#050505` (`var(--archive-black)` in `:root`), **Primary Ink**: `#f0efe9`, **Accent / Highlight**: `#0a0a09`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#050505` (`var(--archive-black)` in `:root`) paired with `#f0efe9` primary typography and `#0a0a09` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Heros` for display copy (`Kavieng Cheng`) with `Junicode` and `Junicode`.
  - **Calibrated Spatial Grid & Motion**: Combines `78px` container bounds (`gap: 16px`, padding `24px`) with `cubic-bezier(.16,1,.3,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-kaviengcreative-com` in your global stylesheet:

:root {
  /* Kavieng Cheng · Art Director and Creative (www-kaviengcreative-com) — Ground-Truth Extracted CSS Variables */
  --archive-black: #050505; /* Canvas / Surface Token (www-kaviengcreative-com) */
  --paper: #f0efe9; /* Canvas / Surface Token (www-kaviengcreative-com) */
  --page-grey: #c9c8c3; /* Color / Atmospheric Token (www-kaviengcreative-com) */
  --hard-ink: #0a0a09; /* Typography Ink Token (www-kaviengcreative-com) */
  --graphite: #8a8a84; /* Color / Atmospheric Token (www-kaviengcreative-com) */
  --silver: #aaa9a2; /* Color / Atmospheric Token (www-kaviengcreative-com) */
  --rule-dark: rgba(10, 10, 9, .19); /* Canvas / Surface Token (www-kaviengcreative-com) */
  --rule-light: rgba(240, 239, 233, .19); /* Canvas / Surface Token (www-kaviengcreative-com) */
  --gutter: 40px; /* Layout / Spatial Grid Token (www-kaviengcreative-com) */
  --perspective-blur: 0px; /* Elevation / Border Token (www-kaviengcreative-com) */
  --www-kaviengcreat-bg: #050505; /* Canvas Substrate (from `var(--archive-black)` in `:root`) (www-kaviengcreative-com) */
  --www-kaviengcreat-ink: #f0efe9; /* Primary Typography Ink (stylesheet-derived) (www-kaviengcreative-com) */
  --www-kaviengcreat-surface: #c9c8c3; /* Surface Substrate (stylesheet-derived) (www-kaviengcreative-com) */
  --www-kaviengcreat-accent: #0a0a09; /* Interactive Accent (stylesheet-derived) (www-kaviengcreative-com) */
  --www-kaviengcreat-muted: #8a8a84; /* Secondary Ink (stylesheet-derived) (www-kaviengcreative-com) */
  --www-kaviengcreat-border: #aaa9a2; /* Structural Border (stylesheet-derived) (www-kaviengcreative-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#050505` — grounded in `var(--archive-black)` in `:root`
- **Primary Typography Ink**: `#f0efe9` — grounded in `var(--paper)` in `:root`
- **Elevated Surface / Card Substrate**: `#c9c8c3` — grounded in `var(--page-grey)` in `:root`
- **Interactive Accent / Highlight**: `#0a0a09` — grounded in `var(--hard-ink)` in `:root`
- **Secondary / Muted Copy**: `#8a8a84` — grounded in `var(--graphite)` in `:root`
- **Structural Hairline Border**: `#aaa9a2` — grounded in `var(--silver)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `78px` extracted from `www-kaviengcreative-com` stylesheet
- **Padding & Gutters**: `24px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 78px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding
- **Media Queries**: `@media (max-width:700px)`, `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:380px)`
- **Corner Radii**: `8px`, `50%`, `5px`, `6px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Heros`
- **Body Font Stack**: `Junicode`
- **Monospace / Technical Font Stack**: `Junicode`
- **H1 Display Rule**: rule `h1` (`letter-spacing: -.055em`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `18px`, `13px`, `11px`, `15px`)
- **Body Copy Rule**: rule `p` (`letter-spacing: -.006em`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `18px`, `13px`, `11px`, `15px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-kaviengcreative-com` (`Kavieng Cheng · Art Director and Creative`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.archive-header> — `www-kaviengcreative-com`)**:
   - DOM & Selectors: Landmark `<header class="archive-header">` hosting `Kavieng Cheng · Art Director and Cre` navigation (`Archive · About · Awards · Press · Private`), DOM attributes (`data-route="archive"`, `data-route="archive"`, `data-route="about"`, `data-route="awards"`), and stylesheet rule `app { width:100%;height:100%;margin:0;overflow:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.archive-header> — `www-kaviengcreative-com`)` (`www-kaviengcreative-com`) adapts across `@media (max-width:700px)`, `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:380px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,1,.4,1)` transitions and links `Archive · About · Awards · Press · Private`.
2. **Hero Stage & Focal Lead (<section.view-shell> — `Kavieng Cheng`)**:
   - DOM & Selectors: Landmark `<section class="view-shell">` presenting display lead `Kavieng Cheng` and copy excerpt *"Art director + creative"* over `#050505` canvas and `#f0efe9` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#050505` background with `#f0efe9` headline `Kavieng Cheng`.
3. **Primary Showcase & Content Grid (<section.view-shell> — `Art director + creative`)**:
   - DOM & Selectors: Landmark `<section class="view-shell">` rendering section `Art director + creative` with copy *"Kavieng Cheng Art director + creative"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `main-C5DSeFRy.js`), and grid rule `html { background:var(--archive-black) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.view-shell> — `Art director + creative`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 78px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `24px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.view-shell> — `Kavieng Cheng Art director + creat`)**:
   - DOM & Selectors: Landmark `<section class="view-shell">` framing `Kavieng Cheng Art director + creative` and `The UN-billed Space` (*"The UN-billed Space"*) with `#c9c8c3` surface cards, `#0a0a09` accents, and `body { background:var(--archive-black);color:var(--paper);font-family:Heros,Ari... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.view-shell> — `Kavieng Cheng Art director + creat`)` uses `8px`, `50%`, `5px`, `6px` radii, `#0a0a09` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.loader__hint> — `https://www.kaviengcreative.com/`)**:
   - DOM & Selectors: Landmark `<footer class="loader__hint">` anchoring `Kavieng Cheng · Art Director and` footer links (`Archive · About · Awards · Press · Private`), copy *"The Touch Annual Report"*, and `#aaa9a2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.loader__hint> — `https://www.kaviengcreative.com/`)` aligns to `78px` extracted from `www-kaviengcreative-com` stylesheet with `24px` lateral canvas padding with `16px` grid gap and attributes (data-route="archive", data-route="archive", data-route="about").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Art director + creative"*
- Copy Excerpt 2: *"Kavieng Cheng Art director + creative"*
- Copy Excerpt 3: *"The UN-billed Space"*
- Copy Excerpt 4: *"The Touch Annual Report"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.3,1,.4,1)`
- **Extracted Stylesheet Rules (`www-kaviengcreative-com`)**:
- `app { width:100%;height:100%;margin:0;overflow:hidden }`
- `html { background:var(--archive-black) }`
- `body { background:var(--archive-black);color:var(--paper);font-family:Heros,Ari... }`
- `img { max-width:100%;-webkit-user-select:none;user-select:none;-webkit-user-dr... }`
- `selection { background:var(--hard-ink);color:var(--paper) }`
- **Per-Selector Transition Rules**:
- **Selector `.tile:before`**: `transition: opacity .36s cubic-bezier(.16,1,.3,1)` extracted from `www-kaviengcreative-com` stylesheet.
- **Selector `.tile img`**: `transition: filter .36s cubic-bezier(.16,1,.3,1)` extracted from `www-kaviengcreative-com` stylesheet.
- **Selector `.focus-reticle`**: `transition: opacity .18s ease` extracted from `www-kaviengcreative-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.archive-header>` and `<section.view-shell>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.view-shell>` and `<section.view-shell>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-kaviengcreative-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
