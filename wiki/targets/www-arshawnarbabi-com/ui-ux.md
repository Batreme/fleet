# UI & UX Architecture: www-arshawnarbabi-com

## Overview & Design Identity
- **Target**: `www-arshawnarbabi-com` (**Arshawn Arbabi, design engineer**)
- **Production URL**: [https://www.arshawnarbabi.com](https://www.arshawnarbabi.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ffe9e6`)
- **Summary**: I design and build custom websites, and the brand behind them if you don't have one yet.
- **Total Clean CSS Variables Extracted**: `379` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `clamp(4.5rem`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `13px`, `10px`, `var(--text-heading-2xl)`, `var(--text-heading-lg)`)
- **Section Heading (`H2`)**: CSS variables `--text-heading-2xl: clamp(2.5rem, 2rem + 2.222vw, 4rem)`, `--leading-heading-2xl: 1.08`, `--tracking-heading-2xl: -.022em`
- **Body Copy**: CSS variables `--text-body-xl: 1.3125rem`, `--leading-body-xl: 1.5`, `--tracking-body-xl: -.008em`
- **Metadata & Labels**: CSS variables `--label-to-input: var(--space-2)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--ink-on)` in `:root` |
| **Primary Typography Ink** | `#fffbfa` | `var(--primary-1)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff2f0` | `var(--primary-2)` in `:root` |
| **Interactive Accent / Highlight** | `#ffe9e6` | `var(--primary-3)` in `:root` |
| **Secondary / Muted Copy** | `#ffdbd7` | `var(--primary-4)` in `:root` |
| **Structural Hairline Border** | `#ffc8c3` | `var(--primary-5)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--photo-travel` | `0px` | Dimension / Scale Token |
| `--ptr-travel` | `var(--parallax-travel-pointer)` | Design System Custom Token |
| `--intro-travel` | `calc(var(--parallax-travel) * 1.5)` | Design System Custom Token |
| `--reveal-r` | `var(--radius-xs)` | Design System Custom Token |
| `--cap-pull` | `var(--space-12)` | Design System Custom Token |
| `--terms-travel` | `0px` | Dimension / Scale Token |
| `--faq-travel` | `0px` | Dimension / Scale Token |
| `--faq-rule` | `var(--neutral-12)` | Design System Custom Token |
| `--faq-row-pad-end` | `var(--space-8)` | Layout / Spatial Grid Token |
| `--faq-sign-size` | `max(32px, var(--text-heading-lg))` | Layout / Spatial Grid Token |
| `--faq-sign-nudge` | `-1px` | Dimension / Scale Token |
| `--closer-rule` | `var(--border-strong)` | Design System Custom Token |
| `--social-icon-size` | `max(24px, calc(var(--text-heading-lg) * .75))` | Layout / Spatial Grid Token |
| `--social-icon-nudge` | `calc(-1 * max(1px, calc(var(--text-heading-lg) * .03125)))` | Dimension / Scale Token |
| `--mark-w` | `96px` | Dimension / Scale Token |
| `--closer-rise` | `.6em` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.SiteNav-module__xVSxrG__nav> — `www-arshawnarbabi-com`)**:
   - Landmark `<nav class="SiteNav-module__xVSxrG__nav">` hosting `Arshawn Arbabi, design engineer` navigation (`Work Work · Process Process`), DOM attributes (`data-theme="dark"`, `data-enter`, `data-instant-reveal`, `data-hero-title`), and stylesheet rule `RouteTransition-module__XvASuW__o... { z-index:9998;pointer-events:none;position:fixed;inset:0 }`.
2. **Hero Stage & Focal Lead (<section.Hero-module__Z8hQ_W__hero> — `Arshawn A r s h a w n Arbabi A r b`)**:
   - Landmark `<section class="Hero-module__Z8hQ_W__hero">` presenting display lead `Arshawn A r s h a w n Arbabi A r b a b i` and copy excerpt *"Arshawn Arbabi Arshawn Arbabi"* over `#fff` canvas and `#ffc8c3` ink.
3. **Primary Showcase & Content Grid (<section.Intro-module__XC4VmG__section> — `What a project includes`)**:
   - Landmark `<section class="Intro-module__XC4VmG__section">` rendering section `What a project includes` with copy *"Start a project Start a project Start a project Start a project"*, asset references (`Manrope-Variable.woff2`, `aura-expanded-vblur.webp`, `3rprz2jei5o6w.css`, `39phslleu3etf.css`), and grid rule `.RouteTransition-module__XvASuW__... { background:var(--neutral-1);will-change:transform;position:absolute;inse... }`.
4. **Interactive Detail & Feature Matrix (<section.RouteTransition-module__XvASuW__top> — `Selected Work`)**:
   - Landmark `<section class="RouteTransition-module__XvASuW__top">` framing `Selected Work` and `Temperance` (*"Start a project Start a project"*) with `#fff2f0` surface cards, `#ffe9e6` accents, and `.RouteTransition-module__XvASuW__top { height:calc(50% + 1px);inset-block-start:0 }`.
5. **Colophon & Global Directory Footer (<footer.SiteNav-module__xVSxrG__nav> — `https://www.arshawnarbabi.com`)**:
   - Landmark `<footer class="SiteNav-module__xVSxrG__nav">` anchoring `Arshawn Arbabi, design engineer` footer links (`Work Work · Process Process`), copy *"Arshawn A r s h a w n"*, and `#ffc8c3` structural dividers.
