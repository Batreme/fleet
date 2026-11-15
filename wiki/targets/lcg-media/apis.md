---
title: "APIs & Protocols: lcg-media"
date: 2026-11-14
target: "lcg-media"
---

# Discovered APIs & Protocols: lcg-media

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/settings` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /settings
```json
{
  "type": "object",
  "properties": {
    "should_obtain_cookie_consent": {
      "type": "boolean"
    },
    "features": {
      "type": "object",
      "properties": {
        "tfw_timeline_list": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_follower_count_sunset": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_tweet_edit_backend": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_refsrc_session": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_fosnr_soft_interventions_enabled": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_mixed_media_15897": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_experiments_cookie_expiration": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_show_birdwatch_pivots_enabled": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_duplicate_scribes_to_settings": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_use_profile_image_shape_enabled": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_video_hls_dynamic_manifests_15082": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_legacy_timeline_sunset": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "tfw_tweet_edit_frontend": {
          "type": "object",
          "properties": {
            "bucket": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

