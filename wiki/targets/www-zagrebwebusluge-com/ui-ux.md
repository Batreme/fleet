# UI & UX Architecture: www-zagrebwebusluge-com

## Overview & Design Identity
- **Target**: `www-zagrebwebusluge-com` (**Web agencija i digitalna rješenja · Zagreb Web Usluge**)
- **Production URL**: [https://www.zagrebwebusluge.com/](https://www.zagrebwebusluge.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#08090d` / `#30323e`)
- **Summary**: Zagreb Web Usluge povezuje web dizajn, WordPress, web trgovine, SEO i sadržaj. Istražite usluge, proces i koncepte za svoj digitalni nastup.
- **Total Clean CSS Variables Extracted**: `84` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ZwuPoppins`
- **Body Font Stack**: `ZwuKarla`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: -.065em`)
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -.052em`)
- **Body Copy**: CSS variables `--zr-body: ZwuKarla,Arial,sans-serif`, `--co-body: clamp(15px, 1.12vw, 18px)`; rule `p` (`font-size: 1rem`)
- **Metadata & Labels**: CSS variables `--eu-metal: #c5b995`, `--co-caption: clamp(11px, .8vw, 13px)`, `--co-metal: #b9ab87`; rule `small` (`letter-spacing: 0`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#08090d` | `var(--zr-bg)` in `:root` |
| **Primary Typography Ink** | `#11131a` | `var(--zr-panel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#171923` | `var(--zr-panel-2)` in `:root` |
| **Interactive Accent / Highlight** | `#30323e` | `var(--zr-line)` in `:root` |
| **Secondary / Muted Copy** | `#eff0f6` | `var(--zr-text)` in `:root` |
| **Structural Hairline Border** | `#abb0c2` | `var(--zr-muted)` in `:root` |
| **Variable Token (`--zr-accent`)** | `#c9a6ff` | `var(--zr-accent)` in `:root` |
| **Variable Token (`--zr-accent-2`)** | `#ffb189` | `var(--zr-accent-2)` in `:root` |
| **Variable Token (`--zm-paper`)** | `#e9e5dc` | `var(--zm-paper)` in `:root` |
| **Variable Token (`--zm-ink`)** | `#090909` | `var(--zm-ink)` in `:root` |
| **Variable Token (`--zm-line`)** | `#48443e` | `var(--zm-line)` in `:root` |
| **Variable Token (`--hud-ink`)** | `#d1c2a0` | `var(--hud-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--zr-bg` | `#08090d` | Canvas / Surface Token |
| `--zr-panel` | `#11131a` | Color / Atmospheric Token |
| `--zr-panel-2` | `#171923` | Color / Atmospheric Token |
| `--zr-line` | `#30323e` | Color / Atmospheric Token |
| `--zr-text` | `#eff0f6` | Typography Ink Token |
| `--zr-muted` | `#abb0c2` | Color / Atmospheric Token |
| `--zr-accent` | `#c9a6ff` | Brand / Palette Token |
| `--zr-accent-2` | `#ffb189` | Brand / Palette Token |
| `--zr-head` | `ZwuPoppins,Arial,sans-serif` | Design System Custom Token |
| `--zr-body` | `ZwuKarla,Arial,sans-serif` | Design System Custom Token |
| `--zm-paper` | `#e9e5dc` | Canvas / Surface Token |
| `--zm-ink` | `#090909` | Typography Ink Token |
| `--zm-line` | `#48443e` | Color / Atmospheric Token |
| `--hud-ink` | `#d1c2a0` | Typography Ink Token |
| `--mist-x` | `62%` | Dimension / Scale Token |
| `--mist-y` | `-95%` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.zm-header> — `www-zagrebwebusluge-com`)**:
   - Landmark `<header class="zm-header zwu-header">` hosting `Web agencija i digitalna rješenja · ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hero-intro-mode="signature"`, `data-hero-intro="fallback"`, `data-zwu-style-bundle="1"`, `data-wp-strategy="defer"`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.wp-block-group> — `Web stranice koje nose vaš potpis.`)**:
   - Landmark `<section class="wp-block-group zm-hero">` presenting display lead `Web stranice koje nose vaš potpis.` and copy excerpt *"Preskoči na sadržaj"* over `#08090d` canvas and `#eff0f6` ink.
3. **Primary Showcase & Content Grid (<section.wp-block-group> — `Povjerenje i pristup`)**:
   - Landmark `<section class="wp-block-group zm-partners">` rendering section `Povjerenje i pristup` with copy *"01 Mogućnosti Usluge U U s s l l u u g g e e"*, asset references (`site-icon-32-v150.png`, `hero-mobile-wide-941-v150b.avif`, `hero-mobile-mid-941-v150b.avif`, `hero-mobile-941-v143b.avif`), and grid rule `body.zr-site { margin:0;background:var(--zr-bg);color:var(--zr-text);font:400 18px/1.6... }`.
4. **Interactive Detail & Feature Matrix (<section.wp-block-group> — `Jasna strategija`)**:
   - Landmark `<section class="wp-block-group zm-services">` framing `Jasna strategija` and `Autorski dizajn` (*"Mogućnosti Usluge U U s s l l u u g g e e"*) with `#171923` surface cards, `#30323e` accents, and `body.zr-site a { color:inherit;text-decoration:none }`.
5. **Colophon & Global Directory Footer (<footer.zwu-footer> — `https://www.zagrebwebusluge.com/`)**:
   - Landmark `<footer class="zwu-footer zm-footer">` anchoring `Web agencija i digitalna rješenj` footer links (`Overview · Index · Archive · About · Contact`), copy *"U U s s l l u u g g e e"*, and `#abb0c2` structural dividers.
