---
title: "APIs & Protocols: kinoria-studio"
date: 2026-11-14
target: "kinoria-studio"
---

# Discovered APIs & Protocols: kinoria-studio

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/assets/hero/finder/barrel.json` | `200` | REST endpoint |
| `GET` | `/assets/hero/finder/barrel_layers.json` | `200` | REST endpoint |
| `GET` | `/assets/hero/bake/frames.json` | `200` | REST endpoint |
| `GET` | `/sound/v2/hero_settle.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/flash.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/main_shutter.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/lamp_on.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/footer_touch.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/walk_click.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/walk_whir.wav` | `200` | REST endpoint |
| `GET` | `/sound/v2/walk_end.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/mouse_air.wav` | `200` | REST endpoint |
| `GET` | `/sound/v2/reroll_a.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/reroll_b.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/drop_whoosh.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/print_pass.wav` | `200` | REST endpoint |
| `GET` | `/sound/v2/tin_hover_a.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/tin_hover_b.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/tin_hover_c.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/tin_select.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/leader_pull.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/zoom_friction.wav` | `200` | REST endpoint |
| `GET` | `/sound/v2/shutter_a.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/shutter_b.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/advance_a.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/advance_b.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/roll_end.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/paper_slide.wav` | `200` | REST endpoint |
| `GET` | `/sound/v2/paper_float.mp3` | `200` | REST endpoint |
| `GET` | `/sound/v2/paper_touch_a.mp3` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /assets/hero/finder/barrel.json
```json
{
  "type": "object",
  "properties": {
    "source": {
      "type": "string"
    },
    "W": {
      "type": "number"
    },
    "H": {
      "type": "number"
    },
    "aperture": {
      "type": "object",
      "properties": {
        "x0": {
          "type": "number"
        },
        "y0": {
          "type": "number"
        },
        "x1": {
          "type": "number"
        },
        "y1": {
          "type": "number"
        }
      }
    },
    "inset": {
      "type": "number"
    },
    "feather": {
      "type": "number"
    },
    "alphaFloor": {
      "type": "number"
    },
    "apertureAspect": {
      "type": "number"
    },
    "exitScaleToClear": {
      "type": "number"
    }
  }
}
```
### `GET` /assets/hero/finder/barrel_layers.json
```json
{
  "type": "object",
  "properties": {
    "source": {
      "type": "string"
    },
    "W": {
      "type": "number"
    },
    "H": {
      "type": "number"
    },
    "aperture": {
      "type": "object",
      "properties": {
        "x0": {
          "type": "number"
        },
        "y0": {
          "type": "number"
        },
        "x1": {
          "type": "number"
        },
        "y1": {
          "type": "number"
        }
      }
    },
    "rim": {
      "type": "object",
      "properties": {
        "x0": {
          "type": "number"
        },
        "y0": {
          "type": "number"
        },
        "x1": {
          "type": "number"
        },
        "y1": {
          "type": "number"
        }
      }
    },
    "pillar": {
      "type": "object",
      "properties": {
        "lx0": {
          "type": "number"
        },
        "lx1": {
          "type": "number"
        },
        "rx0": {
          "type": "number"
        },
        "rx1": {
          "type": "number"
        }
      }
    },
    "bar": {
      "type": "object",
      "properties": {
        "ty0": {
          "type": "number"
        },
        "ty1": {
          "type": "number"
        },
        "by0": {
          "type": "number"
        },
        "by1": {
          "type": "number"
        }
      }
    },
    "apertureVUV": {
      "type": "object",
      "properties": {
        "x0": {
          "type": "number"
        },
        "y0": {
          "type": "number"
        },
        "x1": {
          "type": "number"
        },
        "y1": {
          "type": "number"
        }
      }
    },
    "z": {
      "type": "object",
      "properties": {
        "rim": {
          "type": "number"
        },
        "pillars": {
          "type": "number"
        },
        "bars": {
          "type": "number"
        },
        "wall": {
          "type": "number"
        }
      }
    },
    "planes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /assets/hero/bake/frames.json
```json
{
  "type": "object",
  "properties": {
    "note": {
      "type": "string"
    },
    "plate_px": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "body_crop_px": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "shadow_px": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "yaw_base_deg": {
      "type": "number"
    },
    "range_deg": {
      "type": "number"
    },
    "step_deg": {
      "type": "number"
    },
    "frames": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "i": {
            "type": "any"
          },
          "yaw": {
            "type": "any"
          },
          "obj": {
            "type": "any"
          },
          "shadow": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

