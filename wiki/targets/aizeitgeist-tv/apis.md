---
title: "APIs & Protocols: aizeitgeist-tv"
date: 2026-11-14
target: "aizeitgeist-tv"
---

# Discovered APIs & Protocols: aizeitgeist-tv

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/subscribe` | `200` | REST endpoint |
| `GET` | `/data/messages.json` | `200` | REST endpoint |
| `GET` | `/data/live.json` | `200` | REST endpoint |
| `GET` | `/api/likes` | `200` | REST endpoint |
| `POST` | `/api/presence` | `200` | REST endpoint |
| `GET` | `/data/menu.json` | `200` | REST endpoint |
| `GET` | `/data/zoom.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/subscribe
```json
{
  "type": "object",
  "properties": {
    "ready": {
      "type": "boolean"
    }
  }
}
```
### `GET` /data/messages.json
```json
{
  "type": "object",
  "properties": {
    "schema": {
      "type": "number"
    },
    "generated": {
      "type": "string"
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "count": {
      "type": "number"
    },
    "messages": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "text": {
            "type": "any"
          },
          "set": {
            "type": "any"
          },
          "date": {
            "type": "any"
          },
          "tags": {
            "type": "any"
          },
          "source": {
            "type": "any"
          },
          "context": {
            "type": "any"
          },
          "fragment": {
            "type": "any"
          },
          "expires": {
            "type": "any"
          },
          "promoted_to_base": {
            "type": "any"
          },
          "added_by": {
            "type": "any"
          },
          "checked": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /data/live.json
```json
{
  "type": "object",
  "properties": {
    "generated": {
      "type": "string"
    },
    "window": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "base": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "text": {
            "type": "any"
          },
          "set": {
            "type": "any"
          },
          "date": {
            "type": "any"
          },
          "tags": {
            "type": "any"
          }
        }
      }
    },
    "news": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "text": {
            "type": "any"
          },
          "set": {
            "type": "any"
          },
          "date": {
            "type": "any"
          },
          "tags": {
            "type": "any"
          },
          "added_at": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/likes
```json
{
  "type": "object",
  "properties": {
    "2026-09-12-dario-is-right": {
      "type": "number"
    },
    "2026-09-12-an-extra-year-or-two-before-models-reach-critical-levels": {
      "type": "number"
    },
    "2026-09-01-everything-you-know-is-training-data": {
      "type": "number"
    },
    "2026-02-18-play-russian-roulette-with-every-human-being-on-earth": {
      "type": "number"
    },
    "2026-09-09-without-a-rigorous-understanding-of-its-mind": {
      "type": "number"
    },
    "2026-09-26-upping-my-p-doom": {
      "type": "number"
    },
    "2026-09-13-whoever-wins-ai-wins": {
      "type": "number"
    },
    "2026-09-26-robots-should-fight-not-people": {
      "type": "number"
    },
    "2026-09-09-what-will-the-next-few-years-actually-feel-like": {
      "type": "number"
    },
    "2026-09-01-ineffective-altruism": {
      "type": "number"
    },
    "1968-04-02-im-sorry-dave-im-afraid-i-cant-do-that": {
      "type": "number"
    },
    "2026-09-01-compute-is-the-new-oil": {
      "type": "number"
    },
    "2026-09-01-you-are-a-victim-of-your-context-window": {
      "type": "number"
    },
    "2026-06-23-one-of-the-largest-uncontrolled-experiments-humanity-has-eve": {
      "type": "number"
    },
    "2026-09-26-oh-my-god-it-looks-like-a-teletubby": {
      "type": "number"
    },
    "1965-01-01-the-last-invention-that-man-need-ever-make": {
      "type": "number"
    },
    "2026-09-22-super-intelligence": {
      "type": "number"
    },
    "2026-09-27-i-dont-think-people-realize-how-powerful-and-thus-dangerous-": {
      "type": "number"
    },
    "2026-09-27-they-lie-cheat-deceive-even-try-to-blackmail-to-preserve-the": {
      "type": "number"
    },
    "2026-09-26-make-sure-that-humans-stay-in-charge": {
      "type": "number"
    }
  }
}
```
### `POST` /api/presence
```json
{
  "type": "object",
  "properties": {
    "live": {
      "type": "number"
    },
    "now": {
      "type": "number"
    },
    "likes": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /data/menu.json
```json
{
  "type": "object",
  "properties": {
    "quotes": {
      "type": "number"
    },
    "speakers": {
      "type": "number"
    },
    "topics": {
      "type": "number"
    },
    "years": {
      "type": "number"
    },
    "hot": {
      "type": "number"
    },
    "news": {
      "type": "number"
    },
    "generated": {
      "type": "string"
    }
  }
}
```
### `GET` /data/zoom.json
```json
{
  "type": "object",
  "properties": {
    "generated": {
      "type": "string"
    },
    "roles": {
      "type": "object",
      "properties": {
        "Sam Altman": {
          "type": "string"
        },
        "Gary Marcus": {
          "type": "string"
        },
        "Dario Amodei": {
          "type": "string"
        },
        "Yann LeCun": {
          "type": "string"
        },
        "Jensen Huang": {
          "type": "string"
        },
        "Geoffrey Hinton": {
          "type": "string"
        },
        "Elon Musk": {
          "type": "string"
        },
        "Donald Trump": {
          "type": "string"
        },
        "Mustafa Suleyman": {
          "type": "string"
        },
        "Mark Zuckerberg": {
          "type": "string"
        },
        "Ilya Sutskever": {
          "type": "string"
        },
        "Satya Nadella": {
          "type": "string"
        },
        "Pope Leo XIV": {
          "type": "string"
        },
        "Demis Hassabis": {
          "type": "string"
        },
        "Sundar Pichai": {
          "type": "string"
        },
        "Nathan Lambert": {
          "type": "string"
        },
        "Jack Clark": {
          "type": "string"
        },
        "Zvi Mowshowitz": {
          "type": "string"
        },
        "Stuart Russell": {
          "type": "string"
        },
        "Eliezer Yudkowsky": {
          "type": "string"
        }
      }
    },
    "briefs": {
      "type": "object",
      "properties": {
        "2026-10-18-ai-has-not-come-to-replace-you-it-has-come-to-help-you": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-agentic-flooding": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-a-world-which-feels-more-not-less-automated-and-in-many-case": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-each-new-encoding-trick-is-a-new-hole": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-cute-demo-but-totally-impractical": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-do-not-fear-ai-understand-it-and-remain-adaptable": {
          "type": "object",
          "properties": {
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-i-dont-think-there-will-be-robots-walking-the-streets-for-a-": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-if-youre-not-there-to-understand-ai-ai-will-take-over-from-y": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-i-think-of-all-agents-as-insider-risk": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-its-time-to-take-your-profits-and-not-get-greedy": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-the-risks-of-ai-are-real-but-manageable": {
          "type": "object",
          "properties": {
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-the-correction-is-coming-to-ai": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-just-a-notch-above-being-stupid-maybe-as-smart-as-an-insect": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-the-world-is-very-much-designed-for-people": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-this-is-not-about-scraping-news-sites": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-vertically-integrated-ai-utility": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-theyre-looking-to-connect-to-the-grid-tomorrow-not-in-two-ye": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-18-very-fast-power-fluctuation-disrupts-the-grid": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-17-ai-generated-slop": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        },
        "2026-10-17-a-corrupt-senile-felon": {
          "type": "object",
          "properties": {
            "r": {
              "type": "any"
            },
            "v": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

