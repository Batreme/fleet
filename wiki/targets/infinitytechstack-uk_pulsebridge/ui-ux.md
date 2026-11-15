# UI & UX Architecture: infinitytechstack-uk_pulsebridge

## Overview & Design Identity
- **Target**: `infinitytechstack-uk_pulsebridge` (**PulseBridge [2026] · AI IDE Mobile Companion (Free)**)
- **Production URL**: [https://infinitytechstack.uk/pulsebridge](https://infinitytechstack.uk/pulsebridge)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#05060a` canvas, `#3df5c0` ink, `#ffc53d` accent)
- **Summary**: Free AI IDE mobile companion for Antigravity, Cursor & VS Code: stream live Win32 GDI screens, scroll code & inject prompts over Wi-Fi/4G...
- **Total Clean CSS Variables Extracted**: `157` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--font-home-display: "Space Grotesk","Space Grotesk Fallback"`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: clamp(1.15rem,4.8vw,1.4rem)!i...`, `line-height: 1.28!important`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: .95rem!important`, `line-height: 1.72!important`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#05060a` | `var(--pb-bg)` in `:root` |
| **Primary Typography Ink** | `#0b0e16` | `var(--pb-surface)` in `:root` |
| **Elevated Surface / Card Substrate** | `#10141f` | `var(--pb-surface-2)` in `:root` |
| **Interactive Accent / Highlight** | `#ffc53d` | `var(--pb-amber)` in `:root` |
| **Secondary / Muted Copy** | `#ff7a1a` | `var(--pb-ember)` in `:root` |
| **Structural Hairline Border** | `#3df5c0` | `var(--pb-signal)` in `:root` |
| **Variable Token (`--pb-indigo`)** | `#5b5bf0` | `var(--pb-indigo)` in `:root` |
| **Variable Token (`--pb-text`)** | `#f4f1ea` | `var(--pb-text)` in `:root` |
| **Variable Token (`--pb-muted`)** | `#98a1b3` | `var(--pb-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pb-bg` | `#05060a` | Canvas / Surface Token |
| `--pb-surface` | `#0b0e16` | Canvas / Surface Token |
| `--pb-surface-2` | `#10141f` | Canvas / Surface Token |
| `--pb-hair` | `rgba(255,255,255,0.06)` | Color / Atmospheric Token |
| `--pb-amber` | `#ffc53d` | Color / Atmospheric Token |
| `--pb-ember` | `#ff7a1a` | Color / Atmospheric Token |
| `--pb-amber-rgb` | `255,197,61` | Design System Custom Token |
| `--pb-signal` | `#3df5c0` | Color / Atmospheric Token |
| `--pb-signal-rgb` | `61,245,192` | Design System Custom Token |
| `--pb-indigo` | `#5b5bf0` | Color / Atmospheric Token |
| `--pb-indigo-rgb` | `91,91,240` | Design System Custom Token |
| `--pb-text` | `#f4f1ea` | Typography Ink Token |
| `--pb-muted` | `#98a1b3` | Color / Atmospheric Token |
| `--pb-ease` | `cubic-bezier(0.16,1,0.3,1)` | Motion / Easing Token |
| `--font-inter` | `"Inter","Inter Fallback"` | Typography / Scale Token |
| `--color-amber-300` | `oklch(87.9% .169 91.605)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pb-hero> — `infinitytechstack-uk_pulsebridge`)**:
   - Landmark `<header class="pb-hero">` hosting `PulseBridge [2026] · AI IDE Mobile C` navigation (`INFINITY · PropValuer Pro · Project SPINE · ChronoFact · About & Projects`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.pb-page:before { position:absolute;pointer-events:none;z-index:0 }`.
2. **Hero Stage & Focal Lead (<section.pb-simulator-section> — `Universal AI IDE Companion & Mobil`)**:
   - Landmark `<section class="pb-simulator-section">` presenting display lead `Universal AI IDE Companion & Mobile Telemetry Bridge` and copy excerpt *"Skip to main content"* over `#05060a` canvas and `#3df5c0` ink.
3. **Primary Showcase & Content Grid (<section.pb-captures-section> — `Experience the Live Mobile Compani`)**:
   - Landmark `<section class="pb-captures-section">` rendering section `Experience the Live Mobile Companion` with copy *"PULSEBRIDGE v2.0.0 · RUST AXUM 0.8 + REACT 19 + WIN32 GDI"*, asset references (`e4af272ccee01ff0-s.p.woff2`, `pulsebridge-live-preview.png`, `5f5eb15872b9862c.css`, `5770cea5f2af1200.css`), and grid rule `.pb-container { max-width:1240px;margin:0 auto;padding:0 1.5rem;position:relative;z-index:1 }`.
4. **Interactive Detail & Feature Matrix (<section.pb-architecture-section> — `Authentic Live Host Captures & Zer`)**:
   - Landmark `<section class="pb-architecture-section">` framing `Authentic Live Host Captures & Zero-Trust PWA` and `Engineered for Precision & Zero Latency` (*"Mobile Telemetry Bridge"*) with `#10141f` surface cards, `#ffc53d` accents, and `.pb-breadcrumb a { color:94a3b8;text-decoration:none;transition:color .2s ease }`.
5. **Colophon & Global Directory Footer (<footer.gnav-inner> — `https://infinitytechstack.uk/pulsebridge`)**:
   - Landmark `<footer class="gnav-inner">` anchoring `PulseBridge [2026] · AI IDE Mobi` footer links (`INFINITY · PropValuer Pro · Project SPINE · ChronoFact · About & Projects`), copy *"Real-time Win32 GDI screen streaming, touch-drag remote mous"*, and `#3df5c0` structural dividers.
