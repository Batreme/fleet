---
title: "UI & UX Architecture: www-rikoutaku-work"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-rikoutaku-work

## Overview & Design Identity
- **Target**: `www-rikoutaku-work` (**Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio**)
- **Production URL**: [https://www.rikoutaku.work/](https://www.rikoutaku.work/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f7` / `#0000ff`)
- **Summary**: Rikoutaku（リコウタク）のポートフォリオサイト「RI.Studio」。東京を拠点とするインタラクション／UI・UXデザイナー。3Dスクロール体験、アプリUI、Web、AR、モーションの作品集。Interaction & UI/UX Designer based in...
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`); rule `h1` (`font-size: clamp(29px,2.5vw,40px)`, `line-height: 1.36`, `letter-spacing: -.055em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 67.2px`, `font-weight: 550`, `letter-spacing: -4.16px`); rule `h2` (`font-size: clamp(94px,10.2vw,164px)`, `line-height: .94`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 12px`, `line-height: 1.65`, `letter-spacing: -.01em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0f7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111219` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e2e2eb` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.c2n-menu nav a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#e9e4d8` | `var(--text)` in `:root` |
| **Structural Hairline Border** | `#f2f2f8` | `var(--c2n-line)` in `:root` (`rgb(255 255 255 / 16%)`) |
| **Variable Token (`--ri-curtain-bg`)** | `#2e3bff` | `var(--ri-curtain-bg)` in `:root` |
| **Variable Token (`--bg`)** | `#0b0b0c` | `var(--bg)` in `:root` |
| **Variable Token (`--faint`)** | `#2a2926` | `var(--faint)` in `:root` |
| **Variable Token (`--accent`)** | `#ff3b24` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-2`)** | `#d92c18` | `var(--accent-2)` in `:root` |
| **Variable Token (`--circle-outline`)** | `#505050` | `var(--circle-outline)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ri-ease` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ri-ease-io` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Easing Token |
| `--ri-ease-in` | `cubic-bezier(.7, 0, .84, 0)` | Motion / Easing Token |
| `--ri-curtain-bg` | `#2e3bff` | Canvas / Surface Token |
| `--ri-curtain-ink` | `#f0f0f7` | Typography Ink Token |
| `--ri-curtain-z` | `2147483000` | Design System Custom Token |
| `--bg` | `#0b0b0c` | Canvas / Surface Token |
| `--text` | `#e9e4d8` | Typography Ink Token |
| `--dim` | `#e9e4d8` | Color / Atmospheric Token |
| `--faint` | `#2a2926` | Color / Atmospheric Token |
| `--accent` | `#ff3b24` | Brand / Palette Token |
| `--accent-2` | `#d92c18` | Brand / Palette Token |
| `--circle-outline` | `#505050` | Elevation / Border Token |
| `--ease` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ease-soft` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--pad` | `clamp(1.4rem, 2.4vw, 2.8rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c2n-header> — `www-rikoutaku-work`)**:
   - Landmark `<header class="c2n-header c2n-navigation-simple">` (`1440x99px`) hosting `Rikoutaku（リコウタク）— RI.Studio · Intera` navigation (`01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`), DOM attributes (`data-composition="two"`, `data-c2n-room="hero"`, `data-engine="three.js r165"`, `data-motion-system="studio"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.composition-two> — `Rikoutaku（リコウタク）— RI.Studio · Inte`)**:
   - Landmark `<section class="composition-two">` presenting display lead `Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX...` and copy excerpt *"Let’s create Let’s create something different. something differen"* over `#f0f0f7` canvas and `#111219` ink.
3. **Primary Showcase & Content Grid (<section.c2n-hero> — `Beyond the frame. B e y o n d t h `)**:
   - Landmark `<section class="c2n-hero">` rendering section `Beyond the frame. B e y o n d t h e f r a m e . I...` with copy *"INTERACTION & UI/UX DESIGN"*, asset references (`favicon.svg`, `theme-boot.js`, `2026-8-10-white.glb`, `fonts.googleapis.com`), and grid rule `selection { background:var(--accent);color:fff }`.
4. **Interactive Detail & Feature Matrix (<section.c2n-thinking> — `Selectedwork(06) S e l e c t e d w`)**:
   - Landmark `<section class="c2n-thinking c2n-paper">` framing `Selectedwork(06) S e l e c t e d w o r k ( 0 6 )` and `MofuLog M o f u L o g` (*"Let’s create L e t ’ s c r e a t e something different. s o m e t"*) with `#e2e2eb` surface cards, `#0000ff` accents, and `.light { --bg: ece6d8;--text: 1a1a18;--dim: 807c72;--faint: cdc6b4 }`.
5. **Colophon & Global Directory Footer (<footer.c2n-contact> — `https://www.rikoutaku.work/`)**:
   - Landmark `<footer class="c2n-contact c2n-paper">` anchoring `Rikoutaku（リコウタク）— RI.Studio · In` footer links (`01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`), copy *"Let’s create L e t ’ s c r e a t e"*, and `#f2f2f8` structural dividers.
