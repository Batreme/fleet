---
title: "UI & UX Architecture: ty1official-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ty1official-com

## Overview & Design Identity
- **Target**: `ty1official-com` (**TY1 — DJ & Producer**)
- **Production URL**: [https://ty1official.com](https://ty1official.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#181618` / `#ec651d`)
- **Summary**: TY1, tra i DJ e producer più influenti della scena Hip Hop italiana. Prossimi live, ultime uscite, riconoscimenti e booking.
- **Total Clean CSS Variables Extracted**: `174` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Atkinson Hyperlegible`
- **Body Font Stack**: `Atkinson Hyperlegible`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 48px`, `font-weight: 700`); CSS variables `--font-display: "Thunder", "Anton", "Arial Narrow", system-ui, sans-serif`, `--step-h1: clamp(2.4rem, 8vw, 6.5rem)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 480px`, `line-height: 393.6px`, `font-weight: 900`); CSS variables `--step-h2: clamp(1.9rem, 5vw, 3.75rem)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: "Atkinson Hyperlegible", system-ui, -apple-system, "Segoe UI", sans-serif`, `--step-body: clamp(1rem, 1.05vw, 1.2rem)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--step-small: clamp(.78rem, .95vw, .95rem)`; rule `small` (`font-size: clamp(0.62rem, 2.2vw, 0.9rem)`, `letter-spacing: 0.5em`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#181618` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f5` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0d0b0c` | `.consenso__carta { background: #0d0b0c }` |
| **Interactive Accent / Highlight** | `#ec651d` | `.consenso__testo a:hover { color: #ec651d }` |
| **Secondary / Muted Copy** | `#d7d6d5` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#333132` | `var(--line)` in `:root` (`rgba(215, 214, 213, .14)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-display` | `"Thunder", "Anton", "Arial Narrow", system-ui, sans-serif` | Typography / Scale Token |
| `--font-ui` | `"Inter", system-ui, -apple-system, "Segoe UI", sans-serif` | Typography / Scale Token |
| `--font-decorative` | `"Nebulon", "Oswald", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-body` | `"Atkinson Hyperlegible", system-ui, -apple-system, "Segoe UI", sans-serif` | Typography / Scale Token |
| `--step-hero` | `clamp(4rem, 48vw, 550px)` | Dimension / Scale Token |
| `--step-giant` | `clamp(3.5rem, 17vw, 16rem)` | Dimension / Scale Token |
| `--step-h1` | `clamp(2.4rem, 8vw, 6.5rem)` | Typography / Scale Token |
| `--step-h2` | `clamp(1.9rem, 5vw, 3.75rem)` | Typography / Scale Token |
| `--step-h3` | `clamp(1.75rem, .9rem + 3.6vw, 2.8125rem)` | Typography / Scale Token |
| `--step-h5` | `clamp(1rem, .86rem + .6vw, 1.25rem)` | Dimension / Scale Token |
| `--step-body` | `clamp(1rem, 1.05vw, 1.2rem)` | Dimension / Scale Token |
| `--step-small` | `clamp(.78rem, .95vw, .95rem)` | Dimension / Scale Token |
| `--space-3xs` | `clamp(.25rem, .24rem + .05vw, .3125rem)` | Layout / Spatial Grid Token |
| `--space-2xs` | `clamp(.5rem, .47rem + .15vw, .625rem)` | Layout / Spatial Grid Token |
| `--space-xs` | `clamp(.75rem, .7rem + .24vw, .9375rem)` | Layout / Spatial Grid Token |
| `--space-s` | `clamp(1rem, .93rem + .33vw, 1.25rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.testata> — `ty1official-com`)**:
   - Landmark `<header class="testata">` (`1440x76px`) hosting `TY1 — DJ & Producer` navigation (`A p p l e M u s i c · D e e z e r · S o u n d C l o u d · S p o t i f y`), DOM attributes (`data-world="artist"`, `data-suono`, `data-testata`, `data-fit="0.98"`), and stylesheet rule `property --sfondo-t { syntax: "<number>"; inherits: true; initial-value: 1; }`.
2. **Hero Stage & Focal Lead (<section.intro> — `TY1 — DJ & Producer, Junkie Musik`)**:
   - Landmark `<section class="intro vscroll">` presenting display lead `TY1 — DJ & Producer, Junkie Musik` and copy excerpt *"Clicca il video per ingrandirlo"* over `#181618` canvas and `#f5f5f5` ink.
3. **Primary Showcase & Content Grid (<section.trasf> — `Il vinile di Junkie Musik`)**:
   - Landmark `<section class="trasf vscroll">` rendering section `Il vinile di Junkie Musik` with copy *"S i d e A · S i d e B"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `font-face { font-family:Thunder;src:local("Thunder");font-weight:700;font-style:norm... }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `G i o c a e v i n c i u n i n c o `)**:
   - Landmark `<section class="section vinile">` framing `G i o c a e v i n c i u n i n c o n t r o c o n T...` and `Regolamento — Junkie Run` (*"J u n k i e M u s i k"*) with `#0d0b0c` surface cards, `#ec651d` accents, and `.consenso__piu { position:absolute;bottom:4px;font:400 14px/1 Inter,system-ui,sans-serif;... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ty1official.com`)**:
   - Landmark `<footer class="footer">` anchoring `TY1 — DJ & Producer` footer links (`A p p l e M u s i c · D e e z e r · S o u n d C l o u d · S p o t i f y`), copy *"G i o c a e v i n c i u n"*, and `#333132` structural dividers.
