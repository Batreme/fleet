---
title: "APIs & Protocols: www-butter-video"
date: 2026-11-14
target: "www-butter-video"
---

# Discovered APIs & Protocols: www-butter-video

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/graphql` | `200` | GraphQL: `AnonymousQuery` |
| `GET` | `/v1/projects/8d2efc169d425acb5c4b/settings` | `200` | REST endpoint |
| `GET` | `/v1/analytics-js/actions/google-ads.js` | `200` | REST endpoint |
| `GET` | `/v1/analytics-js/actions/bing-ads.js` | `200` | REST endpoint |
| `GET` | `/v1/analytics-js/actions/meta-pixel.js` | `200` | REST endpoint |
| `GET` | `/v1/analytics-js/actions/google-analytics-4-web.js` | `200` | REST endpoint |
| `GET` | `/v1/analytics-js/actions/twitter-pixel.js` | `200` | REST endpoint |
| `GET` | `/v1/analytics-js/actions/google-tag-manager.js` | `200` | REST endpoint |
| `POST` | `/api/v4/users` | `200` | REST endpoint |
| `GET` | `/api/v1/branding` | `-1` | REST endpoint |
| `GET` | `/api/v1/templates` | `-1` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/graphql
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "currentViewer": {
          "type": "null"
        }
      }
    }
  }
}
```
### `GET` /v1/projects/8d2efc169d425acb5c4b/settings
```json
{
  "type": "object",
  "properties": {
    "integrations": {
      "type": "object",
      "properties": {
        "Customer.io Data Pipelines": {
          "type": "object",
          "properties": {
            "addBundledMetadata": {
              "type": "any"
            },
            "apiHost": {
              "type": "any"
            },
            "apiKey": {
              "type": "any"
            },
            "protocol": {
              "type": "any"
            }
          }
        },
        "Customer.io In-App Plugin": {
          "type": "object",
          "properties": {
            "siteId": {
              "type": "any"
            }
          }
        }
      }
    },
    "metrics": {
      "type": "object",
      "properties": {
        "sampleRate": {
          "type": "number"
        }
      }
    },
    "remotePlugins": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "creationName": {
            "type": "any"
          },
          "libraryName": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "settings": {
            "type": "any"
          },
          "url": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `POST` /api/v4/users
```json
{
  "type": "object",
  "properties": {
    "inAppMessages": {
      "type": "array",
      "items": "any"
    },
    "inboxMessages": {
      "type": "array",
      "items": "any"
    }
  }
}
```

