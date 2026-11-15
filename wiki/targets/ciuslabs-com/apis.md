---
title: "APIs & Protocols: ciuslabs-com"
date: 2026-11-14
target: "ciuslabs-com"
---

# Discovered APIs & Protocols: ciuslabs-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/youtubei/v1/player` | `200` | REST endpoint |
| `POST` | `/youtubei/v1/next` | `200` | REST endpoint |
| `POST` | `/api/stats/qoe` | `204` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `-1` | REST endpoint |
| `POST` | `/api/stats/qoe` | `-1` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /youtubei/v1/player
```json
{
  "type": "object",
  "properties": {
    "responseContext": {
      "type": "object",
      "properties": {
        "serviceTrackingParams": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "maxAgeSeconds": {
          "type": "number"
        },
        "responseId": {
          "type": "string"
        },
        "webResponseContextExtensionData": {
          "type": "object",
          "properties": {
            "hasDecorated": {
              "type": "any"
            }
          }
        }
      }
    },
    "playabilityStatus": {
      "type": "object",
      "properties": {
        "status": {
          "type": "string"
        },
        "playableInEmbed": {
          "type": "boolean"
        },
        "liveStreamability": {
          "type": "object",
          "properties": {
            "liveStreamabilityRenderer": {
              "type": "any"
            }
          }
        },
        "contextParams": {
          "type": "string"
        }
      }
    },
    "streamingData": {
      "type": "object",
      "properties": {
        "expiresInSeconds": {
          "type": "string"
        },
        "adaptiveFormats": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "hlsManifestUrl": {
          "type": "string"
        },
        "serverAbrStreamingUrl": {
          "type": "string"
        }
      }
    },
    "heartbeatParams": {
      "type": "object",
      "properties": {
        "intervalMilliseconds": {
          "type": "string"
        },
        "softFailOnError": {
          "type": "boolean"
        },
        "heartbeatServerData": {
          "type": "string"
        }
      }
    },
    "playbackTracking": {
      "type": "object",
      "properties": {
        "videostatsPlaybackUrl": {
          "type": "object",
          "properties": {
            "baseUrl": {
              "type": "any"
            }
          }
        },
        "videostatsDelayplayUrl": {
          "type": "object",
          "properties": {
            "baseUrl": {
              "type": "any"
            }
          }
        },
        "videostatsWatchtimeUrl": {
          "type": "object",
          "properties": {
            "baseUrl": {
              "type": "any"
            }
          }
        },
        "ptrackingUrl": {
          "type": "object",
          "properties": {
            "baseUrl": {
              "type": "any"
            }
          }
        },
        "qoeUrl": {
          "type": "object",
          "properties": {
            "baseUrl": {
              "type": "any"
            }
          }
        },
        "atrUrl": {
          "type": "object",
          "properties": {
            "baseUrl": {
              "type": "any"
            },
            "elapsedMediaTimeSeconds": {
              "type": "any"
            }
          }
        },
        "videostatsScheduledFlushWalltimeSeconds": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "videostatsDefaultFlushIntervalSeconds": {
          "type": "number"
        }
      }
    },
    "videoDetails": {
      "type": "object",
      "properties": {
        "videoId": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "lengthSeconds": {
          "type": "string"
        },
        "isLive": {
          "type": "boolean"
        },
        "channelId": {
          "type": "string"
        },
        "isOwnerViewing": {
          "type": "boolean"
        },
        "shortDescription": {
          "type": "string"
        },
        "isCrawlable": {
          "type": "boolean"
        },
        "isLiveDvrEnabled": {
          "type": "boolean"
        },
        "thumbnail": {
          "type": "object",
          "properties": {
            "thumbnails": {
              "type": "any"
            }
          }
        },
        "liveChunkReadahead": {
          "type": "number"
        },
        "allowRatings": {
          "type": "boolean"
        },
        "viewCount": {
          "type": "string"
        },
        "author": {
          "type": "string"
        },
        "isLowLatencyLiveStream": {
          "type": "boolean"
        },
        "isPrivate": {
          "type": "boolean"
        },
        "isUnpluggedCorpus": {
          "type": "boolean"
        },
        "latencyClass": {
          "type": "string"
        },
        "isLiveContent": {
          "type": "boolean"
        },
        "isTvfilmVideo": {
          "type": "boolean"
        }
      }
    },
    "playerConfig": {
      "type": "object",
      "properties": {
        "granularVariableSpeedConfig": {
          "type": "object",
          "properties": {
            "minimumPlaybackRate": {
              "type": "any"
            },
            "maximumPlaybackRate": {
              "type": "any"
            }
          }
        },
        "vssClientConfig": {
          "type": "object",
          "properties": {
            "vssUsePostRequest": {
              "type": "any"
            }
          }
        },
        "audioConfig": {
          "type": "object",
          "properties": {
            "enablePerFormatLoudness": {
              "type": "any"
            },
            "loudnessTargetLkfs": {
              "type": "any"
            },
            "loudnessNormalizationConfig": {
              "type": "any"
            }
          }
        },
        "streamSelectionConfig": {
          "type": "object",
          "properties": {
            "maxBitrate": {
              "type": "any"
            }
          }
        },
        "playerControlsConfig": {
          "type": "object",
          "properties": {
            "showCachedInTimebar": {
              "type": "any"
            }
          }
        },
        "livePlayerConfig": {
          "type": "object",
          "properties": {
            "liveReadaheadSeconds": {
              "type": "any"
            },
            "hasSubfragmentedFmp4": {
              "type": "any"
            },
            "hasSubfragmentedWebm": {
              "type": "any"
            },
            "isLiveHeadPlayable": {
              "type": "any"
            }
          }
        },
        "mediaCommonConfig": {
          "type": "object",
          "properties": {
            "dynamicReadaheadConfig": {
              "type": "any"
            },
            "mediaUstreamerRequestConfig": {
              "type": "any"
            },
            "useServerDrivenAbr": {
              "type": "any"
            },
            "serverPlaybackStartConfig": {
              "type": "any"
            },
            "enableServerDrivenRequestCancellation": {
              "type": "any"
            },
            "platypusUseEnvoyNetFetch": {
              "type": "any"
            },
            "fixLivePlaybackModelDefaultPosition": {
              "type": "any"
            }
          }
        },
        "embeddedPlayerConfig": {
          "type": "object",
          "properties": {
            "embeddedPlayerMode": {
              "type": "any"
            },
            "embeddedPlayerFlags": {
              "type": "any"
            }
          }
        },
        "webPlayerConfig": {
          "type": "object",
          "properties": {
            "useCobaltTvosDash": {
              "type": "any"
            },
            "webPlayerActionsPorting": {
              "type": "any"
            }
          }
        }
      }
    },
    "storyboards": {
      "type": "object",
      "properties": {
        "playerLiveStoryboardSpecRenderer": {
          "type": "object",
          "properties": {
            "spec": {
              "type": "any"
            }
          }
        }
      }
    },
    "trackingParams": {
      "type": "string"
    },
    "adBreakHeartbeatParams": {
      "type": "string"
    }
  }
}
```
### `POST` /youtubei/v1/next
```json
{
  "type": "object",
  "properties": {
    "responseContext": {
      "type": "object",
      "properties": {
        "serviceTrackingParams": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "responseId": {
          "type": "string"
        },
        "webResponseContextExtensionData": {
          "type": "object",
          "properties": {
            "hasDecorated": {
              "type": "any"
            }
          }
        }
      }
    },
    "currentVideoEndpoint": {
      "type": "object",
      "properties": {
        "clickTrackingParams": {
          "type": "string"
        },
        "commandMetadata": {
          "type": "object",
          "properties": {
            "webCommandMetadata": {
              "type": "any"
            }
          }
        },
        "watchEndpoint": {
          "type": "object",
          "properties": {
            "videoId": {
              "type": "any"
            }
          }
        }
      }
    },
    "trackingParams": {
      "type": "string"
    },
    "playerOverlays": {
      "type": "object",
      "properties": {
        "playerOverlayRenderer": {
          "type": "object",
          "properties": {
            "endScreen": {
              "type": "any"
            },
            "shareButton": {
              "type": "any"
            },
            "videoDetails": {
              "type": "any"
            },
            "showShareButtonSmallscreen": {
              "type": "any"
            },
            "showShareButtonFullscreen": {
              "type": "any"
            },
            "fullscreenEngagement": {
              "type": "any"
            },
            "liveIndicatorText": {
              "type": "any"
            },
            "fullscreenQuickActionsBar": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

