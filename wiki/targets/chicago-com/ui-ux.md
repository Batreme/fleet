---
title: "UI & Design System: chicago-com"
date: 2026-11-14
target: "[[overview|chicago-com]]"
---

# UI Architecture & Design Tokens: chicago-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--loginForm--color` | `var(--cdc--color--text-primary)` |
| `--loginForm--divider--color` | `var(--cdc--color--text-secondary)` |
| `--loginForm--divider--font-size` | `var(--cdc--font-size--14)` |
| `--loginForm--divider--letter-spacing` | `0` |
| `--loginForm--divider--line-color` | `var(--cdc--color--beige-border)` |
| `--loginForm--divider--margin` | `var(--cdc--spacing--20) 0` |
| `--loginForm--error--accent-color` | `var(--cdc--color--text-danger)` |
| `--loginForm--error--background` | `var(--cdc--color--surface-secondary)` |
| `--loginForm--error--border` | `1px solid var(--cdc--color--text-danger)` |
| `--loginForm--error--border-radius` | `var(--cdc--radius--12)` |
| `--loginForm--error--color` | `var(--cdc--color--text-danger)` |
| `--loginForm--error--padding` | `var(--cdc--spacing--12) var(--cdc--spacing--16)` |
| `--loginForm--font-family` | `var(--cdc--font--primary)` |
| `--loginForm--form--gap` | `var(--cdc--spacing--12)` |
| `--loginForm--input--background` | `var(--cdc--color--surface-secondary)` |
| `--loginForm--input--border` | `1px solid var(--cdc--color--text-link)` |
| `--loginForm--input--border-radius` | `31.25rem` |
| `--loginForm--input--focus-border-color` | `var(--cdc--color--text-link)` |
| `--loginForm--input--font-size` | `var(--cdc--font-size--14)` |
| `--loginForm--input--padding` | `0 var(--cdc--spacing--20)` |
| `--loginForm--label--margin` | `0 0 var(--cdc--spacing--12)` |
| `--loginForm--otp-input--font-size` | `var(--cdc--font-size--24)` |
| `--loginForm--resend--color` | `var(--cdc--color--text-secondary)` |
| `--loginForm--resend--font-size` | `var(--cdc--font-size--14)` |
| `--loginForm--resend--hover-color` | `var(--cdc--color--text-brand)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `PrimaryNav-module-scss-module__spQlca__navMobile` |
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `SiteFooter-module-scss-module__Z-fjzq__social` |
| `<nav>` | `-` | `SiteFooter-module-scss-module__Z-fjzq__social` |
| `<header>` | `-` | `SiteHeader-module-scss-module__-SRi6q__siteHeader SiteHeader-module-scss-module__-SRi6q__overlay` |
| `<main>` | `-` | `layout-module-scss-module__iZ4gNW__main` |
| `<footer>` | `-` | `SiteFooter-module-scss-module__Z-fjzq__siteFooter` |
| `<dialog>` | `mobile-menu-container` | `MobileMenu-module-scss-module__bDxPCa__mobileMenu` |
| `<dialog>` | `welcome-dialog` | `WelcomeDialog-module-scss-module__M6XWxW__dialog` |
