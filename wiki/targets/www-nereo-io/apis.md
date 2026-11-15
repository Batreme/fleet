---
title: "APIs & Protocols: www-nereo-io"
date: 2026-11-14
target: "www-nereo-io"
---

# Discovered APIs & Protocols: www-nereo-io

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/affiliate/status` | `200` | REST endpoint |
| `GET` | `/api/geolocation` | `200` | REST endpoint |
| `GET` | `/api/auth/session` | `200` | REST endpoint |
| `GET` | `/api/auth/session` | `200` | REST endpoint |
| `GET` | `/api/affiliate/offer` | `200` | REST endpoint |
| `GET` | `/pixels/a2_hp2oyzvcydgd/config` | `200` | REST endpoint |
| `GET` | `/gsi/status` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/affiliate/status
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "state": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /api/geolocation
```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "number"
    },
    "message": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "countryCode": {
          "type": "string"
        },
        "country": {
          "type": "string"
        },
        "region": {
          "type": "null"
        },
        "city": {
          "type": "null"
        },
        "ip": {
          "type": "string"
        },
        "userAgent": {
          "type": "string"
        },
        "detected": {
          "type": "boolean"
        },
        "source": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /api/auth/session
```json
{
  "type": "null"
}
```
### `GET` /api/auth/session
```json
{
  "type": "null"
}
```
### `GET` /api/affiliate/offer
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "data": {
      "type": "null"
    }
  }
}
```
### `GET` /pixels/a2_hp2oyzvcydgd/config
```json
{
  "type": "object",
  "properties": {
    "pixelEventConfigs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "trackingType": {
            "type": "any"
          },
          "triggers": {
            "type": "any"
          }
        }
      }
    },
    "aam": {
      "type": "object",
      "properties": {
        "email": {
          "type": "boolean"
        }
      }
    },
    "esc": {
      "type": "object",
      "properties": {
        "page_metadata": {
          "type": "boolean"
        }
      }
    }
  }
}
```

