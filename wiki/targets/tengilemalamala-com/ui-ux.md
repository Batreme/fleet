---
title: "UI & UX Architecture: tengilemalamala-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: tengilemalamala-com

## Overview & Design Identity
- **Target**: `tengilemalamala-com` (**Luxury Safari Experiences in Greater Kruger & Sabi Sand · Tengile MalaMa...**)
- **Production URL**: [https://tengilemalamala.com/](https://tengilemalamala.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5eee9` canvas, `#373f1d` ink, `#5c6e21` accent)
- **Summary**: Discover luxury safari experiences in Greater Kruger and Sabi Sand. Wildlife, luxury accommodation and unforgettable Big Five encounters....
- **Total Clean CSS Variables Extracted**: `5` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Fragment`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 120px`, `line-height: 108px`, `font-weight: 220`, `letter-spacing: -2.4px`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 20px`, `line-height: 24px`, `font-weight: 310`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: -0.16px`); rule `p` (`letter-spacing: -.01em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 40px`, `line-height: 40px`, `font-weight: 220`, `letter-spacing: -0.16px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5eee9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#373f1d` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fbf8f6` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#5c6e21` | `css-module__3-RGkq__cookie a:fo... { color: #5c6e21 }` |
| **Secondary / Muted Copy** | `#a5a593` | `odule-scss-module__mj8AIq__subm... { color: #a5a593 }` |
| **Structural Hairline Border** | `#e3e1d4` | `Banner-module-scss-module__3-RG... { border-top: #e3e1d4 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lvh` | `1vh` | Layout / Spatial Grid Token |
| `--svh` | `1vh` | Layout / Spatial Grid Token |
| `--offset` | `150dvw` | Dimension / Scale Token |
| `--size` | `1440` | Layout / Spatial Grid Token |
| `--duration` | `120s` | Motion / Easing Token |
| `--plyr-color-main` | `#fbf8f6` | Brand / Palette Token |
| `--plyr-video-control-color` | `#fbf8f6` | Brand / Palette Token |
| `--plyr-font-size-small` | `14px` | Typography / Scale Token |
| `--plyr-range-track-height` | `2px` | Layout / Spatial Grid Token |
| `--plyr-range-thumb-height` | `0px` | Layout / Spatial Grid Token |
| `--plyr-video-progress-buffered-background` | `#fbf8f61a` | Canvas / Surface Token |
| `--tengilemalamala--bg` | `#f5eee9` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--tengilemalamala--ink` | `#373f1d` | Primary Typography Ink (computed-derived) |
| `--tengilemalamala--surface` | `#fbf8f6` | Surface Substrate (computed-derived) |
| `--tengilemalamala--accent` | `#5c6e21` | Interactive Accent (computed-derived) |
| `--tengilemalamala--muted` | `#a5a593` | Secondary Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `tengilemalamala-com`)**:
   - Landmark `<header class="site-header">` (`1440x34px`) hosting `Luxury Safari Experiences in Greater` navigation (`About · Accommodation · Experiences · Conservation · Partner Hub`), DOM attributes (`data-next-head`, `data-nscript="beforeInteractive"`, `data-n-g`, `data-n-css`), and stylesheet rule `nner-module-scss-module__3-RGkq__... { width:auto;right:1.6rem }`.
2. **Hero Stage & Focal Lead (<section.no-loader> — `UNMATCHED ABUNDANCE`)**:
   - Landmark `<section class="no-loader">` presenting display lead `UNMATCHED ABUNDANCE` and copy excerpt *"A rare opportunity to experience and protect an iconic African wi"* over `#f5eee9` canvas and `#373f1d` ink.
3. **Primary Showcase & Content Grid (<section.site-header> — `U N M A T C H E D A B U N D A N C `)**:
   - Landmark `<section class="site-header">` rendering section `U N M A T C H E D A B U N D A N C E` with copy *"U N M A T C H E D A B U N D A N C E"*, asset references (`icon-32.png`, `icon-16.png`, `inter-regular.woff2`, `inter-medium.woff2`), and grid rule `er-module-scss-module__3-RGkq__co... { text-decoration:underline;transition:color .3s }`.
4. **Interactive Detail & Feature Matrix (<section.no-lenis> — `A Thriving Wilderness`)**:
   - Landmark `<section class="no-lenis">` framing `A Thriving Wilderness` and `Accommodation` (*"Explore Collection"*) with `#fbf8f6` surface cards, `#5c6e21` accents, and `module__3-RGkq__cookie a:focus-vi... { color:5c6e21 }`.
5. **Colophon & Global Directory Footer (<footer.action-card-click-label> — `https://tengilemalamala.com/`)**:
   - Landmark `<footer class="action-card-click-label">` anchoring `Luxury Safari Experiences in Gre` footer links (`About · Accommodation · Experiences · Conservation · Partner Hub`), copy *"Along one of the most wildlife-rich stretches of the Sand Ri"*, and `#e3e1d4` structural dividers.
