# UI & UX Architecture: turismo-gov-st_fr

## Overview & Design Identity
- **Target**: `turismo-gov-st_fr` (**Homepage · São Tomé E Príncipe**)
- **Production URL**: [https://turismo.gov.st/fr](https://turismo.gov.st/fr)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#EEEDEA` accent)
- **Summary**: Ce que vous devez savoir sur la taxe de tourisme
- **Total Clean CSS Variables Extracted**: `104` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Outfit`
- **Body Font Stack**: `gyst-variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: gyst-variable,serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `0.875em`, `1em`, `24px`, `100%`, `75%`)
- **Body Copy**: CSS variables `--font-body: Outfit,Arial,Helvetica,sans-serif`, `--paragraph-max-width: 100%`, `--paragraph-margin-bottom: 0!important`; rule `p` (`font-size: var(--fz-size, 1.7rem)`, `line-height: 1.5`, `font-weight: 300`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `0.875em`, `1em`, `24px`, `100%`, `75%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#000000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#38492A` | `var(--color-green--dark)` in `:root` |
| **Interactive Accent / Highlight** | `#EEEDEA` | `var(--color-beige)` in `:root` |
| **Secondary / Muted Copy** | `#80802B` | `var(--color-fauna-flora)` in `:root` |
| **Structural Hairline Border** | `#395665` | `var(--color-ocean)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-white--30` | `rgba(255, 255, 255, 0.3)` | Canvas / Surface Token |
| `--color-white--00` | `rgba(255, 255, 255, 0)` | Canvas / Surface Token |
| `--color-white--15` | `rgba(255, 255, 255, 0.15)` | Canvas / Surface Token |
| `--color-white--08` | `rgba(255, 255, 255, 0.08)` | Canvas / Surface Token |
| `--color-black` | `#000000` | Canvas / Surface Token |
| `--color-black--05` | `rgba(0, 0, 0, 0.05)` | Canvas / Surface Token |
| `--color-black--08` | `rgba(0, 0, 0, 0.08)` | Canvas / Surface Token |
| `--color-black--15` | `rgba(0, 0, 0, 0.15)` | Canvas / Surface Token |
| `--color-black--00` | `rgba(0, 0, 0, 0)` | Canvas / Surface Token |
| `--color-black--10` | `rgba(0, 0, 0, 0.1)` | Canvas / Surface Token |
| `--color-black--30` | `rgba(0, 0, 0, 0.3)` | Canvas / Surface Token |
| `--color-black--50` | `rgba(0, 0, 0, 0.5)` | Canvas / Surface Token |
| `--color-black--70` | `rgba(0, 0, 0, 0.7)` | Canvas / Surface Token |
| `--color-green--dark` | `#38492A` | Canvas / Surface Token |
| `--color-green--dark--30` | `rgba(56, 73, 42, 0.3)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Header> — `turismo-gov-st_fr`)**:
   - Landmark `<header class="Header">` hosting `Homepage · São Tomé E Príncipe` navigation (`Nature · Un éden insulaire · Une flore luxuriante · Plages de sable doré`), DOM attributes (`data-barba="wrapper"`, `data-once="form-single-submit we..."`, `data-off-canvas-main-canvas`, `data-container-query-observer-bae45330cd3d4e0e96b60d26b57009b5-1794679749212-0`), and stylesheet rule `.ajax-progress { display: inline-block; padding: 1px 5px 2px 5px; }`.
2. **Hero Stage & Focal Lead (<section.Homepage> — `Pourquoi`)**:
   - Landmark `<section class="Homepage node">` presenting display lead `Pourquoi` and copy excerpt *"São Tomé E Príncipe"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.ParagraphImmersiveMesh> — `Organiser`)**:
   - Landmark `<section class="ParagraphImmersiveMesh paragraph">` rendering section `Organiser` with copy *"Pourquoi São Tomé et Príncipe? Pourquoi Nature Un éden insulaire "*, asset references (`sdk.js`, `gtm.js`, `favicon.png`, `webform.element.flexbox.css`), and grid rule `.ajax-progress-throbber .throbber { display: inline; padding: 1px 6px 2px; background: transparent url(../th... }`.
4. **Interactive Detail & Feature Matrix (<section.ParagraphVerticalSlider> — `Pratique`)**:
   - Landmark `<section class="ParagraphVerticalSlider paragraph">` framing `Pratique` and `Pied de page` (*"Pourquoi São Tomé et Príncipe?"*) with `#38492A` surface cards, `#EEEDEA` accents, and `.ajax-progress-throbber .message { display: inline; padding: 1px 5px 2px; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://turismo.gov.st/fr`)**:
   - Landmark `<footer class="footer">` anchoring `Homepage · São Tomé E Príncipe` footer links (`Nature · Un éden insulaire · Une flore luxuriante · Plages de sable doré`), copy *"Nature Un éden insulaire Une flore exceptionnelle Une flore "*, and `#395665` structural dividers.
