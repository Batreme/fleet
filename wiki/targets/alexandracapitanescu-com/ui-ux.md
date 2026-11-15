# UI & UX Architecture: alexandracapitanescu-com

## Overview & Design Identity
- **Target**: `alexandracapitanescu-com` (**Alexandra Căpitănescu - Official Website**)
- **Production URL**: [https://alexandracapitanescu.com/](https://alexandracapitanescu.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#ba1818` canvas, `#e2d9d0` ink, `#0000` accent)
- **Summary**: Romanian artist Alexandra Căpitănescu and her band blend alternative rock, raw emotion and explosive live energy.
- **Total Clean CSS Variables Extracted**: `33` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `hershey`
- **Body Font Stack**: `hershey Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Times New Roman", Times, serif`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `.section-title` (`font-size: clamp(56px,6.6vw,110px)`)
- **Body Copy**: CSS variables `--font-body: Arial, Helvetica, sans-serif`; rule `p` (`font-size: clamp(18px,1.6vw,22px)`, `line-height: 1.2`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 10px`, `letter-spacing: .14em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ba1818` | `var(--color-red)` in `:root` |
| **Primary Typography Ink** | `#e2d9d0` | `var(--color-cream)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0b090a` | `var(--color-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#ff0000` | `::selection { background: red }` (`#ff0000`) |
| **Structural Hairline Border** | `#000` | `.intro-mask { background: #000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--font-body` | `Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-hershey` | `var(--font-hershey-noailles), "Times New Roman", serif` | Typography / Scale Token |
| `--intro-total` | `4.7s` | Motion / Timing Token |
| `--ease-out-expo` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `alexandracapitanescu-com`)**:
   - Landmark `<header class="site-header intro-reveal">` hosting `Alexandra Căpitănescu - Official Web` navigation (`Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-side="left"`, `data-accent="true"`), and stylesheet rule `font-face { font-family:hershey;src:url(../media/HersheyNoaillesTimes-s.p.2873syaszu... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Alexandra Căpitănescu`)**:
   - Landmark `<section class="relative flex">` presenting display lead `Alexandra Căpitănescu` and copy excerpt *"Music Releases & videos"* over `#ba1818` canvas and `#e2d9d0` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `The Sound Of Our Story`)**:
   - Landmark `<section class="relative mx-auto">` rendering section `The Sound Of Our Story` with copy *"Tickets Tour dates"*, asset references (`1uywzyker6zod.css`, `2j1ir--xjy6fe.css`, `1dx8d72ay49iv.js`, `0s2cptn1mmf6r.js`), and grid rule `.RhbOdG_className { font-family:hershey,hershey Fallback }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Choke Me`)**:
   - Landmark `<section class="relative bg-ink">` framing `Choke Me` and `We Are Making “Noise”` (*"News From the road"*) with `#0b090a` surface cards, `#0000` accents, and `.RhbOdG_variable { --font-hershey-noailles:"hershey", "hershey Fallback" }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://alexandracapitanescu.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Alexandra Căpitănescu - Official` footer links (`Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`), copy *"Fan Art Made by you"*, and `#000` structural dividers.
