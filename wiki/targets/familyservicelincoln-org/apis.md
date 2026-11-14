---
title: "APIs & Protocols: familyservicelincoln-org"
date: 2026-11-14
target: "[[overview|familyservicelincoln-org]]"
---

# Discovered APIs & Protocols: familyservicelincoln-org

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/config/familyservicelincoln.org/config.json` | `200` | REST endpoint |
| `GET` | `/consentconfig/1670e8a1-465b-4331-ab0f-cf4053069b1a/settings.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /config/familyservicelincoln.org/config.json
```json
{
  "type": "object",
  "properties": {
    "time": {
      "type": "string"
    },
    "specifics": {
      "type": "string"
    },
    "addonAnalytics": {
      "type": "boolean"
    },
    "blockMeta": {
      "type": "boolean"
    },
    "blockImages": {
      "type": "boolean"
    },
    "blockStyles": {
      "type": "boolean"
    },
    "blockTextSimplifier": {
      "type": "boolean"
    },
    "widgetSettings": {
      "type": "object",
      "properties": {
        "consistentHelpData": {
          "type": "array",
          "items": "any"
        },
        "disableBgProcess": {
          "type": "boolean"
        },
        "footerHtml": {
          "type": "string"
        },
        "hideComponents": {
          "type": "array",
          "items": "any"
        },
        "hideMobile": {
          "type": "boolean"
        },
        "hideTrigger": {
          "type": "boolean"
        },
        "language": {
          "type": "string"
        },
        "leadColor": {
          "type": "string"
        },
        "position": {
          "type": "string"
        },
        "remoteAnalytics": {
          "type": "boolean"
        },
        "statementLink": {
          "type": "string"
        },
        "statementVariant": {
          "type": "string"
        },
        "triggerColor": {
          "type": "string"
        },
        "triggerIcon": {
          "type": "string"
        },
        "triggerOffsetX": {
          "type": "number"
        },
        "triggerOffsetY": {
          "type": "number"
        },
        "triggerPositionX": {
          "type": "string"
        },
        "triggerPositionY": {
          "type": "string"
        },
        "triggerRadius": {
          "type": "string"
        },
        "triggerSize": {
          "type": "string"
        }
      }
    },
    "featureFlags": {
      "type": "object",
      "properties": {
        "ai-assistant": {
          "type": "boolean"
        },
        "classification-provider": {
          "type": "boolean"
        },
        "text-simplifier": {
          "type": "boolean"
        }
      }
    }
  }
}
```
### `GET` /consentconfig/1670e8a1-465b-4331-ab0f-cf4053069b1a/settings.json
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

