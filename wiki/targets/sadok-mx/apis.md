---
title: "APIs & Protocols: sadok-mx"
date: 2026-11-14
target: "[[overview|sadok-mx]]"
---

# Discovered APIs & Protocols: sadok-mx

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/atlas/pressstart-8.json` | `200` | REST endpoint |
| `GET` | `/atlas/emerald-16.json` | `200` | REST endpoint |
| `GET` | `/atlas/tiny-5.json` | `200` | REST endpoint |
| `GET` | `/atlas/capcom-6.json` | `200` | REST endpoint |
| `GET` | `/audio/ui.json` | `200` | REST endpoint |
| `POST` | `/api/visit` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /atlas/pressstart-8.json
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "size": {
      "type": "number"
    },
    "axes": {
      "type": "object",
      "properties": {}
    },
    "image": {
      "type": "string"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "ascent": {
      "type": "number"
    },
    "descent": {
      "type": "number"
    },
    "lineHeight": {
      "type": "number"
    },
    "capHeight": {
      "type": "number"
    },
    "xHeight": {
      "type": "number"
    },
    "threshold": {
      "type": "number"
    },
    "glyphFormat": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "faces": {
      "type": "object",
      "properties": {
        "400": {
          "type": "object",
          "properties": {
            "glyphs": {
              "type": "any"
            },
            "kerning": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /atlas/emerald-16.json
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "size": {
      "type": "number"
    },
    "axes": {
      "type": "object",
      "properties": {}
    },
    "image": {
      "type": "string"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "ascent": {
      "type": "number"
    },
    "descent": {
      "type": "number"
    },
    "lineHeight": {
      "type": "number"
    },
    "capHeight": {
      "type": "number"
    },
    "xHeight": {
      "type": "number"
    },
    "threshold": {
      "type": "number"
    },
    "glyphFormat": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "faces": {
      "type": "object",
      "properties": {
        "400": {
          "type": "object",
          "properties": {
            "glyphs": {
              "type": "any"
            },
            "kerning": {
              "type": "any"
            }
          }
        },
        "700": {
          "type": "object",
          "properties": {
            "glyphs": {
              "type": "any"
            },
            "kerning": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /atlas/tiny-5.json
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "size": {
      "type": "number"
    },
    "axes": {
      "type": "object",
      "properties": {
        "wdth": {
          "type": "number"
        },
        "ROND": {
          "type": "number"
        },
        "BLED": {
          "type": "number"
        },
        "JITT": {
          "type": "number"
        }
      }
    },
    "image": {
      "type": "string"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "ascent": {
      "type": "number"
    },
    "descent": {
      "type": "number"
    },
    "lineHeight": {
      "type": "number"
    },
    "capHeight": {
      "type": "number"
    },
    "xHeight": {
      "type": "number"
    },
    "threshold": {
      "type": "number"
    },
    "glyphFormat": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "faces": {
      "type": "object",
      "properties": {
        "400": {
          "type": "object",
          "properties": {
            "glyphs": {
              "type": "any"
            },
            "kerning": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /atlas/capcom-6.json
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "size": {
      "type": "number"
    },
    "axes": {
      "type": "object",
      "properties": {}
    },
    "image": {
      "type": "string"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "ascent": {
      "type": "number"
    },
    "descent": {
      "type": "number"
    },
    "lineHeight": {
      "type": "number"
    },
    "capHeight": {
      "type": "number"
    },
    "xHeight": {
      "type": "number"
    },
    "threshold": {
      "type": "null"
    },
    "colored": {
      "type": "boolean"
    },
    "bands": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "any"
          },
          "from": {
            "type": "any"
          },
          "color": {
            "type": "any"
          }
        }
      }
    },
    "glyphFormat": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "faces": {
      "type": "object",
      "properties": {
        "400": {
          "type": "object",
          "properties": {
            "glyphs": {
              "type": "any"
            },
            "kerning": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /audio/ui.json
```json
{
  "type": "object",
  "properties": {
    "src": {
      "type": "string"
    },
    "sampleRate": {
      "type": "number"
    },
    "gap": {
      "type": "number"
    },
    "cues": {
      "type": "object",
      "properties": {
        "boot-chime": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "move": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "bump": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "confirm": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "back": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "whoosh": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "power": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "trainer-landed": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "reveal": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        },
        "text-blip": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `POST` /api/visit
```json
{
  "type": "object",
  "properties": {
    "count": {
      "type": "number"
    },
    "counted": {
      "type": "boolean"
    }
  }
}
```

