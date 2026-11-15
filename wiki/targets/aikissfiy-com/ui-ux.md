# UI & UX Architecture: aikissfiy-com

## Overview & Design Identity
- **Target**: `aikissfiy-com` (**Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy**)
- **Production URL**: [https://aikissfiy.com](https://aikissfiy.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0f172a` ink, `#64748b` accent)
- **Summary**: Description: AIKissfiy creates realistic AI kissing videos from your photos. Choose different kiss styles, keep faces recognizable, and e...
- **Total Clean CSS Variables Extracted**: `441` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Plus Jakarta Sans`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em!important`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`line-height: 1.33`, `font-weight: 600`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--ak-font-size-base: 14px`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--aikiss-surface-solid)` in `:root` |
| **Primary Typography Ink** | `#0f172a` | `var(--aikiss-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#475569` | `var(--aikiss-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#64748b` | `var(--aikiss-soft-muted)` in `:root` |
| **Secondary / Muted Copy** | `#6c63ff` | `var(--halo-border-fallback)` in `:root` |
| **Structural Hairline Border** | `#ffdce5` | `var(--hologram-pink)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#8b81ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#b941ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#ec4899` | `var(--gradient-primary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `Inter,system-ui,sans-serif` | Typography / Scale Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--aikiss-section-bg` | `transparent` | Canvas / Surface Token |
| `--aikiss-surface-solid` | `#fff` | Canvas / Surface Token |
| `--aikiss-surface-muted` | `rgba(248,250,252,.82)` | Canvas / Surface Token |
| `--aikiss-border` | `rgba(99,102,241,.2)` | Elevation / Border Token |
| `--aikiss-border-strong` | `rgba(99,102,241,.34)` | Elevation / Border Token |
| `--aikiss-text` | `#0f172a` | Typography Ink Token |
| `--aikiss-muted` | `#475569` | Color / Atmospheric Token |
| `--aikiss-soft-muted` | `#64748b` | Color / Atmospheric Token |
| `--aikiss-glow-primary` | `rgba(108,99,255,.2)` | Brand / Palette Token |
| `--aikiss-glow-secondary` | `rgba(236,72,153,.14)` | Brand / Palette Token |
| `--gradient-primary` | `linear-gradient(135deg,#6c63ff,#8b81ff 30%,#b941ff 66%,#ec4899)` | Brand / Palette Token |
| `--aikiss-inner-highlight` | `hsla(0,0%,100%,.78)` | Canvas / Surface Token |
| `--aikiss-shadow` | `0 24px 60px rgba(15,23,42,.1)` | Elevation / Border Token |
| `--aikiss-tool-shell` | `hsla(0,0%,100%,.58)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navigate-new> — `aikissfiy-com`)**:
   - Landmark `<header class="navigate-new sticky">` hosting `Free AI Kissing Video Generator: Cre` navigation (`Home · Nano Banana Pro · AI Effects`), DOM attributes (`data-hid="page-structured-data"`, `data-gtag`, `data-v-8a6150fd`, `data-v-a6b3f275`), and stylesheet rule `before { border:1px solid hsla(0,0%,100%,.68);border-radius:27px;content:"";inset... }`.
2. **Hero Stage & Focal Lead (<section.flex> — `Free AI Kissing Video Generator`)**:
   - Landmark `<section class="flex flex-col">` presenting display lead `Free AI Kissing Video Generator` and copy excerpt *"AI Kissing Generator"* over `#fff` canvas and `#0f172a` ink.
3. **Primary Showcase & Content Grid (<section.flex> — `Realistic`)**:
   - Landmark `<section class="flex flex-col">` rendering section `Realistic` with copy *"Love Compatibility"*, asset references (`cdn.aikissfiy.com`, `entry.D5yMvS4u.css`, `OverlayScrollbar.CrLIJdLh.css`, `LanguageSwitch.BsPr10ru.css`), and grid rule `webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Diverse`)**:
   - Landmark `<section class="flex flex-col">` framing `Diverse` and `Fast` (*"AI Character Generator"*) with `#475569` surface cards, `#64748b` accents, and `body { line-height:inherit;margin:0 }`.
5. **Colophon & Global Directory Footer (<footer.w-full> — `https://aikissfiy.com`)**:
   - Landmark `<footer class="w-full border-t">` anchoring `Free AI Kissing Video Generator:` footer links (`Home · Nano Banana Pro · AI Effects`), copy *"AI Kissing Generator Hot"*, and `#ffdce5` structural dividers.
