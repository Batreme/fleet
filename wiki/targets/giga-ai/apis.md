---
title: "APIs & Protocols: giga-ai"
date: 2026-11-14
target: "giga-ai"
---

# Discovered APIs & Protocols: giga-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/agent/health` | `200` | REST endpoint |
| `GET` | `/consentconfig/3e2dee21-57d0-45a0-ab52-e2cc978ce8a1/settings.json` | `200` | REST endpoint |
| `POST` | `/ingest/flags/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/agent/health
```json
{
  "type": "object",
  "properties": {
    "enabled": {
      "type": "boolean"
    },
    "ready": {
      "type": "boolean"
    },
    "live": {
      "type": "boolean"
    },
    "chat": {
      "type": "boolean"
    }
  }
}
```
### `GET` /consentconfig/3e2dee21-57d0-45a0-ab52-e2cc978ce8a1/settings.json
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
### `POST` /ingest/flags/
```json
{
  "type": "object",
  "properties": {
    "errorsWhileComputingFlags": {
      "type": "boolean"
    },
    "flags": {
      "type": "object",
      "properties": {}
    },
    "requestId": {
      "type": "string"
    },
    "evaluatedAt": {
      "type": "number"
    }
  }
}
```

