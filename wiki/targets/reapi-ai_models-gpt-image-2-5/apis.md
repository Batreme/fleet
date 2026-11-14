---
title: "APIs & Protocols: reapi-ai_models-gpt-image-2-5"
date: 2026-11-14
target: "[[overview|reapi-ai_models-gpt-image-2-5]]"
---

# Discovered APIs & Protocols: reapi-ai_models-gpt-image-2-5

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/script.js` | `200` | REST endpoint |
| `GET` | `/api/site/tracking-config/7398c367fb45` | `200` | REST endpoint |
| `GET` | `/api/auth/get-session` | `200` | REST endpoint |
| `POST` | `/api/track` | `200` | REST endpoint |
| `GET` | `/api/internal/announcements` | `200` | REST endpoint |
| `GET` | `/pixel-config/v1/MEBkkW76HXvNsvUWAnZwkX.json` | `200` | REST endpoint |
| `POST` | `/api/pricing/estimate` | `200` | REST endpoint |
| `POST` | `/api/track` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/site/tracking-config/7398c367fb45
```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "featureFlagsEnabled": {
      "type": "boolean"
    },
    "sessionReplay": {
      "type": "boolean"
    },
    "webVitals": {
      "type": "boolean"
    },
    "trackErrors": {
      "type": "boolean"
    },
    "trackOutbound": {
      "type": "boolean"
    },
    "trackUrlParams": {
      "type": "boolean"
    },
    "trackInitialPageView": {
      "type": "boolean"
    },
    "trackSpaNavigation": {
      "type": "boolean"
    },
    "trackButtonClicks": {
      "type": "boolean"
    },
    "trackCopy": {
      "type": "boolean"
    },
    "trackFormInteractions": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/auth/get-session
```json
{
  "type": "null"
}
```
### `POST` /api/track
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/internal/announcements
```json
{
  "type": "object",
  "properties": {
    "locale": {
      "type": "string"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "slug": {
            "type": "any"
          },
          "category": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "desc": {
            "type": "any"
          },
          "body": {
            "type": "any"
          },
          "linkUrl": {
            "type": "any"
          },
          "publishedAt": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /pixel-config/v1/MEBkkW76HXvNsvUWAnZwkX.json
```json
{
  "type": "object",
  "properties": {
    "automatic_advanced_matching_enabled": {
      "type": "boolean"
    }
  }
}
```
### `POST` /api/pricing/estimate
```json
{
  "type": "object",
  "properties": {
    "snapshotVersion": {
      "type": "number"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ok": {
            "type": "any"
          },
          "credits": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `POST` /api/track
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```

