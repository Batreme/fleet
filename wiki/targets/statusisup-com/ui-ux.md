# UI & UX Architecture: statusisup-com

## Overview & Design Identity
- **Target**: `statusisup-com` (**Status Is UP — Index für Service-Uptime, Performance & Zuverlässigkeit**)
- **Production URL**: [https://statusisup.com/](https://statusisup.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111d2f` canvas, `#fffef8` ink, `#fffef8` accent)
- **Summary**: Entdecken Sie Dienste mit geringer beobachteter Ausfallaktivität über einen quellverknüpften Index für Service-Uptime, Performance und Zu...
- **Total Clean CSS Variables Extracted**: `153` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo Black`
- **Body Font Stack**: `DM Mono`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.075em`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`letter-spacing: -.065em`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--siu-body: "Manrope",sans-serif`; rule `p` (`font-size: .76rem`, `line-height: 1.65`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`; rule `small` (`letter-spacing: .09em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111d2f` | `var(--siu-guide-navy)` in `:root` |
| **Primary Typography Ink** | `#14b65b` | `var(--siu-guide-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c7f42b` | `var(--siu-guide-lime)` in `:root` |
| **Interactive Accent / Highlight** | `#fffef8` | `var(--siu-guide-cream)` in `:root` |
| **Secondary / Muted Copy** | `#435064` | `var(--siu-guide-ink)` in `:root` |
| **Structural Hairline Border** | `#17202a` | `var(--action-card-ink)` in `:root` |
| **Variable Token (`--action-card-muted`)** | `#52606d` | `var(--action-card-muted)` in `:root` |
| **Variable Token (`--action-card-border`)** | `#cbd5df` | `var(--action-card-border)` in `:root` |
| **Variable Token (`--action-card-surface`)** | `#ffffff` | `var(--action-card-surface)` in `:root` |
| **Variable Token (`--action-card-subtle`)** | `#f4f7fa` | `var(--action-card-subtle)` in `:root` |
| **Variable Token (`--action-card-accent`)** | `#085cc7` | `var(--action-card-accent)` in `:root` |
| **Variable Token (`--action-card-focus`)** | `#f59e0b` | `var(--action-card-focus)` in `:root` |
| **Variable Token (`--signal-ink`)** | `#08733a` | `var(--signal-ink)` in `:root` |
| **Variable Token (`--signal-cobalt`)** | `#1d4ed8` | `var(--signal-cobalt)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--siu-guide-navy` | `#111d2f` | Layout / Spatial Grid Token |
| `--siu-guide-green` | `#14b65b` | Color / Atmospheric Token |
| `--siu-guide-lime` | `#c7f42b` | Color / Atmospheric Token |
| `--siu-guide-cream` | `#fffef8` | Color / Atmospheric Token |
| `--siu-guide-ink` | `#435064` | Typography Ink Token |
| `--action-card-ink` | `#17202a` | Typography Ink Token |
| `--action-card-muted` | `#52606d` | Color / Atmospheric Token |
| `--action-card-border` | `#cbd5df` | Elevation / Border Token |
| `--action-card-surface` | `#ffffff` | Canvas / Surface Token |
| `--action-card-subtle` | `#f4f7fa` | Color / Atmospheric Token |
| `--action-card-accent` | `#085cc7` | Brand / Palette Token |
| `--action-card-focus` | `#f59e0b` | Color / Atmospheric Token |
| `--signal-tone` | `#14b65b` | Color / Atmospheric Token |
| `--signal-ink` | `#08733a` | Typography Ink Token |
| `--signal-wash` | `rgba(20,182,91,.12)` | Color / Atmospheric Token |
| `--signal-cobalt` | `#1d4ed8` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.siu-site-header> — `statusisup-com`)**:
   - Landmark `<header class="siu-site-header">` hosting `Status Is UP — Index für Service-Upt` navigation (`Launch Kit · Toolkits · Preise`), DOM attributes (`data-siu-asset-recovery`, `data-checked-head="true"`, `data-loc="client/src/pages/Home..."`, `data-loc="client/src/components..."`), and stylesheet rule `.language-selector svg { width:.88rem;height:.88rem;color:08733a }`.
2. **Hero Stage & Focal Lead (<section.min-h-screen> — `WEITERMACHEN.`)**:
   - Landmark `<section class="min-h-screen">` presenting display lead `WEITERMACHEN.` and copy excerpt *"STATUS IS UP UNTERSTÜTZUNG VERFÜGBARKEIT"* over `#111d2f` canvas and `#fffef8` ink.
3. **Primary Showcase & Content Grid (<section.hero-shell> — `Teste auf dem Smartphone, das dein`)**:
   - Landmark `<section class="hero-shell relative">` rendering section `Teste auf dem Smartphone, das deine Besucher nutzen.` with copy *"Website‑Optimierungs‑Wiki"*, asset references (`get_counts`, `show_ads_impl_fy2021.js`, `6a949f167c6f97b4640555e1.js`, `favicon.ico`), and grid rule `.language-selector select { max-width:112px;border:0;background:transparent;color:inherit;font:inher... }`.
4. **Interactive Detail & Feature Matrix (<section.ticker-bar> — `Finden Sie Dienste, die bereit ble`)**:
   - Landmark `<section class="ticker-bar">` framing `Finden Sie Dienste, die bereit bleiben.` and `Gute Nachrichten brauchen gute Belege.` (*"Anzeigesprache wählen"*) with `#c7f42b` surface cards, `#fffef8` accents, and `.language-selector:focus-within { border-color:14b65b;box-shadow:0 0 0 2px 14b65b33 }`.
5. **Colophon & Global Directory Footer (<footer.siu-site-footer> — `https://statusisup.com/`)**:
   - Landmark `<footer class="siu-site-footer">` anchoring `Status Is UP — Index für Service` footer links (`Launch Kit · Toolkits · Preise`), copy *"Live-Status auf SID"*, and `#17202a` structural dividers.
