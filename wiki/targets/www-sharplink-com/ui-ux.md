# UI & UX Architecture: www-sharplink-com

## Overview & Design Identity
- **Target**: `www-sharplink-com` (**Sharplink : Home**)
- **Production URL**: [https://www.sharplink.com/](https://www.sharplink.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f3f3f3`)
- **Summary**: Sharplink is the institutional-grade Ethereum treasury platform giving investors a smarter, more productive access vehicle to ETH
- **Total Clean CSS Variables Extracted**: `590` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo Narrow`
- **Body Font Stack**: `Archivo Narrow Fallback: Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `,h1` (`font-size: 88px`, `line-height: .96`, `letter-spacing: -2.64px`)
- **Section Heading (`H2`)**: rule `,h2` (`font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.35`, `letter-spacing: 0`, `font-weight: 500`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `88px`, `68px`, `52px`, `44px`, `32px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#676767` | `var(--grey-primary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a9a9a9` | `var(--grey-secondary)` in `:root` |
| **Interactive Accent / Highlight** | `#f3f3f3` | `var(--off-white)` in `:root` |
| **Secondary / Muted Copy** | `#f7f7f5` | `var(--surface-background)` in `:root` |
| **Structural Hairline Border** | `#0e76ff` | `var(--brand-blue-primary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--layout-columns-count` | `4` | Layout / Spatial Grid Token |
| `--layout-columns-gap` | `16px` | Layout / Spatial Grid Token |
| `--layout-rows-gap` | `8px` | Layout / Spatial Grid Token |
| `--layout-margin` | `16px` | Layout / Spatial Grid Token |
| `--layout-width` | `calc(100vw - var(--layout-margin)*2)` | Layout / Spatial Grid Token |
| `--pin-color` | `var(--brand-blue-primary)` | Brand / Palette Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--black-0` | `transparent` | Canvas / Surface Token |
| `--black-5` | `rgb(0 0 0/5%)` | Canvas / Surface Token |
| `--black-10` | `rgba(0,0,0,.1)` | Canvas / Surface Token |
| `--black-15` | `rgba(0,0,0,.15)` | Canvas / Surface Token |
| `--black-20` | `rgba(0,0,0,.2)` | Canvas / Surface Token |
| `--black-25` | `rgba(0,0,0,.25)` | Canvas / Surface Token |
| `--black-30` | `rgba(0,0,0,.3)` | Canvas / Surface Token |
| `--black-35` | `rgba(0,0,0,.35)` | Canvas / Surface Token |
| `--black-40` | `rgba(0,0,0,.4)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-sharplink-com`)**:
   - Landmark `<header class="site-header theme-dark">` hosting `Sharplink : Home` navigation (`Home · About · Investors · Opportunity · News`), DOM attributes (`data-v-00374420`, `data-v-e2147945`, `data-v-9d8fa70e`, `data-v-15fa0cd1`), and stylesheet rule `.body-large { font-size:19px;font-style:normal;line-height:1.35 }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Please enable JavaScript`)**:
   - Landmark `<section class="home-hero mobile-only">` presenting display lead `Please enable JavaScript` and copy excerpt *"SharpLink is proudly listed on NASDAQ under the trading symbol SB"* over `#000` canvas and `#f7f7f5` ink.
3. **Primary Showcase & Content Grid (<section.home-productivity> — `This website requires JavaScript i`)**:
   - Landmark `<section class="home-productivity">` rendering section `This website requires JavaScript in order to work...` with copy *"Investors Investors"*, asset references (`entry.097ojG-J.css`, `Content.DYtseY0i.css`, `colors.DCDPWAmH.css`, `Wrapper.CA5eSekD.css`), and grid rule `.body-blog { font-size:16px;font-style:medium;line-height:1.56 }`.
4. **Interactive Detail & Feature Matrix (<section.home-hero> — `Ethereum with an Edge`)**:
   - Landmark `<section class="home-hero wrapped-hero">` framing `Ethereum with an Edge` and `Pioneering Productivity` (*"Opportunity Opportunity"*) with `#a9a9a9` surface cards, `#f3f3f3` accents, and `.mono { font-size:13px;font-weight:500 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.sharplink.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Sharplink : Home` footer links (`Home · About · Investors · Opportunity · News`), copy *"ETH Dashboard ETH Dashboard"*, and `#0e76ff` structural dividers.
