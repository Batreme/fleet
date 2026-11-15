# UI & UX Architecture: inherited-band

## Overview & Design Identity
- **Target**: `inherited-band` (**INHERITED**)
- **Production URL**: [https://inherited.band/](https://inherited.band/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#FCFFFE` ink, `#d50305` accent)
- **Summary**: INHERITED BAND
- **Total Clean CSS Variables Extracted**: `5` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Founders Grotesk`
- **Body Font Stack**: `Founders Grotesk`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.h1` (`line-height: .85`, `letter-spacing: -.1em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15rem`, `115rem`, `80rem`, `25rem`, `12px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15rem`, `115rem`, `80rem`, `25rem`, `12px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15rem`, `115rem`, `80rem`, `25rem`, `12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `#loading { background: #000 }` |
| **Primary Typography Ink** | `#ff03` | `#grid div { background: #ff03 }` |
| **Elevated Surface / Card Substrate** | `#eee2c5` | `#nav-mobile-bar span { background: #eee2c5 }` |
| **Interactive Accent / Highlight** | `#d50305` | `.header { background: #d50305 }` |
| **Secondary / Muted Copy** | `#FCFFFE` | `<meta name="theme-color" content="#FCFFFE">` in `dom.html` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--margin` | `20rem` | Layout / Spatial Grid Token |
| `--gap` | `20rem` | Layout / Spatial Grid Token |
| `--column` | `calc((var(--rvw) * 100 - var(--margin) * 2 - var(--gap) * 5) / 6)` | Layout / Spatial Grid Token |
| `--rvw` | `14.4px` | Layout / Spatial Grid Token |
| `--right-height` | `692px` | Layout / Spatial Grid Token |
| `--inherited-band-bg` | `#000` | Canvas Substrate (from `#loading { background: #000 }`) |
| `--inherited-band-ink` | `#FCFFFE` | Primary Typography Ink (stylesheet-derived) |
| `--inherited-band-surface` | `#eee2c5` | Surface Substrate (stylesheet-derived) |
| `--inherited-band-accent` | `#d50305` | Interactive Accent (stylesheet-derived) |
| `--inherited-band-muted` | `#FCFFFE` | Secondary Ink (stylesheet-derived) |
| `--inherited-band-border` | `#FCFFFE` | Structural Border (stylesheet-derived) |
| `--inherited-band-container` | `1024px` | Container Bound (stylesheet-derived) |
| `--inherited-band-gap` | `20rem` | Grid Gutter (stylesheet-derived) |
| `--inherited-band-pad` | `15rem` | Lateral Padding (stylesheet-derived) |
| `--inherited-band-ease` | `cubic-bezier(.6,.14,0,1)` | Primary Easing Function |
| `--inherited-band-radius` | `0px` | Corner Radius (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `inherited-band`)**:
   - Landmark `<header class="header">` hosting `INHERITED` navigation (`INHERITED · Spotify · Instagram · Tik Tok · Contact us`), DOM attributes (`data-touch="false"`, `data-custom-loaded="true"`, `data-title="about"`, `data-title="members"`), and stylesheet rule `body { font-size:15rem;line-height:1.21;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.member> — `I N H E R I T E D`)**:
   - Landmark `<section class="member no-transition">` presenting display lead `I N H E R I T E D` and copy excerpt *"m e e t @ i n h e r i t e d . b a n d"* over `#000` canvas and `#FCFFFE` ink.
3. **Primary Showcase & Content Grid (<section.member> — `2016 Deathcore Metalcore`)**:
   - Landmark `<section class="member no-transition">` rendering section `2016 Deathcore Metalcore` with copy *"Metalcore Deathcore"*, asset references (`fav.ico`, `fav.svg`, `fav-mask.svg`, `apple-touch.png`), and grid rule `.h3 { line-height:1;letter-spacing:-.015em;margin:0;text-transform:uppercase;f... }`.
4. **Interactive Detail & Feature Matrix (<section.member> — `E d e r A n a y a`)**:
   - Landmark `<section class="member no-transition">` framing `E d e r A n a y a` and `Guitarist Producer` (*"Guitarist Producer"*) with `#eee2c5` surface cards, `#d50305` accents, and `.h1 { font-size:115rem }`.
5. **Colophon & Global Directory Footer (<footer.items> — `https://inherited.band/`)**:
   - Landmark `<footer class="items">` anchoring `INHERITED` footer links (`INHERITED · Spotify · Instagram · Tik Tok · Contact us`), copy *"( Me, Myself, and Sam )"*, and `#FCFFFE` structural dividers.
