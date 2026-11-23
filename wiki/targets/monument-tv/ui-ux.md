---
title: "UI & UX Architecture: monument-tv"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: monument-tv

## Overview & Design Identity
- **Target**: `monument-tv` (**Homepage - Monument**)
- **Production URL**: [https://monument.tv/](https://monument.tv/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#760000` / `#3b758b`)
- **Summary**: Monument is an independent creative production company specializing in unscripted television, documentary, and reality tv. We deliver inn...
- **Total Clean CSS Variables Extracted**: `83` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `obviously-narrow`
- **Body Font Stack**: `neue-haas-grotesk-text`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 180px`, `line-height: 153px`, `font-weight: 470`, `letter-spacing: -3.6px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 39px`, `line-height: 39px`, `font-weight: 500`, `letter-spacing: -0.78px`); rule `h2` (`font-size: 2rem`, `line-height: 1`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 0.75rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 27px`, `line-height: 22.95px`, `font-weight: 470`, `letter-spacing: -0.54px`); CSS variables `--letter-spacing: 0`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#760000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#eee3d1` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#3b758b` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#3b758b` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#f85e34` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#6d0303` | `.cookieconsent ul li { border: #6d0303 }` |
| **Variable Token (`--black`)** | `#020202` | `var(--black)` in `:root` |
| **Variable Token (`--thunderbird`)** | `#ce1f1a` | `var(--thunderbird)` in `:root` |
| **Variable Token (`--tan-hide`)** | `#f8a351` | `var(--tan-hide)` in `:root` |
| **Variable Token (`--piper`)** | `#bd6623` | `var(--piper)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--japanese-maple` | `#760000` | Color / Atmospheric Token |
| `--aths-special` | `#eee3d1` | Color / Atmospheric Token |
| `--flamingo` | `#f85e34` | Color / Atmospheric Token |
| `--font-size` | `2.25rem` | Typography / Scale Token |
| `--black` | `#020202` | Canvas / Surface Token |
| `--thunderbird` | `#ce1f1a` | Color / Atmospheric Token |
| `--ming` | `#3b758b` | Color / Atmospheric Token |
| `--tan-hide` | `#f8a351` | Color / Atmospheric Token |
| `--piper` | `#bd6623` | Color / Atmospheric Token |
| `--underline-width` | `0%` | Layout / Spatial Grid Token |
| `--hover-duration` | `0.3s` | Motion / Easing Token |
| `--box-padding` | `3rem` | Layout / Spatial Grid Token |
| `--global-padding` | `0.75rem` | Layout / Spatial Grid Token |
| `--pin-spacing` | `2.25` | Layout / Spatial Grid Token |
| `--pin` | `0` | Design System Custom Token |
| `--line-height` | `1` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.no-scrollbar> — `monument-tv`)**:
   - Landmark `<header class="no-scrollbar">` (`289x78px`) hosting `Homepage - Monument` navigation (`Work · About · Team · Casting · Press`), DOM attributes (`data-parent`, `data-template="homepage"`, `data-component="navbar"`, `data-component="vector-grid"`), and stylesheet rule `before { box-sizing:inherit;-webkit-tap-highlight-color:rgba(0,0,0,0) }`.
2. **Hero Stage & Focal Lead (<section.hero> — `READY FOR MONUMENTAL TV?`)**:
   - Landmark `<section class="hero sticky-root">` presenting display lead `READY FOR MONUMENTAL TV?` and copy excerpt *"We and our partners use cookies and other technologies to improve"* over `#760000` canvas and `#eee3d1` ink.
3. **Primary Showcase & Content Grid (<article.hero__content__texts> — `Ready for monumental tv?`)**:
   - Landmark `<article class="hero__content__texts">` rendering section `Ready for monumental tv?` with copy *"From first spark to final cut, we craft unforgettable television."*, asset references (`essential.css`, `breeze-prefetch-links.min.js`, `common.js`, `vendors-common.js`), and grid rule `video { height:auto;max-width:100% }`.
4. **Interactive Detail & Feature Matrix (<section.clients> — `Monument is where great stories me`)**:
   - Landmark `<section class="clients sticky-root">` framing `Monument is where great stories meet great storyt...` and `Major stories well-told.` (*"Major stories well-told."*) with `#3b758b` surface cards, `#3b758b` accents, and `.main-preloader { font-size:1.375rem;font-size:var(--font-size,1.375rem);padding:var(--box... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://monument.tv/`)**:
   - Landmark `<footer class="footer sticky-root">` anchoring `Homepage - Monument` footer links (`Work · About · Team · Casting · Press`), copy *"We chase the stories that matter and craft them with precisi"*, and `#6d0303` structural dividers.
