# UI & UX Architecture: brand-helloasso-com

## Overview & Design Identity
- **Target**: `brand-helloasso-com` (**Accueil – Brandbook HelloAsso**)
- **Production URL**: [https://brand.helloasso.com/](https://brand.helloasso.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#cdced0`)
- **Summary**: Logotype, typographie, couleurs, direction photographique et identité verbale de HelloAsso.
- **Total Clean CSS Variables Extracted**: `262` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ITC Franklin Gothic LT`
- **Body Font Stack**: `ABC Diatype Rounded`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: "ITC Franklin Gothic LT", "Arial Narrow", sans-serif`, `--fs-h1: 64px`, `--lh-h1: 58px`
- **Section Heading (`H2`)**: CSS variables `--fs-h2: 48px`, `--lh-h2: 43px`
- **Body Copy**: CSS variables `--fs-body: 14px`, `--lh-body: 18px`, `--fs-body-s: 14px`
- **Metadata & Labels**: CSS variables `--fs-caption: 12px`, `--lh-caption: 17px`, `--caption-gap: var(--space-12)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#101010` | `var(--color-noir)` in `:root` |
| **Primary Typography Ink** | `#434649` | `var(--color-gris-fonce)` in `:root` |
| **Elevated Surface / Card Substrate** | `#888c8f` | `var(--color-gris)` in `:root` |
| **Interactive Accent / Highlight** | `#cdced0` | `var(--color-gris-clair)` in `:root` |
| **Secondary / Muted Copy** | `#f5f5f5` | `var(--color-gris-tres-clair)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--color-blanc)` in `:root` |
| **Variable Token (`--color-vert`)** | `#4a8100` | `var(--color-vert)` in `:root` |
| **Variable Token (`--color-vanille`)** | `#fdffc6` | `var(--color-vanille)` in `:root` |
| **Variable Token (`--color-rose`)** | `#fba2ec` | `var(--color-rose)` in `:root` |
| **Variable Token (`--color-sahara`)** | `#b38806` | `var(--color-sahara)` in `:root` |
| **Variable Token (`--color-lila`)** | `#f1edff` | `var(--color-lila)` in `:root` |
| **Variable Token (`--color-cuir`)** | `#644a02` | `var(--color-cuir)` in `:root` |
| **Variable Token (`--color-prune`)** | `#572a37` | `var(--color-prune)` in `:root` |
| **Variable Token (`--color-sport-jaune-fluo`)** | `#d7e103` | `var(--color-sport-jaune-fluo)` in `:root` |
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
   - Landmark `<header class="is-ready">` hosting `Accueil – Brandbook HelloAsso` navigation (`BRUNO`), DOM attributes (`data-astro-transition-scope="astro-nfpogox7-1"`, `data-layout="fullscreen"`, `data-astro-exec`, `data-svg-origin="24 512"`), and stylesheet rule `root { --fs-h1:var(--fs-h2);--lh-h1:var(--lh-h2) }`.
2. **Hero Stage & Focal Lead (<section.chapter> — `Accueil – Brandbook HelloAsso`)**:
   - Landmark `<section class="chapter">` presenting display lead `Accueil – Brandbook HelloAsso` and copy excerpt *"L’engagement rend les gens meilleurs."* over `#101010` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.chapter> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="chapter">` rendering section `Featured Work & Interactive Showcase` with copy *"Accueil – Brandbook HelloAsso"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `ITCFranklinGothicLT-DemiCompresse...`), and grid rule `after { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.chapter> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="chapter">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#888c8f` surface cards, `#cdced0` accents, and `svg { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.cell-border> — `https://brand.helloasso.com/`)**:
   - Landmark `<footer class="cell-border">` anchoring `Accueil – Brandbook HelloAsso` footer links (`BRUNO`), copy *"Technical Architecture & Narrative"*, and `#fff` structural dividers.
