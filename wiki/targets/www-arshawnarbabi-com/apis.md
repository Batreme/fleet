---
title: "APIs & Protocols: www-arshawnarbabi-com"
date: 2026-11-14
target: "www-arshawnarbabi-com"
---

# Discovered APIs & Protocols: www-arshawnarbabi-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/mark-3d/implementation-1.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /mark-3d/implementation-1.json
```json
{
  "type": "object",
  "properties": {
    "geo": {
      "type": "object",
      "properties": {
        "depth": {
          "type": "number"
        },
        "bevelSize": {
          "type": "number"
        },
        "bevelThickness": {
          "type": "number"
        },
        "bevelSegments": {
          "type": "number"
        },
        "curveSegments": {
          "type": "number"
        },
        "insetWidth": {
          "type": "number"
        },
        "insetRise": {
          "type": "number"
        },
        "insetSegments": {
          "type": "number"
        }
      }
    },
    "mat": {
      "type": "object",
      "properties": {
        "kind": {
          "type": "string"
        },
        "color": {
          "type": "string"
        },
        "metalness": {
          "type": "number"
        },
        "roughness": {
          "type": "number"
        },
        "clearcoat": {
          "type": "number"
        },
        "clearcoatRoughness": {
          "type": "number"
        },
        "reflectivity": {
          "type": "number"
        },
        "iridescence": {
          "type": "number"
        },
        "iridescenceIOR": {
          "type": "number"
        },
        "transmission": {
          "type": "number"
        },
        "thickness": {
          "type": "number"
        },
        "ior": {
          "type": "number"
        },
        "dispersion": {
          "type": "number"
        },
        "attenuationColor": {
          "type": "string"
        },
        "attenuationDistance": {
          "type": "number"
        },
        "envMapIntensity": {
          "type": "number"
        },
        "gradient": {
          "type": "boolean"
        },
        "gradientTo": {
          "type": "string"
        },
        "texUrl": {
          "type": "null"
        },
        "texName": {
          "type": "null"
        }
      }
    },
    "studio": {
      "type": "object",
      "properties": {
        "preset": {
          "type": "string"
        },
        "mode": {
          "type": "string"
        },
        "intensity": {
          "type": "number"
        },
        "rotation": {
          "type": "number"
        },
        "keyIntensity": {
          "type": "number"
        },
        "fillIntensity": {
          "type": "number"
        },
        "rimIntensity": {
          "type": "number"
        },
        "background": {
          "type": "string"
        },
        "roomTop": {
          "type": "string"
        },
        "ambient": {
          "type": "string"
        },
        "sweepIntensity": {
          "type": "number"
        },
        "showFloor": {
          "type": "boolean"
        },
        "shadowOpacity": {
          "type": "number"
        },
        "shadowBlur": {
          "type": "number"
        },
        "source": {
          "type": "string"
        },
        "imageUrl": {
          "type": "null"
        },
        "imageName": {
          "type": "null"
        },
        "imageIntensity": {
          "type": "number"
        },
        "showImageBackground": {
          "type": "boolean"
        }
      }
    },
    "scene": {
      "type": "object",
      "properties": {
        "autoRotate": {
          "type": "boolean"
        },
        "autoRotateSpeed": {
          "type": "number"
        },
        "tiltX": {
          "type": "number"
        },
        "tiltY": {
          "type": "number"
        },
        "fov": {
          "type": "number"
        }
      }
    },
    "surface": {
      "type": "object",
      "properties": {
        "kind": {
          "type": "string"
        },
        "scale": {
          "type": "number"
        },
        "strength": {
          "type": "number"
        },
        "roughMix": {
          "type": "number"
        },
        "angle": {
          "type": "number"
        },
        "flake": {
          "type": "number"
        },
        "flakeScale": {
          "type": "number"
        },
        "flakeSharp": {
          "type": "number"
        }
      }
    },
    "stickers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "spin": {
            "type": "any"
          },
          "conform": {
            "type": "any"
          },
          "lift": {
            "type": "any"
          },
          "bend": {
            "type": "any"
          },
          "peelTop": {
            "type": "any"
          },
          "peelRight": {
            "type": "any"
          },
          "peelBottom": {
            "type": "any"
          },
          "peelLeft": {
            "type": "any"
          },
          "sway": {
            "type": "any"
          },
          "wrap": {
            "type": "any"
          },
          "scale": {
            "type": "any"
          },
          "opacity": {
            "type": "any"
          },
          "roughness": {
            "type": "any"
          },
          "metalness": {
            "type": "any"
          },
          "clearcoat": {
            "type": "any"
          },
          "tint": {
            "type": "any"
          },
          "tintColor": {
            "type": "any"
          },
          "thickness": {
            "type": "any"
          },
          "cutWidth": {
            "type": "any"
          },
          "keylineWidth": {
            "type": "any"
          }
        }
      }
    },
    "library": {
      "type": "object",
      "properties": {
        "disabled": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "gen": {
      "type": "object",
      "properties": {
        "seed": {
          "type": "string"
        },
        "frontMin": {
          "type": "number"
        },
        "frontMax": {
          "type": "number"
        },
        "backMin": {
          "type": "number"
        },
        "backMax": {
          "type": "number"
        },
        "insideMin": {
          "type": "number"
        },
        "insideMax": {
          "type": "number"
        },
        "grouping": {
          "type": "number"
        },
        "spread": {
          "type": "number"
        },
        "layering": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "scaleVar": {
          "type": "number"
        },
        "spin": {
          "type": "number"
        },
        "wrapBias": {
          "type": "number"
        },
        "bendMin": {
          "type": "number"
        },
        "bendMax": {
          "type": "number"
        },
        "peelChance": {
          "type": "number"
        },
        "peelMin": {
          "type": "number"
        },
        "peelMax": {
          "type": "number"
        },
        "holoChance": {
          "type": "number"
        }
      }
    },
    "genHistory": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "seed": {
            "type": "any"
          },
          "at": {
            "type": "any"
          },
          "count": {
            "type": "any"
          },
          "cfg": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

