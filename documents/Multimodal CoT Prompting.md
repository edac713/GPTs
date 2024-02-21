# Multimodal CoT Prompting

[Zhang et al. (2023)](https://arxiv.org/abs/2302.00923) recently proposed a multimodal chain-of-thought prompting approach. Traditional CoT focuses on the language modality. In contrast, Multimodal CoT incorporates text and vision into a two-stage framework. The first step involves rationale generation based on multimodal information. This is followed by the second phase, answer inference, which leverages the informative generated rationales.

The multimodal CoT model (1B) outperforms GPT-3.5 on the ScienceQA benchmark.

### *Figure 1.* Example of the Multimodal CoT task:

![MCOT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmultimodal-cot.a84f6cc1.png&w=1080&q=75)
*Image Source: [Zhang et al. (2023)](https://arxiv.org/abs/2302.00923)*

```Markdown
- **Input**
  - **Language**
    - **Question:** Which property do these two objects have in common?
    - **Context:** Select the better answer.
    - **Options:** `(A) soft`, `(B) salty`
  - **Vision:**
    - ![CRACKER](CRACKER.png)
    - ![FRIES](FRIES.png)

- **Output:**
  - **Rationale:** Look at each object. For each object, decide if it has that property. Potato chips have a salty taste. Both objects are salty. A soft object changes shape when you squeeze it. The fries are soft, but the cracker is not. The property that both objects have in common is salty.
  - **Answer:** The answer is `(B) salty`.

---

*Figure 1.* Example of the Multimodal CoT task.
```

Further reading:

- [Language Is Not All You Need: Aligning Perception with Language Models](https://arxiv.org/abs/2302.14045) (Feb 2023)
