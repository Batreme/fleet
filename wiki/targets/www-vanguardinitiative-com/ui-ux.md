# UI & UX Architecture: www-vanguardinitiative-com

## Overview & Design Identity
- **Target**: `www-vanguardinitiative-com` (**Vanguard Initiative · Software Development Company in Laos**)
- **Production URL**: [https://www.vanguardinitiative.com/](https://www.vanguardinitiative.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e5e5e5` / `#fff`)
- **Summary**: Vanguard Initiative is a Laos-based software company that designs, builds, and ships production-ready web applications, MVPs, internal pl...
- **Total Clean CSS Variables Extracted**: `210` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Hubot Sans`
- **Body Font Stack**: `Hubot Sans Fallback`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--font-display: var(--font-display)`, `--text-display-s: clamp(2.5rem, 1.5rem + 4vw, 5rem)`; rule `h1` (`font-size: var(--text-3xl)`, `line-height: var(--tw-leading,var(...`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: var(--text-2xl)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-body: var(--font-mona), var(--font-noto-sans-lao), system-ui, sans-serif`; rule `p` (`line-height: calc(var(--spacing) * 7)`)
- **Metadata & Labels**: CSS variables `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e5e5e5` | `var(--color-neutral-200)` in `:root` |
| **Primary Typography Ink** | `#262626` | `var(--color-neutral-800)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--color-white)` in `:root` |
| **Secondary / Muted Copy** | `#b00a1d` | `var(--color-danger-ink)` in `:root` |
| **Structural Hairline Border** | `#0000` | `textarea { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-hubot` | `"Hubot Sans", "Hubot Sans Fallback"` | Typography / Scale Token |
| `--font-mona` | `"Mona Sans", "Mona Sans Fallback"` | Typography / Scale Token |
| `--font-geist-mono` | `"Geist Mono", "Geist Mono Fallback"` | Typography / Scale Token |
| `--font-noto-sans-lao` | `"Noto Sans Lao", "Noto Sans Lao Fallback"` | Typography / Scale Token |
| `--color-neutral-200` | `#e5e5e5` | Brand / Palette Token |
| `--color-neutral-800` | `#262626` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xs` | `20rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-nav> — `www-vanguardinitiative-com`)**:
   - Landmark `<header class="site-nav">` hosting `Vanguard Initiative · Software Devel` navigation (`Vision · Services · Customers · Work · News`), DOM attributes (`data-glass="refract"`, `data-starfield="ready"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `sans_e77d6951-module__FFcELq__cla... { font-family:Hubot Sans,Hubot Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.surface-space> — `Vanguard Initiative : Software eng`)**:
   - Landmark `<section class="surface-space">` presenting display lead `Vanguard Initiative : Software engineered for dec...` and copy excerpt *"Vientiane · 17.97° N · 102.63° E"* over `#e5e5e5` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.surface-haze> — `Vision : Driving modern innovation`)**:
   - Landmark `<section class="surface-haze">` rendering section `Vision : Driving modern innovation to build a pro...` with copy *"Build technology. Create innovation. Drive growth."*, asset references (`671921b99e4f15ea-s.p.144u-zwhc_ek...`, `797e433ab948586e-s.p.08e28id.o-ok...`, `88a013264a4e85f3-s.p.0.1xv-4ms-j6...`, `896ab7b170aff81a-s.p.0x1fcv_1lywi...`), and grid rule `sans_e77d6951-module__FFcELq__var... { --font-hubot:"Hubot Sans", "Hubot Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<article.vision__block> — `Mission : Build and incubate start`)**:
   - Landmark `<article class="vision__block brackets">` framing `Mission : Build and incubate startups that use ne...` and `Four orbits around one mission.` (*"Create innovation."*) with `#000` surface cards, `#fff` accents, and `sans_784dac51-module__aFRYXa__cla... { font-family:Mona Sans,Mona Sans Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.surface-space> — `https://www.vanguardinitiative.com/`)**:
   - Landmark `<footer class="surface-space relative">` anchoring `Vanguard Initiative · Software D` footer links (`Vision · Services · Customers · Work · News`), copy *"Vanguard Initiative :"*, and `#0000` structural dividers.
