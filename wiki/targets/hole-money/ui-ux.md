---
title: "UI & UX Architecture: hole-money"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: hole-money

## Overview & Design Identity
- **Target**: `hole-money` (**Money Hole**)
- **Production URL**: [https://hole.money](https://hole.money)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#c3c3c3` / `#1c1c1c`)
- **Summary**: Money Hole is a free personal finance manager for tracking income, expenses, accounts and budgets. Analytics, multi-currency support and...
- **Total Clean CSS Variables Extracted**: `59` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IBM Plex Serif`
- **Body Font Stack**: `IBM Plex Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 120px`, `line-height: 130px`, `font-weight: 700`, `letter-spacing: -0.1px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 70px`, `font-weight: 700`, `letter-spacing: -0.1px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: -0.1px`); rule `body` (`letter-spacing: -.1px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: -0.1px`); rule `small` (`font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#c3c3c3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e4e4e7` | `var(--bg)` in `:root` |
| **Interactive Accent / Highlight** | `#1c1c1c` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#797986` | `var(--ink2)` in `:root` |
| **Structural Hairline Border** | `#d7d7db` | `var(--divider)` in `:root` |
| **Variable Token (`--module`)** | `#ffffff` | `var(--module)` in `:root` |
| **Variable Token (`--primary`)** | `#18181b` | `var(--primary)` in `:root` |
| **Variable Token (`--grab`)** | `#afafb6` | `var(--grab)` in `:root` |
| **Variable Token (`--shadow-btn`)** | `#000000` | `var(--shadow-btn)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ios` | `cubic-bezier(.32,.72,0,1)` | Motion / Timing Token |
| `--bg` | `#e4e4e7` | Canvas / Surface Token |
| `--module` | `#ffffff80` | Color / Atmospheric Token |
| `--card` | `#ffffff` | Color / Atmospheric Token |
| `--glass` | `#ffffff73` | Color / Atmospheric Token |
| `--bsm` | `#ffffff4d` | Color / Atmospheric Token |
| `--primary` | `#18181b` | Brand / Palette Token |
| `--grab` | `#afafb6` | Color / Atmospheric Token |
| `--divider` | `#d7d7db` | Color / Atmospheric Token |
| `--gstroke` | `#ffffff73` | Elevation / Border Token |
| `--shadow-btn` | `#0000000a` | Elevation / Border Token |
| `--icon-shadow` | `#0000000a` | Elevation / Border Token |
| `--ink` | `#18181b` | Typography Ink Token |
| `--ink2` | `#797986` | Typography Ink Token |
| `--inv` | `#ffffff` | Color / Atmospheric Token |
| `--ph` | `#afafb6` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.paused> — `hole-money`)**:
   - Landmark `<header class="paused">` (`1400x20px`) hosting `Money Hole` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-c="0"`, `data-m="0"`, `data-s="1"`, `data-v="incT"`), and stylesheet rule `.stage { position:relative;width:432px;height:871px }`.
2. **Hero Stage & Focal Lead (<section.sl> — `Manage Your Finance`)**:
   - Landmark `<section class="sl show">` presenting display lead `Manage Your Finance` and copy excerpt *"Spending by Category"* over `#c3c3c3` canvas and `#0000ee` ink.
3. **Primary Showcase & Content Grid (<section.sl:nth(2)> — `Manage Your Finance Manage Your Fi`)**:
   - Landmark `<section class="sl">` rendering section `Manage Your Finance Manage Your Finance` with copy *"For example, Salary to Cash, ten thousand dollars"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon.ico`), and grid rule `.device { position:absolute;left:0;top:0;width:432px;height:871px;transform-origin... }`.
4. **Interactive Detail & Feature Matrix (<section.sl:nth(3)> — `For example, Salary to Cash, ten t`)**:
   - Landmark `<section class="sl">` framing `For example, Salary to Cash, ten thousand dollar` and `Manage Your Finance` (*"Manage Your Finance"*) with `#e4e4e7` surface cards, `#1c1c1c` accents, and `.dcut { position:absolute;background:linear-gradient(817e73,c3beac);border-radiu... }`.
5. **Colophon & Global Directory Footer (<footer.dframe> — `https://hole.money`)**:
   - Landmark `<footer class="dframe">` anchoring `Money Hole` footer links (`Overview · Index · Archive · About · Contact`), copy *"– no intrusive ads or subscriptions"*, and `#d7d7db` structural dividers.
