---
title: "APIs & Protocols: www-plugandplaydesign-co-uk"
date: 2026-11-14
target: "www-plugandplaydesign-co-uk"
---

# Discovered APIs & Protocols: www-plugandplaydesign-co-uk

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/page-nav-chrome` | `200` | REST endpoint |
| `POST` | `/api/v1/log` | `200` | REST endpoint |
| `GET` | `/client_data/7f5c47f0526d043f59a840727839602c/7_Q97w8X.json` | `200` | REST endpoint |
| `GET` | `/client_data/7f5c47f0526d043f59a840727839602c/config/BvTtAX88.json` | `200` | REST endpoint |
| `GET` | `/client_data/7f5c47f0526d043f59a840727839602c/translations/4GHuxWJ1.json` | `200` | REST endpoint |
| `GET` | `/client_data/7f5c47f0526d043f59a840727839602c/audit-table/O8bG4wZv.json` | `200` | REST endpoint |
| `GET` | `/v1/chunk/ytKn7GHD000001bWpgSNpybb00GlS52OSOcSVJlZ8HNKMVVqQBzTS9HMavRK600UXTZdanfyTGxFZ7gxVfjuccKv4eg/18446744073709551615.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/ytKn7GHD000001bWpgSNpybb00GlS52OSOcSVJlZ8HNKMVVqQBzTS9HMavRK600UXTZdanfyTGxFZ7gxVfjuccKv4eg/0.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/ytKn7GHD000001bWpgSNpybb00GlS52OSOcSVJlZ8HNKMVVqQBzTS9HMavRK600UXTZdanfyTGxFZ7gxVfjuccKv4eg/1.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/ytKn7GHD000001bWpgSNpybb00GlS52OSOcSVJlZ8HNKMVVqQBzTS9HMavRK600UXTZdanfyTGxFZ7gxVfjuccKv4eg/2.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/ytKn7GHD000001bWpgSNpybb00GlS52OSOcSVJlZ8HNKMVVqQBzTS9HMavRK600UXTZdanfyTGxFZ7gxVfjuccKv4eg/3.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/ytKn7GHD000001bWpgSNpybb00GlS52OSOcSVJlZ8HNKMVVqQBzTS9HMavRK600UXTZdanfyTGxFZ7gxVfjuccKv4eg/4.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/rAd2S7ma6ZUDQLWsJAy5lcbPrbJiB4iX00Yvd02GLM3blaLsRyb8ax333SWt96Sg3ANVnjgsddll1mouakWnr6bg/5.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/cSygkcblpbSuuFckgl3ocbgNttjTU4NcQaUjhXnunOW78Kl4XTJTgJ2YDdETJ4aqX3WCTmbl5S1lp2dQdJ27cg/6.m4s` | `200` | REST endpoint |
| `GET` | `/v1/chunk/1nGgbW3blZ00BJ02rWB0250000DazYJ6phnlXriuQyLWo3dqylAGt4c1lAS6YhYEJZxhZKh00s2u7YjJtK4C8YItb7Hg/7.m4s` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/page-nav-chrome
```json
{
  "type": "object",
  "properties": {
    "initialOverDark": {
      "type": "boolean"
    }
  }
}
```
### `GET` /client_data/7f5c47f0526d043f59a840727839602c/7_Q97w8X.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "targetBanner": {
        "type": "number"
      },
      "condition": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /client_data/7f5c47f0526d043f59a840727839602c/config/BvTtAX88.json
```json
{
  "type": "object",
  "properties": {
    "reloadOnAccept": {
      "type": "boolean"
    },
    "dataShortCodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "any"
          },
          "content": {
            "type": "any"
          },
          "uiTag": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "customTag": {
            "type": "any"
          },
          "attributes": {
            "type": "any"
          },
          "processedHTML": {
            "type": "any"
          }
        }
      }
    },
    "iabDataShortCodes": {
      "type": "array",
      "items": "any"
    },
    "activeLaw": {
      "type": "string"
    },
    "showAuditTable": {
      "type": "boolean"
    },
    "showToggler": {
      "type": "boolean"
    },
    "googleACMEnabled": {
      "type": "boolean"
    },
    "readMore": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "color": {
              "type": "any"
            },
            "border-color": {
              "type": "any"
            },
            "background-color": {
              "type": "any"
            }
          }
        },
        "type": {
          "type": "string"
        }
      }
    },
    "togglerSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "togglerIABSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "ccpaSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "placeHolder": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "border-color": {
              "type": "any"
            },
            "background-color": {
              "type": "any"
            },
            "color": {
              "type": "any"
            }
          }
        }
      }
    },
    "togglerIABTab": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "html": {
      "type": "string"
    },
    "css": {
      "type": "string"
    },
    "defaultLanguage": {
      "type": "string"
    },
    "bannerType": {
      "type": "string"
    },
    "respectGPC": {
      "type": "boolean"
    },
    "iabEnabled": {
      "type": "boolean"
    },
    "scriptExpiry": {
      "type": "number"
    }
  }
}
```
### `GET` /client_data/7f5c47f0526d043f59a840727839602c/translations/4GHuxWJ1.json
```json
{
  "type": "object",
  "properties": {
    "cky_notice_title": {
      "type": "string"
    },
    "cky_notice_description": {
      "type": "string"
    },
    "cky_notice_close_label": {
      "type": "string"
    },
    "cky_readmore_text": {
      "type": "string"
    },
    "cky_readmore_privacyLink": {
      "type": "string"
    },
    "cky_revisit_title": {
      "type": "string"
    },
    "cky_video_placeholder_title": {
      "type": "string"
    },
    "cky_accept_text": {
      "type": "string"
    },
    "cky_reject_text": {
      "type": "string"
    },
    "cky_settings_text": {
      "type": "string"
    },
    "cky_preference_title": {
      "type": "string"
    },
    "cky_preference_description": {
      "type": "string"
    },
    "cky_preference_always_enabled": {
      "type": "string"
    },
    "cky_preference_save_text": {
      "type": "string"
    },
    "cky_preference_accept_text": {
      "type": "string"
    },
    "cky_preference_reject_text": {
      "type": "string"
    },
    "cky_preview_save_text": {
      "type": "string"
    },
    "cky_enable_category_label": {
      "type": "string"
    },
    "cky_disable_category_label": {
      "type": "string"
    },
    "cky_preference_close_label": {
      "type": "string"
    }
  }
}
```
### `GET` /client_data/7f5c47f0526d043f59a840727839602c/audit-table/O8bG4wZv.json
```json
{
  "type": "object",
  "properties": {
    "cookies": {
      "type": "object",
      "properties": {
        "_vwo*": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "__cf_bm": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "rc::a": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "rc::c": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "_lfa": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "VISITOR_PRIVACY_METADATA": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "cookieyes-*": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "VISITOR_INFO1_LIVE": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "ytidb::LAST_RESULT_ENTRY_KEY": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "vuid": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "YSC": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "_ga": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "_ga_*": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "__Secure-YNID": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "__Secure-ROLLOUT_TOKEN": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "__Secure-YEC": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "_gcl_au": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "_lfa_test_cookie_stored": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "x-cb-sid": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        }
      }
    },
    "cky_audit_table_empty_text": {
      "type": "string"
    },
    "cky_audit_table_header_id": {
      "type": "string"
    },
    "cky_audit_table_header_duration": {
      "type": "string"
    },
    "cky_audit_table_header_description": {
      "type": "string"
    },
    "cky_preference_necessary_title": {
      "type": "string"
    },
    "cky_preference_necessary_description": {
      "type": "string"
    },
    "cky_preference_functional_title": {
      "type": "string"
    },
    "cky_preference_functional_description": {
      "type": "string"
    },
    "cky_preference_analytics_title": {
      "type": "string"
    },
    "cky_preference_analytics_description": {
      "type": "string"
    },
    "cky_preference_performance_title": {
      "type": "string"
    },
    "cky_preference_performance_description": {
      "type": "string"
    },
    "cky_preference_advertisement_title": {
      "type": "string"
    },
    "cky_preference_advertisement_description": {
      "type": "string"
    },
    "cky_preference_other_title": {
      "type": "string"
    },
    "cky_preference_other_description": {
      "type": "string"
    }
  }
}
```

