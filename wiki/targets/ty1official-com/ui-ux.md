# UI & UX Architecture: ty1official-com

## Overview & Design Identity
- **Target**: `ty1official-com` (**TY1 — DJ & Producer**)
- **Production URL**: [https://ty1official.com](https://ty1official.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0b0c` / `#c14e12`)
- **Summary**: TY1, tra i DJ e producer più influenti della scena Hip Hop italiana. Prossimi live, ultime uscite, riconoscimenti e booking.
- **Total Clean CSS Variables Extracted**: `172` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Humane`
- **Body Font Stack**: `Thunder`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Thunder", "Anton", "Arial Narrow", system-ui, sans-serif`, `--step-h1: clamp(2.4rem, 8vw, 6.5rem)`
- **Section Heading (`H2`)**: CSS variables `--step-h2: clamp(1.9rem, 5vw, 3.75rem)`
- **Body Copy**: CSS variables `--font-body: "Atkinson Hyperlegible", system-ui, -apple-system, "Segoe UI", sans-serif`, `--step-body: clamp(1rem, 1.05vw, 1.2rem)`
- **Metadata & Labels**: CSS variables `--step-small: clamp(.78rem, .95vw, .95rem)`; rule `small` (`font-size: clamp(0.62rem, 2.2vw, 0.9rem)`, `letter-spacing: 0.5em`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0b0c` | `var(--c-black)` in `:root` |
| **Primary Typography Ink** | `#ec651d` | `var(--c-orange)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d7d6d5` | `var(--c-white)` in `:root` |
| **Interactive Accent / Highlight** | `#c14e12` | `var(--c-orange-deep)` in `:root` |
| **Secondary / Muted Copy** | `#ff7d33` | `var(--c-orange-bright)` in `:root` |
| **Structural Hairline Border** | `#1a1617` | `var(--c-ink)` in `:root` |

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
   - Landmark `<header class="testata">` hosting `TY1 — DJ & Producer` navigation (`A p p l e M u s i c · D e e z e r · S o u n d C l o u d · S p o t i f y`), DOM attributes (`data-world="artist"`, `data-suono`, `data-testata`, `data-fit="0.98"`), and stylesheet rule `property --sfondo-t { syntax: "<number>"; inherits: true; initial-value: 1; }`.
2. **Hero Stage & Focal Lead (<section.intro> — `TY1 — DJ & Producer, Junkie Musik`)**:
   - Landmark `<section class="intro vscroll">` presenting display lead `TY1 — DJ & Producer, Junkie Musik` and copy excerpt *"J u n k i e M u s i k"* over `#0d0b0c` canvas and `#d7d6d5` ink.
3. **Primary Showcase & Content Grid (<section.trasf> — `Fuori ora`)**:
   - Landmark `<section class="trasf vscroll">` rendering section `Fuori ora` with copy *"Clicca il video per ingrandirlo"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `font-face { font-family:Thunder;src:local("Thunder");font-weight:700;font-style:norm... }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Il vinile di Junkie Musik`)**:
   - Landmark `<section class="section vinile">` framing `Il vinile di Junkie Musik` and `G i o c a e v i n c i u n i n c o n t r o c o n T...` (*"S i d e A · S i d e B"*) with `#d7d6d5` surface cards, `#c14e12` accents, and `.consenso__piu { position:absolute;bottom:4px;font:400 14px/1 Inter,system-ui,sans-serif;... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ty1official.com`)**:
   - Landmark `<footer class="footer">` anchoring `TY1 — DJ & Producer` footer links (`A p p l e M u s i c · D e e z e r · S o u n d C l o u d · S p o t i f y`), copy *"G i o c a e v i n c i u n"*, and `#1a1617` structural dividers.
