# UI & UX Architecture: www-stellarmanagement-com

## Overview & Design Identity
- **Target**: `www-stellarmanagement-com` (**Stellar Management · NYC Real Estate Developer & No Fee Rentals**)
- **Production URL**: [https://www.stellarmanagement.com](https://www.stellarmanagement.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#181513` ink, `#f5f5f5` accent)
- **Summary**: Stellar is a leading New York real estate developer and manager providing a wide range of apartments and commercial properties. Browse no...
- **Total Clean CSS Variables Extracted**: `92` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `General Sans Variable`
- **Body Font Stack**: `Playfair Display`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--title-xl-size: max(28px,4.4rem)`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--input-font-size-mob)`, `var(--desc-m-size)`, `var(--swiper-navigation-size)`, `var(--desc-s-size)`, `14px`)
- **Body Copy**: rule `p` (`font-size: var(--desc-l-size)`, `line-height: 150%`, `letter-spacing: 0`, `font-weight: 500`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--input-font-size-mob)`, `var(--desc-m-size)`, `var(--swiper-navigation-size)`, `var(--desc-s-size)`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--white)` in `:root` |
| **Primary Typography Ink** | `#181513` | `var(--black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#cdcdcd` | `var(--grey)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f5f5` | `var(--grey-light)` in `:root` |
| **Secondary / Muted Copy** | `#9e9e9e` | `var(--grey-medium)` in `:root` |
| **Structural Hairline Border** | `#727272` | `var(--grey-dark)` in `:root` |
| **Variable Token (`--grey-skeleton`)** | `#ebebeb` | `var(--grey-skeleton)` in `:root` |
| **Variable Token (`--grey-hover`)** | `#f0f0f0` | `var(--grey-hover)` in `:root` |
| **Variable Token (`--dark-blue`)** | `#06184f` | `var(--dark-blue)` in `:root` |
| **Variable Token (`--sky-blue`)** | `#dee9ff` | `var(--sky-blue)` in `:root` |
| **Variable Token (`--sky-blue-60`)** | `#ebf2ff` | `var(--sky-blue-60)` in `:root` |
| **Variable Token (`--sky-blue-25`)** | `#f7faff` | `var(--sky-blue-25)` in `:root` |
| **Variable Token (`--red`)** | `#e90000` | `var(--red)` in `:root` |
| **Variable Token (`--green`)** | `#0d4f06` | `var(--green)` in `:root` |
| **Variable Token (`--green-light`)** | `#def2df` | `var(--green-light)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `#fff` | Canvas / Surface Token |
| `--black` | `#181513` | Canvas / Surface Token |
| `--grey` | `#cdcdcd` | Color / Atmospheric Token |
| `--grey-light` | `#f5f5f5` | Canvas / Surface Token |
| `--grey-medium` | `#9e9e9e` | Color / Atmospheric Token |
| `--grey-dark` | `#727272` | Canvas / Surface Token |
| `--grey-skeleton` | `#ebebeb` | Color / Atmospheric Token |
| `--grey-hover` | `#f0f0f0` | Color / Atmospheric Token |
| `--dark-blue` | `#06184f` | Canvas / Surface Token |
| `--sky-blue` | `#dee9ff` | Color / Atmospheric Token |
| `--sky-blue-60` | `#ebf2ff` | Color / Atmospheric Token |
| `--sky-blue-25` | `#f7faff` | Color / Atmospheric Token |
| `--red` | `#e90000` | Color / Atmospheric Token |
| `--green` | `#0d4f06` | Color / Atmospheric Token |
| `--green-light` | `#def2df` | Canvas / Surface Token |
| `--black-opacity-l` | `rgba(0,0,0,.8)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-stellarmanagement-com`)**:
   - Landmark `<header class="header">` hosting `Stellar Management · NYC Real Estate` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hid="page-vw"`, `data-gtag`, `data-v-d3185d1d`, `data-path="/"`), and stylesheet rule `root { --block-width-m:84rem;--search-sidebar-width:30rem }`.
2. **Hero Stage & Focal Lead (<section.first> — `We help New Yorkers find home`)**:
   - Landmark `<section class="first scroll-locked-fullscreen">` presenting display lead `We help New Yorkers find home` and copy excerpt *"R e n t w i t h u s R e n t w i t h u s"* over `#fff` canvas and `#181513` ink.
3. **Primary Showcase & Content Grid (<section.block> — `From historic blocks to new develo`)**:
   - Landmark `<section class="block">` rendering section `From historic blocks to new developments, we crea...` with copy *"R e n t w i t h u s"*, asset references (`entry.BO5l_mVZ.css`, `default.D_u9mJpK.css`, `filterMain.Dy3QUOs1.css`, `appInput.BLk3pTmz.css`), and grid rule `before { background:var(--white)!important }`.
4. **Interactive Detail & Feature Matrix (<section.neighborhoods> — `Explore our backyard`)**:
   - Landmark `<section class="neighborhoods neighborhoods-section">` framing `Explore our backyard` and `Where numbers reflect people, places, and purpose` (*"Since 1985, creating, investing, developing & living NYC real est"*) with `#cdcdcd` surface cards, `#f5f5f5` accents, and `focus-within { border-color:var(--dark-blue) }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.stellarmanagement.com`)**:
   - Landmark `<footer class="footer">` anchoring `Stellar Management · NYC Real Es` footer links (`Overview · Index · Archive · About · Contact`), copy *"Approach The Way We Work, Defines Who We Are"*, and `#727272` structural dividers.
