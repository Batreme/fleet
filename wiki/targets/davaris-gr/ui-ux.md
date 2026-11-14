---
title: "UI & Design System: davaris-gr"
date: 2026-11-14
target: "[[overview|davaris-gr]]"
---

# UI Architecture & Design Tokens: davaris-gr

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--space-xs` | `clamp(1rem, 2.2vw, 2.65rem)` |
| `--space-sm` | `clamp(1.875rem, 4.43vw, 5.3125rem)` |
| `--space-md` | `clamp(2.5rem, 6.5vw, 7.8125rem)` |
| `--space-lg` | `clamp(3.75rem, 8.85vw, 10.625rem)` |
| `--block-spacing` | `var(--space-lg)}.bg-beige{background-color:#f5f2e5}.bg-defau` |
| `--bs-blue` | `#0d6efd` |
| `--bs-indigo` | `#6610f2` |
| `--bs-purple` | `#6f42c1` |
| `--bs-pink` | `#d63384` |
| `--bs-red` | `#dc3545` |
| `--bs-orange` | `#fd7e14` |
| `--bs-yellow` | `#ffc107` |
| `--bs-green` | `#198754` |
| `--bs-teal` | `#20c997` |
| `--bs-cyan` | `#0dcaf0` |
| `--bs-black` | `#000` |
| `--bs-white` | `#FFF` |
| `--bs-gray` | `#6c757d` |
| `--bs-gray-dark` | `#343a40` |
| `--bs-gray-100` | `#f8f9fa` |
| `--bs-gray-200` | `#e9ecef` |
| `--bs-gray-300` | `#dee2e6` |
| `--bs-gray-400` | `#ced4da` |
| `--bs-gray-500` | `#adb5bd` |
| `--bs-gray-600` | `#6c757d` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `utility-nav d-none d-lg-block` |
| `<nav>` | `nav-drawer` | `nav-drawer` |
| `<nav>` | `-` | `nav-primary__nav` |
| `<nav>` | `-` | `utility-nav utility-nav--drawer` |
| `<header>` | `-` | `site-header` |
| `<main>` | `main` | `main` |
| `<footer>` | `-` | `nav-primary__footer` |
| `<footer>` | `-` | `site-footer` |
