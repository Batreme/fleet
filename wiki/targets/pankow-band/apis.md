---
title: "APIs & Protocols: pankow-band"
date: 2026-11-14
target: "[[overview|pankow-band]]"
---

# Discovered APIs & Protocols: pankow-band

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/pankow-kirby/json/diskographie.json` | `200` | REST endpoint |
| `GET` | `/pankow-kirby/json/videos.json` | `200` | REST endpoint |
| `GET` | `/pankow-kirby/json/chronik.json` | `200` | REST endpoint |
| `GET` | `/pankow-kirby/json/fangeschichten.json` | `200` | REST endpoint |
| `GET` | `/pankow-kirby/json/bilder.json` | `200` | REST endpoint |
| `GET` | `/pankow-kirby/json/hauptseite.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /pankow-kirby/json/diskographie.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "entry_id": {
        "type": "string"
      },
      "albumname": {
        "type": "string"
      },
      "erscheinungsjahr": {
        "type": "string"
      },
      "label": {
        "type": "string"
      },
      "albumkategorie": {
        "type": "string"
      },
      "coverbild_vorn_original": {
        "type": "string"
      },
      "coverbild_vorn_thumb": {
        "type": "string"
      },
      "coverbild_hinten_original": {
        "type": "null"
      },
      "coverbild_hinten_thumb": {
        "type": "null"
      },
      "streamspotify": {
        "type": "string"
      },
      "streamapple": {
        "type": "string"
      },
      "streamyoutube": {
        "type": "string"
      },
      "streamamazon": {
        "type": "string"
      },
      "streamtidal": {
        "type": "string"
      },
      "streamdeezer": {
        "type": "string"
      },
      "kaufen1": {
        "type": "string"
      },
      "kaufen2": {
        "type": "string"
      },
      "kaufen3": {
        "type": "string"
      },
      "trackliste": {
        "type": "string"
      },
      "albumweitereinfos": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /pankow-kirby/json/videos.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "entry_id": {
        "type": "string"
      },
      "titel": {
        "type": "string"
      },
      "ortlocation": {
        "type": "string"
      },
      "datum": {
        "type": "string"
      },
      "kategorie": {
        "type": "string"
      },
      "videolink": {
        "type": "string"
      },
      "embedcode": {
        "type": "string"
      },
      "thumbnail": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /pankow-kirby/json/chronik.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "entry_id": {
        "type": "string"
      },
      "zuordnungsdatum": {
        "type": "string"
      },
      "infohighlight": {
        "type": "string"
      },
      "spotlight": {
        "type": "string"
      },
      "tourtitel": {
        "type": "string"
      },
      "tourinfos": {
        "type": "string"
      },
      "tour": {
        "type": "string"
      },
      "infotext": {
        "type": "string"
      },
      "pressetext": {
        "type": "string"
      },
      "presselink": {
        "type": "string"
      },
      "presselinktext": {
        "type": "string"
      },
      "pressetext2": {
        "type": "string"
      },
      "presselink2": {
        "type": "string"
      },
      "presselinktext2": {
        "type": "string"
      },
      "pressetext3": {
        "type": "string"
      },
      "presselink3": {
        "type": "string"
      },
      "presselinktext3": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /pankow-kirby/json/fangeschichten.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "entry_id": {
        "type": "string"
      },
      "kategorie": {
        "type": "string"
      },
      "zuordnungsdatum": {
        "type": "string"
      },
      "storytitle": {
        "type": "string"
      },
      "storyhighlight": {
        "type": "string"
      },
      "story": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /pankow-kirby/json/bilder.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "entry_id": {
        "type": "string"
      },
      "titel": {
        "type": "string"
      },
      "alttext": {
        "type": "string"
      },
      "datum": {
        "type": "string"
      },
      "copyright": {
        "type": "string"
      },
      "copyrightlink": {
        "type": "string"
      },
      "bildinfos": {
        "type": "string"
      },
      "bild_original": {
        "type": "string"
      },
      "bild_thumb": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /pankow-kirby/json/hauptseite.json
```json
{
  "type": "object",
  "properties": {
    "entry_id": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "starttext": {
      "type": "string"
    },
    "kontakt": {
      "type": "string"
    },
    "sonstiges": {
      "type": "string"
    }
  }
}
```

