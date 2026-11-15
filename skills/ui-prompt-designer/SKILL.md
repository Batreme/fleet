---
name: ui-prompt-designer
description: Reverse-engineers web properties, design tokens, DOM hierarchies, and visual assets into an actionable, production-grade AI prompt blueprint for generating high-craft web applications without generic AI slop.
---

# UI Prompt Designer Skill

This skill defines the rigorous methodology for reverse-engineering web applications and digital experiences into actionable, production-ready AI design prompts and structural blueprints. It bridges the gap between raw web assets (DOM, CSS variables, runtime network calls, screenshots) and zero-shot code generation models.

## Core Principle: Eradicating AI Slop

A generation prompt derived using this skill must **never** rely on generic design abstractions (e.g., "modern clean interface with blue accents and card shadows"). Instead, it extracts and enforces:
1. **Concrete Mathematical Ratios**: Exact modular grids, fluid clamp formulas, and proportional aspect ratios.
2. **Deterministic Color & Materiality Tokens**: Exact hex/HSL/RGBA values with explicit semantic mappings for substrates, elevated surfaces, hairline borders, and ink hierarchies.
3. **Physical Motion & Easing Curves**: Exact CSS `cubic-bezier()` functions, spring parameters, duration timings, and scroll-scrub triggers.
4. **Authentic Editorial & Graphic Craft**: Distinct typographic pairings, monoline annotations, hairline borders, asymmetric layouts, and purposeful negative space.

---

## 7-Part Prompt Blueprint Schema

Every reverse-engineered application must be documented in a standardized `prompt-blueprint.md` adhering to the following 7 sections:

### 1. Executive Visual Persona & Design Archetype
- **Brand Essence & Positioning**: Target audience, aesthetic philosophy, and emotional tone.
- **Visual Archetype**: Grounded classification (e.g., *Kinetic Horology Lab*, *Monolith Ink & Bone Editorial*, *Tactical Aerospace HUD*, *Avant-Garde Spatial Brutalism*).
- **Anti-AI-Slop Differentiators**: 4–6 specific technical and aesthetic decisions that elevate this interface above standard SaaS templates (e.g., hairline border systems, custom cursor physics, bespoke SVG glyphs, zero-box-shadow philosophy).

### 2. Spatial Architecture & Modular Grid Mathematics
- **Viewport Canvas Allocation**: Maximum width bounds, base padding scales, gutter widths, and column systems.
- **Desktop Grid (`1440×900`+)**: Exact CSS Grid and Flexbox layouts (`grid-template-columns`, `gap`, auto-fill/auto-fit logic).
- **Mobile Grid (`390×844`)**: Structural transformations, drawer collapsibility, horizontal overflow carousels, and responsive touch targets.
- **Aspect-Ratio & Clamping Rules**: Media container aspect ratios, image crop locks, and responsive clamping logic (`min()`, `max()`, `clamp()`).

### 3. Color System, Materiality & Atmospheric Lighting
- **Substrate & Surface Palette**: Exact values for base canvas, secondary panels, backdrop blurs, and glassmorphism.
- **Ink & Contrast Hierarchy**: Primary display text, body copy, muted micro-labels, and disabled states.
- **Hairline Dividers & Framing**: Exact 1px border tokens, opacity values, and perimeter bounding styles.
- **Accent & State Tokens**: Focus states, interactive hovers, active indicators, and notification badges.
- **Lighting & Texture**: Noise shaders, radial gradient spotlights, frosted glass filters (`backdrop-filter: blur(Npx)`), and inset highlights.

### 4. Typographic Scale & Editorial Hierarchy
- **Font Stack Definition**: Display headers, primary body sans/serif, monospaced metadata, and fallback stacks.
- **Fluid Scale Calculations**: Step-by-step fluid typography formulas using `clamp(min, preferred, max)`.
- **Micro-Typographic Tuning**: Explicit `font-weight`, `line-height`, `letter-spacing` (tracking in `em` or `px`), `text-transform`, and OpenType `font-feature-settings` (e.g., `'tnum'`, `'ss01'`).

### 5. Choreographed Motion & Interaction Physics
- **Timing & Bézier Functions**: Exact cubic-bezier easing curves (e.g., `cubic-bezier(0.16, 1, 0.3, 1)` for snappy ease-out, `cubic-bezier(0.83, 0, 0.17, 1)` for cinematic ease-in-out).
- **Interaction States**: Hover, active, focus, and drag feedback on interactive primitives.
- **Scroll & Scrollytelling Choreography**: Scroll-triggered section pinning, parallax layers, progress counters, and optical zoom/scrub mechanics.
- **Canvas / WebGL Shaders**: Ambient particle fields, distortion ripples, or Three.js camera transitions if present.

### 6. Component Wireframe & Structural DOM Map
- **Mermaid / ASCII Structural Hierarchy**: Visual block diagram representing the full layout hierarchy.
- **Granular Region Breakdown**:
  - *Navigation Chrome*: Fixed/floating status, logo placement, desktop navigation links, mobile hamburger drawer, and CTAs.
  - *Hero Section*: Viewport framing, headline hierarchy, optical background media, and primary interaction triggers.
  - *Content / Showcase Architecture*: Product/editorial grids, filter mechanics, multi-pane viewports, and tabbed inspectors.
  - *Interactive Flyouts & Drawers*: Cart drawers, technical detail modals, filter panels, or telemetry HUDs.
  - *Footer Architecture*: Multi-column links, newsletter captures, copyright/colophon annotations, and secondary status indicators.

### 7. Master Zero-Shot AI Generation Prompt
- A fully self-contained, copy-pasteable prompt block (`>= 80 lines`) formatted in Markdown code fence (`markdown`).
- Engineered for direct execution by any code generation agent (e.g., Claude 3.5/3.7, GPT-4o, Gemini 1.5/2.0) to scaffold a complete, pixel-perfect frontend using modern web stacks (React / Next.js / Tailwind CSS / Framer Motion / Lucide / Three.js).
- Contains embedded design tokens, CSS utility classes, component contracts, responsive directives, and animation specifications.

---

## Assets & Directory Conventions

For every target `<slug>` in `fleet/wiki/targets/<slug>/`:
```
fleet/wiki/targets/<slug>/
├── overview.md              # Target overview, metadata, and core architecture
├── apis.md                  # Network endpoints, payloads, and external dependencies
├── data-models.md           # Entity schemas, state trees, and storage schemas
├── ui-ux.md                 # Raw CSS variables and layout primitives
├── source-maps.md           # Reverse-engineered bundles, packages, and frameworks
├── prompt-blueprint.md      # The 7-part AI Prompt Blueprint authored via this skill
└── assets/                  # High-resolution visual captures
    ├── desktop.png          # Full desktop viewport capture (1440px wide)
    └── mobile.png           # Mobile viewport capture (390px wide)
```
