import json
from pathlib import Path

REMOVE_KEYS = {
    "credentials",
    "webhookId",
    "instanceId",
    "versionId",
    "id",
    "cachedResultUrl",
}

for path in Path(".").rglob("*.json"):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        continue

    def clean(obj):
        if isinstance(obj, dict):
            return {
                k: clean(v)
                for k, v in obj.items()
                if k not in REMOVE_KEYS
            }
        if isinstance(obj, list):
            return [clean(x) for x in obj]
        return obj

    cleaned = clean(data)
    path.write_text(json.dumps(cleaned, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("sanitized:", path)