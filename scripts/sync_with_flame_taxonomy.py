"""Sync FLAME taxonomy from the flame-fraud GitHub Pages API.

Fetches the current taxonomy from https://flameintel.org/api/v1/taxonomy.json
and caches it locally at data/flame_taxonomy_cached.json.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

TAXONOMY_URL = "https://flameintel.org/api/v1/taxonomy.json"
CACHE_PATH = Path(__file__).resolve().parent.parent / "data" / "flame_taxonomy_cached.json"


def sync_taxonomy() -> None:
    """Fetch the FLAME taxonomy and write it to the local cache."""
    try:
        response = requests.get(TAXONOMY_URL, timeout=30)
        response.raise_for_status()
    except requests.ConnectionError:
        print(f"ERROR: Could not connect to {TAXONOMY_URL}")
        sys.exit(1)
    except requests.Timeout:
        print(f"ERROR: Request to {TAXONOMY_URL} timed out")
        sys.exit(1)
    except requests.HTTPError as e:
        print(f"ERROR: HTTP {e.response.status_code} from {TAXONOMY_URL}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"ERROR: Failed to fetch taxonomy: {e}")
        sys.exit(1)

    taxonomy_data = response.json()

    cached = {
        "_metadata": {
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "source": TAXONOMY_URL,
        },
        "taxonomy": taxonomy_data,
    }

    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cached, indent=2), encoding="utf-8")

    print(f"SUCCESS: FLAME taxonomy cached to {CACHE_PATH}")
    print(f"  Source: {TAXONOMY_URL}")
    print(f"  Fetched at: {cached['_metadata']['fetched_at']}")


if __name__ == "__main__":
    sync_taxonomy()
