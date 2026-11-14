---
title: "APIs & Protocols: fromearth-love"
date: 2026-11-14
target: "[[overview|fromearth-love]]"
---

# Discovered APIs & Protocols: fromearth-love

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/data/flood-metadata.json` | `200` | REST endpoint |
| `GET` | `/data/climate-manifest.json` | `200` | REST endpoint |
| `GET` | `/data/fire-weather.json` | `200` | REST endpoint |
| `GET` | `/data/flood-cities.json` | `200` | REST endpoint |
| `GET` | `/data/places.json` | `200` | REST endpoint |
| `GET` | `/data/flood-metadata.json` | `200` | REST endpoint |
| `GET` | `/data/population-annual.json` | `200` | REST endpoint |
| `GET` | `/data/places.json` | `200` | REST endpoint |
| `POST` | `/cdn-cgi/rum` | `204` | REST endpoint |
| `GET` | `/data/places.json` | `200` | REST endpoint |
| `GET` | `/data/place-search.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /data/flood-metadata.json
```json
{
  "type": "object",
  "properties": {
    "abi": {
      "type": "string"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "crs": {
      "type": "string"
    },
    "bounds": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "row_order": {
      "type": "string"
    },
    "column_order": {
      "type": "string"
    },
    "pixel_center": {
      "type": "object",
      "properties": {
        "lon": {
          "type": "string"
        },
        "lat": {
          "type": "string"
        }
      }
    },
    "transform": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "encoding": {
      "type": "string"
    },
    "decoded_dtype": {
      "type": "string"
    },
    "byte_order": {
      "type": "string"
    },
    "layout": {
      "type": "string"
    },
    "index": {
      "type": "string"
    },
    "nodata": {
      "type": "string"
    },
    "sampling": {
      "type": "string"
    },
    "missing": {
      "type": "string"
    },
    "coverage": {
      "type": "string"
    },
    "aggregation": {
      "type": "string"
    },
    "return_period_years": {
      "type": "number"
    }
  }
}
```
### `GET` /data/climate-manifest.json
```json
{
  "type": "object",
  "properties": {
    "sources": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "period": {
            "type": "any"
          },
          "variable": {
            "type": "any"
          },
          "filename": {
            "type": "any"
          },
          "url": {
            "type": "any"
          },
          "resolved_url": {
            "type": "any"
          },
          "sha256": {
            "type": "any"
          },
          "bytes": {
            "type": "any"
          },
          "retrieved_utc": {
            "type": "any"
          },
          "last_modified": {
            "type": "any"
          }
        }
      }
    },
    "citations": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "disclosures": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "verification_samples": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "period": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "latitude": {
            "type": "any"
          },
          "longitude": {
            "type": "any"
          },
          "row": {
            "type": "any"
          },
          "column": {
            "type": "any"
          },
          "mask": {
            "type": "any"
          },
          "values": {
            "type": "any"
          }
        }
      }
    },
    "abi": {
      "type": "string"
    },
    "shape": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "dtype": {
      "type": "string"
    },
    "compression": {
      "type": "string"
    },
    "nodata": {
      "type": "string"
    },
    "layout": {
      "type": "string"
    },
    "byte_offset": {
      "type": "string"
    },
    "fields": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "unit": {
            "type": "any"
          },
          "formula": {
            "type": "any"
          },
          "note": {
            "type": "any"
          },
          "period": {
            "type": "any"
          },
          "index": {
            "type": "any"
          }
        }
      }
    },
    "crs": {
      "type": "string"
    },
    "bounds": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "resolution_degrees": {
      "type": "number"
    },
    "cell_center": {
      "type": "object",
      "properties": {
        "longitude": {
          "type": "string"
        },
        "latitude": {
          "type": "string"
        }
      }
    },
    "aggregation": {
      "type": "string"
    },
    "coverage_definition": {
      "type": "string"
    }
  }
}
```
### `GET` /data/fire-weather.json
```json
{
  "type": "object",
  "properties": {
    "source": {
      "type": "string"
    },
    "doi": {
      "type": "string"
    },
    "archive": {
      "type": "string"
    },
    "archiveChecksum": {
      "type": "object",
      "properties": {
        "checkSumAlgorithm": {
          "type": "string"
        },
        "value": {
          "type": "string"
        }
      }
    },
    "scenario": {
      "type": "string"
    },
    "members": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model": {
            "type": "any"
          },
          "file": {
            "type": "any"
          },
          "sha256": {
            "type": "any"
          },
          "crc32": {
            "type": "any"
          }
        }
      }
    },
    "schema": {
      "type": "number"
    },
    "metric": {
      "type": "string"
    },
    "units": {
      "type": "string"
    },
    "thresholdReference": {
      "type": "string"
    },
    "historicalPeriod": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "nearPeriod": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "futurePeriod": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "nearLabelYear": {
      "type": "number"
    },
    "futureLabelYear": {
      "type": "number"
    },
    "timeline": {
      "type": "string"
    },
    "ensemble": {
      "type": "string"
    },
    "modelCount": {
      "type": "number"
    },
    "models": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "biasCorrection": {
      "type": "boolean"
    }
  }
}
```
### `GET` /data/flood-cities.json
```json
{
  "type": "object",
  "properties": {
    "abi": {
      "type": "string"
    },
    "file": {
      "type": "string"
    },
    "fields": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "count": {
      "type": "number"
    },
    "encoding": {
      "type": "string"
    },
    "layout": {
      "type": "string"
    },
    "index": {
      "type": "string"
    },
    "nodata": {
      "type": "string"
    },
    "places_file": {
      "type": "string"
    },
    "places_sha256": {
      "type": "string"
    },
    "coordinates_file": {
      "type": "string"
    },
    "coordinates_sha256": {
      "type": "string"
    },
    "coordinates_encoding": {
      "type": "string"
    },
    "coordinate_precision_degrees": {
      "type": "number"
    },
    "native_resolution_arcseconds": {
      "type": "number"
    },
    "sampling": {
      "type": "string"
    },
    "interpretation": {
      "type": "string"
    },
    "return_period_years": {
      "type": "number"
    },
    "sha256": {
      "type": "string"
    },
    "decoded_sha256": {
      "type": "string"
    }
  }
}
```
### `GET` /data/places.json
```json
{
  "type": "object",
  "properties": {
    "schema": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "villes": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    }
  }
}
```
### `GET` /data/flood-metadata.json
```json
{
  "type": "object",
  "properties": {
    "abi": {
      "type": "string"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "crs": {
      "type": "string"
    },
    "bounds": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "row_order": {
      "type": "string"
    },
    "column_order": {
      "type": "string"
    },
    "pixel_center": {
      "type": "object",
      "properties": {
        "lon": {
          "type": "string"
        },
        "lat": {
          "type": "string"
        }
      }
    },
    "transform": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "encoding": {
      "type": "string"
    },
    "decoded_dtype": {
      "type": "string"
    },
    "byte_order": {
      "type": "string"
    },
    "layout": {
      "type": "string"
    },
    "index": {
      "type": "string"
    },
    "nodata": {
      "type": "string"
    },
    "sampling": {
      "type": "string"
    },
    "missing": {
      "type": "string"
    },
    "coverage": {
      "type": "string"
    },
    "aggregation": {
      "type": "string"
    },
    "return_period_years": {
      "type": "number"
    }
  }
}
```
### `GET` /data/population-annual.json
```json
{
  "type": "object",
  "properties": {
    "AD": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AE": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AF": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AG": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AI": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AL": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AM": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AO": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AR": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AS": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AT": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AU": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AW": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "AZ": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "BA": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "BB": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "BD": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "BE": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "BF": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "BG": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /data/places.json
```json
{
  "type": "object",
  "properties": {
    "schema": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "villes": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    }
  }
}
```
### `GET` /data/places.json
```json
{
  "type": "object",
  "properties": {
    "schema": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "villes": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    }
  }
}
```

