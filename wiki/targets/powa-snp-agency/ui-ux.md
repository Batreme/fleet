---
title: "UI & UX Architecture: powa-snp-agency"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: powa-snp-agency

## Overview & Design Identity
- **Target**: `powa-snp-agency` (**Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol...**)
- **Production URL**: [https://powa.snp.agency/](https://powa.snp.agency/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f4f2` canvas, `#242424` ink, `#a133ff` accent)
- **Summary**: Join POWA's campaign to stand against gender-based violence. Donate and create a symbol for women's equality. Together, we can make a dif...
- **Total Clean CSS Variables Extracted**: `92` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `__figtree_6417dc`
- **Body Font Stack**: `__figtree_6417dc`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 131.25px`, `line-height: 105px`, `font-weight: 800`, `letter-spacing: -2.625px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 131.25px`, `line-height: 105px`, `font-weight: 800`, `letter-spacing: -2.625px`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 15px`, `font-weight: 400`); rule `p` (`letter-spacing: -.02em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 15px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f4f2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#242424` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.WaterfallImageAnimation_item__... { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#a133ff` | `var(--primary-purple)` in `:root` |
| **Secondary / Muted Copy** | `#adabaa` | `var(--secondary-grey)` in `:root` |
| **Structural Hairline Border** | `#acaba9` | `.StyledButton_preset-payment__z... { border: #acaba9 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vw-screen` | `360` | Layout / Spatial Grid Token |
| `--logo-size` | `max(2.5rem,28px)` | Layout / Spatial Grid Token |
| `--z-preloader` | `10` | Elevation / Border Token |
| `--z-cursor` | `9` | Elevation / Border Token |
| `--z-page-transition` | `8` | Motion / Easing Token |
| `--z-overflow` | `7` | Elevation / Border Token |
| `--z-banner` | `6` | Elevation / Border Token |
| `--z-modal` | `5` | Elevation / Border Token |
| `--z-header` | `4` | Layout / Spatial Grid Token |
| `--z-transition` | `3` | Motion / Easing Token |
| `--z-header-dropdown` | `2` | Layout / Spatial Grid Token |
| `--z-selectors` | `1` | Elevation / Border Token |
| `--gap-4` | `calc(4 / var(--vw-screen) * 100 * 1vw)` | Layout / Spatial Grid Token |
| `--gap-8` | `calc(8 / var(--vw-screen) * 100 * 1vw)` | Layout / Spatial Grid Token |
| `--gap-12` | `calc(12 / var(--vw-screen) * 100 * 1vw)` | Layout / Spatial Grid Token |
| `--gap-16` | `calc(16 / var(--vw-screen) * 100 * 1vw)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fonts-loaded> — `powa-snp-agency`)**:
   - Landmark `<header class="fonts-loaded">` (`1440px`) hosting `Donate to POWA & Stand for Women's E` navigation (`Get in touch · DONATE AND CREATE`), DOM attributes (`data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.__className_6417dc { font-family:__figtree_6417dc,__figtree_Fallback_6417dc }`.
2. **Hero Stage & Focal Lead (<section.Land_root__Wp6AW> — `CREATE + DONATE`)**:
   - Landmark `<section class="Land_root__Wp6AW Home_land__wexsp">` presenting display lead `CREATE + DONATE` and copy excerpt *"A safe future for women won’t happen by itself. We have to design"* over `#f6f4f2` canvas and `#242424` ink.
3. **Primary Showcase & Content Grid (<section.Intro_root__El5X_> — `together we can make a difference`)**:
   - Landmark `<section class="Intro_root__El5X_">` rendering section `together we can make a difference` with copy *"to fight the abuse against women"*, asset references (`light-apple-touch-icon.png`, `light-favicon-32x32.png`, `light-favicon-16x16.png`, `light-site.webmanifest`), and grid rule `.__variable_6417dc { --primary-font:"__figtree_6417dc","__figtree_Fallback_6417dc" }`.
4. **Interactive Detail & Feature Matrix (<section.Intro_root__El5X_:nth(2)> — `to fight the abuse against women`)**:
   - Landmark `<section class="Intro_root__El5X_">` framing `to fight the abuse against women` and `powa-snp-agency Archive & Directory` (*"together we can make a difference"*) with `#ffffff` surface cards, `#a133ff` accents, and `before { box-sizing:inherit }`.
5. **Colophon & Global Directory Footer (<footer.Cursor_innerWrap__BCUuD> — `https://powa.snp.agency/`)**:
   - Landmark `<footer class="Cursor_innerWrap__BCUuD">` anchoring `Donate to POWA & Stand for Women` footer links (`Get in touch · DONATE AND CREATE`), copy *"to fight the abuse against women"*, and `#acaba9` structural dividers.
