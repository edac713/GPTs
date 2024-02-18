# Models

## Overview

The OpenAI API is powered by a diverse set of models with different capabilities and price points. You can also make customizations to our models for your specific use case with [fine-tuning](/docs/guides/fine-tuning).

ModelDescription

[GPT-4 and GPT-4 Turbo](/docs/models/gpt-4-and-gpt-4-turbo)
A set of models that improve on GPT-3.5 and can understand as well as generate natural language or code

[GPT-3.5 Turbo](/docs/models/gpt-3-5-turbo)
A set of models that improve on GPT-3.5 and can understand as well as generate natural language or code

[DALL·E](/docs/models/dall-e)
A model that can generate and edit images given a natural language prompt

[TTS](/docs/models/tts)
A set of models that can convert text into natural sounding spoken audio

[Whisper](/docs/models/whisper)
A model that can convert audio into text

[Embeddings](/docs/models/embeddings)
A set of models that can convert text into a numerical form

[Moderation](/docs/models/moderation)
A fine-tuned model that can detect whether text may be sensitive or unsafe

[GPT base](/docs/models/gpt-base)
A set of models without instruction following that can understand as well as generate natural language or code

[Deprecated](/docs/deprecations)
A full list of models that have been deprecated along with the suggested replacement

We have also published open source models including [Point-E](https://github.com/openai/point-e), [Whisper](https://github.com/openai/whisper), [Jukebox](https://github.com/openai/jukebox), and [CLIP](https://github.com/openai/CLIP).

## [Continuous model upgrades

](/docs/models/continuous-model-upgrades)

`gpt-3.5-turbo`, `gpt-4`, and `gpt-4-turbo-preview` point to the latest model version. You can verify this by looking at the [response object](/docs/api-reference/chat/object) after sending a request. The response will include the specific model version used (e.g. `gpt-3.5-turbo-0613`).

We also offer static model versions that developers can continue using for at least three months after an updated model has been introduced. With the new cadence of model updates, we are also giving people the ability to contribute evals to help us improve the model for different use cases. If you are interested, check out the [OpenAI Evals](https://github.com/openai/evals) repository.

Learn more about model deprecation on our [deprecation page](/docs/deprecations).

## [GPT-4 and GPT-4 Turbo

](/docs/models/gpt-4-and-gpt-4-turbo)

GPT-4 is a large multimodal model (accepting text or image inputs and outputting text) that can solve difficult problems with greater accuracy than any of our previous models, thanks to its broader general knowledge and advanced reasoning capabilities. GPT-4 is available in the OpenAI API to [paying customers](https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4). Like `gpt-3.5-turbo`, GPT-4 is optimized for chat but works well for traditional completions tasks using the [Chat Completions API](/docs/api-reference/chat). Learn how to use GPT-4 in our [text generation guide](/docs/guides/text-generation).

ModelDescriptionContext windowTraining data

gpt-4-0125-preview

New

