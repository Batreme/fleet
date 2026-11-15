---
title: "APIs & Protocols: www-imersion-io"
date: 2026-11-14
target: "www-imersion-io"
---

# Discovered APIs & Protocols: www-imersion-io

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/wp-json/wp/v2/immersions` | `200` | REST endpoint |
| `GET` | `/api/wp-json/wp/v2/immersions` | `200` | REST endpoint |
| `GET` | `/api/wp-json/wp/v2/immersions` | `200` | REST endpoint |
| `GET` | `/api/wp-json/wp/v2/immersions` | `200` | REST endpoint |
| `GET` | `/api/wp-json/wp/v2/immersions` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/wp-json/wp/v2/immersions
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "date": {
        "type": "string"
      },
      "date_gmt": {
        "type": "string"
      },
      "guid": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "modified": {
        "type": "string"
      },
      "modified_gmt": {
        "type": "string"
      },
      "slug": {
        "type": "string"
      },
      "status": {
        "type": "string"
      },
      "type": {
        "type": "string"
      },
      "link": {
        "type": "string"
      },
      "title": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "content": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          },
          "protected": {
            "type": "any"
          }
        }
      },
      "featured_media": {
        "type": "number"
      },
      "template": {
        "type": "string"
      },
      "class_list": {
        "type": "array",
        "items": {
          "type": "any"
        }
      },
      "acf": {
        "type": "object",
        "properties": {
          "country": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "zip_code": {
            "type": "any"
          },
          "place_link": {
            "type": "any"
          },
          "contributor_name": {
            "type": "any"
          },
          "contributor_bio": {
            "type": "any"
          },
          "contributor_link": {
            "type": "any"
          },
          "contributor_photo": {
            "type": "any"
          },
          "date_added": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "sponsored": {
            "type": "any"
          },
          "price": {
            "type": "any"
          },
          "summary": {
            "type": "any"
          },
          "address": {
            "type": "any"
          },
          "music_mp3": {
            "type": "any"
          },
          "music_name": {
            "type": "any"
          },
          "music_author": {
            "type": "any"
          },
          "photo": {
            "type": "any"
          }
        }
      },
      "yoast_head": {
        "type": "string"
      },
      "yoast_head_json": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "robots": {
            "type": "any"
          },
          "canonical": {
            "type": "any"
          },
          "og_locale": {
            "type": "any"
          },
          "og_type": {
            "type": "any"
          },
          "og_title": {
            "type": "any"
          },
          "og_description": {
            "type": "any"
          },
          "og_url": {
            "type": "any"
          },
          "og_site_name": {
            "type": "any"
          },
          "article_modified_time": {
            "type": "any"
          },
          "twitter_card": {
            "type": "any"
          },
          "schema": {
            "type": "any"
          }
        }
      },
      "_links": {
        "type": "object",
        "properties": {
          "self": {
            "type": "any"
          },
          "collection": {
            "type": "any"
          },
          "about": {
            "type": "any"
          },
          "wp:attachment": {
            "type": "any"
          },
          "curies": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/wp-json/wp/v2/immersions
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "date": {
        "type": "string"
      },
      "date_gmt": {
        "type": "string"
      },
      "guid": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "modified": {
        "type": "string"
      },
      "modified_gmt": {
        "type": "string"
      },
      "slug": {
        "type": "string"
      },
      "status": {
        "type": "string"
      },
      "type": {
        "type": "string"
      },
      "link": {
        "type": "string"
      },
      "title": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "content": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          },
          "protected": {
            "type": "any"
          }
        }
      },
      "featured_media": {
        "type": "number"
      },
      "template": {
        "type": "string"
      },
      "class_list": {
        "type": "array",
        "items": {
          "type": "any"
        }
      },
      "acf": {
        "type": "object",
        "properties": {
          "summary": {
            "type": "any"
          },
          "country": {
            "type": "any"
          },
          "address": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "zip_code": {
            "type": "any"
          },
          "place_link": {
            "type": "any"
          },
          "contributor_name": {
            "type": "any"
          },
          "contributor_bio": {
            "type": "any"
          },
          "contributor_link": {
            "type": "any"
          },
          "contributor_photo": {
            "type": "any"
          },
          "date_added": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "sponsored": {
            "type": "any"
          },
          "price": {
            "type": "any"
          },
          "music_mp3": {
            "type": "any"
          },
          "music_name": {
            "type": "any"
          },
          "music_author": {
            "type": "any"
          },
          "photo": {
            "type": "any"
          }
        }
      },
      "yoast_head": {
        "type": "string"
      },
      "yoast_head_json": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "robots": {
            "type": "any"
          },
          "canonical": {
            "type": "any"
          },
          "og_locale": {
            "type": "any"
          },
          "og_type": {
            "type": "any"
          },
          "og_title": {
            "type": "any"
          },
          "og_description": {
            "type": "any"
          },
          "og_url": {
            "type": "any"
          },
          "og_site_name": {
            "type": "any"
          },
          "article_modified_time": {
            "type": "any"
          },
          "og_image": {
            "type": "any"
          },
          "twitter_card": {
            "type": "any"
          },
          "twitter_misc": {
            "type": "any"
          },
          "schema": {
            "type": "any"
          }
        }
      },
      "_links": {
        "type": "object",
        "properties": {
          "self": {
            "type": "any"
          },
          "collection": {
            "type": "any"
          },
          "about": {
            "type": "any"
          },
          "wp:featuredmedia": {
            "type": "any"
          },
          "wp:attachment": {
            "type": "any"
          },
          "curies": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/wp-json/wp/v2/immersions
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "date": {
        "type": "string"
      },
      "date_gmt": {
        "type": "string"
      },
      "guid": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "modified": {
        "type": "string"
      },
      "modified_gmt": {
        "type": "string"
      },
      "slug": {
        "type": "string"
      },
      "status": {
        "type": "string"
      },
      "type": {
        "type": "string"
      },
      "link": {
        "type": "string"
      },
      "title": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "content": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          },
          "protected": {
            "type": "any"
          }
        }
      },
      "featured_media": {
        "type": "number"
      },
      "template": {
        "type": "string"
      },
      "class_list": {
        "type": "array",
        "items": {
          "type": "any"
        }
      },
      "acf": {
        "type": "object",
        "properties": {
          "summary": {
            "type": "any"
          },
          "country": {
            "type": "any"
          },
          "address": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "zip_code": {
            "type": "any"
          },
          "place_link": {
            "type": "any"
          },
          "contributor_name": {
            "type": "any"
          },
          "contributor_bio": {
            "type": "any"
          },
          "contributor_link": {
            "type": "any"
          },
          "contributor_photo": {
            "type": "any"
          },
          "date_added": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "sponsored": {
            "type": "any"
          },
          "price": {
            "type": "any"
          },
          "music_mp3": {
            "type": "any"
          },
          "music_name": {
            "type": "any"
          },
          "music_author": {
            "type": "any"
          },
          "photo": {
            "type": "any"
          }
        }
      },
      "yoast_head": {
        "type": "string"
      },
      "yoast_head_json": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "robots": {
            "type": "any"
          },
          "canonical": {
            "type": "any"
          },
          "og_locale": {
            "type": "any"
          },
          "og_type": {
            "type": "any"
          },
          "og_title": {
            "type": "any"
          },
          "og_description": {
            "type": "any"
          },
          "og_url": {
            "type": "any"
          },
          "og_site_name": {
            "type": "any"
          },
          "twitter_card": {
            "type": "any"
          },
          "twitter_misc": {
            "type": "any"
          },
          "schema": {
            "type": "any"
          }
        }
      },
      "_links": {
        "type": "object",
        "properties": {
          "self": {
            "type": "any"
          },
          "collection": {
            "type": "any"
          },
          "about": {
            "type": "any"
          },
          "wp:featuredmedia": {
            "type": "any"
          },
          "wp:attachment": {
            "type": "any"
          },
          "curies": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/wp-json/wp/v2/immersions
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "date": {
        "type": "string"
      },
      "date_gmt": {
        "type": "string"
      },
      "guid": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "modified": {
        "type": "string"
      },
      "modified_gmt": {
        "type": "string"
      },
      "slug": {
        "type": "string"
      },
      "status": {
        "type": "string"
      },
      "type": {
        "type": "string"
      },
      "link": {
        "type": "string"
      },
      "title": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "content": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          },
          "protected": {
            "type": "any"
          }
        }
      },
      "featured_media": {
        "type": "number"
      },
      "template": {
        "type": "string"
      },
      "class_list": {
        "type": "array",
        "items": {
          "type": "any"
        }
      },
      "acf": {
        "type": "object",
        "properties": {
          "summary": {
            "type": "any"
          },
          "country": {
            "type": "any"
          },
          "address": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "zip_code": {
            "type": "any"
          },
          "place_link": {
            "type": "any"
          },
          "contributor_name": {
            "type": "any"
          },
          "contributor_bio": {
            "type": "any"
          },
          "contributor_link": {
            "type": "any"
          },
          "contributor_photo": {
            "type": "any"
          },
          "date_added": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "sponsored": {
            "type": "any"
          },
          "price": {
            "type": "any"
          },
          "music_mp3": {
            "type": "any"
          },
          "music_name": {
            "type": "any"
          },
          "music_author": {
            "type": "any"
          },
          "photo": {
            "type": "any"
          }
        }
      },
      "yoast_head": {
        "type": "string"
      },
      "yoast_head_json": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "robots": {
            "type": "any"
          },
          "canonical": {
            "type": "any"
          },
          "og_locale": {
            "type": "any"
          },
          "og_type": {
            "type": "any"
          },
          "og_title": {
            "type": "any"
          },
          "og_description": {
            "type": "any"
          },
          "og_url": {
            "type": "any"
          },
          "og_site_name": {
            "type": "any"
          },
          "article_modified_time": {
            "type": "any"
          },
          "og_image": {
            "type": "any"
          },
          "twitter_card": {
            "type": "any"
          },
          "twitter_misc": {
            "type": "any"
          },
          "schema": {
            "type": "any"
          }
        }
      },
      "_links": {
        "type": "object",
        "properties": {
          "self": {
            "type": "any"
          },
          "collection": {
            "type": "any"
          },
          "about": {
            "type": "any"
          },
          "wp:featuredmedia": {
            "type": "any"
          },
          "wp:attachment": {
            "type": "any"
          },
          "curies": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/wp-json/wp/v2/immersions
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "date": {
        "type": "string"
      },
      "date_gmt": {
        "type": "string"
      },
      "guid": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "modified": {
        "type": "string"
      },
      "modified_gmt": {
        "type": "string"
      },
      "slug": {
        "type": "string"
      },
      "status": {
        "type": "string"
      },
      "type": {
        "type": "string"
      },
      "link": {
        "type": "string"
      },
      "title": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "content": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          },
          "protected": {
            "type": "any"
          }
        }
      },
      "featured_media": {
        "type": "number"
      },
      "template": {
        "type": "string"
      },
      "class_list": {
        "type": "array",
        "items": {
          "type": "any"
        }
      },
      "acf": {
        "type": "object",
        "properties": {
          "summary": {
            "type": "any"
          },
          "country": {
            "type": "any"
          },
          "address": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "zip_code": {
            "type": "any"
          },
          "place_link": {
            "type": "any"
          },
          "contributor_name": {
            "type": "any"
          },
          "contributor_bio": {
            "type": "any"
          },
          "contributor_link": {
            "type": "any"
          },
          "contributor_photo": {
            "type": "any"
          },
          "date_added": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "sponsored": {
            "type": "any"
          },
          "price": {
            "type": "any"
          },
          "music_mp3": {
            "type": "any"
          },
          "music_name": {
            "type": "any"
          },
          "music_author": {
            "type": "any"
          },
          "photo": {
            "type": "any"
          }
        }
      },
      "yoast_head": {
        "type": "string"
      },
      "yoast_head_json": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "robots": {
            "type": "any"
          },
          "canonical": {
            "type": "any"
          },
          "og_locale": {
            "type": "any"
          },
          "og_type": {
            "type": "any"
          },
          "og_title": {
            "type": "any"
          },
          "og_description": {
            "type": "any"
          },
          "og_url": {
            "type": "any"
          },
          "og_site_name": {
            "type": "any"
          },
          "article_modified_time": {
            "type": "any"
          },
          "og_image": {
            "type": "any"
          },
          "twitter_card": {
            "type": "any"
          },
          "twitter_misc": {
            "type": "any"
          },
          "schema": {
            "type": "any"
          }
        }
      },
      "_links": {
        "type": "object",
        "properties": {
          "self": {
            "type": "any"
          },
          "collection": {
            "type": "any"
          },
          "about": {
            "type": "any"
          },
          "wp:featuredmedia": {
            "type": "any"
          },
          "wp:attachment": {
            "type": "any"
          },
          "curies": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

