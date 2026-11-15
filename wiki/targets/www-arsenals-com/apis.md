---
title: "APIs & Protocols: www-arsenals-com"
date: 2026-11-14
target: "www-arsenals-com"
---

# Discovered APIs & Protocols: www-arsenals-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/media/2026-10-12-PNG_SEQUENCE_48fps_v3/manifest.json` | `200` | REST endpoint |
| `GET` | `/assets/footer-mark-spin-CcBxP2uw.json` | `200` | REST endpoint |
| `GET` | `/media/2026-10-12-PNG_SEQUENCE_48fps_v3/fx/fx.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /media/2026-10-12-PNG_SEQUENCE_48fps_v3/manifest.json
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "number"
    },
    "drop": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    },
    "steps": {
      "type": "number"
    },
    "fps": {
      "type": "number"
    },
    "beats": {
      "type": "object",
      "properties": {
        "descent": {
          "type": "number"
        },
        "water": {
          "type": "number"
        },
        "open-water": {
          "type": "number"
        },
        "fleet": {
          "type": "number"
        }
      }
    },
    "frame": {
      "type": "object",
      "properties": {
        "width": {
          "type": "number"
        },
        "height": {
          "type": "number"
        }
      }
    },
    "levels": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "tiers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "width": {
            "type": "any"
          },
          "height": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          },
          "totalBytes": {
            "type": "any"
          },
          "loop": {
            "type": "any"
          },
          "light": {
            "type": "any"
          }
        }
      }
    },
    "anchors": {
      "type": "object",
      "properties": {
        "hero-logo": {
          "type": "object",
          "properties": {
            "rect": {
              "type": "any"
            },
            "origin": {
              "type": "any"
            },
            "from": {
              "type": "any"
            },
            "transforms": {
              "type": "any"
            },
            "exitStep": {
              "type": "any"
            },
            "trackedUntil": {
              "type": "any"
            },
            "vertical": {
              "type": "any"
            }
          }
        },
        "manifesto": {
          "type": "object",
          "properties": {
            "rect": {
              "type": "any"
            },
            "origin": {
              "type": "any"
            },
            "from": {
              "type": "any"
            },
            "transforms": {
              "type": "any"
            },
            "exitStep": {
              "type": "any"
            },
            "trackedUntil": {
              "type": "any"
            }
          }
        },
        "title": {
          "type": "object",
          "properties": {
            "rect": {
              "type": "any"
            },
            "origin": {
              "type": "any"
            },
            "from": {
              "type": "any"
            },
            "transforms": {
              "type": "any"
            },
            "exitStep": {
              "type": "any"
            },
            "trackedUntil": {
              "type": "any"
            }
          }
        },
        "harpoon": {
          "type": "object",
          "properties": {
            "rect": {
              "type": "any"
            },
            "origin": {
              "type": "any"
            },
            "from": {
              "type": "any"
            },
            "transforms": {
              "type": "any"
            },
            "exitStep": {
              "type": "any"
            },
            "trackedUntil": {
              "type": "any"
            }
          }
        }
      }
    },
    "audit": {
      "type": "object",
      "properties": {
        "ok": {
          "type": "boolean"
        },
        "allowed": {
          "type": "array",
          "items": "any"
        }
      }
    }
  }
}
```
### `GET` /assets/footer-mark-spin-CcBxP2uw.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": "any"
    },
    "meta": {
      "type": "object",
      "properties": {
        "g": {
          "type": "string"
        },
        "axis": {
          "type": "string"
        },
        "spin": {
          "type": "number"
        },
        "pause": {
          "type": "number"
        },
        "depth": {
          "type": "number"
        },
        "weight": {
          "type": "number"
        },
        "joins": {
          "type": "string"
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "shapes": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /media/2026-10-12-PNG_SEQUENCE_48fps_v3/fx/fx.json
```json
{
  "type": "object",
  "properties": {
    "units": {
      "type": "number"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "path": {
      "type": "object",
      "properties": {
        "from": {
          "type": "number"
        },
        "every": {
          "type": "number"
        },
        "data": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "per": {
          "type": "number"
        }
      }
    },
    "through": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "element": {
            "type": "any"
          },
          "rect": {
            "type": "any"
          },
          "release": {
            "type": "any"
          },
          "pass": {
            "type": "any"
          },
          "depth": {
            "type": "any"
          },
          "hide": {
            "type": "any"
          },
          "near": {
            "type": "any"
          },
          "passes": {
            "type": "any"
          },
          "at": {
            "type": "any"
          },
          "cross": {
            "type": "any"
          },
          "H": {
            "type": "any"
          },
          "per": {
            "type": "any"
          },
          "matte": {
            "type": "any"
          }
        }
      }
    },
    "tip": {
      "type": "object",
      "properties": {
        "from": {
          "type": "number"
        },
        "to": {
          "type": "number"
        },
        "matte": {
          "type": "object",
          "properties": {
            "file": {
              "type": "any"
            },
            "steps": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

