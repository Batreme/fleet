---
title: "UI & UX Architecture: lfs-org-uk"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lfs-org-uk

## Overview & Design Identity
- **Target**: `lfs-org-uk` (**London Film School**)
- **Production URL**: [https://lfs.org.uk/](https://lfs.org.uk/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#0000ff` accent)
- **Summary**: The oldest film school in the UK, dedicated to the education of filmmakers.
- **Total Clean CSS Variables Extracted**: `100` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Waldenburg Condensed Black`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 160px`, `line-height: 144px`, `font-weight: 400`, `letter-spacing: -3.2px`); rule `h1` (`font-size: 2rem`, `line-height: 1`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); rule `h2` (`font-size: 1.375rem`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 22px`, `font-weight: 400`); rule `p` (`line-height: 1.2`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 22px`, `font-weight: 400`); CSS variables `--spacing-xsmall: 1rem`, `--spacing-small: 2rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#23282d` | `.wpcf7-spinner { background-color: #23282d }` |
| **Interactive Accent / Highlight** | `#0000ff` | `.page--short-courses .pill-btn { background-color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Structural Hairline Border** | `#d4dae0` | `var(--cc-btn-secondary-hover-border-color)` in `:root` |
| **Variable Token (`--cc-primary-color`)** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Variable Token (`--cc-btn-primary-bg`)** | `#30363c` | `var(--cc-btn-primary-bg)` in `:root` |
| **Variable Token (`--cc-btn-secondary-bg`)** | `#eaeff2` | `var(--cc-btn-secondary-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-modal-border-radius` | `.5rem` | Elevation / Border Token |
| `--cc-btn-border-radius` | `.4rem` | Elevation / Border Token |
| `--cc-modal-transition-duration` | `.25s` | Motion / Easing Token |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` | Typography Ink Token |
| `--cc-modal-margin` | `1rem` | Layout / Spatial Grid Token |
| `--cc-z-index` | `2147480000` | Elevation / Border Token |
| `--cc-bg` | `#fff` | Canvas / Surface Token |
| `--cc-primary-color` | `#2c2f31` | Brand / Palette Token |
| `--cc-secondary-color` | `#5e6266` | Brand / Palette Token |
| `--cc-btn-primary-bg` | `#30363c` | Canvas / Surface Token |
| `--cc-btn-primary-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` | Brand / Palette Token |
| `--cc-btn-primary-hover-bg` | `#000` | Canvas / Surface Token |
| `--cc-btn-primary-hover-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` | Brand / Palette Token |
| `--cc-btn-secondary-bg` | `#eaeff2` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `lfs-org-uk`)**:
   - Landmark `<header class="header js-header">` (`1440x40px`) hosting `London Film School` navigation (`Full time courses · MA Filmmaking · MA Screenwriting · MA Film Marketing · MA Film Producing`), DOM attributes (`data-category="analytics"`, `data-service="Google Analytics"`, `data-category="analytics"`, `data-service="Google Analytics"`), and stylesheet rule `.wpcf7 .hidden-fields-container { display: none; }`.
2. **Hero Stage & Focal Lead (<section.homepage-hero> — `Find your voice in film`)**:
   - Landmark `<section class="homepage-hero homepage-hero--announcement">` presenting display lead `Find your voice in film` and copy excerpt *"A 17-year-old Ada spends the school vacation helping her father s"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.homepage-courses> — `Training the world’s next great fi`)**:
   - Landmark `<section class="homepage-courses background-grey">` rendering section `Training the world’s next great filmmakers and st...` with copy *"Explore London Film School from anywhere"*, asset references (`recaptcha__en.js`, `favicon-96x96.png`, `favicon.svg`, `favicon.ico`), and grid rule `.wpcf7 form .wpcf7-response-output { margin: 2em 0.5em 1em; padding: 0.2em 1em; border: 2px solid 00a0d2; }`.
4. **Interactive Detail & Feature Matrix (<section.featured-film> — `MA Filmmaking`)**:
   - Landmark `<section class="featured-film js-featured-film">` framing `MA Filmmaking` and `MA Screenwriting` (*"Elísabet Ronaldsdóttir"*) with `#23282d` surface cards, `#0000ff` accents, and `form.submitting .wpcf7-response-o... { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://lfs.org.uk/`)**:
   - Landmark `<footer class="footer grid-container">` anchoring `London Film School` footer links (`Full time courses · MA Filmmaking · MA Screenwriting · MA Film Marketing · MA Film Producing`), copy *"LFS is the UK's oldest dedicated film school. Based in the c"*, and `#d4dae0` structural dividers.
