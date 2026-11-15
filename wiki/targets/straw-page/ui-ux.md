# UI & UX Architecture: straw-page

## Overview & Design Identity
- **Target**: `straw-page` (**Straw.Page - Extremely simple website builder**)
- **Production URL**: [https://straw.page](https://straw.page)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#94c3f4` accent)
- **Summary**: Straw.Page is the world's simplest website builder. Create unique websites from your mobile device.
- **Total Clean CSS Variables Extracted**: `4` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Baloo Paaji 2`
- **Body Font Stack**: `Bangers`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 80px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 18px`, `font-weight: 100`)
- **Body Copy**: rule `p` (`font-weight: 900`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.33333em`, `.75em`, `.875em`, `1em`, `2em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--pupilColor)` in `:root` |
| **Primary Typography Ink** | `#eee` | `.fa-border { border: #eee }` |
| **Elevated Surface / Card Substrate** | `#fff` | `.fa-inverse { color: #fff }` |
| **Interactive Accent / Highlight** | `#94c3f4` | `.first { background: #94c3f4 }` |
| **Secondary / Muted Copy** | `#0068ff` | `.first { background: #0068ff }` |
| **Structural Hairline Border** | `#df001d` | `.intro h1 { color: #df001d }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lefter` | `0px` | Dimension / Scale Token |
| `--eyeballHeight` | `40px` | Layout / Spatial Grid Token |
| `--eyeballWidth` | `40px` | Layout / Spatial Grid Token |
| `--pupilColor` | `#000` | Brand / Palette Token |
| `--straw-page-bg` | `#000` | Canvas Substrate (from `var(--pupilColor)` in `:root`) |
| `--straw-page-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--straw-page-surface` | `#fff` | Surface Substrate (stylesheet-derived) |
| `--straw-page-accent` | `#94c3f4` | Interactive Accent (stylesheet-derived) |
| `--straw-page-muted` | `#0068ff` | Secondary Ink (stylesheet-derived) |
| `--straw-page-border` | `#df001d` | Structural Border (stylesheet-derived) |
| `--straw-page-container` | `995px` | Container Bound (stylesheet-derived) |
| `--straw-page-gap` | `10px` | Grid Gutter (stylesheet-derived) |
| `--straw-page-pad` | `40px` | Lateral Padding (stylesheet-derived) |
| `--straw-page-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--straw-page-radius` | `50%` | Corner Radius (stylesheet-derived) |
| `--straw-page-fs-base` | `1.33333em` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.first> — `straw-page`)**:
   - Landmark `<header class="first">` hosting `Straw.Page - Extremely simple websit` navigation (`Pricing · Twitter · Premium · Email · Terms`), DOM attributes (`data-open="signIn"`, `data-open="signUp"`, `data-cf-beacon="("version":"2024.11.0..."`), and stylesheet rule `.fa-lg { font-size:1.33333em;line-height:.75em;vertical-align:-.0667em }`.
2. **Hero Stage & Focal Lead (<div.first> — `Sign in`)**:
   - Landmark `<div class="first">` presenting display lead `Sign in` and copy excerpt *"Check your email for a password reset link. Be sure to check your"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.first> — `Forgot password`)**:
   - Landmark `<div class="first">` rendering section `Forgot password` with copy *"Straw.Page lets you create unique websites straight from your pho"*, asset references (`all.min.css`, `jquery.min.js`, `apple-touch-icon.png`, `favicon-32x32.png`), and grid rule `.fa-xs { font-size:.75em }`.
4. **Interactive Detail & Feature Matrix (<div.first> — `Sign up`)**:
   - Landmark `<div class="first">` framing `Sign up` and `Straw.Page` (*"Get Started for Free"*) with `#fff` surface cards, `#94c3f4` accents, and `.fa-sm { font-size:.875em }`.
5. **Colophon & Global Directory Footer (<footer.innerSun> — `https://straw.page`)**:
   - Landmark `<footer class="innerSun">` anchoring `Straw.Page - Extremely simple we` footer links (`Pricing · Twitter · Premium · Email · Terms`), copy *"Create websites from your phone"*, and `#df001d` structural dividers.
