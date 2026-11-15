# UI & UX Architecture: departmentofemotions-com

## Overview & Design Identity
- **Target**: `departmentofemotions-com` (**Department of Emotions**)
- **Production URL**: [https://departmentofemotions.com/](https://departmentofemotions.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#212c24` canvas, `#fff` ink, `#e2e7db` accent)
- **Summary**: Explore your emotions with an interactive feeling wheel, body-language examples, somatic sensations, and behavioral experiences.
- **Total Clean CSS Variables Extracted**: `11` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gilda Display`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 48px`, `line-height: 1.12`, `letter-spacing: -.6px`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 11px`, `letter-spacing: 1.4px`)
- **Body Copy**: rule `p` (`font-size: 14px`, `line-height: 1.7`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `11px`, `10px`, `46px`, `48px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#212c24` | `.privacy-page { color: #212c24 }` |
| **Primary Typography Ink** | `#fff` | `html { background: #fff }` |
| **Elevated Surface / Card Substrate** | `#33443a` | `.explorer-loading { color: #33443a }` |
| **Interactive Accent / Highlight** | `#e2e7db` | `.explorer-page button:focus-vis... { background: #e2e7db }` |
| **Secondary / Muted Copy** | `#6f7f74` | `.explorer-page button:focus-vis... { border-color: #6f7f74 }` |
| **Structural Hairline Border** | `#292929` | `.explorer-label { fill: #292929 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `oklch(28% .022 154)` | Typography Ink Token |
| `--muted` | `oklch(49% .016 154)` | Color / Atmospheric Token |
| `--line` | `oklch(86% .012 125)` | Color / Atmospheric Token |
| `--paper` | `oklch(98% .008 105)` | Canvas / Surface Token |
| `--desktop-wheel-size` | `clamp(74vw, 120svh, 92vw)` | Layout / Spatial Grid Token |
| `--mobile-wheel-size` | `min(160vw, 820px)` | Layout / Spatial Grid Token |
| `--landscape-wheel-size` | `clamp(560px, 160svh, 92vw)` | Layout / Spatial Grid Token |
| `--lab-toolbar-height` | `0px` | Layout / Spatial Grid Token |
| `--phone-wheel-size` | `213.75vw` | Layout / Spatial Grid Token |
| `--wheel-muted-opacity` | `0.38` | Design System Custom Token |
| `--wheel-fade-duration` | `180ms` | Motion / Easing Token |
| `--departmentofemot-bg` | `#212c24` | Canvas Substrate (from `.privacy-page { color: #212c24 }`) |
| `--departmentofemot-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--departmentofemot-surface` | `#33443a` | Surface Substrate (stylesheet-derived) |
| `--departmentofemot-accent` | `#e2e7db` | Interactive Accent (stylesheet-derived) |
| `--departmentofemot-muted` | `#6f7f74` | Secondary Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lab-switcher> — `departmentofemotions-com`)**:
   - Landmark `<nav class="lab-switcher">` hosting `Department of Emotions` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wheel="feelings"`, `data-moving="false"`, `data-sector-index="0"`, `data-emotion="Anger"`), and stylesheet rule `.privacy-page { max-width:648px;margin-inline:auto;padding:64px 24px;color:212c24;font:1... }`.
2. **Hero Stage & Focal Lead (<section.explorer-page> — `Isolated`)**:
   - Landmark `<section class="explorer-page">` presenting display lead `Isolated` and copy excerpt *"Skip to the emotion explorer"* over `#212c24` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.wheel-workspace> — `How it may feel in the body`)**:
   - Landmark `<section class="wheel-workspace">` rendering section `How it may feel in the body` with copy *"Feeling separated from other people or unable to take part in a s"*, asset references (`favicon.ico`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.privacy-brand { display:inline-flex;align-items:center;gap:5px;font-weight:650;font-size... }`.
4. **Interactive Detail & Feature Matrix (<section.experience-section> — `Possible body language & behaviors`)**:
   - Landmark `<section class="experience-section">` framing `Possible body language & behaviors` and `01 An empty or constricted feeling in the chest.` (*"01 An empty or constricted feeling in the chest."*) with `#33443a` surface cards, `#e2e7db` accents, and `.privacy-page h1 { margin:40px 0 24px;font:400 42px/1.2 Gilda Display,Georgia,serif }`.
5. **Colophon & Global Directory Footer (<footer.sidebar-footer> — `https://departmentofemotions.com/`)**:
   - Landmark `<footer class="sidebar-footer">` anchoring `Department of Emotions` footer links (`Overview · Index · Archive · About · Contact`), copy *"An empty or constricted feeling in the chest."*, and `#292929` structural dividers.
