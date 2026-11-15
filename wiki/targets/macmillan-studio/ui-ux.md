# UI & UX Architecture: macmillan-studio

## Overview & Design Identity
- **Target**: `macmillan-studio` (**Christian MacMillan · Independent Tech Lead—Developer**)
- **Production URL**: [https://macmillan.studio](https://macmillan.studio)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#d3d6da`)
- **Summary**: Over a decade of experience implementing fully custom, high-quality interactive experiences for global agencies and brands.
- **Total Clean CSS Variables Extracted**: `32` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `HelveticaNowDisplayMedium`
- **Body Font Stack**: `HelveticaNowDisplayBold`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `10px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `10px`)
- **Body Copy**: rule `p` (`font-size: max(4vw,1.5rem)`, `line-height: max(4.8vw,1.8rem)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `10px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#bdff00` | `var(--lime)` in `:root` |
| **Interactive Accent / Highlight** | `#d3d6da` | `var(--light-grey)` in `:root` |
| **Secondary / Muted Copy** | `#818388` | `var(--dark-grey)` in `:root` |
| **Structural Hairline Border** | `#000000` | `vg__project__inkollectors__firs... { fill: black }` (`#000000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--col` | `33.3333%` | Layout / Spatial Grid Token |
| `--columns` | `4` | Layout / Spatial Grid Token |
| `--columns-width` | `calc((var(--columns)/var(--layout-columns))*100%)` | Layout / Spatial Grid Token |
| `--columns-gap-width` | `calc(var(--layout-gutter)*(1 - 1/(var(--layout-columns)/var(--columns))))` | Layout / Spatial Grid Token |
| `--gap` | `2` | Layout / Spatial Grid Token |
| `--gap-width` | `calc((var(--gap)/var(--layout-columns))*100%)` | Layout / Spatial Grid Token |
| `--size` | `min(5.5555555556vw,10rem)` | Layout / Spatial Grid Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--lime` | `#bdff00` | Color / Atmospheric Token |
| `--light-grey` | `#d3d6da` | Canvas / Surface Token |
| `--dark-grey` | `#818388` | Canvas / Surface Token |
| `--layout-max-width` | `1800px` | Layout / Spatial Grid Token |
| `--layout-columns` | `8` | Layout / Spatial Grid Token |
| `--layout-margin` | `1.6rem` | Layout / Spatial Grid Token |
| `--layout-gutter` | `.8rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `macmillan-studio`)**:
   - Landmark `<header class="header">` hosting `Christian MacMillan · Independent Te` navigation (`Projects, · Services, · About`), DOM attributes (`data-tab-fixed`, `data-v-7d7b041a`, `data-scroll-target-top`, `data-scroll-continuous`), and stylesheet rule `.svg__project__inkollectors__firs... { display:block;fill:none;height:auto;width:min(187.8933333333vw,338.208rem) }`.
2. **Hero Stage & Focal Lead (<section.home__hero> — `MacMillan Studio—Independent Devel`)**:
   - Landmark `<section class="home__hero">` presenting display lead `MacMillan Studio—Independent Development Studio l...` and copy excerpt *"Independent Tech Lead—Developer"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.home__hero> — `Services`)**:
   - Landmark `<section class="home__hero">` rendering section `Services` with copy *"Over a decade of experience implementing fully custom, high-quali"*, asset references (`entry.CkIT_B6y.css`, `default.Kg7iOwm3.css`, `Pause.BHNIHZ0n.css`, `_slug_.DfTMbnN4.css`), and grid rule `project__inkollectors__first-line... { fill:var(--black) }`.
4. **Interactive Detail & Feature Matrix (<section.home__hero> — `Joining your team as a freelancer `)**:
   - Landmark `<section class="home__hero">` framing `Joining your team as a freelancer or taking on th...` and `Front-end` (*"Joining your team as a freelancer or taking on the project indepe"*) with `#bdff00` surface cards, `#d3d6da` accents, and `oject__inkollectors--animation sv... { opacity:.00001 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://macmillan.studio`)**:
   - Landmark `<footer class="footer">` anchoring `Christian MacMillan · Independen` footer links (`Projects, · Services, · About`), copy *"From large-scale websites to creative campaign landing pages"*, and `#000000` structural dividers.
