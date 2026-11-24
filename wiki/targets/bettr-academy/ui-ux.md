---
title: "UI & UX Architecture: bettr-academy"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: bettr-academy

## Overview & Design Identity
- **Target**: `bettr-academy` (**Bettr Academy · World-Class Barista & Coffee Training**)
- **Production URL**: [https://bettr.academy/](https://bettr.academy/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f4ed` canvas, `#2c1c0f` ink, `#0082f3` accent)
- **Summary**: Bettr Academy offers SCA-certified and WSQ-accredited coffee courses in Singapore — real, hands-on training with up to 70% SkillsFuture f...
- **Total Clean CSS Variables Extracted**: `104` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jobclarendon`
- **Body Font Stack**: `Roboto`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 154.977px`, `line-height: 185.972px`, `font-weight: 600`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 84px`, `line-height: 84px`, `font-weight: 600`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---font-styles--body: Roboto, sans-serif`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_ui-styles---radius--small: .25rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f4ed` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#2c1c0f` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fcbf27` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#fcbf27` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--_primitives---colors--white`)** | `#ffffff` | `var(--_primitives---colors--white)` in `:root` |
| **Variable Token (`--_primitives---opacity--neutral-darkest-5`)** | `#0c0c0c` | `var(--_primitives---opacity--neutral-darkest-5)` in `:root` |
| **Variable Token (`--_primitives---opacity--white-20`)** | `#fff3` | `var(--_primitives---opacity--white-20)` in `:root` |
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
   - Landmark `<header class="section_header">` (`1440x855px`) hosting `Bettr Academy · World-Class Barista ` navigation (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), DOM attributes (`data-wf-domain="bettr.academy"`, `data-wf-page="69f15930f71b5763616e2c5d"`, `data-wf-site="69f15930f71b5763616e2c5c"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.notice-banner_component> — `Bettr Coffee. Bettr World.`)**:
   - Landmark `<section class="notice-banner_component">` presenting display lead `Bettr Coffee. Bettr World.` and copy excerpt *"WORLD-CLASS COFFEE EDUCATION"* over `#f7f4ed` canvas and `#2c1c0f` ink.
3. **Primary Showcase & Content Grid (<section.section_journey> — `B e t t r C o f f e e . B e t t r `)**:
   - Landmark `<section class="section_journey color-scheme-4">` rendering section `B e t t r C o f f e e . B e t t r W o r l d .` with copy *"WORLD-CLASS COfFEE EDUCATION"*, asset references (`cdn.prod.website-files.com`, `bettr-academy.webflow.shared.25d4...`, `bettr-academy.webflow.69f15930f71...`, `fonts.googleapis.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section_rotating-words-banner> — `Where Does Your Bettr Journey Begi`)**:
   - Landmark `<section class="section_rotating-words-banner color-scheme-2">` framing `Where Does Your Bettr Journey Begin?` and `Your Coffee Career, Curated.` (*"Stop just making coffee, start building a career. Gain the SCA cr"*) with `#fcbf27` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://bettr.academy/`)**:
   - Landmark `<footer class="footer_component color-scheme-3">` anchoring `Bettr Academy · World-Class Bari` footer links (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), copy *"Build team skills and foster professional development. Coffe"*, and `#e2e2e2` structural dividers.
