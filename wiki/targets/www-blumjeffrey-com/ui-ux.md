# UI & UX Architecture: www-blumjeffrey-com

## Overview & Design Identity
- **Target**: `www-blumjeffrey-com` (**Jeffrey Blum — AI Digital Creative Director**)
- **Production URL**: [https://www.blumjeffrey.com](https://www.blumjeffrey.com)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#080808` canvas, `#555` ink, `#1e1e1e` accent)
- **Summary**: Jeffrey Blum is a New York-based AI Digital Creative Director building creative systems, intelligent workflows, brand platforms, and digi...
- **Total Clean CSS Variables Extracted**: `46` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Barlow`
- **Body Font Stack**: `Barlow Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(64px,9.6vw,180px)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(64px,9vw,170px)`)
- **Body Copy**: rule `p` (`letter-spacing: .22em`)
- **Metadata & Labels**: rule `small` (`font-size: .6rem`, `letter-spacing: .22em`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#0f0f0f` | `var(--off-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#141414` | `var(--dark)` in `:root` |
| **Interactive Accent / Highlight** | `#1e1e1e` | `var(--mid)` in `:root` |
| **Secondary / Muted Copy** | `#2a2a2a` | `var(--border)` in `:root` |
| **Structural Hairline Border** | `#555` | `var(--muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--motion-instant` | `.12s` | Motion / Easing Token |
| `--motion-fast` | `.2s` | Motion / Easing Token |
| `--motion-medium` | `.3s` | Motion / Easing Token |
| `--motion-slow` | `.4s` | Motion / Easing Token |
| `--motion-reveal` | `.8s` | Motion / Easing Token |
| `--motion-hero` | `.9s` | Motion / Easing Token |
| `--motion-counter` | `1.1s` | Motion / Easing Token |
| `--motion-marquee` | `28s` | Motion / Easing Token |
| `--ease-standard` | `ease` | Motion / Easing Token |
| `--ease-linear` | `linear` | Motion / Easing Token |
| `--ease-pulse` | `ease-in-out` | Motion / Easing Token |
| `--ease-expressive` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--motion-shift-xs` | `4px` | Motion / Easing Token |
| `--motion-shift-sm` | `8px` | Motion / Easing Token |
| `--motion-shift-md` | `20px` | Motion / Easing Token |
| `--motion-shift-lg` | `32px` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cs-hero> — `www-blumjeffrey-com`)**:
   - Landmark `<header class="cs-hero">` hosting `Jeffrey Blum — AI Digital Creative D` navigation (`Work · Lab · Speaking · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-motion="gsap"`), and stylesheet rule `services { overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<section.home> — `Shape vision. Build systems.`)**:
   - Landmark `<section class="home">` presenting display lead `Shape vision. Build systems.` and copy excerpt *"Module / What's New"* over `#080808` canvas and `#555` ink.
3. **Primary Showcase & Content Grid (<section.home-v2> — `Recent projects`)**:
   - Landmark `<section class="home-v2">` rendering section `Recent projects` with copy *"Regular Upper case"*, asset references (`235a0ef330592118-s.p.b3cd1641.woff2`, `303804218d80822e-s.p.9b40bd6c.woff2`, `4f530f52d514af96-s.p.52297690.woff2`, `81cef6a21128489e-s.p.6cf41120.woff2`), and grid rule `after { box-sizing:border-box;border-radius:0;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.clients-scene> — `M·A·C Design System`)**:
   - Landmark `<section class="clients-scene">` framing `M·A·C Design System` and `AI Creative Agents` (*"01 M·A·C Figma Design System"*) with `#141414` surface cards, `#1e1e1e` accents, and `.home-v2 img { max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://www.blumjeffrey.com`)**:
   - Landmark `<footer class="ft fixed">` anchoring `Jeffrey Blum — AI Digital Creati` footer links (`Work · Lab · Speaking · About · Contact`), copy *"M·A·C Figma Design System"*, and `#555` structural dividers.
