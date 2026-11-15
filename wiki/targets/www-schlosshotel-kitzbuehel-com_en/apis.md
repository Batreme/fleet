---
title: "APIs & Protocols: www-schlosshotel-kitzbuehel-com_en"
date: 2026-11-14
target: "www-schlosshotel-kitzbuehel-com_en"
---

# Discovered APIs & Protocols: www-schlosshotel-kitzbuehel-com_en

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/widget-config` | `200` | REST endpoint |
| `POST` | `/api/widget/ping` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/widget-config
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "domain": {
      "type": "string"
    },
    "color": {
      "type": "string"
    },
    "color_trigger": {
      "type": "string"
    },
    "size": {
      "type": "string"
    },
    "mail": {
      "type": "null"
    },
    "widget_position": {
      "type": "object",
      "properties": {
        "desktop": {
          "type": "string"
        },
        "tablet": {
          "type": "string"
        },
        "mobil": {
          "type": "string"
        }
      }
    },
    "user": {
      "type": "object",
      "properties": {
        "logo": {
          "type": "string"
        },
        "logo_negative": {
          "type": "string"
        }
      }
    }
  }
}
```
### `POST` /api/widget/ping
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    }
  }
}
```

