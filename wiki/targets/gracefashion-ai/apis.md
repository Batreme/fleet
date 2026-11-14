---
title: "APIs & Protocols: gracefashion-ai"
date: 2026-11-14
target: "[[overview|gracefashion-ai]]"
---

# Discovered APIs & Protocols: gracefashion-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consentconfig/18b760a2-b60e-4ef0-8a41-8dff2e858d25/settings.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consentconfig/18b760a2-b60e-4ef0-8a41-8dff2e858d25/settings.json
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

