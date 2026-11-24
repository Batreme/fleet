---
title: "UI & UX Architecture: infinitytechstack-uk_pulsebridge"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: infinitytechstack-uk_pulsebridge

## Overview & Design Identity
- **Target**: `infinitytechstack-uk_pulsebridge` (**PulseBridge [2026] · AI IDE Mobile Companion (Free)**)
- **Production URL**: [https://infinitytechstack.uk/pulsebridge](https://infinitytechstack.uk/pulsebridge)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#06060c` canvas, `#f4f1ea` ink, `#00f0ff` accent)
- **Summary**: Free AI IDE mobile companion for Antigravity, Cursor & VS Code: stream live Win32 GDI screens, scroll code & inject prompts over Wi-Fi/4G...
- **Total Clean CSS Variables Extracted**: `174` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Grotesk`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 83.2px`, `line-height: 86.528px`, `font-weight: 800`, `letter-spacing: -3.744px`); CSS variables `--font-home-display: "Space Grotesk","Space Grotesk Fallback"`, `--font-aca-display: "Plus Jakarta Sans","Plus Jakarta Sans Fallback"`; rule `h1` (`font-size: clamp(32px,10vw,46px)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 41.6px`, `line-height: 62.4px`, `font-weight: 800`, `letter-spacing: -1.456px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`letter-spacing: -.02em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: .94rem`, `line-height: 1.68`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-home-mono: "JetBrains Mono","JetBrains Mono Fallback"`, `--c-mono: "SF Mono","Fira Code","JetBrains Mono","Cascadia Code",monospace`, `--font-aca-mono: "JetBrains Mono","JetBrains Mono Fallback"`; rule `small` (`font-size: .72rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#06060c` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f4f1ea` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a10` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00f0ff` | `.lp-secnav-btn--active { color: #00f0ff }` |
| **Secondary / Muted Copy** | `#7a7a9e` | `var(--text-secondary)` in `:root` |
| **Structural Hairline Border** | `#1e1e3a` | `var(--border)` in `:root` |
| **Variable Token (`--bg-secondary`)** | `#0c0c18` | `var(--bg-secondary)` in `:root` |
| **Variable Token (`--bg-card`)** | `#111127` | `var(--bg-card)` in `:root` |
| **Variable Token (`--bg-card-hover`)** | `#181840` | `var(--bg-card-hover)` in `:root` |
| **Variable Token (`--bg-hover`)** | `#1e1e48` | `var(--bg-hover)` in `:root` |
| **Variable Token (`--bg-input`)** | `#0e0e22` | `var(--bg-input)` in `:root` |
| **Variable Token (`--text-primary`)** | `#e4e4f0` | `var(--text-primary)` in `:root` |
| **Variable Token (`--text-muted`)** | `#4e4e6e` | `var(--text-muted)` in `:root` |
| **Variable Token (`--accent`)** | `#8b5cf6` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-light`)** | `#a78bfa` | `var(--accent-light)` in `:root` |
| **Variable Token (`--accent-dim`)** | `#6d40d9` | `var(--accent-dim)` in `:root` |
| **Variable Token (`--cyan`)** | `#22d3ee` | `var(--cyan)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg-primary` | `#06060c` | Canvas / Surface Token |
| `--bg-secondary` | `#0c0c18` | Canvas / Surface Token |
| `--bg-card` | `#111127` | Canvas / Surface Token |
| `--bg-card-hover` | `#181840` | Canvas / Surface Token |
| `--bg-hover` | `#1e1e48` | Canvas / Surface Token |
| `--bg-input` | `#0e0e22` | Canvas / Surface Token |
| `--text-primary` | `#e4e4f0` | Typography Ink Token |
| `--text-secondary` | `#7a7a9e` | Typography Ink Token |
| `--text-muted` | `#4e4e6e` | Typography Ink Token |
| `--accent` | `#8b5cf6` | Brand / Palette Token |
| `--accent-light` | `#a78bfa` | Canvas / Surface Token |
| `--accent-dim` | `#6d40d9` | Brand / Palette Token |
| `--accent-glow` | `#8b5cf640` | Brand / Palette Token |
| `--accent-glow-strong` | `#8b5cf680` | Brand / Palette Token |
| `--cyan` | `#22d3ee` | Color / Atmospheric Token |
| `--cyan-glow` | `#22d3ee33` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pb-hero> — `infinitytechstack-uk_pulsebridge`)**:
   - Landmark `<header class="pb-hero">` (`1192x947px`) hosting `PulseBridge [2026] · AI IDE Mobile C` navigation (`INFINITY · PropValuer Pro · Project SPINE · ChronoFact · About & Projects`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.pb-page:before { position:absolute;pointer-events:none;z-index:0 }`.
2. **Hero Stage & Focal Lead (<section.pb-simulator-section> — `Universal AI IDE Companion & Mobil`)**:
   - Landmark `<section class="pb-simulator-section">` presenting display lead `Universal AI IDE Companion & Mobile Telemetry Bridge` and copy excerpt *"Real-time Win32 GDI screen streaming, touch-drag remote mouse-whe"* over `#06060c` canvas and `#f4f1ea` ink.
3. **Primary Showcase & Content Grid (<section.pb-captures-section> — `Experience the Live Mobile Compani`)**:
   - Landmark `<section class="pb-captures-section">` rendering section `Experience the Live Mobile Companion` with copy *"PULSEBRIDGE v2.0.0 · RUST AXUM 0.8 + REACT 19 + WIN32 GDI"*, asset references (`e4af272ccee01ff0-s.p.woff2`, `pulsebridge-live-preview.png`, `5f5eb15872b9862c.css`, `5770cea5f2af1200.css`), and grid rule `.pb-container { max-width:1240px;margin:0 auto;padding:0 1.5rem;position:relative;z-index:1 }`.
4. **Interactive Detail & Feature Matrix (<section.pb-architecture-section> — `Authentic Live Host Captures & Zer`)**:
   - Landmark `<section class="pb-architecture-section">` framing `Authentic Live Host Captures & Zero-Trust PWA` and `Engineered for Precision & Zero Latency` (*"Mobile Telemetry Bridge"*) with `#0a0a10` surface cards, `#00f0ff` accents, and `.pb-breadcrumb a { color:94a3b8;text-decoration:none;transition:color .2s ease }`.
5. **Colophon & Global Directory Footer (<footer.gnav-inner> — `https://infinitytechstack.uk/pulsebridge`)**:
   - Landmark `<footer class="gnav-inner">` anchoring `PulseBridge [2026] · AI IDE Mobi` footer links (`INFINITY · PropValuer Pro · Project SPINE · ChronoFact · About & Projects`), copy *"Live Mobile Companion"*, and `#1e1e3a` structural dividers.
