---
title: "APIs & Protocols: b3xgraphics-com"
date: 2026-11-14
target: "b3xgraphics-com"
---

# Discovered APIs & Protocols: b3xgraphics-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/wp-content/plugins/b3x-core/assets/home/img/hero-blueprint.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /wp-content/plugins/b3x-core/assets/home/img/hero-blueprint.json
```json
{
  "type": "object",
  "properties": {
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "circles": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "cx": {
            "type": "any"
          },
          "cy": {
            "type": "any"
          },
          "r": {
            "type": "any"
          },
          "coverage": {
            "type": "any"
          },
          "startAngleDeg": {
            "type": "any"
          },
          "endAngleDeg": {
            "type": "any"
          }
        }
      }
    },
    "lines": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "x1": {
            "type": "any"
          },
          "y1": {
            "type": "any"
          },
          "x2": {
            "type": "any"
          },
          "y2": {
            "type": "any"
          },
          "len": {
            "type": "any"
          }
        }
      }
    },
    "ticks": {
      "type": "object",
      "properties": {
        "rulerX1": {
          "type": "number"
        },
        "rulerY1": {
          "type": "number"
        },
        "rulerX2": {
          "type": "number"
        },
        "rulerY2": {
          "type": "number"
        },
        "spacingPx": {
          "type": "number"
        },
        "tickLenPx": {
          "type": "number"
        },
        "oneSided": {
          "type": "boolean"
        }
      }
    },
    "tickSegments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "x1": {
            "type": "any"
          },
          "y1": {
            "type": "any"
          },
          "x2": {
            "type": "any"
          },
          "y2": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

