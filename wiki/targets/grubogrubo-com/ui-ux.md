---
title: "UI & UX Architecture: grubogrubo-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: grubogrubo-com

## Overview & Design Identity
- **Target**: `grubogrubo-com` (**GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw**)
- **Production URL**: [https://grubogrubo.com](https://grubogrubo.com)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#050506` / `#5f1bd0`)
- **Summary**: Independent creative studio in Warsaw: creative concepts, campaigns, storytelling, animation, 3D, CGI and interactive experiences.
- **Total Clean CSS Variables Extracted**: `10` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Arial Black`
- **Body Font Stack**: `Impact`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60.48px`, `line-height: 59.2704px`, `font-weight: 800`, `letter-spacing: -3.6288px`); rule `h1` (`font-size: clamp(33px,3vw,54px)`, `line-height: .89`, `letter-spacing: -.06em`, `font-weight: 800`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 144px`, `line-height: 131.04px`, `font-weight: 900`, `letter-spacing: -12.24px`); rule `h2` (`font-size: clamp(70px,12vw,210px)`, `line-height: .84`, `letter-spacing: -.092em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: 1.3px`); rule `nav` (`font-size: 10px`, `letter-spacing: .13em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#050506` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1f1f1f` | `.page-progress { background: #1f1f1f }` |
| **Interactive Accent / Highlight** | `#5f1bd0` | `.gg-cb-btn:hover { background: #5f1bd0 }` |
| **Secondary / Muted Copy** | `#d1d1d1` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#777777` | `.site-header nav a:last-child { border: #777777 }` |
| **Variable Token (`--acid`)** | `#4c0aaf` | `var(--acid)` in `:root` |
| **Variable Token (`--paper`)** | `#f5f4f0` | `var(--paper)` in `:root` |
| **Variable Token (`--fx-accent`)** | `#c3a0ec` | `var(--fx-accent)` in `:root` |

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
| `--gg-cb-violet` | `var(--violet,#4c0aaf)` | Color / Atmospheric Token |
| `--reveal-delay` | `0ms` | Motion / Easing Token |
| `--gg-marquee-time` | `136s` | Motion / Timing Token |
| `--grubogrubo-com-bg` | `#050506` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--grubogrubo-com-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--grubogrubo-com-surface` | `#1f1f1f` | Surface Substrate (computed-derived) |
| `--grubogrubo-com-accent` | `#5f1bd0` | Interactive Accent (computed-derived) |
| `--grubogrubo-com-muted` | `#d1d1d1` | Secondary Ink (computed-derived) |
| `--grubogrubo-com-border` | `#777777` | Structural Border (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `grubogrubo-com`)**:
   - Landmark `<header class="site-header">` (`1440x89px`) hosting `GruboGrubo — Creative Ideas & Visual` navigation (`WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`), DOM attributes (`data-language="en"`, `data-i18n="manifest"`, `data-i18n="navWork"`, `data-i18n="navStudio"`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.intro> — `AN IDEA WITH CHARACTER.`)**:
   - Landmark `<section class="intro">` presenting display lead `AN IDEA WITH CHARACTER.` and copy excerpt *"WE TURN COMPLEX THINGS INTO COMPELLING EXPERIENCES."* over `#050506` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.about> — `WE DON’T THINK SMALL.`)**:
   - Landmark `<section class="about">` rendering section `WE DON’T THINK SMALL.` with copy *"INDEPENDENT CREATIVE STUDIO"*, asset references (`style.css`, `cookie-consent.css`, `callback.css`, `home-sections.css`), and grid rule `body { margin:0;background:050506;color:fff;font-family:Arial,Helvetica,sans-se... }`.
4. **Interactive Detail & Feature Matrix (<section.team> — `THE IDEA COMES FIRST.`)**:
   - Landmark `<section class="team founder-cinematic">` framing `THE IDEA COMES FIRST.` and `Advertising films` (*"Ideas. Stories. Images. Products. Experiences. Whatever the chall"*) with `#1f1f1f` surface cards, `#5f1bd0` accents, and `button { cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.contact> — `https://grubogrubo.com`)**:
   - Landmark `<footer class="contact">` anchoring `GruboGrubo — Creative Ideas & Vi` footer links (`WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`), copy *"We don’t start with technology. We start with a question: wh"*, and `#777777` structural dividers.
