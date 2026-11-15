# UI & UX Architecture: altufanulu-com_en

## Overview & Design Identity
- **Target**: `altufanulu-com_en` (**Altufan Ulu Law Office · Istanbul Legal Counsel**)
- **Production URL**: [https://altufanulu.com/en/](https://altufanulu.com/en/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#050a34` ink, `#fdfaf6` accent)
- **Summary**: Altufan Ulu Law Office provides trusted, fast and strategic legal services in Istanbul. Expert counsel across corporate, employment, IP,...
- **Total Clean CSS Variables Extracted**: `6` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Victor Serif`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 5rem`, `line-height: 1.1`, `font-weight: 300`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.4rem`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`line-height: 1.75!important`)
- **Metadata & Labels**: rule `small` (`font-size: 2rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--white)` in `:root` |
| **Primary Typography Ink** | `#050a34` | `var(--bg-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f4f4f5` | `var(--bg-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#fdfaf6` | `var(--bg)` in `:root` |
| **Secondary / Muted Copy** | `#263a05` | `var(--bg-green-1)` in `:root` |
| **Structural Hairline Border** | `#003726` | `var(--bg-green-2)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `#fff` | Canvas / Surface Token |
| `--bg-blue` | `#050a34` | Canvas / Surface Token |
| `--bg-grey` | `#f4f4f5` | Canvas / Surface Token |
| `--bg` | `#fdfaf6` | Canvas / Surface Token |
| `--bg-green-1` | `#263a05` | Canvas / Surface Token |
| `--bg-green-2` | `#003726` | Canvas / Surface Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--altufanulu-com-e-bg` | `#fff` | Canvas Substrate (from `var(--white)` in `:root`) |
| `--altufanulu-com-e-ink` | `#050a34` | Primary Typography Ink (stylesheet-derived) |
| `--altufanulu-com-e-surface` | `#f4f4f5` | Surface Substrate (stylesheet-derived) |
| `--altufanulu-com-e-accent` | `#fdfaf6` | Interactive Accent (stylesheet-derived) |
| `--altufanulu-com-e-muted` | `#263a05` | Secondary Ink (stylesheet-derived) |
| `--altufanulu-com-e-border` | `#003726` | Structural Border (stylesheet-derived) |
| `--altufanulu-com-e-container` | `1024px` | Container Bound (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `altufanulu-com_en`)**:
   - Landmark `<header class="lenis">` hosting `Altufan Ulu Law Office · Istanbul Le` navigation (`HOME · ABOUT US · PRACTICE AREAS · SECTORS · CAREER`), DOM attributes (`data-optimized="1"`, `data-optimized="1"`, `data-no-transition`, `data-barba="wrapper"`), and stylesheet rule `root { font-size:10px!important }`.
2. **Hero Stage & Focal Lead (<section.hero-content> — `Trusted, fast and strategic legal `)**:
   - Landmark `<section class="hero-content">` presenting display lead `Trusted, fast and strategic legal services.` and copy excerpt *"Learn more about our approach to legal matters, our working philo"* over `#fff` canvas and `#050a34` ink.
3. **Primary Showcase & Content Grid (<section.padding> — `WHY ALTUFAN ULU?`)**:
   - Landmark `<section class="padding">` rendering section `WHY ALTUFAN ULU?` with copy *"Legal matters are approached with foresight, analysis and a disci"*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `site.webmanifest`), and grid rule `pre { margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.padding> — `BOUTIQUE STRUCTURE, INDEPENDENT AP`)**:
   - Landmark `<section class="padding">` framing `BOUTIQUE STRUCTURE, INDEPENDENT APPROACH` and `STRATEGIC SOLUTIONS` (*"01 BOUTIQUE STRUCTURE, INDEPENDENT APPROACH We give every case th"*) with `#f4f4f5` surface cards, `#fdfaf6` accents, and `img { max-width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.page-template-page-en-home> — `https://altufanulu.com/en/`)**:
   - Landmark `<footer class="page-template-page-en-home">` anchoring `Altufan Ulu Law Office · Istanbu` footer links (`HOME · ABOUT US · PRACTICE AREAS · SECTORS · CAREER`), copy *"We give every case the focus it deserves. When needed, we br"*, and `#003726` structural dividers.
