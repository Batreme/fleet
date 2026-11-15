# UI & UX Architecture: tigris-lorolabs-ai

## Overview & Design Identity
- **Target**: `tigris-lorolabs-ai` (**TIGRIS · Instinct, in Its Rarest Form**)
- **Production URL**: [https://tigris.lorolabs.ai/](https://tigris.lorolabs.ai/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#4a0e1a` / `#c9a24a`)
- **Summary**: Maison Tigris. Sculptural high jewellery in gold, rubies and diamonds. Discover the collection and explore a private viewing.
- **Total Clean CSS Variables Extracted**: `9` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bodoni Moda`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(.9rem,1.4vw,1.2rem)`, `1rem`, `.72rem`, `.7rem`, `clamp(2.6rem,7vw,6rem)`)
- **Section Heading (`H2`)**: rule `.section-title` (`font-size: clamp(2.6rem,7svh,5rem)`)
- **Body Copy**: rule `p` (`font-size: .75rem`, `letter-spacing: .22em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(.9rem,1.4vw,1.2rem)`, `1rem`, `.72rem`, `.7rem`, `clamp(2.6rem,7vw,6rem)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4a0e1a` | `var(--burgundy)` in `:root` |
| **Primary Typography Ink** | `#24060e` | `var(--oxblood)` in `:root` |
| **Elevated Surface / Card Substrate** | `#120309` | `var(--void)` in `:root` |
| **Interactive Accent / Highlight** | `#c9a24a` | `var(--gold)` in `:root` |
| **Secondary / Muted Copy** | `#f2d38a` | `var(--gold-hi)` in `:root` |
| **Structural Hairline Border** | `#9b1b30` | `var(--ruby)` in `:root` |
| **Variable Token (`--cream`)** | `#f5e9d6` | `var(--cream)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--burgundy` | `#4a0e1a` | Color / Atmospheric Token |
| `--oxblood` | `#24060e` | Color / Atmospheric Token |
| `--void` | `#120309` | Color / Atmospheric Token |
| `--gold` | `#c9a24a` | Color / Atmospheric Token |
| `--gold-hi` | `#f2d38a` | Color / Atmospheric Token |
| `--ruby` | `#9b1b30` | Color / Atmospheric Token |
| `--cream` | `#f5e9d6` | Color / Atmospheric Token |
| `--serif` | `"Bodoni Moda", "Didot", serif` | Typography / Scale Token |
| `--grot` | `"Space Grotesk", system-ui, sans-serif` | Dimension / Scale Token |
| `--tigris-lorolabs--bg` | `#4a0e1a` | Canvas Substrate (from `var(--burgundy)` in `:root`) |
| `--tigris-lorolabs--ink` | `#f2d38a` | Primary Typography Ink (stylesheet-derived) |
| `--tigris-lorolabs--surface` | `#120309` | Surface Substrate (stylesheet-derived) |
| `--tigris-lorolabs--accent` | `#c9a24a` | Interactive Accent (stylesheet-derived) |
| `--tigris-lorolabs--muted` | `#f2d38a` | Secondary Ink (stylesheet-derived) |
| `--tigris-lorolabs--border` | `#9b1b30` | Structural Border (stylesheet-derived) |
| `--tigris-lorolabs--container` | `20ch` | Container Bound (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `tigris-lorolabs-ai`)**:
   - Landmark `<header class="nav">` hosting `TIGRIS · Instinct, in Its Rarest For` navigation (`Collection · Heritage · Acquire`), DOM attributes (`data-hover`, `data-variant="gold"`, `data-variant="enamel"`, `data-variant="pave"`), and stylesheet rule `html { scrollbar-width:thin;scrollbar-color:var(--gold) var(--void);background:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `TIGRIS`)**:
   - Landmark `<section class="hero">` presenting display lead `TIGRIS` and copy excerpt *"Skip to the collection"* over `#4a0e1a` canvas and `#f2d38a` ink.
3. **Primary Showcase & Content Grid (<section.manifesto> — `The Stripes`)**:
   - Landmark `<section class="manifesto">` rendering section `The Stripes` with copy *"TIGRIS · Please enable JavaScript to enter the collection."*, asset references (`manifest.webmanifest`, `icon-192.png`, `bodoni-moda-latin-normal.woff2`, `space-grotesk-latin-normal.woff2`), and grid rule `html.lenis body { height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.stripes> — `Stripe`)**:
   - Landmark `<section class="stripes">` framing `Stripe` and `Stripe II` (*"Instinct, in its rarest form."*) with `#120309` surface cards, `#c9a24a` accents, and `.lenis.lenis-smooth { scroll-behavior:auto!important }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tigris.lorolabs.ai/`)**:
   - Landmark `<footer class="footer">` anchoring `TIGRIS · Instinct, in Its Rarest` footer links (`Collection · Heritage · Acquire`), copy *"Scroll to discover"*, and `#9b1b30` structural dividers.
