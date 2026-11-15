---
title: "APIs & Protocols: matchball-today"
date: 2026-11-14
target: "matchball-today"
---

# Discovered APIs & Protocols: matchball-today

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/sonidos/sonidos.json` | `200` | REST endpoint |
| `GET` | `/api/portada` | `200` | REST endpoint |
| `POST` | `/cdn-cgi/rum` | `204` | REST endpoint |
| `GET` | `/api/modelo/a3KiE5p2TsG94kb3jtDvBB` | `200` | REST endpoint |
| `GET` | `/api/modelo/6RKLLVOM3DMr8UMC0tpFnU` | `200` | REST endpoint |
| `GET` | `/api/modelo/jZI_VTGROgpELh0eJOgWOA` | `200` | REST endpoint |
| `GET` | `/api/modelo/eF_Bar3Gn4WVe80Ztynzpa` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /sonidos/sonidos.json
```json
{
  "type": "object",
  "properties": {
    "bote": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "choque": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "toque": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "chut": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "poste": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "red": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "parada": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "silbato": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "ambiente": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "ovacion": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "lamento": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "tramo": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "nombrado": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "musica": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /api/portada
```json
{
  "type": "object",
  "properties": {
    "modelos": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "nitidos": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

