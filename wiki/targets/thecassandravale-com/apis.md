---
title: "APIs & Protocols: thecassandravale-com"
date: 2026-11-14
target: "thecassandravale-com"
---

# Discovered APIs & Protocols: thecassandravale-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/watch/111770258/1` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /watch/111770258/1
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
        "cf": {
          "type": "number"
        },
        "mcf": {
          "type": "number"
        },
        "aytm": {
          "type": "boolean"
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

