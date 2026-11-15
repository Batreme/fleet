# UI & UX Architecture: pixvibe-ai

## Overview & Design Identity
- **Target**: `pixvibe-ai` (**PixVibe — Free Background Remover, Converter & Upscaler**)
- **Production URL**: [https://pixvibe.ai](https://pixvibe.ai)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#bdbdbd` / `#c23a58`)
- **Summary**: Remove backgrounds, convert, compress, resize, crop and upscale images — free, batch up to 20 at once, right in your browser.
- **Total Clean CSS Variables Extracted**: `565` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `fontInter`
- **Body Font Stack**: `fontInter Fallback`
- **Monospace / Technical Font Stack**: `fontDmMono`
- **Hero Display (`H1`)**: CSS variables `--tool-hero-title-badge-font-size: 12px`, `--text-display: 68px`, `--home-hero-title-size: clamp(44px, 6.3vw, var(--text-hero))`; rule `h1` (`font-size: var(--text-subpage-hero)`, `line-height: var(--leading-subpage...`, `letter-spacing: var(--tracking-subpag...`, `font-weight: var(--subpage...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 25px`, `line-height: 1.14`, `letter-spacing: -.05em`, `font-weight: 700`)
- **Body Copy**: CSS variables `--body: var(--font-inter), Inter, ui-sans-serif, system-ui, sans-serif`, `--text-body-sm: 16px`, `--text-body: 18px`; rule `p` (`font-size: var(--text-body-sm)`)
- **Metadata & Labels**: CSS variables `--tool-processing-label-size: 10px`, `--tool-hero-label-height: 36px`, `--tool-hero-label-font-size: 14px`; rule `small` (`font-size: 12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#bdbdbd` | `var(--tool-background-gray)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--tool-background-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#4d9c63` | `var(--status-success)` in `:root` |
| **Interactive Accent / Highlight** | `#c23a58` | `var(--status-error)` in `:root` |
| **Secondary / Muted Copy** | `#a36b28` | `var(--status-warning)` in `:root` |
| **Structural Hairline Border** | `#232324` | `var(--footer-background)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tool-color-picker-width` | `260px` | Brand / Palette Token |
| `--tool-file-name-max-width` | `24ch` | Layout / Spatial Grid Token |
| `--tool-processing-label-size` | `10px` | Layout / Spatial Grid Token |
| `--remover-scope-title-size` | `13px` | Layout / Spatial Grid Token |
| `--tool-thumbnail-action-font-size` | `11px` | Typography / Scale Token |
| `--tool-thumbnail-action-icon-size` | `14px` | Layout / Spatial Grid Token |
| `--tool-background-gray` | `#bdbdbd` | Canvas / Surface Token |
| `--tool-background-black` | `#000` | Canvas / Surface Token |
| `--tool-hero-enhancer-max-width` | `1760px` | Layout / Spatial Grid Token |
| `--tool-hero-label-height` | `36px` | Layout / Spatial Grid Token |
| `--tool-hero-label-font-size` | `14px` | Typography / Scale Token |
| `--tool-hero-label-icon-size` | `20px` | Layout / Spatial Grid Token |
| `--tool-hero-title-badge-font-size` | `12px` | Typography / Scale Token |
| `--layer-credit-modal` | `9998` | Design System Custom Token |
| `--layer-auth-modal` | `1000000` | Design System Custom Token |
| `--layer-confirm-modal` | `1200` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pv-notification-header> — `pixvibe-ai`)**:
   - Landmark `<header class="pv-notification-header">` hosting `PixVibe — Free Background Remover, C` navigation (`Home · Pricing · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `root { --status-success-soft:color-mix(in srgb, var(--status-success) 10%, var(... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `The private image toolkit for you `)**:
   - Landmark `<section class="home-hero">` presenting display lead `The private image toolkit for you and your AI age...` and copy excerpt *"Free · In-browser processing"* over `#bdbdbd` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.home-section> — `Free image tools`)**:
   - Landmark `<section class="home-section home-toolkit">` rendering section `Free image tools` with copy *"Remove Background Transparent PNG in seconds."*, asset references (`dm_mono_400_latin-s.p.38hmww4cj4v...`, `dm_mono_500_latin-s.p.2yee423r7ah...`, `inter_400_700_latin-s.p.2bn3s6zvc...`, `manrope_400_700_latin-s.p.1sj6eob...`), and grid rule `html { scroll-behavior:smooth;background:var(--canvas) }`.
4. **Interactive Detail & Feature Matrix (<section.home-tool-group> — `Background Remover`)**:
   - Landmark `<section class="home-tool-group">` framing `Background Remover` and `Image Converter` (*"Transparent PNG in seconds."*) with `#4d9c63` surface cards, `#c23a58` accents, and `body { min-width:320px;color:var(--ink);background:var(--canvas);font-family:va... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://pixvibe.ai`)**:
   - Landmark `<footer class="site-footer feedback-footer">` anchoring `PixVibe — Free Background Remove` footer links (`Home · Pricing · Blog`), copy *"Image Converter Switch between image formats."*, and `#232324` structural dividers.
