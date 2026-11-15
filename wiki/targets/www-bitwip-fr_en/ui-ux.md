# UI & UX Architecture: www-bitwip-fr_en

## Overview & Design Identity
- **Target**: `www-bitwip-fr_en` (**Communications consulting agency for Overseas France · Bitwip**)
- **Production URL**: [https://www.bitwip.fr/en](https://www.bitwip.fr/en)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#FC622A` ink, `#FC622A` accent)
- **Summary**: Communications consulting agency in Overseas France and Occitanie: strategy, branding, web and campaigns. French Guiana, Martinique, Guad...
- **Total Clean CSS Variables Extracted**: `184` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cabinet Grotesk`
- **Body Font Stack**: `Clash Display`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: CSS variables `--t-h1: clamp(2.75rem,1.6rem + 4.6vw,6rem)`
- **Section Heading (`H2`)**: CSS variables `--t-h2: clamp(2.375rem,1.55rem + 3.4vw,5rem)`; rule `h2` (`font-size: var(--t-h3)`, `line-height: 1.12`, `letter-spacing: -.025em`, `font-weight: 500`)
- **Body Copy**: CSS variables `--t-body: clamp(1.0625rem,1rem + .2vw,1.1875rem)`; rule `p` (`font-size: clamp(1.625rem,.9rem + 1.6vw,...`, `line-height: 1.16`, `letter-spacing: -.03em`)
- **Metadata & Labels**: CSS variables `--f-label: "Clash Display","Cabinet Grotesk","Helvetica Neue",Arial,sans-serif`, `--t-small: .9375rem`, `--t-label: .75rem`; rule `.label` (`font-size: .6875rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--noir)` in `:root` |
| **Primary Typography Ink** | `#0B0B0B` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#141414` | `var(--ink-2)` in `:root` |
| **Interactive Accent / Highlight** | `#FC622A` | `var(--papaye)` in `:root` |
| **Secondary / Muted Copy** | `#EE5520` | `var(--papaye-titre)` in `:root` |
| **Structural Hairline Border** | `#B23C0B` | `var(--papaye-ink)` in `:root` |
| **Variable Token (`--papier`)** | `#F4EFE7` | `var(--papier)` in `:root` |
| **Variable Token (`--papier-2`)** | `#EAE3D8` | `var(--papier-2)` in `:root` |
| **Variable Token (`--blanc`)** | `#FFF` | `var(--blanc)` in `:root` |
| **Variable Token (`--encre`)** | `#121212` | `var(--encre)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--noir` | `#000` | Color / Atmospheric Token |
| `--ink` | `#0B0B0B` | Typography Ink Token |
| `--ink-2` | `#141414` | Typography Ink Token |
| `--papaye` | `#FC622A` | Color / Atmospheric Token |
| `--papaye-titre` | `#EE5520` | Color / Atmospheric Token |
| `--papaye-ink` | `#B23C0B` | Typography Ink Token |
| `--etoile-y` | `-.015em` | Dimension / Scale Token |
| `--etoile-h` | `.26em` | Dimension / Scale Token |
| `--etoile-w` | `.28em` | Dimension / Scale Token |
| `--papier` | `#F4EFE7` | Color / Atmospheric Token |
| `--papier-2` | `#EAE3D8` | Color / Atmospheric Token |
| `--blanc` | `#FFF` | Color / Atmospheric Token |
| `--encre` | `#121212` | Color / Atmospheric Token |
| `--txt` | `#FFF` | Color / Atmospheric Token |
| `--txt-2` | `rgba(255,255,255,.74)` | Color / Atmospheric Token |
| `--txt-3` | `rgba(255,255,255,.54)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `www-bitwip-fr_en`)**:
   - Landmark `<header class="nav nav--allegee">` hosting `Communications consulting agency for` navigation (`Services · All our services · Work · View all work · Culture & tourism`), DOM attributes (`data-gdifilm="direct"`, `data-page="accueil"`, `data-variante="allegee"`, `data-entree`), and stylesheet rule `root { --gc-x:0px }`.
2. **Hero Stage & Focal Lead (<section.hh> — `Bitwip, tech and creative communic`)**:
   - Landmark `<section class="hh mj">` presenting display lead `Bitwip, tech and creative communications agency T...` and copy excerpt *"Four disciplines, one team"* over `#000` canvas and `#FC622A` ink.
3. **Primary Showcase & Content Grid (<section.sec> — `We believe in meaningful communica`)**:
   - Landmark `<section class="sec papier">` rendering section `We believe in meaningful communication` with copy *"Strategy & consulting Give your communications a clear structure"*, asset references (`mesure.js`, `consentement.js`, `favicon-b-fond-noir.webp`, `CabinetGrotesk-900.woff2`), and grid rule `after { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Our services`)**:
   - Landmark `<section class="sec">` framing `Our services` and `Strategy & consulting` (*"Strategy & consulting"*) with `#141414` surface cards, `#FC622A` accents, and `html { -webkit-text-size-adjust:100%;text-size-adjust:100%;scroll-padding-top:1... }`.
5. **Colophon & Global Directory Footer (<footer.pied> — `https://www.bitwip.fr/en`)**:
   - Landmark `<footer class="pied">` anchoring `Communications consulting agency` footer links (`Services · All our services · Work · View all work · Culture & tourism`), copy *"Give your communications a clear structure"*, and `#B23C0B` structural dividers.
