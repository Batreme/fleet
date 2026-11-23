---
title: "UI & UX Architecture: www-chriswilliamsart-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-chriswilliamsart-com

## Overview & Design Identity
- **Target**: `www-chriswilliamsart-com` (**Chris Williams Art Gallery · Contemporary painting in London**)
- **Production URL**: [https://www.chriswilliamsart.com/](https://www.chriswilliamsart.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f5f5` / `#b08a5c`)
- **Summary**: Chris Williams Art Gallery shows contemporary painting in Bethnal Green, East London. Explore the work of seven artists online or visit W...
- **Total Clean CSS Variables Extracted**: `7` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Google Sans Flex`
- **Body Font Stack**: `Google Sans Flex`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 66.24px`, `line-height: 67.5648px`, `font-weight: 500`, `letter-spacing: -2.6496px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 37.44px`, `line-height: 39.312px`, `font-weight: 700`, `letter-spacing: -1.1232px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 1.6`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -0.13px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f5f5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#282828` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#b08a5c` | `.room__art--oak { background: #b08a5c }` |
| **Interactive Accent / Highlight** | `#b08a5c` | `.room__art--oak { background: #b08a5c }` |
| **Secondary / Muted Copy** | `#aaaaaa` | `var(--color-muted)` in `:root` |
| **Structural Hairline Border** | `#dbdcdc` | `.list-panel__row { border-bottom: #dbdcdc }` |
| **Variable Token (`--color-placeholder`)** | `#d9d9d9` | `var(--color-placeholder)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#f4f5f5` | Canvas / Surface Token |
| `--color-fg` | `#282828` | Typography Ink Token |
| `--color-muted` | `#aaa` | Brand / Palette Token |
| `--color-placeholder` | `#d9d9d9` | Brand / Palette Token |
| `--font-base` | `"Google Sans Flex", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--aspect` | `.75` | Design System Custom Token |
| `--long` | `calc(var(--u) * 364)` | Design System Custom Token |
| `--www-chriswilliam-bg` | `#f4f5f5` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-chriswilliam-ink` | `#282828` | Primary Typography Ink (computed-derived) |
| `--www-chriswilliam-surface` | `#b08a5c` | Surface Substrate (computed-derived) |
| `--www-chriswilliam-accent` | `#b08a5c` | Interactive Accent (computed-derived) |
| `--www-chriswilliam-muted` | `#aaaaaa` | Secondary Ink (computed-derived) |
| `--www-chriswilliam-border` | `#dbdcdc` | Structural Border (computed-derived) |
| `--www-chriswilliam-container` | `1440px` | Container Bound (computed-derived) |
| `--www-chriswilliam-gap` | `16px` | Grid Gutter (computed-derived) |
| `--www-chriswilliam-pad` | `20px` | Lateral Padding (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-chriswilliamsart-com`)**:
   - Landmark `<header class="site-header">` (`1440x76px`) hosting `Chris Williams Art Gallery · Contemp` navigation (`about a b o u t`), DOM attributes (`data-nav-field`, `data-reveal-text="gallery area"`, `data-reveal-split="1"`, `data-char="g"`), and stylesheet rule `body { overscroll-behavior:none;height:100%;overflow-x:hidden }`.
2. **Hero Stage & Focal Lead (<section.about-intro> — `Chris Williams Art Gallery shows c`)**:
   - Landmark `<section class="about-intro">` presenting display lead `Chris Williams Art Gallery shows contemporary pai...` and copy excerpt *"Jack Wolfstein Jack Wolfstein"* over `#f4f5f5` canvas and `#282828` ink.
3. **Primary Showcase & Content Grid (<section.about-outro> — `Jack Wolfstein`)**:
   - Landmark `<section class="about-outro">` rendering section `Jack Wolfstein` with copy *"Jack Wolfstein J a c k W o l f s t e i n"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `wolfstein-01-CIJigwF-.webp`), and grid rule `button { font:inherit;color:inherit;cursor:pointer;background:0 0;border:none }`.
4. **Interactive Detail & Feature Matrix (<section.about-outro:nth(2)> — `The ground floor`)**:
   - Landmark `<section class="about-outro">` framing `The ground floor` and `Mira Lindqvist` (*"British, b. 1968 Seascape"*) with `#b08a5c` surface cards, `#b08a5c` accents, and `.site-nav { letter-spacing:-.01em;align-items:center;gap:16px;font-size:13px;font-we... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.chriswilliamsart.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Chris Williams Art Gallery · Con` footer links (`about a b o u t`), copy *"Jack Wolfstein paints the North Sea coast, usually in bad we"*, and `#dbdcdc` structural dividers.
