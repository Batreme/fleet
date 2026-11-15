# UI & UX Architecture: 21oaks-org

## Overview & Design Identity
- **Target**: `21oaks-org` (**21Oaks Student Apartments • USC & Williams-Brice**)
- **Production URL**: [https://21oaks.org/](https://21oaks.org/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#292929` canvas, `#ff0` ink, `#000` accent)
- **Summary**: Freshly renovated student apartments minutes from Williams-Brice and USC. Modern living with pool, study spaces, and everything within re...
- **Total Clean CSS Variables Extracted**: `9` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Exposure`
- **Body Font Stack**: `Exposure Italic`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#292929` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#e8ceff` | `var(--primary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `a { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#000` | `mark { color: #000 }` |
| **Secondary / Muted Copy** | `#ff0` | `mark { background: #ff0 }` |
| **Structural Hairline Border** | `#333` | `body { color: #333 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `white` | Canvas / Surface Token |
| `--black` | `#292929` | Canvas / Surface Token |
| `--primary` | `#e8ceff` | Brand / Palette Token |
| `--icon` | `40px` | Dimension / Scale Token |
| `--shift-gap` | `0.25em` | Layout / Spatial Grid Token |
| `--dur` | `650ms` | Motion / Timing Token |
| `--ease` | `cubic-bezier(0.83, 0, 0.17, 1)` | Motion / Easing Token |
| `--scribble-line-color` | `#e8ceff` | Brand / Palette Token |
| `--ring-size` | `0.1em` | Layout / Spatial Grid Token |
| `--21oaks-org-bg` | `#292929` | Canvas Substrate (from `var(--black)` in `:root`) |
| `--21oaks-org-ink` | `#ff0` | Primary Typography Ink (stylesheet-derived) |
| `--21oaks-org-surface` | `#0000` | Surface Substrate (stylesheet-derived) |
| `--21oaks-org-accent` | `#000` | Interactive Accent (stylesheet-derived) |
| `--21oaks-org-muted` | `#ff0` | Secondary Ink (stylesheet-derived) |
| `--21oaks-org-border` | `#333` | Structural Border (stylesheet-derived) |
| `--21oaks-org-container` | `940px` | Container Bound (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `21oaks-org`)**:
   - Landmark `<header class="header">` hosting `21Oaks Student Apartments • USC & Wi` navigation (`21Oaks · Home · Apartments · Amenities · Location`), DOM attributes (`data-wf-domain="21oaks.org"`, `data-wf-page="6a31483f3822b51654193a43"`, `data-wf-site="6a31483f3822b51654193a68"`, `data-appearance="horizontal"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Live better, closer to USC`)**:
   - Landmark `<section class="hero">` presenting display lead `Live better, closer to USC` and copy excerpt *"He sido nominado como submission.awardCategory.nameHonors en Awww"* over `#292929` canvas and `#ff0` ink.
3. **Primary Showcase & Content Grid (<section.dynamic_section> — `Everything student living should b`)**:
   - Landmark `<section class="dynamic_section">` rendering section `Everything student living should be` with copy *"Designed to recharge"*, asset references (`cdn.prod.website-files.com`, `21oakswebsite.webflow.shared.1884...`, `6a31483f3822b51654193afd_favicon.png`, `69fb54ec6fea40c496e176b6_favicon.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.sides> — `Made for everyday living`)**:
   - Landmark `<section class="sides">` framing `Made for everyday living` and `Where student life feels balanced` (*"Comfort in every corner"*) with `#0000` surface cards, `#000` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://21oaks.org/`)**:
   - Landmark `<footer class="footer">` anchoring `21Oaks Student Apartments • USC ` footer links (`21Oaks · Home · Apartments · Amenities · Location`), copy *"Little details matter"*, and `#333` structural dividers.
