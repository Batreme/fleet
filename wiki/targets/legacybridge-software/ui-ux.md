---
title: "UI & Design System: legacybridge-software"
date: 2026-11-14
target: "[[overview|legacybridge-software]]"
---

# UI Architecture & Design Tokens: legacybridge-software

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--rise` | `110px` |
| `--rise-ease` | `cubic-bezier(0, 1, 0.4, 1)` |
| `--rise` | `60px` |
| `--overlap` | `clamp(120px, 14.6vw, 280px)` |
| `--text-ink` | `#082a1c` |
| `--text-muted` | `#64707a` |
| `--text-inverse` | `#ffffff` |
| `--text-inverse-muted` | `#94a3b8` |
| `--brand-primary` | `#082a1c` |
| `--brand-secondary` | `#94a3b8` |
| `--brand-accent` | `#cdff8c` |
| `--surface-white` | `#ffffff` |
| `--surface-page` | `#ffffff` |
| `--surface-card` | `#f4f7f9` |
| `--surface-section` | `#f4f7f9` |
| `--surface-accent` | `#dde3e7` |
| `--surface-subtle` | `#dde3e7` |
| `--border-divider` | `#dde3e7` |
| `--radius-8` | `8px` |
| `--radius-12` | `12px` |
| `--radius-16` | `16px` |
| `--radius-full` | `999px` |
| `--font` | `"Geist", ui-sans-serif, system-ui, -apple-system, "Segoe UI"` |
| `--container-w` | `100%` |
| `--page-pad` | `max(100px, 5.2vw)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `site-header__nav` |
| `<header>` | `site-header` | `site-header` |
| `<aside>` | `contact-drawer` | `contact-drawer` |
| `<aside>` | `legal-terms` | `contact-drawer legal-drawer` |
| `<aside>` | `legal-privacy` | `contact-drawer legal-drawer` |
| `<main>` | `-` | `` |
| `<footer>` | `footer` | `site-footer is-offscreen` |
