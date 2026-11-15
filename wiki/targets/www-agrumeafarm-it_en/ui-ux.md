# UI & UX Architecture: www-agrumeafarm-it_en

## Overview & Design Identity
- **Target**: `www-agrumeafarm-it_en` (**Agrumea Farm · Jams, pestos and flavours of Sicily**)
- **Production URL**: [https://www.agrumeafarm.it/en](https://www.agrumeafarm.it/en)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#e94e1b` / `#f39200`)
- **Summary**: Agrumea Farm transforms Sicilian citrus fruits, other fruits and produce into artisanal jams, pestos and preserves with an authentic flavour
- **Total Clean CSS Variables Extracted**: `66` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ivystyle-sans`
- **Body Font Stack**: `ivymode`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--text-display: clamp(4rem, calc(2.9rem + 11vw) ,999999px)`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-base)`, `var(--text-small)`, `var(--text-medium)`, `var(--text-large)`, `.9em`)
- **Body Copy**: CSS variables `--text-base: 1rem`
- **Metadata & Labels**: CSS variables `--text-small: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e94e1b` | `var(--color-orange)` in `:root` |
| **Primary Typography Ink** | `#762530` | `var(--color-border)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdf3eb` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#f39200` | `var(--color-yellow)` in `:root` |
| **Secondary / Muted Copy** | `#ffa500` | `:hover { color: orange }` (`#ffa500`) |
| **Structural Hairline Border** | `#ffffff` | `:hover { color: white }` (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--jar-circle-rotation` | `0deg` | Design System Custom Token |
| `--jar-marquee-top` | `55%` | Dimension / Scale Token |
| `--jar-marquee-w` | `100vw` | Dimension / Scale Token |
| `--jar-marquee-h` | `560px` | Dimension / Scale Token |
| `--jar-marquee-angle` | `10deg` | Design System Custom Token |
| `--jar-item-w` | `200px` | Dimension / Scale Token |
| `--jar-item-h` | `320px` | Dimension / Scale Token |
| `--jar-shape-intro-opacity` | `0` | Design System Custom Token |
| `--jar-shape-intro-y` | `24px` | Dimension / Scale Token |
| `--jar-badge-intro-opacity` | `0` | Design System Custom Token |
| `--jar-badge-intro-y` | `12px` | Dimension / Scale Token |
| `--jar-badge-intro-rotation` | `-18deg` | Design System Custom Token |
| `--jar-parallax-x` | `0` | Design System Custom Token |
| `--jar-parallax-y` | `0` | Design System Custom Token |
| `--jar-badge-shift-x` | `-52%` | Dimension / Scale Token |
| `--color-orange` | `#e94e1b` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.is-initial> — `www-agrumeafarm-it_en`)**:
   - Landmark `<header class="is-initial site-header">` hosting `Agrumea Farm · Jams, pestos and flav` navigation (`IT · EN`), DOM attributes (`data-v-aa931410`, `data-v-3a145d88`, `data-header-theme="dark"`, `data-header-logo="full"`), and stylesheet rule `active { cursor:grabbing }`.
2. **Hero Stage & Focal Lead (<section.jar-slider> — `Agrumea Farm: Sicilian artisan mar`)**:
   - Landmark `<section class="jar-slider">` presenting display lead `Agrumea Farm: Sicilian artisan marmalades, spread...` and copy excerpt *"Agrumea Farm · Jams, pestos and flavours of Sicily"* over `#e94e1b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.jar-slider> — `Agrumea Farm · Jams, pestos and fl`)**:
   - Landmark `<section class="jar-slider">` rendering section `Agrumea Farm · Jams, pestos and flavours of Sici` with copy *"m m e e n n u u c c l l o o s s e e"*, asset references (`use.typekit.net`, `p.typekit.net`, `yey3ruw.css`, `CmsHomePage.CpbPGEL3.css`), and grid rule `.tk-ivystyle-sans { font-family: "ivystyle-sans",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<section.jar-slider> — `m m e e n n u u c c l l o o s s e `)**:
   - Landmark `<section class="jar-slider">` framing `m m e e n n u u c c l l o o s s e e` and `c c l l o o s s e e` (*"c c l l o o s s e e"*) with `#fdf3eb` surface cards, `#f39200` accents, and `.tk-ivymode { font-family: "ivymode",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.site-shell__legal> — `https://www.agrumeafarm.it/en`)**:
   - Landmark `<footer class="site-shell__legal">` anchoring `Agrumea Farm · Jams, pestos and ` footer links (`IT · EN`), copy *"Scroll to discover"*, and `#ffffff` structural dividers.
