# UI & UX Architecture: lolawilde-com

## Overview & Design Identity
- **Target**: `lolawilde-com` (**LOLA WILDE — Learning Me**)
- **Production URL**: [https://lolawilde.com/](https://lolawilde.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000000` ink, `#000000` accent)
- **Summary**: Learning Me, the new album by LOLA WILDE. Listen on Spotify and read the lyrics.
- **Total Clean CSS Variables Extracted**: `176` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo Black`
- **Monospace / Technical Font Stack**: `SpotifyMixMono`
- **Hero Display (`H1`)**: CSS variables `--text-link-standalone-display: block`, `--encore-overlay-trigger-display: block`, `--display: 'Archivo Black', 'Arial Black', sans-serif`
- **Section Heading (`H2`)**: rule `.h2` (`font-size: clamp(2.1rem,4.6vw,3.8rem)`, `line-height: 1`, `letter-spacing: -.035em`, `font-weight: 800`)
- **Body Copy**: CSS variables `--text-base: #ffffff`; rule `body` (`font-size: 16px`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--encore-text-size-smaller-3: 0.625rem`, `--encore-text-size-smaller-2: 0.75rem`, `--encore-text-size-smaller: 0.875rem`; rule `.meta` (`font-size: 14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `var(--encore-list-row-bg)` in `:root` |
| **Primary Typography Ink** | `#121212` | `var(--background-base)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1f1f1f` | `var(--background-highlight)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--background-press)` in `:root` |
| **Secondary / Muted Copy** | `#2a2a2a` | `var(--background-elevated-highlight)` in `:root` |
| **Structural Hairline Border** | `#191919` | `var(--background-elevated-press)` in `:root` |
| **Variable Token (`--encore-overlay-box-shadow`)** | `#0000004d` | `var(--encore-overlay-box-shadow)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--trans-x` | `0px` | Dimension / Scale Token |
| `--encore-shortest-1` | `50ms` | Motion / Timing Token |
| `--encore-shortest-2` | `100ms` | Motion / Timing Token |
| `--encore-shortest-3` | `150ms` | Motion / Timing Token |
| `--encore-shortest-4` | `200ms` | Motion / Timing Token |
| `--encore-short-1` | `250ms` | Motion / Timing Token |
| `--encore-short-2` | `300ms` | Motion / Timing Token |
| `--encore-productive` | `cubic-bezier(0.3,0,0,1)` | Motion / Timing Token |
| `--encore-productive-decelerate` | `cubic-bezier(0,0,0.2,1)` | Motion / Timing Token |
| `--encore-productive-accelerate` | `cubic-bezier(0.8,0,1,1)` | Motion / Timing Token |
| `--encore-productive-exit-duration` | `var(--encore-shortest-4)` | Motion / Easing Token |
| `--encore-opacity-disabled` | `0.3` | Design System Custom Token |
| `--encore-opacity-active` | `0.7` | Design System Custom Token |
| `--encore-border-radius-rounded` | `9999px` | Elevation / Border Token |
| `--encore-overlay-box-shadow` | `0 4px 12px 0 #0000004d` | Elevation / Border Token |
| `--encore-overlay-drop-shadow` | `0 4px 6px #0000004d` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `lolawilde-com`)**:
   - Landmark `<header class="nav">` hosting `LOLA WILDE — Learning Me` navigation (`Songs · Album · About · Shop · Press`), DOM attributes (`data-album-title`, `data-i="0"`, `data-i="1"`, `data-i="2"`), and stylesheet rule `.Error_wrapper__7m1Fk { display:flex;align-items:center;flex-direction:column }`.
2. **Hero Stage & Focal Lead (<section.hero> — `LOLA WILDE — Learning Me`)**:
   - Landmark `<section class="hero">` presenting display lead `LOLA WILDE — Learning Me` and copy excerpt *"Out now · New album"* over `#0000` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.blk> — `Learning Me`)**:
   - Landmark `<section class="blk">` rendering section `Learning Me` with copy *"01 Golden ▶ Play and sing along"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `.Error_title__KvfPv { font-size:48px;line-height:1;letter-spacing:-.04em;margin:40px 0 16px;fo... }`.
4. **Interactive Detail & Feature Matrix (<section.about-sec> — `The girl in the front row, learnin`)**:
   - Landmark `<section class="about-sec">` framing `The girl in the front row, learning who she is.` and `Lipstick Confessions on vinyl.` (*"▶ Play and sing along"*) with `#1f1f1f` surface cards, `#000000` accents, and `.Error_description__h_wjs { line-height:24px;max-width:507px;margin:0 0 40px;font-weight:200;display... }`.
5. **Colophon & Global Directory Footer (<footer.pill> — `https://lolawilde.com/`)**:
   - Landmark `<footer class="pill">` anchoring `LOLA WILDE — Learning Me` footer links (`Songs · Album · About · Shop · Press`), copy *"02 The Way You Said My Name ▶ Play and sing along"*, and `#191919` structural dividers.
