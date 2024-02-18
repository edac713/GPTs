# Knowledge in GPTs

Here is what you need to know about the GPT knowledge feature

## What is Knowledge?

Using the knowledge feature in a GPT, builders can upload files containing additional context. GPTs then use a variety of methods to access this data in response to user prompts.

## How does Knowledge work?

You can use the GPT editor to attach up to 20 files to a GPT. Each file can be up to 512 MB in size and can contain 2,000,000 tokens. You can include files containing images, but only the text is currently processed. When you upload a file, the GPT breaks the text up into chunks, creates embeddings (a mathematical way of representing text), and stores them for later use.

When a user interacts with your GPT, the GPT can access the uploaded files to get additional context to augment the user’s query. The GPT chooses one of the following methods based on the requirements of the user’s prompt:

1. Semantic search - Returns relevant text chunks as described above.
   - Preferred when responding to “Q&A” style prompts, where a specific portion of the source document is required.
  
2. Document review - Entire short documents and/or relevant excerpts of larger documents are returned and included along with the prompt as additional context.
   - Preferred when responding to summarization or translation prompts, where the entire source document is required.

## When to use Knowledge

Currently, the only way to manage the files attached to a GPT is using the GPT Builder UI. This means it is best for applications where context changes infrequently (employee handbooks, policy documents, school curricula, etc).

## Tips for getting the most out of Knowledge

1. The file parser we use to extract text from documents work best with simple formatting. A single column of text is best. The parser can struggle with multi-column PDFs, and won’t understand the nuance conveyed by the relative positions of text on a PowerPoint slide.
2. Using Instructions in the GPT editor, you can encourage the GPT to rely on Knowledge first before searching the internet.
3. By default, GPTs will avoid revealing the names of uploaded files. If you want GPTs to “cite their sources,” indicate that in the Instructions.
