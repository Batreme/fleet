# UI & UX Architecture: familyservicelincoln-org

## Overview & Design Identity
- **Target**: `familyservicelincoln-org` (**Family Service Lincoln: Everyone Deserves the Chance to Thrive**)
- **Production URL**: [https://familyservicelincoln.org](https://familyservicelincoln.org)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#1b1f2a` canvas, `#ffffff` ink, `#ffc145` accent)
- **Summary**: For over 135 years, we have adapted to meet the needs of families, serving as Lincoln's first charitable organization.
- **Total Clean CSS Variables Extracted**: `39` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Google Sans`
- **Body Font Stack**: `Libre Caslon Text`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 3rem`, `line-height: 1`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(32px,5vw,70px)`, `line-height: 1.17`, `letter-spacing: -1.4px`, `font-weight: 400`)
- **Body Copy**: rule `,p` (`font-size: 1rem`, `line-height: 1.5rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `15px`, `13px`, `16px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1b1f2a` | `var(--gmcc-bg)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--gmcc-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a7b0bd` | `var(--gmcc-text-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#ffc145` | `var(--gmcc-accent)` in `:root` |
| **Secondary / Muted Copy** | `#15171c` | `var(--gmcc-accent-text)` in `:root` |
| **Structural Hairline Border** | `#ffd37a` | `var(--gmcc-accent-hover)` in `:root` |
| **Variable Token (`--gmcc-link`)** | `#7cc6ff` | `var(--gmcc-link)` in `:root` |
| **Variable Token (`--gmcc-focus`)** | `#3b82f6` | `var(--gmcc-focus)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gmcc-bg` | `#1b1f2a` | Canvas / Surface Token |
| `--gmcc-text` | `#ffffff` | Typography Ink Token |
| `--gmcc-text-muted` | `#a7b0bd` | Typography Ink Token |
| `--gmcc-accent` | `#ffc145` | Brand / Palette Token |
| `--gmcc-accent-text` | `#15171c` | Typography Ink Token |
| `--gmcc-accent-hover` | `#ffd37a` | Brand / Palette Token |
| `--gmcc-link` | `#7cc6ff` | Typography Ink Token |
| `--gmcc-focus` | `#3b82f6` | Color / Atmospheric Token |
| `--gmcc-radius` | `16px` | Elevation / Border Token |
| `--gmcc-font` | `inherit` | Typography / Scale Token |
| `--header-height` | `88px` | Layout / Spatial Grid Token |
| `--admin-bar-height` | `32px` | Layout / Spatial Grid Token |
| `--gform-theme-control-shadow` | `none` | Brand / Palette Token |
| `--gform-theme-control-size` | `auto` | Brand / Palette Token |
| `--gform-theme-control-checked-shadow` | `none` | Brand / Palette Token |
| `--gform-theme-control-checkbox-checked-shadow` | `none` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `familyservicelincoln-org`)**:
   - Landmark `<header class="fixed top-0">` hosting `Family Service Lincoln: Everyone Des` navigation (`About Us · Leadership Team · Annual Report · Strategic Plan · Form 990`), DOM attributes (`data-cbid="1670e8a1-465b-4331-ab..."`, `data-blockingmode="manual"`, `data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`), and stylesheet rule `.gm-cc { padding: 0 2% 1.25rem; }`.
2. **Hero Stage & Focal Lead (<section.module-hero> — `Everyone Deserves the Chance to Th`)**:
   - Landmark `<section class="module-hero full">` presenting display lead `Everyone Deserves the Chance to Thrive` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#1b1f2a` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.module-program_tabs> — `Serving Thousands of Households An`)**:
   - Landmark `<section class="module-program_tabs full">` rendering section `Serving Thousands of Households Annually` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`widgetIcon.min.js`, `state.js`, `logconsent.ashx`, `cc.js`), and grid rule `.gm-cc.is-visible { transform: none; opacity: 1; }`.
4. **Interactive Detail & Feature Matrix (<section.module-impact_stats> — `Together, Our Efforts Make a Measu`)**:
   - Landmark `<section class="module-impact_stats full">` framing `Together, Our Efforts Make a Measurable Difference` and `Strong Families Build Strong Communities` (*"Skip to main content"*) with `#a7b0bd` surface cards, `#ffc145` accents, and `.gm-cc__card { padding: 1.75rem 2rem; }`.
5. **Colophon & Global Directory Footer (<footer.full> — `https://familyservicelincoln.org`)**:
   - Landmark `<footer class="full relative">` anchoring `Family Service Lincoln: Everyone` footer links (`About Us · Leadership Team · Annual Report · Strategic Plan · Form 990`), copy *"The FiftyOne Commons STEAM Activity Center is now available "*, and `#ffd37a` structural dividers.
