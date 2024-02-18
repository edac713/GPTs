# File uploads FAQ

What’s changing?AvailabilityHow does the new file uploads capability work?What types of files are supported?How many files can I upload at once per GPT?What are those file upload size restrictions?How do I delete files I upload?How are files vs chats retained?Are you able to handle images embedded in docs/presentations?Will OpenAI use files uploaded to train its models?

## What’s changing?

We’re adding a new capability to upload and work with different types of documents inside ChatGPT. This capability builds on our existing Advanced Data Analysis model (formerly known as Code Interpreter) to improve performance on text-rich documents including PDFs, Microsoft Word documents, and presentations.

## Availability

Available now to all ChatGPT Plus and ChatGPT Enterprise users on the web at chat.openai.com, our iOS/Android mobile apps, and coming soon via API.

## How does the new file uploads capability work?

The file uploads capability was created to support the following tasks:

1. Synthesis: Combining or analyzing information from files and documents to create something new, for example:

   a. Upload a spreadsheet, for example a CSV, with a mix of qualitative and quantitative information, and ask ChatGPT to help you understand and visualize the data.

   b. Compare and contrast two documents.

   c. Analyze sentiment or tone in a document.

   d. Analyze a spreadsheet.

   e. Apply a framework or rubric from one document to the contents of another.

2. Transformation: Reshaping information from documents without changing its essence, for example:

   a. Upload a complicated research paper and ask ChatGPT to provide a simple summary.

   b. Upload a powerpoint presentation and ask ChatGPT for feedback on the content.

   c. Summarize a document in simple terms.

   d. Rewrite a short document in a particular style.

   e. Turn a presentation into a document.

3. Extraction: Pulling out specific information out of a document, for example:

   a. Upload a PDF and have ChatGPT find any references to a certain topic.

   b. Pull out relevant quotes from a document.

   c. Search for any mention of a particular topic from a document or spreadsheet.

   d. Extract metadata (author, creation date, etc.) from a document.

   e. Count the number of rows in a spreadsheet that contain a certain attribute

   f. Extract specific sections of a document (e.g., all headings or all bullet-point lists).

## What types of files are supported?

All common file extensions for text files, spreadsheets, presentations, and documents.

## How many files can I upload at once per GPT?

Up to 20 files per GPT for the lifetime of that GPT. Keep in mind there are file size restrictions and usage caps per user/org.

## What are those file upload size restrictions?

- All files uploaded to a GPT or a ChatGPT conversation have a hard limit of 512MB per file.

- All text and document files uploaded to a GPT or to a ChatGPT conversation are capped at 2M tokens per file. This limitation does not apply to spreadsheets.

- For images, there's a limit of 20MB per image.

- Additionally, there are usage caps:

  - Each end-user is capped at 10GB.

  - Each organization is capped at 100GB.

  - Note: An error will be displayed if a user/org cap has been hit.

## How do I delete files I upload?

Files uploaded to Advanced Data Analysis are deleted within 3 hours. If you are encountering your file usage cap, you can also delete files from recent chats or from any GPTs that you built, as these share caps.

## How are files vs chats retained?

Chats

1. Saved indefinitely provided Data Controls -> Chat History is = ON

2. If a chat is deleted from ChatGPT it is gone from the UI. To monitor for abuse, we will retain all conversations for 30 days before permanently deleting for good.

Files

1. Files processed via ADA / Document Analysis, and when chatting with a custom GPT (not uploaded as knowledge in GPT config): Retained for 3 hours.

2. Images processed via Vision and Files uploaded as knowledge to custom GPT: Retained indefinitely.

## Are you able to handle images embedded in docs/presentations?

Images embedded in documents/presentations (i.e. in image in the slide of a slide deck) are not supported yet. We plan to add support for this in the future.

## Will OpenAI use files uploaded to train its models?

The answer depends on the service you are using. As explained in this article, we may use content submitted to ChatGPT, DALL·E, and our other services for individuals to improve model performance. Content may include files that are uploaded. Please refer to this article to understand how content may be used to improve model performance and the choices that users have.

Please note that we do not use content submitted by customers to our business offerings such as our API and ChatGPT Enterprise to improve model performance.
