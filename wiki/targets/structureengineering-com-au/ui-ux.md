---
title: "UI & UX Architecture: structureengineering-com-au"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: structureengineering-com-au

## Overview & Design Identity
- **Target**: `structureengineering-com-au` (**Structure Consulting Engineers · Structural Engineering Sydney**)
- **Production URL**: [https://structureengineering.com.au/](https://structureengineering.com.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#000000` ink, `#ffffff` accent)
- **Summary**: Specialists in structural engineering in Sydney, we work across a range of industries from residential to commercial, remedial, governmen...
- **Total Clean CSS Variables Extracted**: `5` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SequelSans`
- **Body Font Stack**: `SequelSans`
- **Monospace / Technical Font Stack**: `PPFraktionMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 81.6px`, `line-height: 81.6px`, `font-weight: 400`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 81.6px`, `line-height: 81.6px`, `font-weight: 400`); rule `.h2` (`font-size: 3.7em`, `line-height: 1`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); rule `p` (`font-size: 0.8em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.background-color-white { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#ffffff` | `ackground-color-gold .block-hea... { color: #ffffff }` |
| **Secondary / Muted Copy** | `#777777` | `form-wrap .dropdown-menu>.disab... { color: #777777 }` |
| **Structural Hairline Border** | `#ffffff` | `a.btn-with-arrow:hover { border-color: #ffffff }` |
| **Variable Token (`--color-gold`)** | `#b9b36d` | `var(--color-gold)` in `:root` |
| **Variable Token (`--color-grey`)** | `#bebebe` | `var(--color-grey)` in `:root` |
| **Variable Token (`--wp--preset--color--cyan-bluish-gray`)** | `#abb8c3` | `var(--wp--preset--color--cyan-bluish-gray)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-gold` | `#B9B36D` | Brand / Palette Token |
| `--color-background-grey` | `#F5F5F5` | Canvas / Surface Token |
| `--color-grey` | `#BEBEBE` | Brand / Palette Token |
| `--wp--preset--aspect-ratio--square` | `1` | Design System Custom Token |
| `--wp--preset--aspect-ratio--4-3` | `4/3` | Design System Custom Token |
| `--wp--preset--aspect-ratio--3-4` | `3/4` | Design System Custom Token |
| `--wp--preset--aspect-ratio--3-2` | `3/2` | Design System Custom Token |
| `--wp--preset--aspect-ratio--2-3` | `2/3` | Design System Custom Token |
| `--wp--preset--aspect-ratio--16-9` | `16/9` | Design System Custom Token |
| `--wp--preset--aspect-ratio--9-16` | `9/16` | Design System Custom Token |
| `--wp--preset--color--black` | `#000000` | Canvas / Surface Token |
| `--wp--preset--color--cyan-bluish-gray` | `#abb8c3` | Brand / Palette Token |
| `--structureenginee-bg` | `#f5f5f5` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--structureenginee-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.top-nav> — `structureengineering-com-au`)**:
   - Landmark `<nav class="top-nav font-PPFraktionMono">` (`878x93px`) hosting `Structure Consulting Engineers · Str` navigation (`About · Company · Careers · People · Sectors`), DOM attributes (`data-section-background-color="background-color-black"`, `data-rocket-prefetch`, `data-rocket-preload`, `data-rocket-async="style"`), and stylesheet rule `html { scrollbar-gutter: stable; }`.
2. **Hero Stage & Focal Lead (<section.section> — `A different approach to traditiona`)**:
   - Landmark `<section class="section section-topbannerhome">` presenting display lead `A different approach to traditional structural en...` and copy excerpt *"Residential Northbridge House II"* over `#f5f5f5` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section-intro> — `Northbridge House II`)**:
   - Landmark `<section class="section section-intro">` rendering section `Northbridge House II` with copy *"Residential Castlecrag House"*, asset references (`gtm.js`, `www.googletagmanager.com`, `SequelSans-Medium.woff2`, `PPFraktionMono-Regular.woff2`), and grid rule `figure { border: none; padding: 0; display: inline-block; margin: 1em 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-spread> — `Castlecrag House`)**:
   - Landmark `<section class="section section-spread">` framing `Castlecrag House` and `Marrickville House` (*"Residential Marrickville House"*) with `#ffffff` surface cards, `#ffffff` accents, and `img { pointer-events: none; }`.
5. **Colophon & Global Directory Footer (<footer.preloadergone> — `https://structureengineering.com.au/`)**:
   - Landmark `<footer class="preloadergone">` anchoring `Structure Consulting Engineers ·` footer links (`About · Company · Careers · People · Sectors`), copy *"Through thoughtful design, clear communication and lateral t"*, and `#ffffff` structural dividers.
