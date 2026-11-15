---
title: "APIs & Protocols: white-desert-com"
date: 2026-11-14
target: "white-desert-com"
---

# Discovered APIs & Protocols: white-desert-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/v2/27087760/banner.js` | `200` | REST endpoint |
| `GET` | `/livechat-public/v1/message/public` | `200` | REST endpoint |
| `GET` | `/collected-forms/v1/config/json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /livechat-public/v1/message/public
```json
{
  "type": "object",
  "properties": {
    "@type": {
      "type": "string"
    },
    "metadata": {
      "type": "object",
      "properties": {
        "@type": {
          "type": "string"
        },
        "reason": {
          "type": "string"
        },
        "description": {
          "type": "string"
        }
      }
    },
    "type": {
      "type": "string"
    }
  }
}
```
### `GET` /collected-forms/v1/config/json
```json
{
  "type": "object",
  "properties": {
    "portalId": {
      "type": "number"
    },
    "submissionsApiDomain": {
      "type": "string"
    },
    "reportScraperTest": {
      "type": "boolean"
    },
    "formCaptureEnabled": {
      "type": "boolean"
    },
    "token": {
      "type": "number"
    }
  }
}
```

