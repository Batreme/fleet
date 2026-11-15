# UI & UX Architecture: www-3moons-it

## Overview & Design Identity
- **Target**: `www-3moons-it` (**3Moons Studio · App mobile, software enterprise e AI su misura**)
- **Production URL**: [https://www.3moons.it](https://www.3moons.it)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#060A14` canvas, `#F8FAFC` ink, `#A9A3B8` accent)
- **Summary**: Creiamo soluzioni software su misura per aziende e startup tecnologiche, dall’ideazione al prodotto finito: prototipi rapidi, costi conte...
- **Total Clean CSS Variables Extracted**: `17` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: "JetBrains Mono",ui-monospace,"SFMono-Regular",Consolas,monospace`; rule `h1` (`line-height: 0`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(24px,3.2vw,36px)`, `line-height: 1.2`, `letter-spacing: -.01em`, `font-weight: 700`)
- **Body Copy**: CSS variables `--font-body: "DM Sans","Segoe UI",system-ui,-apple-system,sans-serif`; rule `body` (`font-size: 16px`, `line-height: 1.65`)
- **Metadata & Labels**: CSS variables `--font-mono: "JetBrains Mono",ui-monospace,"SFMono-Regular",Consolas,monospace`; rule `small` (`font-size: 13px`, `letter-spacing: 0`, `font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#060A14` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#111112` | `var(--bg-alt)` in `:root` |
| **Elevated Surface / Card Substrate** | `#F8FAFC` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#A9A3B8` | `var(--muted)` in `:root` |
| **Secondary / Muted Copy** | `#7DB2FF` | `var(--cobalt)` in `:root` |
| **Structural Hairline Border** | `#2563EB` | `var(--primary)` in `:root` |
| **Variable Token (`--glow`)** | `#1E3A8A` | `var(--glow)` in `:root` |
| **Variable Token (`--sky`)** | `#4FCDF2` | `var(--sky)` in `:root` |
| **Variable Token (`--mustard`)** | `#FFCC00` | `var(--mustard)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#060A14` | Canvas / Surface Token |
| `--bg-alt` | `#111112` | Canvas / Surface Token |
| `--surface` | `rgba(255,255,255,.05)` | Canvas / Surface Token |
| `--ink` | `#F8FAFC` | Typography Ink Token |
| `--muted` | `#A9A3B8` | Color / Atmospheric Token |
| `--cobalt` | `#7DB2FF` | Color / Atmospheric Token |
| `--primary` | `#2563EB` | Brand / Palette Token |
| `--glow` | `#1E3A8A` | Color / Atmospheric Token |
| `--sky` | `#4FCDF2` | Color / Atmospheric Token |
| `--mustard` | `#FFCC00` | Color / Atmospheric Token |
| `--chip` | `rgba(255,255,255,.05)` | Color / Atmospheric Token |
| `--line` | `rgba(255,255,255,.10)` | Color / Atmospheric Token |
| `--font-display` | `"JetBrains Mono",ui-monospace,"SFMono-Regular",Consolas,monospace` | Typography / Scale Token |
| `--font-body` | `"DM Sans","Segoe UI",system-ui,-apple-system,sans-serif` | Typography / Scale Token |
| `--font-mono` | `"JetBrains Mono",ui-monospace,"SFMono-Regular",Consolas,monospace` | Typography / Scale Token |
| `--gutter` | `clamp(16px,4vw,40px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `www-3moons-it`)**:
   - Landmark `<header class="topbar">` hosting `3Moons Studio · App mobile, software` navigation (`Moonshot · Cross-platform · Enterprise · Pervasive AI · Team`), DOM attributes (`data-cert="guru"`, `data-cert="cssda"`, `data-cert="sotd"`, `data-endpoint="/app/ReceiveMessage"`), and stylesheet rule `html { scroll-behavior:smooth;scroll-padding-top:72px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Dal desiderio alla realizzazione`)**:
   - Landmark `<section class="hero">` presenting display lead `Dal desiderio alla realizzazione` and copy excerpt *"Creiamo soluzioni software su misura per aziende e startup tecnol"* over `#060A14` canvas and `#F8FAFC` ink.
3. **Primary Showcase & Content Grid (<section.panel> — `Qualità senza compromessi`)**:
   - Landmark `<section class="panel">` rendering section `Qualità senza compromessi` with copy *"Startup Engineering"*, asset references (`index_en.html`, `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `body::before { animation:none!important;transition:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.panel> — `Tecnologia allo stato dell’arte`)**:
   - Landmark `<section class="panel flip">` framing `Tecnologia allo stato dell’arte` and `La nuova frontiera dell’IT` (*"Fast Time-to-Value"*) with `#F8FAFC` surface cards, `#A9A3B8` accents, and `.mascot img { animation:float 6s ease-in-out infinite!important }`.
5. **Colophon & Global Directory Footer (<footer.topbar> — `https://www.3moons.it`)**:
   - Landmark `<footer class="topbar">` anchoring `3Moons Studio · App mobile, soft` footer links (`Moonshot · Cross-platform · Enterprise · Pervasive AI · Team`), copy *"Social Communities"*, and `#2563EB` structural dividers.
