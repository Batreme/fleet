---
title: "APIs & Protocols: later-com_made-you-look"
date: 2026-11-14
target: "[[overview|later-com_made-you-look]]"
---

# Discovered APIs & Protocols: later-com_made-you-look

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cm/fbbd5676-fc7c-424c-b807-57283f8579e8/translations/en.json` | `200` | REST endpoint |
| `GET` | `/page-data/app-data.json` | `200` | REST endpoint |
| `GET` | `/page-data/made-you-look/page-data.json` | `200` | REST endpoint |
| `GET` | `/page-data/sq/d/353462786.json` | `200` | REST endpoint |
| `POST` | `/youtubei/v1/player` | `200` | REST endpoint |
| `GET` | `/pagead/id` | `200` | REST endpoint |
| `POST` | `/youtubei/v1/navigation/resolve_url` | `200` | REST endpoint |
| `GET` | `/pagead/id` | `200` | REST endpoint |
| `GET` | `/pagead/id` | `200` | REST endpoint |
| `POST` | `/youtubei/v1/player` | `200` | REST endpoint |
| `POST` | `/youtubei/v1/navigation/resolve_url` | `200` | REST endpoint |
| `POST` | `/youtubei/v1/navigation/resolve_url` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/api/stats/qoe` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/player` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/api/stats/qoe` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/next` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/api/stats/qoe` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/next` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/api/stats/qoe` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/player` | `-1` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/api/stats/qoe` | `-1` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /cm/fbbd5676-fc7c-424c-b807-57283f8579e8/translations/en.json
```json
{
  "type": "object",
  "properties": {
    "purpose.trackingType.Advertising.description": {
      "type": "string"
    },
    "purpose.trackingType.Analytics.description": {
      "type": "string"
    },
    "purpose.trackingType.Essential.description": {
      "type": "string"
    },
    "purpose.trackingType.Functional.description": {
      "type": "string"
    },
    "purpose.trackingType.SaleOfInfo.description": {
      "type": "string"
    },
    "ui.src.bottomMenu.backButtonText": {
      "type": "string"
    },
    "ui.src.bottomMenu.backButtonTooltip": {
      "type": "string"
    },
    "ui.src.bottomMenu.moreChoicesButtonLabel": {
      "type": "string"
    },
    "ui.src.bottomMenu.moreChoicesButtonPrimary": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonAcceptAll": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonAcceptAllOrMoreChoices": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonAcceptAllRejectAllToggle": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonAcceptOrRejectAdvertising": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonAcceptOrRejectAll": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonAcceptOrRejectAllOrMoreChoices": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonAcceptOrRejectAnalytics": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonCompleteOptions": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonCompleteOptionsInverted": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonCompleteOptionsToggles": {
      "type": "string"
    },
    "ui.src.bottomMenu.showPolicyButtonDoNotSellDisclosure": {
      "type": "string"
    }
  }
}
```
### `GET` /page-data/app-data.json
```json
{
  "type": "object",
  "properties": {
    "webpackCompilationHash": {
      "type": "string"
    }
  }
}
```
### `GET` /page-data/made-you-look/page-data.json
```json
{
  "type": "object",
  "properties": {
    "componentChunkName": {
      "type": "string"
    },
    "path": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "pageContext": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "staticQueryHashes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "slicesMap": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /page-data/sq/d/353462786.json
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "site": {
          "type": "object",
          "properties": {
            "siteMetadata": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

