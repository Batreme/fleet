---
title: "APIs & Protocols: dsquaredmedia-net"
date: 2026-11-14
target: "[[overview|dsquaredmedia-net]]"
---

# Discovered APIs & Protocols: dsquaredmedia-net

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/d2cms-page-style` | `200` | REST endpoint |
| `POST` | `/api/v1/snippets/websites/c4de75ba-c1a8-49ef-baa6-5aacac53ebfc/statistics` | `201` | REST endpoint |
| `GET` | `/api/v1/snippets/websites/c4de75ba-c1a8-49ef-baa6-5aacac53ebfc/cookies` | `200` | REST endpoint |
| `POST` | `/api/v1/snippets/websites/c4de75ba-c1a8-49ef-baa6-5aacac53ebfc/statistics` | `201` | REST endpoint |
| `GET` | `/api/v1/snippets/websites/c4de75ba-c1a8-49ef-baa6-5aacac53ebfc/cookies` | `200` | REST endpoint |
| `GET` | `/resource-blocker/i18n/en.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/v1/snippets/websites/c4de75ba-c1a8-49ef-baa6-5aacac53ebfc/statistics
```json
{
  "type": "number"
}
```
### `GET` /api/v1/snippets/websites/c4de75ba-c1a8-49ef-baa6-5aacac53ebfc/cookies
```json
{
  "type": "object",
  "properties": {
    "cookies": {
      "type": "object",
      "properties": {
        "unclassified": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "essential": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "performance": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "analytics": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "advertising": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "social_networking": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "prefix": {
          "type": "array",
          "items": "any"
        }
      }
    }
  }
}
```
### `POST` /api/v1/snippets/websites/c4de75ba-c1a8-49ef-baa6-5aacac53ebfc/statistics
```json
{
  "type": "number"
}
```
### `GET` /api/v1/snippets/websites/c4de75ba-c1a8-49ef-baa6-5aacac53ebfc/cookies
```json
{
  "type": "object",
  "properties": {
    "cookies": {
      "type": "object",
      "properties": {
        "unclassified": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "essential": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "performance": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "analytics": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "advertising": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "social_networking": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "prefix": {
          "type": "array",
          "items": "any"
        }
      }
    }
  }
}
```
### `GET` /resource-blocker/i18n/en.json
```json
{
  "type": "object",
  "properties": {
    "advanced-gcm-defaults-disclosure.disclosure": {
      "type": "string"
    },
    "back-button.back": {
      "type": "string"
    },
    "blocked-content.enable": {
      "type": "string"
    },
    "blocked-content.notice": {
      "type": "string"
    },
    "blocked-content.prefs": {
      "type": "string"
    },
    "blocked-content.title": {
      "type": "string"
    },
    "blocked-content.to-allow-content": {
      "type": "string"
    },
    "categories-tab-content.subtitle": {
      "type": "string"
    },
    "consent-prompt-content.accept": {
      "type": "string"
    },
    "consent-prompt-content.decline": {
      "type": "string"
    },
    "consent-prompt-content.powered-by": {
      "type": "string"
    },
    "consent-prompt.aria-label": {
      "type": "string"
    },
    "consent-settings-table.advertising-description": {
      "type": "string"
    },
    "consent-settings-table.advertising-title": {
      "type": "string"
    },
    "consent-settings-table.analytics-description": {
      "type": "string"
    },
    "consent-settings-table.analytics-title": {
      "type": "string"
    },
    "consent-settings-table.details": {
      "type": "string"
    },
    "consent-settings-table.essential-description": {
      "type": "string"
    },
    "consent-settings-table.essential-title": {
      "type": "string"
    },
    "consent-settings-table.performance-description": {
      "type": "string"
    }
  }
}
```

