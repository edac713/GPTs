# Retrieval Augmented Generation (RAG) and Semantic Search for GPTs

Learn about RAG and how it is useful to GPT builders

## What is Retrieval Augmented Generation (RAG), and why is it valuable for GPT builders?

RAG is the process of *retrieving* relevant contextual information from a data source and passing that information to a large language model alongside the user’s prompt. This information is used to improve the model’s output (*generated* text or images) by *augmenting* the model’s base knowledge.

### Basic RAG workflow

1. User Submits prompt to → Large Language Model (LLM)
2. LLM Sumbmits query for context to → Data Source
3. Data Source Responds with relevant context to → LLM
4. LLM Consumes prompt + context to generate response to → User

RAG is valuable for use-cases where the model needs knowledge which is not included in the information the model has learned from. For example, let’s say you are building a GPT to help your support team answer customer inquiries. GPT-4 is able to reason about customer problems using its base knowledge, but it cannot know the latest facts about your specific product or service. You can get much better results by giving a GPT access to your ticketing system, so that it can retrieve past tickets pertaining to similar issues and use that context to generate more relevant answers. When you use the knowledge retrieval feature in a GPT, RAG is being performed for you automatically.

## What is Semantic Search?

**Semantic search** goes beyond keyword search (which relies on the occurrence of specific index words in the search input) to find contextually relevant data based on the conceptual similarity of the input string.

| Data source | Search method |
| --- | --- |
| Document management systems (Google Drive, Sharepoint, etc.) | Keyword search, custom query string |
| Relational databases (Postgres, MySQL, etc.) | SQL query |
| Vector databases | Semantic search query |

As a result, it has been a good choice for providing more context to models like GPT-4 (since queries are likely to be heavily context dependent). Semantic search uses a **vector database**, which stores text chunks (derived from some documents) and their vectors (mathematical representations of the text). When you query a vector database, the search input (in vector form) is compared to all of the stored vectors, and the most similar text chunks are returned.

## Example of semantic search

Let’s say that you are building a customer support chatbot. If you want to populate a vector database with articles from a knowledge base, you might:

1. Break each of the articles up into chunks
   - This could be at the sentence, paragraph, or page level. Different chunking strategies will yield different results.
2. Use the OpenAI Embedding API to process those chunks and return embeddings (i.e. mathematical representations of the nature of the chunk in vector space)
   - For example: \[ -0.006929283495992422,-0.005336422007530928, … -4.547132266452536e-05, -0.024047505110502243\]
3. Store the chunks and their embeddings in the database

When a user asks the chatbot a question, a semantic search is performed:

1. User submits a query like “How can I use the OpenAI API?”
2. Use the OpenAI Embedding API to produce a vector representation of the query string
3. Submit that vector to the search endpoint associated with my vector db
4. Get back one or more text chunks which are similar to my query

The chatbot application then submits the text chunks along with the initial user prompt to the OpenAI Chat Completions API to get a response.

For GPT builders, you can leverage semantic search out of the box by uploading files and enabling knowledge retrieval in your GPT.
