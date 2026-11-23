---
title: "UI & UX Architecture: lolawilde-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lolawilde-com

## Overview & Design Identity
- **Target**: `lolawilde-com` (**LOLA WILDE — Learning Me**)
- **Production URL**: [https://lolawilde.com/](https://lolawilde.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0b0a09` canvas, `#f3eee7` ink, `#ff0000` accent)
- **Summary**: Learning Me, the new album by LOLA WILDE. Listen on Spotify and read the lyrics.
- **Total Clean CSS Variables Extracted**: `183` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SpotifyMixMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 48px`, `font-weight: 700`); CSS variables `--display: 'Archivo Black', 'Arial Black', sans-serif`, `--text-link-standalone-display: block`, `--encore-overlay-trigger-display: block`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.8px`, `line-height: 60.8px`, `font-weight: 800`, `letter-spacing: -2.128px`); rule `.h2` (`font-size: clamp(2.1rem,4.6vw,3.8rem)`, `line-height: 1`, `letter-spacing: -.035em`, `font-weight: 800`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `body` (`font-size: 16px`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--encore-text-size-smaller-3: 0.625rem`, `--encore-text-size-smaller-2: 0.75rem`, `--encore-text-size-smaller: 0.875rem`; rule `.meta` (`font-size: 14px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0a09` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f3eee7` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1d1915` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.btn-red { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#f3727f` | `var(--text-negative)` in `:root` |
| **Structural Hairline Border** | `#272524` | `var(--line)` in `:root` (`rgba(243,238,231,.12)`) |
| **Variable Token (`--bg-2`)** | `#14110e` | `var(--bg-2)` in `:root` |
| **Variable Token (`--red`)** | `#d9141f` | `var(--red)` in `:root` |
| **Variable Token (`--amber`)** | `#c8823a` | `var(--amber)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0b0a09` | Canvas / Surface Token |
| `--bg-2` | `#14110e` | Canvas / Surface Token |
| `--bg-3` | `#1d1915` | Canvas / Surface Token |
| `--ink` | `#f3eee7` | Typography Ink Token |
| `--ink-2` | `rgba(243,238,231,.66)` | Typography Ink Token |
| `--ink-3` | `rgba(243,238,231,.38)` | Typography Ink Token |
| `--line` | `rgba(243,238,231,.12)` | Color / Atmospheric Token |
| `--red` | `#d9141f` | Color / Atmospheric Token |
| `--amber` | `#c8823a` | Color / Atmospheric Token |
| `--serif` | `'Archivo', 'Helvetica Neue', Arial, sans-serif` | Typography / Scale Token |
| `--sans` | `'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif` | Typography / Scale Token |
| `--display` | `'Archivo Black', 'Arial Black', sans-serif` | Dimension / Scale Token |
| `--radius` | `22px` | Elevation / Border Token |
| `--card-h` | `min(52vh, 500px)` | Dimension / Scale Token |
| `--card-w` | `calc(var(--card-h) * .64)` | Design System Custom Token |
| `--trans-x` | `0px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `lolawilde-com`)**:
   - Landmark `<header class="nav">` (`1440x82px`) hosting `LOLA WILDE — Learning Me` navigation (`Songs · Album · About · Shop · Press`), DOM attributes (`data-album-title`, `data-i="0"`, `data-i="1"`, `data-i="2"`), and stylesheet rule `etadata_condensedMetadataWrapper_... { inset-inline:16px 56px;bottom:32px;width:auto;position:absolute;font-siz... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `LOLA WILDE — LEARNING ME`)**:
   - Landmark `<section class="hero">` presenting display lead `LOLA WILDE — LEARNING ME` and copy excerpt *"Out now · New album"* over `#0b0a09` canvas and `#f3eee7` ink.
3. **Primary Showcase & Content Grid (<section.blk> — `LOLA WILDE — Learning Me`)**:
   - Landmark `<section class="blk">` rendering section `LOLA WILDE — Learning Me` with copy *"▶ Play and sing along"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `adata_condensedMetadataContainer_... { align-items:center;display:inline-flex }`.
4. **Interactive Detail & Feature Matrix (<section.about-sec> — `The girl in the front row, learnin`)**:
   - Landmark `<section class="about-sec">` framing `The girl in the front row, learning who she is.` and `Lipstick Confessions on vinyl.` (*"The Way You Said My Name"*) with `#1d1915` surface cards, `#ff0000` accents, and `F.CondensedMetadata_isPreRelease_... { inset-inline-start:12px;bottom:36px;-webkit-margin-end:154px;margin-inli... }`.
5. **Colophon & Global Directory Footer (<footer.pill> — `https://lolawilde.com/`)**:
   - Landmark `<footer class="pill">` anchoring `LOLA WILDE — Learning Me` footer links (`Songs · Album · About · Shop · Press`), copy *"Someone Else’s Version"*, and `#272524` structural dividers.
