"""Write index.json: one entry per night, newest first, for the dream site's archive."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

nights = []
for path in sorted((ROOT / "dreams").glob("*.json"), reverse=True):
    try:
        d = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        continue
    date = d.get("date") or path.stem
    nights.append({
        "date": date,
        "mood": d.get("mood", ""),
        "comic": (ROOT / "comics" / f"{date}.jpg").exists(),
    })

(ROOT / "index.json").write_text(json.dumps({"nights": nights}, indent=2, ensure_ascii=False) + "\n")
print(f"index.json: {len(nights)} nights")
