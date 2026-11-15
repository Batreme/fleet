# UI & UX Architecture: cobaltaf-org

## Overview & Design Identity
- **Target**: `cobaltaf-org` (**Cobalt Abortion Fund**)
- **Production URL**: [https://cobaltaf.org/](https://cobaltaf.org/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0047ba` canvas, `#f2f2f2` ink, `#e6d2ee` accent)
- **Summary**: Read privacy and digital security tips here →
- **Total Clean CSS Variables Extracted**: `249` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `bookmania`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `,h1` (`font-size: clamp(2.5658rem,1.4795rem + 5...`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: clamp(2.0273rem,1.4553rem + 2...`, `font-weight: 500`)
- **Body Copy**: rule `p` (`line-height: inherit`)
- **Metadata & Labels**: CSS variables `--container-small: 76rem`, `--label-color: #344054`, `--label-padding: 0px 0px 5px 0px`; rule `,small` (`font-size: clamp(.8rem,.9173rem + -.1422...`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0047ba` | `var(--color-cobalt-blue)` in `:root` |
| **Primary Typography Ink** | `#132048` | `var(--color-navy-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c79fe5` | `var(--color-lavender)` in `:root` |
| **Interactive Accent / Highlight** | `#e6d2ee` | `var(--color-lavender-light)` in `:root` |
| **Secondary / Muted Copy** | `#f86` | `var(--color-chartreuse)` in `:root` |
| **Structural Hairline Border** | `#f2f2f2` | `var(--color-gray)` in `:root` |
| **Variable Token (`--color-white`)** | `#fff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-cobalt-blue` | `#0047ba` | Brand / Palette Token |
| `--color-navy-blue` | `#132048` | Brand / Palette Token |
| `--color-lavender` | `#c79fe5` | Brand / Palette Token |
| `--color-lavender-light` | `#e6d2ee` | Canvas / Surface Token |
| `--color-chartreuse` | `#f86` | Brand / Palette Token |
| `--color-gray` | `#f2f2f2` | Brand / Palette Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--anim-time` | `0.3s` | Motion / Easing Token |
| `--anim-time-long` | `0.6s` | Motion / Easing Token |
| `--anim-ease` | `ease-in` | Motion / Easing Token |
| `--container-fluid` | `100rem` | Layout / Spatial Grid Token |
| `--container` | `83rem` | Layout / Spatial Grid Token |
| `--container-small` | `76rem` | Layout / Spatial Grid Token |
| `--container-padding` | `var(--space-m)` | Layout / Spatial Grid Token |
| `--header-spacing` | `9rem` | Layout / Spatial Grid Token |
| `--font-bookmania` | `"bookmania",serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `cobaltaf-org`)**:
   - Landmark `<header class="header js-header">` hosting `Cobalt Abortion Fund` navigation (`Support · Services · Find A Clinic · Resources · Necesito Apoyo`), DOM attributes (`data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`, `data-acsb-force-visible="true"`, `data-acsb`), and stylesheet rule `.addtoany_content { clear:both;margin:16px auto }`.
2. **Hero Stage & Focal Lead (<section.section> — `Abortion Seekers`)**:
   - Landmark `<section class="section section-1">` presenting display lead `Abortion Seekers` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#0047ba` canvas and `#f2f2f2` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Cobalt Abortion Fund provides dire`)**:
   - Landmark `<section class="section section-2">` rendering section `Cobalt Abortion Fund provides direct financial as...` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`analytics.js`, `gtm.js`, `static.addtoany.com`, `maps.googleapis.com`), and grid rule `.addtoany_header { margin:0 0 16px }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Whatever your reason is for gettin`)**:
   - Landmark `<section class="section section-3">` framing `Whatever your reason is for getting an abortion,...` and `Our Services` (*"Read privacy and digital security tips here →"*) with `#c79fe5` surface cards, `#e6d2ee` accents, and `.addtoany_list { display:inline;line-height:16px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://cobaltaf.org/`)**:
   - Landmark `<footer class="footer">` anchoring `Cobalt Abortion Fund` footer links (`Support · Services · Find A Clinic · Resources · Necesito Apoyo`), copy *"Lea consejos de privacidad y seguridad digital aquí →"*, and `#f2f2f2` structural dividers.
