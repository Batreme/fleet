---
title: "APIs & Protocols: vadimcarazan-com"
date: 2026-10-31
target: "[[overview|vadimcarazan-com]]"
---

# Discovered APIs & Protocols: vadimcarazan-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/data/cosmos.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /data/cosmos.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "number"
    },
    "D0": {
      "type": "number"
    },
    "cols": {
      "type": "number"
    },
    "rows": {
      "type": "number"
    },
    "cell": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "aspect": {
      "type": "number"
    },
    "period": {
      "type": "number"
    },
    "travel": {
      "type": "number"
    },
    "atlases": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "src": {
            "type": "any"
          },
          "cols": {
            "type": "any"
          },
          "rows": {
            "type": "any"
          }
        }
      }
    },
    "projects": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "t": {
            "type": "any"
          },
          "d": {
            "type": "any"
          },
          "s": {
            "type": "any"
          },
          "u": {
            "type": "any"
          },
          "g": {
            "type": "any"
          },
          "m": {
            "type": "any"
          },
          "k": {
            "type": "any"
          }
        }
      }
    },
    "images": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    },
    "cells": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    },
    "seq": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  }
}
```

