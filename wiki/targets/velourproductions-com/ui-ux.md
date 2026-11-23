---
title: "UI & UX Architecture: velourproductions-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: velourproductions-com

## Overview & Design Identity
- **Target**: `velourproductions-com` (**Velour Productions · Vancouver Video & Photography**)
- **Production URL**: [https://velourproductions.com/](https://velourproductions.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f0e5` canvas, `#1a1a1a` ink, `#ff0000` accent)
- **Summary**: Velour Productions is a Vancouver production studio creating cinematic video, photography, social content and creative direction for brands.
- **Total Clean CSS Variables Extracted**: `79` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Velour Display`
- **Body Font Stack**: `Velour Mono`
- **Monospace / Technical Font Stack**: `Velour Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 252px`, `line-height: 181.44px`, `font-weight: 900`); CSS variables `--font-display: "Velour Display", "Arial Narrow", "Helvetica Neue", sans-serif`, `--type-display-caption: clamp(1.25rem, 1.55vw, 1.75rem)`, `--type-display-xs: clamp(2.25rem, 3vw, 3rem)`; rule `h1` (`font-size: var(--type-photo-booth-headline)`, `line-height: .78`, `letter-spacing: 0`, `font-weight: 900`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 194.4px`, `line-height: 149.688px`, `font-weight: 900`); rule `h2` (`font-size: var(--type-display-lg)`, `line-height: .77`, `font-weight: 900`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--type-body: clamp(.875rem, 1.2vw, 1rem)`, `--leading-body: 1.3`; rule `p` (`font-size: var(--type-body)`, `line-height: var(--leading-body)`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10.368px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-mono: "Velour Mono", "Courier New", monospace`, `--type-meta: clamp(.625rem, .72vw, .6875rem)`, `--type-small: clamp(.75rem, .9vw, .8125rem)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f0e5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1a` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e4e0d6` | `.about-profile__portrait { background: #e4e0d6 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.brand-opening__work-link:focus... { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#202020` | `var(--color-ink-soft)` in `:root` |
| **Structural Hairline Border** | `#7c7b76` | `.section-kicker { border-bottom: #7c7b76 }` |
| **Variable Token (`--color-red`)** | `#fe2f00` | `var(--color-red)` in `:root` |
| **Variable Token (`--color-blue`)** | `#3a70e6` | `var(--color-blue)` in `:root` |
| **Variable Token (`--color-taupe`)** | `#a59b87` | `var(--color-taupe)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red` | `#fe2f00` | Brand / Palette Token |
| `--color-blue` | `#3a70e6` | Brand / Palette Token |
| `--color-paper` | `#f4f0e5` | Canvas / Surface Token |
| `--color-ink` | `#1a1a1a` | Typography Ink Token |
| `--color-ink-soft` | `#202020` | Typography Ink Token |
| `--color-taupe` | `#a59b87` | Brand / Palette Token |
| `--font-display` | `"Velour Display", "Arial Narrow", "Helvetica Neue", sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Velour Mono", "Courier New", monospace` | Typography / Scale Token |
| `--type-meta` | `clamp(.625rem, .72vw, .6875rem)` | Typography / Scale Token |
| `--type-small` | `clamp(.75rem, .9vw, .8125rem)` | Typography / Scale Token |
| `--type-body` | `clamp(.875rem, 1.2vw, 1rem)` | Typography / Scale Token |
| `--leading-body` | `1.3` | Typography / Scale Token |
| `--type-display-caption` | `clamp(1.25rem, 1.55vw, 1.75rem)` | Typography / Scale Token |
| `--type-work-filter` | `clamp(1.875rem, 3.6vw, 3.5rem)` | Typography / Scale Token |
| `--type-display-xs` | `clamp(2.25rem, 3vw, 3rem)` | Typography / Scale Token |
| `--type-display-sm` | `clamp(2.75rem, 6.4vw, 6.5rem)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `velourproductions-com`)**:
   - Landmark `<header class="site-header">` (`1425x78px`) hosting `Velour Productions · Vancouver Video` navigation (`Work · About · Instagram · LinkedIn`), DOM attributes (`data-velour-hero-opening-seen="true"`, `data-home-theme="paper"`, `data-velour-hero-phase="ready"`, `data-precedence="next"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.brand-opening> — `WE GIVE YOU A POINT OF VIEW`)**:
   - Landmark `<section class="brand-opening">` presenting display lead `WE GIVE YOU A POINT OF VIEW` and copy excerpt *"You’re building a brand with something to say. We translate that "* over `#f4f0e5` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.work> — `We give you a point of view`)**:
   - Landmark `<section class="work filmstrip">` rendering section `We give you a point of view` with copy *"A selection of films, photographs, campaigns, and brand worlds."*, asset references (`loading-bracket-left.svg`, `loading-dots.svg`, `loading-bracket-right.svg`, `0035rp4bt3s1g.css`), and grid rule `smooth-content { min-height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.services> — `Selected Work`)**:
   - Landmark `<section class="services">` framing `Selected Work` and `Good company. Great stories.` (*"View project 01 Rugby Bricks Photography + Videography 2026"*) with `#e4e0d6` surface cards, `#ff0000` accents, and `smooth-wrapper { overflow-x:clip }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://velourproductions.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Velour Productions · Vancouver V` footer links (`Work · About · Instagram · LinkedIn`), copy *"Photography + Videography"*, and `#7c7b76` structural dividers.
