# Duck Dreams

Every morning at 7:07 (Pacific), a scheduled Claude task writes a two-paragraph dream for Yellow Duck Sweater, the robot microduck trained at [microduck-challenges](https://github.com/StephenForte/microduck-challenges), and commits it here.

The dream is built from the duck's training runs on [Hugging Face](https://huggingface.co/YellowDuckSweater), the Menlo Park weather, its portfolio (SPCX, BTC, GE), the moon, and ideas sent in from the duck page.

## Read the dreams

https://stephenforte.github.io/duck-dreams/

Today's comic and dream, with every earlier night below. Ideas for the duck go in through the duck page on Claude, linked from the site.

## Files

| Path | What it is |
|---|---|
| `dreams/YYYY-MM-DD.json` | One dream per day |
| `latest.json` | A copy of the newest dream, at a fixed URL |
| `comics/YYYY-MM-DD.jpg` | The six-panel comic for each night, drawn by the workflow |
| `index.json` | List of nights for the site's archive |
| `index.html` | The dream site (GitHub Pages) |
| `reference/microduck.png` | Photo of the real robot |
| `reference/duck-visual.md` | The fixed character, comic layout, and style text every image prompt is built from |

Fixed URL for the newest dream:

```
https://raw.githubusercontent.com/StephenForte/duck-dreams/main/latest.json
```

## Dream format

```json
{
  "date": "2026-11-07",
  "mood": "crowded, then hopeful",
  "paragraphs": ["...", "..."],
  "text": "both paragraphs joined by a blank line",
  "imagePrompt": "character + layout + six panels + style, ready for an image model",
  "panels": ["one sentence per panel", "..."],
  "idea": null,
  "telemetry": {
    "moon": "waning crescent, 6%",
    "weather": "fog late, 73°F high",
    "portfolio": [{"symbol": "SPCX", "change": 8.6}],
    "training": "6 new runs, one per event"
  }
}
```

`imagePrompt` is the field to send to an image generator: it asks for a six-panel color comic of the dream. `panels` has the six panel descriptions on their own, for tools that draw one panel at a time. Attach `reference/microduck.png` too if the tool takes a reference image.

## The comic

`.github/workflows/comic.yml` runs whenever a new `latest.json` lands. It sends the `imagePrompt` and `reference/microduck.png` to OpenAI's image API (key in the `OPENAI_API_KEY` repository secret), saves `comics/<date>.jpg`, and rebuilds `index.json`. Set a repository variable `IMAGE_MODEL` to pick a different model. To redraw a comic, run the workflow by hand from the Actions tab with "Redraw" ticked.
