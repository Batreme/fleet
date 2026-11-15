# UI & UX Architecture: iroom-devinthehood-com

## Overview & Design Identity
- **Target**: `iroom-devinthehood-com` (**iRoom framework 3 · Get started**)
- **Production URL**: [https://iroom.devinthehood.com/](https://iroom.devinthehood.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#14181f` ink, `#e3e6eb` accent)
- **Summary**: iRoom, the flex CSS framework: a twelve columns grid, 30+ components, light and dark themes driven by CSS custom properties, parallax, a...
- **Total Clean CSS Variables Extracted**: `113` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Libre Barcode 128 Text`
- **Monospace / Technical Font Stack**: `Libre Barcode 128 Text`
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: clamp(2rem,1.55rem + 1.9vw,2....`, `letter-spacing: -0.02em`)
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: clamp(1.5rem,1.3rem + .9vw,2rem)`, `letter-spacing: -0.015em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `1em`, `1rem`, `100%`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `1em`, `1rem`, `100%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--ir-bg)` in `:root` |
| **Primary Typography Ink** | `#f6f7f9` | `var(--ir-surface-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eceef2` | `var(--ir-surface-3)` in `:root` |
| **Interactive Accent / Highlight** | `#e3e6eb` | `var(--ir-border)` in `:root` |
| **Secondary / Muted Copy** | `#cdd2da` | `var(--ir-border-strong)` in `:root` |
| **Structural Hairline Border** | `#14181f` | `var(--ir-text)` in `:root` |
| **Variable Token (`--ir-text-muted`)** | `#5d6675` | `var(--ir-text-muted)` in `:root` |
| **Variable Token (`--ir-text-subtle`)** | `#8b93a1` | `var(--ir-text-subtle)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ir-bg` | `#ffffff` | Canvas / Surface Token |
| `--ir-surface` | `#ffffff` | Canvas / Surface Token |
| `--ir-surface-2` | `#f6f7f9` | Canvas / Surface Token |
| `--ir-surface-3` | `#eceef2` | Canvas / Surface Token |
| `--ir-border` | `#e3e6eb` | Elevation / Border Token |
| `--ir-border-strong` | `#cdd2da` | Elevation / Border Token |
| `--ir-text` | `#14181f` | Typography Ink Token |
| `--ir-text-muted` | `#5d6675` | Typography Ink Token |
| `--ir-text-subtle` | `#8b93a1` | Typography Ink Token |
| `--ir-inverse-bg` | `#14181f` | Canvas / Surface Token |
| `--ir-inverse-fg` | `#f6f7f9` | Typography Ink Token |
| `--ir-overlay` | `rgba(10, 12, 16, 0.55)` | Color / Atmospheric Token |
| `--ir-shadow-sm` | `0 1px 2px rgba(16, 24, 40, 0.06), 0 1px 3px rgba(16, 24, 40, 0.08)` | Elevation / Border Token |
| `--ir-shadow-xl` | `0 28px 56px -14px rgba(16, 24, 40, 0.28)` | Elevation / Border Token |
| `--ir-soft-mix` | `11%` | Dimension / Scale Token |
| `--ir-border-mix` | `32%` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar> — `iroom-devinthehood-com`)**:
   - Landmark `<header class="navbar navbar-sticky">` hosting `iRoom framework 3 · Get started` navigation (`Get started · Components · CSS · JavaScript · Download`), DOM attributes (`data-theme="auto"`, `data-theme-toggle`, `data-tooltip="Dark theme"`, `data-tooltip-position="bottom"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.demo-hero> — `The flex one, in a flex world.`)**:
   - Landmark `<section class="demo-hero parallax">` presenting display lead `The flex one, in a flex world.` and copy excerpt *"A CSS framework built on flexbox, cascade layers and custom prope"* over `#ffffff` canvas and `#14181f` ink.
3. **Primary Showcase & Content Grid (<section.demo-section> — `Everything a page needs, nothing i`)**:
   - Landmark `<section class="demo-section">` rendering section `Everything a page needs, nothing it does not` with copy *"Classes that read like what they do, a grid that bends to every s"*, asset references (`iroom.ico`, `favicon.png`, `iroom.min.css`, `demo.css`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100%;-webkit-tap-highligh... }`.
4. **Interactive Detail & Feature Matrix (<section.demo-section> — `A real flex grid`)**:
   - Landmark `<section class="demo-section bg-subtle">` framing `A real flex grid` and `Cascade layers` (*"Twelve columns, four sizes, true gaps instead of negative margins"*) with `#eceef2` surface cards, `#e3e6eb` accents, and `body { margin:0;min-height:100vh;min-height:100dvh }`.
5. **Colophon & Global Directory Footer (<footer.demo-footer> — `https://iroom.devinthehood.com/`)**:
   - Landmark `<footer class="demo-footer">` anchoring `iRoom framework 3 · Get started` footer links (`Get started · Components · CSS · JavaScript · Download`), copy *"Reset, tokens, base, layout, components, utilities: an utili"*, and `#14181f` structural dividers.
