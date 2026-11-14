---
title: "APIs & Protocols: nodenza-com"
date: 2026-11-14
target: "[[overview|nodenza-com]]"
---

# Discovered APIs & Protocols: nodenza-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/config/nodenza.com/config.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /config/nodenza.com/config.json
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
      "type": "null"
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

