---
title: "UI & UX Architecture: brand-helloasso-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: brand-helloasso-com

## Overview & Design Identity
- **Target**: `brand-helloasso-com` (**Accueil – Brandbook HelloAsso**)
- **Production URL**: [https://brand.helloasso.com/](https://brand.helloasso.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#d7e103`)
- **Summary**: Logotype, typographie, couleurs, direction photographique et identité verbale de HelloAsso.
- **Total Clean CSS Variables Extracted**: `262` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ITC Franklin Gothic LT`
- **Body Font Stack**: `ABC Diatype Rounded`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: "ITC Franklin Gothic LT", "Arial Narrow", sans-serif`, `--fs-h1: 64px`, `--lh-h1: 58px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 132px`, `line-height: 118.8px`, `font-weight: 700`, `letter-spacing: -1.32px`); CSS variables `--fs-h2: 48px`, `--lh-h2: 43px`
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 18px`, `font-weight: 400`); CSS variables `--fs-body: 14px`, `--lh-body: 18px`, `--fs-body-s: 14px`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: 14.3px`, `font-weight: 400`); CSS variables `--fs-caption: 12px`, `--lh-caption: 17px`, `--caption-gap: var(--space-12)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#101010` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ededed` | `var(--tools-surface-hover)` in `:root` |
| **Interactive Accent / Highlight** | `#d7e103` | `var(--color-sport-jaune-fluo)` in `:root` |
| **Secondary / Muted Copy** | `#878787` | `var(--color-placeholder)` in `:root` |
| **Structural Hairline Border** | `#e7e7e7` | `var(--tools-line)` in `:root` |
| **Variable Token (`--color-gris-fonce`)** | `#434649` | `var(--color-gris-fonce)` in `:root` |
| **Variable Token (`--color-gris`)** | `#888c8f` | `var(--color-gris)` in `:root` |
| **Variable Token (`--color-gris-clair`)** | `#cdced0` | `var(--color-gris-clair)` in `:root` |
| **Variable Token (`--color-gris-tres-clair`)** | `#f5f5f5` | `var(--color-gris-tres-clair)` in `:root` |
| **Variable Token (`--color-vert`)** | `#4a8100` | `var(--color-vert)` in `:root` |
| **Variable Token (`--color-vanille`)** | `#fdffc6` | `var(--color-vanille)` in `:root` |
| **Variable Token (`--color-rose`)** | `#fba2ec` | `var(--color-rose)` in `:root` |
| **Variable Token (`--color-sahara`)** | `#b38806` | `var(--color-sahara)` in `:root` |
| **Variable Token (`--color-lila`)** | `#f1edff` | `var(--color-lila)` in `:root` |
| **Variable Token (`--color-cuir`)** | `#644a02` | `var(--color-cuir)` in `:root` |
| **Variable Token (`--color-prune`)** | `#572a37` | `var(--color-prune)` in `:root` |
| **Variable Token (`--color-sport-logo-fond-clair`)** | `#c6cf0e` | `var(--color-sport-logo-fond-clair)` in `:root` |
| **Variable Token (`--color-sport-anthracite`)** | `#504e44` | `var(--color-sport-anthracite)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-noir` | `#101010` | Brand / Palette Token |
| `--color-gris-fonce` | `#434649` | Brand / Palette Token |
| `--color-gris` | `#888c8f` | Brand / Palette Token |
| `--color-gris-clair` | `#cdced0` | Brand / Palette Token |
| `--color-gris-tres-clair` | `#f5f5f5` | Brand / Palette Token |
| `--color-blanc` | `#fff` | Brand / Palette Token |
| `--color-vert` | `#4a8100` | Brand / Palette Token |
| `--color-vanille` | `#fdffc6` | Brand / Palette Token |
| `--color-rose` | `#fba2ec` | Brand / Palette Token |
| `--color-sahara` | `#b38806` | Brand / Palette Token |
| `--color-lila` | `#f1edff` | Brand / Palette Token |
| `--color-cuir` | `#644a02` | Brand / Palette Token |
| `--color-prune` | `#572a37` | Brand / Palette Token |
| `--color-sport-jaune-fluo` | `#d7e103` | Brand / Palette Token |
| `--color-sport-logo-fond-clair` | `#c6cf0e` | Brand / Palette Token |
| `--color-sport-anthracite` | `#504e44` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.is-ready> — `brand-helloasso-com`)**:
   - Landmark `<header class="is-ready">` (`1440px`) hosting `Accueil – Brandbook HelloAsso` navigation (`BRUNO`), DOM attributes (`data-astro-transition-scope="astro-nfpogox7-1"`, `data-layout="fullscreen"`, `data-astro-exec`, `data-svg-origin="24 512"`), and stylesheet rule `body { background:var(--blanc);color:var(--noir);font-family:var(--ff-ui) }`.
2. **Hero Stage & Focal Lead (<section.chapter> — `Accueil – Brandbook HelloAsso`)**:
   - Landmark `<section class="chapter">` presenting display lead `Accueil – Brandbook HelloAsso` and copy excerpt *"L’ENGAGEMENT REND LES GENS MEILLEURS."* over `#ffffff` canvas and `#101010` ink.
3. **Primary Showcase & Content Grid (<section.chapter:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="chapter">` rendering section `Featured Work & Interactive Showcase` with copy *"L’engagement rend les gens meilleurs."*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `ITCFranklinGothicLT-DemiCompresse...`), and grid rule `.cursor { will-change:transform;display:none }`.
4. **Interactive Detail & Feature Matrix (<section.chapter:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="chapter">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#ededed` surface cards, `#d7e103` accents, and `.scroller { height:620vh;position:relative }`.
5. **Colophon & Global Directory Footer (<footer.cell-border> — `https://brand.helloasso.com/`)**:
   - Landmark `<footer class="cell-border">` anchoring `Accueil – Brandbook HelloAsso` footer links (`BRUNO`), copy *"Technical Architecture & Narrative"*, and `#e7e7e7` structural dividers.
