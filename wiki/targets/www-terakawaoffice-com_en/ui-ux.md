---
title: "UI & UX Architecture: www-terakawaoffice-com_en"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-terakawaoffice-com_en

## Overview & Design Identity
- **Target**: `www-terakawaoffice-com_en` (**Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office**)
- **Production URL**: [https://www.terakawaoffice.com/en/](https://www.terakawaoffice.com/en/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fbfaf7` / `#7e6538`)
- **Summary**: Tokyo architectural photographer Naoki Terakawa. Completion photography, drone aerials, models, time-lapse — for architects and developer...
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EB Garamond`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 51.84px`, `line-height: 60.1344px`, `font-weight: 400`, `letter-spacing: 0.2592px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 33.12px`, `line-height: 42.3936px`, `font-weight: 400`, `letter-spacing: -0.13248px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 300`); rule `p` (`font-size: 17px`, `line-height: 1.65`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 300`); CSS variables `--bh-caption-gap: 36px`, `--tx-label: 'Inter',-apple-system,'Helvetica Neue',sans-serif`; rule `small` (`font-size: 0.32em`, `letter-spacing: 0.15em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fbfaf7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#141414` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f2ea` | `var(--paper-warm)` in `:root` |
| **Interactive Accent / Highlight** | `#7e6538` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#8f8f8f` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e4e2dc` | `var(--line)` in `:root` |
| **Variable Token (`--ink-2`)** | `#3a3a3a` | `var(--ink-2)` in `:root` |
| **Variable Token (`--ink-soft`)** | `#6b6b6b` | `var(--ink-soft)` in `:root` |
| **Variable Token (`--ink-mute`)** | `#6d6d6d` | `var(--ink-mute)` in `:root` |
| **Variable Token (`--line-soft`)** | `#efede7` | `var(--line-soft)` in `:root` |
| **Variable Token (`--accent-dark`)** | `#6d5a33` | `var(--accent-dark)` in `:root` |
| **Variable Token (`--accent-soft`)** | `#c4b18a` | `var(--accent-soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#141414` | Typography Ink Token |
| `--ink-2` | `#3a3a3a` | Typography Ink Token |
| `--ink-soft` | `#6b6b6b` | Typography Ink Token |
| `--ink-mute` | `#6d6d6d` | Typography Ink Token |
| `--line` | `#e4e2dc` | Color / Atmospheric Token |
| `--line-soft` | `#efede7` | Color / Atmospheric Token |
| `--paper` | `#fbfaf7` | Canvas / Surface Token |
| `--paper-warm` | `#f5f2ea` | Canvas / Surface Token |
| `--accent` | `#7e6538` | Brand / Palette Token |
| `--accent-dark` | `#6d5a33` | Canvas / Surface Token |
| `--accent-soft` | `#c4b18a` | Brand / Palette Token |
| `--serif-jp` | `'Noto Serif JP',serif` | Typography / Scale Token |
| `--serif-en` | `'EB Garamond',serif` | Typography / Scale Token |
| `--sans` | `'Inter','Noto Serif JP',sans-serif` | Typography / Scale Token |
| `--tpo-ease` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--fin` | `20px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.tpo-js> — `www-terakawaoffice-com_en`)**:
   - Landmark `<header class="tpo-js">` (`1440x87px`) hosting `Architectural Photographer in Tokyo,` navigation (`Works · Services · Pricing · About · Contact`), DOM attributes (`data-tpo-field-worker`, `data-blue-hour`, `data-bh-mode="holding"`, `data-work-title="Nogeyama Zoological P..."`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Architecture, as it truly is.`)**:
   - Landmark `<section class="hero">` presenting display lead `Architecture, as it truly is.` and copy excerpt *"Photography for Architecture — Tokyo, Japan."* over `#fbfaf7` canvas and `#141414` ink.
3. **Primary Showcase & Content Grid (<section.trust-bar> — `Space and intent, in a single fram`)**:
   - Landmark `<section class="trust-bar">` rendering section `Space and intent, in a single frame.` with copy *"Light, recomposed."*, asset references (`favicon.ico`, `favicon-96.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `img { display:block;max-width:100% }`.
4. **Interactive Detail & Feature Matrix (<section.works-index> — `Three reasons to work with TERAKAW`)**:
   - Landmark `<section class="works-index">` framing `Three reasons to work with TERAKAWA.` and `Fine detail, faithfully recorded.` (*"Click or tap to enlarge. Hold to move the light; release to revea"*) with `#f5f2ea` surface cards, `#7e6538` accents, and `.topbar-center { justify-self:center;display:flex;align-items:center;gap:16px }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.terakawaoffice.com/en/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Architectural Photographer in To` footer links (`Works · Services · Pricing · About · Contact`), copy *"Move the pointer or your finger to guide the light. Release "*, and `#e4e2dc` structural dividers.
