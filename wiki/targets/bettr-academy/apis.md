---
title: "APIs & Protocols: bettr-academy"
date: 2026-11-14
target: "[[overview|bettr-academy]]"
---

# Discovered APIs & Protocols: bettr-academy

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/license` | `200` | REST endpoint |
| `GET` | `/` | `200` | REST endpoint |
| `GET` | `/api/v3/cookie-consent/sites/getAllSiteServiceSettings/69f15930f71b5763616e2c5c` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/license
```json
{
  "type": "object",
  "properties": {
    "siteId": {
      "type": "string"
    },
    "appName": {
      "type": "string"
    },
    "active": {
      "type": "boolean"
    }
  }
}
```
### `GET` /
```json
{
  "type": "object",
  "properties": {
    "over": {
      "type": "boolean"
    },
    "site_id": {
      "type": "number"
    }
  }
}
```
### `GET` /api/v3/cookie-consent/sites/getAllSiteServiceSettings/69f15930f71b5763616e2c5c
```json
{
  "type": "object",
  "properties": {
    "googleAnalyticsId": {
      "type": "string"
    },
    "googleAnalyticsRequiredConsents": {
      "type": "null"
    },
    "useGoogleTagManager": {
      "type": "boolean"
    },
    "facebookPixelId": {
      "type": "string"
    },
    "facebookPixelRequiredConsents": {
      "type": "null"
    },
    "googleTagManagerId": {
      "type": "string"
    },
    "zendeskId": {
      "type": "string"
    },
    "zendeskRequiredConsents": {
      "type": "null"
    },
    "tikTokPixelId": {
      "type": "string"
    },
    "tikTokPixelRequiredConsents": {
      "type": "null"
    },
    "linkedInInsightTagId": {
      "type": "string"
    },
    "linkedInInsightTagRequiredConsents": {
      "type": "null"
    },
    "hotjarId": {
      "type": "string"
    },
    "hotjarRequiredConsents": {
      "type": "null"
    },
    "consentStoringEndpoint": {
      "type": "null"
    },
    "consentWebhookEndpoint": {
      "type": "null"
    },
    "cookiePopupShowingSide": {
      "type": "string"
    },
    "cookiePopupDelay": {
      "type": "number"
    },
    "cookiePopupShowingRegion": {
      "type": "string"
    },
    "hideCookieButton": {
      "type": "boolean"
    }
  }
}
```

