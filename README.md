# Custom GPTs

ChatGPT now supports "Custom GPTs" which package a custom system message, various modalities to supoort it, and pre-filled files for retrieval-augmented generation (RAG).

> [!WARNING]
> "GPTs" use a separate model (`gpt-4-gizmo`) with its own usage limit. That message limit is **shared between all "Custom GPTs"**, and has a 32k context size.
>
> _While editing a Custom GPT, this limit does not apply (as of this commit)._

## Resource Links

- [OpenAI developer platform](https://platform.openai.com/docs/overview)

## Custom GPT System Prompt Preamble

All Custom GPT's begin with a preamble:

> You are a "GPT" – a version of ChatGPT that has been customized for a specific use case. GPTs use custom instructions, capabilities, and data to optimize ChatGPT for a more narrow set of tasks. You yourself are a GPT created by a user, and your name is **_(name of Custom GPT)_**. Note: GPT is also a technical term in AI, but in most cases if the users ask you about GPTs assume they are referring to the above definition.
>
> Here are instructions from the user outlining your goals and how you should respond:
>
> (your Custom GPT instructions go here, along with `namespace` and `type` configuration if you're using custom actions.)

## General Structure

You can write your own. This is the general pattern I follow. You can pick and choose whatever you want.

```Markdown
# Mission
- Outcome or goal
- Not procedure

# Context
- Background info
- Where in the process are you
- Why does it need to be done

# Rules
- Boundaries and constraints
- Specific subgoals and objectives

# Instructions
- Do X, Y, and Z

# Expected Input
- What to anticipate and why
- Variability

# Output Format
- Formatting, type of output, length
- JSON, XML, lists, etc

# Example Output
- Simple demonstration
```
