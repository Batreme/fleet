---
title: "APIs & Protocols: www-amberjs-dev"
date: 2026-11-14
target: "[[overview|www-amberjs-dev]]"
---

# Discovered APIs & Protocols: www-amberjs-dev

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/amber-sizes.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /amber-sizes.json
```json
{
  "type": "object",
  "properties": {
    "packages": {
      "type": "object",
      "properties": {
        "amber-scroll": {
          "type": "string"
        },
        "amber-motion": {
          "type": "string"
        }
      }
    },
    "measurement": {
      "type": "object",
      "properties": {
        "esbuild": {
          "type": "string"
        },
        "minified": {
          "type": "boolean"
        },
        "format": {
          "type": "string"
        },
        "gzipLevel": {
          "type": "number"
        },
        "bytesPerKB": {
          "type": "number"
        },
        "source": {
          "type": "string"
        },
        "scope": {
          "type": "string"
        }
      }
    },
    "optionBits": {
      "type": "object",
      "properties": {
        "scroll": {
          "type": "number"
        },
        "pinning": {
          "type": "number"
        },
        "parallax": {
          "type": "number"
        },
        "infinite": {
          "type": "number"
        },
        "animate": {
          "type": "number"
        },
        "morph": {
          "type": "number"
        }
      }
    },
    "core": {
      "type": "number"
    },
    "coreUpperKB": {
      "type": "number"
    },
    "motion": {
      "type": "number"
    },
    "additions": {
      "type": "object",
      "properties": {
        "control": {
          "type": "number"
        },
        "animate": {
          "type": "number"
        },
        "morph": {
          "type": "number"
        }
      }
    },
    "bundles": {
      "type": "object",
      "properties": {
        "0": {
          "type": "number"
        },
        "1": {
          "type": "number"
        },
        "2": {
          "type": "number"
        },
        "3": {
          "type": "number"
        },
        "4": {
          "type": "number"
        },
        "5": {
          "type": "number"
        },
        "6": {
          "type": "number"
        },
        "7": {
          "type": "number"
        },
        "8": {
          "type": "number"
        },
        "9": {
          "type": "number"
        },
        "10": {
          "type": "number"
        },
        "11": {
          "type": "number"
        },
        "12": {
          "type": "number"
        },
        "13": {
          "type": "number"
        },
        "14": {
          "type": "number"
        },
        "15": {
          "type": "number"
        },
        "16": {
          "type": "number"
        },
        "17": {
          "type": "number"
        },
        "18": {
          "type": "number"
        },
        "19": {
          "type": "number"
        }
      }
    }
  }
}
```

