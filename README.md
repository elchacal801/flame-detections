# FLAME Detections

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Open-source fraud detection rule pack built on FLAME taxonomy.**

This is the experimental detection-content sibling of [FLAME Exchange](https://github.com/elchacal801/flame-fraud). Different cadence, different quality bar, different contribution requirements. Detection rules live here; taxonomy, threat paths, and intelligence context live in flame-fraud.

---

## Stats

| Metric | Count |
|--------|-------|
| Total detection rules | 221 |
| Sigma-compatible rules | 98 (44%) |
| Native-query-required rules | 123 (56%) |

## Portability

**98 rules are pure Sigma** and auto-convert to SPL, EQL, and KQL via pySigma backends.

**123 rules require stateful correlation** that Sigma cannot express (aggregation, temporal sequencing, multi-event joins). For these we ship hand-written CQL and SPL native queries. KQL and EQL native equivalents are tracked as roadmap.

> **Note:** KQL output is generated via pySigma's Microsoft 365 Defender backend and is not ASIM-aligned.

> **Note:** Elasticsearch output uses the Lucene query backend, not native EQL.

See [docs/PORTABILITY.md](docs/PORTABILITY.md) for the full breakdown.

## Quick Start

### Prerequisites

```bash
python -m pip install -r requirements.txt
```

### Validate rules

```bash
python scripts/validate_rules.py
```

### Export Sigma packs

```bash
python scripts/export_sigma.py
```

### Sync FLAME taxonomy

```bash
python scripts/sync_with_flame_taxonomy.py
```

This fetches the current FLAME taxonomy from [flameintel.org](https://flameintel.org) and caches it locally for rule validation.

## Repository Structure

```
flame-detections/
  DetectionLogic/       # Sigma-format YAML detection rules
  sigma-exports/        # Auto-generated Sigma exports (SPL, KQL, EQL)
  data/                 # Cached taxonomy and reference data
  scripts/              # Build and validation scripts
  tests/                # Pytest test suite
  docs/                 # Architecture and design docs
```

## Relationship to FLAME Exchange

This repo consumes the [FLAME taxonomy](https://github.com/elchacal801/flame-fraud) but does not duplicate it. Threat path IDs (TP-XXXX) referenced in detection rules are validated against a cached copy of the taxonomy fetched from the FLAME GitHub Pages API.

For taxonomy context, threat intelligence, and the full fraud kill chain, see [flame-fraud](https://github.com/elchacal801/flame-fraud).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the quality bar and submission requirements.

## License

This project is licensed under the MIT License.
