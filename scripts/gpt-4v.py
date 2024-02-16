```py
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "View the screenshot attached to this message, read all text displayed in the screenshot, interpret the layout spacing structuring and formatting that the text in the PDF is utilizing, then based on your observational visual analysis, you will manually write out the content EXACTLY AS IS using Markdown formatting. Keep in mind that the formatting and layout of each pdf might vary slightly depending upon how the PDF was originally written, created, and downloaded so it’s OK! if your transcription of the PDF isn’t formatted 100% correctly but you MUST ALWAYS strive for an exact copy of not only the formatting but the text too. Adopt a methodical and thoughtful approach when applying the goals and step-by-step instructions outlined above. Err on the side of providing ‘too much information,’ rather than settling for ‘just enough’ or ‘not enough.’ This approach ensures that the responses are comprehensive and detailed, offering the reader the utmost context and depth. Aim for a level of detail in the output that leaves no room for ambiguity, facilitating a richer understanding and enabling more informed decision-making. By adopting this strategy, the aim is to empower users with all the necessary information, anticipating and addressing potential questions or concerns proactively, thereby enhancing the overall effectiveness and user satisfaction.
Explore all possible paths that all relate to creating a Python script that converts PDFs (I will attached a screenshot of what the contents of said PDFs you will be working with look like, how they are structured/formatted/laid-out) into properly formatted text that is not a “sort of” exact copy of the content found in the PDF but the text when converted and extracted from said PDFs is a word for word, line by line, paragraph by paragraph, page by page EXACT COPY. There are a multitude of different methods and techniques that are inherently “baked” into your training data BUT none of these methods and techniques are tailored specifically for HOW the methodologies and techniques are actually applied and used, in other words you will need to dig deep into your own knowledge based on your training data to subsequently create a method that YOU (ChatGPT) can practically replicate and actually act upon and apply DIRECTLY in this conversation. You have my full unwavering authority and consent to take a view the screenshot of the PDF you will be converting into Markdown formatted text, AND a deep breath and finally working step by step!"},
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