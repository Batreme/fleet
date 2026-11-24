---
title: "UI & UX Architecture: sotz-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: sotz-org

## Overview & Design Identity
- **Target**: `sotz-org` (**Shout out to Zanzibar**)
- **Production URL**: [https://sotz.org/](https://sotz.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×3312px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#e9e2d3` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: S h o u t o u t t o Z a n z i b a r :
- **Total Clean CSS Variables Extracted**: `15` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 54px`, `line-height: 56.7px`, `font-weight: 700`, `letter-spacing: 2.16px`); rule `h1` (`font-size: clamp(22px, 4.2vw, 54px)`, `line-height: 1.05`, `letter-spacing: .04em`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 33px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: 1.98px`); rule `h2` (`font-size: clamp(18px, 2.6vw, 33px)`, `letter-spacing: .06em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: clamp(11px, 1.35vw, 17px)`, `letter-spacing: .02em`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e9e2d3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3eddd` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#4a4233` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#b9ae95` | `.site-footer { border-top: #b9ae95 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dd` | `0s` | Motion / Timing Token |
| `--breath-time` | `5.2s` | Motion / Timing Token |
| `--breath-delay` | `-.9s` | Motion / Easing Token |
| `--breath-x` | `1.5px` | Dimension / Scale Token |
| `--breath-y` | `-2.5px` | Dimension / Scale Token |
| `--sd` | `4.2s` | Motion / Timing Token |
| `--sdd` | `0s` | Motion / Timing Token |
| `--fx` | `12.686829972268164px` | Dimension / Scale Token |
| `--fy` | `-42.338201167836075px` | Dimension / Scale Token |
| `--fd` | `8.03990141361104s` | Motion / Timing Token |
| `--fdd` | `-4.525146343807082s` | Motion / Timing Token |
| `--gd` | `3.218259545023418s` | Motion / Timing Token |
| `--gdd` | `-1.1055247801866024s` | Motion / Timing Token |
| `--dx` | `97.66093029928604px` | Dimension / Scale Token |
| `--dy` | `-56.65180577215252px` | Dimension / Scale Token |
| `--sotz-org-bg` | `#e9e2d3` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.headline> — `sotz-org`)**:
   - Landmark `<header class="headline">` (`769x237px`) hosting `Shout out to Zanzibar` navigation (`Home · About Us · Pictures · Writings · Projects`), DOM attributes (`data-story="mission"`, `data-story="tanzania"`, `data-story="work"`, `data-story="school"`), and stylesheet rule `.site-footer .flinks { display: flex; flex-wrap: wrap; justify-content: center; gap: clamp(14px... }`.
2. **Hero Stage & Focal Lead (<article.story-panel> — `SHOUT OUT TO ZANZIBAR:`)**:
   - Landmark `<article class="story-panel">` presenting display lead `SHOUT OUT TO ZANZIBAR:` and copy excerpt *"Where every small hand holds a big dream — beneath Kilimanjaro’s "* over `#e9e2d3` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.story-panel:nth(2)> — `S h o u t o u t t o Z a n z i b a `)**:
   - Landmark `<article class="story-panel">` rendering section `S h o u t o u t t o Z a n z i b a r :` with copy *"Shout out to Zanzibar"*, asset references (`sotz_logo.png`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `.site-footer .flinks a:focus-visible { border-color: 8a6b47; color: 4a4233; }`.
4. **Interactive Detail & Feature Matrix (<article.story-panel:nth(3)> — `No Pity but for the Future of Chil`)**:
   - Landmark `<article class="story-panel">` framing `No Pity but for the Future of Children` and `SOTZ, Shout out to Zanzibar is the non-profit or` (*"SOTZ, Shout out to Zanzibar is the non-profit organization dedica"*) with `#f3eddd` surface cards, `#0000ee` accents, and `.stage-art { position: absolute; inset: 0; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://sotz.org/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Shout out to Zanzibar` footer links (`Home · About Us · Pictures · Writings · Projects`), copy *"We believe that charity should not originate from a sense of"*, and `#b9ae95` structural dividers.
