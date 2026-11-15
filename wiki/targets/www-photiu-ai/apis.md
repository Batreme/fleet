---
title: "APIs & Protocols: www-photiu-ai"
date: 2026-11-14
target: "www-photiu-ai"
---

# Discovered APIs & Protocols: www-photiu-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cache` | `200` | REST endpoint |
| `POST` | `/cdn-cgi/rum` | `204` | REST endpoint |
| `GET` | `/api/credits/featurePricingRules` | `200` | REST endpoint |
| `GET` | `/api/auth/session` | `200` | REST endpoint |
| `POST` | `/api/v1/snippets/websites/3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5/statistics` | `201` | REST endpoint |
| `GET` | `/api/v1/snippets/websites/3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5/cookies` | `200` | REST endpoint |
| `GET` | `/resource-blocker/i18n/en.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /cache
```json
{
  "type": "object",
  "properties": {
    "ht": {
      "type": "number"
    }
  }
}
```
### `GET` /api/credits/featurePricingRules
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "featureCode": {
            "type": "any"
          },
          "parameterKey": {
            "type": "any"
          },
          "parameterPackage": {
            "type": "any"
          },
          "outputPolicy": {
            "type": "any"
          },
          "creditsRequirement": {
            "type": "any"
          },
          "paymentTiming": {
            "type": "any"
          },
          "creditsCentiCost": {
            "type": "any"
          },
          "batchCentiCostPerImage": {
            "type": "any"
          },
          "batchCreditsRequirement": {
            "type": "any"
          },
          "batchPaymentTiming": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/auth/session
```json
{
  "type": "object",
  "properties": {}
}
```
### `POST` /api/v1/snippets/websites/3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5/statistics
```json
{
  "type": "number"
}
```
### `GET` /api/v1/snippets/websites/3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5/cookies
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
          "items": "any"
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

