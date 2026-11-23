---
title: "UI & UX Architecture: www-urbik-eu"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-urbik-eu

## Overview & Design Identity
- **Target**: `www-urbik-eu` (**Jakub 'Urbik' Urbanec · Web Developer · DJ · AV artist**)
- **Production URL**: [https://www.urbik.eu/](https://www.urbik.eu/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080909` / `#d3ff3f`)
- **Summary**: Senior web developer and DJ with alias Urbik created this personal portfolio
- **Total Clean CSS Variables Extracted**: `127` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Oxanium`
- **Body Font Stack**: `Oxanium`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: normal`, `font-weight: 700`); CSS variables `--ds-text-4xl: 19px`, `--ds-text-5xl: 24px`, `--ds-text-display: clamp(32px, 8vw, 72px)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: normal`, `font-weight: 700`); CSS variables `--ds-text-2xl: 16px`, `--ds-text-3xl: 18px`, `--ds-text-h2: clamp(26px, 4vw, 48px)`; rule `h2` (`font-size: 18px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--ds-text-base: 13px`, `--ds-leading-body: 1.6`; rule `p` (`line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 26px`, `line-height: normal`, `font-weight: 400`); CSS variables `--ds-font-mono: ui-monospace, SFMono-Regular, Menlo, monospace`, `--ds-text-xs: 10px`, `--ds-text-sm: 11px`; rule `small` (`font-size: 0.55rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080909` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f1f1ec` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#101212` | `var(--ds-color-bg-soft)` in `:root` |
| **Interactive Accent / Highlight** | `#d3ff3f` | `var(--ds-color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#676b68` | `var(--ds-color-text-faint)` in `:root` |
| **Structural Hairline Border** | `#303432` | `var(--ds-color-line)` in `:root` |
| **Variable Token (`--ds-color-bg-deep`)** | `#0b0d0d` | `var(--ds-color-bg-deep)` in `:root` |
| **Variable Token (`--ds-color-card`)** | `#131515` | `var(--ds-color-card)` in `:root` |
| **Variable Token (`--ds-color-card-hover`)** | `#181b1b` | `var(--ds-color-card-hover)` in `:root` |
| **Variable Token (`--ds-color-text-soft`)** | `#9d9f9b` | `var(--ds-color-text-soft)` in `:root` |
| **Variable Token (`--ds-color-line-strong`)** | `#555b57` | `var(--ds-color-line-strong)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--menu-row-height` | `76px` | Layout / Spatial Grid Token |
| `--menu-height` | `var(--menu-row-height)` | Layout / Spatial Grid Token |
| `--ds-color-bg` | `#080909` | Canvas / Surface Token |
| `--ds-color-bg-rgb` | `8 9 9` | Canvas / Surface Token |
| `--ds-color-bg-soft` | `#101212` | Canvas / Surface Token |
| `--ds-color-bg-deep` | `#0b0d0d` | Canvas / Surface Token |
| `--ds-color-card` | `#131515` | Brand / Palette Token |
| `--ds-color-card-hover` | `#181b1b` | Brand / Palette Token |
| `--ds-color-text` | `#f1f1ec` | Typography Ink Token |
| `--ds-color-text-rgb` | `241 241 236` | Typography Ink Token |
| `--ds-color-text-soft` | `#9d9f9b` | Typography Ink Token |
| `--ds-color-text-faint` | `#676b68` | Typography Ink Token |
| `--ds-color-line` | `#303432` | Brand / Palette Token |
| `--ds-color-line-strong` | `#555b57` | Brand / Palette Token |
| `--ds-color-accent` | `#d3ff3f` | Brand / Palette Token |
| `--ds-color-accent-soft` | `rgba(211, 255, 63, 0.12)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-urbik-eu`)**:
   - Landmark `<header class="header header--intro">` (`1440x163px`) hosting `Jakub 'Urbik' Urbanec · Web Develope` navigation (`General · Developer · DJing`), DOM attributes (`data-engine="three.js r186"`, `data-util="music"`, `data-util="visuals"`, `data-util="blog"`), and stylesheet rule `eraser-app { top: 25px; }`.
2. **Hero Stage & Focal Lead (<section.content__content> — `Jakub 'Urbik' Urbanec`)**:
   - Landmark `<section class="content__content">` presenting display lead `Jakub 'Urbik' Urbanec` and copy excerpt *"Hello, I’m Jakub Urbanec — a Prague-based web developer and DJ pe"* over `#080909` canvas and `#f1f1ec` ink.
3. **Primary Showcase & Content Grid (<article.content__child> — `Developer, DJ and explorer of digi`)**:
   - Landmark `<article class="content__child content__child--basic">` rendering section `Developer, DJ and explorer of digital things` with copy *"I have spent more than a decade working with the web, primarily o"*, asset references (`apple-touch-icon.png`, `favicon-96x96.png`, `favicon.ico`, `oxanium.woff2`), and grid rule `eraser-app canvas { display: block; }`.
4. **Interactive Detail & Feature Matrix (<section.ds-article__section> — `Three important parts of my life`)**:
   - Landmark `<section class="ds-article__section">` framing `Three important parts of my life` and `Web development` (*"Outside software development, music is a major part of my life. I"*) with `#101212` surface cards, `#d3ff3f` accents, and `video-bg .video { position: fixed; top: 0; left: 0; width: 100%; height: 100%; object-fit:... }`.
5. **Colophon & Global Directory Footer (<footer.header--intro> — `https://www.urbik.eu/`)**:
   - Landmark `<footer class="header--intro">` anchoring `Jakub 'Urbik' Urbanec · Web Deve` footer links (`General · Developer · DJing`), copy *"Urbik / Dark Atmo Breaks"*, and `#303432` structural dividers.
