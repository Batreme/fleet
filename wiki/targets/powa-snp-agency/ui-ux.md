# UI & UX Architecture: powa-snp-agency

## Overview & Design Identity
- **Target**: `powa-snp-agency` (**Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol...**)
- **Production URL**: [https://powa.snp.agency/](https://powa.snp.agency/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f4f2` canvas, `#000` ink, `#000` accent)
- **Summary**: Join POWA's campaign to stand against gender-based violence. Donate and create a symbol for women's equality. Together, we can make a dif...
- **Total Clean CSS Variables Extracted**: `92` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `__figtree_6417dc`
- **Body Font Stack**: `__figtree_Fallback_6417dc`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `15px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `15px`)
- **Body Copy**: rule `p` (`letter-spacing: -.02em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f4f2` | `var(--color-1)` in `:root` |
| **Primary Typography Ink** | `#b7b6b4` | `var(--color-4)` in `:root` |
| **Elevated Surface / Card Substrate** | `#404040` | `var(--color-5)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--black)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--white)` in `:root` |
| **Structural Hairline Border** | `#a133ff` | `var(--primary-purple)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gradient-position` | `0%!important` | Dimension / Scale Token |
| `--hsp` | `calc(14.12% * (1 - var(--gradient-val)) + 100% * var(--gradient-val))` | Dimension / Scale Token |
| `--color` | `hsl(0 0% var(--hsp)/1)` | Brand / Palette Token |
| `--p2` | `1` | Design System Custom Token |
| `--p3` | `1` | Design System Custom Token |
| `--content-position` | `none` | Design System Custom Token |
| `--card-width` | `max(26.25rem,294px)` | Layout / Spatial Grid Token |
| `--card-height` | `max(35rem,392px)` | Layout / Spatial Grid Token |
| `--in` | `0` | Design System Custom Token |
| `--scale-bg-image` | `calc(1 * (1 - var(--parallax)) + 1.08 * var(--parallax))` | Canvas / Surface Token |
| `--primary-font` | `"__figtree_6417dc","__figtree_Fallback_6417dc"` | Brand / Palette Token |
| `--vw-screen` | `360` | Layout / Spatial Grid Token |
| `--logo-size` | `max(2.5rem,28px)` | Layout / Spatial Grid Token |
| `--z-preloader` | `10` | Elevation / Border Token |
| `--z-cursor` | `9` | Elevation / Border Token |
| `--z-page-transition` | `8` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `powa-snp-agency`)**:
   - Landmark `<header class="lenis">` hosting `Donate to POWA & Stand for Women's E` navigation (`Get in touch · DONATE AND CREATE`), DOM attributes (`data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.Button_root__tsZ_o { position:relative;-webkit-user-select:none;-moz-user-select:none;user-se... }`.
2. **Hero Stage & Focal Lead (<section.Land_root__Wp6AW> — `CREATE + DONATE`)**:
   - Landmark `<section class="Land_root__Wp6AW Home_land__wexsp">` presenting display lead `CREATE + DONATE` and copy excerpt *"People Opposing Women Abuse People Opposing Women Abuse"* over `#f6f4f2` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.Intro_root__El5X_> — `together we can make a difference`)**:
   - Landmark `<section class="Intro_root__El5X_">` rendering section `together we can make a difference` with copy *"to fight the abuse against women"*, asset references (`pre_loader_1_1ff729f650.webp`, `pre_loader_2_ab07e72eb0.webp`, `pre_loader_3_518c8cc74b.webp`, `pre_loader_4_35a48a8bf5.webp`), and grid rule `.StyledButton_root___XGUu { display:inline-flex }`.
4. **Interactive Detail & Feature Matrix (<section.Intro_root__El5X_> — `to fight the abuse against women`)**:
   - Landmark `<section class="Intro_root__El5X_">` framing `to fight the abuse against women` and `A safe future for women won’t happen by itself. ` (*"A safe future for women won’t happen by itself. We have to design"*) with `#404040` surface cards, `#000` accents, and `.StyledButton_inner__p0jg2 { -webkit-user-select:none;-moz-user-select:none;user-select:none }`.
5. **Colophon & Global Directory Footer (<footer.Cursor_innerWrap__BCUuD> — `https://powa.snp.agency/`)**:
   - Landmark `<footer class="Cursor_innerWrap__BCUuD">` anchoring `Donate to POWA & Stand for Women` footer links (`Get in touch · DONATE AND CREATE`), copy *"to fight the abuse against women"*, and `#a133ff` structural dividers.
