# UI & UX Architecture: www-johnbolster-design

## Overview & Design Identity
- **Target**: `www-johnbolster-design` (**John Bolster · Brand Identity Designer and Art Director, Saratoga Spring...**)
- **Production URL**: [https://www.johnbolster.design/](https://www.johnbolster.design/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ECEAE2` / `#D3D0C6`)
- **Summary**: Independent brand identity designer and art director in Saratoga Springs, NY. Brand strategy, identity, print and web for businesses, hig...
- **Total Clean CSS Variables Extracted**: `22` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Serif Display`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--display: "BebasPro","Bebas Neue","Arial Narrow",Impact,sans-serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `11px`, `clamp(15px,1.15vw,18px)`, `14px`, `22px`)
- **Body Copy**: CSS variables `--body: "Geist",ui-sans-serif,system-ui,sans-serif`; rule `p` (`font-size: clamp(15px,1.15vw,18px)`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--mono: "Geist Mono",ui-monospace,Menlo,monospace`; rule `.mono` (`font-size: 12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ECEAE2` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#121413` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5E6360` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#D3D0C6` | `var(--hair)` in `:root` |
| **Secondary / Muted Copy** | `#2234E0` | `var(--line)` in `:root` |
| **Structural Hairline Border** | `#F47920` | `var(--orange)` in `:root` |
| **Variable Token (`--black`)** | `#0A0A0A` | `var(--black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#ECEAE2` | Canvas / Surface Token |
| `--ink` | `#121413` | Typography Ink Token |
| `--muted` | `#5E6360` | Color / Atmospheric Token |
| `--hair` | `#D3D0C6` | Color / Atmospheric Token |
| `--line` | `#2234E0` | Color / Atmospheric Token |
| `--orange` | `#F47920` | Color / Atmospheric Token |
| `--black` | `#0A0A0A` | Canvas / Surface Token |
| `--display` | `"BebasPro","Bebas Neue","Arial Narrow",Impact,sans-serif` | Design System Custom Token |
| `--body` | `"Geist",ui-sans-serif,system-ui,sans-serif` | Dimension / Scale Token |
| `--mono` | `"Geist Mono",ui-monospace,Menlo,monospace` | Typography / Scale Token |
| `--serif` | `"DM Serif Display",Georgia,serif` | Typography / Scale Token |
| `--gut` | `max(16px, env(safe-area-inset-left, 0px))` | Dimension / Scale Token |
| `--gutR` | `max(16px, env(safe-area-inset-right, 0px))` | Dimension / Scale Token |
| `--fp` | `1` | Design System Custom Token |
| `--sc` | `var(--ink)` | Design System Custom Token |
| `--on` | `clamp(0, calc((var(--fp) * 1.7 - var(--li,0) * .22) * 15 - var(--i)), 1)` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bar> — `www-johnbolster-design`)**:
   - Landmark `<header class="bar">` hosting `John Bolster · Brand Identity Design` navigation (`01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`), DOM attributes (`data-sdkn="@vercel/analytics"`, `data-sdkv="2.0.1"`, `data-go="hero"`, `data-go="about"`), and stylesheet rule `html { background:var(--bg) }`.
2. **Hero Stage & Focal Lead (<section.st> — `About John Bolster`)**:
   - Landmark `<section class="st">` presenting display lead `About John Bolster` and copy excerpt *"John Bolster is an independent brand identity designer and art di"* over `#ECEAE2` canvas and `#121413` ink.
3. **Primary Showcase & Content Grid (<section.st> — `Services`)**:
   - Landmark `<section class="st">` rendering section `Services` with copy *"Brand Strategy: Positioning and differentiation, Audience definit"*, asset references (`favicon-32.png`, `icon-512.png`, `apple-touch-icon.png`, `bebas-neue-pro-semiexp-bold.woff2`), and grid rule `body::-webkit-scrollbar { display:none;width:0;height:0 }`.
4. **Interactive Detail & Feature Matrix (<section.st> — `Selected work`)**:
   - Landmark `<section class="st">` framing `Selected work` and `Contact` (*"Brand Identity: Logo design, Typography and color systems, Guidel"*) with `#5E6360` surface cards, `#D3D0C6` accents, and `img { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.burger> — `https://www.johnbolster.design/`)**:
   - Landmark `<footer class="burger">` anchoring `John Bolster · Brand Identity De` footer links (`01 About · 02 Journey · 03 What I do · 04 Work · 05 Distinkt`), copy *"Art Direction: Campaign concepts, Art direction and imagery"*, and `#F47920` structural dividers.
