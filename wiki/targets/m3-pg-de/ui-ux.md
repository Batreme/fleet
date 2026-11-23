---
title: "UI & UX Architecture: m3-pg-de"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: m3-pg-de

## Overview & Design Identity
- **Target**: `m3-pg-de` (**M3 Planungsgruppe**)
- **Production URL**: [https://m3-pg.de](https://m3-pg.de)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0d6efd` accent)
- **Summary**: Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.
- **Total Clean CSS Variables Extracted**: `445` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 155.4px`, `line-height: 155.4px`, `font-weight: 700`, `letter-spacing: -4.662px`); rule `h1` (`font-size: clamp(40px, 11.1cqw, 198px)`, `line-height: 1em`, `letter-spacing: -0.03em`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 74px`, `font-weight: 600`, `letter-spacing: -1.92px`); rule `.h2` (`font-size: 64px`, `line-height: 1.125em`, `letter-spacing: -0.03em`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `body` (`font-size: 16px`, `line-height: 1.5em`, `letter-spacing: -0.01em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 24px`, `font-weight: 600`, `letter-spacing: -0.4px`); rule `,small` (`font-size: .875em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f8f9fa` | `var(--bs-tertiary-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0d6efd` | `var(--bs-primary)` in `:root` |
| **Secondary / Muted Copy** | `#6c757d` | `var(--bs-secondary)` in `:root` |
| **Structural Hairline Border** | `#9ec5fe` | `var(--bs-primary-border-subtle)` in `:root` |
| **Variable Token (`--bs-indigo`)** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Variable Token (`--bs-purple`)** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Variable Token (`--bs-pink`)** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Variable Token (`--bs-red`)** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Variable Token (`--bs-orange`)** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Variable Token (`--bs-yellow`)** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Variable Token (`--bs-green`)** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
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
   - Landmark `<header class="header-desk">` (`1440x60px`) hosting `M3 Planungsgruppe` navigation (`M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`), DOM attributes (`data-wp-strategy="defer"`, `data-more="Mehr erfahren"`, `data-less="Weniger"`, `data-more="Mehr erfahren"`), and stylesheet rule `.wpcf7 .hidden-fields-container { display: none; }`.
2. **Hero Stage & Focal Lead (<section.wp-singular> — `M3 Planungsgruppe`)**:
   - Landmark `<section class="wp-singular">` presenting display lead `M3 Planungsgruppe` and copy excerpt *"Gute Planung verbindet für uns Nachhaltigkeit, Ästhetik und Wirts"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.page-template> — `Nachhaltigkeit. Ästhetik. Wirtscha`)**:
   - Landmark `<section class="page-template">` rendering section `Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.` with copy *"Unser Fokus liegt auf präziser Planung, bewusst eingesetzten Mate"*, asset references (`bootstrap.min.css`, `slick.min.css`, `main.css`, `responsive.css`), and grid rule `.wpcf7 form .wpcf7-response-output { margin: 2em 0.5em 1em; padding: 0.2em 1em; border: 2px solid 00a0d2; }`.
4. **Interactive Detail & Feature Matrix (<section.page-template-templates> — `Planung, die Bestand hat.`)**:
   - Landmark `<section class="page-template-templates">` framing `Planung, die Bestand hat.` and `B18 – Fachwerk trifft Glas` (*"Jedes Projekt beginnt mit einem offenen und zielgerichteten Dialo"*) with `#f8f9fa` surface cards, `#0d6efd` accents, and `form.submitting .wpcf7-response-o... { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.page-template-home> — `https://m3-pg.de`)**:
   - Landmark `<footer class="page-template-home">` anchoring `M3 Planungsgruppe` footer links (`M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`), copy *"Auf dieser Grundlage entwickeln wir eine klare Projektstrate"*, and `#9ec5fe` structural dividers.
