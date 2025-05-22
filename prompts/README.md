# Prompts

Prompt templates and example GPT configurations live in this directory. The `gpts` subfolder holds many Markdown files describing individual GPTs, while `prompt_injections` collects examples for testing prompt injection resilience. The `gpt_all_tools.md` file demonstrates a complete system setup with multiple tools.

Browse these files to learn how different prompts are structured or to reuse them when crafting your own GPTs.

Note: Several GPT prompts explicitly instruct that generated code should not contain unfinished `TODO` placeholders. This is unrelated to the "TODO list" example found in the `documents/Getting started - OpenAI API.md` guide, which demonstrates building a task‑tracking GPT. The "NO TODOs" rule only applies to code output by these GPTs.
