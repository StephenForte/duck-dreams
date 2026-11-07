"""Turn the newest dream into a six-panel comic with OpenAI's image API.

Reads latest.json and reference/microduck.png, sends both to the image edits
endpoint, and saves the result as comics/<date>.jpg. Skips the work when that
file already exists, unless FORCE=1.

Environment:
  OPENAI_API_KEY  required (a repository secret)
  IMAGE_MODEL     optional, comma-separated models to try in order
  FORCE           optional, "1" to redraw an existing comic
"""
import base64
import io
import json
import os
import sys
from pathlib import Path

from openai import OpenAI, BadRequestError, NotFoundError, PermissionDeniedError
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MODELS = "gpt-image-2.5-flare,gpt-image-1"
SIZE = "1024x1536"  # portrait, fits a 2 x 3 grid
REFERENCE_NOTE = (
    "The attached photo shows the real robot this character is based on. "
    "Match its head shape, camera eye, neck, torso, legs, and feet as closely as the "
    "comic style allows, and add the sweater described below. "
)


def fail(msg: str) -> None:
    # ::error:: shows up as an annotation on the run, readable without logging in.
    print(f"::error::{msg}")
    sys.exit(1)


def main() -> None:
    dream = json.loads((ROOT / "latest.json").read_text())
    date = dream["date"]
    prompt = dream.get("imagePrompt")
    if not prompt:
        fail(f"latest.json for {date} has no imagePrompt")

    out = ROOT / "comics" / f"{date}.jpg"
    if out.exists() and os.environ.get("FORCE") != "1":
        print(f"{out.name} already exists; nothing to do.")
        return

    client = OpenAI()
    models = [m.strip() for m in os.environ.get("IMAGE_MODEL", "").split(",") if m.strip()]
    models = models or DEFAULT_MODELS.split(",")
    reference = ROOT / "reference" / "microduck.png"

    errors = []
    for model in models:
        for size in (SIZE, None):
            kwargs = {"model": model, "prompt": REFERENCE_NOTE + prompt}
            if size:
                kwargs["size"] = size
            try:
                with reference.open("rb") as ref:
                    result = client.images.edit(image=ref, **kwargs)
            except (NotFoundError, PermissionDeniedError) as e:
                errors.append(f"{model}: {e}")
                break  # model not available on this account; try the next one
            except BadRequestError as e:
                errors.append(f"{model} size={size}: {e}")
                if size and "size" in str(e).lower():
                    continue  # retry this model without a size
                break
            b64 = result.data[0].b64_json
            img = Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")
            out.parent.mkdir(exist_ok=True)
            img.save(out, "JPEG", quality=88, optimize=True)
            print(f"Saved {out.relative_to(ROOT)} with {model} ({img.width}x{img.height}).")
            return

    fail("No image model worked. " + " | ".join(errors)[:1500])


if __name__ == "__main__":
    main()
