---
title: "APIs & Protocols: midnightvideo-cuchillo-rocks"
date: 2026-11-14
target: "[[overview|midnightvideo-cuchillo-rocks]]"
---

# Discovered APIs & Protocols: midnightvideo-cuchillo-rocks

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/send` | `200` | REST endpoint |
| `GET` | `/catalog/current.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/send
```json
{
  "type": "object",
  "properties": {
    "cache": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "visitId": {
      "type": "string"
    }
  }
}
```
### `GET` /catalog/current.json
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string"
    },
    "path": {
      "type": "string"
    },
    "films": {
      "type": "number"
    },
    "withPoster": {
      "type": "number"
    },
    "generatedAt": {
      "type": "string"
    },
    "publishedAt": {
      "type": "string"
    }
  }
}
```

