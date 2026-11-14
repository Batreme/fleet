---
title: "APIs & Protocols: hopecancerresources-org"
date: 2026-11-14
target: "[[overview|hopecancerresources-org]]"
---

# Discovered APIs & Protocols: hopecancerresources-org

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/Content/Scripts/Api/Bloomerang-v2.js` | `200` | REST endpoint |
| `POST` | `/cdn-cgi/challenge-platform/h/b/precursor/f8df4d4a0cd6/0.9022723236724343:1794676231:nrRk5ESG8VPW2Cm7RCNXimfS5SHULqwF5vKrYaCOuYA/a5a7f62e281811c6` | `200` | REST endpoint |
| `POST` | `/v1/Widget/455680` | `200` | REST endpoint |
| `GET` | `/v3/` | `200` | REST endpoint |
| `GET` | `/v3/m-outer-0edadf75b42c6ef7240c043f3272f3f9.html` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/m-outer-df5ee3b49f88025f22168cdfc5823764.js` | `200` | REST endpoint |
| `POST` | `/6` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /cdn-cgi/challenge-platform/h/b/precursor/f8df4d4a0cd6/0.9022723236724343:1794676231:nrRk5ESG8VPW2Cm7RCNXimfS5SHULqwF5vKrYaCOuYA/a5a7f62e281811c6
```json
{
  "type": "object",
  "properties": {
    "i": {
      "type": "number"
    },
    "n": {
      "type": "boolean"
    }
  }
}
```
### `POST` /v1/Widget/455680
```json
{
  "type": "object",
  "properties": {
    "WidgetJavascript": {
      "type": "string"
    },
    "IsSuccess": {
      "type": "boolean"
    },
    "Id": {
      "type": "number"
    }
  }
}
```
### `POST` /6
```json
{
  "type": "object",
  "properties": {
    "muid": {
      "type": "string"
    },
    "guid": {
      "type": "string"
    },
    "sid": {
      "type": "string"
    }
  }
}
```

