# UI & UX Architecture: lifetimepastapass-com

## Overview & Design Identity
- **Target**: `lifetimepastapass-com` (**LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY**)
- **Production URL**: [https://lifetimepastapass.com](https://lifetimepastapass.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#ff2079`)
- **Summary**: Braden is an Olive Garden Lifetime Pasta Pass holder. Now the internet votes on what he eats next. Live results, vote history, and the fu...
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `VT323`
- **Body Font Stack**: `monospace)`
- **Monospace / Technical Font Stack**: `monospace)`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `19px`, `0.9rem`, `0.65rem`, `12px`, `0.5rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.1rem`)
- **Body Copy**: CSS variables `--body-font: 'VT323', monospace`; rule `body` (`font-size: 19px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `19px`, `0.9rem`, `0.65rem`, `12px`, `0.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#141414` | `var(--bg-panel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#39ff14` | `var(--neon-green)` in `:root` |
| **Interactive Accent / Highlight** | `#ff2079` | `var(--neon-pink)` in `:root` |
| **Secondary / Muted Copy** | `#ffe900` | `var(--neon-yellow)` in `:root` |
| **Structural Hairline Border** | `#00e5ff` | `var(--neon-cyan)` in `:root` |
| **Variable Token (`--white`)** | `#f5f5f5` | `var(--white)` in `:root` |
| **Variable Token (`--trophy-bronze`)** | `#d98a3d` | `var(--trophy-bronze)` in `:root` |
| **Variable Token (`--trophy-silver`)** | `#d8d8e2` | `var(--trophy-silver)` in `:root` |
| **Variable Token (`--trophy-gold`)** | `#ffd700` | `var(--trophy-gold)` in `:root` |
| **Variable Token (`--bada-bing`)** | `#ff7a3d` | `var(--bada-bing)` in `:root` |
| **Variable Token (`--bada-boom`)** | `#ff2b1f` | `var(--bada-boom)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0a0a0a` | Canvas / Surface Token |
| `--bg-panel` | `#141414` | Canvas / Surface Token |
| `--neon-green` | `#39ff14` | Color / Atmospheric Token |
| `--neon-pink` | `#ff2079` | Typography Ink Token |
| `--neon-yellow` | `#ffe900` | Color / Atmospheric Token |
| `--neon-cyan` | `#00e5ff` | Color / Atmospheric Token |
| `--white` | `#f5f5f5` | Canvas / Surface Token |
| `--pixel-font` | `'Press Start 2P', monospace` | Typography / Scale Token |
| `--body-font` | `'VT323', monospace` | Typography / Scale Token |
| `--trophy-bronze` | `#d98a3d` | Color / Atmospheric Token |
| `--trophy-silver` | `#d8d8e2` | Color / Atmospheric Token |
| `--trophy-gold` | `#ffd700` | Color / Atmospheric Token |
| `--bada-bing` | `#ff7a3d` | Color / Atmospheric Token |
| `--bada-boom` | `#ff2b1f` | Color / Atmospheric Token |
| `--lifetimepastapas-bg` | `#0a0a0a` | Canvas Substrate (from `var(--bg)` in `:root`) |
| `--lifetimepastapas-ink` | `#ffe900` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `lifetimepastapass-com`)**:
   - Landmark `<header class="site-header">` hosting `LIFETIME PASTA PASS · BRADEN'S INFIN` navigation (`Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`), DOM attributes (`data-address="braden@lifetimepastap..."`, `data-track="mailapp"`, `data-category="Pasta"`, `data-category="Pasta"`), and stylesheet rule `h3 { font-family: var(--pixel-font); text-transform: uppercase; letter-spacin... }`.
2. **Hero Stage & Focal Lead (<section.poll-section> — `Vote on what a LIFETIME PASTA PASS`)**:
   - Landmark `<section class="poll-section">` presenting display lead `Vote on what a LIFETIME PASTA PASS holder eats next` and copy excerpt *"BRADEN'S INFINITE TOUR OF ITALY"* over `#0a0a0a` canvas and `#ffe900` ink.
3. **Primary Showcase & Content Grid (<section.visits-section> — `Pasta`)**:
   - Landmark `<section class="visits-section">` rendering section `Pasta` with copy *"12:06 PM EST Spaghetti + Spicy Alfredo + Meat Sauce + Italian Sau"*, asset references (`fonts.googleapis.com`, `css2`, `style.css`, `card.png (Lifetime Pasta Pass card)`), and grid rule `.site-header { position: sticky; top: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.visits-section> — `Sauce`)**:
   - Landmark `<section class="visits-section">` framing `Sauce` and `Second Sauce` (*"11:45 AM EST Spaghetti + Creamy Mushroom + Five Cheese Marinara +"*) with `#39ff14` surface cards, `#ff2079` accents, and `.site-nav.open { right: 0; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://lifetimepastapass.com`)**:
   - Landmark `<footer class="site-footer">` anchoring `LIFETIME PASTA PASS · BRADEN'S I` footer links (`Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`), copy *"Connecticut, United States"*, and `#00e5ff` structural dividers.
