# UI & UX Architecture: effepinnastudio-com

## Overview & Design Identity
- **Target**: `effepinnastudio-com` (**Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio**)
- **Production URL**: [https://effepinnastudio.com/](https://effepinnastudio.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#ef233c` / `#ee2c3d`)
- **Summary**: Direzione artistica, progettazione grafica e produzione di immagini, video e animazioni per agenzie e brand. Fabio Pinna, freelance a Gra...
- **Total Clean CSS Variables Extracted**: `95` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `clamp(34px`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--type-display: 6rem`, `--leading-display: 6.25rem`; rule `h1` (`font-size: 2rem`, `line-height: 2.25rem`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--type-section)`, `line-height: var(--leading-section)`, `font-weight: var(--weight-...`)
- **Body Copy**: CSS variables `--type-body: 1.125rem`, `--leading-body: 1.75rem`, `--space-paragraph: 1.5rem`; rule `p` (`font-size: var(--type-block)`, `line-height: var(--leading-block)`, `font-weight: var(--weight-...`)
- **Metadata & Labels**: CSS variables `--weight-label: 500`, `--type-meta: .875rem`, `--leading-meta: 1.25rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ef233c` | `var(--red)` in `:root` |
| **Primary Typography Ink** | `#f3f2ef` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0a0a0a` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#ee2c3d` | `var(--menu-background)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--menu-foreground)` in `:root` |
| **Structural Hairline Border** | `#fdc400` | `var(--work-hover-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--red` | `#ef233c` | Color / Atmospheric Token |
| `--paper` | `#f3f2ef` | Canvas / Surface Token |
| `--ink` | `#0a0a0a` | Typography Ink Token |
| `--menu-background` | `#ee2c3d` | Canvas / Surface Token |
| `--menu-foreground` | `#fff` | Typography Ink Token |
| `--menu-pixel-color` | `#ee2c3d` | Brand / Palette Token |
| `--menu-button-background` | `#ee2c3d` | Canvas / Surface Token |
| `--menu-button-foreground` | `#fff` | Typography Ink Token |
| `--menu-button-open-background` | `#fff` | Canvas / Surface Token |
| `--menu-button-open-foreground` | `#ee2c3d` | Typography Ink Token |
| `--loader-mask-size` | `220px` | Layout / Spatial Grid Token |
| `--ragdoll-hint-x` | `0px` | Dimension / Scale Token |
| `--ragdoll-hint-y` | `0px` | Dimension / Scale Token |
| `--manifesto-progress` | `0` | Design System Custom Token |
| `--path-opacity` | `.9` | Design System Custom Token |
| `--audiences-progress` | `0` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero> — `effepinnastudio-com`)**:
   - Landmark `<header class="hero">` hosting `Fabio Pinna — Art Director e Graphic` navigation (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), DOM attributes (`data-work-preview-loading="true"`, `data-loading-theme="red"`, `data-loading-state="ready"`, `data-font-status="instrument-sans"`), and stylesheet rule `root { color-scheme: light;--red: ef233c;--paper: f3f2ef;--ink: 0a0a0a; }`.
2. **Hero Stage & Focal Lead (<section.manifesto> — `Fabio Pinna - Art Direction, Multi`)**:
   - Landmark `<section class="manifesto editorial-grid">` presenting display lead `Fabio Pinna - Art Direction, Multimedia Graphic D...` and copy excerpt *"DISPONIBILE PER COLLABORAZIONI FREELANCE."* over `#ef233c` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.work> — `Selezione Lavori`)**:
   - Landmark `<section class="work">` rendering section `Selezione Lavori` with copy *"Generative AI Production"*, asset references (`motion-policy-20261012.js`, `favicon-192.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `body { touch-action: manipulation;touch-action: pan-x pan-y; }`.
4. **Interactive Detail & Feature Matrix (<article.work-row> — `Fastweb Tu sei Futuro`)**:
   - Landmark `<article class="work-row">` framing `Fastweb Tu sei Futuro` and `Divoora` (*"Mi occupo di direzione artistica e graphic design multimediale. M"*) with `#0a0a0a` surface cards, `#ee2c3d` accents, and `focus-visible { outline: 2px solid currentColor;outline-offset: 4px; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://effepinnastudio.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Fabio Pinna — Art Director e Gra` footer links (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), copy *"Mi occupo di direzione artistica e graphic design multimedia"*, and `#fdc400` structural dividers.
