# UI & UX Architecture: xavierjoliot-com

## Overview & Design Identity
- **Target**: `xavierjoliot-com` (**Xavier Joliot · Développeur Créatif**)
- **Production URL**: [https://xavierjoliot.com](https://xavierjoliot.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#3ddc84` / `#f4ead9`)
- **Summary**: Xavier Joliot, développeur créatif à Béziers : branding, UI/UX, stratégie, développement full-stack et mise en production. Disponible imm...
- **Total Clean CSS Variables Extracted**: `37` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Unbounded`
- **Body Font Stack**: `Unbounded Fallback`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: CSS variables `--h1: #ffe066`
- **Section Heading (`H2`)**: CSS variables `--h2: #ff7a3a`; rule `h2` (`font-size: 22px`)
- **Body Copy**: rule `p` (`font-size: 13.5px`, `line-height: 1.65`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`; rule `small` (`letter-spacing: .16em`, `font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3ddc84` | `var(--ok)` in `:root` |
| **Primary Typography Ink** | `#0d0a1a` | `var(--bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#110d20` | `var(--scr)` in `:root` |
| **Interactive Accent / Highlight** | `#f4ead9` | `var(--ink)` in `:root` |
| **Secondary / Muted Copy** | `#9a8fb5` | `var(--dim)` in `:root` |
| **Structural Hairline Border** | `#ff5a36` | `var(--a1)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-unbounded` | `"Unbounded","Unbounded Fallback"` | Typography / Scale Token |
| `--font-chakra` | `"Chakra Petch","Chakra Petch Fallback"` | Typography / Scale Token |
| `--font-space` | `"Space Mono","Space Mono Fallback"` | Typography / Scale Token |
| `--font-vt` | `"VT323","VT323 Fallback"` | Typography / Scale Token |
| `--radius-md` | `.375rem` | Elevation / Border Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |
| `--ease-in-out` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--ok` | `#3ddc84` | Color / Atmospheric Token |
| `--bg` | `#0d0a1a` | Canvas / Surface Token |
| `--scr` | `#110d20` | Color / Atmospheric Token |
| `--ink` | `#f4ead9` | Typography Ink Token |
| `--dim` | `#9a8fb5` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top> — `xavierjoliot-com`)**:
   - Landmark `<header class="top">` hosting `Xavier Joliot · Développeur Créatif` navigation (`FR · EN`), DOM attributes (`data-precedence="next"`, `data-label="Connexion"`, `data-n="1"`, `data-n="2"`), and stylesheet rule `nded_fdf5727d-module__3a_gmq__cla... { font-family:Unbounded,Unbounded Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.screen> — `Xavier Joliot · Développeur Créati`)**:
   - Landmark `<section class="screen">` presenting display lead `Xavier Joliot · Développeur Créatif` and copy excerpt *"3615 Développeur créatif"* over `#3ddc84` canvas and `#0d0a1a` ink.
3. **Primary Showcase & Content Grid (<section.screen> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="screen">` rendering section `Featured Work & Interactive Showcase` with copy *"© 2026 Xavier Joliot"*, asset references (`0c8c4ded07fff55c-s.p.5c4452a7.woff2`, `1ccf8ef962b3f693-s.p.1edb596a.woff2`, `374a88ea0960b3d4-s.p.eb0a589c.woff2`, `8d05cfa5faa8406c-s.p.4adea45d.woff2`), and grid rule `unded_fdf5727d-module__3a_gmq__va... { --font-unbounded:"Unbounded","Unbounded Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.screen> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="screen">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Développement · Branding · UI/UX · Stratégie"*) with `#110d20` surface cards, `#f4ead9` accents, and `etch_f484a735-module__S-MHga__cla... { font-family:Chakra Petch,Chakra Petch Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.sp> — `https://xavierjoliot.com`)**:
   - Landmark `<footer class="sp">` anchoring `Xavier Joliot · Développeur Créa` footer links (`FR · EN`), copy *"Je pense la marque, je conçois l'interface, je développe le "*, and `#ff5a36` structural dividers.
