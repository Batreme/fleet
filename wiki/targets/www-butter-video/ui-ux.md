# UI & UX Architecture: www-butter-video

## Overview & Design Identity
- **Target**: `www-butter-video` (**Butter Video · Online Video Editor Engineered for Creativity**)
- **Production URL**: [https://www.butter.video/](https://www.butter.video/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#00ffd0`)
- **Summary**: The first video editor and design platform built with creative code for creative teams. It's a whole new timeline.
- **Total Clean CSS Variables Extracted**: `22` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DieGrotesk`
- **Body Font Stack**: `DieGrotesk Fallback`
- **Monospace / Technical Font Stack**: `monospace)`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(5.6rem,6.6vw,12.5rem)`, `line-height: .92`, `letter-spacing: -1px`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(3.2rem,6vw,7rem)`, `line-height: .94`, `letter-spacing: -.5px`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: clamp(1.05rem,1.5vw,1.25rem)`, `line-height: 1.45`)
- **Metadata & Labels**: rule `small` (`font-size: inherit`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--perf-text)` in `:root` |
| **Primary Typography Ink** | `#a0aec0` | `var(--perf-text-dim)` in `:root` |
| **Elevated Surface / Card Substrate** | `#718096` | `var(--perf-text-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#00ffd0` | `var(--perf-fps)` in `:root` |
| **Secondary / Muted Copy** | `#ff9f43` | `var(--perf-gpu)` in `:root` |
| **Structural Hairline Border** | `#a78bfa` | `var(--perf-cpu)` in `:root` |
| **Variable Token (`--perf-success`)** | `#10b981` | `var(--perf-success)` in `:root` |
| **Variable Token (`--perf-warning`)** | `#f59e0b` | `var(--perf-warning)` in `:root` |
| **Variable Token (`--perf-danger`)** | `#ef4444` | `var(--perf-danger)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--perf-bg` | `rgba(8, 10, 15, .92)` | Canvas / Surface Token |
| `--perf-glass` | `rgba(255, 255, 255, .03)` | Color / Atmospheric Token |
| `--perf-border` | `rgba(255, 255, 255, .08)` | Elevation / Border Token |
| `--perf-text` | `#ffffff` | Typography Ink Token |
| `--perf-text-dim` | `#a0aec0` | Typography Ink Token |
| `--perf-text-muted` | `#718096` | Typography Ink Token |
| `--perf-gauge-bg` | `rgba(0, 0, 0, .15)` | Canvas / Surface Token |
| `--perf-fps` | `#00ffd0` | Color / Atmospheric Token |
| `--perf-gpu` | `#ff9f43` | Color / Atmospheric Token |
| `--perf-cpu` | `#a78bfa` | Color / Atmospheric Token |
| `--perf-success` | `#10b981` | Color / Atmospheric Token |
| `--perf-warning` | `#f59e0b` | Color / Atmospheric Token |
| `--perf-danger` | `#ef4444` | Color / Atmospheric Token |
| `--perf-gradient-primary` | `linear-gradient(135deg, #00ffd0 0%, #a78bfa 100%)` | Brand / Palette Token |
| `--perf-radius` | `12px` | Elevation / Border Token |
| `--perf-radius-sm` | `8px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.kbhUnc> — `www-butter-video`)**:
   - Landmark `<header class="kbhUnc">` hosting `Butter Video · Online Video Editor E` navigation (`Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-styled="active"`, `data-styled-version="6.4.4"`), and stylesheet rule `.__className_8d5843 { font-family:DieGrotesk,DieGrotesk Fallback;font-weight:400;font-style:no... }`.
2. **Hero Stage & Focal Lead (<section.hsoZjO> — `Engineered for Creativity Engineer`)**:
   - Landmark `<section class="hsoZjO">` presenting display lead `Engineered for Creativity Engineered for Creativity` and copy excerpt *"It's a whole new timeline."* over `#ffffff` canvas and `#718096` ink.
3. **Primary Showcase & Content Grid (<section.glnUmG> — `Butter is the first video editor w`)**:
   - Landmark `<section class="glnUmG">` rendering section `Butter is the first video editor where creatives...` with copy *"Co-Create Co-Create"*, asset references (`5fb8d156cdd6d753-s.p.woff2`, `da60608f2183158e-s.p.woff2`, `2836d44e2fdcb041.css`, `6294d87c4b6dbd81.css`), and grid rule `.__className_210739 { font-family:ABCDiatype,ABCDiatype Fallback;font-weight:400;font-style:no... }`.
4. **Interactive Detail & Feature Matrix (<section.lhNRew> — `Browse curated blocks for motion g`)**:
   - Landmark `<section class="lhNRew">` framing `Browse curated blocks for motion graphics, kineti...` and `Make blocks your own with intuitive dials, slider...` (*"Templates Templates"*) with `#718096` surface cards, `#00ffd0` accents, and `.CreatorSlice_inner__5XvuM { width:100%;max-width:1920px;margin-inline:auto }`.
5. **Colophon & Global Directory Footer (<footer.bdNowa> — `https://www.butter.video/`)**:
   - Landmark `<footer class="bdNowa">` anchoring `Butter Video · Online Video Edit` footer links (`Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`), copy *"Product Product Explore features Explore features"*, and `#a78bfa` structural dividers.
