---
title: "APIs & Protocols: awards-racing"
date: 2026-11-14
target: "awards-racing"
---

# Discovered APIs & Protocols: awards-racing

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `GET` | `/api/health` | `200` | REST endpoint |
| `GET` | `/images/optimized/.hashes.202609071504.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /api/health
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "db": {
      "type": "string"
    }
  }
}
```
### `GET` /images/optimized/.hashes.202609071504.json
```json
{
  "type": "object",
  "properties": {
    "c1": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c1_bg": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "bg": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c1_menu": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c2_menu": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c1": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c2_bg": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c3_menu": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c2": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c3": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_g5": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_c3_bg": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_g7": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_h1": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_g6": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_h13": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_h13_g5_m1_bg1": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_h13_g6_m1_bg1": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_h13_g5_m4_bg1": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    },
    "c1_h13_g5_m3_bg1": {
      "type": "object",
      "properties": {
        "hash": {
          "type": "string"
        },
        "version": {
          "type": "string"
        }
      }
    }
  }
}
```

