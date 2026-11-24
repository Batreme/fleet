---
title: "UI & UX Architecture: imdday-ch"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: imdday-ch

## Overview & Design Identity
- **Target**: `imdday-ch` (**IMDDay 2026**)
- **Production URL**: [https://imdday.ch/](https://imdday.ch/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#b2b2b2` / `#bbbcc4`)
- **Summary**: Dirk Koy, born in 1977, is a Basel-based artist active in various fields of moving image creation. He is a digital world-builder who samp...
- **Total Clean CSS Variables Extracted**: `53` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Neue Montreal`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 114.307px`, `line-height: 114.307px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 114.307px`, `line-height: 114.307px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 19.6922px`, `line-height: 23.6306px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 19.6922px`, `line-height: 19.6922px`, `font-weight: 400`); CSS variables `--text-xs: calc(0.4231rem + 0.8974vw)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#b2b2b2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#bbbcc4` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#bbbcc4` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#8e8e8e` | `.Speakers_Item { border-bottom: #8e8e8e }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--main-font` | `"Neue Montreal"` | Typography / Scale Token |
| `--text-xs` | `calc(0.4231rem + 0.8974vw)` | Typography Ink Token |
| `--text-s` | `calc(-0.0962rem + 3.2051vw)` | Typography Ink Token |
| `--text-m` | `calc(1.2019rem + 1.6026vw)` | Typography Ink Token |
| `--text-l` | `calc(1.1731rem + 4.2308vw)` | Typography Ink Token |
| `--text-xl` | `calc(0.4519rem + 7.4359vw)` | Typography Ink Token |
| `--padding` | `calc(-33.8462px + 12.1795vw)` | Layout / Spatial Grid Token |
| `--left-column` | `calc(1.2019rem + 14.1026vw)` | Layout / Spatial Grid Token |
| `--space-xs` | `calc(7.6923px + 0.641vw)` | Layout / Spatial Grid Token |
| `--space-s` | `calc(2.1538px + 2.1795vw)` | Layout / Spatial Grid Token |
| `--space-m` | `calc(29.2308px + 1.6026vw)` | Layout / Spatial Grid Token |
| `--space-l` | `calc(50.7692px + 2.5641vw)` | Layout / Spatial Grid Token |
| `--ease-inout-sine` | `cubic-bezier(0.37, 0, 0.63, 1)` | Motion / Easing Token |
| `--ease-in-cubic` | `cubic-bezier(0.32, 0, 0.67, 0)` | Motion / Easing Token |
| `--ease-out-cubic` | `cubic-bezier(0.33, 1, 0.68, 1)` | Motion / Easing Token |
| `--ease-inout-cubic` | `cubic-bezier(0.65, 0, 0.35, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Navigation_Main> — `imdday-ch`)**:
   - Landmark `<header class="Navigation_Main">` (`116x400px`) hosting `IMDDay 2026` navigation (`T ickets · L ineup · T imetable · G etting there · A bout`), DOM attributes (`data-tp-style="plugin-default"`, `data-engine="three.js r181"`, `data-config="%7B%22speed%22:0.2,%2..."`, `data-id="lineup"`), and stylesheet rule `selection { background: a1a1a1; color: white; }`.
2. **Hero Stage & Focal Lead (<article.Speakers_Item> — `Getting there`)**:
   - Landmark `<article class="Speakers_Item Stage_Node">` presenting display lead `Getting there` and copy excerpt *"Dirk Koy, born in 1977, is a Basel-based artist active in various"* over `#b2b2b2` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.Stage_Node> — `Elodie Anglade`)**:
   - Landmark `<article class="Speakers_Item Stage_Node">` rendering section `Elodie Anglade` with copy *"In his visual logic, traces are not static. They continue to evol"*, asset references (`favicon.image-6ZC672GS.svg`, `favicon-TJBRTTS6.png`, `index.html`, `index.js`), and grid rule `.Html_Visible { opacity: 1; }`.
4. **Interactive Detail & Feature Matrix (<article.Speakers_Item:nth(2)> — `Immo Schneider`)**:
   - Landmark `<article class="Speakers_Item Stage_Node">` framing `Immo Schneider` and `Joëlle Bitton` (*"Elodie Anglade is a media and interaction designer based in Switz"*) with `#ffffff` surface cards, `#bbbcc4` accents, and `canvas { position: absolute; width: 100%; height: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.Footer_Main> — `https://imdday.ch/`)**:
   - Landmark `<footer class="Footer_Main">` anchoring `IMDDay 2026` footer links (`T ickets · L ineup · T imetable · G etting there · A bout`), copy *"Her work often sits at the intersection of image-making, ani"*, and `#8e8e8e` structural dividers.
