# UI & UX Architecture: www-chriswilliamsart-com

## Overview & Design Identity
- **Target**: `www-chriswilliamsart-com` (**Chris Williams Art Gallery · Contemporary painting in London**)
- **Production URL**: [https://www.chriswilliamsart.com/](https://www.chriswilliamsart.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f5f5` / `#d9d9d9`)
- **Summary**: Chris Williams Art Gallery shows contemporary painting in Bethnal Green, East London. Explore the work of seven artists online or visit W...
- **Total Clean CSS Variables Extracted**: `7` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Google Sans Flex`
- **Body Font Stack**: `Google Sans Flex`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `14px`, `11px`, `12px`, `clamp(26px,2.6vw,44px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `14px`, `11px`, `12px`, `clamp(26px,2.6vw,44px)`)
- **Body Copy**: rule `p` (`font-size: 13px`, `line-height: 1.6`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `14px`, `11px`, `12px`, `clamp(26px,2.6vw,44px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f5f5` | `var(--color-bg)` in `:root` |
| **Primary Typography Ink** | `#282828` | `var(--color-fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#aaa` | `var(--color-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#d9d9d9` | `var(--color-placeholder)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `.cursor-dot { color: #fff }` |
| **Structural Hairline Border** | `#5a3f2a` | `.room__art--walnut { background: #5a3f2a }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#f4f5f5` | Canvas / Surface Token |
| `--color-fg` | `#282828` | Typography Ink Token |
| `--color-muted` | `#aaa` | Brand / Palette Token |
| `--color-placeholder` | `#d9d9d9` | Brand / Palette Token |
| `--font-base` | `"Google Sans Flex", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--aspect` | `.75` | Design System Custom Token |
| `--long` | `calc(var(--u) * 364)` | Design System Custom Token |
| `--www-chriswilliam-bg` | `#f4f5f5` | Canvas Substrate (from `var(--color-bg)` in `:root`) |
| `--www-chriswilliam-ink` | `#282828` | Primary Typography Ink (stylesheet-derived) |
| `--www-chriswilliam-surface` | `#aaa` | Surface Substrate (stylesheet-derived) |
| `--www-chriswilliam-accent` | `#d9d9d9` | Interactive Accent (stylesheet-derived) |
| `--www-chriswilliam-muted` | `#fff` | Secondary Ink (stylesheet-derived) |
| `--www-chriswilliam-border` | `#5a3f2a` | Structural Border (stylesheet-derived) |
| `--www-chriswilliam-container` | `82vw` | Container Bound (stylesheet-derived) |
| `--www-chriswilliam-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--www-chriswilliam-pad` | `22px` | Lateral Padding (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-chriswilliamsart-com`)**:
   - Landmark `<header class="site-header">` hosting `Chris Williams Art Gallery · Contemp` navigation (`about a b o u t`), DOM attributes (`data-nav-field`, `data-reveal-text="gallery area"`, `data-reveal-split="1"`, `data-char="g"`), and stylesheet rule `body { overscroll-behavior:none;height:100%;overflow-x:hidden }`.
2. **Hero Stage & Focal Lead (<section.about-intro> — `Chris Williams Art Gallery shows c`)**:
   - Landmark `<section class="about-intro">` presenting display lead `Chris Williams Art Gallery shows contemporary pai...` and copy excerpt *"gallery area g a l l e r y a r e a"* over `#f4f5f5` canvas and `#282828` ink.
3. **Primary Showcase & Content Grid (<section.about-outro> — `History`)**:
   - Landmark `<section class="about-outro">` rendering section `History` with copy *"contacts c o n t a c t s"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `wolfstein-01-CIJigwF-.webp`), and grid rule `button { font:inherit;color:inherit;cursor:pointer;background:0 0;border:none }`.
4. **Interactive Detail & Feature Matrix (<section.about-outro> — `Opening`)**:
   - Landmark `<section class="about-outro">` framing `Opening` and `Jack Wolfstein` (*"Chris Williams Art gallery"*) with `#aaa` surface cards, `#d9d9d9` accents, and `.site-nav { letter-spacing:-.01em;align-items:center;gap:16px;font-size:13px;font-we... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.chriswilliamsart.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Chris Williams Art Gallery · Con` footer links (`about a b o u t`), copy *"Jack Wolfstein J a c k W o l f s t e i n"*, and `#5a3f2a` structural dividers.
