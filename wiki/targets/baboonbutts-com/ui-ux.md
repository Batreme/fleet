# UI & UX Architecture: baboonbutts-com

## Overview & Design Identity
- **Target**: `baboonbutts-com` (**Baboon Butts - The redder the better!**)
- **Production URL**: [https://baboonbutts.com/](https://baboonbutts.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#204ce5` canvas, `#fff` ink, `#112337` accent)
- **Summary**: This Cheeky ad campaign to show how effective a little strategy – and a lot of raunchy visuals and messaging – can be.
- **Total Clean CSS Variables Extracted**: `769` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `mono45-headline`
- **Body Font Stack**: `inline-block`
- **Monospace / Technical Font Stack**: `mono45-headline`
- **Hero Display (`H1`)**: CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `h1` (`font-size: clamp(3rem, -3.3099rem + 13.1...`, `line-height: 0.8`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2.1875rem, 1.7493rem +...`, `line-height: 0.8421052632`)
- **Body Copy**: rule `body` (`line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--gf-label-width: 30%`, `--gf-label-req-gap: 6px`, `--gf-label-space-primary: 8px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#204ce5` | `var(--gf-color-primary)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--gf-color-primary-contrast)` in `:root` |
| **Elevated Surface / Card Substrate** | `#044ad3` | `var(--gf-color-primary-darker)` in `:root` |
| **Interactive Accent / Highlight** | `#112337` | `var(--gf-color-secondary-contrast)` in `:root` |
| **Secondary / Muted Copy** | `#f2f3f5` | `var(--gf-color-secondary-darker)` in `:root` |
| **Structural Hairline Border** | `#585e6a` | `var(--gf-color-out-ctrl-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gf-form-gap-x` | `16px` | Layout / Spatial Grid Token |
| `--gf-form-gap-y` | `40px` | Layout / Spatial Grid Token |
| `--gf-form-footer-margin-y-start` | `24px` | Layout / Spatial Grid Token |
| `--gf-form-footer-gap` | `8px` | Layout / Spatial Grid Token |
| `--gf-field-gap-x` | `12px` | Layout / Spatial Grid Token |
| `--gf-field-gap-y` | `12px` | Layout / Spatial Grid Token |
| `--gf-field-date-width` | `168px` | Layout / Spatial Grid Token |
| `--gf-field-time-width` | `110px` | Layout / Spatial Grid Token |
| `--gf-field-list-btns-gap` | `8px` | Layout / Spatial Grid Token |
| `--gf-field-list-btns-width` | `calc(32px + var(--gf-field-list-btns-gap) + var(--gf-field-gap-x))` | Layout / Spatial Grid Token |
| `--gf-field-pg-steps-gap-y` | `8px` | Layout / Spatial Grid Token |
| `--gf-field-pg-steps-gap-x` | `24px` | Layout / Spatial Grid Token |
| `--gf-label-width` | `30%` | Layout / Spatial Grid Token |
| `--gf-label-req-gap` | `6px` | Layout / Spatial Grid Token |
| `--header-height` | `90px` | Layout / Spatial Grid Token |
| `--gf-radius` | `3px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wp-block-thirtysixblocks-header> — `baboonbutts-com`)**:
   - Landmark `<header class="wp-block-thirtysixblocks-header">` hosting `Baboon Butts - The redder the better` navigation (`Get a Hold of Us`), DOM attributes (`data-magnet`, `data-magnet-movement="80"`, `data-magnet-rotation="15"`, `data-magnet-smooth="0.5"`), and stylesheet rule `.gform-theme--foundation ::before { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.wp-block-thirtysixblocks-slide> — `The Fascinating Tail of Baboon But`)**:
   - Landmark `<section class="wp-block-thirtysixblocks-slide slide-intro">` presenting display lead `The Fascinating Tail of Baboon Butts` and copy excerpt *"A cheeky look at one of nature’s most successful forms of adverti"* over `#204ce5` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.wp-block-thirtysixblocks-image> — `Before billboards, branding, and b`)**:
   - Landmark `<section class="wp-block-thirtysixblocks-image">` rendering section `Before billboards, branding, and billion-dollar a...` with copy *"Before billboards, branding, and billion-dollar ad campaigns, nat"*, asset references (`insight.min.js`, `use.typekit.net`, `style-index.css`, `bmx2okd.css`), and grid rule `.gform-theme--foundation legend { background:0 0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.wp-block-thirtysixblocks-slide> — `Meet one of nature’s most eye-catc`)**:
   - Landmark `<section class="wp-block-thirtysixblocks-slide">` framing `Meet one of nature’s most eye-catching advertisin...` and `The baboon’s brilliantly bold backside. T h e b a...` (*"B e f o r e b i l l b o a r d s , b r a n d i n g , a n d b i l l"*) with `#044ad3` surface cards, `#112337` accents, and `.gform-theme--foundation fieldset { border:none;display:block;margin:0 }`.
5. **Colophon & Global Directory Footer (<footer.wp-block-thirtysixblocks-footer> — `https://baboonbutts.com/`)**:
   - Landmark `<footer class="wp-block-thirtysixblocks-footer">` anchoring `Baboon Butts - The redder the be` footer links (`Get a Hold of Us`), copy *"b i l l b o a r d s ,"*, and `#585e6a` structural dividers.
