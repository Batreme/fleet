---
title: "APIs & Protocols: hoyojerez-com"
date: 2026-11-14
target: "[[overview|hoyojerez-com]]"
---

# Discovered APIs & Protocols: hoyojerez-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/eventos.json` | `200` | REST endpoint |
| `GET` | `/api/galeria.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/eventos.json
```json
{
  "type": "object",
  "properties": {
    "fuente": {
      "type": "string"
    },
    "eventos": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nombre": {
            "type": "any"
          },
          "fecha": {
            "type": "any"
          },
          "fechaLarga": {
            "type": "any"
          },
          "hora": {
            "type": "any"
          },
          "horaFin": {
            "type": "any"
          },
          "diaSemana": {
            "type": "any"
          },
          "descripcion": {
            "type": "any"
          },
          "url": {
            "type": "any"
          },
          "imagen": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/galeria.json
```json
{
  "type": "object",
  "properties": {
    "fuente": {
      "type": "string"
    },
    "fiestas": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nombre": {
            "type": "any"
          },
          "fecha": {
            "type": "any"
          },
          "fotos": {
            "type": "any"
          },
          "miniaturas": {
            "type": "any"
          },
          "portada": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

