# MAGNIFIC AI

## Scale factor

- 2x
- 4x
- 8x
- 16x

## Optimized for

- Standard
- Portraits (Soft)
- Portraits (Hard)
- Art & Illustrations
- Videogame Assets
- Nature & Landscapes
- Films & Photography
- 3d Renders
- Science Fiction & Horror

## Prompt

You can guide the upscaling process with a descriptive prompt. If the image you're upscaling is AI-generated, reusing the original prompt here can greatly improve the upscaling quality!

You can also use your imagination to alter images: for example, transform a city into ruins during the upscaling process (typically after at least 4x upscale), change a person's eye color, or give a portrait the look of a famous person.

IMPORTANT: You can weigh specific parts of the prompt by using a number in parentheses, ranging from 1 to 1.4, like "(beautiful green eyes:1.3)". Magnific AI sometimes ages faces in its outputs. To counter this, adjust your prompt weights, for example: "(young woman:1.3), (cute young face:1.2), (cute:1.2)".

## Creativity

Value ranges = (-10) to (+10)
Default = 0

Allows the AI to "hallucinate" additional details, achieving greater realism at the cost of moving further away from the original image. Here's where Magnific's magic shines! But be careful: really high values can lead to some pretty strange results.

## HDR

Value ranges = (-10) to (+10)
Default = 0

Increases definition and detail, though very high values can result in images with an artificial appearance or blotches.

## Resemblance

Value ranges = (-10) to (+10)
Default = 0

(Advanced) Increasing this value will make the generation more closely resemble the original image, but very high values can result in blotches or a dirtier look. Lower values give more freedom to the generation at the cost of moving further away from the original image.

## Fractality

range: min="-10" max="10" value="0" id="mySlider4">

(Advanced) Control the strength of your prompt and intricacy per square pixel:

- Lower Fractality: less detail, but typically resulting in fewer glitches. If vertical bands appear in your image, reducing Fractality might resolve it.
- Higher Fractality: amplifies your prompt in increasingly smaller areas of your overall image. E.g., if your image is a rose and you use "A photograph of a rose" as your prompt with a high Fractality value, smaller rose-like details may emerge within the main rose. A bit crazy, but this can be useful sometimes for artistic purposes. For intricate images, like fantasy maps, high Fractality at resolutions up to 10k can generate astonishing details like rivers, mountains, and cities suggested in your prompt.
- 