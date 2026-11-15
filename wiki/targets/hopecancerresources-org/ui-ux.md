# UI & UX Architecture: hopecancerresources-org

## Overview & Design Identity
- **Target**: `hopecancerresources-org` (**Hope Cancer Resources - Support. Educate. Prevent.**)
- **Production URL**: [https://hopecancerresources.org/](https://hopecancerresources.org/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0e1829` canvas, `#edf1f4` ink, `#476577` accent)
- **Summary**: Providing free cancer support services through counseling, transportation, financial assistance, personal training, tobacco treatment, &...
- **Total Clean CSS Variables Extracted**: `20` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `BrandonText`
- **Body Font Stack**: `SourceSans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2rem`, `line-height: 1`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.6rem,5vw,3rem)`, `font-weight: 900`)
- **Body Copy**: CSS variables `--color-brand-text-base: var(--color-brand-black)`; rule `p` (`font-size: 2rem`, `line-height: 1.5`, `font-weight: 400`)
- **Metadata & Labels**: rule `.label` (`font-size: 1rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0e1829` | `var(--color-brand-black)` in `:root` |
| **Primary Typography Ink** | `#1b7aaf` | `var(--color-brand-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1fa0e5` | `var(--color-brand-lightblue)` in `:root` |
| **Interactive Accent / Highlight** | `#476577` | `var(--color-brand-darkblue)` in `:root` |
| **Secondary / Muted Copy** | `#90a3bf` | `var(--color-brand-gray-500)` in `:root` |
| **Structural Hairline Border** | `#edf1f4` | `var(--color-lightest-gray)` in `:root` |
| **Variable Token (`--color-notice-warning`)** | `#dc4b4b` | `var(--color-notice-warning)` in `:root` |
| **Variable Token (`--color-notice-success`)** | `#2DB292` | `var(--color-notice-success)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-primary` | `"BrandonText", Arial, Helvetica, sans-serif` | Brand / Palette Token |
| `--font-heading` | `"BrandonText", Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--font-base` | `"SourceSans", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-serif` | `"EightiesComebackIt", "Times New Roman", "Garamond", serif` | Typography / Scale Token |
| `--color-brand-black` | `#0e1829` | Canvas / Surface Token |
| `--color-brand-blue` | `#1b7aaf` | Brand / Palette Token |
| `--color-brand-lightblue` | `#1fa0e5` | Canvas / Surface Token |
| `--color-brand-darkblue` | `#476577` | Canvas / Surface Token |
| `--color-brand-gray-500` | `#90a3bf` | Brand / Palette Token |
| `--color-light-gray` | `#476577` | Canvas / Surface Token |
| `--color-lightest-gray` | `#edf1f4` | Canvas / Surface Token |
| `--color-notice-warning` | `#dc4b4b` | Brand / Palette Token |
| `--color-notice-success` | `#2DB292` | Brand / Palette Token |
| `--color-primary` | `var(--color-brand-black)` | Brand / Palette Token |
| `--color-secondary` | `var(--color-brand-black)` | Brand / Palette Token |
| `--color-brand-text-base` | `var(--color-brand-black)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `hopecancerresources-org`)**:
   - Landmark `<header class="site-header template-home">` hosting `Hope Cancer Resources - Support. Edu` navigation (`Shop for Hope · About Hope · Our Story · Our Foundation · Staff`), DOM attributes (`data-template="base.twig"`), and stylesheet rule `content { background:fff;background-size:100% }`.
2. **Hero Stage & Focal Lead (<article.post-type-page> — `Support. Educate. Prevent.`)**:
   - Landmark `<article class="post-type-page">` presenting display lead `Support. Educate. Prevent.` and copy excerpt *"Skip to main content"* over `#0e1829` canvas and `#edf1f4` ink.
3. **Primary Showcase & Content Grid (<section.page_heading> — `Driving real Change in Northwest A`)**:
   - Landmark `<section class="page_heading section-block">` rendering section `Driving real Change in Northwest Arkansas (2025 R...` with copy *"About Back to About Hope Unscripted Podcast About Hope Our Story "*, asset references (`gtm.js`, `style.css`, `humans.txt`, `xmlrpc.php`), and grid rule `ge-template-wp-content .default-h... { padding-top:100px }`.
4. **Interactive Detail & Feature Matrix (<section.stats_block_one> — `At Hope Cancer Resources, we walk `)**:
   - Landmark `<section class="stats_block_one section-block">` framing `At Hope Cancer Resources, we walk beside those fa...` and `Ways We Help` (*"Hope Unscripted Podcast"*) with `#1fa0e5` surface cards, `#476577` accents, and `projects-template-default .post-h... { padding-top:80px }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://hopecancerresources.org/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Hope Cancer Resources - Support.` footer links (`Shop for Hope · About Hope · Our Story · Our Foundation · Staff`), copy *"Board of Directors"*, and `#edf1f4` structural dividers.
