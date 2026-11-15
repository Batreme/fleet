# UI & UX Architecture: bettr-academy

## Overview & Design Identity
- **Target**: `bettr-academy` (**Bettr Academy · World-Class Barista & Coffee Training**)
- **Production URL**: [https://bettr.academy/](https://bettr.academy/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0c0c0c` ink, `#fcbf27` accent)
- **Summary**: Bettr Academy offers SCA-certified and WSQ-accredited coffee courses in Singapore — real, hands-on training with up to 70% SkillsFuture f...
- **Total Clean CSS Variables Extracted**: `104` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jobclarendon`
- **Body Font Stack**: `Agipo Condensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 5.25rem`, `line-height: 1`, `font-weight: 600`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 3.75rem`, `line-height: 1.1`, `font-weight: 600`)
- **Body Copy**: CSS variables `--_typography---font-styles--body: Roboto, sans-serif`; rule `body` (`font-size: 1rem`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--_ui-styles---radius--small: .25rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--_primitives---colors--white)` in `:root` |
| **Primary Typography Ink** | `#0c0c0c` | `var(--_primitives---colors--neutral-darkest)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff3` | `var(--_primitives---opacity--white-20)` in `:root` |
| **Interactive Accent / Highlight** | `#fcbf27` | `var(--_primitives---colors--sunshine)` in `:root` |
| **Secondary / Muted Copy** | `#2c1c0f` | `var(--_primitives---colors--coffee)` in `:root` |
| **Structural Hairline Border** | `#f7f4ed` | `var(--_primitives---colors--cream)` in `:root` |
| **Variable Token (`--_primitives---opacity--neutral-darkest-5`)** | `#0c0c0c0d` | `var(--_primitives---opacity--neutral-darkest-5)` in `:root` |
| **Variable Token (`--_primitives---opacity--neutral-darkest-15`)** | `#0c0c0c26` | `var(--_primitives---opacity--neutral-darkest-15)` in `:root` |
| **Variable Token (`--_primitives---opacity--white-10`)** | `#ffffff1a` | `var(--_primitives---opacity--white-10)` in `:root` |
| **Variable Token (`--_primitives---colors--earth`)** | `#ed612f` | `var(--_primitives---colors--earth)` in `:root` |
| **Variable Token (`--_primitives---colors--latte`)** | `#edd5b7` | `var(--_primitives---colors--latte)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-scheme-1--background` | `var(--_primitives---colors--cream)` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `Roboto, sans-serif` | Typography / Scale Token |
| `--color-scheme-1--text` | `var(--_primitives---colors--coffee)` | Typography Ink Token |
| `--_typography---font-styles--heading` | `Jobclarendon, Arial, sans-serif` | Typography Ink Token |
| `--_primitives---colors--white` | `#fff` | Canvas / Surface Token |
| `--_primitives---opacity--transparent` | `transparent` | Design System Custom Token |
| `--_primitives---opacity--neutral-darkest-5` | `#0c0c0c0d` | Canvas / Surface Token |
| `--_primitives---opacity--neutral-darkest-15` | `#0c0c0c26` | Canvas / Surface Token |
| `--_primitives---colors--neutral-darkest` | `#0c0c0c` | Canvas / Surface Token |
| `--_primitives---opacity--white-10` | `#ffffff1a` | Canvas / Surface Token |
| `--_primitives---opacity--white-20` | `#fff3` | Canvas / Surface Token |
| `--_primitives---colors--sunshine` | `#fcbf27` | Brand / Palette Token |
| `--_primitives---colors--coffee` | `#2c1c0f` | Brand / Palette Token |
| `--_primitives---colors--cream` | `#f7f4ed` | Brand / Palette Token |
| `--_primitives---colors--earth` | `#ed612f` | Brand / Palette Token |
| `--_primitives---colors--latte` | `#edd5b7` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.section_header> — `bettr-academy`)**:
   - Landmark `<header class="section_header">` hosting `Bettr Academy · World-Class Barista ` navigation (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), DOM attributes (`data-wf-domain="bettr.academy"`, `data-wf-page="69f15930f71b5763616e2c5d"`, `data-wf-site="69f15930f71b5763616e2c5c"`, `data-barba="wrapper"`), and stylesheet rule `ul { margin-top: 1rem; margin-bottom: 1rem; padding-left: 1.25rem; }`.
2. **Hero Stage & Focal Lead (<section.notice-banner_component> — `B e t t r C o f f e e . B e t t r `)**:
   - Landmark `<section class="notice-banner_component">` presenting display lead `B e t t r C o f f e e . B e t t r W o r l d .` and copy excerpt *"Hospitality Skills"* over `#fff` canvas and `#0c0c0c` ink.
3. **Primary Showcase & Content Grid (<section.section_journey> — `Where Does Your Bettr Journey Begi`)**:
   - Landmark `<section class="section_journey color-scheme-4">` rendering section `Where Does Your Bettr Journey Begin?` with copy *"SkillsFuture Career Transition Programme"*, asset references (`cdn.prod.website-files.com`, `bettr-academy.webflow.shared.25d4...`, `bettr-academy.webflow.69f15930f71...`, `fonts.googleapis.com`), and grid rule `ol { margin-top: 1rem; margin-bottom: 1rem; padding-left: 1.5rem; }`.
4. **Interactive Detail & Feature Matrix (<section.section_rotating-words-banner> — `Yourself`)**:
   - Landmark `<section class="section_rotating-words-banner color-scheme-2">` framing `Yourself` and `Your Team` (*"Workshops & Experiences"*) with `#fff3` surface cards, `#fcbf27` accents, and `li { margin-top: .25rem; margin-bottom: .25rem; padding-left: .5rem; }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://bettr.academy/`)**:
   - Landmark `<footer class="footer_component color-scheme-3">` anchoring `Bettr Academy · World-Class Bari` footer links (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), copy *"Corporate Training"*, and `#f7f4ed` structural dividers.
