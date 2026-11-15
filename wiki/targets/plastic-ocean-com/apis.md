---
title: "APIs & Protocols: plastic-ocean-com"
date: 2026-11-14
target: "plastic-ocean-com"
---

# Discovered APIs & Protocols: plastic-ocean-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/vkid_sdk_get_config` | `200` | REST endpoint |
| `POST` | `/stat_events_vkid_sdk` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /vkid_sdk_get_config
```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "object",
      "properties": {
        "error_msg": {
          "type": "string"
        }
      }
    }
  }
}
```
### `POST` /stat_events_vkid_sdk
```json
{
  "type": "object",
  "properties": {
    "failed_ids": {
      "type": "array",
      "items": "any"
    }
  }
}
```

