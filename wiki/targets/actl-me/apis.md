---
title: "APIs & Protocols: actl-me"
date: 2026-11-14
target: "[[overview|actl-me]]"
---

# Discovered APIs & Protocols: actl-me

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/store/catalog` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/store/catalog
```json
{
  "type": "object",
  "properties": {
    "products": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "productId": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "baseAmount": {
            "type": "any"
          },
          "unitAmount": {
            "type": "any"
          },
          "sizes": {
            "type": "any"
          },
          "taxAmount": {
            "type": "any"
          },
          "colors": {
            "type": "any"
          }
        }
      }
    },
    "available": {
      "type": "boolean"
    },
    "shippingAmount": {
      "type": "number"
    },
    "currency": {
      "type": "string"
    },
    "deliveryBusinessDays": {
      "type": "number"
    }
  }
}
```

