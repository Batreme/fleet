---
title: "APIs & Protocols: no-merci-michel-com"
date: 2026-11-14
target: "no-merci-michel-com"
---

# Discovered APIs & Protocols: no-merci-michel-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/send` | `200` | REST endpoint |
| `POST` | `/v1/accounts:signUp` | `200` | REST endpoint |
| `POST` | `/v1/accounts:lookup` | `200` | REST endpoint |
| `GET` | `/production-api/listIceServers` | `200` | REST endpoint |
| `GET` | `/production-api/leaderboard/getLeaderboard` | `200` | REST endpoint |
| `GET` | `/assets/sprites.579ced6f37592b2b.json` | `200` | REST endpoint |
| `GET` | `/assets/sparks.7f5cb19c37592b2b.json` | `200` | REST endpoint |
| `GET` | `/assets/stars.ce333a9037592b2b.json` | `200` | REST endpoint |
| `GET` | `/assets/trail_1.a27bd9c337592b2b.json` | `200` | REST endpoint |
| `GET` | `/assets/trail_2.2490a38f37592b2b.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/send
```json
{
  "type": "object",
  "properties": {
    "cache": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "visitId": {
      "type": "string"
    }
  }
}
```
### `POST` /v1/accounts:signUp
```json
{
  "type": "object",
  "properties": {
    "kind": {
      "type": "string"
    },
    "idToken": {
      "type": "string"
    },
    "refreshToken": {
      "type": "string"
    },
    "expiresIn": {
      "type": "string"
    },
    "localId": {
      "type": "string"
    }
  }
}
```
### `POST` /v1/accounts:lookup
```json
{
  "type": "object",
  "properties": {
    "kind": {
      "type": "string"
    },
    "users": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "localId": {
            "type": "any"
          },
          "lastLoginAt": {
            "type": "any"
          },
          "createdAt": {
            "type": "any"
          },
          "lastRefreshAt": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /production-api/listIceServers
```json
{
  "type": "object",
  "properties": {
    "iceServers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {
            "type": "any"
          },
          "urls": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /production-api/leaderboard/getLeaderboard
```json
{
  "type": "object",
  "properties": {
    "leaderboard": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "accessToken": {
            "type": "any"
          },
          "arm": {
            "type": "any"
          },
          "leaderboardID": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "rank": {
            "type": "any"
          },
          "streak": {
            "type": "any"
          },
          "updatedAt": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /assets/sprites.579ced6f37592b2b.json
```json
{
  "type": "object",
  "properties": {
    "frames": {
      "type": "object",
      "properties": {
        "fire_00047": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00048": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00049": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00050": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00051": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00052": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00053": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00054": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00055": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00056": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00057": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00058": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00059": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00060": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00061": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00062": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00063": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00064": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00065": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "fire_00066": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        }
      }
    },
    "animations": {
      "type": "object",
      "properties": {
        "fire": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "app": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "image": {
          "type": "string"
        },
        "format": {
          "type": "string"
        },
        "size": {
          "type": "object",
          "properties": {
            "w": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "scale": {
          "type": "string"
        },
        "smartupdate": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /assets/sparks.7f5cb19c37592b2b.json
```json
{
  "type": "object",
  "properties": {
    "frames": {
      "type": "object",
      "properties": {
        "sparks_000": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_001": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_002": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_003": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_004": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_005": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_006": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_007": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_008": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_009": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_010": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_011": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_012": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_013": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_014": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_015": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_016": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_017": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_018": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "sparks_019": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        }
      }
    },
    "animations": {
      "type": "object",
      "properties": {
        "sparks": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "app": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "image": {
          "type": "string"
        },
        "format": {
          "type": "string"
        },
        "size": {
          "type": "object",
          "properties": {
            "w": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "scale": {
          "type": "string"
        },
        "smartupdate": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /assets/stars.ce333a9037592b2b.json
```json
{
  "type": "object",
  "properties": {
    "frames": {
      "type": "object",
      "properties": {
        "ANIMATIONGLASSES_FRONT00000000": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATIONGLASSES_FRONT00000001": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATIONGLASSES_FRONT00000002": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATIONGLASSES_FRONT00000003": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATIONGLASSES_FRONT00000004": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATIONGLASSES_FRONT00000005": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATIONGLASSES_FRONT00000006": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATIONGLASSES_FRONT00000007": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        }
      }
    },
    "animations": {
      "type": "object",
      "properties": {
        "stars": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "app": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "image": {
          "type": "string"
        },
        "format": {
          "type": "string"
        },
        "size": {
          "type": "object",
          "properties": {
            "w": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "scale": {
          "type": "string"
        },
        "smartupdate": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /assets/trail_1.a27bd9c337592b2b.json
```json
{
  "type": "object",
  "properties": {
    "frames": {
      "type": "object",
      "properties": {
        "trail_000": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_001": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_002": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_003": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_004": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_005": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_006": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_007": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_008": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_009": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_010": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_011": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_012": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_013": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_014": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_015": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_016": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_017": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_018": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "trail_019": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        }
      }
    },
    "animations": {
      "type": "object",
      "properties": {
        "trail_1": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "app": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "image": {
          "type": "string"
        },
        "format": {
          "type": "string"
        },
        "size": {
          "type": "object",
          "properties": {
            "w": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "scale": {
          "type": "string"
        },
        "smartupdate": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /assets/trail_2.2490a38f37592b2b.json
```json
{
  "type": "object",
  "properties": {
    "frames": {
      "type": "object",
      "properties": {
        "ANIMATION03_FRONT00000000": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000001": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000002": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000003": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000004": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000005": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000006": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000007": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000008": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000009": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000010": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000011": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000012": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000013": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000014": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000015": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000016": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000017": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        },
        "ANIMATION03_FRONT00000018": {
          "type": "object",
          "properties": {
            "frame": {
              "type": "any"
            },
            "rotated": {
              "type": "any"
            },
            "trimmed": {
              "type": "any"
            },
            "spriteSourceSize": {
              "type": "any"
            },
            "sourceSize": {
              "type": "any"
            }
          }
        }
      }
    },
    "animations": {
      "type": "object",
      "properties": {
        "trail_2": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "app": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "image": {
          "type": "string"
        },
        "format": {
          "type": "string"
        },
        "size": {
          "type": "object",
          "properties": {
            "w": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "scale": {
          "type": "string"
        },
        "smartupdate": {
          "type": "string"
        }
      }
    }
  }
}
```

