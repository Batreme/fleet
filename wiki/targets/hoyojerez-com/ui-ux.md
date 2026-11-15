# UI & UX Architecture: hoyojerez-com

## Overview & Design Identity
- **Target**: `hoyojerez-com` (**HOYO Jerez · Discoteca en Jerez de la Frontera**)
- **Production URL**: [https://hoyojerez.com/](https://hoyojerez.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#0000` / `#010101`)
- **Summary**: HOYO, la discoteca de Jerez de la Frontera. Entra en el túnel: próximas fiestas y entradas, las fotos de cada noche y dónde encontrarnos.
- **Total Clean CSS Variables Extracted**: `6` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Panchang`
- **Body Font Stack**: `Morganite`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.6rem`, `14px`, `12px`, `clamp(88px,min(17svh,30vw)`, `13px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.6rem`, `14px`, `12px`, `clamp(88px,min(17svh,30vw)`, `13px`)
- **Body Copy**: rule `p` (`font-size: 13px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.6rem`, `14px`, `12px`, `clamp(88px,min(17svh,30vw)`, `13px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `.evento-enlace { color: #0000 }` |
| **Primary Typography Ink** | `#fff` | `.evento-enlace:focus-visible { color: #fff }` |
| **Elevated Surface / Card Substrate** | `#5be010` | `.evento-enlace:focus-visible { border: #5be010 }` |
| **Interactive Accent / Highlight** | `#010101` | `._actions_1d25v_67 button:hover { color: #010101 }` |
| **Secondary / Muted Copy** | `#fff3` | `preferences_1d25v_98 ._necessar... { border-top: #fff3 }` |
| **Structural Hairline Border** | `#fff0` | `._boton_1qcud_34 { background: #fff0 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tamano` | `22px` | Dimension / Scale Token |
| `--nivel` | `1` | Design System Custom Token |
| `--pista` | `2px` | Dimension / Scale Token |
| `--pulgar` | `9px` | Dimension / Scale Token |
| `--retraso` | `.2s` | Motion / Timing Token |
| `--cookies-tapa` | `0px` | Dimension / Scale Token |
| `--hoyojerez-com-bg` | `#0000` | Canvas Substrate (from `.evento-enlace { color: #0000 }`) |
| `--hoyojerez-com-ink` | `#010101` | Primary Typography Ink (stylesheet-derived) |
| `--hoyojerez-com-surface` | `#5be010` | Surface Substrate (stylesheet-derived) |
| `--hoyojerez-com-accent` | `#010101` | Interactive Accent (stylesheet-derived) |
| `--hoyojerez-com-muted` | `#fff3` | Secondary Ink (stylesheet-derived) |
| `--hoyojerez-com-border` | `#fff0` | Structural Border (stylesheet-derived) |
| `--hoyojerez-com-container` | `410px` | Container Bound (stylesheet-derived) |
| `--hoyojerez-com-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--hoyojerez-com-pad` | `.8rem` | Lateral Padding (stylesheet-derived) |
| `--hoyojerez-com-ease` | `cubic-bezier(.22,1,.36,1)` | Primary Easing Function |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `hoyojerez-com`)**:
   - Landmark `<header class="lenis">` hosting `HOYO Jerez · Discoteca en Jerez de l` navigation (`Galería · Eventos · Contacto`), DOM attributes (`data-astro-cid-wetux6vv`, `data-astro-exec`, `data-astro-transition-persist="hoyo-tunnel"`, `data-persistent-tunnel`), and stylesheet rule `focus-visible { outline-offset:3px;outline:2px solid fff }`.
2. **Hero Stage & Focal Lead (<main.main-content> — `Eventos`)**:
   - Landmark `<main class="main-content">` presenting display lead `Eventos` and copy excerpt *"Paciencia, se está cargando el Hoyo."* over `#0000` canvas and `#010101` ink.
3. **Primary Showcase & Content Grid (<main.main-content> — `Galería`)**:
   - Landmark `<main class="main-content">` rendering section `Galería` with copy *"La conexión va lenta · seguimos cargando"*, asset references (`index.astro_astro_type_script_ind...`, `alien.DVECqh-s.glb`, `pulsador.BQ51WIjM.glb`, `draco_wasm_wrapper.js`), and grid rule `._panel_1d25v_1 { padding:22px;bottom:28px;left:28px }`.
4. **Interactive Detail & Feature Matrix (<main.main-content> — `Proyección`)**:
   - Landmark `<main class="main-content">` framing `Proyección` and `Tú eliges el ritmo.` (*"No se pudo cargar el Hoyo"*) with `#5be010` surface cards, `#010101` accents, and `._panel_1d25v_1 h2 { text-transform:uppercase;color:5be010;margin:8px 0 12px;font:900 44px/.9... }`.
5. **Colophon & Global Directory Footer (<footer.intro-cargando> — `https://hoyojerez.com/`)**:
   - Landmark `<footer class="intro-cargando">` anchoring `HOYO Jerez · Discoteca en Jerez ` footer links (`Galería · Eventos · Contacto`), copy *"Púlsalo. Entra en el Hoyo"*, and `#fff0` structural dividers.
