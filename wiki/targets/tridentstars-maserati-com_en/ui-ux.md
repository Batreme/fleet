# UI & UX Architecture: tridentstars-maserati-com_en

## Overview & Design Identity
- **Target**: `tridentstars-maserati-com_en` (**Discover Maserati’s Trident Constellation in the Sky**)
- **Production URL**: [https://tridentstars.maserati.com/en/](https://tridentstars.maserati.com/en/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#2d2d2d`)
- **Summary**: A real constellation of stars created to celebrate 100 years of vision, performance and iconic design.
- **Total Clean CSS Variables Extracted**: `89` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `TWK Everett`
- **Body Font Stack**: `Roboto Mono`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy**: rule `p` (`font-size: .75em`)
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: 1.42857`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffc845` | `var(--color-accent-yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#2d2d2d` | `var(--tl-border-color)` in `:root` |
| **Secondary / Muted Copy** | `#f5f5f5` | `var(--scrollbar-track)` in `:root` |
| **Structural Hairline Border** | `#ddd` | `var(--scrollbar-thumb)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spin` | `0deg` | Design System Custom Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.42857` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |
| `--text-xl--line-height` | `1.4` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |
| `--text-2xl--line-height` | `1.33333` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--radius-lg` | `16px` | Elevation / Border Token |
| `--radius-xl` | `.75rem` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.absolute> — `tridentstars-maserati-com_en`)**:
   - Landmark `<header class="absolute top-0">` hosting `Discover Maserati’s Trident Constell` navigation (`the manifesto · discover more`), DOM attributes (`data-domain-script="81be852f-f22f-496a-87..."`, `data-document-language="true"`, `data-hid="adobe-launch"`, `data-hid="adobe-data-layer"`), and stylesheet rule `.external-link-icon__arrow { transition:translate .3s }`.
2. **Hero Stage & Focal Lead (<section.ot-sdk-row> — `100 YEARS OF THE TRIDENT LOGO 1 0 `)**:
   - Landmark `<section class="ot-sdk-row ot-cat-grp">` presenting display lead `100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F...` and copy excerpt *"100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F T H E T R I D E"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.ot-hide> — `Privacy Preference Center`)**:
   - Landmark `<section class="ot-hide ot-hosts-ui">` rendering section `Privacy Preference Center` with copy *"100 YEARS OF THE TRIDENT LOGO"*, asset references (`entry.Btz3ffrH.css`, `default.CffeYOeI.css`, `MoleculesExternalLink.BgGEM1Uz.css`, `MoleculesPopup.CyDrrBxz.css`), and grid rule `hover .external-link-icon__arrow { translate:2px -2px }`.
4. **Interactive Detail & Feature Matrix (<section.left-0> — `Manage Consent Preferences`)**:
   - Landmark `<section class="left-0">` framing `Manage Consent Preferences` and `Cookie List` (*"1 0 0 Y E A R S O F T H E T R I D E N T L O G O"*) with `#ffc845` surface cards, `#2d2d2d` accents, and `after { outline:1px solid var(--color-secondary-white);outline-offset:2px }`.
5. **Colophon & Global Directory Footer (<footer.z-header> — `https://tridentstars.maserati.com/en/`)**:
   - Landmark `<footer class="z-header">` anchoring `Discover Maserati’s Trident Cons` footer links (`the manifesto · discover more`), copy *"100 STARS BEHIND ITS LEGEND 1 0 0 S T A R S B E H I N D I T "*, and `#ddd` structural dividers.
