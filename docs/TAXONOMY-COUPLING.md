# Taxonomy Coupling

## How flame-detections imports the FLAME taxonomy

flame-detections imports the FLAME taxonomy via `scripts/sync_with_flame_taxonomy.py`. This script fetches the taxonomy from the FLAME GitHub Pages API and caches it locally.

## Mechanism

- **Source:** https://flameintel.org/api/v1/taxonomy.json
- **Local cache:** `data/flame_taxonomy_cached.json`
- **No git submodule.** The taxonomy is not vendored or pinned to a specific commit.
- **No vendoring.** There is no copy of flame-fraud source code in this repository.

## Refresh Strategy

The cached taxonomy is refreshed:

- **On-demand:** Run `python scripts/sync_with_flame_taxonomy.py` manually.
- **Via daily cron:** A scheduled workflow (planned) will refresh the cache automatically.

The cache file includes metadata with a `fetched_at` timestamp so you can verify currency.

## Validation

Threat path IDs (`TP-XXXX`) referenced in detection rules are validated against the cached taxonomy during rule validation (`scripts/validate_rules.py`). If a rule references a threat path ID that does not exist in the cached taxonomy, validation fails.

This ensures referential integrity between detection rules and the FLAME taxonomy without requiring the two repositories to share a release cadence.

## Why Not a Git Submodule?

Git submodules create tight coupling between repositories and require coordinated updates. The API-based approach allows flame-detections to consume taxonomy updates independently, on its own schedule, without requiring contributors to manage submodule state.
