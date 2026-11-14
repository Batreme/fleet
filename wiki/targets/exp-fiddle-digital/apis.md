---
title: "APIs & Protocols: exp-fiddle-digital"
date: 2026-11-14
target: "[[overview|exp-fiddle-digital]]"
---

# Discovered APIs & Protocols: exp-fiddle-digital

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/decide/` | `200` | REST endpoint |
| `POST` | `/graphql` | `200` | GraphQL: `AnonymousQuery` |
| `GET` | `/exps/exp-7/models/kobo/kobo.gltf` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /decide/
```json
{
  "type": "object",
  "properties": {
    "errorsWhileComputingFlags": {
      "type": "boolean"
    },
    "featureFlags": {
      "type": "object",
      "properties": {}
    },
    "featureFlagPayloads": {
      "type": "object",
      "properties": {}
    },
    "requestId": {
      "type": "string"
    },
    "evaluatedAt": {
      "type": "number"
    },
    "errorTracking": {
      "type": "object",
      "properties": {
        "autocaptureExceptions": {
          "type": "boolean"
        },
        "suppressionRules": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "supportedCompression": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "productTours": {
      "type": "boolean"
    },
    "analytics": {
      "type": "object",
      "properties": {
        "endpoint": {
          "type": "string"
        }
      }
    },
    "siteApps": {
      "type": "array",
      "items": "any"
    },
    "autocaptureExceptions": {
      "type": "boolean"
    },
    "conversations": {
      "type": "boolean"
    },
    "surveys": {
      "type": "boolean"
    },
    "autocapture_opt_out": {
      "type": "boolean"
    },
    "push": {
      "type": "object",
      "properties": {
        "appIds": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "elementsChainAsString": {
      "type": "boolean"
    },
    "capturePerformance": {
      "type": "object",
      "properties": {
        "network_timing": {
          "type": "boolean"
        },
        "web_vitals": {
          "type": "boolean"
        },
        "web_vitals_allowed_metrics": {
          "type": "null"
        }
      }
    },
    "hasFeatureFlags": {
      "type": "boolean"
    },
    "defaultIdentifiedOnly": {
      "type": "boolean"
    },
    "sessionRecording": {
      "type": "boolean"
    }
  }
}
```
### `POST` /graphql
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "projectCategories": {
          "type": "object",
          "properties": {
            "data": {
              "type": "any"
            }
          }
        },
        "projectPage": {
          "type": "object",
          "properties": {
            "data": {
              "type": "any"
            }
          }
        },
        "navigation": {
          "type": "object",
          "properties": {
            "data": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

