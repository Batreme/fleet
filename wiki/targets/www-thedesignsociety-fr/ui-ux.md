# UI & UX Architecture: www-thedesignsociety-fr

## Overview & Design Identity
- **Target**: `www-thedesignsociety-fr` (**The Design Society Lyon — la communauté des designers**)
- **Production URL**: [https://www.thedesignsociety.fr/](https://www.thedesignsociety.fr/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ebedf5` canvas, `#1e1e1e` ink, `#bcf015` accent)
- **Summary**: L'association qui réunit les designers de Lyon autour de talks et d'apéros. Une société secrète si mal gardée qu'on a fait un site. Proch...
- **Total Clean CSS Variables Extracted**: `60` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Fkrasterromancompact Smooth`
- **Body Font Stack**: `Geistpixel Line`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ebedf5` | `var(--background)` in `:root` |
| **Primary Typography Ink** | `#f0f0f0` | `var(--blue--content)` in `:root` |
| **Elevated Surface / Card Substrate** | `#350aff` | `var(--brand-color-2)` in `:root` |
| **Interactive Accent / Highlight** | `#bcf015` | `var(--brand-color-1)` in `:root` |
| **Secondary / Muted Copy** | `#1e1e1e` | `var(--content)` in `:root` |
| **Structural Hairline Border** | `#f7f7f7` | `var(--background-subtle)` in `:root` |
| **Variable Token (`--border`)** | `#1d1d1d26` | `var(--border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#ebedf5` | Canvas / Surface Token |
| `--_theme---content` | `var(--content)` | Brand / Palette Token |
| `--radius--radius-s` | `4px` | Elevation / Border Token |
| `--border` | `#1d1d1d26` | Elevation / Border Token |
| `--radius--radius-m` | `6px` | Elevation / Border Token |
| `--_theme---background-accent` | `var(--background-accent)` | Canvas / Surface Token |
| `--_theme---brand-color-2` | `var(--brand-color-2)` | Brand / Palette Token |
| `--_responsive---hero--padding-top` | `10em` | Layout / Spatial Grid Token |
| `--blue--content` | `#f0f0f0` | Color / Atmospheric Token |
| `--_responsive---hero--title-marquee` | `10em` | Dimension / Scale Token |
| `--brand-color-2` | `#350aff` | Brand / Palette Token |
| `--brand-color-1` | `#bcf015` | Brand / Palette Token |
| `--_responsive---hero--eye` | `150px` | Dimension / Scale Token |
| `--_responsive---hero--margin` | `var(--size--m)` | Layout / Spatial Grid Token |
| `--_theme---border` | `var(--border)` | Brand / Palette Token |
| `--_theme---content-subtle` | `var(--content-subtle)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.twostep-nav> — `www-thedesignsociety-fr`)**:
   - Landmark `<nav class="twostep-nav">` hosting `The Design Society Lyon — la communa` navigation (`A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`), DOM attributes (`data-wf-domain="www.thedesignsociety.fr"`, `data-wf-page="698de82380130d2fe9cadaf6"`, `data-wf-site="698de82080130d2fe9cada54"`, `data-barba="wrapper"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.mwg020> — `The Design Society — La société se`)**:
   - Landmark `<section class="mwg020">` presenting display lead `The Design Society — La société secrète la moins...` and copy excerpt *"É v è n e m e n t s"* over `#ebedf5` canvas and `#1e1e1e` ink.
3. **Primary Showcase & Content Grid (<section.mwg005> — `É v è n e m e n t s`)**:
   - Landmark `<section class="mwg005">` rendering section `É v è n e m e n t s` with copy *"E v e n t b r i t e"*, asset references (`cdn.prod.website-files.com`, `the-design-society-22535e.webflow...`, `6a96a56caf2dbc50ad13753b_webclip.png`, `6a96a56c5cc7207fcb2e955c_webclip.png`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.section-6> — `E v e n t b r i t e`)**:
   - Landmark `<section class="section-6">` framing `E v e n t b r i t e` and `A c c è s p r e s q u e r e s t r e i n t` (*"A c c è s p r e s q u e r e s t r e i n t"*) with `#350aff` surface cards, `#bcf015` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.thedesignsociety.fr/`)**:
   - Landmark `<footer class="footer">` anchoring `The Design Society Lyon — la com` footer links (`A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`), copy *"A n o n y m a t r e l a t i f"*, and `#f7f7f7` structural dividers.
