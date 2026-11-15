# UI & UX Architecture: inks-studio

## Overview & Design Identity
- **Target**: `inks-studio` (**Ink Studio - UI UX Design, CRO & Webflow Development Agency**)
- **Production URL**: [http://inks.studio/](http://inks.studio/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#f2f9fe` ink, `#959ba6` accent)
- **Summary**: Ink Studio is a UI/UX design and CRO agency. We build high-converting Webflow sites, mobile & web apps, and design systems for SaaS and s...
- **Total Clean CSS Variables Extracted**: `443` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Ibmplexserif`
- **Body Font Stack**: `Instrument Serif`
- **Monospace / Technical Font Stack**: `Ibmplexserif`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-base)!important`, `line-height: var(--tw-leading,var(...`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: var(--text-sm)!important`, `line-height: var(--tw-leading,var(...`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#4141f2` | `var(--blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffd401` | `var(--primary)` in `:root` |
| **Interactive Accent / Highlight** | `#959ba6` | `var(--gray)` in `:root` |
| **Secondary / Muted Copy** | `#afafaf` | `var(--white-light)` in `:root` |
| **Structural Hairline Border** | `#f2f9fe` | `var(--white-tiny)` in `:root` |
| **Variable Token (`--dark-light`)** | `#3f3f3f` | `var(--dark-light)` in `:root` |
| **Variable Token (`--gray-bg`)** | `#e9e9e9` | `var(--gray-bg)` in `:root` |
| **Variable Token (`--bg-color`)** | `#0f1115` | `var(--bg-color)` in `:root` |
| **Variable Token (`--divider`)** | `#e8e8e8` | `var(--divider)` in `:root` |
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
   - Landmark `<header class="section-hero">` hosting `Ink Studio - UI UX Design, CRO & Web` navigation (`Home · Work · Webflow · Framer · Astro`), DOM attributes (`data-wf-domain="www.inks.studio"`, `data-wf-page="67375bd348251862372613c7"`, `data-wf-site="67375bd348251862372613c8"`, `data-gtag-id="AW-18125669814"`), and stylesheet rule `body { color:333;font-family:Manrope,sans-serif;font-size:1rem;line-height:20px }`.
2. **Hero Stage & Focal Lead (<section.section-featured-item> — `Building Impact`)**:
   - Landmark `<section class="section-featured-item">` presenting display lead `Building Impact` and copy excerpt *"at checkout for 30% off any template"* over `#000` canvas and `#f2f9fe` ink.
3. **Primary Showcase & Content Grid (<section.section-service> — `Level up your SaaS.Turn sign-ups i`)**:
   - Landmark `<section class="section-service">` rendering section `Level up your SaaS.Turn sign-ups into paying users.` with copy *"UI & UX Design Services"*, asset references (`cdn.prod.website-files.com`, `inks-studio.webflow.shared.1e5091...`, `inks-studio.webflow.67375bd348251...`, `fonts.googleapis.com`), and grid rule `label { color:var(--black);margin-bottom:5px;font-family:Sourcesanspro;font-weig... }`.
4. **Interactive Detail & Feature Matrix (<section.section-trust> — `Trusted by founders. Built for mea`)**:
   - Landmark `<section class="section-trust">` framing `Trusted by founders. Built for measurable growth.` and `Before & After: How We Transformed These Products` (*"Conversion Strategist"*) with `#ffd401` surface cards, `#959ba6` accents, and `figure { margin-bottom:10px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `http://inks.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Ink Studio - UI UX Design, CRO &` footer links (`Home · Work · Webflow · Framer · Astro`), copy *"Let's Discuss project Let's Discuss project"*, and `#f2f9fe` structural dividers.
