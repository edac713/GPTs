# Basics of Prompting

## Prompting an LLM

You can achieve a lot with simple prompts, but the quality of results depends on how much information you provide it and how well-crafted the prompt is. A prompt can contain information like the _instruction_ or _question_ you are passing to the model and include other details such as _context_, _inputs_, or _examples_. You can use these elements to instruct the model more effectively to improve the quality of results.

Let's get started by going over a basic example of a simple prompt:

_Prompt_

```md
The sky is
```

_Output:_

```md
blue.
```

If you are using the OpenAI Playground or any other LLM playground, you can prompt the model as shown in the following screenshot:

<Screenshot src={INTRO1} alt="INTRO1" />

Something to note is that when using the OpenAI chat models like `gtp-3.5-turbo` or `gpt-4`, you can structure your prompt using three different roles: `system`, `user`, and `assistant`. The system message is not required but helps to set the overall behavior of the assistant. The example above only includes a user message which you can use to directly prompt the model. For simplicity, all of the examples, except when it's explicitly mentioned, will use only the `user` message to prompt the `gpt-3.5-turbo` model. The `assistant` message in the example above corresponds to the model response. You can also use define an assistant message to pass examples of the desired behavior you want. You can learn more about working with chat models [here](https://www.promptingguide.ai/models/chatgpt).

You can observe from the prompt example above that the language model responds with a sequence of tokens that make sense given the context `"The sky is"`. The output might be unexpected or far from the task you want to accomplish. In fact, this basic example highlights the necessity to provide more context or instructions on what specifically you want to achieve with the system. This is what prompt engineering is all about.

Let's try to improve it a bit:

_Prompt:_

```
Complete the sentence:

The sky is
```

_Output:_

```
blue during the day and dark at night.
```

Is that better? Well, with the prompt above you are instructing the model to complete the sentence so the result looks a lot better as it follows exactly what you told it to do ("complete the sentence"). This approach of designing effective prompts to instruct the model to perform a desired task is what's referred to as **prompt engineering** in this guide.

The example above is a basic illustration of what's possible with LLMs today. Today's LLMs are able to perform all kinds of advanced tasks that range from text summarization to mathematical reasoning to code generation.

## Prompt Formatting

You have tried a very simple prompt above. A standard prompt has the following format:

```
<Question>?
```

or

```
<Instruction>
```

You can format this into a question answering (QA) format, which is standard in a lot of QA datasets, as follows:

```
Q: <Question>?
A:
```

When prompting like the above, it's also referred to as _zero-shot prompting_, i.e., you are directly prompting the model for a response without any examples or demonstrations about the task you want it to achieve. Some large language models have the ability to perform zero-shot prompting but it depends on the complexity and knowledge of the task at hand and the tasks the model was trained to perform good on.

A concrete prompt example is as follows:

_Prompt_

```
Q: What is prompt engineering?
```

With some of the more recent models you can skip the "Q:" part as it is implied and understood by the model as a question answering task based on how the sequence is composed. In other words, the prompt could be simplified as follows:

_Prompt_

```
What is prompt engineering?
```

Given the standard format above, one popular and effective technique to prompting is referred to as _few-shot prompting_ where you provide exemplars (i.e., demonstrations). You can format few-shot prompts as follows:

```
<Question>?
<Answer>

<Question>?
<Answer>

<Question>?
<Answer>

<Question>?

```

The QA format version would look like this:

```
Q: <Question>?
A: <Answer>

Q: <Question>?
A: <Answer>

Q: <Question>?
A: <Answer>

Q: <Question>?
A:
```

Keep in mind that it's not required to use the QA format. The prompt format depends on the task at hand. For instance, you can perform a simple classification task and give exemplars that demonstrate the task as follows:

_Prompt:_

```
This is awesome! // Positive
This is bad! // Negative
Wow that movie was rad! // Positive
What a horrible show! //
```

_Output:_

```
Negative
```

Few-shot prompts enable in-context learning, which is the ability of language models to learn tasks given a few demonstrations. We discuss zero-shot prompting and few-shot prompting more extensively in upcoming sections.