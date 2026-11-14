---
title: "APIs & Protocols: auge-xp-com"
date: 2026-11-14
target: "[[overview|auge-xp-com]]"
---

# Discovered APIs & Protocols: auge-xp-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consentconfig/ced38b07-60a9-4c9f-ba53-383fcf19e154/settings.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consentconfig/ced38b07-60a9-4c9f-ba53-383fcf19e154/settings.json
```json
{
  "type": "object",
  "properties": {
    "widget": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "position": {
          "type": "object",
          "properties": {
            "position": {
              "type": "any"
            },
            "distanceVerticalPx": {
              "type": "any"
            },
            "distanceHorizontalPx": {
              "type": "any"
            }
          }
        },
        "theme": {
          "type": "object",
          "properties": {
            "closed": {
              "type": "any"
            },
            "opened": {
              "type": "any"
            }
          }
        },
        "content": {
          "type": "object",
          "properties": {
            "cultures": {
              "type": "any"
            },
            "default": {
              "type": "any"
            },
            "autodetectLanguage": {
              "type": "any"
            }
          }
        }
      }
    },
    "twipla": {
      "type": "null"
    }
  }
}
```

