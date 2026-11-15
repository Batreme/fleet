---
title: "APIs & Protocols: aikissfiy-com"
date: 2026-11-14
target: "aikissfiy-com"
---

# Discovered APIs & Protocols: aikissfiy-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/releases/aikissfiy/versions/2026/11/13/57fc75c8/sources/builds/meta/36e46465-322d-4158-94de-fbaa428a8035.json` | `200` | REST endpoint |
| `GET` | `/_i18n/Hm7CEWWX/en/messages.json` | `200` | REST endpoint |
| `GET` | `/settings/website/e3872e16-cd9a-4922-8868-4c1b0055262f/prelude/` | `200` | REST endpoint |
| `GET` | `/settings/website/e3872e16-cd9a-4922-8868-4c1b0055262f/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /releases/aikissfiy/versions/2026/11/13/57fc75c8/sources/builds/meta/36e46465-322d-4158-94de-fbaa428a8035.json
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "timestamp": {
      "type": "number"
    },
    "matcher": {
      "type": "object",
      "properties": {
        "static": {
          "type": "object",
          "properties": {
            "/sitemap.xml": {
              "type": "any"
            }
          }
        },
        "wildcard": {
          "type": "object",
          "properties": {}
        },
        "dynamic": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "prerendered": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /_i18n/Hm7CEWWX/en/messages.json
```json
{
  "type": "object",
  "properties": {
    "en": {
      "type": "object",
      "properties": {
        "interface": {
          "type": "object",
          "properties": {
            "loading_dialog": {
              "type": "any"
            },
            "home": {
              "type": "any"
            },
            "home_link": {
              "type": "any"
            },
            "close_navigation": {
              "type": "any"
            },
            "primary_navigation": {
              "type": "any"
            },
            "secondary_navigation": {
              "type": "any"
            },
            "close_submenu": {
              "type": "any"
            },
            "toggle_navigation": {
              "type": "any"
            },
            "collapse_menu": {
              "type": "any"
            },
            "previous_gallery": {
              "type": "any"
            },
            "next_gallery": {
              "type": "any"
            },
            "play_video": {
              "type": "any"
            },
            "upload_example": {
              "type": "any"
            },
            "face_photo": {
              "type": "any"
            },
            "face_example": {
              "type": "any"
            },
            "badge_new": {
              "type": "any"
            },
            "badge_hot": {
              "type": "any"
            },
            "badge_new_upper": {
              "type": "any"
            },
            "badge_new_lower": {
              "type": "any"
            },
            "badge_hot_lower": {
              "type": "any"
            }
          }
        },
        "related_tools": {
          "type": "object",
          "properties": {
            "previous": {
              "type": "any"
            },
            "next": {
              "type": "any"
            }
          }
        },
        "faqs_title": {
          "type": "string"
        },
        "start_for_free": {
          "type": "string"
        },
        "start_creating_now": {
          "type": "string"
        },
        "generate": {
          "type": "string"
        },
        "download": {
          "type": "string"
        },
        "retry": {
          "type": "string"
        },
        "back": {
          "type": "string"
        },
        "all_article": {
          "type": "string"
        },
        "last_updated": {
          "type": "string"
        },
        "explore_more": {
          "type": "string"
        },
        "confirm": {
          "type": "string"
        },
        "cancel": {
          "type": "string"
        },
        "delete_success": {
          "type": "string"
        },
        "pricing": {
          "type": "string"
        },
        "ai_baby": {
          "type": "object",
          "properties": {
            "father_photo": {
              "type": "any"
            },
            "mother_photo": {
              "type": "any"
            },
            "parent_likeness": {
              "type": "any"
            },
            "baby_gender": {
              "type": "any"
            },
            "boy": {
              "type": "any"
            },
            "girl": {
              "type": "any"
            },
            "baby_age": {
              "type": "any"
            },
            "baby": {
              "type": "any"
            },
            "child": {
              "type": "any"
            },
            "teenager": {
              "type": "any"
            }
          }
        },
        "anniversary_video": {
          "type": "object",
          "properties": {
            "shot": {
              "type": "any"
            },
            "caption": {
              "type": "any"
            },
            "sample_shot_tip": {
              "type": "any"
            },
            "sample_shots_remaining": {
              "type": "any"
            },
            "sample_shot": {
              "type": "any"
            },
            "replace_photo": {
              "type": "any"
            },
            "add_shot": {
              "type": "any"
            },
            "delete_shot": {
              "type": "any"
            },
            "anniversary_list": {
              "type": "any"
            }
          }
        },
        "hug": {
          "type": "object",
          "properties": {
            "back_hug": {
              "type": "any"
            },
            "front_hug": {
              "type": "any"
            },
            "koala_hug": {
              "type": "any"
            },
            "running_hug": {
              "type": "any"
            },
            "side_hug": {
              "type": "any"
            },
            "bear_hug": {
              "type": "any"
            },
            "shoulder_carry": {
              "type": "any"
            },
            "waist_hug": {
              "type": "any"
            },
            "princess_carry": {
              "type": "any"
            },
            "spin_hug": {
              "type": "any"
            }
          }
        },
        "menu_label": {
          "type": "object",
          "properties": {
            "ai_shadow_remover": {
              "type": "any"
            },
            "ai_reflection_remover": {
              "type": "any"
            },
            "ai_image_denoiser": {
              "type": "any"
            },
            "ai_mosaic_remover": {
              "type": "any"
            },
            "creative_tools": {
              "type": "any"
            },
            "see_all_tools": {
              "type": "any"
            },
            "ai_outfit_generator": {
              "type": "any"
            },
            "all_tools": {
              "type": "any"
            },
            "photo_editing": {
              "type": "any"
            },
            "home": {
              "type": "any"
            },
            "products": {
              "type": "any"
            },
            "pricing": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "ai_tools": {
              "type": "any"
            },
            "ai_kissing_generator": {
              "type": "any"
            },
            "ai_kiss_photo_generator": {
              "type": "any"
            },
            "ai_family_photo_generator": {
              "type": "any"
            },
            "kiss_effects": {
              "type": "any"
            },
            "ai_character_generator": {
              "type": "any"
            },
            "anime_kissing": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /settings/website/e3872e16-cd9a-4922-8868-4c1b0055262f/prelude/
```json
{
  "type": "object",
  "properties": {
    "socket": {
      "type": "boolean"
    },
    "token": {
      "type": "string"
    },
    "buster": {
      "type": "number"
    },
    "endpoints": {
      "type": "object",
      "properties": {
        "socket": {
          "type": "object",
          "properties": {
            "client": {
              "type": "any"
            },
            "stream": {
              "type": "any"
            }
          }
        },
        "rescue": {
          "type": "object",
          "properties": {
            "socket": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /settings/website/e3872e16-cd9a-4922-8868-4c1b0055262f/
```json
{
  "type": "object",
  "properties": {
    "website": {
      "type": "string"
    },
    "domain": {
      "type": "string"
    },
    "mailer": {
      "type": "string"
    },
    "settings": {
      "type": "object",
      "properties": {
        "logo": {
          "type": "string"
        },
        "audit_log": {
          "type": "boolean"
        },
        "rating": {
          "type": "boolean"
        },
        "transcript": {
          "type": "boolean"
        },
        "enrich": {
          "type": "boolean"
        },
        "junk_filter": {
          "type": "boolean"
        },
        "tile": {
          "type": "string"
        },
        "conversations": {
          "type": "boolean"
        },
        "wait_game": {
          "type": "boolean"
        },
        "website_logo": {
          "type": "boolean"
        },
        "last_operator_face": {
          "type": "boolean"
        },
        "ongoing_operator_face": {
          "type": "boolean"
        },
        "activity_metrics": {
          "type": "boolean"
        },
        "operator_privacy": {
          "type": "boolean"
        },
        "visitor_privacy": {
          "type": "boolean"
        },
        "availability_tooltip": {
          "type": "boolean"
        },
        "hide_vacation": {
          "type": "boolean"
        },
        "hide_on_away": {
          "type": "boolean"
        },
        "hide_on_mobile": {
          "type": "boolean"
        },
        "position_reverse": {
          "type": "boolean"
        }
      }
    },
    "operators": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "user_id": {
            "type": "any"
          },
          "avatar": {
            "type": "any"
          },
          "nickname": {
            "type": "any"
          },
          "timestamp": {
            "type": "any"
          }
        }
      }
    },
    "plugins": {
      "type": "object",
      "properties": {}
    },
    "online": {
      "type": "boolean"
    },
    "trial": {
      "type": "boolean"
    },
    "overlay": {
      "type": "null"
    },
    "channels": {
      "type": "object",
      "properties": {}
    }
  }
}
```

