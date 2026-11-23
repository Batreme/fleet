---
title: "UI & UX Architecture: perappelgren-de"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: perappelgren-de

## Overview & Design Identity
- **Target**: `perappelgren-de` (**Per Appelgren**)
- **Production URL**: [https://perappelgren.de/](https://perappelgren.de/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#213547`)
- **Summary**: Per Appelgren is a Paris and Berlin based photographer working across fashion, beauty, editorial, and commercial image-making.
- **Total Clean CSS Variables Extracted**: `30` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `neueMontreal`
- **Body Font Stack**: `neueMontreal`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: observed font-size ladder: `22px`, `16px`, `29px`, `10px`, `1em`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 22px`, `line-height: 28px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f0f15` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1f1f2b` | `:hover { background-color: #1f1f2b }` |
| **Interactive Accent / Highlight** | `#213547` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#33333d` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#33333d` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-neue-montreal` | `"neueMontreal", "neueMontreal Fallback"` | Typography / Scale Token |
| `--font-vemior` | `"vemior", "vemior Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-neue-montreal)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--tracking-normal` | `0em` | Typography / Scale Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.home-nav> — `perappelgren-de`)**:
   - Landmark `<nav class="home-nav top-0">` (`1440x40px`) hosting `Per Appelgren` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-gallery-title-track="true"`, `data-cursor="arrow"`), and stylesheet rule `real_94799760-module__C5EBEW__cla... { font-family:neueMontreal,neueMontreal Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Per Appelgren`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Per Appelgren` and copy excerpt *"Hi! I am Per! I'm a German-Swedish photographer based between Par"* over `#ffffff` canvas and `#0f0f15` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="relative w-full">` rendering section `Featured Work & Interactive Showcase` with copy *"CASABLANCA PRE-FALL ´26 CAMPAIGN"*, asset references (`vemior-s.p.0loat6znd6m5-.otf`, `12mrv9~q-_9yg.css`, `0wjx1qarcnur7.js`, `14x4ulv7j4.e5.js`), and grid rule `treal_94799760-module__C5EBEW__va... { --font-neue-montreal:"neueMontreal", "neueMontreal Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.h-auto> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="h-auto relative">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"ARCHIVE A R C H I V E"*) with `#1f1f2b` surface cards, `#213547` accents, and `mior_bd07f20d-module__cotiFq__cla... { font-family:vemior,vemior Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.z-42> — `https://perappelgren.de/`)**:
   - Landmark `<footer class="z-42 relative">` anchoring `Per Appelgren` footer links (`Overview · Index · Archive · About · Contact`), copy *"CONTACT C O N T A C T"*, and `#33333d` structural dividers.
