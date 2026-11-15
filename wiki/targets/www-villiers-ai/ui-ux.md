# UI & UX Architecture: www-villiers-ai

## Overview & Design Identity
- **Target**: `www-villiers-ai` (**Private Jet Charter and Empty Leg Flights · Villiers**)
- **Production URL**: [https://www.villiers.ai/](https://www.villiers.ai/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0f0f15` canvas, `#f8f9f9` ink, `#1a1a1f` accent)
- **Summary**: Charter a private jet or find an empty leg flight. Villiers is an independent broker that compares vetted operators and quotes one clear...
- **Total Clean CSS Variables Extracted**: `91` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Benton Fallback`
- **Body Font Stack**: `Haas Display Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--text-h1: 4rem`, `--text-h1-clamp: clamp(64px,4rem,160px)`
- **Section Heading (`H2`)**: CSS variables `--text-h2: 3.25rem`, `--text-h2-small: 2.333rem`, `--text-h2-clamp: clamp(52px,3.25rem,68px)`
- **Body Copy**: CSS variables `--text-body: clamp(16px,1rem,9999px)`, `--text-body-sm: clamp(14px,0.875rem,9999px)`, `--text-body-xs: clamp(12px,0.75rem,9999px)`; rule `p` (`line-height: 1.625`)
- **Metadata & Labels**: CSS variables `--text-h2-small: 2.333rem`, `--text-h2-small-clamp: clamp(37px,2.333rem,44px)`, `--font-jetbrains-mono: "JetBrains Mono","JetBrains Mono Fallback",Menlo,ui-monospace,monospace`; rule `.meta` (`font-size: 13px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0f0f15` | `var(--empty-bg)` in `:root` |
| **Primary Typography Ink** | `#f8f9f9` | `var(--empty-fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d9d9d9` | `var(--empty-sec)` in `:root` |
| **Interactive Accent / Highlight** | `#1a1a1f` | `var(--empty-search-bg)` in `:root` |
| **Secondary / Muted Copy** | `#b4b4b2` | `var(--empty-pill-unselected-text)` in `:root` |
| **Structural Hairline Border** | `#29292b` | `var(--empty-card-bg)` in `:root` |

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
1. **Brand Header & Navigation Bar (<header.fixed> — `www-villiers-ai`)**:
   - Landmark `<header class="fixed left-0">` hosting `Private Jet Charter and Empty Leg Fl` navigation (`H H O O M M E E · B B L L O O G G · A A B B O O U U T T`), DOM attributes (`data-header-ready="true"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `1. Your Route`)**:
   - Landmark `<section class="relative min-h-screen">` presenting display lead `1. Your Route` and copy excerpt *"E E M M P P T T Y Y L L E E G G S S"* over `#0f0f15` canvas and `#f8f9f9` ink.
3. **Primary Showcase & Content Grid (<section.py-section-lg> — `New Trip`)**:
   - Landmark `<section class="py-section-lg bg-neutral-50">` rendering section `New Trip` with copy *"E E M M P P T T Y Y"*, asset references (`0484562807a97172-s.p.woff2`, `2cc74b96cdc9383d-s.p.woff2`, `36966cca54120369-s.p.woff2`, `427e4a37d3642943-s.p.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-section-lg> — `Summary`)**:
   - Landmark `<section class="py-section-lg bg-neutral-50">` framing `Summary` and `Special Requirements` (*"v v i i l l l l i i e e r r s s O O S S"*) with `#d9d9d9` surface cards, `#1a1a1f` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://www.villiers.ai/`)**:
   - Landmark `<footer class="flex flex-col">` anchoring `Private Jet Charter and Empty Le` footer links (`H H O O M M E E · B B L L O O G G · A A B B O O U U T T`), copy *"B B I I T T C C O O I I N N"*, and `#29292b` structural dividers.
