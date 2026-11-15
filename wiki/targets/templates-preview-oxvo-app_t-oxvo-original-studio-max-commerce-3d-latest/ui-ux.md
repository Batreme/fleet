# UI & UX Architecture: templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest

## Overview & Design Identity
- **Target**: `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest` (**SOLARA HALO S1 · Sound with presence.**)
- **Production URL**: [https://templates-preview.oxvo.app/t/oxvo-original-studio-max-commerce-3d/latest/#/](https://templates-preview.oxvo.app/t/oxvo-original-studio-max-commerce-3d/latest/#/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0c0f` / `#f9f6ef`)
- **Summary**: Explore SOLARA HALO S1: a portable spatial speaker with a tactile acoustic shell. Choose a finish and try the local reservation preview.
- **Total Clean CSS Variables Extracted**: `92` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Variable`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `10px`, `13px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 23px`, `letter-spacing: -.04em`, `font-weight: 800`)
- **Body Copy**: rule `p` (`font-size: 11px`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--materials-caption-h: 57px`, `--materials-caption-gap: 12px`; rule `small` (`font-size: 10px`, `letter-spacing: .12em`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0c0f` | `var(--studio-ink)` in `:root` |
| **Primary Typography Ink** | `#16171b` | `var(--studio-panel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f0ece4` | `var(--studio-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#f9f6ef` | `var(--studio-white)` in `:root` |
| **Secondary / Muted Copy** | `#b2b1b8` | `var(--studio-muted)` in `:root` |
| **Structural Hairline Border** | `#b29af3` | `var(--studio-accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist Variable", "Geist Fallback", sans-serif` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `"Geist Variable", "Geist Fallback", sans-serif` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--background` | `oklch(100% 0 0)` | Canvas / Surface Token |
| `--foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--card` | `oklch(100% 0 0)` | Color / Atmospheric Token |
| `--card-foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--popover` | `oklch(100% 0 0)` | Color / Atmospheric Token |
| `--popover-foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--primary` | `oklch(20.5% 0 0)` | Brand / Palette Token |
| `--primary-foreground` | `oklch(98.5% 0 0)` | Typography Ink Token |
| `--secondary` | `oklch(97% 0 0)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest`)**:
   - Landmark `<header class="site-header">` hosting `SOLARA HALO S1 · Sound with presence` navigation (`The idea · Design · Finishes · Specifications`), DOM attributes (`data-first-load="done"`, `data-first-load-path="warm@3365"`, `data-oxvo-mounted-static-preview-router`, `data-product-runtime-ready="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.immersive-hero> — `SOUND THAT HOLDS THE ROOM.`)**:
   - Landmark `<section class="immersive-hero">` presenting display lead `SOUND THAT HOLDS THE ROOM.` and copy excerpt *"Skip to main content"* over `#0b0c0f` canvas and `#f9f6ef` ink.
3. **Primary Showcase & Content Grid (<section.content-band> — `WRAPPED AROUND AIR.`)**:
   - Landmark `<section class="content-band promise-band">` rendering section `WRAPPED AROUND AIR.` with copy *"Choose your finish"*, asset references (`index-B571lmvU.js`, `index-CiVtvupN.css`, `geist-latin-wght-normal-Dm3htQBi....`, `PersistentProductCanvas-m78oPoe0.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.persistent-product-canvas> — `TACTILE BY DESIGN.`)**:
   - Landmark `<article class="persistent-product-canvas">` framing `TACTILE BY DESIGN.` and `BUILT FOR THE SECOND ROOM.` (*"Portable spatial speaker"*) with `#f0ece4` surface cards, `#f9f6ef` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://templates-preview.oxvo.app/t/oxvo-original-studio-max-commerce-3d/latest/#/`)**:
   - Landmark `<footer class="site-footer">` anchoring `SOLARA HALO S1 · Sound with pres` footer links (`The idea · Design · Finishes · Specifications`), copy *"Preparing your experience"*, and `#b29af3` structural dividers.
