---
title: "APIs & Protocols: about-centra-com"
date: 2026-11-14
target: "[[overview|about-centra-com]]"
---

# Discovered APIs & Protocols: about-centra-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consentconfig/93a8c043-1906-4454-8625-b2e5166abf78/settings.json` | `200` | REST endpoint |
| `GET` | `/cms-js-static/ex/js/island-runtime/v1/island-runtime.mjs` | `200` | REST endpoint |
| `GET` | `/embed/v4/visitor/7733481/ceeda43d-5606-4529-bd4c-6aeb15fc18f7` | `200` | REST endpoint |
| `GET` | `/embed/v4/feature-control/7733481` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consentconfig/93a8c043-1906-4454-8625-b2e5166abf78/settings.json
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
### `GET` /embed/v4/visitor/7733481/ceeda43d-5606-4529-bd4c-6aeb15fc18f7
```json
{
  "type": "object",
  "properties": {
    "countryCode": {
      "type": "string"
    }
  }
}
```
### `GET` /embed/v4/feature-control/7733481
```json
{
  "type": "object",
  "properties": {
    "featureControls": {
      "type": "object",
      "properties": {
        "enabledSvgCountryFlags": {
          "type": "boolean"
        },
        "enabledHeartbeat": {
          "type": "boolean"
        },
        "enabledFeedbackTrellisSmiley": {
          "type": "boolean"
        },
        "resumeFormFill": {
          "type": "boolean"
        },
        "datePickerField": {
          "type": "boolean"
        },
        "recaptchaScriptPerformance": {
          "type": "boolean"
        },
        "formV4ReCaptchaV3Fix": {
          "type": "boolean"
        },
        "recaptchaLoadOnInteraction": {
          "type": "boolean"
        },
        "showBranding": {
          "type": "boolean"
        }
      }
    }
  }
}
```

