---
title: "UI & UX Architecture: pixlpin-com_designs"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: pixlpin-com_designs

## Overview & Design Identity
- **Target**: `pixlpin-com_designs` (**Pixlpin: 64K+ Free UI Designs, App Screens, Motion & Graphics**)
- **Production URL**: [https://pixlpin.com/designs](https://pixlpin.com/designs)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#171717` ink, `#ff0844` accent)
- **Summary**: Join free. Browse 64K+ real app screens, user flows, websites, motion, logos & 3D, curated from the internet and updated daily.
- **Total Clean CSS Variables Extracted**: `406` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `GeistSans`
- **Body Font Stack**: `GeistSans`
- **Monospace / Technical Font Stack**: `monoFont`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`); CSS variables `--text-size-display: 48px`, `--text-line-display: 56px`, `--text-track-display: -.06em`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18px`, `line-height: 16px`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`); CSS variables `--font-mono: var(--font-geist-mono), ui-monospace, monospace`, `--read-small-size: 15px`, `--read-small-line: 24px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171717` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f2f2` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0844` | `var(--gradient-member-1)` in `:root` |
| **Secondary / Muted Copy** | `#666666` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f2f2f2` | `var(--color-card-border)` in `:root` |
| **Variable Token (`--ds-background-200`)** | `#fafafa` | `var(--ds-background-200)` in `:root` |
| **Variable Token (`--ds-gray-200`)** | `#ebebeb` | `var(--ds-gray-200)` in `:root` |
| **Variable Token (`--ds-gray-300`)** | `#e6e6e6` | `var(--ds-gray-300)` in `:root` |
| **Variable Token (`--ds-gray-500`)** | `#c9c9c9` | `var(--ds-gray-500)` in `:root` |
| **Variable Token (`--ds-gray-600`)** | `#a8a8a8` | `var(--ds-gray-600)` in `:root` |
| **Variable Token (`--ds-gray-700`)** | `#8f8f8f` | `var(--ds-gray-700)` in `:root` |
| **Variable Token (`--ds-gray-alpha-400`)** | `#000000` | `var(--ds-gray-alpha-400)` in `:root` |
| **Variable Token (`--ds-blue-700`)** | `#006bff` | `var(--ds-blue-700)` in `:root` |
| **Variable Token (`--ds-blue-800`)** | `#005ae0` | `var(--ds-blue-800)` in `:root` |
| **Variable Token (`--ds-blue-900`)** | `#005ff2` | `var(--ds-blue-900)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lightningcss-light` | `initial` | Canvas / Surface Token |
| `--ds-background-100` | `#fff` | Canvas / Surface Token |
| `--ds-background-200` | `#fafafa` | Canvas / Surface Token |
| `--ds-gray-100` | `#f2f2f2` | Color / Atmospheric Token |
| `--ds-gray-200` | `#ebebeb` | Color / Atmospheric Token |
| `--ds-gray-300` | `#e6e6e6` | Color / Atmospheric Token |
| `--ds-gray-400` | `#ebebeb` | Color / Atmospheric Token |
| `--ds-gray-500` | `#c9c9c9` | Color / Atmospheric Token |
| `--ds-gray-600` | `#a8a8a8` | Color / Atmospheric Token |
| `--ds-gray-700` | `#8f8f8f` | Color / Atmospheric Token |
| `--ds-gray-900` | `#666` | Color / Atmospheric Token |
| `--ds-gray-1000` | `#171717` | Color / Atmospheric Token |
| `--ds-gray-alpha-400` | `#00000014` | Color / Atmospheric Token |
| `--ds-blue-700` | `#006bff` | Color / Atmospheric Token |
| `--ds-blue-800` | `#005ae0` | Color / Atmospheric Token |
| `--ds-blue-900` | `#005ff2` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-bar> — `pixlpin-com_designs`)**:
   - Landmark `<header class="top-bar">` (`264x900px`) hosting `Pixlpin: 64K+ Free UI Designs, App S` navigation (`All · Apps · AI · Productivity · Business and SaaS`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.rAj-_a_className { font-family:GeistSans,GeistSans Fallback }`.
2. **Hero Stage & Focal Lead (<article.tile> — `Featured Designs`)**:
   - Landmark `<article class="tile tile--video">` presenting display lead `Featured Designs` and copy excerpt *"Explore 64,000+ designs Join 1,000+ Members, Explore 64,000+ desi"* over `#ffffff` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<article.tile--video> — `Explore 64,000+ designs Join 1,000`)**:
   - Landmark `<article class="tile tile--video">` rendering section `Explore 64,000+ designs Join 1,000+ Members, Exp` with copy *"Gemini AI GIF Generation Feature Announcement by Google Gemini Sh"*, asset references (`lovable.webp`, `44hnhs08my_73.css`, `349k6yv56b9jt.css`, `3l0ai14c31l8b.css`), and grid rule `.rAj-_a_variable { --font-geist-sans:"GeistSans", "GeistSans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<article.tile:nth(2)> — `Gemini AI GIF Generation Feature A`)**:
   - Landmark `<article class="tile tile--video">` framing `Gemini AI GIF Generation Feature Announcement by` and `Gemini AI GIF Generation Feature Announcement by` (*"Gemini AI GIF Generation Feature Announcement by Google Gemini"*) with `#f2f2f2` surface cards, `#ff0844` accents, and `after { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.shell-footer> — `https://pixlpin.com/designs`)**:
   - Landmark `<footer class="shell-footer">` anchoring `Pixlpin: 64K+ Free UI Designs, A` footer links (`All · Apps · AI · Productivity · Business and SaaS`), copy *"Claude Mobile App Redesign Walkthrough by Daniel Destefanis "*, and `#f2f2f2` structural dividers.
