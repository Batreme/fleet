---
title: "APIs & Protocols: cobaltaf-org"
date: 2026-11-14
target: "cobaltaf-org"
---

# Discovered APIs & Protocols: cobaltaf-org

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/maps/api/js` | `200` | REST endpoint |
| `GET` | `/maps/api/mapsjs/gen_204` | `200` | REST endpoint |
| `GET` | `/config/cobaltaf.org/config.json` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/common.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/util.js` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /maps/api/mapsjs/gen_204
```json
{
  "type": "object",
  "properties": {}
}
```
### `GET` /config/cobaltaf.org/config.json
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
        "text-simplifier": {
          "type": "boolean"
        },
        "ai-assistant": {
          "type": "boolean"
        },
        "classification-provider": {
          "type": "boolean"
        }
      }
    }
  }
}
```

