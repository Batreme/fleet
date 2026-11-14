---
title: "APIs & Protocols: seedrouter-ai"
date: 2026-11-14
target: "[[overview|seedrouter-ai]]"
---

# Discovered APIs & Protocols: seedrouter-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/script.js` | `200` | REST endpoint |
| `GET` | `/api/auth/get-session` | `200` | REST endpoint |
| `GET` | `/api/analytics/x/events` | `200` | REST endpoint |
| `GET` | `/api/site/tracking-config/f69abe718e34` | `200` | REST endpoint |
| `POST` | `/api/track` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/auth/get-session
```json
{
  "type": "null"
}
```
### `GET` /api/analytics/x/events
```json
{
  "type": "object",
  "properties": {
    "events": {
      "type": "array",
      "items": "any"
    },
    "pending": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/site/tracking-config/f69abe718e34
```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "featureFlagsEnabled": {
      "type": "boolean"
    },
    "sessionReplay": {
      "type": "boolean"
    },
    "webVitals": {
      "type": "boolean"
    },
    "trackErrors": {
      "type": "boolean"
    },
    "trackOutbound": {
      "type": "boolean"
    },
    "trackUrlParams": {
      "type": "boolean"
    },
    "trackInitialPageView": {
      "type": "boolean"
    },
    "trackSpaNavigation": {
      "type": "boolean"
    },
    "trackButtonClicks": {
      "type": "boolean"
    },
    "trackCopy": {
      "type": "boolean"
    },
    "trackFormInteractions": {
      "type": "boolean"
    }
  }
}
```
### `POST` /api/track
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```

