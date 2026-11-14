---
title: "UI & Design System: www-politico-eu_sponsored-content-saving-costs-and-improving-lives"
date: 2026-11-14
target: "[[overview|www-politico-eu_sponsored-content-saving-costs-and-improving-lives]]"
---

# UI Architecture & Design Tokens: www-politico-eu_sponsored-content-saving-costs-and-improving-lives

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--card-image-ratio` | `3/2` |
| `--button-padding-block` | `var(--wp--custom--spacing--6)` |
| `--button-padding-inline` | `var(--wp--custom--spacing--6)` |
| `--button-outline-color` | `var(--color-border)` |
| `--button-background-color` | `var(--color-background-inverse)` |
| `--button-text-color` | `var(--color-text-inverse)` |
| `--button-hover-background-color` | `var(--wp--custom--color--grey--800)` |
| `--button-hover-text-color` | `var(--color-text-inverse)` |
| `--button-focus-background-color` | `var(--color-background-inverse)` |
| `--button-focus-text-color` | `var(--color-text-inverse)` |
| `--button-active-background-color` | `var(--wp--custom--color--grey--800)` |
| `--button-active-text-color` | `var(--color-text-inverse-50pc)` |
| `--button-plain-background-color` | `transparent` |
| `--button-plain-text-color` | `var(--color-text-primary)` |
| `--button-plain-hover-text-color` | `var(--color-link)` |
| `--button-plain-focus-text-color` | `var(--color-text-primary)` |
| `--button-plain-active-text-color` | `var(--color-link-50pc)` |
| `--button-disabled-background-color` | `var(--color-background-disabled)` |
| `--button-disabled-text-color` | `var(--color-text-disabled)` |
| `--transition-style-button-in` | `var(--wp--custom--animation--duration--default) var(--wp--cu` |
| `--transition-style-button-out` | `var(--wp--custom--animation--duration--extra-small) var(--wp` |
| `--transition-style-link-in` | `var(--wp--custom--animation--duration--default) var(--wp--cu` |
| `--transition-style-link-out` | `var(--wp--custom--animation--duration--extra-small) var(--wp` |
| `--z-index-skin` | `0` |
| `--z-index-content` | `10` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `navigation-mini header__edition-nav-alt` |
| `<nav>` | `-` | `primary-nav` |
| `<nav>` | `-` | `navigation-mini header__edition-nav` |
| `<nav>` | `-` | `secondary-nav` |
| `<nav>` | `-` | `navigation-mini social-sharing has-alt-style has-flat-layout` |
| `<nav>` | `-` | `navigation-simple` |
| `<nav>` | `-` | `site-footer__social-nav` |
| `<nav>` | `-` | `site-footer__main-nav` |
| `<nav>` | `-` | `site-footer__legal-nav` |
| `<header>` | `-` | `header` |
| `<main>` | `main` | `main` |
| `<footer>` | `-` | `article__footer-inline` |
| `<footer>` | `-` | `article__footer without-secondary-content` |
| `<footer>` | `-` | `site-footer` |
