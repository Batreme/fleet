# UI & UX Architecture: www-gravelleduparc-com

## Overview & Design Identity
- **Target**: `www-gravelleduparc-com` (**Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026**)
- **Production URL**: [https://www.gravelleduparc.com/](https://www.gravelleduparc.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fffbf0` canvas, `#15663c` ink, `#baf1c5` accent)
- **Summary**: La Gravelle du Parc, c’est un week-end de gravel : vélo de gravelle le samedi, course à pied le dimanche. Plusieurs distances, expérience...
- **Total Clean CSS Variables Extracted**: `49` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Frama Regular`
- **Body Font Stack**: `PP Frama Black`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 700`)
- **Metadata & Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fffbf0` | `var(--token-a5ac08d3-da39-4d23-ae40-d4bbcd8e3fd1)` in `:root` |
| **Primary Typography Ink** | `#cca7e4` | `var(--token-801dfdec-b31d-4dcb-87a3-9e0e817b84a0)` in `:root` |
| **Elevated Surface / Card Substrate** | `#15663c` | `var(--token-b73f07c2-b1d7-4a83-b30a-c43c65cbb498)` in `:root` |
| **Interactive Accent / Highlight** | `#baf1c5` | `var(--token-5eaeb86f-8e78-453e-95cb-73c07bed6a1e)` in `:root` |
| **Secondary / Muted Copy** | `#a980c4` | `var(--token-955bd1bf-f5bd-48e1-aa7a-184730d5a46a)` in `:root` |
| **Structural Hairline Border** | `#7ede92` | `var(--token-819cd3c1-358d-4fbc-829d-c778243cf65a)` in `:root` |
| **Variable Token (`--token-59b8ee6e-2d8c-4453-b6ce-0800b1668299`)** | `#f8efda` | `var(--token-59b8ee6e-2d8c-4453-b6ce-0800b1668299)` in `:root` |
| **Variable Token (`--token-e2fce9db-4f7d-4508-8af5-6e27334c8d93`)** | `#f7ebff` | `var(--token-e2fce9db-4f7d-4508-8af5-6e27334c8d93)` in `:root` |
| **Variable Token (`--token-9e8de558-3943-41e7-b539-eba07384897f`)** | `#59396e` | `var(--token-9e8de558-3943-41e7-b539-eba07384897f)` in `:root` |
| **Variable Token (`--token-ebd8e842-7d03-4da2-a324-48cca40569ff`)** | `#84ba8f` | `var(--token-ebd8e842-7d03-4da2-a324-48cca40569ff)` in `:root` |
| **Variable Token (`--token-9a333514-96bd-43a4-9d9c-387c4eccd2bb`)** | `#363229` | `var(--token-9a333514-96bd-43a4-9d9c-387c4eccd2bb)` in `:root` |
| **Variable Token (`--token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb`)** | `#dbd0b4` | `var(--token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb)` in `:root` |
| **Variable Token (`--token-394b655e-eb71-48d0-ad1f-647e45a4f590`)** | `#f5fbff` | `var(--token-394b655e-eb71-48d0-ad1f-647e45a4f590)` in `:root` |
| **Variable Token (`--token-7271da1b-9f0a-41bd-91b9-d7098d8944de`)** | `#efedff` | `var(--token-7271da1b-9f0a-41bd-91b9-d7098d8944de)` in `:root` |
| **Variable Token (`--token-3d3e37dc-c784-4b46-95bf-180ff18227e6`)** | `#0b0b0b` | `var(--token-3d3e37dc-c784-4b46-95bf-180ff18227e6)` in `:root` |
| **Variable Token (`--token-a37e6c3e-a10c-437b-b258-07d1d49555da`)** | `#fcebef` | `var(--token-a37e6c3e-a10c-437b-b258-07d1d49555da)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-a5ac08d3-da39-4d23-ae40-d4bbcd8e3fd1` | `#fffbf0` | Color / Atmospheric Token |
| `--token-801dfdec-b31d-4dcb-87a3-9e0e817b84a0` | `#cca7e4` | Color / Atmospheric Token |
| `--token-b73f07c2-b1d7-4a83-b30a-c43c65cbb498` | `#15663c` | Color / Atmospheric Token |
| `--token-5eaeb86f-8e78-453e-95cb-73c07bed6a1e` | `#baf1c5` | Color / Atmospheric Token |
| `--token-955bd1bf-f5bd-48e1-aa7a-184730d5a46a` | `#a980c4` | Color / Atmospheric Token |
| `--token-819cd3c1-358d-4fbc-829d-c778243cf65a` | `#7ede92` | Color / Atmospheric Token |
| `--token-59b8ee6e-2d8c-4453-b6ce-0800b1668299` | `#f8efda` | Color / Atmospheric Token |
| `--token-e2fce9db-4f7d-4508-8af5-6e27334c8d93` | `#f7ebff` | Color / Atmospheric Token |
| `--token-9e8de558-3943-41e7-b539-eba07384897f` | `#59396e` | Color / Atmospheric Token |
| `--token-ebd8e842-7d03-4da2-a324-48cca40569ff` | `#84ba8f` | Color / Atmospheric Token |
| `--token-9a333514-96bd-43a4-9d9c-387c4eccd2bb` | `#363229` | Color / Atmospheric Token |
| `--token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb` | `#dbd0b4` | Color / Atmospheric Token |
| `--token-394b655e-eb71-48d0-ad1f-647e45a4f590` | `#f5fbff` | Color / Atmospheric Token |
| `--token-7271da1b-9f0a-41bd-91b9-d7098d8944de` | `#efedff` | Color / Atmospheric Token |
| `--token-3d3e37dc-c784-4b46-95bf-180ff18227e6` | `#0b0b0b` | Color / Atmospheric Token |
| `--token-a37e6c3e-a10c-437b-b258-07d1d49555da` | `#fcebef` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-gravelleduparc-com`)**:
   - Landmark `<header class="lenis">` hosting `Gravelle du Parc · Événement gravel ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `html.lenis body { height: auto; }`.
2. **Hero Stage & Focal Lead (<section.framer-3c888> — `GRAVELLE DU PARC`)**:
   - Landmark `<section class="framer-3c888">` presenting display lead `GRAVELLE DU PARC` and copy excerpt *"Événement Événement"* over `#fffbf0` canvas and `#15663c` ink.
3. **Primary Showcase & Content Grid (<section.framer-1qtcgda> — `Ils seront là! Et toi?`)**:
   - Landmark `<section class="framer-1qtcgda">` rendering section `Ils seront là! Et toi?` with copy *"Expériences Expériences"*, asset references (`iM7hUimGereN8t0VwJyHekeIY.png`, `kPdF8fyktsGL7BKiYVgEs0g8Ozg.png`, `BPKxeJbv6FMQXmeKTCEyN570iaI.png`, `script`), and grid rule `.lenis-stopped { overflow: clip; }`.
4. **Interactive Detail & Feature Matrix (<section.framer-597gjk> — `Le parcours`)**:
   - Landmark `<section class="framer-597gjk">` framing `Le parcours` and `Les expériences` (*"horaire du weekend horaire du weekend"*) with `#15663c` surface cards, `#baf1c5` accents, and `.lenis.lenis-smooth iframe { pointer-events: none; }`.
5. **Colophon & Global Directory Footer (<footer.framer-17xvneb-container> — `https://www.gravelleduparc.com/`)**:
   - Landmark `<footer class="framer-17xvneb-container">` anchoring `Gravelle du Parc · Événement gra` footer links (`Overview · Index · Archive · About · Contact`), copy *"Instagram Instagram"*, and `#7ede92` structural dividers.
