---
title: "UI & UX Architecture: www-kaviengcreative-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-kaviengcreative-com

## Overview & Design Identity
- **Target**: `www-kaviengcreative-com` (**Kavieng Cheng · Art Director and Creative**)
- **Production URL**: [https://www.kaviengcreative.com/](https://www.kaviengcreative.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#050505` canvas, `#f0efe9` ink, `#62625e` accent)
- **Summary**: Kavieng Cheng is a Hong Kong-based art director and creative working across advertising, product, fine art and photography.
- **Total Clean CSS Variables Extracted**: `10` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Heros`
- **Body Font Stack**: `Heros`
- **Monospace / Technical Font Stack**: `Junicode`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 18px`, `line-height: 13.68px`, `font-weight: 700`, `letter-spacing: -0.45px`); rule `h1` (`letter-spacing: -.055em`)
- **Section Heading (`H2`)**: observed font-size ladder: `18px`, `16px`, `13px`, `12px`, `11px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`letter-spacing: -.006em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#050505` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f0efe9` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `html { background: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#62625e` | `.filter-projects button span:la... { color: #62625e }` |
| **Secondary / Muted Copy** | `#0a0a09` | `var(--hard-ink)` in `:root` |
| **Structural Hairline Border** | `#060606` | `var(--rule-dark)` in `:root` (`rgba(10, 10, 9, .19)`) |
| **Variable Token (`--page-grey`)** | `#c9c8c3` | `var(--page-grey)` in `:root` |
| **Variable Token (`--graphite`)** | `#8a8a84` | `var(--graphite)` in `:root` |
| **Variable Token (`--silver`)** | `#aaa9a2` | `var(--silver)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--archive-black` | `#050505` | Canvas / Surface Token |
| `--paper` | `#f0efe9` | Canvas / Surface Token |
| `--page-grey` | `#c9c8c3` | Color / Atmospheric Token |
| `--hard-ink` | `#0a0a09` | Typography Ink Token |
| `--graphite` | `#8a8a84` | Color / Atmospheric Token |
| `--silver` | `#aaa9a2` | Color / Atmospheric Token |
| `--rule-dark` | `rgba(10, 10, 9, .19)` | Canvas / Surface Token |
| `--rule-light` | `rgba(240, 239, 233, .19)` | Canvas / Surface Token |
| `--gutter` | `40px` | Layout / Spatial Grid Token |
| `--perspective-blur` | `0px` | Elevation / Border Token |
| `--www-kaviengcreat-bg` | `#050505` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-kaviengcreat-ink` | `#f0efe9` | Primary Typography Ink (computed-derived) |
| `--www-kaviengcreat-surface` | `#000000` | Surface Substrate (computed-derived) |
| `--www-kaviengcreat-accent` | `#62625e` | Interactive Accent (computed-derived) |
| `--www-kaviengcreat-muted` | `#0a0a09` | Secondary Ink (computed-derived) |
| `--www-kaviengcreat-border` | `#060606` | Structural Border (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.archive-header> — `www-kaviengcreative-com`)**:
   - Landmark `<header class="archive-header">` (`1440x66px`) hosting `Kavieng Cheng · Art Director and Cre` navigation (`Archive · About · Awards · Press · Private`), DOM attributes (`data-route="archive"`, `data-route="archive"`, `data-route="about"`, `data-route="awards"`), and stylesheet rule `app { width:100%;height:100%;margin:0;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.view-shell> — `KAVIENG CHENG`)**:
   - Landmark `<section class="view-shell">` presenting display lead `KAVIENG CHENG` and copy excerpt *"Art director + creative"* over `#050505` canvas and `#f0efe9` ink.
3. **Primary Showcase & Content Grid (<section.view-shell:nth(2)> — `Kavieng Cheng`)**:
   - Landmark `<section class="view-shell">` rendering section `Kavieng Cheng` with copy *"The UN-billed Space"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `main-C5DSeFRy.js`), and grid rule `html { background:var(--archive-black) }`.
4. **Interactive Detail & Feature Matrix (<section.view-shell:nth(3)> — `The UN-billed Space`)**:
   - Landmark `<section class="view-shell">` framing `The UN-billed Space` and `The Touch Annual Report` (*"The Touch Annual Report"*) with `#000000` surface cards, `#62625e` accents, and `body { background:var(--archive-black);color:var(--paper);font-family:Heros,Ari... }`.
5. **Colophon & Global Directory Footer (<footer.loader__hint> — `https://www.kaviengcreative.com/`)**:
   - Landmark `<footer class="loader__hint">` anchoring `Kavieng Cheng · Art Director and` footer links (`Archive · About · Awards · Press · Private`), copy *"The Cigarette Book"*, and `#060606` structural dividers.
