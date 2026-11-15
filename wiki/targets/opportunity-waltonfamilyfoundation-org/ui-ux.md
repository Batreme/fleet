# UI & UX Architecture: opportunity-waltonfamilyfoundation-org

## Overview & Design Identity
- **Target**: `opportunity-waltonfamilyfoundation-org` (**Access to Opportunity: Gallup Research · Walton Family Foundation**)
- **Production URL**: [https://opportunity.waltonfamilyfoundation.org/](https://opportunity.waltonfamilyfoundation.org/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#12110e`)
- **Summary**: Explore Walton Family Foundation and Gallup research on opportunity. See how investments in education, nature, and communities help oppor...
- **Total Clean CSS Variables Extracted**: `73` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Serrif`
- **Body Font Stack**: `Serrif Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--tw-fluid-clamp-min_18_75-cl...`, `var(--tw-fluid-clamp-min_31_5-cla...`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--tw-fluid-clamp-min_18_75-cl...`, `var(--tw-fluid-clamp-min_31_5-cla...`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--tw-fluid-clamp-min_18_75-cl...`, `var(--tw-fluid-clamp-min_31_5-cla...`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e7e72b` | `var(--highlight)` in `:root` |
| **Interactive Accent / Highlight** | `#12110e` | `var(--foreground)` in `:root` |
| **Secondary / Muted Copy** | `#5f8763` | `var(--green)` in `:root` |
| **Structural Hairline Border** | `#337c83` | `var(--teal)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-sans)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |
| `--radius-xl` | `.75rem` | Elevation / Border Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-white-100` | `var(--white-100)` | Canvas / Surface Token |
| `--font-serrif-compressed` | `var(--font-serrif-compressed)` | Typography / Scale Token |
| `--font-serrif` | `var(--font-serrif)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.is-loading> — `opportunity-waltonfamilyfoundation-org`)**:
   - Landmark `<header class="is-loading">` hosting `Access to Opportunity: Gallup Resear` navigation (`Privacy Policy · Terms of Use`), DOM attributes (`data-precedence="next"`, `data-lenis-prevent="true"`, `data-menu-background="true"`, `data-menu-link="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Where opportunity takes root`)**:
   - Landmark `<section class="antialiased">` presenting display lead `Where opportunity takes root` and copy excerpt *"01 Where Opportunity Takes Root The vision behind our work"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.lenis> — `Opportunity enables people to fulf`)**:
   - Landmark `<section class="lenis">` rendering section `Opportunity enables people to fulfill their highe...` with copy *"Where Opportunity Takes Root The vision behind our work"*, asset references (`0okt1rwt07m_z.css`, `0ji28_e_~fdtg.js`, `0nz2u-qe8z68i.js`, `0yjw-7sa79pfd.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.lenis-stopped> — `What does opportunity mean today? `)**:
   - Landmark `<section class="lenis-stopped">` framing `What does opportunity mean today? What does oppor...` and `Lets go deeper... Lets go deeper...` (*"Where Opportunity Takes Root"*) with `#e7e72b` surface cards, `#12110e` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://opportunity.waltonfamilyfoundation.org/`)**:
   - Landmark `<footer class="fixed inset-x-0">` anchoring `Access to Opportunity: Gallup Re` footer links (`Privacy Policy · Terms of Use`), copy *"The vision behind our work"*, and `#337c83` structural dividers.
