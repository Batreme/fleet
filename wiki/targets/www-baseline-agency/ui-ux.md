# UI & UX Architecture: www-baseline-agency

## Overview & Design Identity
- **Target**: `www-baseline-agency` (**Baseline · Brand identity systems, designed and built**)
- **Production URL**: [https://www.baseline.agency/](https://www.baseline.agency/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff3`)
- **Summary**: Brand identity studio in Cluj-Napoca led by Victor Deaconu. Positioning, identity, rules and guidelines in 3 to 4 weeks, for brands that...
- **Total Clean CSS Variables Extracted**: `61` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: CSS variables `--t-display: clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px))`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.875rem`, `.75063rem`, `1.11113rem`, `1em`, `80%`)
- **Body Copy**: CSS variables `--t-body: clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px))`
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--t-label: calc(14*1px)`, `--about-small: clamp(calc(11 * 1px), .88vw, calc(24 * 1px))`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e0e0e0` | `.UwedmG_neutral .UwedmG_layerBase { background: #e0e0e0 }` |
| **Interactive Accent / Highlight** | `#fff3` | `.UwedmG_ghost .UwedmG_layerBase { background: #fff3 }` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#000000` | `.border-black { border-color: black }` (`#000000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink-light` | `0` | Canvas / Surface Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-inter-tight` | `"Inter Tight", "Inter Tight Fallback"` | Typography / Scale Token |
| `--font-hedvig` | `"Hedvig Letters Serif", "Hedvig Letters Serif Fallback"` | Typography / Scale Token |
| `--font-averia` | `"Averia Serif Libre", "Averia Serif Libre Fallback"` | Typography / Scale Token |
| `--font-geist` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--col-r` | `44.5` | Layout / Spatial Grid Token |
| `--row-t` | `61` | Design System Custom Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-baseline-agency`)**:
   - Landmark `<header class="lenis">` hosting `Baseline · Brand identity systems, d` navigation (`About > A b o u t`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.LW-vgW_cta { opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s linear .3s }`.
2. **Hero Stage & Focal Lead (<section.hero-drift> — `You got here with your brand worki`)**:
   - Landmark `<section class="hero-drift relative">` presenting display lead `You got here with your brand working against you....` and copy excerpt *"Baseline B a s e l i n e Studio S t u d i o"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Clients who’ve raised $100M+ betwe`)**:
   - Landmark `<section class="relative text-white">` rendering section `Clients who’ve raised $100M+ between them` with copy *"Baseline B a s e l i n e"*, asset references (`387c923d20582ec7-s.p.2m62wczl7f17...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `9873593f5e895d3f-s.p.1q5z3qm5aeja...`, `a69a711ce91a20c2-s.p.288yeszdmy1l...`), and grid rule `.LW-vgW_dim { opacity:0;transition:opacity 0s linear .3s }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `We rebuild the baseline.`)**:
   - Landmark `<article class="flex flex-col">` framing `We rebuild the baseline.` and `v21 Studio` (*"Studio S t u d i o"*) with `#e0e0e0` surface cards, `#fff3` accents, and `.LW-vgW_line { margin:0 -.1em -.14em;padding:0 .1em .14em;display:block;overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.baseline.agency/`)**:
   - Landmark `<footer class="relative w-full">` anchoring `Baseline · Brand identity system` footer links (`About > A b o u t`), copy *"Services > S e r v i c e s"*, and `#000000` structural dividers.
