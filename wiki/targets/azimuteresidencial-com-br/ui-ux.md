---
title: "UI & UX Architecture: azimuteresidencial-com-br"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: azimuteresidencial-com-br

## Overview & Design Identity
- **Target**: `azimuteresidencial-com-br` (**Azimute — Seu próximo horizonte · ASL**)
- **Production URL**: [https://azimuteresidencial.com.br/](https://azimuteresidencial.com.br/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#202725` canvas, `#fff8ec` ink, `#f4d7af` accent)
- **Summary**: Conheça o Residencial Azimute, da ASL, na Vila Vitória, em Mauá. Apartamentos de 63 e 67 m², com 2 dormitórios, 1 suíte e varanda gourmet.
- **Total Clean CSS Variables Extracted**: `20` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 141.12px`, `line-height: 132.653px`, `font-weight: 400`, `letter-spacing: -3.528px`); rule `h1` (`letter-spacing: -.025em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 144px`, `line-height: 129.6px`, `font-weight: 400`, `letter-spacing: -2.16px`); rule `h2` (`letter-spacing: -.045em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 1rem`, `line-height: 1.7`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: normal`, `font-weight: 400`); rule `small` (`font-size: .875rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#202725` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fff8ec` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1f2623` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f4d7af` | `photo-viewer__formats button:fo... { color: #f4d7af }` |
| **Secondary / Muted Copy** | `#68665e` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#292e2a` | `var(--line)` in `:root` (`534d432d`) |
| **Variable Token (`--paper`)** | `#f3f0e9` | `var(--paper)` in `:root` |
| **Variable Token (`--ink`)** | `#262825` | `var(--ink)` in `:root` |
| **Variable Token (`--copper`)** | `#87654c` | `var(--copper)` in `:root` |
| **Variable Token (`--line`)** | `#534d43` | `var(--line)` in `:root` |
| **Variable Token (`--az-crystal-white`)** | `#f6f0e5` | `var(--az-crystal-white)` in `:root` |
| **Variable Token (`--az-crystal-bronze`)** | `#ccb494` | `var(--az-crystal-bronze)` in `:root` |
| **Variable Token (`--az-crystal-ink`)** | `#272925` | `var(--az-crystal-ink)` in `:root` |
| **Variable Token (`--journey-ink`)** | `#292b27` | `var(--journey-ink)` in `:root` |
| **Variable Token (`--journey-muted`)** | `#655b4f` | `var(--journey-muted)` in `:root` |
| **Variable Token (`--journey-line`)** | `#776958` | `var(--journey-line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#f3f0e9` | Canvas / Surface Token |
| `--ink` | `#262825` | Typography Ink Token |
| `--muted` | `#68665e` | Color / Atmospheric Token |
| `--copper` | `#87654c` | Color / Atmospheric Token |
| `--line` | `#534d432d` | Color / Atmospheric Token |
| `--gutter` | `6.25vw` | Layout / Spatial Grid Token |
| `--serif` | `'Instrument Serif',Georgia,serif` | Typography / Scale Token |
| `--sans` | `'DM Sans',Arial,sans-serif` | Typography / Scale Token |
| `--az-crystal-white` | `#f6f0e5` | Canvas / Surface Token |
| `--az-crystal-bronze` | `#ccb494` | Elevation / Border Token |
| `--az-crystal-ink` | `#272925` | Typography Ink Token |
| `--sculpture-expansion` | `0` | Design System Custom Token |
| `--journey-ink` | `#292b27` | Typography Ink Token |
| `--journey-muted` | `#655b4f` | Color / Atmospheric Token |
| `--journey-line` | `#77695840` | Color / Atmospheric Token |
| `--hero-presence` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `azimuteresidencial-com-br`)**:
   - Landmark `<header class="header">` (`1440x107px`) hosting `Azimute — Seu próximo horizonte · AS` navigation (`O projeto · Perspectiva · Essência · Residências · Espaços`), DOM attributes (`data-atmosphere-bound="true"`, `data-svg-origin="44 56"`, `data-active-index="0"`, `data-scroll-start="2170"`), and stylesheet rule `font-face { font-family:Marcellus;src:url(assets/fonts/marcellus.ttf) format('truety... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `SEU PRÓXIMO horizonte.`)**:
   - Landmark `<section class="hero">` presenting display lead `SEU PRÓXIMO horizonte.` and copy excerpt *"VILA VITÓRIA · MAUÁ"* over `#202725` canvas and `#fff8ec` ink.
3. **Primary Showcase & Content Grid (<section.project> — `A VIDA EM boa direção.`)**:
   - Landmark `<section class="project">` rendering section `A VIDA EM boa direção.` with copy *"Uma nova direção para morar. Um empreendimento ASL."*, asset references (`azimute-symbol-crystal.svg`, `instrument-serif.ttf`, `fachada-azimute-1920.webp`, `azimute.css`), and grid rule `body { margin:0;overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<section.architecture-chapter> — `Ambientes que se conectam`)**:
   - Landmark `<section class="architecture-chapter cinema-tour">` framing `Ambientes que se conectam` and `Uma nova perspectiva.` (*"UMA NOVA DIREÇÃO PARA MORAR"*) with `#1f2623` surface cards, `#f4d7af` accents, and `button { font:inherit;cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://azimuteresidencial.com.br/`)**:
   - Landmark `<footer class="footer section-wrap">` anchoring `Azimute — Seu próximo horizonte ` footer links (`O projeto · Perspectiva · Essência · Residências · Espaços`), copy *"VILA VITÓRIA · MAUÁ / SP"*, and `#292e2a` structural dividers.
