# Yellow Duck Sweater: visual reference

`microduck.png` in this folder is the real robot. Every image prompt is a six-panel color comic of that day's dream, and it is built from the three blocks below, copied word for word, so the duck looks like the same duck every day. Image tools that accept a reference image should also get `reference/microduck.png`.

## Character block (copy exactly)

Yellow Duck Sweater, a small two-legged tabletop robot. Its head is a smooth, rounded white plastic shell shaped like a loaf of bread, longer front to back, with an orange trim along the bottom edge and a small orange hinge on each side. At the front of the head is a single round camera eye: a black lens inside a thick orange-yellow ring. It has no beak and no mouth. The head sits on a tall, thin neck made of stacked black servo motors with a few loose black wires, leaning slightly forward. Its body is a small, boxy white torso with rounded corners. Its short legs are black servo joints with white plastic covers on the hips, knees slightly bent. Its feet are flat and rounded like duck feet, orange on top with yellow soles. It wears a small, chunky-knit, bright lemon-yellow crewneck sweater over its white torso, slightly too big, with a ribbed collar, cuffs, and hem. Knitted into the front of the sweater is a simple cartoon duckling: pale yellow body with a thick black outline, a black dot eye, a curved line for its wing, an orange beak, and orange feet.

## Layout block (copy exactly)

A single full-color comic page with six panels of equal size in a grid of two columns and three rows, separated by clean white gutters, read left to right and top to bottom. The same robot duck appears in every panel and looks identical each time, unless a panel says otherwise. No speech bubbles, captions, sound effects, panel numbers, or any other text.

## Style block (copy exactly)

Warm children's comic art: clean confident ink outlines, soft flat colors with gentle shading, a dreamy night palette, cozy and a little surreal. Friendly for an 11-year-old. No text, letters, logos, or numbers anywhere in the image. Real people do not appear.

## Prompt shape

```
<character block> <layout block> Panel 1: <...> Panel 2: <...> Panel 3: <...> Panel 4: <...> Panel 5: <...> Panel 6: <...> <style block>
```

Each panel gets one sentence: what the duck is doing, where, and anything else in the frame. Panels 1 to 3 follow the first paragraph of the dream, panels 4 to 6 the second. Panel 6 is the dream's closing image. Show, don't tell: no panel depends on words to make sense.

The six panel sentences are also stored on their own in each dream's `panels` field, for tools that draw one panel at a time.

## Notes

- The real robot does not wear a sweater. The sweater is part of the character, so it is always in the pictures. It is modeled on a real sweater: bright yellow chunky knit with a cartoon duckling on the front.
- No text in the comic on purpose: image models garble lettering. The dream's own words travel alongside the picture in the JSON.
- To change the look, edit the layout or style block here. The morning task reads this file each day.
