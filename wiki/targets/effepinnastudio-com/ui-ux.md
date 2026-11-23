---
title: "UI & UX Architecture: effepinnastudio-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: effepinnastudio-com

## Overview & Design Identity
- **Target**: `effepinnastudio-com` (**Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio**)
- **Production URL**: [https://effepinnastudio.com/](https://effepinnastudio.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)
- **Summary**: Direzione artistica, progettazione grafica e produzione di immagini, video e animazioni per agenzie e brand. Fabio Pinna, freelance a Gra...
- **Total Clean CSS Variables Extracted**: `94` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 36px`, `line-height: 28px`, `font-weight: 700`); CSS variables `--type-display: 6rem`, `--leading-display: 6.25rem`; rule `h1` (`font-size: 2rem`, `line-height: 2.25rem`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50.4px`, `line-height: 52.92px`, `font-weight: 700`); rule `h2` (`font-size: var(--type-section)`, `line-height: var(--leading-section)`, `font-weight: var(--weight-...`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--type-body: 1.125rem`, `--leading-body: 1.75rem`, `--space-paragraph: 1.5rem`; rule `p` (`font-size: var(--type-block)`, `line-height: var(--leading-block)`, `font-weight: var(--weight-...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--weight-label: 500`, `--type-meta: .875rem`, `--leading-meta: 1.25rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f2ef` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.controls button { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#ee2c3d` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ff0000` | `.hero-doodle { border: #ff0000 }` |
| **Variable Token (`--red`)** | `#ef233c` | `var(--red)` in `:root` |
| **Variable Token (`--ink`)** | `#0a0a0a` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--red` | `#ef233c` | Color / Atmospheric Token |
| `--paper` | `#f3f2ef` | Canvas / Surface Token |
| `--ink` | `#0a0a0a` | Typography Ink Token |
| `--font-text` | `"Instrument Sans", Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--weight-text` | `400` | Typography Ink Token |
| `--weight-label` | `500` | Design System Custom Token |
| `--weight-heading` | `700` | Typography Ink Token |
| `--type-display` | `6rem` | Typography / Scale Token |
| `--leading-display` | `6.25rem` | Typography / Scale Token |
| `--type-page` | `4rem` | Typography / Scale Token |
| `--leading-page` | `4.25rem` | Typography / Scale Token |
| `--type-section` | `3rem` | Typography / Scale Token |
| `--leading-section` | `3.25rem` | Typography / Scale Token |
| `--type-block` | `1.75rem` | Typography / Scale Token |
| `--leading-block` | `2.125rem` | Typography / Scale Token |
| `--type-intro` | `1.5rem` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero> — `effepinnastudio-com`)**:
   - Landmark `<header class="hero">` (`1440x900px`) hosting `Fabio Pinna — Art Director e Graphic` navigation (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), DOM attributes (`data-work-preview-loading="true"`, `data-loading-theme="red"`, `data-loading-state="ready"`, `data-font-status="instrument-sans"`), and stylesheet rule `root { color-scheme: light;--red: ef233c;--paper: f3f2ef;--ink: 0a0a0a; }`.
2. **Hero Stage & Focal Lead (<section.manifesto> — `Fabio Pinna - Art Direction, Multi`)**:
   - Landmark `<section class="manifesto editorial-grid">` presenting display lead `Fabio Pinna - Art Direction, Multimedia Graphic D...` and copy excerpt *"Mi occupo di direzione artistica e graphic design multimediale. M"* over `#ffffff` canvas and `#0000ee` ink.
3. **Primary Showcase & Content Grid (<section.work> — `Selezione Lavori`)**:
   - Landmark `<section class="work">` rendering section `Selezione Lavori` with copy *"Mi occupo di direzione artistica e graphic design multimediale."*, asset references (`motion-policy-20261012.js`, `favicon-192.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `body { touch-action: manipulation;touch-action: pan-x pan-y; }`.
4. **Interactive Detail & Feature Matrix (<article.work-row> — `Fastweb Tu sei Futuro`)**:
   - Landmark `<article class="work-row">` framing `Fastweb Tu sei Futuro` and `Dose e Dadda Summer Merch` (*"Sviluppo il concept, progetto il linguaggio visivo e lavoro alla "*) with `#f3f2ef` surface cards, `#ff0000` accents, and `focus-visible { outline: 2px solid currentColor;outline-offset: 4px; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://effepinnastudio.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Fabio Pinna — Art Director e Gra` footer links (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), copy *"Art director e graphic designer multimediale, tra Milano e G"*, and `#ff0000` structural dividers.
