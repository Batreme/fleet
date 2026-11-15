---
title: "UI Prompt Blueprint: wiro-ae"
date: 2026-11-15
target: "wiro-ae"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Warm-Paper Tactile SaaS Operating System & Scatter-Card Workspace (`Bricolage Grotesque` + `DM Sans`)"
---

# UI Design System & Master Generation Blueprint: wiro-ae

> **Wiro · Operating System for All Agencies** — An inventive agency operating system interface built on a warm cream paper canvas (`--wiro-canvas: #f6efe3`), deep charcoal ink (`--wiro-ink: #10100f`), and tactile pastel workspace accents (`--wiro-pink: #efacd4`, `--wiro-yellow: #f6d94e`, `--wiro-sage: #9caf63`, `--wiro-blue: #a9c5e9`).

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Wiro · Operating System for All Agencies**. An inventive agency operating system interface built on a warm cream paper canvas (`--wiro-canvas: #f6efe3`), deep charcoal ink (`--wiro-ink: #10100f`), and tactile pastel workspace accents (`--wiro-pink: #efacd4`, `--wiro-yellow: #f6d94e`, `--wiro-sage: #9caf63`, `--wiro-blue: #a9c5e9`).
- **Visual Archetype**: **Warm-Paper Tactile SaaS Operating System & Scatter-Card Workspace (`Bricolage Grotesque` + `DM Sans`)**.
- **Anti-AI-Slop Differentiators**:
  1. **Warm Cream Paper Substrate (`--wiro-canvas**: #f6efe3`)**: Rejects sterile white or dark-mode SaaS clichés in favor of a tactile paper canvas (`#f6efe3`) with stepped warm stone surfaces (`--wiro-surface-2: #ece5da`, `#fffdf8`).
  2. **Color-Coded Agency OS Modules**: Maps core agency workflows (`H3: Projects`, `H3: Clients`, `H3: Finance`) to distinct pastel workspace tokens (`--wiro-pink: #efacd4`, `--wiro-yellow: #f6d94e`, `--wiro-sage: #9caf63`, `--wiro-blue: #a9c5e9`).
  3. **Interactive Scatter-Card Physics (`nav.lp-scatter`, `footer.lp-footer-scatter`)**: Floating agency artifact cards and module tabs arranged around the central workspace viewport (`section.lp-hero`).
  4. **Expressive Display Grotesque Pairing**: Pairs `--font-heading: "Bricolage Grotesque"` for charismatic headlines (`"Organize Your Chaos"`) with `--font-ui: "DM Sans"` and `2.5px` solar icon strokes (`--solar-stroke-width: 2.5`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Full-Page Dimensions**: Desktop `1440×7497px` (`assets/desktop.png`), Mobile `390×8396px` (`assets/mobile.png`).
- **Master Container Bounds**: 1536px (`@media (min-width:1536px)`) with central OS stage max-width `1280px`.
- **Canvas Lateral Padding & Spacing**: Desktop `clamp(24px, 4vw, 56px)`, mobile `16px` below `@media (max-width:900px)`.
- **Border Radius Scale**: `--wiro-radius-lg: 18px` for primary OS window frames, `--wiro-radius-md: 12px` for module cards and pills.

### Responsive Breakpoint Architecture
- **Desktop Layout**: 12-column SaaS showcase grid with 3-column feature bento (`Projects`, `Clients`, `Finance`) in `<section id="pages" class="lp-section lp-pages">`.
- **Mobile Layout**: Single-column stack below `@media (max-width:900px)` and `@media (min-width:768px)`, collapsing `.lp-scatter` floating cards into an inline grid.
- **Extracted CSS Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (max-width:900px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`, `@media (min-width:1536px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| Primary Warm Paper Canvas | `#f6efe3` | `--wiro-canvas` / `--wiro-surface` (`:root`) |
| Secondary Recessed Surface | `#ece5da` | `--wiro-surface-2` (`:root`) |
| Elevated Paper Sheet | `#fffdf8` | Card surface hex in stylesheet (`#fffdf8`) |
| Primary Charcoal Ink | `#10100f` | `--wiro-ink` (`:root`) |
| Muted Secondary Ink | `rgba(16,16,15,.52)` | `--wiro-muted` (`:root`) |
| Subtle Hairline Border | `rgba(16,16,15,.12)` | `--wiro-border` (`:root`) |
| Projects Module Pink | `#efacd4` | `--wiro-pink` (`:root`) |
| Finance Module Yellow | `#f6d94e` | `--wiro-yellow` (`:root`) |
| Clients Module Sage | `#9caf63` | `--wiro-sage` (`:root`) |
| Operations Module Blue | `#a9c5e9` | `--wiro-blue` (`:root`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-heading` | `var(--font-bricolage),"Bricolage Grotesque",sans-serif` | Primary display heading font stack |
| `--font-ui` | `var(--font-dmsans),"DM Sans",Arial,Helvetica,sans-serif` | UI controls & body copy font stack |
| `--solar-stroke-width` | `2.5` | Custom stroke weight for vector UI icons |
| `--wiro-ink` | `#10100f` | Primary deep charcoal ink |
| `--wiro-muted` | `rgba(16,16,15,.52)` | Muted label & description ink |
| `--wiro-canvas` | `#f6efe3` | Warm paper viewport canvas |
| `--wiro-surface` | `#f6efe3` | Primary container surface |
| `--wiro-surface-2` | `#ece5da` | Secondary recessed bento card surface |
| `--wiro-border` | `rgba(16,16,15,.12)` | 1px structural card & table border |
| `--wiro-pink` | `#efacd4` | Pastel pink accent for Projects module |
| `--wiro-yellow` | `#f6d94e` | Warm yellow accent for Finance module |
| `--wiro-sage` | `#9caf63` | Sage green accent for Clients module |
| `--wiro-blue` | `#a9c5e9` | Sky blue accent for Team/Docs module |
| `--wiro-radius-lg` | `18px` | Outer OS window & section border radius |
| `--wiro-radius-md` | `12px` | Inner card & button border radius |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `"Bricolage Grotesque", sans-serif` (`--font-heading`).
- **Primary Body Stack**: `"DM Sans", Arial, Helvetica, sans-serif` (`--font-ui`).
- **Technical / Metadata Stack**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace` (KPI counters, invoice IDs, keyboard shortcuts).

### Typographic Scale & Rules
- **Hero Display (`H1`)**: `clamp(2.75rem, 6vw, 5.25rem)`, `font-family: var(--font-heading)`, `font-weight: 700`, `line-height: 0.98`, `letter-spacing: -0.03em` ("Organize Your Chaos").
- **Section Heading (`H2`)**: `clamp(1.75rem, 3.5vw, 3rem)`, `font-family: var(--font-heading)`, `font-weight: 600`, `line-height: 1.1` ("One system for every page your agency runs.").
- **Body Copy**: `1rem (16px)`, `font-family: var(--font-ui)`, `line-height: 1.6`, `color: var(--wiro-muted)`.
- **Metadata & Navigation Labels**: `0.8125rem (13px)`, `font-family: var(--font-ui)`, `font-weight: 600`, pill badges colored with `--wiro-pink`, `--wiro-yellow`, `--wiro-sage`, `--wiro-blue`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,1,0.36,1)` (smooth quintic out) and `cubic-bezier(0.55,0,0.75,0.2)`.

### Per-Element Transition & Choreography Rules
- `.lp-scatter` floating cards -> `transition: transform 400ms cubic-bezier(0.22,1,0.36,1)` (interactive hover lift & tilt)
- `Tab switcher in section#pages.lp-pages` -> `cubic-bezier(.4,0,.2,1)` (`250ms` active pill morph)
- `Waitlist CTA button` -> `transition: background-color 200ms cubic-bezier(0,0,.2,1), transform 200ms`

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ <nav class="lj-bar-links"> [Wiro]     [Pages] [OS Preview] [Join Waitl │
├────────────────────────────────────────────────────────────────────────┤
│ <main class="lp-page"> <section class="lp-hero"> (Canvas: #f6efe3)     │
│   H1: Organize Your Chaos                                              │
│   <nav class="lp-scatter"> [Pink: Projects] [Sage: Clients] [Yellow: F │
├────────────────────────────────────────────────────────────────────────┤
│ <section id="pages" class="lp-section lp-pages"> (Radius: 18px)        │
│   H2: One system for every page your agency runs.                      │
│   [ H3: Projects (#efacd4) ] [ H3: Clients (#9caf63) ] [ H3: Finance ] │
├────────────────────────────────────────────────────────────────────────┤
│ <section id="waitlist" class="lp-section lp-waitlist"> [Early Access F │
├────────────────────────────────────────────────────────────────────────┤
│ <footer class="lp-footer lp-footer-scatter"> © Wiro Agency OS          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Top Bar Navigation (`<nav class="lj-bar-links">`)**:
   - Floating pill bar on `--wiro-canvas: #f6efe3` with `1px solid var(--wiro-border)` linking `#pages`, `#waitlist`, and workspace login.
2. **Hero Stage & Scatter Cards (`<section class="lp-hero">` and `<nav class="lp-scatter">`)**:
   - Centers `H1: Organize Your Chaos` in `--font-heading` surrounded by interactive `.lp-scatter` cards color-coded with `--wiro-pink: #efacd4`, `--wiro-yellow: #f6d94e`, `--wiro-sage: #9caf63`, and `--wiro-blue: #a9c5e9`.
3. **Interactive Agency Pages Bento (`<section id="pages" class="lp-section lp-pages">`)**:
   - Anchored by `H2: One system for every page your agency runs.`, showcasing live interactive previews of `H3: Projects`, `H3: Clients`, and `H3: Finance` inside `--wiro-radius-lg: 18px` frames on `#fffdf8` sheets.
4. **Waitlist Conversion Module (`<section id="waitlist" class="lp-section lp-waitlist">`)**:
   - High-contrast onboarding capture card on `--wiro-surface-2: #ece5da` with `--wiro-radius-md: 12px` inputs and `--wiro-ink: #10100f` submit button.
5. **Scatter Footer (`<footer class="lp-footer lp-footer-scatter">`)**:
   - Playful footer with scattered agency module badges and colophon links.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: wiro-ae (Wiro · Operating System for All Agencies)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `wiro-ae` (Wiro · Operating System for All Agencies).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Warm-Paper Tactile SaaS Operating System & Scatter-Card Workspace (`Bricolage Grotesque` + `DM Sans`).
- **Primary Substrate**: `#f6efe3` (`--wiro-canvas` / `--wiro-surface` (`:root`)), **Primary Ink**: `#10100f`, **Accent / Highlight**: `#a9c5e9`.
- **Site-Specific Differentiators**:
  1. **Warm Cream Paper Substrate (`--wiro-canvas**: #f6efe3`)**: Rejects sterile white or dark-mode SaaS clichés in favor of a tactile paper canvas (`#f6efe3`) with stepped warm stone surfaces (`--wiro-surface-2: #ece5da`, `#fffdf8`).
  2. **Color-Coded Agency OS Modules**: Maps core agency workflows (`H3: Projects`, `H3: Clients`, `H3: Finance`) to distinct pastel workspace tokens (`--wiro-pink: #efacd4`, `--wiro-yellow: #f6d94e`, `--wiro-sage: #9caf63`, `--wiro-blue: #a9c5e9`).
  3. **Interactive Scatter-Card Physics (`nav.lp-scatter`, `footer.lp-footer-scatter`)**: Floating agency artifact cards and module tabs arranged around the central workspace viewport (`section.lp-hero`).
  4. **Expressive Display Grotesque Pairing**: Pairs `--font-heading: "Bricolage Grotesque"` for charismatic headlines (`"Organize Your Chaos"`) with `--font-ui: "DM Sans"` and `2.5px` solar icon strokes (`--solar-stroke-width: 2.5`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `wiro-ae` in your global stylesheet:

:root {
  /* Wiro · Operating System for All Agencies — Ground-Truth Extracted CSS Variables */
  --font-heading: var(--font-bricolage),"Bricolage Grotesque",sans-serif; /* Primary display heading font stack */
  --font-ui: var(--font-dmsans),"DM Sans",Arial,Helvetica,sans-serif; /* UI controls & body copy font stack */
  --solar-stroke-width: 2.5; /* Custom stroke weight for vector UI icons */
  --wiro-ink: #10100f; /* Primary deep charcoal ink */
  --wiro-muted: rgba(16,16,15,.52); /* Muted label & description ink */
  --wiro-canvas: #f6efe3; /* Warm paper viewport canvas */
  --wiro-surface: #f6efe3; /* Primary container surface */
  --wiro-surface-2: #ece5da; /* Secondary recessed bento card surface */
  --wiro-border: rgba(16,16,15,.12); /* 1px structural card & table border */
  --wiro-pink: #efacd4; /* Pastel pink accent for Projects module */
  --wiro-yellow: #f6d94e; /* Warm yellow accent for Finance module */
  --wiro-sage: #9caf63; /* Sage green accent for Clients module */
  --wiro-blue: #a9c5e9; /* Sky blue accent for Team/Docs module */
  --wiro-radius-lg: 18px; /* Outer OS window & section border radius */
  --wiro-radius-md: 12px; /* Inner card & button border radius */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Warm Paper Canvas**: `#f6efe3` — grounded in `--wiro-canvas` / `--wiro-surface` (`:root`)
- **Secondary Recessed Surface**: `#ece5da` — grounded in `--wiro-surface-2` (`:root`)
- **Elevated Paper Sheet**: `#fffdf8` — grounded in Card surface hex in stylesheet (`#fffdf8`)
- **Primary Charcoal Ink**: `#10100f` — grounded in `--wiro-ink` (`:root`)
- **Muted Secondary Ink**: `rgba(16,16,15,.52)` — grounded in `--wiro-muted` (`:root`)
- **Subtle Hairline Border**: `rgba(16,16,15,.12)` — grounded in `--wiro-border` (`:root`)
- **Projects Module Pink**: `#efacd4` — grounded in `--wiro-pink` (`:root`)
- **Finance Module Yellow**: `#f6d94e` — grounded in `--wiro-yellow` (`:root`)
- **Clients Module Sage**: `#9caf63` — grounded in `--wiro-sage` (`:root`)
- **Operations Module Blue**: `#a9c5e9` — grounded in `--wiro-blue` (`:root`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7497px` full-page capture (`1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×8396px` full-page capture (`390px` standard mobile width).
- **Container Max-Width**: 1536px (`@media (min-width:1536px)`) with central OS stage max-width `1280px`
- **Padding & Gutters**: Desktop `clamp(24px, 4vw, 56px)`, mobile `16px` below `@media (max-width:900px)`
- **Desktop Grid**: 12-column SaaS showcase grid with 3-column feature bento (`Projects`, `Clients`, `Finance`) in `<section id="pages" class="lp-section lp-pages">`
- **Mobile Adaptation**: Single-column stack below `@media (max-width:900px)` and `@media (min-width:768px)`, collapsing `.lp-scatter` floating cards into an inline grid
- **Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (max-width:900px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`, `@media (min-width:1536px)`
- **Corner Radii**: `--wiro-radius-lg: 18px` for primary OS window frames, `--wiro-radius-md: 12px` for module cards and pills

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `"Bricolage Grotesque", sans-serif` (`--font-heading`)
- **Body Font Stack**: `"DM Sans", Arial, Helvetica, sans-serif` (`--font-ui`)
- **Monospace / Technical Font Stack**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace` (KPI counters, invoice IDs, keyboard shortcuts)
- **H1 Display Rule**: `clamp(2.75rem, 6vw, 5.25rem)`, `font-family: var(--font-heading)`, `font-weight: 700`, `line-height: 0.98`, `letter-spacing: -0.03em` ("Organize Your Chaos")
- **H2 Section Rule**: `clamp(1.75rem, 3.5vw, 3rem)`, `font-family: var(--font-heading)`, `font-weight: 600`, `line-height: 1.1` ("One system for every page your agency runs.")
- **Body Copy Rule**: `1rem (16px)`, `font-family: var(--font-ui)`, `line-height: 1.6`, `color: var(--wiro-muted)`
- **Metadata & Index Rule**: `0.8125rem (13px)`, `font-family: var(--font-ui)`, `font-weight: 600`, pill badges colored with `--wiro-pink`, `--wiro-yellow`, `--wiro-sage`, `--wiro-blue`

### 6. Component Hierarchy & Real DOM Landmarks
Scaffold the interface with these exact structural regions and class selectors from `wiro-ae`:
1. **Top Bar Navigation (`<nav class="lj-bar-links">`)**:
   - Architecture & Selectors: Floating pill bar on `--wiro-canvas: #f6efe3` with `1px solid var(--wiro-border)` linking `#pages`, `#waitlist`, and workspace login.
   - Layout & State Contract: Sticky/fixed top header navigation adapting across `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (max-width:900px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`, `@media (min-width:1536px)` with `cubic-bezier(0.22,1,0.36,1)` (smooth quintic out) and `cubic-bezier(0.55,0,0.75,0.2)` menu transitions.
2. **Hero Stage & Scatter Cards (`<section class="lp-hero">` and `<nav class="lp-scatter">`)**:
   - Architecture & Selectors: Centers `H1: Organize Your Chaos` in `--font-heading` surrounded by interactive `.lp-scatter` cards color-coded with `--wiro-pink: #efacd4`, `--wiro-yellow: #f6d94e`, `--wiro-sage: #9caf63`, and `--wiro-blue: #a9c5e9`.
   - Layout & State Contract: Full-viewport hero stage (`1440px` desktop / `390px` mobile) pairing `#f6efe3` substrate with `#10100f` display typography (`H1`).
3. **Interactive Agency Pages Bento (`<section id="pages" class="lp-section lp-pages">`)**:
   - Architecture & Selectors: Anchored by `H2: One system for every page your agency runs.`, showcasing live interactive previews of `H3: Projects`, `H3: Clients`, and `H3: Finance` inside `--wiro-radius-lg: 18px` frames on `#fffdf8` sheets.
   - Layout & State Contract: Primary showcase grid executing 12-column SaaS showcase grid with 3-column feature bento (`Projects`, `Clients`, `Finance`) in `<section id="pages" class="lp-section lp-pages">` on desktop and Single-column stack below `@media (max-width:900px)` and `@media (min-width:768px)`, collapsing `.lp-scatter` floating cards into an inline grid on mobile.
4. **Waitlist Conversion Module (`<section id="waitlist" class="lp-section lp-waitlist">`)**:
   - Architecture & Selectors: High-contrast onboarding capture card on `--wiro-surface-2: #ece5da` with `--wiro-radius-md: 12px` inputs and `--wiro-ink: #10100f` submit button.
   - Layout & State Contract: Interactive specification & narrative module framed by `--wiro-radius-lg: 18px` for primary OS window frames, `--wiro-radius-md: 12px` for module cards and pills and `#a9c5e9` highlights.
5. **Scatter Footer (`<footer class="lp-footer lp-footer-scatter">`)**:
   - Architecture & Selectors: Playful footer with scattered agency module badges and colophon links.
   - Layout & State Contract: Footer directory and utility bar anchored to 1536px (`@media (min-width:1536px)`) with central OS stage max-width `1280px` with Desktop `clamp(24px, 4vw, 56px)`, mobile `16px` below `@media (max-width:900px)` lateral gutters.

### 7. Motion & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,1,0.36,1)` (smooth quintic out) and `cubic-bezier(0.55,0,0.75,0.2)`
- **Per-Selector Transition Rules**:
- `.lp-scatter` floating cards -> `transition: transform 400ms cubic-bezier(0.22,1,0.36,1)` (interactive hover lift & tilt)
- `Tab switcher in section#pages.lp-pages` -> `cubic-bezier(.4,0,.2,1)` (`250ms` active pill morph)
- `Waitlist CTA button` -> `transition: background-color 200ms cubic-bezier(0,0,.2,1), transform 200ms`

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
