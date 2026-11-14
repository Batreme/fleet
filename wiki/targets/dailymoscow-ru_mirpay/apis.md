---
title: "APIs & Protocols: dailymoscow-ru_mirpay"
date: 2026-11-14
target: "[[overview|dailymoscow-ru_mirpay]]"
---

# Discovered APIs & Protocols: dailymoscow-ru_mirpay

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/rum/vitals` | `200` | REST endpoint |
| `GET` | `/watch/60687529/1` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /rum/vitals
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    }
  }
}
```
### `GET` /watch/60687529/1
```json
{
  "type": "object",
  "properties": {
    "settings": {
      "type": "object",
      "properties": {
        "auto_goals": {
          "type": "number"
        },
        "button_goals": {
          "type": "number"
        },
        "c_recp": {
          "type": "string"
        },
        "form_goals": {
          "type": "number"
        },
        "pcs": {
          "type": "string"
        },
        "webvisor": {
          "type": "object",
          "properties": {
            "ad_recp": {
              "type": "any"
            },
            "arch_type": {
              "type": "any"
            },
            "date": {
              "type": "any"
            },
            "forms": {
              "type": "any"
            },
            "recp": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            }
          }
        },
        "sbp": {
          "type": "object",
          "properties": {
            "a": {
              "type": "any"
            },
            "b": {
              "type": "any"
            }
          }
        },
        "eu": {
          "type": "number"
        },
        "region": {
          "type": "string"
        },
        "nss": {
          "type": "number"
        },
        "hittoken": {
          "type": "string"
        },
        "oauth": {
          "type": "number"
        },
        "wstoken": {
          "type": "string"
        },
        "hidv2": {
          "type": "string"
        },
        "ymclid": {
          "type": "string"
        }
      }
    },
    "userData": {
      "type": "object",
      "properties": {}
    }
  }
}
```

