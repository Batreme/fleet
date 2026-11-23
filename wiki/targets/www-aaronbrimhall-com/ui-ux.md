---
title: "UI & UX Architecture: www-aaronbrimhall-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-aaronbrimhall-com

## Overview & Design Identity
- **Target**: `www-aaronbrimhall-com` (**Aaron Brimhall · Action & Automotive Photographer**)
- **Production URL**: [https://www.aaronbrimhall.com/](https://www.aaronbrimhall.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#fe019a`)
- **Summary**: Action and automotive photography by Aaron Brimhall: dynamic compositions, high-octane shoots and globe-trotting adventures. Fun fuels cr...
- **Total Clean CSS Variables Extracted**: `26` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Variablefont Opsz Wght`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: observed font-size ladder: `100px`, `38px`, `14px`, `11px`, `2em`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 100px`, `line-height: 95px`, `font-weight: 200`, `letter-spacing: 1px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `.paragraph` (`letter-spacing: .01em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#101010` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#fe019a` | `.ab-ab-cta-arrow { color: #fe019a }` |
| **Secondary / Muted Copy** | `#333333` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#101010` | Canvas / Surface Token |
| `--pink` | `#fe019a` | Typography Ink Token |
| `--font-family` | `"IBM Plex Mono",sans-serif` | Typography / Scale Token |
| `--ab-pink` | `#fe019a` | Typography Ink Token |
| `--ab-black` | `#101010` | Canvas / Surface Token |
| `--ab-ease-osmo` | `cubic-bezier(0.625, 0.05, 0, 1)` | Motion / Easing Token |
| `--ab-ease-out` | `cubic-bezier(0.19, 1, 0.22, 1)` | Motion / Easing Token |
| `--ab-edge` | `24px` | Dimension / Scale Token |
| `--ab-nav-ride` | `0.45s cubic-bezier(0.19, 1, 0.22, 1)` | Layout / Spatial Grid Token |
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--ab-ldx-aw` | `max(96px,min(clamp(140px,44vw,210px),35.16dvh))` | Dimension / Scale Token |
| `--tr-cover` | `#101010` | Color / Atmospheric Token |
| `--hs-e` | `var(--ab-edge,24px)` | Dimension / Scale Token |
| `--hs-trim` | `4px` | Dimension / Scale Token |
| `--vf-i` | `clamp(24px,4vw,64px)` | Dimension / Scale Token |
| `--vf-t` | `max(var(--vf-i),60px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.ab-cs-socials> — `www-aaronbrimhall-com`)**:
   - Landmark `<nav class="ab-cs-socials">` (`317x177px`) hosting `Aaron Brimhall · Action & Automotive` navigation (`INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`), DOM attributes (`data-wf-domain="www.aaronbrimhall.com"`, `data-wf-page="6941d6f273b44a2836ceae0d"`, `data-wf-site="6941d6f273b44a2836ceae16"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero_section> — `Aaron Brimhall · Action & Automoti`)**:
   - Landmark `<section class="hero_section ab-hx-short">` presenting display lead `Aaron Brimhall · Action & Automotive Photographe` and copy excerpt *"TRANSMISSION RECEIVED"* over `#101010` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.hero-section_wrapper> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="hero-section_wrapper">` rendering section `Featured Work & Interactive Showcase` with copy *"SIGNAL LOST — TRY AGAIN"*, asset references (`cdn.prod.website-files.com`, `aaron-brimhall-site-09-25-f01e7c4...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.gallery_section> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="gallery_section">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"I M A G E G E N E R A T O R →"*) with `#222222` surface cards, `#fe019a` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-ibmplexmono-n6-active> — `https://www.aaronbrimhall.com/`)**:
   - Landmark `<footer class="wf-ibmplexmono-n6-active">` anchoring `Aaron Brimhall · Action & Automo` footer links (`INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`), copy *"I M A G E G E N E R A T O R"*, and `#3898ec` structural dividers.