**GPT-4 Turbo**  
The latest GPT-4 model intended to reduce cases of “laziness” where the model doesn’t complete a task. Returns a maximum of 4,096 output tokens. [Learn more](https://openai.com/blog/new-embedding-models-and-api-updates).
128,000 tokens
Up to Dec 2023

gpt-4-turbo-preview
Currently points to `gpt-4-0125-preview`.
128,000 tokens
Up to Dec 2023

gpt-4-1106-preview
GPT-4 Turbo model featuring improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. This is a preview model. [Learn more](https://openai.com/blog/new-models-and-developer-products-announced-at-devday).
128,000 tokens
Up to Apr 2023

gpt-4-vision-preview
GPT-4 with the ability to understand images, in addition to all other GPT-4 Turbo capabilities. Returns a maximum of 4,096 output tokens. This is a preview model version. [Learn more](https://openai.com/blog/new-models-and-developer-products-announced-at-devday).
128,000 tokens
Up to Apr 2023

gpt-4
Currently points to `gpt-4-0613`. See [continuous model upgrades](/docs/models/continuous-model-upgrades).
8,192 tokens
Up to Sep 2021

gpt-4-0613
Snapshot of `gpt-4` from June 13th 2023 with improved function calling support.
8,192 tokens
Up to Sep 2021

gpt-4-32k
Currently points to `gpt-4-32k-0613`. See [continuous model upgrades](/docs/models/continuous-model-upgrades). This model was never rolled out widely in favor of GPT-4 Turbo.
32,768 tokens
Up to Sep 2021

gpt-4-32k-0613
Snapshot of `gpt-4-32k` from June 13th 2023 with improved function calling support. This model was never rolled out widely in favor of GPT-4 Turbo.
32,768 tokens
Up to Sep 2021

For many basic tasks, the difference between GPT-4 and GPT-3.5 models is not significant. However, in more complex reasoning situations, GPT-4 is much more capable than any of our previous models.

#### [Multilingual capabilities

](/docs/models/multilingual-capabilities)

GPT-4 [outperforms both previous large language models](https://cdn.openai.com/papers/gpt-4.pdf) and as of 2023, most state-of-the-art systems (which often have benchmark-specific training or hand-engineering). On the MMLU benchmark, an English-language suite of multiple-choice questions covering 57 subjects, GPT-4 not only outperforms existing models by a considerable margin in English, but also demonstrates strong performance in other languages.

## [GPT-3.5 Turbo

](/docs/models/gpt-3-5-turbo)

GPT-3.5 Turbo models can understand and generate natural language or code and have been optimized for chat using the [Chat Completions API](/docs/api-reference/chat) but work well for non-chat tasks as well.

ModelDescriptionContext windowTraining data

gpt-3.5-turbo-0125

New

**Updated GPT 3.5 Turbo**  
The latest GPT-3.5 Turbo model with higher accuracy at responding in requested formats and a fix for a bug which caused a text encoding issue for non-English language function calls. Returns a maximum of 4,096 output tokens. [Learn more](https://openai.com/blog/new-embedding-models-and-api-updates#:~:text=Other%20new%20models%20and%20lower%20pricing).
16,385 tokens
Up to Sep 2021

gpt-3.5-turbo
Currently points to `gpt-3.5-turbo-0613`. The `gpt-3.5-turbo` model alias will be automatically upgraded from `gpt-3.5-turbo-0613` to `gpt-3.5-turbo-0125` on February 16th.
4,096 tokens
Up to Sep 2021

gpt-3.5-turbo-1106
GPT-3.5 Turbo model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. [Learn more](https://openai.com/blog/new-models-and-developer-products-announced-at-devday).
16,385 tokens
Up to Sep 2021

gpt-3.5-turbo-instruct
Similar capabilities as GPT-3 era models. Compatible with legacy Completions endpoint and not Chat Completions.
4,096 tokens
Up to Sep 2021

gpt-3.5-turbo-16k

Legacy

Currently points to `gpt-3.5-turbo-16k-0613`.
16,385 tokens
Up to Sep 2021

gpt-3.5-turbo-0613

Legacy

Snapshot of `gpt-3.5-turbo` from June 13th 2023. Will be [deprecated](/docs/deprecations/2023-10-06-chat-model-updates) on June 13, 2024.
4,096 tokens
Up to Sep 2021

gpt-3.5-turbo-16k-0613

Legacy

Snapshot of `gpt-3.5-16k-turbo` from June 13th 2023. Will be [deprecated](/docs/deprecations/2023-10-06-chat-model-updates) on June 13, 2024.
16,385 tokens
Up to Sep 2021

## [DALL·E

](/docs/models/dall-e)

DALL·E is a AI system that can create realistic images and art from a description in natural language. DALL·E 3 currently supports the ability, given a prompt, to create a new image with a specific size. DALL·E 2 also support the ability to edit an existing image, or create variations of a user provided image.

[DALL·E 3](https://openai.com/dall-e-3) is available through our [Images API](/docs/guides/images/introduction) along with [DALL·E 2](https://openai.com/blog/dall-e-api-now-available-in-public-beta). You can try DALL·E 3 through [ChatGPT Plus](https://chat.openai.com).

ModelDescription

`dall-e-3`

New

**DALL·E 3**  
The latest DALL·E model released in Nov 2023. [Learn more](https://openai.com/blog/new-models-and-developer-products-announced-at-devday).

`dall-e-2`
The previous DALL·E model released in Nov 2022. The 2nd iteration of DALL·E with more realistic, accurate, and 4x greater resolution images than the original model.

## [TTS

](/docs/models/tts)

TTS is an AI model that converts text to natural sounding spoken text. We offer two different model variates, `tts-1` is optimized for real time text to speech use cases and `tts-1-hd` is optimized for quality. These models can be used with the [Speech endpoint in the Audio API](/docs/guides/text-to-speech).

ModelDescription

`tts-1`

New

**Text-to-speech 1**  
The latest text to speech model, optimized for speed.

`tts-1-hd`

New

**Text-to-speech 1 HD**  
The latest text to speech model, optimized for quality.

## [Whisper

](/docs/models/whisper)

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification. The Whisper v2-large model is currently available through our API with the `whisper-1` model name.

Currently, there is no difference between the [open source version of Whisper](https://github.com/openai/whisper) and the version available through our API. However, [through our API](/docs/guides/speech-to-text), we offer an optimized inference process which makes running Whisper through our API much faster than doing it through other means. For more technical details on Whisper, you can [read the paper](https://arxiv.org/abs/2212.04356).

## [Embeddings

](/docs/models/embeddings)

Embeddings are a numerical representation of text that can be used to measure the relatedness between two pieces of text. Embeddings are useful for search, clustering, recommendations, anomaly detection, and classification tasks. You can read more about our latest embedding models in the [announcement blog post](https://openai.com/blog/new-embedding-models-and-api-updates).

ModelDescriptionOutput Dimension

text-embedding-3-large

New

**Embedding V3 large**  
Most capable embedding model for both english and non-english tasks
3,072

text-embedding-3-small

New

**Embedding V3 small**  
Increased performance over 2nd generation ada embedding model
1,536

text-embedding-ada-002
Most capable 2nd generation embedding model, replacing 16 first generation models
1,536

* * *

## [Moderation

](/docs/models/moderation)

The Moderation models are designed to check whether content complies with OpenAI's [usage policies](https://openai.com/policies/usage-policies). The models provide classification capabilities that look for content in the following categories: hate, hate/threatening, self-harm, sexual, sexual/minors, violence, and violence/graphic. You can find out more in our [moderation guide](/docs/guides/moderation/overview).

Moderation models take in an arbitrary sized input that is automatically broken up into chunks of 4,096 tokens. In cases where the input is more than 32,768 tokens, truncation is used which in a rare condition may omit a small number of tokens from the moderation check.

The final results from each request to the moderation endpoint shows the maximum value on a per category basis. For example, if one chunk of 4K tokens had a category score of 0.9901 and the other had a score of 0.1901, the results would show 0.9901 in the API response since it is higher.

ModelDescriptionMax tokens

text-moderation-latest
Currently points to `text-moderation-007`.
32,768

text-moderation-stable
Currently points to `text-moderation-007`.
32,768

text-moderation-007
Most capable moderation model across all categories.
32,768

## [GPT base

](/docs/models/gpt-base)

GPT base models can understand and generate natural language or code but are not trained with instruction following. These models are made to be replacements for our original GPT-3 base models and use the legacy Completions API. Most customers should use GPT-3.5 or GPT-4.

ModelDescriptionMax tokensTraining data

`babbage-002`
Replacement for the GPT-3 `ada` and `babbage` base models.
16,384 tokens
Up to Sep 2021

`davinci-002`
Replacement for the GPT-3 `curie` and `davinci` base models.
16,384 tokens
Up to Sep 2021

## [How we use your data

](/docs/models/how-we-use-your-data)

Your data is your data.

As of March 1, 2023, data sent to the OpenAI API will not be used to train or improve OpenAI models (unless you explicitly [opt in](https://docs.google.com/forms/d/e/1FAIpQLSevgtKyiSWIOj6CV6XWBHl1daPZSOcIWzcUYUXQ1xttjBgDpA/viewform)). One advantage to opting in is that the models may get better at your use case over time.

To help identify abuse, API data may be retained for up to 30 days, after which it will be deleted (unless otherwise required by law). For trusted customers with sensitive applications, zero data retention may be available. With zero data retention, request and response bodies are not persisted to any logging mechanism and exist only in memory in order to serve the request.

Note that this data policy does not apply to OpenAI's non-API consumer services like [ChatGPT](https://chat.openai.com/) or [DALL·E Labs](https://labs.openai.com/).

### [Default usage policies by endpoint

](/docs/models/default-usage-policies-by-endpoint)

EndpointData used for trainingDefault retentionEligible for zero retention

`/v1/chat/completions`*
No
30 days
Yes, except image inputs*

`/v1/files`
No
Until deleted by customer
No

`/v1/assistants`
No
Until deleted by customer
No

`/v1/threads`
No
60 days *
No

`/v1/threads/messages`
No
60 days *
No

`/v1/threads/runs`
No
60 days *
No

`/v1/threads/runs/steps`
No
60 days *
No

`/v1/images/generations`
No
30 days
No

`/v1/images/edits`
No
30 days
No

`/v1/images/variations`
No
30 days
No

`/v1/embeddings`
No
30 days
Yes

`/v1/audio/transcriptions`
No
Zero data retention
-

`/v1/audio/translations`
No
Zero data retention
-

`/v1/audio/speech`
No
30 days
No

`/v1/fine_tuning/jobs`
No
Until deleted by customer
No

`/v1/moderations`
No
Zero data retention
-

`/v1/completions`
No
30 days
Yes

* Image inputs via the `gpt-4-vision-preview` model are not eligible for zero retention.

* For the Assistants API, we are still evaluating the default retention period during the Beta. We expect that the default retention period will be stable after the end of the Beta.

For details, see our [API data usage policies](https://openai.com/policies/api-data-usage-policies). To learn more about zero retention, get in touch with our [sales team](https://openai.com/contact-sales).

## [Model endpoint compatibility

](/docs/models/model-endpoint-compatibility)

EndpointLatest models

/v1/assistants
All models except `gpt-3.5-turbo-0301` supported. The `retrieval` tool requires `gpt-4-turbo-preview` (and subsequent dated model releases) or `gpt-3.5-turbo-1106` (and subsequent versions).

/v1/audio/transcriptions
`whisper-1`

/v1/audio/translations
`whisper-1`

/v1/audio/speech
`tts-1`, `tts-1-hd`

/v1/chat/completions
`gpt-4` and dated model releases, `gpt-4-turbo-preview` and dated model releases, `gpt-4-vision-preview`, `gpt-4-32k` and dated model releases, `gpt-3.5-turbo` and dated model releases, `gpt-3.5-turbo-16k` and dated model releases, fine-tuned versions of `gpt-3.5-turbo`

/v1/completions (Legacy)
`gpt-3.5-turbo-instruct`, `babbage-002`, `davinci-002`

/v1/embeddings
`text-embedding-3-small`, `text-embedding-3-large`, `text-embedding-ada-002`

/v1/fine_tuning/jobs
`gpt-3.5-turbo`, `babbage-002`, `davinci-002`

/v1/moderations
`text-moderation-stable`, `text-moderation-latest`

/v1/images/generations
`dall-e-2`, `dall-e-3`

This list excludes all of our [deprecated models](/docs/deprecations).

Was this page useful?‍‍
