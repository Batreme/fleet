---
title: "UI & UX Architecture: janiswanger-ch"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: janiswanger-ch

## Overview & Design Identity
- **Target**: `janiswanger-ch` (**Janis Wanger — Creative Engineer in Bern**)
- **Production URL**: [https://janiswanger.ch](https://janiswanger.ch)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e5e5e5` / `#007bc4`)
- **Summary**: Portfolio of Janis Wanger, a creative Frontend Engineer in Bern working across design and code. Projects, experience, and how to get in t...
- **Total Clean CSS Variables Extracted**: `76` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PolySans`
- **Body Font Stack**: `PolySans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 50.4px`, `line-height: 56.448px`, `font-weight: 700`, `letter-spacing: -1.26px`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e5e5e5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a19` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff8a3d` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#007bc4` | `var(--color-accent-inverted)` in `:root` |
| **Secondary / Muted Copy** | `#6d6a66` | `var(--color-muted)` in `:root` |
| **Structural Hairline Border** | `#c8c8c8` | `var(--color-hairline)` in `:root` (`1a1a1924`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-transition-duration` | `.45s` | Motion / Easing Token |
| `--page-transition-ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--page-transition-blur` | `1rem` | Motion / Easing Token |
| `--spacing-container-level-1` | `4svw` | Layout / Spatial Grid Token |
| `--spacing-container-level-2` | `6svw` | Layout / Spatial Grid Token |
| `--spacing-container-level-3` | `8svw` | Layout / Spatial Grid Token |
| `--spacing-container-level-4` | `10svw` | Layout / Spatial Grid Token |
| `--navbar-height` | `3rem` | Layout / Spatial Grid Token |
| `--font-sans` | `PolySans, ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `Georgia, ui-serif, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `1.33333` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.42857` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero-home> — `janiswanger-ch`)**:
   - Landmark `<header class="hero-home gap-2">` (`1430x900px`) hosting `Janis Wanger — Creative Engineer in ` navigation (`Main navigation`), DOM attributes (`data-hid="canonical"`, `data-hid="hreflang-de-CH"`, `data-hid="hreflang-en"`, `data-hid="hreflang-x-default"`), and stylesheet rule `webkit-media-controls { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.py-32> — `Janis is a Bern-based creative Fro`)**:
   - Landmark `<section class="py-32 scroll-mt-navbar-height">` presenting display lead `Janis is a Bern-based creative Frontend Engineer...` and copy excerpt *"Sometimes the frequencies just match"* over `#e5e5e5` canvas and `#1a1a19` ink.
3. **Primary Showcase & Content Grid (<section.scroll-mt-navbar-height> — `Technical skills`)**:
   - Landmark `<section class="py-32 scroll-mt-navbar-height">` rendering section `Technical skills` with copy *"O P E N T O G E T T I N G H I R E D ☆ ♡ ✧ O P E N T O G E T T I N"*, asset references (`entry.CeVzuLMF.css`, `HireBadge.BgIwIulx.css`, `AutoplayVideo.ulh4C2Gx.css`, `DsRIxAzj.js`), and grid rule `it-media-controls-start-playback-... { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<article.skills-enter> — `Want to work together ?`)**:
   - Landmark `<article class="skills-enter relative">` framing `Want to work together ?` and `Will I fit in your office?` (*"so beautiful patterns emerge."*) with `#ff8a3d` surface cards, `#007bc4` accents, and `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://janiswanger.ch`)**:
   - Landmark `<footer class="site-footer overflow-x-clip">` anchoring `Janis Wanger — Creative Engineer` footer links (`Main navigation`), copy *"Based in Switzerland, Bern"*, and `#c8c8c8` structural dividers.
