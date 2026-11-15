# UI & UX Architecture: ieqtechnology-com

## Overview & Design Identity
- **Target**: `ieqtechnology-com` (**IEQ Technology · Innovation. Experience. Quality.**)
- **Production URL**: [https://ieqtechnology.com/](https://ieqtechnology.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#0d91d0` canvas, `#fff` ink, `#e1eff6` accent)
- **Summary**: Managed IT, legacy system modernization, custom software and custom websites from a 100% U.S.-based team in Springfield, Oregon. Since 2011.
- **Total Clean CSS Variables Extracted**: `51` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cabin`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Cabin","Geist",ui-sans-serif,system-ui,sans-serif`; rule `h1` (`font-size: 34px`, `letter-spacing: -.03em`)
- **Section Heading (`H2`)**: rule `.h2` (`font-size: clamp(40px,5vw,68px)`)
- **Body Copy**: rule `p` (`font-size: 15px`)
- **Metadata & Labels**: CSS variables `--font-mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace`; rule `small` (`font-size: 12px`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d91d0` | `var(--ieq-blue)` in `:root` |
| **Primary Typography Ink** | `#074a6a` | `var(--ieq-teal)` in `:root` |
| **Elevated Surface / Card Substrate** | `#003e71` | `var(--ieq-navy)` in `:root` |
| **Interactive Accent / Highlight** | `#e1eff6` | `var(--ieq-tint)` in `:root` |
| **Secondary / Muted Copy** | `#d5ebf6` | `var(--ieq-tint-2)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--bg)` in `:root` |
| **Variable Token (`--bg-2`)** | `#fafafa` | `var(--bg-2)` in `:root` |
| **Variable Token (`--bg-3`)** | `#f4f6f8` | `var(--bg-3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-display` | `"Cabin","Geist",ui-sans-serif,system-ui,sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace` | Typography / Scale Token |
| `--r-sm` | `6px` | Dimension / Scale Token |
| `--r-lg` | `16px` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(.2,.7,.1,1)` | Motion / Easing Token |
| `--max` | `1440px` | Dimension / Scale Token |
| `--nav-h` | `76px` | Layout / Spatial Grid Token |
| `--ieq-blue` | `#0d91d0` | Color / Atmospheric Token |
| `--ieq-teal` | `#074a6a` | Color / Atmospheric Token |
| `--ieq-navy` | `#003e71` | Layout / Spatial Grid Token |
| `--ieq-tint` | `#e1eff6` | Canvas / Surface Token |
| `--ieq-tint-2` | `#d5ebf6` | Canvas / Surface Token |
| `--bg` | `#fff` | Canvas / Surface Token |
| `--bg-2` | `#fafafa` | Canvas / Surface Token |
| `--bg-3` | `#f4f6f8` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `ieqtechnology-com`)**:
   - Landmark `<header class="nav">` hosting `IEQ Technology · Innovation. Experie` navigation (`About · Services · All services · Our Work · Awards`), DOM attributes (`data-theme="light"`, `data-k="nw"`, `data-k="ne"`, `data-k="sw"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `I nnovation. E xperience. Q uality`)**:
   - Landmark `<section class="hero">` presenting display lead `I nnovation. E xperience. Q uality. That's IEQ Te...` and copy excerpt *"Managed IT Monitoring, security & support"* over `#0d91d0` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.block> — `Four core services. One dedicated `)**:
   - Landmark `<section class="block">` rendering section `Four core services. One dedicated local team.` with copy *"Legacy Systems Modernize & integrate"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `sitemap.xml`), and grid rule `html { scroll-behavior:smooth;-webkit-text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.block> — `Managed IT Services`)**:
   - Landmark `<section class="block">` framing `Managed IT Services` and `Legacy Systems` (*"Custom Software Built for your exact needs"*) with `#003e71` surface cards, `#e1eff6` accents, and `svg { display:block }`.
5. **Colophon & Global Directory Footer (<footer.block> — `https://ieqtechnology.com/`)**:
   - Landmark `<footer class="block site-foot">` anchoring `IEQ Technology · Innovation. Exp` footer links (`About · Services · All services · Our Work · Awards`), copy *"Custom Websites Responsive · SEO"*, and `#fff` structural dividers.
