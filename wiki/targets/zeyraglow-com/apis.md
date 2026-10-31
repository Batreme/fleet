---
title: "APIs & Protocols: zeyraglow-com"
date: 2026-10-31
target: "[[overview|zeyraglow-com]]"
---

# Discovered APIs & Protocols: zeyraglow-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/` | `200` | REST endpoint |
| `POST` | `/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "fragments": {
          "type": "object",
          "properties": {
            ".zg-cart-link": {
              "type": "any"
            },
            "#zeyra-cart-drawer": {
              "type": "any"
            },
            ".elementor-menu-cart__toggle_button span.elementor-button-text": {
              "type": "any"
            },
            ".elementor-menu-cart__toggle_button span.elementor-button-icon-qty": {
              "type": "any"
            }
          }
        },
        "cart_hash": {
          "type": "string"
        },
        "cart_count": {
          "type": "number"
        },
        "backup_saved": {
          "type": "boolean"
        }
      }
    }
  }
}
```
### `POST` /
```json
{
  "type": "object",
  "properties": {
    "fragments": {
      "type": "object",
      "properties": {
        "div.widget_shopping_cart_content": {
          "type": "string"
        },
        ".zg-cart-link": {
          "type": "string"
        },
        "#zeyra-cart-drawer": {
          "type": "string"
        },
        ".elementor-menu-cart__toggle_button span.elementor-button-text": {
          "type": "string"
        },
        ".elementor-menu-cart__toggle_button span.elementor-button-icon-qty": {
          "type": "string"
        },
        "div.elementor-widget-container .woocommerce .cross-sells": {
          "type": "string"
        },
        "div.elementor-widget-container .woocommerce section.up-sells": {
          "type": "string"
        }
      }
    },
    "cart_hash": {
      "type": "string"
    }
  }
}
```

