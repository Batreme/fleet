# UI & UX Architecture: azimuteresidencial-com-br

## Overview & Design Identity
- **Target**: `azimuteresidencial-com-br` (**Azimute — Seu próximo horizonte · ASL**)
- **Production URL**: [https://azimuteresidencial.com.br/](https://azimuteresidencial.com.br/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#625e55` canvas, `#f6f0e5` ink, `#ccb494` accent)
- **Summary**: Conheça o Residencial Azimute, da ASL, na Vila Vitória, em Mauá. Apartamentos de 63 e 67 m², com 2 dormitórios, 1 suíte e varanda gourmet.
- **Total Clean CSS Variables Extracted**: `20` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Marcellus`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: -.025em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(62px,7.4vw,118px)`, `line-height: .94`, `letter-spacing: -.045em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 1.75`)
- **Metadata & Labels**: rule `small` (`font-size: .875rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#625e55` | `var(--muted)` in `:root` |
| **Primary Typography Ink** | `#79573f` | `var(--copper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f6f0e5` | `var(--az-crystal-white)` in `:root` |
| **Interactive Accent / Highlight** | `#ccb494` | `var(--az-crystal-bronze)` in `:root` |
| **Secondary / Muted Copy** | `#272925` | `var(--az-crystal-ink)` in `:root` |
| **Structural Hairline Border** | `#292b27` | `var(--journey-ink)` in `:root` |
| **Variable Token (`--line`)** | `#534d432d` | `var(--line)` in `:root` |
| **Variable Token (`--journey-muted`)** | `#655b4f` | `var(--journey-muted)` in `:root` |
| **Variable Token (`--journey-line`)** | `#77695840` | `var(--journey-line)` in `:root` |
| **Variable Token (`--paper`)** | `#f3f0e9` | `var(--paper)` in `:root` |
| **Variable Token (`--ink`)** | `#262825` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--muted` | `#625e55` | Color / Atmospheric Token |
| `--copper` | `#79573f` | Color / Atmospheric Token |
| `--line` | `#534d432d` | Color / Atmospheric Token |
| `--az-crystal-white` | `#f6f0e5` | Canvas / Surface Token |
| `--az-crystal-bronze` | `#ccb494` | Elevation / Border Token |
| `--az-crystal-ink` | `#272925` | Typography Ink Token |
| `--journey-ink` | `#292b27` | Typography Ink Token |
| `--journey-muted` | `#655b4f` | Color / Atmospheric Token |
| `--journey-line` | `#77695840` | Color / Atmospheric Token |
| `--sculpture-expansion` | `0` | Design System Custom Token |
| `--paper` | `#f3f0e9` | Canvas / Surface Token |
| `--ink` | `#262825` | Typography Ink Token |
| `--gutter` | `6.25vw` | Layout / Spatial Grid Token |
| `--serif` | `'Instrument Serif',Georgia,serif` | Typography / Scale Token |
| `--sans` | `'DM Sans',Arial,sans-serif` | Typography / Scale Token |
| `--hero-presence` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `azimuteresidencial-com-br`)**:
   - Landmark `<header class="header">` hosting `Azimute — Seu próximo horizonte · AS` navigation (`O projeto · Perspectiva · Essência · Residências · Espaços`), DOM attributes (`data-atmosphere-bound="true"`, `data-svg-origin="44 56"`, `data-active-index="0"`, `data-scroll-start="2170"`), and stylesheet rule `body { isolation:isolate;background:202725 }`.
2. **Hero Stage & Focal Lead (<section.hero> — `SEU PRÓXIMO horizonte.`)**:
   - Landmark `<section class="hero">` presenting display lead `SEU PRÓXIMO horizonte.` and copy excerpt *"Ir para o conteúdo"* over `#625e55` canvas and `#f6f0e5` ink.
3. **Primary Showcase & Content Grid (<section.project> — `A VIDA EM boa direção.`)**:
   - Landmark `<section class="project">` rendering section `A VIDA EM boa direção.` with copy *"UMA NOVA DIREÇÃO PARA MORAR"*, asset references (`azimute-symbol-crystal.svg`, `instrument-serif.ttf`, `fachada-azimute-1920.webp`, `azimute.css`), and grid rule `body>.footer { position:relative;z-index:1 }`.
4. **Interactive Detail & Feature Matrix (<section.architecture-chapter> — `Ambientes que se conectam`)**:
   - Landmark `<section class="architecture-chapter cinema-tour">` framing `Ambientes que se conectam` and `Uma nova perspectiva.` (*"ASL INCORPORADORA E CONSTRUTORA"*) with `#f6f0e5` surface cards, `#ccb494` accents, and `.site-atmosphere.is-resting>div { will-change:auto }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://azimuteresidencial.com.br/`)**:
   - Landmark `<footer class="footer section-wrap">` anchoring `Azimute — Seu próximo horizonte ` footer links (`O projeto · Perspectiva · Essência · Residências · Espaços`), copy *"INCORPORADORA E CONSTRUTORA"*, and `#292b27` structural dividers.
