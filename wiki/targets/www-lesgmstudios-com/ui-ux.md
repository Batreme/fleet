# UI & UX Architecture: www-lesgmstudios-com

## Overview & Design Identity
- **Target**: `www-lesgmstudios-com` (**GM Studios — Du contenu qui dépasse les chiffres**)
- **Production URL**: [https://www.lesgmstudios.com/](https://www.lesgmstudios.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#0c0c0c` accent)
- **Summary**: Agence de contenu & studio d'enregistrement à Montréal. 1 milliard de vues générées pour nos clients.
- **Total Clean CSS Variables Extracted**: `62` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-clash), system-ui, sans-serif`
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--h2-size,clamp(38px, 5.1...`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-sm)`, `10.5px`)
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#070707` | `var(--color-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0c0c0c` | `var(--color-bg-page)` in `:root` |
| **Secondary / Muted Copy** | `#1d1d1d` | `var(--color-surface)` in `:root` |
| **Structural Hairline Border** | `#fff9` | `var(--color-text-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--font-clash` | `"clashDisplay", "clashDisplay Fallback"` | Typography / Scale Token |
| `--font-whisper` | `"Whisper", "Whisper Fallback"` | Typography / Scale Token |
| `--font-dm-sans` | `"DM Sans", "DM Sans Fallback"` | Typography / Scale Token |
| `--font-caveat` | `"Caveat", "Caveat Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-geist), system-ui, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `www-lesgmstudios-com`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `GM Studios — Du contenu qui dépasse ` navigation (`Accueil · Agence · Évènements · Cas clients · Équipe`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-transition-curtain="true"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Du contenu qui dé p asse les chiff`)**:
   - Landmark `<section class="fixed inset-x-0">` presenting display lead `Du contenu qui dé p asse les chiffres` and copy excerpt *"Selon plus de 450 clients satisfaits"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Clients & Partenaires`)**:
   - Landmark `<section class="relative w-full">` rendering section `Clients & Partenaires` with copy *"Studio de production à Montréal"*, asset references (`ClashDisplay_Bold-s.p.2nvxwaktzfx...`, `ClashDisplay_Medium-s.p.0olkjtjdv...`, `ClashDisplay_Regular-s.p.2qbs-i2c...`, `ClashDisplay_Semibold-s.p.082yiqt...`), and grid rule `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`.
4. **Interactive Detail & Feature Matrix (<section.noise-layer> — `Bienvenue`)**:
   - Landmark `<section class="noise-layer relative">` framing `Bienvenue` and `Nos services` (*"Du contenu qui dé p asse"*) with `#070707` surface cards, `#0c0c0c` accents, and `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.lesgmstudios.com/`)**:
   - Landmark `<footer class="relative flex">` anchoring `GM Studios — Du contenu qui dépa` footer links (`Accueil · Agence · Évènements · Cas clients · Équipe`), copy *"Nous transformons vos idées en contenus percutants qui capti"*, and `#fff9` structural dividers.
