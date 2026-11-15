# UI & UX Architecture: explorajourneys-com_int-en-explora-journal

## Overview & Design Identity
- **Target**: `explorajourneys-com_int-en-explora-journal` (**The Explora Journal, A Magazine by Explora Journeys**)
- **Production URL**: [https://explorajourneys.com/int/en/explora-journal](https://explorajourneys.com/int/en/explora-journal)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#454545` canvas, `#fef2f2` ink, `#ba0c2f` accent)
- **Summary**: Step aboard The Explora Journal for stories of ships and destinations, from wellness and dining to ports and cultures, told through the O...
- **Total Clean CSS Variables Extracted**: `29` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `WT Monarch Nova`
- **Body Font Stack**: `Shapiro`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`font-size: 15px`, `font-weight: 600`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 24px`, `line-height: 140%`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 18px`, `line-height: auto`, `font-weight: 400`)
- **Metadata & Labels**: rule `.label` (`font-size: 9pt`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#454545` | `var(--rich-footer-text-color)` in `:root` |
| **Primary Typography Ink** | `#d1d1d1` | `var(--rich-footer-inactive-color-border)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fef2f2` | `var(--bg-color--error)` in `:root` |
| **Interactive Accent / Highlight** | `#ba0c2f` | `var(--bg-color--error-dark)` in `:root` |
| **Secondary / Muted Copy** | `#262626` | `var(--color-text)` in `:root` |
| **Structural Hairline Border** | `#003` | `var(--custom-primary-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rich-footer-text-color` | `#454545` | Typography Ink Token |
| `--rich-footer-muted-color` | `rgba(69,69,69,0.7)` | Brand / Palette Token |
| `--rich-footer-inactive-color` | `rgba(69,69,69,0.4)` | Brand / Palette Token |
| `--rich-footer-inactive-color-border` | `#d1d1d1` | Brand / Palette Token |
| `--required-field` | `attr(data-form-field-required)` | Design System Custom Token |
| `--image-ratio-tablet` | `1/1` | Design System Custom Token |
| `--image-ratio-tablet-nc` | `665/370` | Design System Custom Token |
| `--image-ratio-mob` | `1/1` | Design System Custom Token |
| `--image-ratio` | `870/488` | Design System Custom Token |
| `--bg-color--error` | `#fef2f2` | Canvas / Surface Token |
| `--bg-color--error-dark` | `#ba0c2f` | Canvas / Surface Token |
| `--color-text` | `#262626` | Typography Ink Token |
| `--alert-height` | `0px` | Layout / Spatial Grid Token |
| `--menu-height-desktop` | `95px` | Layout / Spatial Grid Token |
| `--menu-height-mobile` | `80px` | Layout / Spatial Grid Token |
| `--partner-header-height` | `81px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.experiencefragment> — `explorajourneys-com_int-en-explora-journal`)**:
   - Landmark `<header class="experiencefragment header-sticky">` hosting `The Explora Journal, A Magazine by E` navigation (`Find a journey · All Destinations · Alaska · Asia · Grand Journeys`), DOM attributes (`data-destex-discover-bound`, `data-description="Scene7DefaultCSS"`, `data-component="ScrollBar"`, `data-namespace="s7classic"`), and stylesheet rule `.cta-dark-btn a { color:fff }`.
2. **Hero Stage & Focal Lead (<section.emag-home-hero> — `Sign In to Your My Explora Account`)**:
   - Landmark `<section class="emag-home-hero emag-home-hero--imageBackground">` presenting display lead `Sign In to Your My Explora Account` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#454545` canvas and `#fef2f2` ink.
3. **Primary Showcase & Content Grid (<section.emag-home-grid> — `The Explora Journal`)**:
   - Landmark `<section class="emag-home-grid">` rendering section `The Explora Journal` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`a0e0fa57lf3jbh6.js`, `gtm.js`, `loader.js`, `5zcb1pbpn89ggc4.js`), and grid rule `.cta-dark-btn { min-width:212.52px;height:47px;text-align:center;letter-spacing:.1em;pad... }`.
4. **Interactive Detail & Feature Matrix (<article.article-card> — `Introducing EXPLORA III`)**:
   - Landmark `<article class="article-card card--small">` framing `Introducing EXPLORA III` and `Out of Office: Jannik Sinner’s Way` (*"Continue without agreeing →"*) with `#fef2f2` surface cards, `#ba0c2f` accents, and `.cta-dark-btn.res--1 { font-size:10px;font-size:.67rem;line-height:15px;line-height:1rem;height... }`.
5. **Colophon & Global Directory Footer (<footer.quotesubject> — `https://explorajourneys.com/int/en/explora-journal`)**:
   - Landmark `<footer class="quotesubject">` anchoring `The Explora Journal, A Magazine ` footer links (`Find a journey · All Destinations · Alaska · Asia · Grand Journeys`), copy *"With your agreement, we and our 9 partners use cookies or si"*, and `#003` structural dividers.
