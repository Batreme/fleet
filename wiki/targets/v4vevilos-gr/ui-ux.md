# UI & UX Architecture: v4vevilos-gr

## Overview & Design Identity
- **Target**: `v4vevilos-gr` (**Βέβηλος • Once dead twice alive**)
- **Production URL**: [https://v4vevilos.gr](https://v4vevilos.gr)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#050507` / `#ffffff`)
- **Summary**: Επίσημο hub του Βέβηλου • μουσική, live, δισκογραφία & σύνδεσμοι σε ένα σημείο.
- **Total Clean CSS Variables Extracted**: `27` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Advent Pro`
- **Body Font Stack**: `Bebas Neue`
- **Monospace / Technical Font Stack**: `Fira Sans Extra Condensed`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Bebas Neue", "Fira Sans Extra Condensed", "Arial Narrow", sans-serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.72rem`, `1.05rem`, `.78rem`, `clamp(2rem,4vw,2.6rem)`, `.9rem`)
- **Body Copy**: CSS variables `--font-body: "Advent Pro", sans-serif`; rule `p` (`font-size: .98rem`)
- **Metadata & Labels**: rule `small` (`font-size: .55em`, `font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#050507` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#ff3e3e` | `var(--accent)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff6a00` | `var(--accent-fire)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `var(--text)` in `:root` |
| **Secondary / Muted Copy** | `#050506` | `var(--pl-bg)` in `:root` |
| **Structural Hairline Border** | `#060405` | `var(--gig-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#050507` | Canvas / Surface Token |
| `--bg-soft` | `rgba(255,255,255,.02)` | Canvas / Surface Token |
| `--card-bg` | `rgba(255,255,255,.035)` | Canvas / Surface Token |
| `--card-bg-strong` | `rgba(255,255,255,.05)` | Canvas / Surface Token |
| `--border` | `rgba(255,255,255,.09)` | Elevation / Border Token |
| `--border-strong` | `rgba(255,62,62,.22)` | Elevation / Border Token |
| `--accent` | `#ff3e3e` | Brand / Palette Token |
| `--accent-fire` | `#ff6a00` | Brand / Palette Token |
| `--text` | `#ffffff` | Typography Ink Token |
| `--text-muted` | `rgba(255,255,255,.68)` | Typography Ink Token |
| `--text-soft` | `rgba(255,255,255,.45)` | Typography Ink Token |
| `--glass` | `blur(18px) saturate(155%)` | Dimension / Scale Token |
| `--radius-xl` | `32px` | Elevation / Border Token |
| `--radius-lg` | `22px` | Elevation / Border Token |
| `--radius-md` | `16px` | Elevation / Border Token |
| `--font-display` | `"Bebas Neue", "Fira Sans Extra Condensed", "Arial Narrow", sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `v4vevilos-gr`)**:
   - Landmark `<header class="topbar reveal">` hosting `Βέβηλος • Once dead twice alive` navigation (`EL · EN`), DOM attributes (`data-ga-id="G-KS1TX8NEVW"`, `data-consent="granted"`, `data-consent="denied"`, `data-zap="Βέβηλος·Vevilos·V4"`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.vv-consent> — `Βέβηλος Β έ β η λ ο ς`)**:
   - Landmark `<section class="vv-consent">` presenting display lead `Βέβηλος Β έ β η λ ο ς` and copy excerpt *"Μετάβαση στο περιεχόμενο"* over `#050507` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Νεκρή Ζώνη V`)**:
   - Landmark `<section class="hero">` rendering section `Νεκρή Ζώνη V` with copy *"Google Analytics · μόνο analytics, όχι marketing"*, asset references (`favicon.ico`, `apple-touch-icon.png`, `advent-pro-100-700-greek.woff2`, `advent-pro-100-700-latin.woff2`), and grid rule `body { overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<section.gig-banner> — `Η επόμενη σελίδα γράφεται και από `)**:
   - Landmark `<section class="gig-banner hero-gig">` framing `Η επόμενη σελίδα γράφεται και από σένα.` and `The Manifesto` (*"Χρησιμοποιούμε το Google Analytics για να καταλάβουμε πώς χρησιμο"*) with `#ff6a00` surface cards, `#ffffff` accents, and `img { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.vv-consent> — `https://v4vevilos.gr`)**:
   - Landmark `<footer class="vv-consent">` anchoring `Βέβηλος • Once dead twice alive` footer links (`EL · EN`), copy *"Once dead Twice alive"*, and `#060405` structural dividers.
