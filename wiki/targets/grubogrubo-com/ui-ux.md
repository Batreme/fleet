# UI & UX Architecture: grubogrubo-com

## Overview & Design Identity
- **Target**: `grubogrubo-com` (**GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw**)
- **Production URL**: [https://grubogrubo.com](https://grubogrubo.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#4c0aaf` / `#bcb8c5`)
- **Summary**: Independent creative studio in Warsaw: creative concepts, campaigns, storytelling, animation, 3D, CGI and interactive experiences.
- **Total Clean CSS Variables Extracted**: `8` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Arial`
- **Body Font Stack**: `Arial Black`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(33px,3vw,54px)`, `line-height: .89`, `letter-spacing: -.06em`, `font-weight: 800`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(70px,12vw,210px)`, `line-height: .84`, `letter-spacing: -.092em`)
- **Body Copy**: rule `p` (`font-size: 12px`, `line-height: 1.5`)
- **Metadata & Labels**: rule `nav` (`font-size: 10px`, `letter-spacing: .13em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4c0aaf` | `var(--acid)` in `:root` |
| **Primary Typography Ink** | `#f5f4f0` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c3a0ec` | `var(--fx-accent)` in `:root` |
| **Interactive Accent / Highlight** | `#bcb8c5` | `.cookie-settings-launcher button { color: #bcb8c5 }` |
| **Secondary / Muted Copy** | `#494551` | `.cookie-settings-launcher button { border: #494551 }` |
| **Structural Hairline Border** | `#ffffff` | `kie-settings-launcher button:fo... { color: white }` (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--acid` | `#4c0aaf` | Color / Atmospheric Token |
| `--paper` | `#f5f4f0` | Canvas / Surface Token |
| `--violet` | `#4c0aaf` | Color / Atmospheric Token |
| `--accent` | `var(--violet)` | Brand / Palette Token |
| `--fx-accent` | `#c3a0ec` | Brand / Palette Token |
| `--mx` | `50%` | Dimension / Scale Token |
| `--my` | `50%` | Dimension / Scale Token |
| `--reveal-delay` | `0ms` | Motion / Easing Token |
| `--grubogrubo-com-bg` | `#4c0aaf` | Canvas Substrate (from `var(--acid)` in `:root`) |
| `--grubogrubo-com-ink` | `#ffffff` | Primary Typography Ink (stylesheet-derived) |
| `--grubogrubo-com-surface` | `#c3a0ec` | Surface Substrate (stylesheet-derived) |
| `--grubogrubo-com-accent` | `#bcb8c5` | Interactive Accent (stylesheet-derived) |
| `--grubogrubo-com-muted` | `#494551` | Secondary Ink (stylesheet-derived) |
| `--grubogrubo-com-border` | `#ffffff` | Structural Border (stylesheet-derived) |
| `--grubogrubo-com-container` | `620px` | Container Bound (stylesheet-derived) |
| `--grubogrubo-com-gap` | `22px` | Grid Gutter (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `grubogrubo-com`)**:
   - Landmark `<header class="site-header">` hosting `GruboGrubo — Creative Ideas & Visual` navigation (`WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`), DOM attributes (`data-language="en"`, `data-i18n="manifest"`, `data-i18n="navWork"`, `data-i18n="navStudio"`), and stylesheet rule `.cookie-settings-launcher { position:fixed;left:12px;bottom:12px;z-index:40 }`.
2. **Hero Stage & Focal Lead (<section.intro> — `IDEA`)**:
   - Landmark `<section class="intro">` presenting display lead `IDEA` and copy excerpt *"WE TURN COMPLEX THINGS INTO COMPELLING EXPERIENCES."* over `#4c0aaf` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.about> — `WE DON’T THINK SMALL.`)**:
   - Landmark `<section class="about">` rendering section `WE DON’T THINK SMALL.` with copy *"Ideas that shift perspectives. Concepts, campaigns and storytelli"*, asset references (`style.css`, `cookie-consent.css`, `header-logo.png (GRUBO)`, `maciej-scroll.mp4`), and grid rule `settings-launcher button:focus-vi... { opacity:1;background:4c0aaf;color:white }`.
4. **Interactive Detail & Feature Matrix (<section.team> — `THE IDEA COMES FIRST.`)**:
   - Landmark `<section class="team founder-cinematic">` framing `THE IDEA COMES FIRST.` and `Advertising films` (*"INDEPENDENT CREATIVE STUDIO"*) with `#c3a0ec` surface cards, `#bcb8c5` accents, and `.cookie-banner strong { font-size:14px }`.
5. **Colophon & Global Directory Footer (<footer.contact> — `https://grubogrubo.com`)**:
   - Landmark `<footer class="contact">` anchoring `GruboGrubo — Creative Ideas & Vi` footer links (`WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`), copy *"Ideas. Stories. Images. Products. Experiences. Whatever the "*, and `#ffffff` structural dividers.
