---
title: "UI & UX Architecture: www-villiers-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-villiers-ai

## Overview & Design Identity
- **Target**: `www-villiers-ai` (**Private Jet Charter and Empty Leg Flights · Villiers**)
- **Production URL**: [https://www.villiers.ai/](https://www.villiers.ai/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0f0f15` canvas, `#ffffff` ink, `#4879ef` accent)
- **Summary**: Charter a private jet or find an empty leg flight. Villiers is an independent broker that compares vetted operators and quotes one clear...
- **Total Clean CSS Variables Extracted**: `103` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `neue-haas-grotesk-display`
- **Body Font Stack**: `neue-haas-grotesk-display`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14px`, `line-height: 21px`, `font-weight: 400`); CSS variables `--text-h1: 4rem`, `--text-h1-clamp: clamp(64px,4rem,160px)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 52.5px`, `line-height: 46.2px`, `font-weight: 700`, `letter-spacing: -1.575px`); CSS variables `--text-h2: 3.25rem`, `--text-h2-small: 2.333rem`, `--text-h2-clamp: clamp(52px,3.25rem,68px)`
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 21px`, `font-weight: 400`); CSS variables `--text-body: clamp(16px,1rem,9999px)`, `--text-body-sm: clamp(14px,0.875rem,9999px)`, `--text-body-xs: clamp(12px,0.75rem,9999px)`; rule `p` (`line-height: 1.625`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 38.5px`, `line-height: 33.88px`, `font-weight: 600`); CSS variables `--text-h2-small: 2.333rem`, `--text-h2-small-clamp: clamp(37px,2.333rem,44px)`, `--font-jetbrains-mono: "JetBrains Mono","JetBrains Mono Fallback",Menlo,ui-monospace,monospace`; rule `.meta` (`font-size: 13px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0f0f15` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `footer` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1a1a1f` | `var(--empty-search-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#4879ef` | `.accent-accent-blue { color: #4879ef }` |
| **Secondary / Muted Copy** | `#707070` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#707070` | `var(--empty-card-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mobile-bar-h` | `4rem` | Dimension / Scale Token |
| `--background` | `222 47% 11%` | Canvas / Surface Token |
| `--foreground` | `210 40% 98%` | Typography Ink Token |
| `--card` | `222 47% 11%` | Dimension / Scale Token |
| `--card-foreground` | `210 40% 98%` | Typography Ink Token |
| `--popover` | `222 47% 11%` | Dimension / Scale Token |
| `--popover-foreground` | `210 40% 98%` | Typography Ink Token |
| `--primary` | `210 40% 98%` | Brand / Palette Token |
| `--primary-foreground` | `222 47% 11%` | Typography Ink Token |
| `--secondary` | `217.2 32.6% 17.5%` | Brand / Palette Token |
| `--secondary-foreground` | `210 40% 98%` | Typography Ink Token |
| `--muted` | `217.2 32.6% 17.5%` | Dimension / Scale Token |
| `--muted-foreground` | `215 20.2% 82%` | Typography Ink Token |
| `--accent` | `217.2 32.6% 17.5%` | Brand / Palette Token |
| `--accent-foreground` | `210 40% 98%` | Typography Ink Token |
| `--destructive` | `0 62.8% 30.6%` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.left-0> — `www-villiers-ai`)**:
   - Landmark `<header class="left-0 right-0">` (`1440x82px`) hosting `Private Jet Charter and Empty Leg Fl` navigation (`H H O O M M E E · B B L L O O G G · A A B B O O U U T T`), DOM attributes (`data-header-ready="true"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.app-scene_vappSection__NNKxF> — `Your Private Jet Charter`)**:
   - Landmark `<section class="app-scene_vappSection__NNKxF">` presenting display lead `Your Private Jet Charter` and copy excerpt *"© 2026 Villiers. All rights reserved."* over `#0f0f15` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Your charter, on your lock screen.`)**:
   - Landmark `<section class="relative min-h-screen">` rendering section `Your charter, on your lock screen.` with copy *"E E M M P P T T Y Y L L E E G G S S"*, asset references (`0484562807a97172-s.p.woff2`, `2cc74b96cdc9383d-s.p.woff2`, `36966cca54120369-s.p.woff2`, `427e4a37d3642943-s.p.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-section-lg> — `E E M M P P T T Y Y L L E E G G S `)**:
   - Landmark `<section class="py-section-lg bg-neutral-50">` framing `E E M M P P T T Y Y L L E E G G S S` and `E E M M P P T T Y Y` (*"E E M M P P T T Y Y"*) with `#1a1a1f` surface cards, `#4879ef` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-neutral-500> — `https://www.villiers.ai/`)**:
   - Landmark `<footer class="bg-neutral-500 pt-16">` anchoring `Private Jet Charter and Empty Le` footer links (`H H O O M M E E · B B L L O O G G · A A B B O O U U T T`), copy *"v v i i l l l l i i e e r r s s O O S S"*, and `#707070` structural dividers.
