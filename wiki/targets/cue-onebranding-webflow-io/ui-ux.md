# UI & UX Architecture: cue-onebranding-webflow-io

## Overview & Design Identity
- **Target**: `cue-onebranding-webflow-io` (**Cue - Creating Unforgettable Experiences**)
- **Production URL**: [https://cue-onebranding.webflow.io/](https://cue-onebranding.webflow.io/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#13171a` canvas, `#f5f5f7` ink, `#e4e5e5` accent)
- **Summary**: Fan-first technology for premium brands and event experiences. Take your events to the next level with CUE and experience true fan engage...
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: 2.5rem`)
- **Body Copy**: rule `p` (`font-size: inherit`, `line-height: inherit`, `font-weight: 400!important`)
- **Metadata & Labels**: CSS variables `--radius--small: .25rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#13171a` | `var(--color--black)` in `:root` |
| **Primary Typography Ink** | `#3aebdb` | `var(--color--aqua)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f5f5f7` | `var(--color--gray)` in `:root` |
| **Interactive Accent / Highlight** | `#e4e5e5` | `var(--color--mid-gray)` in `:root` |
| **Secondary / Muted Copy** | `#030b15` | `var(--color--dark-blue)` in `:root` |
| **Structural Hairline Border** | `#010012` | `var(--color--deep-blue)` in `:root` |
| **Variable Token (`--on-light-gradient`)** | `#03b7e8` | `var(--on-light-gradient)` in `:root` |
| **Variable Token (`--on-light-gradient`)** | `#2f68e9` | `var(--on-light-gradient)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color--black` | `#13171a` | Canvas / Surface Token |
| `--color--aqua` | `#3aebdb` | Brand / Palette Token |
| `--color--white` | `white` | Canvas / Surface Token |
| `--radius--small` | `.25rem` | Elevation / Border Token |
| `--color--gray` | `#f5f5f7` | Brand / Palette Token |
| `--color--mid-gray` | `#e4e5e5` | Brand / Palette Token |
| `--color--dark-blue` | `#030b15` | Canvas / Surface Token |
| `--gap--2-5` | `2.5rem` | Layout / Spatial Grid Token |
| `--page-padding` | `0px` | Layout / Spatial Grid Token |
| `--color--deep-blue` | `#010012` | Brand / Palette Token |
| `--radius--main` | `.75rem` | Elevation / Border Token |
| `--transition-speed` | `1.5s` | Motion / Easing Token |
| `--on-light-gradient` | `linear-gradient(82deg, #03b7e8 2.55%, #2f68e9 100.58%)` | Canvas / Surface Token |
| `--speed` | `100s` | Motion / Easing Token |
| `--cue-onebranding--bg` | `#13171a` | Canvas Substrate (from `var(--color--black)` in `:root`) |
| `--cue-onebranding--ink` | `#f5f5f7` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.section> — `cue-onebranding-webflow-io`)**:
   - Landmark `<header class="section cc-header-centered-gradient">` hosting `Cue - Creating Unforgettable Experie` navigation (`NAB · Ross Video · REQUEST A DEMO · WE ARE CUE`), DOM attributes (`data-wf-domain="cue-onebranding.webfl..."`, `data-wf-page="662871ca1b5c639c39515607"`, `data-wf-site="662871ca1b5c639c39515603"`, `data-ads-portal-id="8068777"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Create Unforgettable Experiences`)**:
   - Landmark `<section class="section cc-2col-text-cta">` presenting display lead `Create Unforgettable Experiences` and copy excerpt *"This website stores cookies on your computer. These cookies are u"* over `#13171a` canvas and `#f5f5f7` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Sports`)**:
   - Landmark `<section class="section cc-video-zoom">` rendering section `Sports` with copy *"If you decline, your information won’t be tracked when you visit "*, asset references (`cdn.prod.website-files.com`, `cue-onebranding.shared.e83737123....`, `clarity.js`, `odet0ilb8r`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `High schools`)**:
   - Landmark `<section class="section cc-product-starter">` framing `High schools` and `Agency` (*"Reach out to the team if you need to publish something."*) with `#f5f5f7` surface cards, `#e4e5e5` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://cue-onebranding.webflow.io/`)**:
   - Landmark `<footer class="footer">` anchoring `Cue - Creating Unforgettable Exp` footer links (`NAB · Ross Video · REQUEST A DEMO · WE ARE CUE`), copy *"It was a great week at NAB with our friends from Ross Video "*, and `#010012` structural dividers.
