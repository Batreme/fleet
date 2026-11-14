---
title: "APIs & Protocols: key-co"
date: 2026-11-14
target: "[[overview|key-co]]"
---

# Discovered APIs & Protocols: key-co

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/4508133229133824/envelope/` | `200` | REST endpoint |
| `POST` | `/flags/` | `200` | REST endpoint |
| `GET` | `/v1/lst/universal-script` | `200` | REST endpoint |
| `GET` | `/gsi/status` | `200` | REST endpoint |
| `GET` | `/api/surveys/` | `200` | REST endpoint |
| `GET` | `/pixel-config/v1/L5pGvfTUhXmi8dSYbPEUt4.json` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |
| `GET` | `/v1/lst/gusid` | `301` | REST endpoint |
| `POST` | `/client/sessions/` | `201` | REST endpoint |
| `GET` | `/custom-fonts/api/v1/company-fonts/onsite` | `200` | REST endpoint |
| `GET` | `/forms/api/v7/Rsq5Yt/full-forms` | `200` | REST endpoint |
| `GET` | `/v1/lst/gusid` | `200` | REST endpoint |
| `GET` | `/v1/lst/session` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |
| `GET` | `/v1/lst/pc` | `200` | REST endpoint |
| `POST` | `/api/4508133229133824/envelope/` | `200` | REST endpoint |
| `POST` | `/api/4508133229133824/envelope/` | `200` | REST endpoint |
| `POST` | `/api/4508133229133824/envelope/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/4508133229133824/envelope/
```json
{
  "type": "object",
  "properties": {}
}
```
### `POST` /flags/
```json
{
  "type": "object",
  "properties": {
    "errorsWhileComputingFlags": {
      "type": "boolean"
    },
    "flags": {
      "type": "object",
      "properties": {
        "tagline_title": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "show_map_on_search": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "checkout_page": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "dev_wishlist_ui_enabled": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "dev_homepage_hero_title": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "hdp_cta": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "survey-targeting-71bd713b22-custom": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "survey-targeting-490d733fba-custom": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "dev_show_map_on_search": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "dev_hdp_cta": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "dev_checkout_page": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        }
      }
    },
    "requestId": {
      "type": "string"
    },
    "evaluatedAt": {
      "type": "number"
    }
  }
}
```
### `GET` /api/surveys/
```json
{
  "type": "object",
  "properties": {
    "surveys": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "appearance": {
            "type": "any"
          },
          "conditions": {
            "type": "any"
          },
          "current_iteration": {
            "type": "any"
          },
          "current_iteration_start_date": {
            "type": "any"
          },
          "enable_partial_responses": {
            "type": "any"
          },
          "end_date": {
            "type": "any"
          },
          "id": {
            "type": "any"
          },
          "internal_targeting_flag_key": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "questions": {
            "type": "any"
          },
          "schedule": {
            "type": "any"
          },
          "start_date": {
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
```
### `GET` /pixel-config/v1/L5pGvfTUhXmi8dSYbPEUt4.json
```json
{
  "type": "object",
  "properties": {
    "automatic_advanced_matching_enabled": {
      "type": "boolean"
    }
  }
}
```
### `POST` /client/sessions/
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "id": {
          "type": "string"
        },
        "attributes": {
          "type": "object",
          "properties": {
            "identifiers": {
              "type": "any"
            },
            "kx": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /custom-fonts/api/v1/company-fonts/onsite
```json
{
  "type": "object",
  "properties": {
    "google": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "family": {
            "type": "any"
          },
          "fallback": {
            "type": "any"
          },
          "font_type": {
            "type": "any"
          },
          "variants": {
            "type": "any"
          }
        }
      }
    },
    "typekit": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "family": {
            "type": "any"
          },
          "fallback": {
            "type": "any"
          },
          "font_type": {
            "type": "any"
          },
          "typekit_url": {
            "type": "any"
          },
          "display_name": {
            "type": "any"
          }
        }
      }
    },
    "custom": {
      "type": "array",
      "items": "any"
    }
  }
}
```

