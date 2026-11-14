---
title: "APIs & Protocols: sixescricket-com"
date: 2026-11-14
target: "[[overview|sixescricket-com]]"
---

# Discovered APIs & Protocols: sixescricket-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consentconfig/8473bd6d-ff6d-4fb6-83df-e5f62c59643a/settings.json` | `200` | REST endpoint |
| `GET` | `/v1/chunk/OEdXQAazMK02K1IWX1FDdTdzn2Mz2lAzKaLqQ6LeeSx64tIunatbiAtg015aMuwby02sgxvqqiM8MZEjIbiJHx3NQ/18446744073709551615.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/OEdXQAazMK02K1IWX1FDdTdzn2Mz2lAzKaLqQ6LeeSx64tIunatbiAtg015aMuwby02sgxvqqiM8MZEjIbiJHx3NQ/0.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/OEdXQAazMK02K1IWX1FDdTdzn2Mz2lAzKaLqQ6LeeSx64tIunatbiAtg015aMuwby02sgxvqqiM8MZEjIbiJHx3NQ/18446744073709551615.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/OEdXQAazMK02K1IWX1FDdTdzn2Mz2lAzKaLqQ6LeeSx64tIunatbiAtg015aMuwby02sgxvqqiM8MZEjIbiJHx3NQ/0.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/Id00RIinsxTVMV7MjT01Uaa2Ycoh4i1xzYOWHYzT8dsgDVdosNS00WmVuwB02p6SpDC02RPmilev602K01KwlXO00YFFzInypwgTWs7H/18446744073709551615.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/Id00RIinsxTVMV7MjT01Uaa2Ycoh4i1xzYOWHYzT8dsgDVdosNS00WmVuwB02p6SpDC02RPmilev602K01KwlXO00YFFzInypwgTWs7H/0.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/Id00RIinsxTVMV7MjT01Uaa2Ycoh4i1xzYOWHYzT8dsgDVdosNS00WmVuwB02p6SpDC02RPmilev602K01KwlXO00YFFzInypwgTWs7H/18446744073709551615.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/Id00RIinsxTVMV7MjT01Uaa2Ycoh4i1xzYOWHYzT8dsgDVdosNS00WmVuwB02p6SpDC02RPmilev602K01KwlXO00YFFzInypwgTWs7H/0.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/Id00RIinsxTVMV7MjT01Uaa2Ycoh4i1xzYOWHYzT8dsgDVdosNS00WmVuwB02p6SpDC02RPmilev602K01KwlXO00YFFzInypwgTWs7H/1.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/Id00RIinsxTVMV7MjT01Uaa2Ycoh4i1xzYOWHYzT8dsgDVdosNS00WmVuwB02p6SpDC02RPmilev602K01KwlXO00YFFzInypwgTWs7H/1.m4s` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consentconfig/8473bd6d-ff6d-4fb6-83df-e5f62c59643a/settings.json
```json
{
  "type": "object",
  "properties": {
    "widget": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "position": {
          "type": "object",
          "properties": {
            "position": {
              "type": "any"
            },
            "distanceVerticalPx": {
              "type": "any"
            },
            "distanceHorizontalPx": {
              "type": "any"
            }
          }
        },
        "theme": {
          "type": "object",
          "properties": {
            "closed": {
              "type": "any"
            },
            "opened": {
              "type": "any"
            }
          }
        },
        "content": {
          "type": "object",
          "properties": {
            "cultures": {
              "type": "any"
            },
            "default": {
              "type": "any"
            },
            "autodetectLanguage": {
              "type": "any"
            }
          }
        }
      }
    },
    "twipla": {
      "type": "null"
    }
  }
}
```

