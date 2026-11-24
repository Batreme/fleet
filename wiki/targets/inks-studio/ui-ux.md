---
title: "UI & UX Architecture: inks-studio"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: inks-studio

## Overview & Design Identity
- **Target**: `inks-studio` (**Ink Studio - UI UX Design, CRO & Webflow Development Agency**)
- **Production URL**: [http://inks.studio/](http://inks.studio/)
- **Final Redirected URL**: [https://www.inks.studio/](https://www.inks.studio/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ff` accent)
- **Summary**: Ink Studio is a UI/UX design and CRO agency. We build high-converting Webflow sites, mobile & web apps, and design systems for SaaS and s...
- **Total Clean CSS Variables Extracted**: `446` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Plus Jakarta Sans`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44.8px`, `line-height: 53.76px`, `font-weight: 500`, `letter-spacing: -1.2px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 28.8px`, `line-height: 34.56px`, `font-weight: 500`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffd401` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `:text-blue-600 a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#6b7280` | `var(--cal-text-subtle)` in `:root` |
| **Structural Hairline Border** | `#e8e8e8` | `var(--divider)` in `:root` |
| **Variable Token (`--blue`)** | `#4141f2` | `var(--blue)` in `:root` |
| **Variable Token (`--gray`)** | `#959ba6` | `var(--gray)` in `:root` |
| **Variable Token (`--white-light`)** | `#afafaf` | `var(--white-light)` in `:root` |
| **Variable Token (`--white-tiny`)** | `#f2f9fe` | `var(--white-tiny)` in `:root` |
| **Variable Token (`--dark-light`)** | `#3f3f3f` | `var(--dark-light)` in `:root` |
| **Variable Token (`--gray-bg`)** | `#e9e9e9` | `var(--gray-bg)` in `:root` |
| **Variable Token (`--bg-color`)** | `#0f1115` | `var(--bg-color)` in `:root` |
| **Variable Token (`--bg-blue`)** | `#d5ecf8` | `var(--bg-blue)` in `:root` |
| **Variable Token (`--purple`)** | `#27104e` | `var(--purple)` in `:root` |
| **Variable Token (`--green`)** | `#104e3b` | `var(--green)` in `:root` |
| **Variable Token (`--color`)** | `#ffefed` | `var(--color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#000` | Canvas / Surface Token |
| `--background` | `whitesmoke` | Canvas / Surface Token |
| `--blue` | `#4141f2` | Color / Atmospheric Token |
| `--primary` | `#ffd401` | Brand / Palette Token |
| `--gray` | `#959ba6` | Color / Atmospheric Token |
| `--white-light` | `#afafaf` | Canvas / Surface Token |
| `--white-tiny` | `#f2f9fe` | Canvas / Surface Token |
| `--dark-light` | `#3f3f3f` | Canvas / Surface Token |
| `--gray-bg` | `#e9e9e9` | Canvas / Surface Token |
| `--white` | `white` | Canvas / Surface Token |
| `--bg-color` | `#0f1115` | Canvas / Surface Token |
| `--divider` | `#e8e8e8` | Color / Atmospheric Token |
| `--bg-blue` | `#d5ecf8` | Canvas / Surface Token |
| `--purple` | `#27104e` | Color / Atmospheric Token |
| `--green` | `#104e3b` | Color / Atmospheric Token |
| `--color` | `#ffefed` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.section-hero> — `inks-studio`)**:
   - Landmark `<header class="section-hero">` (`1440x805px`) hosting `Ink Studio - UI UX Design, CRO & Web` navigation (`Home · Work · Webflow · Framer · Astro`), DOM attributes (`data-wf-domain="www.inks.studio"`, `data-wf-page="67375bd348251862372613c7"`, `data-wf-site="67375bd348251862372613c8"`, `data-gtag-id="AW-18125669814"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section-featured-item> — `Level up your SaaS.Turn sign-ups i`)**:
   - Landmark `<section class="section-featured-item">` presenting display lead `Level up your SaaS.Turn sign-ups into paying users.` and copy excerpt *"120+ Satisfied Clients"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section-service> — `Building Impact`)**:
   - Landmark `<section class="section-service">` rendering section `Building Impact` with copy *"We find where your product leaks revenue, redesign the flows that"*, asset references (`cdn.prod.website-files.com`, `inks-studio.webflow.shared.1e5091...`, `inks-studio.webflow.67375bd348251...`, `fonts.googleapis.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-trust> — `Trusted by founders. Built for mea`)**:
   - Landmark `<section class="section-trust">` framing `Trusted by founders. Built for measurable growth.` and `Before & After: How We Transformed These Products` (*"Trusted by 100+ founders"*) with `#ffd401` surface cards, `#0000ff` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `http://inks.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Ink Studio - UI UX Design, CRO &` footer links (`Home · Work · Webflow · Framer · Astro`), copy *"45+ products redesigned"*, and `#e8e8e8` structural dividers.
