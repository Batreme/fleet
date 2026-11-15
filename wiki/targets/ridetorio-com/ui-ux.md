# UI & UX Architecture: ridetorio-com

## Overview & Design Identity
- **Target**: `ridetorio-com` (**The Ride to Rio · Bicycle documentary, Los Angeles to Rio**)
- **Production URL**: [https://ridetorio.com/](https://ridetorio.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#F4EAD0` / `#4A4337`)
- **Summary**: A documentary about five friends who cycled 10,000 miles from Los Angeles to Rio de Janeiro. Watch the trailers and full film, and follow...
- **Total Clean CSS Variables Extracted**: `25` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Alfa Slab One`
- **Body Font Stack**: `Caveat`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.06rem, 0.98rem + 0.34vw,...`, `.78rem`, `clamp(2rem, 1.2rem + 3.6vw, 4.4rem)`, `1.22em`, `1.5em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.06rem, 0.98rem + 0.34vw,...`, `.78rem`, `clamp(2rem, 1.2rem + 3.6vw, 4.4rem)`, `1.22em`, `1.5em`)
- **Body Copy**: CSS variables `--font-body: "Fraunces", "Iowan Old Style", Georgia, serif`; rule `body` (`font-size: clamp(1.06rem, 0.98rem + 0.34...`, `line-height: 1.55`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.06rem, 0.98rem + 0.34vw,...`, `.78rem`, `clamp(2rem, 1.2rem + 3.6vw, 4.4rem)`, `1.22em`, `1.5em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#F4EAD0` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#FBF4DF` | `var(--paper-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1E1B16` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#4A4337` | `var(--ink-soft)` in `:root` |
| **Secondary / Muted Copy** | `#8C9A4A` | `var(--olive)` in `:root` |
| **Structural Hairline Border** | `#2F4A2C` | `var(--forest)` in `:root` |
| **Variable Token (`--mustard`)** | `#D9A93B` | `var(--mustard)` in `:root` |
| **Variable Token (`--teal`)** | `#2F8F8B` | `var(--teal)` in `:root` |
| **Variable Token (`--red`)** | `#C8452C` | `var(--red)` in `:root` |
| **Variable Token (`--sky`)** | `#A9D3DE` | `var(--sky)` in `:root` |
| **Variable Token (`--dusk`)** | `#F2A27C` | `var(--dusk)` in `:root` |
| **Variable Token (`--night`)** | `#16233A` | `var(--night)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#F4EAD0` | Canvas / Surface Token |
| `--paper-2` | `#FBF4DF` | Canvas / Surface Token |
| `--ink` | `#1E1B16` | Typography Ink Token |
| `--ink-soft` | `#4A4337` | Typography Ink Token |
| `--olive` | `#8C9A4A` | Color / Atmospheric Token |
| `--forest` | `#2F4A2C` | Color / Atmospheric Token |
| `--mustard` | `#D9A93B` | Color / Atmospheric Token |
| `--teal` | `#2F8F8B` | Color / Atmospheric Token |
| `--red` | `#C8452C` | Color / Atmospheric Token |
| `--sky` | `#A9D3DE` | Color / Atmospheric Token |
| `--dusk` | `#F2A27C` | Color / Atmospheric Token |
| `--night` | `#16233A` | Color / Atmospheric Token |
| `--sky-top` | `var(--paper)` | Design System Custom Token |
| `--sky-bot` | `var(--paper)` | Design System Custom Token |
| `--stars` | `0` | Design System Custom Token |
| `--font-body` | `"Fraunces", "Iowan Old Style", Georgia, serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `ridetorio-com`)**:
   - Landmark `<header class="nav">` hosting `The Ride to Rio · Bicycle documentar` navigation (`Trailers · Story · Journey · Film · Contact`), DOM attributes (`data-nav`, `data-hero-video`, `data-play="trailer-2"`, `data-reveal`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `The Ride to Rio`)**:
   - Landmark `<section class="hero">` presenting display lead `The Ride to Rio` and copy excerpt *"Los Angeles → to Rio de Janeiro · 2012–13"* over `#F4EAD0` canvas and `#1E1B16` ink.
3. **Primary Showcase & Content Grid (<section.reel> — `Also showing`)**:
   - Landmark `<section class="reel">` rendering section `Also showing` with copy *"Four friends (five, by Panama), thirteen countries and ten thousa"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`, `fraunces-normal-latin.woff2`), and grid rule `html { background: var(--paper); -webkit-text-size-adjust: 100%; scroll-padding... }`.
4. **Interactive Detail & Feature Matrix (<section.story> — `How to cycle to Brazil without rea`)**:
   - Landmark `<section class="story">` framing `How to cycle to Brazil without really knowing how...` and `What` (*"Play the trailer 2:17"*) with `#1E1B16` surface cards, `#4A4337` accents, and `canvas { display: block; max-width: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.atmos__sky> — `https://ridetorio.com/`)**:
   - Landmark `<footer class="atmos__sky">` anchoring `The Ride to Rio · Bicycle docume` footer links (`Trailers · Story · Journey · Film · Contact`), copy *"Watch the whole film"*, and `#2F4A2C` structural dividers.
