---
title: "APIs & Protocols: both-sides-the7eye-org-il_en"
date: 2026-11-14
target: "[[overview|both-sides-the7eye-org-il_en]]"
---

# Discovered APIs & Protocols: both-sides-the7eye-org-il_en

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/events.json` | `200` | REST endpoint |
| `GET` | `/events-en.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /events.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "rowId": {
        "type": "string"
      },
      "side": {
        "type": "string"
      },
      "actor": {
        "type": "string"
      },
      "category": {
        "type": "string"
      },
      "date": {
        "type": "string"
      },
      "descHeMedium": {
        "type": "string"
      },
      "crowd": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /events-en.json
```json
{
  "type": "object",
  "properties": {
    "row-5": {
      "type": "string"
    },
    "row-6": {
      "type": "string"
    },
    "row-7": {
      "type": "string"
    },
    "row-10": {
      "type": "string"
    },
    "row-11": {
      "type": "string"
    },
    "row-12": {
      "type": "string"
    },
    "row-13": {
      "type": "string"
    },
    "row-18": {
      "type": "string"
    },
    "row-22": {
      "type": "string"
    },
    "row-24": {
      "type": "string"
    },
    "row-26": {
      "type": "string"
    },
    "row-27": {
      "type": "string"
    },
    "row-28": {
      "type": "string"
    },
    "row-29": {
      "type": "string"
    },
    "row-30": {
      "type": "string"
    },
    "row-31": {
      "type": "string"
    },
    "row-32": {
      "type": "string"
    },
    "row-33": {
      "type": "string"
    },
    "row-34": {
      "type": "string"
    },
    "row-35": {
      "type": "string"
    }
  }
}
```

