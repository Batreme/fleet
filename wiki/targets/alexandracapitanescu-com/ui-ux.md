---
title: "UI & UX Architecture: alexandracapitanescu-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: alexandracapitanescu-com

## Overview & Design Identity
- **Target**: `alexandracapitanescu-com` (**Alexandra Căpitănescu - Official Website**)
- **Production URL**: [https://alexandracapitanescu.com/](https://alexandracapitanescu.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0b090a` canvas, `#e2d9d0` ink, `#ff0000` accent)
- **Summary**: Romanian artist Alexandra Căpitănescu and her band blend alternative rock, raw emotion and explosive live energy.
- **Total Clean CSS Variables Extracted**: `33` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `hershey`
- **Body Font Stack**: `hershey Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-display: "Times New Roman", Times, serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 149.76px`, `line-height: 134.784px`, `font-weight: 400`, `letter-spacing: -5.2416px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `.section-title` (`font-size: clamp(56px,6.6vw,110px)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: Arial, Helvetica, sans-serif`; rule `p` (`font-size: clamp(18px,1.6vw,22px)`, `line-height: 1.2`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 10px`, `letter-spacing: .14em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b090a` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#e2d9d0` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff0000` | `::selection { background: red }` (`#ff0000`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.stream-link__arrow { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#e0514f` | `.submit__error { color: #e0514f }` |
| **Structural Hairline Border** | `#ff0000` | `.intro-pulse svg { stroke: #ff0000 }` |
| **Variable Token (`--color-red`)** | `#ba1818` | `var(--color-red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--intro-total` | `4.7s` | Motion / Timing Token |
| `--ease-out-expo` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ease-in-expo` | `cubic-bezier(.7, 0, .84, 0)` | Motion / Easing Token |
| `--ease-door` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Easing Token |
| `--font-hershey-noailles` | `"hershey", "hershey Fallback"` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |
| `--text-2xl--line-height` | `calc(2 / 1.5)` | Typography Ink Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-red` | `#ba1818` | Brand / Palette Token |
| `--color-cream` | `#e2d9d0` | Brand / Palette Token |
| `--color-ink` | `#0b090a` | Typography Ink Token |
| `--font-display` | `"Times New Roman", Times, serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `alexandracapitanescu-com`)**:
   - Landmark `<header class="site-header intro-reveal">` (`1440x72px`) hosting `Alexandra Căpitănescu - Official Web` navigation (`Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-side="left"`, `data-accent="true"`), and stylesheet rule `font-face { font-family:hershey;src:url(../media/HersheyNoaillesTimes-s.p.2873syaszu... }`.
2. **Hero Stage & Focal Lead (<section.h-svh> — `Alexandra Căpitănescu`)**:
   - Landmark `<section class="h-svh overflow-clip">` presenting display lead `Alexandra Căpitănescu` and copy excerpt *"Out now Latest Choke Me"* over `#0b090a` canvas and `#e2d9d0` ink.
3. **Primary Showcase & Content Grid (<section.px-2> — `The Sound Of Our Story`)**:
   - Landmark `<section class="px-2 pt-20">` rendering section `The Sound Of Our Story` with copy *"Alexandra Căpitănescu"*, asset references (`1uywzyker6zod.css`, `2j1ir--xjy6fe.css`, `1dx8d72ay49iv.js`, `0s2cptn1mmf6r.js`), and grid rule `.RhbOdG_className { font-family:hershey,hershey Fallback }`.
4. **Interactive Detail & Feature Matrix (<section.bg-ink> — `We Are Making “Noise”`)**:
   - Landmark `<section class="bg-ink relative">` framing `We Are Making “Noise”` and `Made by you.` (*"Alternative rock, raw emotion and live energy — the sound of Alex"*) with `#ff0000` surface cards, `#ff0000` accents, and `.RhbOdG_variable { --font-hershey-noailles:"hershey", "hershey Fallback" }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://alexandracapitanescu.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Alexandra Căpitănescu - Official` footer links (`Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`), copy *"( 01 ) Choke Me Album · 2026"*, and `#ff0000` structural dividers.
