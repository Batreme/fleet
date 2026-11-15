# UI & UX Architecture: henrietta-wearetattoodigital-com

## Overview & Design Identity
- **Target**: `henrietta-wearetattoodigital-com` (**Henrietta Said : Scandalously Spicy**)
- **Production URL**: [https://henrietta.wearetattoodigital.com/](https://henrietta.wearetattoodigital.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e3a898` / `#8b231a`)
- **Summary**: It’s hard to contain this kind of spiciness. That’s why we’re bringing our scandalously spicy selves to the mainstream with bold wing-fla...
- **Total Clean CSS Variables Extracted**: `21` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Changa One`
- **Body Font Stack**: `Thedodgerinky`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: CSS variables `--body: #e3a898`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e3a898` | `var(--body)` in `:root` |
| **Primary Typography Ink** | `#d32929` | `var(--kimchi-red)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eae6e3` | `var(--light-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#8b231a` | `var(--brown-chicken)` in `:root` |
| **Secondary / Muted Copy** | `#f45016` | `var(--orange)` in `:root` |
| **Structural Hairline Border** | `#efc415` | `var(--lemon)` in `:root` |
| **Variable Token (`--dark`)** | `#2d2a26` | `var(--dark)` in `:root` |
| **Variable Token (`--white`)** | `#fff` | `var(--white)` in `:root` |
| **Variable Token (`--black`)** | `#0E0E0E` | `var(--black)` in `:root` |
| **Variable Token (`--salmon`)** | `#f7894e` | `var(--salmon)` in `:root` |
| **Variable Token (`--dark-red`)** | `#761615` | `var(--dark-red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--body` | `#e3a898` | Color / Atmospheric Token |
| `--kimchi-red` | `#d32929` | Color / Atmospheric Token |
| `--light-grey` | `#eae6e3` | Canvas / Surface Token |
| `--brown-chicken` | `#8b231a` | Color / Atmospheric Token |
| `--orange` | `#f45016` | Color / Atmospheric Token |
| `--lemon` | `#efc415` | Color / Atmospheric Token |
| `--dark` | `#2d2a26` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--black` | `#0E0E0E` | Canvas / Surface Token |
| `--salmon` | `#f7894e` | Color / Atmospheric Token |
| `--dark-red` | `#761615` | Canvas / Surface Token |
| `--blush` | `#e3a898` | Color / Atmospheric Token |
| `--hst-duration-exit` | `0.8s` | Motion / Easing Token |
| `--hst-duration-enter` | `0.95s` | Motion / Easing Token |
| `--hst-easing` | `cubic-bezier(0.76, 0, 0.24, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.our-products-list> — `henrietta-wearetattoodigital-com`)**:
   - Landmark `<nav class="our-products-list w-dropdown-list">` hosting `Henrietta Said : Scandalously Spicy` navigation (`ancho kimchi · original buffalo · lemon pepper`), DOM attributes (`data-wf-domain="henrietta.wearetattoo..."`, `data-wf-page="69fc9bd508ea045856fc2e42"`, `data-wf-site="69fc9bd208ea045856fc2c0a"`, `data-preloader-counter`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.preloader> — `home`)**:
   - Landmark `<div class="preloader">` presenting display lead `home` and copy excerpt *"s c a n d a l p a g e s"* over `#e3a898` canvas and `#8b231a` ink.
3. **Primary Showcase & Content Grid (<div.preloader> — `scandal pages`)**:
   - Landmark `<div class="preloader">` rendering section `scandal pages` with copy *"NASHVILLE HOT CHICKEN"*, asset references (`cdn.prod.website-files.com`, `henrietta-said.webflow.shared.afe...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.preloader> — `our story`)**:
   - Landmark `<div class="preloader">` framing `our story` and `press` (*"nashville hot chicken"*) with `#eae6e3` surface cards, `#8b231a` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.lenis> — `https://henrietta.wearetattoodigital.com/`)**:
   - Landmark `<footer class="lenis">` anchoring `Henrietta Said : Scandalously Sp` footer links (`ancho kimchi · original buffalo · lemon pepper`), copy *"Jumbo roasted peanuts with a fusion of flavorfully fun ancho"*, and `#efc415` structural dividers.
