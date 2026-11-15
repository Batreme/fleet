---
title: "APIs & Protocols: www-motorq-com"
date: 2026-11-14
target: "www-motorq-com"
---

# Discovered APIs & Protocols: www-motorq-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/v1/log` | `200` | REST endpoint |
| `GET` | `/client_data/19e007bab17d7408619e8c242e918294/DaXlO6LJ.json` | `200` | REST endpoint |
| `GET` | `/client_data/19e007bab17d7408619e8c242e918294/config/aZxrGaef.json` | `200` | REST endpoint |
| `GET` | `/client_data/19e007bab17d7408619e8c242e918294/translations/GcYCGaC4.json` | `200` | REST endpoint |
| `GET` | `/client_data/19e007bab17d7408619e8c242e918294/audit-table/nfuz3zH9.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /client_data/19e007bab17d7408619e8c242e918294/DaXlO6LJ.json
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
### `GET` /client_data/19e007bab17d7408619e8c242e918294/config/aZxrGaef.json
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
### `GET` /client_data/19e007bab17d7408619e8c242e918294/translations/GcYCGaC4.json
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
### `GET` /client_data/19e007bab17d7408619e8c242e918294/audit-table/nfuz3zH9.json
```json
{
  "type": "object",
  "properties": {
    "cookies": {
      "type": "object",
      "properties": {
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
        "X-CSRF-TOKEN": {
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
        "DOVER_SERVER": {
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
        "_cfuvid": {
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
        "lidc": {
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
        "li_gc": {
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
        "__hstc": {
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
        "hubspotutk": {
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
        "__hssrc": {
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
        "__hssc": {
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
        "_leadgenie_session": {
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

