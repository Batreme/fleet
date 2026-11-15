# UI & UX Architecture: kohenavocats-com_avocats-droit-famille-paris

## Overview & Design Identity
- **Target**: `kohenavocats-com_avocats-droit-famille-paris` (**Avocat Droit de la Famille Paris · Divorce, Garde d'Enfants, Succession**)
- **Production URL**: [https://kohenavocats.com/avocats-droit-famille-paris/](https://kohenavocats.com/avocats-droit-famille-paris/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#39aa59` canvas, `#000` ink, `#fff` accent)
- **Summary**: Avocat en droit de la famille à Paris. Divorce amiable ou contentieux, garde d'enfants, pension alimentaire, succession. Accompagnement h...
- **Total Clean CSS Variables Extracted**: `298` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Lato`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: clamp(26px, 6vw, 86px)`, `line-height: 1.12`, `letter-spacing: -.025em`, `font-weight: 900`)
- **Section Heading (`H2`)**: CSS variables `--e-contact-buttons-top-bar-subtitle: #fff`; rule `h2` (`font-size: clamp(18px, 0.9rem + 0.6vw, 2...`, `line-height: 1.12 !important`, `letter-spacing: 0.02em !important`, `font-weight: 400 !important`)
- **Body Copy**: CSS variables `--e-contact-buttons-message-bubble-body: #000`; rule `p` (`font-size: 18px`)
- **Metadata & Labels**: CSS variables `--e-contact-buttons-size-small: 55px`, `--e-contact-buttons-svg-size-small: 32px`, `--e-contact-buttons-profile-image-size-small: 65px`; rule `small` (`font-size: 11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#39aa59` | `var(--e-contact-buttons-profile-dot-bg)` in `:root` |
| **Primary Typography Ink** | `#467ff7` | `var(--e-contact-buttons-button-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1c2448` | `var(--e-contact-buttons-button-bg-hover)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--e-contact-buttons-button-icon)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--e-contact-buttons-message-bubble-name)` in `:root` |
| **Structural Hairline Border** | `#c8d5dc` | `var(--e-contact-buttons-message-bubble-chat-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--km-beacon` | `360deg` | Design System Custom Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--justify-content` | `initial` | Design System Custom Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |
| `--order` | `initial` | Design System Custom Token |
| `--align-self` | `initial` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--border-radius` | `0` | Elevation / Border Token |
| `--border-top-width` | `0px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `kohenavocats-com_avocats-droit-famille-paris`)**:
   - Landmark `<header class="elementor elementor-25177">` hosting `Avocat Droit de la Famille Paris · D` navigation (`Urgence pénale · Garde à vue · Détention provisoire · Cour d’assises · Instruction pénale`), DOM attributes (`data-kfh-variant="transparent"`, `data-cfasync="false"`, `data-no-minify="1"`, `data-no-optimize="1"`), and stylesheet rule `property --km-beacon { syntax: '<angle>'; inherits: false; initial-value: 0deg; }`.
2. **Hero Stage & Focal Lead (<section.kfh-conversion> — `Avocat en droit de la famille à Pa`)**:
   - Landmark `<section class="kfh-conversion kfg-unified">` presenting display lead `Avocat en droit de la famille à Paris` and copy excerpt *"Droit pénal · Avocat pénaliste à Paris Urgence pénale Garde à vue"* over `#39aa59` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.kohen-avis-panel> — `Recevez une première analyse`)**:
   - Landmark `<section class="kohen-avis-panel kohen-avis-wrap">` rendering section `Recevez une première analyse` with copy *"Droit pénal · Avocat pénaliste à Paris"*, asset references (`bat.js`, `scripts.clarity.ms`, `www.googletagmanager.com`, `www.clarity.ms`), and grid rule `to { --km-beacon: 360deg; }`.
4. **Interactive Detail & Feature Matrix (<section.knp> — `Ils parlent de nous`)**:
   - Landmark `<section class="knp knp--manuel">` framing `Ils parlent de nous` and `Comment le cabinet vous accompagne en droit de la...` (*"Comparution immédiate"*) with `#1c2448` surface cards, `#fff` accents, and `svg { position: relative; z-index: 1; width: 24px; height: 24px; }`.
5. **Colophon & Global Directory Footer (<footer.kohen-avis-panel-footer> — `https://kohenavocats.com/avocats-droit-famille-paris/`)**:
   - Landmark `<footer class="kohen-avis-panel-footer">` anchoring `Avocat Droit de la Famille Paris` footer links (`Urgence pénale · Garde à vue · Détention provisoire · Cour d’assises · Instruction pénale`), copy *"Détention provisoire"*, and `#c8d5dc` structural dividers.
