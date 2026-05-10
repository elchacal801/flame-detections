# Architecture

## Overview

**flame-detections** is the detection content sibling of [flame-fraud](https://github.com/elchacal801/flame-fraud) (the FLAME fraud intelligence exchange). This repository houses all detection rules; flame-fraud houses the taxonomy, threat paths, and intelligence context.

## Detection Rule Format

Detection rules are Sigma-format YAML files stored under `DetectionLogic/`. Each rule file contains:

- Standard Sigma fields (title, status, level, detection, etc.)
- FLAME-specific fields (`sigma_compatible`, `threat_paths`, `native_query_required`)
- For non-Sigma rules: a `queries:` block with hand-written CQL and SPL native queries

## Taxonomy Import

This repo imports the FLAME taxonomy via `scripts/sync_with_flame_taxonomy.py`. There is no git submodule and no vendored copy of the taxonomy. The script fetches the taxonomy from the FLAME GitHub Pages API and caches it locally at `data/flame_taxonomy_cached.json`.

This design keeps the two repositories loosely coupled: flame-detections consumes the taxonomy as a read-only dependency, and taxonomy updates flow through the API without requiring coordinated commits.

## Build Pipeline

```
DetectionLogic/          Source detection rules (Sigma YAML)
       |
       v
validate_rules.py        Validate rule structure, required fields,
       |                 and threat path IDs against cached taxonomy
       v
export_sigma.py          Convert Sigma-compatible rules to SPL, KQL,
       |                 EQL via pySigma backends
       v
sigma-exports/           Generated output files
```

## Relationship to flame-fraud

| Concern | flame-fraud | flame-detections |
|---------|------------|------------------|
| Taxonomy & threat paths | Owned here | Consumed via API |
| Detection rules | Being decoupled | Owned here |
| Intelligence reports | Owned here | Not applicable |
| Release cadence | Stable | Experimental |
| Quality bar | Production | Iterative |

The taxonomy is consumed, not duplicated. Threat path IDs (`TP-XXXX`) in detection rules are validated against the cached taxonomy to ensure referential integrity.
