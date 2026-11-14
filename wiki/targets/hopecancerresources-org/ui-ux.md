---
title: "UI & Design System: hopecancerresources-org"
date: 2026-11-14
target: "[[overview|hopecancerresources-org]]"
---

# UI Architecture & Design Tokens: hopecancerresources-org

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-primary` | `"BrandonText", Arial, Helvetica, sans-serif` |
| `--font-heading` | `"BrandonText", Arial, Helvetica, sans-serif` |
| `--font-base` | `"SourceSans", Arial, Helvetica, sans-serif` |
| `--font-serif` | `"EightiesComebackIt", "Times New Roman", "Garamond", serif` |
| `--color-brand-black` | `#0e1829` |
| `--color-brand-blue` | `#1b7aaf` |
| `--color-brand-lightblue` | `#1fa0e5` |
| `--color-brand-darkblue` | `#476577` |
| `--color-brand-gray-500` | `#90a3bf` |
| `--color-light-gray` | `#476577` |
| `--color-lightest-gray` | `#edf1f4` |
| `--color-notice-warning` | `#dc4b4b` |
| `--color-notice-success` | `#2DB292` |
| `--color-primary` | `var(--color-brand-black)` |
| `--color-secondary` | `var(--color-brand-black)` |
| `--color-brand-text-base` | `var(--color-brand-black)` |
| `--color-link` | `var(--color-brand-black)` |
| `--color-link-hover` | `var(--color-brand-black)` |
| `--color-bg-dark` | `var(--color-brand-black)` |
| `--color-bg-light` | `white}#content{background:#fff` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `nav-mobile` | `mobile-nav` |
| `<nav>` | `nav-desktop` | `desktop-nav` |
| `<header>` | `-` | `site-header template-home header-unscrolled` |
| `<main>` | `content` | `site-content style-` |
| `<footer>` | `footer` | `site-footer` |
