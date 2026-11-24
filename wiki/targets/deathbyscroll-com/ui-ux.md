---
title: "UI & UX Architecture: deathbyscroll-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: deathbyscroll-com

## Overview & Design Identity
- **Target**: `deathbyscroll-com` (**Death by Scroll**)
- **Production URL**: [https://deathbyscroll.com](https://deathbyscroll.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#111111` / `#ff0000`)
- **Summary**: Killer scroll animation. Perfect for product launches, microsites, and explainers. Create a cult-like devotion to your brand.
- **Total Clean CSS Variables Extracted**: `91` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Girthy`
- **Body Font Stack**: `Satoshi`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 66px`, `line-height: 66px`, `font-weight: 400`); CSS variables `--font-size--h1: 2.3125rem`, `--line-height--h1: 2.375rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 54px`, `line-height: 54px`, `font-weight: 400`); CSS variables `--font-size--h2: 2.5rem`, `--line-height--h2: 3rem`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.2`, `letter-spacing: 2px`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22px`, `font-weight: 400`); CSS variables `--typeface-body: "Satoshi",sans-serif`, `--typeface-body-bold: "Satoshi Black",sans-serif`, `--line-height--body: 1.375rem`; rule `p` (`font-size: 1rem`, `line-height: 1.25rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 22px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.dxs-footer { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.dxs-menu__link:hover { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#ff5e5e` | `var(--color-red-muted)` in `:root` |
| **Structural Hairline Border** | `#d52127` | `.narrative-heading.narrative-he... { stroke: #d52127 }` |
| **Variable Token (`--color-medium-grey`)** | `#282828` | `var(--color-medium-grey)` in `:root` |
| **Variable Token (`--color-dark-grey`)** | `#1e1e1e` | `var(--color-dark-grey)` in `:root` |
| **Variable Token (`--color-light-grey`)** | `#777777` | `var(--color-light-grey)` in `:root` |
| **Variable Token (`--color-off-white`)** | `#f4efed` | `var(--color-off-white)` in `:root` |
| **Variable Token (`--color-highlight`)** | `#e8e8e8` | `var(--color-highlight)` in `:root` |
| **Variable Token (`--color-purple`)** | `#ae5eff` | `var(--color-purple)` in `:root` |
| **Variable Token (`--color-red-white`)** | `#fad2d2` | `var(--color-red-white)` in `:root` |
| **Variable Token (`--color-green`)** | `#4cc44c` | `var(--color-green)` in `:root` |
| **Variable Token (`--color-shadow-2`)** | `#212121` | `var(--color-shadow-2)` in `:root` |
| **Variable Token (`--color-shadow-3`)** | `#222222` | `var(--color-shadow-3)` in `:root` |
| **Variable Token (`--color-brass`)** | `#f9de95` | `var(--color-brass)` in `:root` |
| **Variable Token (`--color-brass-dark`)** | `#e7b882` | `var(--color-brass-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-off-black` | `#111` | Canvas / Surface Token |
| `--color-medium-grey` | `#282828` | Brand / Palette Token |
| `--color-dark-grey` | `#1e1e1e` | Canvas / Surface Token |
| `--color-light-grey` | `#777` | Canvas / Surface Token |
| `--color-off-white` | `#f4efed` | Canvas / Surface Token |
| `--color-highlight` | `#e8e8e8` | Canvas / Surface Token |
| `--color-red` | `#d52127` | Brand / Palette Token |
| `--color-purple` | `#ae5eff` | Brand / Palette Token |
| `--color-red-rgb` | `213,33,39` | Brand / Palette Token |
| `--color-red-muted` | `#ff5e5e` | Brand / Palette Token |
| `--color-red-white` | `#fad2d2` | Canvas / Surface Token |
| `--color-green` | `#4cc44c` | Brand / Palette Token |
| `--color-shadow-2` | `#212121` | Brand / Palette Token |
| `--color-shadow-3` | `#222` | Brand / Palette Token |
| `--color-brass` | `#f9de95` | Brand / Palette Token |
| `--color-brass-dark` | `#e7b882` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.dxs-header> — `deathbyscroll-com`)**:
   - Landmark `<header class="dxs-header">` (`1440x160px`) hosting `Death by Scroll` navigation (`Summon us Summon us`), DOM attributes (`data-open-accessibility="accessibility-toggle-..."`, `data-end-announce="Summon Us. The page n..."`, `data-guided="prev"`, `data-guided="playpause"`), and stylesheet rule `root { --font-size--h1:5.375rem;--font-size--h2:4rem;--line-height--h1:5.375rem... }`.
2. **Hero Stage & Focal Lead (<section.guided-player> — `DEATH BY SCROLL. KILLER SCROLL ANI`)**:
   - Landmark `<section class="guided-player">` presenting display lead `DEATH BY SCROLL. KILLER SCROLL ANIMATION` and copy excerpt *"A circle of hooded cult members stands on a pentagram sigil in th"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.temple-scene> — `Death by Scroll. Killer scroll ani`)**:
   - Landmark `<section class="temple-scene">` rendering section `Death by Scroll. Killer scroll animation` with copy *"Animation is turned off. Each scene is described in turn below."*, asset references (`tg-girthyultra-webfont.woff2`, `Satoshi-Bold.woff2`, `styles.min.css`, `favicon.png`), and grid rule `html { -webkit-text-size-adjust:100%;line-height:1.15 }`.
4. **Interactive Detail & Feature Matrix (<section.heads-scene> — `Scene player`)**:
   - Landmark `<section class="heads-scene">` framing `Scene player` and `Don't just get people's attention, get inside the...` (*"Play moves through the scenes on its own, naming each chapter. Ne"*) with `#000000` surface cards, `#ff0000` accents, and `main { display:block }`.
5. **Colophon & Global Directory Footer (<footer.dxs-footer> — `https://deathbyscroll.com`)**:
   - Landmark `<footer class="dxs-footer">` anchoring `Death by Scroll` footer links (`Summon us Summon us`), copy *"A cult leaders head splits up like a Russian doll revealing "*, and `#d52127` structural dividers.
