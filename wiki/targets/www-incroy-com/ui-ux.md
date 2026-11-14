---
title: "UI & Design System: www-incroy-com"
date: 2026-11-14
target: "[[overview|www-incroy-com]]"
---

# UI Architecture & Design Tokens: www-incroy-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--w-backdrop-animation` | `initial` |
| `--large` | `before {
  border-width: 5px` |
| `--large` | `after {
  border-width: 5px` |
| `--vertical` | `before, .w-widget-twitter-count-shim.w--vertical:after {
  c` |
| `--vertical` | `before {
  border-width: 5px` |
| `--vertical` | `after {
  border-width: 4px` |
| `--link-color--link-primary` | `var(--base-color-brand--brand-primary)` |
| `--background-color--background-primary` | `var(--base-color-neutral--black)` |
| `--text-color--text-alternate` | `var(--base-color-neutral--white)` |
| `--text-color--text-primary` | `var(--base-color-neutral--black)` |
| `--text-color--text-secondary` | `var(--base-color-neutral--neutral-darker)` |
| `--background-color--background-success` | `var(--base-color-system--success-green)` |
| `--text-color--text-success` | `var(--base-color-system--success-green-dark)` |
| `--base-color-neutral--white` | `#fff` |
| `--border-color--border-primary` | `var(--base-color-neutral--neutral-lightest)` |
| `--background-color--background-alternate` | `var(--base-color-neutral--white)` |
| `--background-color--background-secondary` | `var(--base-color-brand--brand-primary)` |
| `--background-color--background-tertiary` | `var(--base-color-brand--pink)` |
| `--background-color--background-error` | `var(--base-color-system--error-red)` |
| `--text-color--text-error` | `var(--base-color-system--error-red-dark)` |
| `--border-color--border-subtle` | `var(--base-color-neutral--neutral-dark)` |
| `--background-color--background-warning` | `var(--base-color-system--warning-yellow)` |
| `--text-color--text-warning` | `var(--base-color-system--warning-yellow-dark)` |
| `--base-color-brand--brand-primary` | `#6053e5` |
| `--text-color--text-brand` | `var(--base-color-brand--brand-primary)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `navigation` |
| `<main>` | `-` | `main-wrapper` |
