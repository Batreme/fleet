---
title: "APIs & Protocols: re-cycle-org"
date: 2026-11-14
target: "re-cycle-org"
---

# Discovered APIs & Protocols: re-cycle-org

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/frontend_data/v2` | `200` | REST endpoint |
| `POST` | `/frontend_data/v2` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /frontend_data/v2
```json
{
  "type": "object",
  "properties": {
    "event_token": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "operation_status": {
          "type": "string"
        }
      }
    },
    "error_no": {
      "type": "number"
    },
    "error_message": {
      "type": "string"
    },
    "error_trace": {
      "type": "string"
    },
    "host_name": {
      "type": "string"
    },
    "page_url": {
      "type": "string"
    },
    "ip_version": {
      "type": "number"
    }
  }
}
```
### `POST` /frontend_data/v2
```json
{
  "type": "object",
  "properties": {
    "event_token": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "operation_status": {
          "type": "string"
        }
      }
    },
    "error_no": {
      "type": "number"
    },
    "error_message": {
      "type": "string"
    },
    "error_trace": {
      "type": "string"
    },
    "host_name": {
      "type": "string"
    },
    "page_url": {
      "type": "string"
    },
    "ip_version": {
      "type": "number"
    }
  }
}
```

