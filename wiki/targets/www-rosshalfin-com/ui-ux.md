# UI & UX Architecture: www-rosshalfin-com

## Overview & Design Identity
- **Target**: `www-rosshalfin-com` (**Ross Halfin Photography · Music Images + Fine Art Prints**)
- **Production URL**: [https://www.rosshalfin.com](https://www.rosshalfin.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#161618` ink, `#161618` accent)
- **Summary**: Unparalleled music photography by Ross Halfin - Limited edition Fine-Art prints, signed & embossed. Worldwide shipping
- **Total Clean CSS Variables Extracted**: `68` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Barlow Semi Condensed`
- **Body Font Stack**: `Barlow`
- **Monospace / Technical Font Stack**: `IBM Plex Sans`
- **Hero Display (`H1`)**: rule `.title` (`font-size: large`, `font-weight: bold`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.375rem,.9939rem + 1.2...`, `letter-spacing: -.01em`)
- **Body Copy**: CSS variables `--cmplz_category_body_font_size: 12px`, `--wp--custom--line-height--body: 1.618`; rule `p` (`font-size: 12px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `14px`, `11px`, `12px`, `13px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--cmplz_banner_background_color)` in `:root` |
| **Primary Typography Ink** | `#f2f2f2` | `var(--cmplz_banner_border_color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#222222` | `var(--cmplz_text_color)` in `:root` |
| **Interactive Accent / Highlight** | `#161618` | `var(--cmplz_hyperlink_color)` in `:root` |
| **Secondary / Muted Copy** | `#f9f9f9` | `var(--cmplz_button_deny_background_color)` in `:root` |
| **Structural Hairline Border** | `#333333` | `var(--cmplz_button_settings_text_color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cmplz_banner_width` | `490px` | Layout / Spatial Grid Token |
| `--cmplz_banner_background_color` | `#ffffff` | Canvas / Surface Token |
| `--cmplz_banner_border_color` | `#f2f2f2` | Brand / Palette Token |
| `--cmplz_banner_border_width` | `0px 0px 0px 0px` | Layout / Spatial Grid Token |
| `--cmplz_banner_border_radius` | `15px 15px 15px 15px` | Elevation / Border Token |
| `--cmplz_banner_margin` | `10px` | Layout / Spatial Grid Token |
| `--cmplz_categories-height` | `216px` | Layout / Spatial Grid Token |
| `--cmplz_title_font_size` | `15px` | Typography / Scale Token |
| `--cmplz_text_line_height` | `calc(var(--cmplz_text_font_size) * 1.5)` | Typography Ink Token |
| `--cmplz_text_color` | `#222222` | Typography Ink Token |
| `--cmplz_hyperlink_color` | `#161618` | Typography Ink Token |
| `--cmplz_text_font_size` | `12px` | Typography Ink Token |
| `--cmplz_link_font_size` | `12px` | Typography Ink Token |
| `--cmplz_category_body_font_size` | `12px` | Typography / Scale Token |
| `--cmplz_button_accept_background_color` | `#161618` | Canvas / Surface Token |
| `--cmplz_button_accept_border_color` | `#161618` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-rosshalfin-com`)**:
   - Landmark `<header class="site-header">` hosting `Ross Halfin Photography · Music Imag` navigation (`€ 0.00 0`), DOM attributes (`data-partner-attribution-id="PaymentPlugins_PCP"`, `data-uid-auto="uid_znuqasiucahxrfuik..."`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `body .is-layout-constrained>.alig... { max-width:var(--wp--style--global--wide-size) }`.
2. **Hero Stage & Focal Lead (<section.pageSection> — `Welcome To Ross Halfin Photography`)**:
   - Landmark `<section class="pageSection home__sec__hl">` presenting display lead `Welcome To Ross Halfin Photography` and copy excerpt *"We use cookies to improve site performance and functionality. You"* over `#ffffff` canvas and `#161618` ink.
3. **Primary Showcase & Content Grid (<section.pageSection> — `Latest Diaries + Updates`)**:
   - Landmark `<section class="pageSection home__sec__latest_news">` rendering section `Latest Diaries + Updates` with copy *"Functional Always active"*, asset references (`clarity.js`, `recaptcha__en.js`, `xmlrpc.php`, `banner-2-optin.css`), and grid rule `.has-text-align-center { text-align:center }`.
4. **Interactive Detail & Feature Matrix (<section.pageSection> — `Most Popular Prints`)**:
   - Landmark `<section class="pageSection home__sec__text">` framing `Most Popular Prints` and `Metallica` (*"Required to enable core site functionality and services you reque"*) with `#222222` surface cards, `#161618` accents, and `.site .wc-block-grid__products { display:grid;gap:30px;margin:0 }`.
5. **Colophon & Global Directory Footer (<footer.page-template-template-homepage> — `https://www.rosshalfin.com`)**:
   - Landmark `<footer class="page-template-template-homepage">` anchoring `Ross Halfin Photography · Music ` footer links (`€ 0.00 0`), copy *"Used to store your preferences, such as language or display "*, and `#333333` structural dividers.
