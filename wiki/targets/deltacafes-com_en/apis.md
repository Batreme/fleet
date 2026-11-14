---
title: "APIs & Protocols: deltacafes-com_en"
date: 2026-11-14
target: "[[overview|deltacafes-com_en]]"
---

# Discovered APIs & Protocols: deltacafes-com_en

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/en/_payload.json` | `200` | REST endpoint |
| `GET` | `/_i18n/e3b0c442/en/messages.json` | `200` | REST endpoint |
| `POST` | `/api/send` | `200` | REST endpoint |
| `GET` | `/consentconfig/cb6cab0b-3666-47f6-90c9-9b7c7a3eed9b/settings.json` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/147c56e1-a59f-4648-b720-74230f1ff006.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /en/_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /_i18n/e3b0c442/en/messages.json
```json
{
  "type": "object",
  "properties": {
    "en": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `POST` /api/send
```json
{
  "type": "object",
  "properties": {
    "cache": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "visitId": {
      "type": "string"
    }
  }
}
```
### `GET` /consentconfig/cb6cab0b-3666-47f6-90c9-9b7c7a3eed9b/settings.json
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
### `GET` /_nuxt/builds/meta/147c56e1-a59f-4648-b720-74230f1ff006.json
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "timestamp": {
      "type": "number"
    },
    "prerendered": {
      "type": "array",
      "items": "any"
    }
  }
}
```

