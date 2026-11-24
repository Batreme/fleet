---
title: "UI & UX Architecture: www-imersion-io"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-imersion-io

## Overview & Design Identity
- **Target**: `www-imersion-io` (**Imersion — Get Immersed in the World's Most Beautiful Places**)
- **Production URL**: [https://www.imersion.io](https://www.imersion.io)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111111` canvas, `#ffffff` ink, `#007bff` accent)
- **Summary**: Get immersed in the most beautiful places on Earth — breathtaking landscapes, hidden hotels and surreal restaurants, each with its own st...
- **Total Clean CSS Variables Extracted**: `28` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Mono`
- **Body Font Stack**: `Source Code Pro`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 100.8px`, `line-height: 92.736px`, `font-weight: 500`, `letter-spacing: -3.528px`); rule `,h1` (`font-size: 2.5rem`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 76.8px`, `line-height: 78.336px`, `font-weight: 500`, `letter-spacing: -2.304px`); rule `,h2` (`font-size: 2rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `,small` (`font-size: 80%`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a0d` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#007bff` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#999999` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#0f0f0f` | `hr { border-top: #0f0f0f }` |
| **Variable Token (`--indigo`)** | `#6610f2` | `var(--indigo)` in `:root` |
| **Variable Token (`--purple`)** | `#6f42c1` | `var(--purple)` in `:root` |
| **Variable Token (`--pink`)** | `#e83e8c` | `var(--pink)` in `:root` |
| **Variable Token (`--red`)** | `#dc3545` | `var(--red)` in `:root` |
| **Variable Token (`--orange`)** | `#fd7e14` | `var(--orange)` in `:root` |
| **Variable Token (`--yellow`)** | `#ffc107` | `var(--yellow)` in `:root` |
| **Variable Token (`--green`)** | `#28a745` | `var(--green)` in `:root` |
| **Variable Token (`--teal`)** | `#20c997` | `var(--teal)` in `:root` |
| **Variable Token (`--cyan`)** | `#17a2b8` | `var(--cyan)` in `:root` |
| **Variable Token (`--gray`)** | `#6c757d` | `var(--gray)` in `:root` |
| **Variable Token (`--gray-dark`)** | `#343a40` | `var(--gray-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--blue` | `#007bff` | Color / Atmospheric Token |
| `--indigo` | `#6610f2` | Color / Atmospheric Token |
| `--purple` | `#6f42c1` | Color / Atmospheric Token |
| `--pink` | `#e83e8c` | Typography Ink Token |
| `--red` | `#dc3545` | Color / Atmospheric Token |
| `--orange` | `#fd7e14` | Color / Atmospheric Token |
| `--yellow` | `#ffc107` | Color / Atmospheric Token |
| `--green` | `#28a745` | Color / Atmospheric Token |
| `--teal` | `#20c997` | Color / Atmospheric Token |
| `--cyan` | `#17a2b8` | Color / Atmospheric Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--gray` | `#6c757d` | Color / Atmospheric Token |
| `--gray-dark` | `#343a40` | Canvas / Surface Token |
| `--primary` | `#007bff` | Brand / Palette Token |
| `--secondary` | `#6c757d` | Brand / Palette Token |
| `--success` | `#28a745` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hh> — `www-imersion-io`)**:
   - Landmark `<header class="hh">` (`1440x80px`) hosting `Imersion — Get Immersed in the World` navigation (`Contact Contact`), DOM attributes (`data-n-head="%7B%22lang%22:%7B%22s..."`, `data-n-head="ssr"`, `data-n-head="ssr"`, `data-n-head="ssr"`), and stylesheet rule `before { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.wow> — `GETIMMERSED`)**:
   - Landmark `<section class="wow">` presenting display lead `GETIMMERSED` and copy excerpt *"…in breathtaking landscapes, hidden hotels and surreal restaurant"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.recent> — `…in breathtaking landscapes, hidde`)**:
   - Landmark `<section class="recent">` rendering section `…in breathtaking landscapes, hidden hotels and s` with copy *"Need a crew of AI agents?"*, asset references (`favicon.ico`, `hero-poster.jpg`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `html { font-family:sans-serif;line-height:1.15;-webkit-text-size-adjust:100%;-w... }`.
4. **Interactive Detail & Feature Matrix (<section.about> — `Need a crew of AI agents?`)**:
   - Landmark `<section class="about">` framing `Need a crew of AI agents?` and `G E T I M M E R S E D` (*"G E T I M M E R S E D"*) with `#0a0a0d` surface cards, `#007bff` accents, and `section { display:block }`.
5. **Colophon & Global Directory Footer (<footer.hf> — `https://www.imersion.io`)**:
   - Landmark `<footer class="hf">` anchoring `Imersion — Get Immersed in the W` footer links (`Contact Contact`), copy *"Nusa Penida, Klungkung, Indonesia"*, and `#0f0f0f` structural dividers.
