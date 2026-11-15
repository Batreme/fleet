# UI & UX Architecture: www-iamsunnywang-com

## Overview & Design Identity
- **Target**: `www-iamsunnywang-com` (**Sunny's Journey**)
- **Production URL**: [http://www.iamsunnywang.com/](http://www.iamsunnywang.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#62d6dc` / `#fffdfc`)
- **Summary**: A résumé you can walk through: Sunny Wang's design career, from Beijing to Pittsburgh to Silicon Valley, rebuilt as hand-crafted worlds y...
- **Total Clean CSS Variables Extracted**: `191` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Barlow Condensed`
- **Body Font Stack**: `Cormorant Infant`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(36px,7vw,80px)`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -.025em`)
- **Body Copy**: CSS variables `--airbnb-section-body-size-value: 1.9`, `--mpc-body: rgba(23,63,70,.7)`, `--hover-card-body: rgba(74,60,45,.8)`; rule `p` (`font-size: clamp(15px, 1.55vw, 20px)`, `line-height: 1.34`, `letter-spacing: 0`, `font-weight: 300`)
- **Metadata & Labels**: CSS variables `--mono: "IBM Plex Mono", ui-monospace, monospace`; rule `small` (`letter-spacing: .06em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#62d6dc` | `var(--text-highlight-color)` in `:root` |
| **Primary Typography Ink** | `#321f25` | `var(--guest-story-ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d94b55` | `var(--guest-story-red)` in `:root` |
| **Interactive Accent / Highlight** | `#fffdfc` | `var(--guest-story-paper)` in `:root` |
| **Secondary / Muted Copy** | `#17202a` | `var(--billboard-ink)` in `:root` |
| **Structural Hairline Border** | `#78838f` | `var(--billboard-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--case-iframe-radius` | `22px` | Elevation / Border Token |
| `--title-font` | `"Quicksand",var(--body-font)` | Typography / Scale Token |
| `--kicker-font` | `"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace` | Typography / Scale Token |
| `--text-highlight-color` | `#62d6dc` | Canvas / Surface Token |
| `--google-text-highlight-color` | `#62d6dc` | Canvas / Surface Token |
| `--airbnb-section-kicker-size-value` | `1.4` | Layout / Spatial Grid Token |
| `--airbnb-section-title-size-value` | `4.9` | Layout / Spatial Grid Token |
| `--airbnb-section-body-size-value` | `1.9` | Layout / Spatial Grid Token |
| `--portfolio-rail` | `clamp(40px, 5vw, 62px)` | Dimension / Scale Token |
| `--portfolio-offset` | `clamp(106px, 12vw, 154px)` | Dimension / Scale Token |
| `--portfolio-dot-top` | `50%` | Dimension / Scale Token |
| `--portfolio-hover-image-scale` | `1.24` | Design System Custom Token |
| `--poster-slider-height` | `clamp(320px, 36cqw, 520px)` | Layout / Spatial Grid Token |
| `--poster-slider-peek` | `clamp(24px, 3.2cqw, 46px)` | Dimension / Scale Token |
| `--poster-slider-fade-width` | `clamp(56px, 6cqw, 96px)` | Layout / Spatial Grid Token |
| `--portfolio-lightbox-top` | `clamp(64px, 8vh, 96px)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.journey-header> — `www-iamsunnywang-com`)**:
   - Landmark `<header class="journey-header">` hosting `Sunny's Journey` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scene-skin="default"`, `data-storymode-i18n="rotateTitle"`, `data-storymode-i18n="rotateBody"`, `data-i18n-aria="restart"`), and stylesheet rule `.split-panel-host .case-media-iframe { display:block;width:100%;height:100%;border:0;border-radius:inherit;back... }`.
2. **Hero Stage & Focal Lead (<section.ios-fallback> — `Sunny's Journey Original Sound Tra`)**:
   - Landmark `<section class="ios-fallback">` presenting display lead `Sunny's Journey Original Sound Tracks` and copy excerpt *"Skip to the journey"* over `#62d6dc` canvas and `#17202a` ink.
3. **Primary Showcase & Content Grid (<section.journey-stage> — `Collected skills`)**:
   - Landmark `<section class="journey-stage">` rendering section `Collected skills` with copy *"Please visit on desktop"*, asset references (`favicon.svg`, `storymode-analytics.js`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `panel-host .case-media-open-corne... { width:1.25em;height:1.25em;fill:none;stroke:currentColor;stroke-width:1.... }`.
4. **Interactive Detail & Feature Matrix (<section.reflection-playlist> — `A small door before the PDF`)**:
   - Landmark `<section class="reflection-playlist">` framing `A small door before the PDF` and `Prologue · The water forest` (*"Prologue · The water forest"*) with `#d94b55` surface cards, `#fffdfc` accents, and `.split-panel-host .ai-ip-video-vi... { display:flex;align-items:center;justify-content:center;width:100%;height... }`.
5. **Colophon & Global Directory Footer (<footer.ios-fallback__message> — `http://www.iamsunnywang.com/`)**:
   - Landmark `<footer class="ios-fallback__message">` anchoring `Sunny's Journey` footer links (`Overview · Index · Archive · About · Contact`), copy *"Assembling the little world…"*, and `#78838f` structural dividers.
