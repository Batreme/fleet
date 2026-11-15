# UI & UX Architecture: overworldaudio-com

## Overview & Design Identity
- **Target**: `overworldaudio-com` (**Overworld Audio**)
- **Production URL**: [https://overworldaudio.com/](https://overworldaudio.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e9ecee` / `#6e8799`)
- **Summary**: Audio co-development for games and interactive experiences, from prototype to final mix.
- **Total Clean CSS Variables Extracted**: `25` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IvarHeadline`
- **Body Font Stack**: `PPFrama`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.h1` (`font-size: 2.375rem`)
- **Section Heading (`H2`)**: rule `,.h2` (`line-height: .95`, `font-weight: 500`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.5625rem`, `.75rem`, `1.875rem`, `16px`, `clamp(16px,1.11111vw,20px)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.5625rem`, `.75rem`, `1.875rem`, `16px`, `clamp(16px,1.11111vw,20px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e9ecee` | `var(--off-white)` in `:root` |
| **Primary Typography Ink** | `#13151f` | `var(--off-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#aab9c7` | `var(--color-secondary)` in `:root` |
| **Interactive Accent / Highlight** | `#6e8799` | `var(--gray)` in `:root` |
| **Secondary / Muted Copy** | `#4c5e6b` | `var(--dark-gray)` in `:root` |
| **Structural Hairline Border** | `#1a1a1a` | `var(--surface)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--nav-align-col` | `6` | Layout / Spatial Grid Token |
| `--off-white` | `#e9ecee` | Canvas / Surface Token |
| `--off-black` | `#13151f` | Canvas / Surface Token |
| `--color-secondary` | `#aab9c7` | Brand / Palette Token |
| `--gray` | `#6e8799` | Color / Atmospheric Token |
| `--dark-gray` | `#4c5e6b` | Canvas / Surface Token |
| `--expo-out` | `cubic-bezier(.14,1,.34,1)` | Motion / Timing Token |
| `--quint-out` | `cubic-bezier(.23,1,.32,1)` | Motion / Timing Token |
| `--z-sound-toggle` | `100` | Elevation / Border Token |
| `--chrome-bottom` | `2.6rem` | Dimension / Scale Token |
| `--gl-bleed` | `0px` | Dimension / Scale Token |
| `--border` | `hsla(0,0%,91%,.1)` | Elevation / Border Token |
| `--surface` | `#1a1a1a` | Canvas / Surface Token |
| `--grid-cols` | `12` | Layout / Spatial Grid Token |
| `--grid-gutter` | `1rem` | Layout / Spatial Grid Token |
| `--grid-max-width` | `calc(100% - 4.9rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav-bar> — `overworldaudio-com`)**:
   - Landmark `<nav class="nav-bar">` hosting `Overworld Audio` navigation (`Projects Projects · Studio Studio · Contact Contact`), DOM attributes (`data-v-a6ea98c7`, `data-v-3f1fbcc8`, `data-v-71a6f60d`, `data-v-05faef33`), and stylesheet rule `hover { color:var(--off-black) }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building unforgettable sonic exper`)**:
   - Landmark `<section class="hero">` presenting display lead `Building unforgettable sonic experiences` and copy excerpt *"Enter with sound Enter with sound"* over `#e9ecee` canvas and `#13151f` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Enter with sound Enter with sound`)**:
   - Landmark `<section class="hero">` rendering section `Enter with sound Enter with sound` with copy *"Enter without sound"*, asset references (`entry.B6zjpOmH.css`, `CmsText.BXNuEsZZ.css`, `IvarHeadline-Regular.woff2`, `PPFrama-Regular.woff2`), and grid rule `last-child { left:0;opacity:0;position:absolute;top:0;transform:translateY(120%);widt... }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Enter without sound`)**:
   - Landmark `<section class="hero">` framing `Enter without sound` and `Drag or scroll to navigate. Click markers to exp` (*"Drag or scroll to navigate. Click markers to explore. Drag to nav"*) with `#aab9c7` surface cards, `#6e8799` accents, and `first-child { opacity:0;transform:translateY(-120%) }`.
5. **Colophon & Global Directory Footer (<footer.is-visible> — `https://overworldaudio.com/`)**:
   - Landmark `<footer class="is-visible">` anchoring `Overworld Audio` footer links (`Projects Projects · Studio Studio · Contact Contact`), copy *"Drag or scroll to navigate. Click markers to explore."*, and `#1a1a1a` structural dividers.
