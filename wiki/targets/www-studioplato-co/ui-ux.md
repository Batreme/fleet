# UI & UX Architecture: www-studioplato-co

## Overview & Design Identity
- **Target**: `www-studioplato-co` (**Studio Plato - Contemporary Interior Design**)
- **Production URL**: [https://www.studioplato.co/](https://www.studioplato.co/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#4f4f4f` / `#fff`)
- **Summary**: STUDIO PLATO specializes in interior and architecture design. Connect with us for innovative design solutions.
- **Total Clean CSS Variables Extracted**: `11` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Opensaucesans`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4f4f4f` | `var(--grey-darkest)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--grey-lightest)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007aff` | `:root { color: #007aff }` |
| **Interactive Accent / Highlight** | `#fff` | `.swiper-lazy-preloader-white { color: #fff }` |
| **Secondary / Muted Copy** | `#000` | `.swiper-lazy-preloader-black { color: #000 }` |
| **Structural Hairline Border** | `#0000` | `a { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--grey-darkest` | `#4f4f4f` | Canvas / Surface Token |
| `--white` | `white` | Canvas / Surface Token |
| `--black` | `black` | Canvas / Surface Token |
| `--site-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--grey-lightest` | `#ddd` | Canvas / Surface Token |
| `--spacing-120` | `7.5em` | Layout / Spatial Grid Token |
| `--spacing-200` | `12.5em` | Layout / Spatial Grid Token |
| `--grey-dark` | `grey` | Canvas / Surface Token |
| `--plato-nav-blur` | `0.005em` | Layout / Spatial Grid Token |
| `--plato-nav-opacity` | `0.959856` | Layout / Spatial Grid Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--www-studioplato--bg` | `#4f4f4f` | Canvas Substrate (from `var(--grey-darkest)` in `:root`) |
| `--www-studioplato--ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-studioplato-co`)**:
   - Landmark `<header class="w-mod-js">` hosting `Studio Plato - Contemporary Interior` navigation (`Projects · Studio · Services · Insights · Instagram`), DOM attributes (`data-wf-domain="www.studioplato.co"`, `data-wf-page="6a27da652c4e1ce8d473b28a"`, `data-wf-site="69fc480c359115ee0044a0b6"`, `data-plato-home-guard`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<div.cursor_follower> — `T i n y A p a r t m e n t`)**:
   - Landmark `<div class="cursor_follower">` presenting display lead `T i n y A p a r t m e n t` and copy excerpt *"Contemporary interior design for successful living."* over `#4f4f4f` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.cursor_follower> — `Every space starts with a conversa`)**:
   - Landmark `<div class="cursor_follower">` rendering section `Every space starts with a conversation.` with copy *"I n t e r i o r d e s i g n p r o j e c t f o r a t i n y a p a r"*, asset references (`cdn.prod.website-files.com`, `studio-plato.webflow.shared.d6524...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `host { display:block;margin-left:auto;margin-right:auto;position:relative;z-ind... }`.
4. **Interactive Detail & Feature Matrix (<div.cursor_follower> — `I n t e r i o r d e s i g n p r o `)**:
   - Landmark `<div class="cursor_follower">` framing `I n t e r i o r d e s i g n p r o j e c t f o r ` and `Featured Projects —` (*"Featured Projects —"*) with `#007aff` surface cards, `#fff` accents, and `.swiper { display:block;list-style:none;margin-left:auto;margin-right:auto;overflo... }`.
5. **Colophon & Global Directory Footer (<footer.wf-instrumentsans-n3-active> — `https://www.studioplato.co/`)**:
   - Landmark `<footer class="wf-instrumentsans-n3-active">` anchoring `Studio Plato - Contemporary Inte` footer links (`Projects · Studio · Services · Insights · Instagram`), copy *"S t u d i o P l a t o"*, and `#0000` structural dividers.
