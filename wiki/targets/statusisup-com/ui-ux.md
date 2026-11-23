---
title: "UI & UX Architecture: statusisup-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: statusisup-com

## Overview & Design Identity
- **Target**: `statusisup-com` (**Status Is UP — Index für Service-Uptime, Performance & Zuverlässigkeit**)
- **Production URL**: [https://statusisup.com/](https://statusisup.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f3ea` canvas, `#111d2f` ink, `#f2a30f` accent)
- **Summary**: Entdecken Sie Dienste mit geringer beobachteter Ausfallaktivität über einen quellverknüpften Index für Service-Uptime, Performance und Zu...
- **Total Clean CSS Variables Extracted**: `153` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo Black`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 158.4px`, `line-height: 131.472px`, `font-weight: 400`, `letter-spacing: -13.464px`); CSS variables `--siu-display: "Archivo Black",sans-serif`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`; rule `h1` (`letter-spacing: -.075em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 74.88px`, `line-height: 65.8944px`, `font-weight: 400`, `letter-spacing: -4.8672px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`letter-spacing: -.065em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--siu-body: "Manrope",sans-serif`, `--text-base: 1rem`, `--text-base--line-height: 1.5`; rule `p` (`font-size: .76rem`, `line-height: 1.65`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--siu-label: "DM Mono",ui-monospace,monospace`, `--siu-label-size: .62rem`, `--siu-label-line: 1.35`; rule `small` (`letter-spacing: .09em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f3ea` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111d2f` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fffef8` | `var(--card)` in `:root` |
| **Interactive Accent / Highlight** | `#f2a30f` | `.rating-stars button.is-selected { color: #f2a30f }` |
| **Secondary / Muted Copy** | `#8f9a91` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cbd3c9` | `var(--border)` in `:root` |
| **Variable Token (`--primary`)** | `#14b65b` | `var(--primary)` in `:root` |
| **Variable Token (`--primary-foreground`)** | `#112235` | `var(--primary-foreground)` in `:root` |
| **Variable Token (`--secondary`)** | `#e6ece5` | `var(--secondary)` in `:root` |
| **Variable Token (`--muted`)** | `#e9e9e1` | `var(--muted)` in `:root` |
| **Variable Token (`--muted-foreground`)** | `#526073` | `var(--muted-foreground)` in `:root` |
| **Variable Token (`--accent`)** | `#c7f42b` | `var(--accent)` in `:root` |
| **Variable Token (`--destructive`)** | `#dc4d42` | `var(--destructive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--radius` | `.5rem` | Elevation / Border Token |
| `--background` | `#f5f3ea` | Canvas / Surface Token |
| `--foreground` | `#111d2f` | Typography Ink Token |
| `--card` | `#fffef8` | Color / Atmospheric Token |
| `--card-foreground` | `#111d2f` | Typography Ink Token |
| `--popover` | `#fffef8` | Color / Atmospheric Token |
| `--popover-foreground` | `#111d2f` | Typography Ink Token |
| `--primary` | `#14b65b` | Brand / Palette Token |
| `--primary-foreground` | `#112235` | Typography Ink Token |
| `--secondary` | `#e6ece5` | Brand / Palette Token |
| `--secondary-foreground` | `#112235` | Typography Ink Token |
| `--muted` | `#e9e9e1` | Color / Atmospheric Token |
| `--muted-foreground` | `#526073` | Typography Ink Token |
| `--accent` | `#c7f42b` | Brand / Palette Token |
| `--accent-foreground` | `#112235` | Typography Ink Token |
| `--destructive` | `#dc4d42` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.siu-site-header> — `statusisup-com`)**:
   - Landmark `<header class="siu-site-header">` (`1440x78px`) hosting `Status Is UP — Index für Service-Upt` navigation (`Launch Kit · Toolkits · Preise · Lerne Siu kennen`), DOM attributes (`data-siu-asset-recovery`, `data-checked-head="true"`, `data-loc="client/src/pages/Home..."`, `data-loc="client/src/components..."`), and stylesheet rule `.language-selector svg { width:.88rem;height:.88rem;color:08733a }`.
2. **Hero Stage & Focal Lead (<section.hero-shell> — `WEITERMACHEN.`)**:
   - Landmark `<section class="hero-shell px-5">` presenting display lead `WEITERMACHEN.` and copy excerpt *"Status Is Up (SIU) ist eine Plattform zur Unterstützung der Verfü"* over `#f5f3ea` canvas and `#111d2f` ink.
3. **Primary Showcase & Content Grid (<section.ticker-bar> — `Teste auf dem Smartphone, das dein`)**:
   - Landmark `<section class="ticker-bar">` rendering section `Teste auf dem Smartphone, das deine Besucher nutzen.` with copy *"Von Status Is Down überwachte Dienste"*, asset references (`get_counts`, `show_ads_impl_fy2021.js`, `6a949f167c6f97b4640555e1.js`, `favicon.ico`), and grid rule `.language-selector select { max-width:112px;border:0;background:transparent;color:inherit;font:inher... }`.
4. **Interactive Detail & Feature Matrix (<section.siu-app-promo> — `Finden Sie Dienste, die bereit ble`)**:
   - Landmark `<section class="siu-app-promo">` framing `Finden Sie Dienste, die bereit bleiben.` and `Gute Nachrichten brauchen gute Belege.` (*"Von Status Is Down überwachte Websites"*) with `#fffef8` surface cards, `#f2a30f` accents, and `.language-selector:focus-within { border-color:14b65b;box-shadow:0 0 0 2px 14b65b33 }`.
5. **Colophon & Global Directory Footer (<footer.siu-site-footer> — `https://statusisup.com/`)**:
   - Landmark `<footer class="siu-site-footer">` anchoring `Status Is UP — Index für Service` footer links (`Launch Kit · Toolkits · Preise · Lerne Siu kennen`), copy *"Belege beginnen bei Status Is Down"*, and `#cbd3c9` structural dividers.
