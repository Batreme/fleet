---
title: "UI Prompt Blueprint: abhayrohit-com"
date: 2026-11-15
target: "[[overview|abhayrohit-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f5ead6` / `#d1c5ac`)"
---

# UI Design System & Master Generation Blueprint: abhayrohit-com

> **Abhay Rohit — Creative Product Engineer** (https://abhayrohit.com/) — Abhay Rohit is a creative product engineer in Indore, India, specializing in frontend engineering and interactive design with React, Next...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/abhayrohit-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Abhay Rohit — Creative Product Engineer** (`https://abhayrohit.com/`). Abhay Rohit is a creative product engineer in Indore, India, specializing in frontend engineering and interactive design with React, Next...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f5ead6` / `#d1c5ac`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f5ead6` (`var(--ink)` in `:root`) paired with `#241910` primary typography and `#d1c5ac` accents.
  - **Extracted Typographic Hierarchy**: Pairs `instrumentSans` for display copy (`A B H A Y R O H I T`) with `instrumentSans Fallback` and `jetbrainsMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `26ch` container bounds (`gap: 5px`, padding `6px`) with `cubic-bezier(.22,1,.36,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/abhayrohit-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `26ch` extracted from `abhayrohit-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `5px` grid gap.
- **Border Radius Scale**: `50%`, `28%`, `22%`, `39%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 26ch`, `gap: 5px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:reduce),(hover:none),(pointer:coa...`, `@media (max-width:760px),(max-height:600px),(pointer:coarse)`, `@media (max-height:600px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5ead6` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#241910` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f9ebd2` | `var(--text)` in `:root` |
| **Interactive Accent / Highlight** | `#d1c5ac` | `var(--rail-accent)` in `:root` |
| **Secondary / Muted Copy** | `#c1b8a6` | `var(--rail-ink)` in `:root` |
| **Structural Hairline Border** | `#20251f` | `var(--rail-active-ink)` in `:root` |
| **Variable Token (`--edge`)** | `#dcb67c66` | `var(--edge)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#f5ead6` | Typography Ink Token |
| `--paper` | `#241910` | Canvas / Surface Token |
| `--text` | `#f9ebd2` | Typography Ink Token |
| `--edge` | `#dcb67c66` | Color / Atmospheric Token |
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--cursor-paper` | `242 237 222` | Canvas / Surface Token |
| `--cursor-ink` | `39 40 33` | Typography Ink Token |
| `--cursor-accent` | `167 45 40` | Brand / Palette Token |
| `--cursor-ease` | `cubic-bezier(.2, .8, .2, 1)` | Motion / Easing Token |
| `--cursor-fill` | `rgb(var(--cursor-paper) / .96)` | Color / Atmospheric Token |
| `--cursor-text` | `rgb(var(--cursor-ink))` | Typography Ink Token |
| `--cursor-line` | `rgb(var(--cursor-paper) / .9)` | Color / Atmospheric Token |
| `--cursor-edge` | `rgb(var(--cursor-ink) / .48)` | Color / Atmospheric Token |
| `--cursor-mark` | `rgb(var(--cursor-accent))` | Color / Atmospheric Token |
| `--chapter-index` | `0` | Design System Custom Token |
| `--chapter-progress` | `0` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `instrumentSans`.
- **Primary Body Stack**: `instrumentSans Fallback`.
- **Technical / Metadata Stack**: `jetbrainsMono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--qi-font-display: "anton", "anton Fallback", Impact, Arial Narrow, sans-serif`, `--qi-font-studio-display: "antonStudio", "antonStudio Fallback"`, `--archive-display: "display", "display Fallback", Impact`; rule `h1` (`font-size: clamp(58px,8.8vw,144px)`).
- **Section Heading (`H2`)**: CSS variables `--opening-subtitle: clamp(34.72px,3.224cqw,59.52px)`; rule `h2` (`font-size: clamp(36px,5vw,80px)`).
- **Body Copy**: rule `p` (`font-size: clamp(16px,1.8vw,25px)`).
- **Metadata & Navigation Labels**: CSS variables `--qi-font-mono: "jetbrainsMono", ui-monospace, monospace`, `--archive-mono: "mono", "mono Fallback", Courier New`; rule `small` (`font-size: clamp(10px,.8vw,14px)`, `line-height: 1.4`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.76,0,.24,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.RaGumW_frame`**: `transition: opacity .42s var(--ease)` extracted from `abhayrohit-com` stylesheet.
- **Selector `.RaGumW_corner`**: `transition: transform .66s var(--ease)` extracted from `abhayrohit-com` stylesheet.
- **Selector `.RaGumW_copy`**: `transition: opacity .24s ease,transform .58s var(--ease)` extracted from `abhayrohit-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.MLPEba_header>` and `<section.KKuYoa_variable>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Abhay Rohit — Creative Product Engineer    │
│ ====================================================================== │
│ [ <header.MLPEba_header>   | Website · Patient portal · Care team · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.MLPEba_hero>                                |   │
│ | H1: A B H A Y R O H I T                                          |   │
│ | Substrate: #f5ead6    | Ink: #241910    | Accent: #d1c5ac        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.KKuYoa_variable> ) max-w: 26ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | My first engineering job.    |  | Where care begins.           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 5px   ) | │
│ | [<header.MLPEba_hea] -> [<section.MLPEba_he] -> [<section.KKuYoa_va] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.jFvPUW_footer>) | https://abhayrohit.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.MLPEba_header> — `abhayrohit-com`)**:
   - Landmark `<header class="MLPEba_header">` hosting `Abhay Rohit — Creative Product Engin` navigation (`Website · Patient portal · Care team · Operations · Read the case study`), DOM attributes (`data-film-entry="cold-home"`, `data-paint-loader="active"`, `data-preload-tier="desktop"`, `data-preload-bytes="153382"`), and stylesheet rule `.RaGumW_cue .RaGumW_frame { opacity:.36 }`.
2. **Hero Stage & Focal Lead (<section.MLPEba_hero> — `A B H A Y R O H I T`)**:
   - Landmark `<section class="MLPEba_hero">` presenting display lead `A B H A Y R O H I T` and copy excerpt *"Skip to the written portfolio"* over `#f5ead6` canvas and `#241910` ink.
3. **Primary Showcase & Content Grid (<section.KKuYoa_variable> — `My first engineering job.`)**:
   - Landmark `<section class="KKuYoa_variable">` rendering section `My first engineering job.` with copy *"Drag or tap Drag the grip to explore; release to return home. Tap"*, asset references (`anton_full_entry_subset-s.p.0dq58...`, `anton_kinetic_margin-s.p.1o1u0v9k...`, `instrument_sans_latin_wdth_normal...`, `jetbrains_mono_latin_wght_normal_...`), and grid rule `.RaGumW_cue { --ink:38251d;--paper:38251d;--text:fff1d8;--edge:38251d66 }`.
4. **Interactive Detail & Feature Matrix (<article.rojSVa_variable> — `Where care begins.`)**:
   - Landmark `<article class="rojSVa_variable">` framing `Where care begins.` and `A clearer experience for patients.` (*"Drag the grip to explore; release to return home. Tap to visit th"*) with `#f9ebd2` surface cards, `#d1c5ac` accents, and `.RaGumW_frame { transition:opacity .42s var(--ease);position:absolute;inset:0 }`.
5. **Colophon & Global Directory Footer (<footer.jFvPUW_footer> — `https://abhayrohit.com/`)**:
   - Landmark `<footer class="jFvPUW_footer">` anchoring `Abhay Rohit — Creative Product E` footer links (`Website · Patient portal · Care team · Operations · Read the case study`), copy *"Gaming . A miniature world of music, gaming, photography and"*, and `#20251f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: abhayrohit-com (Abhay Rohit — Creative Product Engineer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `abhayrohit-com` (**Abhay Rohit — Creative Product Engineer** — `https://abhayrohit.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5ead6` / `#d1c5ac`).
- **Identity & Domain Context**: Abhay Rohit is a creative product engineer in Indore, India, specializing in frontend engineering and interactive design with React, Next...
- **Primary Substrate**: `#f5ead6` (`var(--ink)` in `:root`), **Primary Ink**: `#241910`, **Accent / Highlight**: `#d1c5ac`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f5ead6` (`var(--ink)` in `:root`) paired with `#241910` primary typography and `#d1c5ac` accents.
  - **Extracted Typographic Hierarchy**: Pairs `instrumentSans` for display copy (`A B H A Y R O H I T`) with `instrumentSans Fallback` and `jetbrainsMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `26ch` container bounds (`gap: 5px`, padding `6px`) with `cubic-bezier(.22,1,.36,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `abhayrohit-com` in your global stylesheet:

:root {
  /* Abhay Rohit — Creative Product Engineer (abhayrohit-com) — Ground-Truth Extracted CSS Variables */
  --ink: #f5ead6; /* Typography Ink Token (abhayrohit-com) */
  --paper: #241910; /* Canvas / Surface Token (abhayrohit-com) */
  --text: #f9ebd2; /* Typography Ink Token (abhayrohit-com) */
  --edge: #dcb67c66; /* Color / Atmospheric Token (abhayrohit-com) */
  --ease: cubic-bezier(.22, 1, .36, 1); /* Motion / Easing Token (abhayrohit-com) */
  --cursor-paper: 242 237 222; /* Canvas / Surface Token (abhayrohit-com) */
  --cursor-ink: 39 40 33; /* Typography Ink Token (abhayrohit-com) */
  --cursor-accent: 167 45 40; /* Brand / Palette Token (abhayrohit-com) */
  --cursor-ease: cubic-bezier(.2, .8, .2, 1); /* Motion / Easing Token (abhayrohit-com) */
  --cursor-fill: rgb(var(--cursor-paper) / .96); /* Color / Atmospheric Token (abhayrohit-com) */
  --cursor-text: rgb(var(--cursor-ink)); /* Typography Ink Token (abhayrohit-com) */
  --cursor-line: rgb(var(--cursor-paper) / .9); /* Color / Atmospheric Token (abhayrohit-com) */
  --cursor-edge: rgb(var(--cursor-ink) / .48); /* Color / Atmospheric Token (abhayrohit-com) */
  --cursor-mark: rgb(var(--cursor-accent)); /* Color / Atmospheric Token (abhayrohit-com) */
  --chapter-index: 0; /* Design System Custom Token (abhayrohit-com) */
  --chapter-progress: 0; /* Design System Custom Token (abhayrohit-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5ead6` — grounded in `var(--ink)` in `:root`
- **Primary Typography Ink**: `#241910` — grounded in `var(--paper)` in `:root`
- **Elevated Surface / Card Substrate**: `#f9ebd2` — grounded in `var(--text)` in `:root`
- **Interactive Accent / Highlight**: `#d1c5ac` — grounded in `var(--rail-accent)` in `:root`
- **Secondary / Muted Copy**: `#c1b8a6` — grounded in `var(--rail-ink)` in `:root`
- **Structural Hairline Border**: `#20251f` — grounded in `var(--rail-active-ink)` in `:root`
- **Variable Token (`--edge`)**: `#dcb67c66` — grounded in `var(--edge)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `26ch` extracted from `abhayrohit-com` stylesheet
- **Padding & Gutters**: `6px` lateral canvas padding with `5px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 26ch`, `gap: 5px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:reduce),(hover:none),(pointer:coa...`, `@media (max-width:760px),(max-height:600px),(pointer:coarse)`, `@media (max-height:600px)`
- **Corner Radii**: `50%`, `28%`, `22%`, `39%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `instrumentSans`
- **Body Font Stack**: `instrumentSans Fallback`
- **Monospace / Technical Font Stack**: `jetbrainsMono`
- **H1 Display Rule**: CSS variables `--qi-font-display: "anton", "anton Fallback", Impact, Arial Narrow, sans-serif`, `--qi-font-studio-display: "antonStudio", "antonStudio Fallback"`, `--archive-display: "display", "display Fallback", Impact`; rule `h1` (`font-size: clamp(58px,8.8vw,144px)`)
- **H2 Section Rule**: CSS variables `--opening-subtitle: clamp(34.72px,3.224cqw,59.52px)`; rule `h2` (`font-size: clamp(36px,5vw,80px)`)
- **Body Copy Rule**: rule `p` (`font-size: clamp(16px,1.8vw,25px)`)
- **Metadata & Index Rule**: CSS variables `--qi-font-mono: "jetbrainsMono", ui-monospace, monospace`, `--archive-mono: "mono", "mono Fallback", Courier New`; rule `small` (`font-size: clamp(10px,.8vw,14px)`, `line-height: 1.4`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `abhayrohit-com` (`Abhay Rohit — Creative Product Engineer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.MLPEba_header> — `abhayrohit-com`)**:
   - DOM & Selectors: Landmark `<header class="MLPEba_header">` hosting `Abhay Rohit — Creative Product Engin` navigation (`Website · Patient portal · Care team · Operations · Read the case study`), DOM attributes (`data-film-entry="cold-home"`, `data-paint-loader="active"`, `data-preload-tier="desktop"`, `data-preload-bytes="153382"`), and stylesheet rule `.RaGumW_cue .RaGumW_frame { opacity:.36 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.MLPEba_header> — `abhayrohit-com`)` (`abhayrohit-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:reduce),(hover:none),(pointer:coa...`, `@media (max-width:760px),(max-height:600px),(pointer:coarse)`, `@media (max-height:600px)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.76,0,.24,1)` transitions and links `Website · Patient portal · Care team · Operations · Read the case study`.
2. **Hero Stage & Focal Lead (<section.MLPEba_hero> — `A B H A Y R O H I T`)**:
   - DOM & Selectors: Landmark `<section class="MLPEba_hero">` presenting display lead `A B H A Y R O H I T` and copy excerpt *"Skip to the written portfolio"* over `#f5ead6` canvas and `#241910` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f5ead6` background with `#241910` headline `A B H A Y R O H I T`.
3. **Primary Showcase & Content Grid (<section.KKuYoa_variable> — `My first engineering job.`)**:
   - DOM & Selectors: Landmark `<section class="KKuYoa_variable">` rendering section `My first engineering job.` with copy *"Drag or tap Drag the grip to explore; release to return home. Tap"*, asset references (`anton_full_entry_subset-s.p.0dq58...`, `anton_kinetic_margin-s.p.1o1u0v9k...`, `instrument_sans_latin_wdth_normal...`, `jetbrains_mono_latin_wght_normal_...`), and grid rule `.RaGumW_cue { --ink:38251d;--paper:38251d;--text:fff1d8;--edge:38251d66 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.KKuYoa_variable> — `My first engineering job.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 26ch`, `gap: 5px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.rojSVa_variable> — `Where care begins.`)**:
   - DOM & Selectors: Landmark `<article class="rojSVa_variable">` framing `Where care begins.` and `A clearer experience for patients.` (*"Drag the grip to explore; release to return home. Tap to visit th"*) with `#f9ebd2` surface cards, `#d1c5ac` accents, and `.RaGumW_frame { transition:opacity .42s var(--ease);position:absolute;inset:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.rojSVa_variable> — `Where care begins.`)` uses `50%`, `28%`, `22%`, `39%` radii, `#d1c5ac` highlights, and assets (anton_full_entry_subset-s.p.0dq58..., anton_kinetic_margin-s.p.1o1u0v9k..., instrument_sans_latin_wdth_normal...).
5. **Colophon & Global Directory Footer (<footer.jFvPUW_footer> — `https://abhayrohit.com/`)**:
   - DOM & Selectors: Landmark `<footer class="jFvPUW_footer">` anchoring `Abhay Rohit — Creative Product E` footer links (`Website · Patient portal · Care team · Operations · Read the case study`), copy *"Gaming . A miniature world of music, gaming, photography and"*, and `#20251f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.jFvPUW_footer> — `https://abhayrohit.com/`)` aligns to `26ch` extracted from `abhayrohit-com` stylesheet with `6px` lateral canvas padding with `5px` grid gap and attributes (data-film-entry="cold-home", data-paint-loader="active", data-preload-tier="desktop").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to the written portfolio"*
- Copy Excerpt 2: *"Drag or tap Drag the grip to explore; release to return home. Tap to visit the nex..."*
- Copy Excerpt 3: *"Drag the grip to explore; release to return home. Tap to visit the next detail. Th..."*
- Copy Excerpt 4: *"Gaming . A miniature world of music, gaming, photography and training behind the n..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.76,0,.24,1)`
- **Extracted Stylesheet Rules (`abhayrohit-com`)**:
- `.RaGumW_cue .RaGumW_frame { opacity:.36 }`
- `.RaGumW_cue { --ink:38251d;--paper:38251d;--text:fff1d8;--edge:38251d66 }`
- `.RaGumW_frame { transition:opacity .42s var(--ease);position:absolute;inset:0 }`
- `.RaGumW_corner { width:calc(19px*var(--d));height:calc(19px*var(--d));transition:transfor... }`
- `.RaGumW_corner:after { content:"";opacity:.8;background:currentColor;position:absolute }`
- **Per-Selector Transition Rules**:
- **Selector `.RaGumW_frame`**: `transition: opacity .42s var(--ease)` extracted from `abhayrohit-com` stylesheet.
- **Selector `.RaGumW_corner`**: `transition: transform .66s var(--ease)` extracted from `abhayrohit-com` stylesheet.
- **Selector `.RaGumW_copy`**: `transition: opacity .24s ease,transform .58s var(--ease)` extracted from `abhayrohit-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.MLPEba_header>` and `<section.KKuYoa_variable>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `abhayrohit-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
