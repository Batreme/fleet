---
title: "UI & UX Architecture: mont-rural-emblematica-agency"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: mont-rural-emblematica-agency

## Overview & Design Identity
- **Target**: `mont-rural-emblematica-agency` (**MontRural — Private Masia Among the Vineyards of Penedès**)
- **Production URL**: [https://mont-rural.emblematica.agency](https://mont-rural.emblematica.agency)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#37482f` canvas, `#f8e8c5` ink, `#cfa65a` accent)
- **Summary**: Rent a masia for a peaceful and cozy getaway just an hour's drive from Barcelona. Perfect for nature retreats, family gatherings, and int...
- **Total Clean CSS Variables Extracted**: `140` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Playfair`
- **Body Font Stack**: `Arial)`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `13.3333px`, `100%`, `26px`, `14px`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `13.3333px`, `100%`, `26px`, `14px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#37482f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f8e8c5` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#293b21` | `.t_datepicker__day-cell:hover { background: #293b21 }` |
| **Interactive Accent / Highlight** | `#cfa65a` | `.tn-atom .tn-atom__button-text { color: #cfa65a }` |
| **Secondary / Muted Copy** | `#000000` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#5f6d59` | `.t_datepicker__header { border-bottom: #5f6d59 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--button-shadow` | `none` | Elevation / Border Token |
| `--button-content-gap` | `0` | Layout / Spatial Grid Token |
| `--size` | `20px` | Layout / Spatial Grid Token |
| `--border-width` | `2px` | Layout / Spatial Grid Token |
| `--border-radius` | `0` | Elevation / Border Token |
| `--check` | `calc(var(--size) - var(--border-width)*2)` | Design System Custom Token |
| `--line-height` | `1` | Typography / Scale Token |
| `--dot` | `calc(var(--size)/2)` | Design System Custom Token |
| `--offset-y` | `calc((1em*var(--line-height) - var(--size))/2)` | Dimension / Scale Token |
| `--t-headline-font` | `'Playfair',Arial,sans-serif` | Typography / Scale Token |
| `--t-text-font` | `'Arial',Arial,sans-serif` | Typography Ink Token |
| `--uc-typo-fontsize-Bi2HZBV1z` | `82px` | Typography / Scale Token |
| `--uc-typo-fontweight-Bi2HZBV1z` | `400` | Typography / Scale Token |
| `--uc-typo-letterspacing-Bi2HZBV1z` | `-6.5px` | Layout / Spatial Grid Token |
| `--uc-typo-fontfamily-Bi2HZBV1z` | `var(--t-headline-font,Arial)` | Typography / Scale Token |
| `--uc-typo-lineheight-Bi2HZBV1z` | `.9` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.t450__menu> — `mont-rural-emblematica-agency`)**:
   - Landmark `<nav class="t450__menu">` (`180x151px`) hosting `MontRural — Private Masia Among the ` navigation (`About · location · What's Inside · SERVICES · Contacts`), DOM attributes (`data-hook="blocks-collection-con..."`, `data-tilda-project-id="25144176"`, `data-tilda-page-id="139030856"`, `data-tilda-page-alias="en"`), and stylesheet rule `.t_datepicker__selected-day::after { display: none !important; content: none !important; }`.
2. **Hero Stage & Focal Lead (<div.t-records> — `MontRural — Private Masia Among th`)**:
   - Landmark `<div class="t-records t-records_animated">` presenting display lead `MontRural — Private Masia Among the Vineyards of` and copy excerpt *"CHECK AVAILABILITY"* over `#37482f` canvas and `#f8e8c5` ink.
3. **Primary Showcase & Content Grid (<div.t-records_animated> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="t-records t-records_animated">` rendering section `Featured Work & Interactive Showcase` with copy *"R e n t a m a s i a f o r a p e a c e f u l a n d c o z y g e t a"*, asset references (`mont-rural.emblematica.agency`, `ws.tildacdn.com`, `static.tildacdn.com`, `Frame_1948756319.png`), and grid rule `.t_datepicker__header { background: transparent; border-bottom: 1px solid rgba(255,255,255,0.2); }`.
4. **Interactive Detail & Feature Matrix (<div.t-records_visible> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="t-records t-records_animated">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"a n h o u r ' s d r i v e f r o m B a r c e l o n a . P e r f e c"*) with `#293b21` surface cards, `#cfa65a` accents, and `.t_datepicker__label span { color: 8F8637; font-weight: 500; }`.
5. **Colophon & Global Directory Footer (<footer.t-records_visible> — `https://mont-rural.emblematica.agency`)**:
   - Landmark `<footer class="t-records_visible">` anchoring `MontRural — Private Masia Among ` footer links (`About · location · What's Inside · SERVICES · Contacts`), copy *"B a r c e l o n a ."*, and `#5f6d59` structural dividers.
