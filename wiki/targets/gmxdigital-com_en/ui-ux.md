# UI & UX Architecture: gmxdigital-com_en

## Overview & Design Identity
- **Target**: `gmxdigital-com_en` (**GMX Digital — Visual Engineering for Real Estate Launches**)
- **Production URL**: [https://gmxdigital.com/en/](https://gmxdigital.com/en/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#bcb4c7`)
- **Summary**: Launch films, 3D visualization and immersive digital experiences for real estate. GMX turns unbuilt architecture into desire before const...
- **Total Clean CSS Variables Extracted**: `39` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: CSS variables `--display: 'Inter',Arial,sans-serif`; rule `h1` (`font-size: clamp(3.2rem, 8.8vw, 9.3rem)`, `line-height: .84`, `letter-spacing: -.065em`, `font-weight: 470`)
- **Section Heading (`H2`)**: rule `h2` (`font-weight: 450`)
- **Body Copy**: rule `p` (`font-size: .96rem`, `line-height: 1.65`)
- **Metadata & Labels**: rule `small` (`font-size: .875rem`, `letter-spacing: .04em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#07090c` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#f2f0eb` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b7bec5` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#bcb4c7` | `var(--violet)` in `:root` |
| **Secondary / Muted Copy** | `#ee99cd` | `var(--rose)` in `:root` |
| **Structural Hairline Border** | `#c6a5fa` | `var(--accent)` in `:root` |
| **Variable Token (`--hairline`)** | `#ffffff24` | `var(--hairline)` in `:root` |
| **Variable Token (`--violet-deep`)** | `#75647f` | `var(--violet-deep)` in `:root` |
| **Variable Token (`--magenta`)** | `#b86b9f` | `var(--magenta)` in `:root` |
| **Variable Token (`--mist`)** | `#9fb5b7` | `var(--mist)` in `:root` |
| **Variable Token (`--accent-gradient`)** | `#bba2cf` | `var(--accent-gradient)` in `:root` |
| **Variable Token (`--accent-gradient`)** | `#8277a9` | `var(--accent-gradient)` in `:root` |
| **Variable Token (`--accent-gradient`)** | `#68899d` | `var(--accent-gradient)` in `:root` |
| **Variable Token (`--petrol`)** | `#07171b` | `var(--petrol)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#07090c` | Typography Ink Token |
| `--paper` | `#f2f0eb` | Canvas / Surface Token |
| `--muted` | `#b7bec5` | Color / Atmospheric Token |
| `--hairline` | `#ffffff24` | Color / Atmospheric Token |
| `--violet` | `#bcb4c7` | Color / Atmospheric Token |
| `--page-pad` | `clamp(1.25rem,4.5vw,6.25rem)` | Layout / Spatial Grid Token |
| `--ui` | `'Inter',Arial,sans-serif` | Design System Custom Token |
| `--display` | `'Inter',Arial,sans-serif` | Design System Custom Token |
| `--rose` | `#ee99cd` | Color / Atmospheric Token |
| `--accent` | `#c6a5fa` | Brand / Palette Token |
| `--violet-deep` | `#75647f` | Color / Atmospheric Token |
| `--magenta` | `#b86b9f` | Color / Atmospheric Token |
| `--mist` | `#9fb5b7` | Color / Atmospheric Token |
| `--accent-gradient` | `linear-gradient(90deg, #bba2cf 0%, #8277a9 48%, #68899d 100%)` | Brand / Palette Token |
| `--petrol` | `#07171b` | Color / Atmospheric Token |
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `gmxdigital-com_en`)**:
   - Landmark `<header class="site-header">` hosting `GMX Digital — Visual Engineering for` navigation (`Films · Process · Digital · Studio · PT`), DOM attributes (`data-matter-scene="genesis"`, `data-matter-canvas`, `data-matter-intro`, `data-intro-state="closed"`), and stylesheet rule `.gmx-edition h2 { font-weight:450; }`.
2. **Hero Stage & Focal Lead (<section.genesis> — `We engineer reality.`)**:
   - Landmark `<section class="genesis">` presenting display lead `We engineer reality.` and copy excerpt *"GMX // MATTER ENGINE PRIME MATTER"* over `#07090c` canvas and `#f2f0eb` ink.
3. **Primary Showcase & Content Grid (<section.selected-films> — `Direction you can see. And feel.`)**:
   - Landmark `<section class="selected-films">` rendering section `Direction you can see. And feel.` with copy *"GMX // MATTER ENGINE"*, asset references (`favicon.svg`, `inter-latin-wght-normal.woff2`, `gmx-smoke.webp`, `smoke-volumetric.webp`), and grid rule `.gmx-edition h2 em { color:b7becb; font-style:normal; }`.
4. **Interactive Detail & Feature Matrix (<section.studio> — `What makes a film a GMX film.`)**:
   - Landmark `<section class="studio">` framing `What makes a film a GMX film.` and `Architecture, understood` (*"The invisible becomes matter."*) with `#b7bec5` surface cards, `#bcb4c7` accents, and `.gmx-edition p { text-wrap:pretty; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://gmxdigital.com/en/`)**:
   - Landmark `<footer class="footer footer--signature">` anchoring `GMX Digital — Visual Engineering` footer links (`Films · Process · Digital · Studio · PT`), copy *"Preparing opening…"*, and `#c6a5fa` structural dividers.
