---
title: "APIs & Protocols: www-thelasttango-com"
date: 2026-11-14
target: "www-thelasttango-com"
---

# Discovered APIs & Protocols: www-thelasttango-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/webgl/config.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /webgl/config.json
```json
{
  "type": "object",
  "properties": {
    "audio": {
      "type": "object",
      "properties": {
        "master_volume": {
          "type": "number"
        },
        "tracks": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "names": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "segmentation": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "threshold": {
          "type": "number"
        },
        "bit": {
          "type": "number"
        },
        "star": {
          "type": "object",
          "properties": {
            "density": {
              "type": "any"
            },
            "size": {
              "type": "any"
            },
            "brightness": {
              "type": "any"
            }
          }
        },
        "ball": {
          "type": "object",
          "properties": {
            "density": {
              "type": "any"
            },
            "size": {
              "type": "any"
            },
            "brightness": {
              "type": "any"
            }
          }
        },
        "team": {
          "type": "object",
          "properties": {
            "density": {
              "type": "any"
            },
            "size": {
              "type": "any"
            },
            "brightness": {
              "type": "any"
            }
          }
        },
        "other": {
          "type": "object",
          "properties": {
            "density": {
              "type": "any"
            },
            "size": {
              "type": "any"
            },
            "brightness": {
              "type": "any"
            }
          }
        }
      }
    },
    "ball_trail": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "scale": {
          "type": "number"
        },
        "fade_seconds": {
          "type": "number"
        },
        "intensity": {
          "type": "number"
        },
        "color": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "scene": {
      "type": "object",
      "properties": {
        "background": {
          "type": "string"
        },
        "fog_density": {
          "type": "number"
        }
      }
    },
    "camera": {
      "type": "object",
      "properties": {
        "fov": {
          "type": "number"
        },
        "near": {
          "type": "number"
        },
        "far": {
          "type": "number"
        },
        "zoom": {
          "type": "number"
        },
        "orbit_speed": {
          "type": "number"
        },
        "orbit_elev": {
          "type": "number"
        },
        "damping": {
          "type": "number"
        },
        "lookat_y": {
          "type": "number"
        },
        "focal_length": {
          "type": "number"
        },
        "position": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "look_at": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "tracking": {
          "type": "string"
        },
        "track_follow": {
          "type": "number"
        },
        "min_terrain_clearance": {
          "type": "number"
        }
      }
    },
    "terrain": {
      "type": "object",
      "properties": {
        "dot_pitch": {
          "type": "number"
        },
        "mesh_resolution": {
          "type": "number"
        },
        "brightness": {
          "type": "number"
        },
        "jitter": {
          "type": "number"
        },
        "min_point_px": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "depth": {
          "type": "number"
        },
        "rotation_x": {
          "type": "number"
        },
        "ridge_center": {
          "type": "number"
        },
        "ridge_strength": {
          "type": "number"
        },
        "ridge_falloff": {
          "type": "number"
        },
        "noise_scale": {
          "type": "number"
        },
        "noise_offset": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "height_mult": {
          "type": "number"
        },
        "height_offset": {
          "type": "number"
        },
        "edge_fade_power": {
          "type": "number"
        },
        "coverage": {
          "type": "number"
        }
      }
    },
    "ambient": {
      "type": "object",
      "properties": {
        "height_min": {
          "type": "number"
        },
        "height_range": {
          "type": "number"
        },
        "point_size_ratio": {
          "type": "number"
        },
        "lift": {
          "type": "number"
        },
        "tilt_follow": {
          "type": "number"
        }
      }
    },
    "colors": {
      "type": "object",
      "properties": {
        "low": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "mid": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "bright": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "height_scale": {
          "type": "number"
        },
        "height_offset": {
          "type": "number"
        },
        "fade_near": {
          "type": "number"
        },
        "fade_far": {
          "type": "number"
        },
        "base_alpha": {
          "type": "number"
        },
        "disc_inner": {
          "type": "number"
        },
        "disc_outer": {
          "type": "number"
        }
      }
    },
    "tiers": {
      "type": "object",
      "properties": {
        "high": {
          "type": "object",
          "properties": {
            "cols": {
              "type": "any"
            },
            "rows": {
              "type": "any"
            },
            "octaves": {
              "type": "any"
            },
            "dpr_max": {
              "type": "any"
            },
            "ambient_count": {
              "type": "any"
            },
            "animated": {
              "type": "any"
            },
            "point_size": {
              "type": "any"
            }
          }
        },
        "medium": {
          "type": "object",
          "properties": {
            "cols": {
              "type": "any"
            },
            "rows": {
              "type": "any"
            },
            "octaves": {
              "type": "any"
            },
            "dpr_max": {
              "type": "any"
            },
            "ambient_count": {
              "type": "any"
            },
            "animated": {
              "type": "any"
            },
            "point_size": {
              "type": "any"
            }
          }
        },
        "low": {
          "type": "object",
          "properties": {
            "cols": {
              "type": "any"
            },
            "rows": {
              "type": "any"
            },
            "octaves": {
              "type": "any"
            },
            "dpr_max": {
              "type": "any"
            },
            "ambient_count": {
              "type": "any"
            },
            "animated": {
              "type": "any"
            },
            "point_size": {
              "type": "any"
            }
          }
        }
      }
    },
    "post_fx": {
      "type": "object",
      "properties": {
        "vignette_offset": {
          "type": "number"
        },
        "vignette_darkness": {
          "type": "number"
        },
        "pointer_amp": {
          "type": "number"
        },
        "pointer_damping": {
          "type": "number"
        },
        "video_max_world_size": {
          "type": "number"
        },
        "video_fade_duration": {
          "type": "number"
        },
        "camera_anim_duration": {
          "type": "number"
        },
        "bloom_strength": {
          "type": "number"
        },
        "bloom_radius": {
          "type": "number"
        },
        "bloom_threshold": {
          "type": "number"
        },
        "video_parallax_amp": {
          "type": "number"
        },
        "pointer_rot_amp": {
          "type": "number"
        },
        "scrub_smoothing": {
          "type": "number"
        },
        "scrub_sensitivity": {
          "type": "number"
        }
      }
    },
    "video_fx": {
      "type": "object",
      "properties": {
        "group_scale": {
          "type": "number"
        },
        "mesh_depth_scale": {
          "type": "number"
        },
        "mesh_depth_bias": {
          "type": "number"
        },
        "mesh_opacity": {
          "type": "number"
        },
        "mesh_blending": {
          "type": "number"
        },
        "mesh_use_color": {
          "type": "boolean"
        },
        "cloud_depth_scale": {
          "type": "number"
        },
        "cloud_depth_bias": {
          "type": "number"
        },
        "cloud_emissive_intensity": {
          "type": "number"
        },
        "depth_smooth_radius": {
          "type": "number"
        },
        "depth_edge_max": {
          "type": "number"
        },
        "cloud_opacity": {
          "type": "number"
        },
        "cloud_point_size": {
          "type": "number"
        },
        "cloud_blending": {
          "type": "number"
        },
        "cloud_depth_write": {
          "type": "boolean"
        },
        "point_cloud_order": {
          "type": "number"
        },
        "terrain_order": {
          "type": "number"
        },
        "video_mesh_order": {
          "type": "number"
        },
        "mask_radius": {
          "type": "number"
        },
        "mask_smoothness": {
          "type": "number"
        }
      }
    },
    "cover": {
      "type": "object",
      "properties": {
        "initial": {
          "type": "boolean"
        },
        "segmentation": {
          "type": "boolean"
        },
        "cloud_emissive_intensity": {
          "type": "number"
        },
        "cloud_saturation": {
          "type": "number"
        },
        "image": {
          "type": "string"
        },
        "file": {
          "type": "string"
        },
        "mesh_depth_scale": {
          "type": "number"
        },
        "cloud_depth_scale": {
          "type": "number"
        },
        "cloud_cols": {
          "type": "number"
        },
        "cloud_rows": {
          "type": "number"
        },
        "terrain_position": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "terrain_rotation": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "atlas_height": {
          "type": "number"
        },
        "color_height": {
          "type": "number"
        },
        "depth_direction": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "depth_fov": {
          "type": "number"
        },
        "depth_k1": {
          "type": "number"
        },
        "depth_k2": {
          "type": "number"
        },
        "video_position": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "audio": {
          "type": "string"
        }
      }
    },
    "camera_types": {
      "type": "object",
      "properties": {
        "tv": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "follow": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "goal_cam": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "close": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        }
      }
    },
    "videos": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "label": {
            "type": "any"
          },
          "initial": {
            "type": "any"
          },
          "file": {
            "type": "any"
          },
          "terrain_dot_pitch": {
            "type": "any"
          },
          "terrain_brightness": {
            "type": "any"
          },
          "terrain_coverage": {
            "type": "any"
          },
          "camera_type": {
            "type": "any"
          },
          "cloud_cols": {
            "type": "any"
          },
          "cloud_rows": {
            "type": "any"
          },
          "cloud_point_size": {
            "type": "any"
          },
          "alt_cams": {
            "type": "any"
          },
          "terrain_position": {
            "type": "any"
          },
          "terrain_rotation": {
            "type": "any"
          },
          "atlas_height": {
            "type": "any"
          },
          "color_height": {
            "type": "any"
          },
          "depth_direction": {
            "type": "any"
          },
          "depth_fov": {
            "type": "any"
          },
          "depth_k1": {
            "type": "any"
          },
          "depth_k2": {
            "type": "any"
          }
        }
      }
    },
    "404": {
      "type": "object",
      "properties": {
        "initial": {
          "type": "boolean"
        },
        "segmentation": {
          "type": "boolean"
        },
        "cloud_emissive_intensity": {
          "type": "number"
        },
        "cloud_point_size": {
          "type": "number"
        },
        "cloud_saturation": {
          "type": "number"
        },
        "image": {
          "type": "string"
        },
        "file": {
          "type": "string"
        },
        "mesh_depth_scale": {
          "type": "number"
        },
        "cloud_depth_scale": {
          "type": "number"
        },
        "cloud_cols": {
          "type": "number"
        },
        "cloud_rows": {
          "type": "number"
        },
        "terrain_position": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "terrain_rotation": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "atlas_height": {
          "type": "number"
        },
        "color_height": {
          "type": "number"
        },
        "depth_direction": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "depth_fov": {
          "type": "number"
        },
        "depth_k1": {
          "type": "number"
        },
        "depth_k2": {
          "type": "number"
        },
        "video_position": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "records": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "initial": {
            "type": "any"
          },
          "segmentation": {
            "type": "any"
          },
          "cloud_emissive_intensity": {
            "type": "any"
          },
          "cloud_point_size": {
            "type": "any"
          },
          "cloud_saturation": {
            "type": "any"
          },
          "image": {
            "type": "any"
          },
          "terrain_height_mult": {
            "type": "any"
          },
          "file": {
            "type": "any"
          },
          "mesh_depth_scale": {
            "type": "any"
          },
          "cloud_depth_scale": {
            "type": "any"
          },
          "cloud_cols": {
            "type": "any"
          },
          "cloud_rows": {
            "type": "any"
          },
          "terrain_position": {
            "type": "any"
          },
          "terrain_rotation": {
            "type": "any"
          },
          "atlas_height": {
            "type": "any"
          },
          "color_height": {
            "type": "any"
          },
          "depth_direction": {
            "type": "any"
          },
          "depth_fov": {
            "type": "any"
          },
          "depth_k1": {
            "type": "any"
          },
          "depth_k2": {
            "type": "any"
          }
        }
      }
    },
    "pointer_star": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "orbit": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "count": {
              "type": "any"
            },
            "radius_scale": {
              "type": "any"
            },
            "speed": {
              "type": "any"
            },
            "hide_center": {
              "type": "any"
            }
          }
        }
      }
    },
    "frontal_debug": {
      "type": "boolean"
    }
  }
}
```

