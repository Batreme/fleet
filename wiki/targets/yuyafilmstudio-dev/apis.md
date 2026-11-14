---
title: "APIs & Protocols: yuyafilmstudio-dev"
date: 2026-11-14
target: "[[overview|yuyafilmstudio-dev]]"
---

# Discovered APIs & Protocols: yuyafilmstudio-dev

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/assets/data/previs-cameras.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /assets/data/previs-cameras.json
```json
{
  "type": "object",
  "properties": {
    "source": {
      "type": "string"
    },
    "cameras": {
      "type": "object",
      "properties": {
        "CAM_Shot01_ProductHeroPush": {
          "type": "object",
          "properties": {
            "lens": {
              "type": "any"
            },
            "sensor": {
              "type": "any"
            },
            "fit": {
              "type": "any"
            },
            "fovY": {
              "type": "any"
            },
            "dof": {
              "type": "any"
            },
            "fstop": {
              "type": "any"
            },
            "frames": {
              "type": "any"
            },
            "fps": {
              "type": "any"
            },
            "res": {
              "type": "any"
            },
            "path": {
              "type": "any"
            }
          }
        },
        "CAM_Shot02": {
          "type": "object",
          "properties": {
            "lens": {
              "type": "any"
            },
            "sensor": {
              "type": "any"
            },
            "fit": {
              "type": "any"
            },
            "fovY": {
              "type": "any"
            },
            "dof": {
              "type": "any"
            },
            "fstop": {
              "type": "any"
            },
            "frames": {
              "type": "any"
            },
            "fps": {
              "type": "any"
            },
            "res": {
              "type": "any"
            },
            "path": {
              "type": "any"
            }
          }
        },
        "CAM_Shot03": {
          "type": "object",
          "properties": {
            "lens": {
              "type": "any"
            },
            "sensor": {
              "type": "any"
            },
            "fit": {
              "type": "any"
            },
            "fovY": {
              "type": "any"
            },
            "dof": {
              "type": "any"
            },
            "fstop": {
              "type": "any"
            },
            "frames": {
              "type": "any"
            },
            "fps": {
              "type": "any"
            },
            "res": {
              "type": "any"
            },
            "path": {
              "type": "any"
            }
          }
        }
      }
    },
    "empties": {
      "type": "object",
      "properties": {
        "TARGET_Product": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "TARGET_Shot03_Upper": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "FOCUS_Shot03_SprayHead": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "SUBJECT_ProductProxy": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "lights": {
      "type": "object",
      "properties": {
        "LIGHT_Key": {
          "type": "object",
          "properties": {
            "pos": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        },
        "LIGHT_Fill": {
          "type": "object",
          "properties": {
            "pos": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

