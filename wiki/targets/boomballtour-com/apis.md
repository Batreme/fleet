---
title: "APIs & Protocols: boomballtour-com"
date: 2026-11-14
target: "boomballtour-com"
---

# Discovered APIs & Protocols: boomballtour-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/view` | `200` | REST endpoint |
| `GET` | `/v3/geolocate/json` | `200` | REST endpoint |
| `POST` | `/` | `200` | REST endpoint |
| `POST` | `/api/v2/pixel` | `200` | REST endpoint |
| `POST` | `/api/v2/pixel` | `200` | REST endpoint |
| `POST` | `/api/v2/pixel/act` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /v3/geolocate/json
```json
{
  "type": "object",
  "properties": {
    "ip": {
      "type": "string"
    },
    "region_name": {
      "type": "string"
    },
    "region_code": {
      "type": "string"
    },
    "country": {
      "type": "string"
    },
    "country_eu": {
      "type": "boolean"
    },
    "country_iso": {
      "type": "string"
    },
    "city": {
      "type": "string"
    },
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "zip_code": {
      "type": "string"
    },
    "time_zone": {
      "type": "string"
    }
  }
}
```
### `POST` /
```json
{
  "type": "object",
  "properties": {
    "fragments": {
      "type": "object",
      "properties": {
        ".fkcart-modal-container": {
          "type": "string"
        },
        ".fkcart-mini-toggler": {
          "type": "string"
        },
        "fkcart_qty": {
          "type": "number"
        },
        "fkcart_total": {
          "type": "string"
        }
      }
    },
    "ajax_nonce": {
      "type": "string"
    },
    "fkcart_re_run_slide_cart": {
      "type": "string"
    },
    "cart_hash": {
      "type": "string"
    },
    "code": {
      "type": "number"
    },
    "status": {
      "type": "boolean"
    },
    "message": {
      "type": "string"
    }
  }
}
```

