---
title: "APIs & Protocols: www-paragonproductions-co"
date: 2026-11-14
target: "www-paragonproductions-co"
---

# Discovered APIs & Protocols: www-paragonproductions-co

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/context-v2/117787750` | `200` | REST endpoint |
| `POST` | `/prediction/117787750` | `200` | REST endpoint |
| `POST` | `/logger` | `200` | REST endpoint |
| `POST` | `/logger` | `200` | REST endpoint |
| `GET` | `/api/v1/intent_pixel/can_track_visitor` | `200` | REST endpoint |
| `POST` | `/api/v1/intent_pixel/track_request` | `400` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /context-v2/117787750
```json
{
  "type": "object",
  "properties": {
    "requestId": {
      "type": "string"
    },
    "clientIp": {
      "type": "string"
    },
    "userAgentDigest": {
      "type": "string"
    },
    "userAgent": {
      "type": "object",
      "properties": {
        "deviceClass": {
          "type": "string"
        },
        "deviceName": {
          "type": "string"
        },
        "deviceBrand": {
          "type": "string"
        },
        "osClass": {
          "type": "string"
        },
        "osName": {
          "type": "string"
        },
        "osVersion": {
          "type": "string"
        },
        "agentClass": {
          "type": "string"
        },
        "agentName": {
          "type": "string"
        },
        "agentVersionMajor": {
          "type": "string"
        }
      }
    },
    "location": {
      "type": "object",
      "properties": {
        "countryIso": {
          "type": "string"
        },
        "countryName": {
          "type": "string"
        }
      }
    },
    "integrationData": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `POST` /prediction/117787750
```json
{
  "type": "object",
  "properties": {
    "policy": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "timestamp": {
          "type": "number"
        },
        "experiences": {
          "type": "object",
          "properties": {}
        }
      }
    }
  }
}
```
### `POST` /logger
```json
{
  "type": "object",
  "properties": {}
}
```
### `POST` /logger
```json
{
  "type": "object",
  "properties": {}
}
```
### `GET` /api/v1/intent_pixel/can_track_visitor
```json
{
  "type": "object",
  "properties": {
    "can_track": {
      "type": "boolean"
    }
  }
}
```
### `POST` /api/v1/intent_pixel/track_request
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  }
}
```

