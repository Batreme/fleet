---
title: "APIs & Protocols: bennos-light-org"
date: 2026-11-14
target: "bennos-light-org"
---

# Discovered APIs & Protocols: bennos-light-org

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consentconfig/82d3d280-508f-4be5-9570-29e06901b3f9/settings.json` | `200` | REST endpoint |
| `GET` | `/assets/NeueHelvetica45Light_normal_normal-BN2GpD-1.json` | `200` | REST endpoint |
| `GET` | `/assets/ProximaNova-Regular-CRpnmU__.json` | `200` | REST endpoint |
| `GET` | `/assets/AcuminProWide-Black-CvkDKoQR.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consentconfig/82d3d280-508f-4be5-9570-29e06901b3f9/settings.json
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
    }
  }
}
```
### `GET` /assets/NeueHelvetica45Light_normal_normal-BN2GpD-1.json
```json
{
  "type": "object",
  "properties": {
    "atlas": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "distanceRange": {
          "type": "number"
        },
        "distanceRangeMiddle": {
          "type": "number"
        },
        "size": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "height": {
          "type": "number"
        },
        "yOrigin": {
          "type": "string"
        }
      }
    },
    "metrics": {
      "type": "object",
      "properties": {
        "emSize": {
          "type": "number"
        },
        "lineHeight": {
          "type": "number"
        },
        "ascender": {
          "type": "number"
        },
        "descender": {
          "type": "number"
        },
        "underlineY": {
          "type": "number"
        },
        "underlineThickness": {
          "type": "number"
        }
      }
    },
    "glyphs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "unicode": {
            "type": "any"
          },
          "advance": {
            "type": "any"
          }
        }
      }
    },
    "kerning": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /assets/ProximaNova-Regular-CRpnmU__.json
```json
{
  "type": "object",
  "properties": {
    "atlas": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "distanceRange": {
          "type": "number"
        },
        "distanceRangeMiddle": {
          "type": "number"
        },
        "size": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "height": {
          "type": "number"
        },
        "yOrigin": {
          "type": "string"
        }
      }
    },
    "metrics": {
      "type": "object",
      "properties": {
        "emSize": {
          "type": "number"
        },
        "lineHeight": {
          "type": "number"
        },
        "ascender": {
          "type": "number"
        },
        "descender": {
          "type": "number"
        },
        "underlineY": {
          "type": "number"
        },
        "underlineThickness": {
          "type": "number"
        }
      }
    },
    "glyphs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "unicode": {
            "type": "any"
          },
          "advance": {
            "type": "any"
          }
        }
      }
    },
    "kerning": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /assets/AcuminProWide-Black-CvkDKoQR.json
```json
{
  "type": "object",
  "properties": {
    "atlas": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "distanceRange": {
          "type": "number"
        },
        "distanceRangeMiddle": {
          "type": "number"
        },
        "size": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "height": {
          "type": "number"
        },
        "yOrigin": {
          "type": "string"
        }
      }
    },
    "metrics": {
      "type": "object",
      "properties": {
        "emSize": {
          "type": "number"
        },
        "lineHeight": {
          "type": "number"
        },
        "ascender": {
          "type": "number"
        },
        "descender": {
          "type": "number"
        },
        "underlineY": {
          "type": "number"
        },
        "underlineThickness": {
          "type": "number"
        }
      }
    },
    "glyphs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "unicode": {
            "type": "any"
          },
          "advance": {
            "type": "any"
          }
        }
      }
    },
    "kerning": {
      "type": "array",
      "items": "any"
    }
  }
}
```

