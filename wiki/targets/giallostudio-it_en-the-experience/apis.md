---
title: "APIs & Protocols: giallostudio-it_en-the-experience"
date: 2026-11-14
target: "giallostudio-it_en-the-experience"
---

# Discovered APIs & Protocols: giallostudio-it_en-the-experience

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/experience/city/manifest.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /experience/city/manifest.json
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "number"
    },
    "bakedAt": {
      "type": "string"
    },
    "frame": {
      "type": "object",
      "properties": {
        "axes": {
          "type": "string"
        },
        "projection": {
          "type": "string"
        },
        "groundY": {
          "type": "number"
        },
        "layerY": {
          "type": "object",
          "properties": {
            "board": {
              "type": "any"
            },
            "yard": {
              "type": "any"
            },
            "square": {
              "type": "any"
            },
            "parking": {
              "type": "any"
            },
            "grass": {
              "type": "any"
            },
            "pedestrian": {
              "type": "any"
            },
            "water": {
              "type": "any"
            },
            "canal": {
              "type": "any"
            },
            "carriageway": {
              "type": "any"
            },
            "path": {
              "type": "any"
            },
            "road": {
              "type": "any"
            },
            "island": {
              "type": "any"
            },
            "rail": {
              "type": "any"
            },
            "parks": {
              "type": "any"
            },
            "roads": {
              "type": "any"
            },
            "rails": {
              "type": "any"
            }
          }
        }
      }
    },
    "center": {
      "type": "object",
      "properties": {
        "lat": {
          "type": "number"
        },
        "lon": {
          "type": "number"
        }
      }
    },
    "metersPerDegree": {
      "type": "object",
      "properties": {
        "lat": {
          "type": "number"
        },
        "lon": {
          "type": "number"
        }
      }
    },
    "extent": {
      "type": "number"
    },
    "bbox": {
      "type": "object",
      "properties": {
        "south": {
          "type": "number"
        },
        "west": {
          "type": "number"
        },
        "north": {
          "type": "number"
        },
        "east": {
          "type": "number"
        }
      }
    },
    "requestedArea": {
      "type": "object",
      "properties": {
        "south": {
          "type": "number"
        },
        "west": {
          "type": "number"
        },
        "north": {
          "type": "number"
        },
        "east": {
          "type": "number"
        }
      }
    },
    "uv": {
      "type": "string"
    },
    "lods": {
      "type": "object",
      "properties": {
        "high": {
          "type": "object",
          "properties": {
            "buildings": {
              "type": "any"
            },
            "ground": {
              "type": "any"
            },
            "trees": {
              "type": "any"
            }
          }
        },
        "low": {
          "type": "object",
          "properties": {
            "buildings": {
              "type": "any"
            },
            "ground": {
              "type": "any"
            },
            "trees": {
              "type": "any"
            }
          }
        }
      }
    },
    "ground": {
      "type": "object",
      "properties": {
        "landuse": {
          "type": "object",
          "properties": {
            "0": {
              "type": "any"
            },
            "1": {
              "type": "any"
            },
            "2": {
              "type": "any"
            },
            "3": {
              "type": "any"
            },
            "4": {
              "type": "any"
            },
            "5": {
              "type": "any"
            }
          }
        },
        "sections": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "note": {
          "type": "string"
        }
      }
    },
    "styles": {
      "type": "object",
      "properties": {
        "0": {
          "type": "string"
        },
        "1": {
          "type": "string"
        },
        "2": {
          "type": "string"
        },
        "3": {
          "type": "string"
        }
      }
    },
    "roofs": {
      "type": "object",
      "properties": {
        "0": {
          "type": "string"
        },
        "1": {
          "type": "string"
        },
        "2": {
          "type": "string"
        },
        "3": {
          "type": "string"
        }
      }
    },
    "trees": {
      "type": "object",
      "properties": {
        "kinds": {
          "type": "object",
          "properties": {
            "0": {
              "type": "any"
            },
            "1": {
              "type": "any"
            },
            "2": {
              "type": "any"
            },
            "3": {
              "type": "any"
            }
          }
        },
        "note": {
          "type": "string"
        }
      }
    },
    "metro": {
      "type": "object",
      "properties": {
        "file": {
          "type": "string"
        },
        "bytes": {
          "type": "number"
        },
        "lines": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "spread": {
      "type": "object",
      "properties": {
        "files": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "meaning": {
          "type": "string"
        },
        "tMaxSeconds": {
          "type": "number"
        }
      }
    },
    "origin": {
      "type": "object",
      "properties": {
        "buildingIndex": {
          "type": "number"
        },
        "osm": {
          "type": "string"
        },
        "name": {
          "type": "null"
        },
        "tags": {
          "type": "object",
          "properties": {
            "building": {
              "type": "any"
            },
            "levels": {
              "type": "any"
            },
            "height": {
              "type": "any"
            },
            "office": {
              "type": "any"
            }
          }
        },
        "latlon": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "height": {
          "type": "number"
        },
        "levels": {
          "type": "number"
        },
        "center": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "windowPoint": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "windowNormal": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "wallDir": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "wallLength": {
          "type": "number"
        },
        "windowWallUV": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "windowFloor": {
          "type": "number"
        },
        "streetClearance": {
          "type": "number"
        },
        "approachPoint": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "spreadAtOrigin": {
          "type": "number"
        }
      }
    },
    "districts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "sector": {
            "type": "any"
          },
          "label_it": {
            "type": "any"
          },
          "label_en": {
            "type": "any"
          },
          "place": {
            "type": "any"
          },
          "href": {
            "type": "any"
          },
          "center": {
            "type": "any"
          },
          "radius": {
            "type": "any"
          },
          "latlon": {
            "type": "any"
          }
        }
      }
    },
    "landmarks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "any"
          },
          "found": {
            "type": "any"
          },
          "osm": {
            "type": "any"
          },
          "parts": {
            "type": "any"
          },
          "maxHeight": {
            "type": "any"
          },
          "center": {
            "type": "any"
          },
          "inHigh": {
            "type": "any"
          },
          "inLow": {
            "type": "any"
          }
        }
      }
    },
    "attribution": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

