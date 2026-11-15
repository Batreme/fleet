# UI & UX Architecture: aestudio-studio_hozon

## Overview & Design Identity
- **Target**: `aestudio-studio_hozon` (**Hozon — Pickle & Fermented Food Recipe App**)
- **Production URL**: [https://aestudio.studio/hozon](https://aestudio.studio/hozon)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#20221c` / `#fff`)
- **Summary**: Find Japanese pickle recipes and fermented food recipes in Hozon for iPhone. Explore quick pickles and nukazuke, track jars and discover...
- **Total Clean CSS Variables Extracted**: `10` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Arial`
- **Body Font Stack**: `Georgia`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(100px,22.5vw,345px)`, `line-height: .76`, `letter-spacing: -.075em`, `font-weight: 900`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(32px,3.4vw,52px)`, `line-height: 1.04`, `letter-spacing: -.045em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 1.7`)
- **Metadata & Labels**: rule `nav` (`font-size: 14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#20221c` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#4b603c` | `var(--green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dedfd7` | `var(--line)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--paper)` in `:root` |
| **Secondary / Muted Copy** | `#62665b` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#008000` | `.brand-dot { background: green }` (`#008000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#20221c` | Typography Ink Token |
| `--green` | `#4b603c` | Color / Atmospheric Token |
| `--line` | `#dedfd7` | Color / Atmospheric Token |
| `--paper` | `#fff` | Canvas / Surface Token |
| `--muted` | `#62665b` | Color / Atmospheric Token |
| `--angle` | `-26deg` | Design System Custom Token |
| `--px` | `0px!important` | Dimension / Scale Token |
| `--sy` | `0px!important` | Dimension / Scale Token |
| `--study-shift` | `0px!important` | Dimension / Scale Token |
| `--rock` | `0deg!important` | Design System Custom Token |
| `--aestudio-studio--bg` | `#20221c` | Canvas Substrate (from `var(--ink)` in `:root`) |
| `--aestudio-studio--ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--aestudio-studio--surface` | `#dedfd7` | Surface Substrate (stylesheet-derived) |
| `--aestudio-studio--accent` | `#fff` | Interactive Accent (stylesheet-derived) |
| `--aestudio-studio--muted` | `#62665b` | Secondary Ink (stylesheet-derived) |
| `--aestudio-studio--border` | `#008000` | Structural Border (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `aestudio-studio_hozon`)**:
   - Landmark `<header class="header">` hosting `Hozon — Pickle & Fermented Food Reci` navigation (`The app · The idea`), DOM attributes (`data-depth="-0.65"`, `data-depth="0.65"`, `data-depth="-0.3"`, `data-depth="0.4"`), and stylesheet rule `button { font:inherit;color:inherit }`.
2. **Hero Stage & Focal Lead (<section.hero> — `HOZON`)**:
   - Landmark `<section class="hero">` presenting display lead `HOZON` and copy excerpt *"THE ART OF KEEPING."* over `#20221c` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.app-section> — `A little time. A lot of flavour.`)**:
   - Landmark `<section class="app-section section-wrap">` rendering section `A little time. A lot of flavour.` with copy *"A pickling companion. A slower kind of good."*, asset references (`hozon`, `favicon.svg`, `jar-v1.webp`, `cucumber-v2.webp`), and grid rule `img { display:block;max-width:100%;height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.idea-section> — `Pickle recipes. Fermented favourit`)**:
   - Landmark `<section class="idea-section section-wrap">` framing `Pickle recipes. Fermented favourites.` and `Less waste. More wonder.` (*"FRESH TODAY. SAVOURED TOMORROW."*) with `#dedfd7` surface cards, `#fff` accents, and `focus-visible { outline:3px solid var(--green);outline-offset:6px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://aestudio.studio/hozon`)**:
   - Landmark `<footer class="footer">` anchoring `Hozon — Pickle & Fermented Food ` footer links (`The app · The idea`), copy *"Turn everyday ingredients into something worth waiting for. "*, and `#008000` structural dividers.
