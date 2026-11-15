---
title: "APIs & Protocols: www-bluesqx-com"
date: 2026-11-14
target: "www-bluesqx-com"
---

# Discovered APIs & Protocols: www-bluesqx-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/events` | `200` | REST endpoint |
| `GET` | `/v1/components/verify` | `200` | REST endpoint |
| `GET` | `/v1/components/verify` | `200` | REST endpoint |
| `GET` | `/v1/components/verify` | `200` | REST endpoint |
| `GET` | `/unified/v1/master/getSubscriptions` | `200` | REST endpoint |
| `POST` | `/data` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /v1/components/verify
```json
{
  "type": "object",
  "properties": {
    "valid": {
      "type": "boolean"
    }
  }
}
```
### `GET` /v1/components/verify
```json
{
  "type": "object",
  "properties": {
    "valid": {
      "type": "boolean"
    }
  }
}
```
### `GET` /v1/components/verify
```json
{
  "type": "object",
  "properties": {
    "valid": {
      "type": "boolean"
    }
  }
}
```
### `GET` /unified/v1/master/getSubscriptions
```json
{
  "type": "object",
  "properties": {
    "err": {
      "type": "boolean"
    },
    "subscriptions": {
      "type": "object",
      "properties": {
        "ws": {
          "type": "object",
          "properties": {
            "websiteId": {
              "type": "any"
            }
          }
        }
      }
    },
    "_zitok": {
      "type": "string"
    },
    "_vtok": {
      "type": "string"
    },
    "evi": {
      "type": "boolean"
    },
    "productUrls": {
      "type": "object",
      "properties": {
        "sch": {
          "type": "string"
        },
        "fc": {
          "type": "string"
        },
        "ws": {
          "type": "string"
        }
      }
    },
    "fcForms": {
      "type": "array",
      "items": "any"
    },
    "domainId": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "eventId": {
      "type": "string"
    }
  }
}
```
### `POST` /data
```json
{
  "type": "object",
  "properties": {
    "b": {
      "type": "string"
    },
    "tags": {
      "type": "string"
    }
  }
}
```

