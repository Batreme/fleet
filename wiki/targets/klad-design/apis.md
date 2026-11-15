---
title: "APIs & Protocols: klad-design"
date: 2026-11-14
target: "klad-design"
---

# Discovered APIs & Protocols: klad-design

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/images/team/v1/0.avif` | `200` | REST endpoint |
| `GET` | `/pixel-config/v1/2F1igqdAReuX4NLvTBfvfv.json` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /pixel-config/v1/2F1igqdAReuX4NLvTBfvfv.json
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

