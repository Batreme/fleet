---
title: "APIs & Protocols: mrcresidencesbocaraton-com"
date: 2026-11-14
target: "[[overview|mrcresidencesbocaraton-com]]"
---

# Discovered APIs & Protocols: mrcresidencesbocaraton-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/pixel-config/v1/CdtyzNRHM89c3WuLsJAEgf.json` | `200` | REST endpoint |
| `POST` | `/group/0/68b4700b4d338e93e39a/12/swap_session.json` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /pixel-config/v1/CdtyzNRHM89c3WuLsJAEgf.json
```json
{
  "type": "object",
  "properties": {
    "automatic_advanced_matching_enabled": {
      "type": "boolean"
    }
  }
}
```
### `POST` /group/0/68b4700b4d338e93e39a/12/swap_session.json
```json
{
  "type": "object",
  "properties": {
    "a": {
      "type": "object",
      "properties": {
        "320876232": {
          "type": "object",
          "properties": {
            "5616773921": {
              "type": "any"
            },
            "5614319199": {
              "type": "any"
            }
          }
        }
      }
    },
    "r": {
      "type": "object",
      "properties": {}
    },
    "domless": {
      "type": "boolean"
    },
    "number_assignment": {
      "type": "boolean"
    },
    "integration_retry": {
      "type": "boolean"
    },
    "integration_retries": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  }
}
```

