# UI & UX Architecture: f-list-cleancreatives-org

## Overview & Design Identity
- **Target**: `f-list-cleancreatives-org` (**F-List 2026**)
- **Production URL**: [https://f-list.cleancreatives.org/](https://f-list.cleancreatives.org/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1d1d1d` ink, `#edcc4b` accent)
- **Summary**: Search the F-List 2026 to uncover the 802 advertising and PR agencies behind 1,321 documented fossil fuel contracts worldwide.
- **Total Clean CSS Variables Extracted**: `56` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `roc-grotesk`
- **Body Font Stack**: `roc-grotesk-compressed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: 4.5rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 17px`)
- **Body Copy**: CSS variables `--cmplz_category_body_font_size: 12px`, `--font-longform-paragraph-margin: 2.125rem 0 0 0`; rule `p` (`font-size: 16px`, `line-height: 24px`)
- **Metadata & Labels**: rule `small` (`line-height: 100%`, `font-weight: 300`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--cmplz_banner_background_color)` in `:root` |
| **Primary Typography Ink** | `#f2f2f2` | `var(--cmplz_banner_border_color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1d1d1d` | `var(--cmplz_text_color)` in `:root` |
| **Interactive Accent / Highlight** | `#edcc4b` | `var(--cmplz_button_accept_background_color)` in `:root` |
| **Secondary / Muted Copy** | `#dddddd` | `var(--cmplz_slider_inactive_color)` in `:root` |
| **Structural Hairline Border** | `#FFF` | `var(--fl-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cmplz_banner_width` | `526px` | Layout / Spatial Grid Token |
| `--cmplz_banner_background_color` | `#ffffff` | Canvas / Surface Token |
| `--cmplz_banner_border_color` | `#f2f2f2` | Brand / Palette Token |
| `--cmplz_banner_border_width` | `0px 0px 0px 0px` | Layout / Spatial Grid Token |
| `--cmplz_banner_border_radius` | `0px 0px 0px 0px` | Elevation / Border Token |
| `--cmplz_banner_margin` | `10px` | Layout / Spatial Grid Token |
| `--cmplz_categories-height` | `216px` | Layout / Spatial Grid Token |
| `--cmplz_title_font_size` | `15px` | Typography / Scale Token |
| `--cmplz_text_line_height` | `calc(var(--cmplz_text_font_size) * 1.5)` | Typography Ink Token |
| `--cmplz_text_color` | `#1d1d1d` | Typography Ink Token |
| `--cmplz_hyperlink_color` | `#1d1d1d` | Typography Ink Token |
| `--cmplz_text_font_size` | `12px` | Typography Ink Token |
| `--cmplz_link_font_size` | `12px` | Typography Ink Token |
| `--cmplz_category_body_font_size` | `12px` | Typography / Scale Token |
| `--cmplz_button_accept_background_color` | `#edcc4b` | Canvas / Surface Token |
| `--cmplz_button_accept_border_color` | `#1d1d1d` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.browser-chrome> — `f-list-cleancreatives-org`)**:
   - Landmark `<header class="browser-chrome">` hosting `F-List 2026` navigation (`The report · The F-List · Dirty work · Take Action`), DOM attributes (`data-cmplz="1"`, `data-nosnippet="true"`, `data-prefix="fas"`, `data-icon="times"`), and stylesheet rule `.cmplz-category { width: initial; -webkit-appearance: checkbox; }`.
2. **Hero Stage & Focal Lead (<section.flex> — `The Creative Cover-up`)**:
   - Landmark `<section class="flex hero">` presenting display lead `The Creative Cover-up` and copy excerpt *"Functional Always active"* over `#ffffff` canvas and `#1d1d1d` ink.
3. **Primary Showcase & Content Grid (<section.flex> — `Dirty work. Exposed.`)**:
   - Landmark `<section class="flex call-intro">` rendering section `Dirty work. Exposed.` with copy *"The technical storage or access is strictly necessary for the leg"*, asset references (`xmlrpc.php`, `www.googletagmanager.com`, `flist2026.b-cdn.net`, `embed`), and grid rule `.cmplz-category:checked::before { content: ''; }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `We are exposing`)**:
   - Landmark `<section class="flex redacted">` framing `We are exposing` and `The 2026 picture` (*"The technical storage or access is necessary for the legitimate p"*) with `#1d1d1d` surface cards, `#edcc4b` accents, and `.cmplz-cookiebanner { box-sizing: border-box; }`.
5. **Colophon & Global Directory Footer (<footer.page-template> — `https://f-list.cleancreatives.org/`)**:
   - Landmark `<footer class="page-template">` anchoring `F-List 2026` footer links (`The report · The F-List · Dirty work · Take Action`), copy *"The technical storage or access that is used exclusively for"*, and `#FFF` structural dividers.
