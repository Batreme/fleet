# UI & UX Architecture: www-kubehotel-saint-tropez-com_fr

## Overview & Design Identity
- **Target**: `www-kubehotel-saint-tropez-com_fr` (**Hôtel 5 étoiles à Saint-Tropez – Nouveau site bientôt en ligne**)
- **Production URL**: [https://www.kubehotel-saint-tropez.com/fr](https://www.kubehotel-saint-tropez.com/fr)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fdf9f4` ink, `#7c7c7c` accent)
- **Summary**: Notre nouveau site arrive très bientôt. Hôtel, restaurants, bien-être et piscines à Saint-Tropez : revenez nous voir prochainement.
- **Total Clean CSS Variables Extracted**: `160` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Saphion`
- **Body Font Stack**: `Inter Variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: rule `p` (`line-height: var(--_typography---l...`)
- **Metadata & Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--tight)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--swatch--black)` in `:root` |
| **Primary Typography Ink** | `#e1dcd9` | `var(--swatch--grey-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c6c6c6` | `var(--swatch--grey-300)` in `:root` |
| **Interactive Accent / Highlight** | `#7c7c7c` | `var(--swatch--grey-700)` in `:root` |
| **Secondary / Muted Copy** | `#484847` | `var(--swatch--grey-800)` in `:root` |
| **Structural Hairline Border** | `#fdf9f4` | `var(--swatch--beige)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_theme---background` | `var(--swatch--beige)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--black)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--large)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-light)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--tight)` | Typography Ink Token |
| `--radius--main` | `.5rem` | Elevation / Border Token |
| `--_theme---background-2` | `var(--swatch--beige-2)` | Canvas / Surface Token |
| `--site--column-count` | `12` | Layout / Spatial Grid Token |
| `--_responsive---large` | `1` | Design System Custom Token |
| `--_responsive---medium` | `0` | Design System Custom Token |
| `--_responsive---small` | `0` | Design System Custom Token |
| `--_responsive---xsmall` | `0` | Design System Custom Token |
| `--max-width--small` | `calc(var(--site--viewport-max)*1rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero_header_wrap> — `www-kubehotel-saint-tropez-com_fr`)**:
   - Landmark `<header class="hero_header_wrap">` hosting `Hôtel 5 étoiles à Saint-Tropez – Nou` navigation (`fr · en · it · ru`), DOM attributes (`data-wf-domain="www.layne-sainttropez..."`, `data-wf-page="69c122f05101301b0245c797"`, `data-wf-site="69c122f05101301b0245c7c6"`, `data-padding-bottom="none"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `Les plus belles vacances ont le go`)**:
   - Landmark `<section class="hero_wrap u-section">` presenting display lead `Les plus belles vacances ont le goût de l’insouci...` and copy excerpt *"Hôtel - Restaurant - Spa - Piscines"* over `#000` canvas and `#fdf9f4` ink.
3. **Primary Showcase & Content Grid (<section.hero_wrap> — `Hôtel - Restaurant - Spa - Piscine`)**:
   - Landmark `<section class="hero_wrap u-section">` rendering section `Hôtel - Restaurant - Spa - Piscines` with copy *"Ouverture 1 er mai 2027"*, asset references (`cdn.prod.website-files.com`, `layne-sainttropez.webflow.shared....`, `player.vimeo.com`, `vod-adaptive-ak.vimeocdn.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.hero_wrap> — `Ouverture 1 er mai 2027`)**:
   - Landmark `<section class="hero_wrap u-section">` framing `Ouverture 1 er mai 2027` and `Informations et réservations : info@layne-saintt` (*"Informations et réservations : info@layne-sainttropez.com"*) with `#c6c6c6` surface cards, `#7c7c7c` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.w-embed> — `https://www.kubehotel-saint-tropez.com/fr`)**:
   - Landmark `<footer class="w-embed">` anchoring `Hôtel 5 étoiles à Saint-Tropez –` footer links (`fr · en · it · ru`), copy *"Informations et réservations :"*, and `#fdf9f4` structural dividers.
