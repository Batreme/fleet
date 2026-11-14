---
title: "APIs & Protocols: cue-onebranding-webflow-io"
date: 2026-11-14
target: "[[overview|cue-onebranding-webflow-io]]"
---

# Discovered APIs & Protocols: cue-onebranding-webflow-io

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/player.js` | `200` | REST endpoint |
| `POST` | `/cookie-banner-public/v1/activity/view` | `204` | REST endpoint |
| `POST` | `/cdn-cgi/challenge-platform/h/b/precursor/f8df4d4a0cd6/0.9747044336468882:1794679828:vm66zsVz0PMNNilolybpbHUidBuLOW5TLJZhUcykc2c/a5a855990c279bf5` | `200` | REST endpoint |
| `GET` | `/api/v2/client/ws` | `101` | REST endpoint |
| `POST` | `/` | `200` | REST endpoint |
| `GET` | `/assets/js/blockedDomains.json` | `200` | REST endpoint |
| `GET` | `/api/forms/blockList` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /cdn-cgi/challenge-platform/h/b/precursor/f8df4d4a0cd6/0.9747044336468882:1794679828:vm66zsVz0PMNNilolybpbHUidBuLOW5TLJZhUcykc2c/a5a855990c279bf5
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
### `POST` /
```json
{
  "type": "object",
  "properties": {
    "content_uuid": {
      "type": "string"
    },
    "success": {
      "type": "boolean"
    }
  }
}
```
### `GET` /assets/js/blockedDomains.json
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```
### `GET` /api/forms/blockList
```json
{
  "type": "object",
  "properties": {
    "enabled": {
      "type": "boolean"
    },
    "additionalBlockedDomains": {
      "type": "array",
      "items": "any"
    }
  }
}
```

