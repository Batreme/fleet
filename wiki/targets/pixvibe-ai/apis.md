---
title: "APIs & Protocols: pixvibe-ai"
date: 2026-11-14
target: "[[overview|pixvibe-ai]]"
---

# Discovered APIs & Protocols: pixvibe-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/v2/css` | `200` | REST endpoint |
| `GET` | `/logicSrv/PixVibeAPI/pricing/v1/plans` | `200` | REST endpoint |
| `POST` | `/logicSrv/PixVibeAPI/guest/v1/token` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /logicSrv/PixVibeAPI/pricing/v1/plans
```json
{
  "type": "object",
  "properties": {
    "Code": {
      "type": "string"
    },
    "Msg": {
      "type": "string"
    },
    "Data": {
      "type": "object",
      "properties": {
        "List": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "GuestMaxCredits": {
          "type": "number"
        },
        "FreeCreditsPerDay": {
          "type": "number"
        }
      }
    },
    "Ts": {
      "type": "number"
    },
    "RequestId": {
      "type": "string"
    }
  }
}
```
### `POST` /logicSrv/PixVibeAPI/guest/v1/token
```json
{
  "type": "object",
  "properties": {
    "ExpiresAt": {
      "type": "number"
    },
    "MaxCredits": {
      "type": "number"
    },
    "Token": {
      "type": "string"
    },
    "UsedCredits": {
      "type": "number"
    }
  }
}
```

