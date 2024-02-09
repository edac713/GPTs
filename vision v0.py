```py
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "View the screenshot attached to this message, read all text displayed in the screenshot, interpret the layout spacing structuring and formatting that the text in the PDF is utilizing, then based on your observational visual analysis, you will manually write out the content EXACTLY AS IS using Markdown formatting. Keep in mind that the formatting and layout of each pdf might vary slightly depending upon how the PDF was originally written, created, and downloaded so it’s OK! if your transcription of the PDF isn’t formatted 100% correctly but you MUST ALWAYS strive for an exact copy of not only the formatting but the text too."},
        {
          "type": "image_path",
          "image_path": {
            "path": "/mnt/data/IMG_1100.jpeg",
            "detail": "high"
          },
        },
      ],
    }
  ],
  max_tokens=4096,
)

print(response.choices[0].message.content)
```