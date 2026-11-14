---
title: "APIs & Protocols: rialto-com-au"
date: 2026-11-14
target: "[[overview|rialto-com-au]]"
---

# Discovered APIs & Protocols: rialto-com-au

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/wp-admin/admin-ajax.php` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /wp-admin/admin-ajax.php
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
        "html": {
          "type": "string"
        },
        "feedStatus": {
          "type": "object",
          "properties": {
            "shouldPaginate": {
              "type": "any"
            }
          }
        },
        "report": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "resizedImages": {
          "type": "object",
          "properties": {
            "17914904283239923": {
              "type": "any"
            },
            "18118937926708778": {
              "type": "any"
            },
            "18132471832731550": {
              "type": "any"
            },
            "18032080850687067": {
              "type": "any"
            },
            "18105515201263616": {
              "type": "any"
            },
            "18079732661753976": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

