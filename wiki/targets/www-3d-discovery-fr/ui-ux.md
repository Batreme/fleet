# UI & UX Architecture: www-3d-discovery-fr

## Overview & Design Identity
- **Target**: `www-3d-discovery-fr` (**3D Discovery · Exploring New Dimensions**)
- **Production URL**: [https://www.3d-discovery.fr/](https://www.3d-discovery.fr/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1a1a1a` / `#ebebeb`)
- **Summary**: Transformez vos lieux, projets et produits en expériences web immersives : exploration 3D, contenus et interactions réunis pour présenter...
- **Total Clean CSS Variables Extracted**: `81` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: 1.875rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`)
- **Body Copy**: CSS variables `--bg-body: #1a1a1a`, `--tra-body-h: 16rem`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `2.25rem`, `3rem`, `3.75rem`, `4.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1a1a1a` | `var(--color-primary)` in `:root` |
| **Primary Typography Ink** | `#2e2e2e` | `var(--color-primary-light)` in `:root` |
| **Elevated Surface / Card Substrate** | `#242424` | `var(--bg-elevated)` in `:root` |
| **Interactive Accent / Highlight** | `#ebebeb` | `var(--bg-inverse)` in `:root` |
| **Secondary / Muted Copy** | `#b3b3b3` | `var(--text-secondary)` in `:root` |
| **Structural Hairline Border** | `#999` | `var(--text-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-sora` | `"Sora", "Sora Fallback"` | Typography / Scale Token |
| `--color-primary` | `#1a1a1a` | Brand / Palette Token |
| `--color-primary-light` | `#2e2e2e` | Canvas / Surface Token |
| `--color-primary-dark` | `#1a1a1a` | Canvas / Surface Token |
| `--color-secondary` | `#1a1a1a` | Brand / Palette Token |
| `--header-height` | `64px` | Layout / Spatial Grid Token |
| `--header-height-mobile` | `56px` | Layout / Spatial Grid Token |
| `--container-padding` | `1.5rem` | Layout / Spatial Grid Token |
| `--transition-fast` | `.15s ease` | Motion / Easing Token |
| `--transition-base` | `.2s ease` | Motion / Easing Token |
| `--transition-slow` | `.3s ease` | Motion / Easing Token |
| `--transition-theme` | `.2s ease` | Brand / Palette Token |
| `--z-header` | `30` | Layout / Spatial Grid Token |
| `--z-modal` | `50` | Elevation / Border Token |
| `--z-tooltip` | `70` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-3d-discovery-fr`)**:
   - Landmark `<header class="header">` hosting `3D Discovery · Exploring New Dimensi` navigation (`Solutions · Expériences · Fonctionnalités · Blog`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `nter_2fe1ab3d-module__-T-KAq__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.sg-section> — `Transformez vos lieux en experienc`)**:
   - Landmark `<section class="sg-section">` presenting display lead `Transformez vos lieux en experiences immersives` and copy excerpt *"Planifier une démo"* over `#1a1a1a` canvas and `#ebebeb` ink.
3. **Primary Showcase & Content Grid (<section.sg-section> — `Choisissez votre terrain`)**:
   - Landmark `<section class="sg-section sg-section--seq">` rendering section `Choisissez votre terrain` with copy *"03 Fonctionnalités"*, asset references (`83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `c41ca59f1c34ba31-s.p.0xxb547n1hn7...`, `0ghcmdv7avfm..css`, `04vxxuqck~drg.css`), and grid rule `inter_2fe1ab3d-module__-T-KAq__va... { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.sg-section> — `Voir, c’est comprendre`)**:
   - Landmark `<section class="sg-section sg-solutions">` framing `Voir, c’est comprendre` and `Planifier une démo` (*"3D Discovery · ©2026"*) with `#242424` surface cards, `#ebebeb` accents, and `sora_3fd80e00-module__HLND6q__cla... { font-family:Sora,Sora Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.sg-footer> — `https://www.3d-discovery.fr/`)**:
   - Landmark `<footer class="sg-footer">` anchoring `3D Discovery · Exploring New Dim` footer links (`Solutions · Expériences · Fonctionnalités · Blog`), copy *"Exploring new dimensions"*, and `#999` structural dividers.
