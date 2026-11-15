# UI & UX Architecture: sinedogma-com-tr

## Overview & Design Identity
- **Target**: `sinedogma-com-tr` (**sinedogma**)
- **Production URL**: [https://sinedogma.com.tr/](https://sinedogma.com.tr/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#d9d9d9` accent)
- **Summary**: sinedogma ve dogma yayın: dijital arşiv, dergiler, kitaplar, haberler ve satış noktaları.
- **Total Clean CSS Variables Extracted**: `201` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EB Garamond Local`
- **Body Font Stack**: `Garamond`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 15px`)
- **Metadata & Labels**: rule `small` (`font-size: .72rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#111` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6f6f6f` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#d9d9d9` | `var(--line)` in `:root` |
| **Secondary / Muted Copy** | `#f5f5f3` | `var(--soft)` in `:root` |
| **Structural Hairline Border** | `#000` | `var(--w2w-start-background-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#fff` | Canvas / Surface Token |
| `--ink` | `#111` | Typography Ink Token |
| `--muted` | `#6f6f6f` | Color / Atmospheric Token |
| `--line` | `#d9d9d9` | Color / Atmospheric Token |
| `--soft` | `#f5f5f3` | Color / Atmospheric Token |
| `--max` | `1080px` | Dimension / Scale Token |
| `--reading` | `680px` | Dimension / Scale Token |
| `--motion-fast` | `160ms` | Motion / Easing Token |
| `--motion-base` | `220ms` | Motion / Easing Token |
| `--motion-slow` | `300ms` | Motion / Easing Token |
| `--motion-ease` | `cubic-bezier(.22,.61,.36,1)` | Motion / Easing Token |
| `--mobile-gutter` | `16px` | Layout / Spatial Grid Token |
| `--mobile-radius` | `0px` | Elevation / Border Token |
| `--circulation-progress` | `0` | Design System Custom Token |
| `--garamond-tracking` | `0em` | Typography / Scale Token |
| `--garamond-heading-tracking` | `-0.025em` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `sinedogma-com-tr`)**:
   - Landmark `<header class="site-header">` hosting `sinedogma` navigation (`haberler · satış noktaları · hakkımızda`), DOM attributes (`data-path="/"`, `data-path="/haberler"`, `data-path="/satis-noktalari"`, `data-path="/hakkimizda"`), and stylesheet rule `root { --paper: fff; --ink: 111; --muted: 6f6f6f; --line: d9d9d9; --soft: f5f5f3; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `iki yayın tek dolaşım`)**:
   - Landmark `<section class="hero shell">` presenting display lead `iki yayın tek dolaşım` and copy excerpt *"yazı gönder / kitap dosyası gönder yazı / kitap gönder"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.section> — `sinedogma dijital arşiv`)**:
   - Landmark `<section class="section shell">` rendering section `sinedogma dijital arşiv` with copy *"yazı gönder / kitap dosyası gönder"*, asset references (`EBGaramond-VariableFont_wght.woff2`, `favicon-32x32.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `html { scroll-behavior: smooth; }`.
4. **Interactive Detail & Feature Matrix (<article.article-card> — `“bu ben değilim” yönetmenleri ile `)**:
   - Landmark `<article class="article-card">` framing `“bu ben değilim” yönetmenleri ile bir söyleşi` and `+1 belgesel: jim’le tanışmak "kısa incelemesi"` (*"yazı / kitap gönder"*) with `#6f6f6f` surface cards, `#d9d9d9` accents, and `input { font: inherit; text-transform: lowercase; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://sinedogma.com.tr/`)**:
   - Landmark `<footer class="site-footer">` anchoring `sinedogma` footer links (`haberler · satış noktaları · hakkımızda`), copy *"sinedogma · güz 2026 güz 2026 beş sayı antoloji koleksiyonu "*, and `#000` structural dividers.
