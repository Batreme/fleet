# UI & UX Architecture: ksenpanchenko-com

## Overview & Design Identity
- **Target**: `ksenpanchenko-com` (**Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS**)
- **Production URL**: [https://ksenpanchenko.com/](https://ksenpanchenko.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#a8a8a6`)
- **Summary**: Ksen (Kseniia) Panchenko, independent UX/UI & Product Designer in Dublin: websites, products and design systems for FinTech and SaaS — pl...
- **Total Clean CSS Variables Extracted**: `240` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `GeistSans`
- **Body Font Stack**: `GeistSans Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--type-display-size: 220px`, `--type-display-line-height: 198px`, `--type-display-letter-spacing: -6.6px`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `13px`, `32px`, `52px`, `12px`)
- **Body Copy**: CSS variables `--type-body-lead-size: 24px`, `--type-body-lead-line-height: 31.2px`, `--type-body-lead-letter-spacing: 0px`; rule `p` (`font-size: 16px`, `line-height: 24px`)
- **Metadata & Labels**: CSS variables `--font-family-mono: "JetBrains Mono",ui-monospace,monospace`, `--type-display-letter-spacing: -6.6px`, `--type-heading-large-letter-spacing: 0px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--color-neutral-0)` in `:root` |
| **Primary Typography Ink** | `#f4f1ec` | `var(--color-neutral-50)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f1f0ec` | `var(--color-neutral-100)` in `:root` |
| **Interactive Accent / Highlight** | `#a8a8a6` | `var(--color-neutral-400)` in `:root` |
| **Secondary / Muted Copy** | `#6b6b6b` | `var(--color-neutral-500)` in `:root` |
| **Structural Hairline Border** | `#2b2b2b` | `var(--color-neutral-800)` in `:root` |
| **Variable Token (`--color-neutral-950`)** | `#141414` | `var(--color-neutral-950)` in `:root` |
| **Variable Token (`--color-orange-500`)** | `#ff5c2e` | `var(--color-orange-500)` in `:root` |
| **Variable Token (`--color-orange-600`)** | `#e8461a` | `var(--color-orange-600)` in `:root` |
| **Variable Token (`--color-green-500`)** | `#4dd973` | `var(--color-green-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gap` | `6cqw` | Layout / Spatial Grid Token |
| `--stage` | `min(816px,calc(100vh - var(--component-nav-height)))` | Dimension / Scale Token |
| `--ts` | `64` | Design System Custom Token |
| `--font-geist-sans` | `"GeistSans","GeistSans Fallback"` | Typography / Scale Token |
| `--font-serif-loaded` | `"serif","serif Fallback",Georgia,serif` | Typography / Scale Token |
| `--color-neutral-0` | `#ffffff` | Brand / Palette Token |
| `--color-neutral-50` | `#f4f1ec` | Brand / Palette Token |
| `--color-neutral-100` | `#f1f0ec` | Brand / Palette Token |
| `--color-neutral-400` | `#a8a8a6` | Brand / Palette Token |
| `--color-neutral-500` | `#6b6b6b` | Brand / Palette Token |
| `--color-neutral-800` | `#2b2b2b` | Brand / Palette Token |
| `--color-neutral-950` | `#141414` | Brand / Palette Token |
| `--color-orange-500` | `#ff5c2e` | Brand / Palette Token |
| `--color-orange-600` | `#e8461a` | Brand / Palette Token |
| `--color-green-500` | `#4dd973` | Brand / Palette Token |
| `--font-family-serif` | `var(--font-serif-loaded,"Instrument Serif"),Georgia,serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `ksenpanchenko-com`)**:
   - Landmark `<header class="nav">` hosting `Ksen Panchenko — UX/UI & Product Des` navigation (`Work · About`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-end="1"`), and stylesheet rule `.sw__reel.is-active { opacity:1;visibility:visible;transition:opacity .55s var(--ease-out) .08... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Ksen Panchenko — UX/UI & Product D`)**:
   - Landmark `<section class="hero">` presenting display lead `Ksen Panchenko — UX/UI & Product Designer in Dubl...` and copy excerpt *"Available for projects"* over `#ffffff` canvas and `#2b2b2b` ink.
3. **Primary Showcase & Content Grid (<section.sw> — `Selected work`)**:
   - Landmark `<section class="sw">` rendering section `Selected work` with copy *"Dublin 19:22 GMT+0"*, asset references (`7cb8e1b9ab81be17-s.p.woff2`, `dbccb4a9e22cbf0d-s.p.woff2`, `e872e3f251959e82-s.p.woff2`, `kseniia-cutout.webp`), and grid rule `.sw__reel img { position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacit... }`.
4. **Interactive Detail & Feature Matrix (<section.philo> — `Services`)**:
   - Landmark `<section class="philo">` framing `Services` and `Product & UX` (*"E m a i l m e Email me"*) with `#f1f0ec` surface cards, `#a8a8a6` accents, and `.sw__reel.is-active .sw__win { translate:0 0 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ksenpanchenko.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Ksen Panchenko — UX/UI & Product` footer links (`Work · About`), copy *"Gold London Design Awards 2026 · Emerald24 · UI Design"*, and `#2b2b2b` structural dividers.
