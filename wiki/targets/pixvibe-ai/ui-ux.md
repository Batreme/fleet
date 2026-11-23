---
title: "UI & UX Architecture: pixvibe-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: pixvibe-ai

## Overview & Design Identity
- **Target**: `pixvibe-ai` (**PixVibe — Free Background Remover, Converter & Upscaler**)
- **Production URL**: [https://pixvibe.ai](https://pixvibe.ai)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)
- **Summary**: Remove backgrounds, convert, compress, resize, crop and upscale images — free, batch up to 20 at once, right in your browser.
- **Total Clean CSS Variables Extracted**: `565` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `fontJakarta`
- **Body Font Stack**: `fontInter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78px`, `line-height: 78px`, `font-weight: 700`, `letter-spacing: -4px`); CSS variables `--pv-font-display: "Clash Display",system-ui,sans-serif`, `--tool-hero-title-badge-font-size: 12px`, `--text-display: 68px`; rule `h1` (`font-size: clamp(28px,7vw,40px)`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 20px`, `line-height: 28px`, `font-weight: 600`, `letter-spacing: -0.8px`); rule `h2` (`font-size: clamp(21px,1.9vw,26px)`, `line-height: 1.25`, `letter-spacing: -.02em`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--pv-font-body: "Satoshi",system-ui,sans-serif`, `--body: var(--font-inter), Inter, ui-sans-serif, system-ui, sans-serif`, `--text-base: 1rem`; rule `p` (`font-size: clamp(15px,1.1vw,16.5px)`, `line-height: 1.8`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--tool-processing-label-size: 10px`, `--tool-hero-label-height: 36px`, `--tool-hero-label-font-size: 14px`; rule `small` (`font-size: 12px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#18172d` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#bdbdbd` | `var(--tool-background-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.uikit-button-ai { background: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#4d94ff` | `var(--color-secondary)` in `:root` |
| **Structural Hairline Border** | `#e7e9f0` | `var(--module-line)` in `:root` |
| **Variable Token (`--color-primary`)** | `#9b6dff` | `var(--color-primary)` in `:root` |
| **Variable Token (`--pv-bone`)** | `#f0ebe1` | `var(--pv-bone)` in `:root` |
| **Variable Token (`--pv-sheet`)** | `#faf6f0` | `var(--pv-sheet)` in `:root` |
| **Variable Token (`--pv-ink`)** | `#1b1620` | `var(--pv-ink)` in `:root` |
| **Variable Token (`--pv-violet`)** | `#7c3aed` | `var(--pv-violet)` in `:root` |
| **Variable Token (`--pv-fuchsia`)** | `#d946ef` | `var(--pv-fuchsia)` in `:root` |
| **Variable Token (`--pv-coral`)** | `#fb7185` | `var(--pv-coral)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-primary` | `#9b6dff` | Brand / Palette Token |
| `--color-primary-dark` | `#9b6dff` | Canvas / Surface Token |
| `--color-secondary` | `#4d94ff` | Brand / Palette Token |
| `--gradient-primary` | `linear-gradient(135deg, #9b6dff, #4d94ff)` | Brand / Palette Token |
| `--pv-bone` | `#f0ebe1` | Color / Atmospheric Token |
| `--pv-sheet` | `#faf6f0` | Color / Atmospheric Token |
| `--pv-card` | `#fff` | Color / Atmospheric Token |
| `--pv-ink` | `#1b1620` | Typography Ink Token |
| `--pv-muted` | `#1b16209e` | Color / Atmospheric Token |
| `--pv-faint` | `#1b16206b` | Color / Atmospheric Token |
| `--pv-violet` | `#7c3aed` | Color / Atmospheric Token |
| `--pv-fuchsia` | `#d946ef` | Color / Atmospheric Token |
| `--pv-coral` | `#fb7185` | Color / Atmospheric Token |
| `--pv-line` | `#1b16201a` | Color / Atmospheric Token |
| `--pv-line-2` | `#1b16200f` | Color / Atmospheric Token |
| `--pv-grad` | `linear-gradient(100deg,#7c3aed 0%,#d946ef 48%,#fb7185 100%)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pv-notification-header> — `pixvibe-ai`)**:
   - Landmark `<header class="pv-notification-header">` (`419x65px`) hosting `PixVibe — Free Background Remover, C` navigation (`Home · Pricing · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `root { --fv-section-x:16px;--fv-section-top:12px;--fv-section-y:20px }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `The private image toolkit for you `)**:
   - Landmark `<section class="home-hero">` presenting display lead `The private image toolkit for you and your AI age...` and copy excerpt *"Full guide for AI agents, with shortcut URLs and parameters for e"* over `#ffffff` canvas and `#18172d` ink.
3. **Primary Showcase & Content Grid (<section.home-section> — `Free image tools`)**:
   - Landmark `<section class="home-section home-toolkit">` rendering section `Free image tools` with copy *"11 free tools · free batch processing · runs in your browser · pl"*, asset references (`dm_mono_400_latin-s.p.38hmww4cj4v...`, `dm_mono_500_latin-s.p.2yee423r7ah...`, `inter_400_700_latin-s.p.2bn3s6zvc...`, `manrope_400_700_latin-s.p.1sj6eob...`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.home-tool-group> — `Background Remover`)**:
   - Landmark `<section class="home-tool-group">` framing `Background Remover` and `Image Converter` (*"11 free tools · free batch processing · runs in your browser"*) with `#bdbdbd` surface cards, `#0000ff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://pixvibe.ai`)**:
   - Landmark `<footer class="site-footer feedback-footer">` anchoring `PixVibe — Free Background Remove` footer links (`Home · Pricing · Blog`), copy *"· plus 3 Pro tools"*, and `#e7e9f0` structural dividers.
