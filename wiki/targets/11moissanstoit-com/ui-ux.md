# UI & UX Architecture: 11moissanstoit-com

## Overview & Design Identity
- **Target**: `11moissanstoit-com` (**11 mois sans toi(t), le tour du monde de Josué & Philippe**)
- **Production URL**: [https://11moissanstoit.com/](https://11moissanstoit.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fee422` / `#92939d`)
- **Summary**: Tour du monde autobiographique 2010-2011 de Josué & Philippe. 11 mois, des dizaines d'étapes, des milliers de tweets, de photos et de sou...
- **Total Clean CSS Variables Extracted**: `9` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Founders Grotesk X-Condensed`
- **Body Font Stack**: `Founders Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fee422` | `var(--primary-yellow)` in `:root` |
| **Primary Typography Ink** | `#151723` | `var(--dark-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--white-clear)` in `:root` |
| **Interactive Accent / Highlight** | `#92939d` | `var(--medium-blue-grey)` in `:root` |
| **Secondary / Muted Copy** | `#e8edf3` | `var(--hyper-light-blue-grey)` in `:root` |
| **Structural Hairline Border** | `#d1c658` | `var(--brown-yellow-bright)` in `:root` |
| **Variable Token (`--blue-notif`)** | `#3acfe1` | `var(--blue-notif)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--primary-yellow` | `#fee422` | Brand / Palette Token |
| `--dark-blue` | `#151723` | Canvas / Surface Token |
| `--white-clear` | `#fff` | Canvas / Surface Token |
| `--medium-blue-grey` | `#92939d` | Color / Atmospheric Token |
| `--hyper-light-blue-grey` | `#e8edf3` | Canvas / Surface Token |
| `--brown-yellow-bright` | `#d1c658` | Color / Atmospheric Token |
| `--blue-notif` | `#3acfe1` | Color / Atmospheric Token |
| `--background` | `#fee422` | Canvas / Surface Token |
| `--foreground` | `#151723` | Typography Ink Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--11moissanstoit-c-bg` | `#fee422` | Canvas Substrate (from `var(--primary-yellow)` in `:root`) |
| `--11moissanstoit-c-ink` | `#151723` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.h-full> — `11moissanstoit-com`)**:
   - Landmark `<header class="h-full">` hosting `11 mois sans toi(t), le tour du mond` navigation (`MapLibre · EOxCloudless 2024 · CC BY-NC-SA · OpenFreeMap · © OpenMapTiles`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `11 mois sans toi(t), le tour du mo`)**:
   - Landmark `<section class="relative font-condensed">` presenting display lead `11 mois sans toi(t), le tour du monde de Josué &` and copy excerpt *"October 2010. Philippe and Josué , two childhood friends, make th"* over `#fee422` canvas and `#151723` ink.
3. **Primary Showcase & Content Grid (<section.font-condensed> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="font-condensed font-medium">` rendering section `Featured Work & Interactive Showcase` with copy *"a journey told in real time through their digital footprints, on "*, asset references (`logo-vecto.svg`, `photoLogo_11moissanstoi.png`, `2_er3-xpipny2.css`, `3cwyw8ne2vg7_.js`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="relative font-condensed">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"15 years later, for the anniversary of our return (August 24, 201"*) with `#fff` surface cards, `#92939d` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.inset-0> — `https://11moissanstoit.com/`)**:
   - Landmark `<footer class="inset-0">` anchoring `11 mois sans toi(t), le tour du ` footer links (`MapLibre · EOxCloudless 2024 · CC BY-NC-SA · OpenFreeMap · © OpenMapTiles`), copy *"Everything that follows was written live, in 2010 and 2011, "*, and `#d1c658` structural dividers.
