# UI & UX Architecture: m3-pg-de

## Overview & Design Identity
- **Target**: `m3-pg-de` (**M3 Planungsgruppe**)
- **Production URL**: [https://m3-pg.de](https://m3-pg.de)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0d6efd` canvas, `#6610f2` ink, `#d63384` accent)
- **Summary**: Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.
- **Total Clean CSS Variables Extracted**: `445` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `212529`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `body` (`font-size: 16px`, `line-height: 1.5em`, `letter-spacing: -0.01em`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--bs-carousel-caption-color: #000`; rule `,small` (`font-size: .875em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d6efd` | `var(--bs-blue)` in `:root` |
| **Primary Typography Ink** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Interactive Accent / Highlight** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Secondary / Muted Copy** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Structural Hairline Border** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Variable Token (`--bs-yellow`)** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Variable Token (`--bs-green`)** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-black`)** | `#000` | `var(--bs-black)` in `:root` |
| **Variable Token (`--bs-white`)** | `#fff` | `var(--bs-white)` in `:root` |
| **Variable Token (`--bs-gray`)** | `#6c757d` | `var(--bs-gray)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
| **Variable Token (`--bs-gray-100`)** | `#f8f9fa` | `var(--bs-gray-100)` in `:root` |
| **Variable Token (`--bs-gray-200`)** | `#e9ecef` | `var(--bs-gray-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-purple` | `#6f42c1` | Color / Atmospheric Token |
| `--bs-pink` | `#d63384` | Typography Ink Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |
| `--bs-orange` | `#fd7e14` | Color / Atmospheric Token |
| `--bs-yellow` | `#ffc107` | Color / Atmospheric Token |
| `--bs-green` | `#198754` | Color / Atmospheric Token |
| `--bs-teal` | `#20c997` | Color / Atmospheric Token |
| `--bs-cyan` | `#0dcaf0` | Color / Atmospheric Token |
| `--bs-black` | `#000` | Canvas / Surface Token |
| `--bs-white` | `#fff` | Canvas / Surface Token |
| `--bs-gray` | `#6c757d` | Color / Atmospheric Token |
| `--bs-gray-dark` | `#343a40` | Canvas / Surface Token |
| `--bs-gray-100` | `#f8f9fa` | Color / Atmospheric Token |
| `--bs-gray-200` | `#e9ecef` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header-desk> — `m3-pg-de`)**:
   - Landmark `<header class="header-desk">` hosting `M3 Planungsgruppe` navigation (`M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`), DOM attributes (`data-wp-strategy="defer"`, `data-more="Mehr erfahren"`, `data-less="Weniger"`, `data-more="Mehr erfahren"`), and stylesheet rule `.bi-123::before { content:"\f67f" }`.
2. **Hero Stage & Focal Lead (<section.wp-singular> — `Nachhaltigkeit. Ästhetik. Wirtscha`)**:
   - Landmark `<section class="wp-singular">` presenting display lead `Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.` and copy excerpt *"Projekte Alle Projekte Büro & Verwaltung Industrie Wohnen"* over `#0d6efd` canvas and `#6610f2` ink.
3. **Primary Showcase & Content Grid (<section.page-template> — `Planung, die Bestand hat.`)**:
   - Landmark `<section class="page-template">` rendering section `Planung, die Bestand hat.` with copy *"Gute Planung verbindet für uns Nachhaltigkeit, Ästhetik und Wirts"*, asset references (`bootstrap.min.css`, `slick.min.css`, `main.css`, `responsive.css`), and grid rule `.bi-alarm-fill::before { content:"\f101" }`.
4. **Interactive Detail & Feature Matrix (<section.page-template-templates> — `Labwerk`)**:
   - Landmark `<section class="page-template-templates">` framing `Labwerk` and `Hanghaus` (*"Unser Fokus liegt auf präziser Planung, bewusst eingesetzten Mate"*) with `#6f42c1` surface cards, `#d63384` accents, and `.bi-alarm::before { content:"\f102" }`.
5. **Colophon & Global Directory Footer (<footer.page-template-home> — `https://m3-pg.de`)**:
   - Landmark `<footer class="page-template-home">` anchoring `M3 Planungsgruppe` footer links (`M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`), copy *"Jedes Projekt beginnt mit einem offenen und zielgerichteten "*, and `#fd7e14` structural dividers.
