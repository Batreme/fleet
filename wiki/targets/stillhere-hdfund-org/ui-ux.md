---
title: "UI & UX Architecture: stillhere-hdfund-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: stillhere-hdfund-org

## Overview & Design Identity
- **Target**: `stillhere-hdfund-org` (**STILL HERE. · Three Years in Gaza · HDF**)
- **Production URL**: [https://stillhere.hdfund.org/](https://stillhere.hdfund.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111111` canvas, `#ffffff` ink, `#0000ff` accent)
- **Summary**: Three years. One story. Experience three years of HDF’s work in Gaza from 2023–2026.
- **Total Clean CSS Variables Extracted**: `74` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Opening Barlow`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 126.72px`, `line-height: 117.85px`, `font-weight: 700`, `letter-spacing: -1.9008px`); CSS variables `--display: Barlow,'Arial Narrow',Impact,sans-serif`; rule `h1` (`font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 302.4px`, `line-height: 266.112px`, `font-weight: 900`, `letter-spacing: -6.048px`); rule `h2` (`font-size: clamp(76px,8.8vw,156px)`, `line-height: .93`, `letter-spacing: -.015em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body: Inter,Arial,sans-serif`; rule `p` (`font-size: 14px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: normal`, `font-weight: 600`, `letter-spacing: 1.05px`); rule `small` (`font-size: 12px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `footer` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#090a09` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.button-outline:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#a8aaa1` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#20201e` | `.year-ghost { stroke: #20201e }` |
| **Variable Token (`--ink`)** | `#101210` | `var(--ink)` in `:root` |
| **Variable Token (`--paper`)** | `#eeeee8` | `var(--paper)` in `:root` |
| **Variable Token (`--gold`)** | `#fed545` | `var(--gold)` in `:root` |
| **Variable Token (`--blue`)** | `#2564aa` | `var(--blue)` in `:root` |
| **Variable Token (`--n-paper`)** | `#f7f5f0` | `var(--n-paper)` in `:root` |
| **Variable Token (`--campaign-red`)** | `#bb0305` | `var(--campaign-red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#101210` | Typography Ink Token |
| `--paper` | `#eeeee8` | Canvas / Surface Token |
| `--muted` | `#a8aaa1` | Color / Atmospheric Token |
| `--gold` | `#FED545` | Color / Atmospheric Token |
| `--blue` | `#2564AA` | Color / Atmospheric Token |
| `--display` | `Barlow,'Arial Narrow',Impact,sans-serif` | Design System Custom Token |
| `--body` | `Inter,Arial,sans-serif` | Design System Custom Token |
| `--gutter` | `7.2vw` | Layout / Spatial Grid Token |
| `--n-ink` | `#111111` | Typography Ink Token |
| `--n-paper` | `#F7F5F0` | Canvas / Surface Token |
| `--n-blue` | `#2564AA` | Color / Atmospheric Token |
| `--n-yellow` | `#FED545` | Color / Atmospheric Token |
| `--n-gutter` | `clamp(26px,6.25vw,120px)` | Layout / Spatial Grid Token |
| `--campaign-red` | `#BB0305` | Color / Atmospheric Token |
| `--chapter-gutter` | `var(--n-gutter)` | Layout / Spatial Grid Token |
| `--doc-paper` | `#F7F5F0` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `stillhere-hdfund-org`)**:
   - Landmark `<header class="site-header">` (`1440x112px`) hosting `STILL HERE. · Three Years in Gaza · ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-opening-bootstrap`, `data-site-webpage`, `data-campaign-identity="3e"`, `data-campaign-identity="3e"`), and stylesheet rule `html { scroll-padding-top:100px }`.
2. **Hero Stage & Focal Lead (<section.intro> — `THE WORLD WATCHED.`)**:
   - Landmark `<section class="intro scroll-scene">` presenting display lead `THE WORLD WATCHED.` and copy excerpt *"The opening couldn’t load."* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.first-days> — `THE WORLD WATCHED .`)**:
   - Landmark `<section class="first-days scroll-scene">` rendering section `THE WORLD WATCHED .` with copy *"TIME KEPT MOVING ."*, asset references (`door-leaf.webp`, `al-aqsa-wall-print.webp`, `door-leaf-mono.webp`, `al-aqsa-wall-print-mono.webp`), and grid rule `button:focus-visible { outline:2px solid var(--gold);outline-offset:7px }`.
4. **Interactive Detail & Feature Matrix (<section.timeline-intro> — `THE FIRST DAYS`)**:
   - Landmark `<section class="timeline-intro">` framing `THE FIRST DAYS` and `THREE YEARS . STILL HERE .` (*"SCROLL UP TO BEGIN"*) with `#090a09` surface cards, `#0000ff` accents, and `img { display:block;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.campaign-footer> — `https://stillhere.hdfund.org/`)**:
   - Landmark `<footer class="campaign-footer">` anchoring `STILL HERE. · Three Years in Gaz` footer links (`Overview · Index · Archive · About · Contact`), copy *"GAZA CRISIS RESPONSE"*, and `#20201e` structural dividers.
