# UI & UX Architecture: legacybridge-software

## Overview & Design Identity
- **Target**: `legacybridge-software` (**AI Document Entry for AS/400 & Legacy Systems · LegacyBridge**)
- **Production URL**: [https://legacybridge.software/](https://legacybridge.software/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#082a1c` canvas, `#ffffff` ink, `#94a3b8` accent)
- **Summary**: An AI agent that reads invoices, orders and claims and keys them into AS/400 (IBM i), mainframe and other legacy systems. Human approval,...
- **Total Clean CSS Variables Extracted**: `46` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: rule `.h1` (`letter-spacing: -0.05em`)
- **Section Heading (`H2`)**: rule `.h2` (`letter-spacing: -0.04em`)
- **Body Copy**: rule `body` (`letter-spacing: -0.04em`)
- **Metadata & Labels**: CSS variables `--mono: "Geist Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace`; rule `.caption` (`letter-spacing: -0.04em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#082a1c` | `var(--text-ink)` in `:root` |
| **Primary Typography Ink** | `#64707a` | `var(--text-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--text-inverse)` in `:root` |
| **Interactive Accent / Highlight** | `#94a3b8` | `var(--text-inverse-muted)` in `:root` |
| **Secondary / Muted Copy** | `#cdff8c` | `var(--brand-accent)` in `:root` |
| **Structural Hairline Border** | `#f4f7f9` | `var(--surface-card)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ring-m` | `max(16px, calc(50vw - 704px))` | Elevation / Border Token |
| `--rot-h` | `58px` | Dimension / Scale Token |
| `--rot-step` | `88px` | Dimension / Scale Token |
| `--rot-nudge` | `-2px` | Dimension / Scale Token |
| `--rise` | `110px` | Dimension / Scale Token |
| `--rise-ease` | `cubic-bezier(0, 1, 0.4, 1)` | Motion / Easing Token |
| `--text-ink` | `#082a1c` | Typography Ink Token |
| `--text-muted` | `#64707a` | Typography Ink Token |
| `--text-inverse` | `#ffffff` | Typography Ink Token |
| `--text-inverse-muted` | `#94a3b8` | Typography Ink Token |
| `--brand-primary` | `#082a1c` | Brand / Palette Token |
| `--brand-secondary` | `#94a3b8` | Brand / Palette Token |
| `--brand-accent` | `#cdff8c` | Brand / Palette Token |
| `--surface-white` | `#ffffff` | Canvas / Surface Token |
| `--surface-page` | `#ffffff` | Canvas / Surface Token |
| `--surface-card` | `#f4f7f9` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `legacybridge-software`)**:
   - Landmark `<header class="site-header">` hosting `AI Document Entry for AS/400 & Legac` navigation (`How it works · Solutions · Use cases · Blog · Why us`), DOM attributes (`data-lb-cta="header"`, `data-label="Book a demo"`, `data-label="Book"`, `data-contact-open="header"`), and stylesheet rule `.announce.is-tucked { transform: translateY(-100%); }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Stop retyping invoices, claims and`)**:
   - Landmark `<section class="hero">` presenting display lead `Stop retyping invoices, claims and orders into AS...` and copy excerpt *"legacy bridge is now part of scandiweb"* over `#082a1c` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.compare-cards> — `Your AS/400 (IBM i) system is not `)**:
   - Landmark `<section class="compare-cards">` rendering section `Your AS/400 (IBM i) system is not the problem. Th...` with copy *"Read the announcement Read more"*, asset references (`favicon.svg`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `.announce { transition: none; }`.
4. **Interactive Detail & Feature Matrix (<article.compare-cards__card> — `Hours of processing & typing`)**:
   - Landmark `<article class="compare-cards__card compare-cards__card--without">` framing `Hours of processing & typing` and `Seconds to approve` (*"Read the announcement"*) with `#ffffff` surface cards, `#94a3b8` accents, and `.announce.is-hidden { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://legacybridge.software/`)**:
   - Landmark `<footer class="site-footer is-offscreen">` anchoring `AI Document Entry for AS/400 & L` footer links (`How it works · Solutions · Use cases · Blog · Why us`), copy *"Document entry automation for AS/400 (IBM i)"*, and `#f4f7f9` structural dividers.
