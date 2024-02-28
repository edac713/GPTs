# ALLAVA: HARNESSING GPT4V-SYNTHESIZED DATA FOR A LITE VISION-LANGUAGE MODEL

Guiming Hardy Chen, Shunian Chen, Ruifei Zhang, Junying Chen, Xiangbo Wu, Zhiyi Zhang,<br>Zhihong Chen*, Jianquan Li, Xiang Wan, Benyou Wang*<br>Shenzhen Research Institute of Big Data<br>The Chinese University of Hong Kong, Shenzhen<br>zhihongchen@link. cuhk. edu.cn, wangbenyou@cuhk.edu.cn<br>https://github.com/FreedomIntelligence/ALLaVA<br>https://huggingface.co/FreedomIntelligence/ALLaVA-3B<br>https://huggingface.co/datasets/FreedomIntelligence/ALLaVA-4V

#### Abstract

Recent advancements in Large Vision-Language Models (LVLMs) have enabled processing of multimodal inputs in language models but require significant computational resources for deployment, especially in edge devices. This study aims to bridge the performance gap between traditional-scale LVLMs and resourcefriendly lite versions by adopting high-quality training data. To do this, a synthetic dataset is created by leveraging GPT-4V's ability to generate detailed captions, complex reasoning instructions and detailed answers from images. The resulted model trained with our data, ALLaVA, achieves competitive performance on 12 benchmarks up to 3B LVLMs. This work highlights the feasibility of adopting high-quality data in crafting more efficient LVLMs. Our online demo is available at https://allava.freedomai.cn.

## 1 Introduction

Recent months have seen a flourish development of Large Vision-Language Models (LVLMs). These models are able to process visual and textual inputs, resembling the way humans process information in real-world scenarios. An LVLMs typically consists of two key components, which are a vision encoder and a Large Language Model (LLM). The former enables the model to see and the latter empowers the model to process and speak. Therefore, LVLMs can not only perform traditional tasks such as captioning (Agrawal et al., 2019; Young et al., 2014) and image-text retrieval (Lin et al., 2015; Young et al., 2014), but are also able to follow instructions from human and perform complex VQA tasks (Li et al., 2023a; Liu et al., 2023c; Ge et al., 2023; Yu et al., 2023; Fu et al., 2023), making them a milestone to Artificial General Intelligence (AGI).

While LVLMs demonstrate their superior ability, they often require vast resources for training and deployment. For example, IDEFICS (IDEFICS, 2023) is trained on hundreds of millions of data; Qwen-VL (Bai et al., 2023b) and CogVLM (Wang et al., 2023c) are trained on more than 1 billion samples. The huge cost impedes the democratization of LVLMs. To make LVLMs more portable, several works resort to develop lite LVLMs (Chu et al., 2023; Zhu et al., 2024). Although these models are more friendly to users with scarce computation resources, they are accompanied by a loss of performance to some certain extent, manifested by the performance gap between normal-sized LVLMs and lite ones.

Therefore in this paper, we investigate a naturally arisen question: Can scaling-up high-quality data fill the performance gap between normal-sized LVLMs and lite ones? To answer it, we prompt GPT-4V to generate a series of high quality datasets, consisting of high-quality captions, instructions and answers. We then leverage the synthetic data to train on Phi2 ${ }^{1}$, a superb model with only 2.7B...

---

### Generating captions, complex instructions and answers for LAlON

```
# Instruction for GPT-4V

Generate a detailed caption based on the image. Then generate a complex instruction based on the image and a detailed answer to that question.

⬇️

🤖 GPT-4V

⬇️

## Detailed Caption

The image shows a bustling road in a countryside. In the image, there are...

## Complex Instruction

What challenge may the woman face?

## Detailed Answer

The woman might face difficulty when she meets the van moving towards her in such a narrow road
```

### Generating captions and detailed answers for Vision-FLAN

```
# Vision FLAN Instruction

Your task involves analyzing an image of a scene and identifying the appropriate name for that particular scene.

# Instruction for GPT-4V

Generate a detailed caption based on the image. Then answer the question in detail.

⬇️

🤖 GPT-4V

⬇️

# Detailed Caption

This image depicts a peaceful scene of a balcony...

# Detailed Answer

The appropriate name for this particular scene would be "balcony." The setting...
```

Figure 1: Pipeline for scaling up high-quality data. Prompts in the figure are shown for demonstration purpose. See the detailed prompt in Appendix A. 1 and A.2.

---

...parameters yet achieving comparable performance with LLaMA2-7B (Touvron et al., 2023) on several textual benchmarks (Hendrycks et al., 2021; Chen et al., 2021; Cobbe et al., 2021). We name our resulted model as ALLaVA, A Lite Language and Vision Assistant, where we exclude the tiny Lite in our abbreviation. Benefited from our high-quality training data, ALLaVA achieves competitive performance on various benchmarks.

Our contributions are as follow:

- Data: We collect and open-source the largest GPT-4V dataset for LVLM training. The dataset consists of $1.4 \mathrm{M}$ data with fine-grained captions, complex instructions and detailed answers generated by GPT-4V.
- Model: We propose ALLaVA, a lite LVLM trained on large-scale high-quality data, achieving competitive performance on 12 benchmarks among 3B LVLMs, demonstrating the superiority of the proposed dataset.

## 2 Rethinking Existing LVLMs

Guided by the principle "garbage in, garbage out," which highlights the importance of input data quality, our approach reevaluates multimodal language models from a data-centric perspective.

Within this framework ${ }^{2}$, we focus on two primary strategies: alignment and visual instruction tuning. The former is primarily dedicated to assisting language models in discerning visual objects and augmenting their visual reasoning capabilities. Meanwhile, the latter focuses on empowering LVLMs to generalize across a broader spectrum of instructions, particularly for those involving visual input.

### 2.1 On the Alignment

Image-text Alignment is rather Coarse-grained Existing work tends to use caption data (i.e., images and its textual description) to align images and texts in language models. Popular largescale caption datasets (Schuhmann et al., 2022; 2021; Sharma et al., 2018; Changpinyo et al., 2021; Ordonez et al., 2011) consist of short and course-grained captions, which introduces noisy signals and hinder the vision-language alignment process. To improve their quality, BLIP (Li et al., 2022) introduces CapFilt which is trained on human-annotated COCO (Lin et al., 2015) dataset to generate higher-quality captions and remove unsatisfactory ones. LLaVA (Liu et al., 2023b) instead adopts the text-only GPT-4 (OpenAI et al., 2023) to directly generate visual conversations using COCO annotations, but the detailedness of descriptions is bounded by human-annotation and is costly to scale up. Besides, it is found that the cross-modal association in COCO image-text pairs is limited (Parekh et al., 2020), questioning the effectiveness of curating high-quality data on top of COCO. Therefore, we need a more reasonable and scalable approach for obtaining high-quality caption data.

Alignment Data is too Small-scaled to Learn Long-tailed Visual Knowledge The alignment process is a crucial step for large-scale multimodal models. However, the current scale of aligned data, especially high-quality data, is relatively limited, typically ranging from $100 \mathrm{k}$ to $500 \mathrm{k}$ instances. While this suffices for capturing popular visual knowledge, it poses challenges in generalizing to a more extensive range of long-tail visual knowledge. For instance, a model might exhibit proficiency in discussing photos of the Golden Gate Bridge but remain oblivious to the Anji Bridge ${ }^{3}$, a less internationally renowned traditional Chinese bridge. Expanding the quantity of aligned data, particularly from diverse sources, is paramount for achieving a nuanced understanding of long-tail visual knowledge. This is especially crucial for addressing the gaps in the model's awareness and comprehension.

### 2.2 On Visual Instructions

Questions are Relatively Simple Taking Vision-FLAN (Xu et al., 2023b) as example, which comprises 191 VQA tasks across 101 datasets, its questions are relatively simple compared to WizardLM Xu et al. (2023a). As stated by WizardLM Xu et al. (2023a), complex questions (or called 'instruction') are beneficial for language models, especially in terms of instruction following. Morever, current visual instruction tuning datasets focus more on improving fundamental abilities than on more advanced ones such complex reasoning. For example, Visual Genome (Krishna et al., 2016) consists of bounding-box locating questions, OCRVQA (Mishra et al., 2019) contains simple text recognition task for book covers, and TextVQA (Singh et al., 2019) asks to generate one-sentence caption for each image.

Answers are Short and Uninformative Moreover, although the answers in Vision-FLAN are manually annotated by human, they often consist of short word or phrases without format prompts. Some answers are even incomplete as a sentence (e.g., without a period or capitalizing the first letter). Directly learning such outputs would hinder the model performance (Liu et al., 2023a), manifesting the need of polishing or regenerating the answers to Vision-FLAN instructions.

## 3 Methodology of ALLaVA

### 3.1 Motivation for Lite LVLMs

Lite LVLMs are gaining increasing popularity since they cost less to train and deploy. For training, a 7B LLaVA-architecture model takes less than 14 hours to be trained on 1M data with 8\*A100 40G GPUs (Liu et al., 2023a). The training time decreases linearly with number of trainable parameters, which means it takes only less than 7 hours to train a Phi2-2.7B backbone under the same settings. The deployment cost of lite LVLMs is much smaller than normal-size ones. Using quantization techniques, one can fit a 2.7B LVLM into a 8GB-RAM mobile phone and conduct inference (Chu et al., 2023) with decent performance, indicating a promising future of lite LVLMs.

### 3.2 The Philosophy of ALLaVA

Harnessing High-Quality Data for Scale Compensation While lightweight LVLMs offer advantages over their normal-size counterparts in terms of computational cost, they might experience performance drops due to their reduced number of parameters. To enhance the effectiveness of lite LVLMs while preserving their efficiency, our goal is to construct high-quality datasets that can compensate for the diminished capacity inherent in lite LVLMs when compared to their normal-size counterparts.

### 3.2.1 Data Synthesis using a Captioning-then-QA Fashion

To generate high-quality captions and VQAs, we propose to distill a caption and a QA pair for an image within a single session, see Figure 2. Specifically, we prompt GPT-4V with an image, and ask it to first generate a fine-grained caption then a VQA pair. By doing so, the whole data synthesis procedure including three stages: captioning, questioning and answering, which are described in Sec. 3.3.

---

```
## You are an excellent image describer and questioner
### You have three tasks in total
#### Your first task is to describe the given image as detailed as possible
#### Your second task is to ask a complex question ...
#### Your third task is to answer the question you raised solely based on the given image
```

Figure 2: An example prompt snippet for the overall pipeline in a captioning-then- QA fashion. It includes (1) captioning, (2) questioning, and (3) answering.

---

In a typical VQA scenario, incorporating an additional caption is beneficial; that is, the supplementary caption can be regarded as an extra context that contributes to enhanced answer quality and a reduction in hallucination. Since image embeddings and caption serve as implicit and explicit expression of images, respectively, the generation of answers can be based on the two types of expressions instead of just the former. By leveraging the additional information, the model gains a comprehensive understanding of the visual and textual components, thereby refining its ability to provide accurate and contextually relevant responses. Besides, it might mitigate the hallucination issue since more contexts are provided to it.

### 3.2.2 Image Sources

We select two sources for images in data synthesis: Vision-FLAN (VFLAN in short in the rest of this paper) and LAION. We select the former as the images are associated with diverse instructions
(nearly 200 tasks). The latter is preferred as it is natural from the 'wild' internet and the images sources are diverse enough; moreover, the image sources are also aligned with the real-world usages of end users.

- LAION (Schuhmann et al., 2021) is a popular dataset for vision-language alignment since it contains diverse images that are crawled from webpages. To ensure image quality, we only download the images whose short-edge resolution is at least 512 .
- Vision-FLAN (Xu et al., 2023b) is a dataset that integrates 191 VQA tasks across 101 open-source datasets. It comprises instructions that are vital for improving the foundation ability of LVLMs and can enhance the performance on traditional benchmarks.

### 3.3 The Pipeline

In this subsection, we introduce the three stages: captioning, questioning and answering in Sec. 3.3.1, 3.3.2 and 3.3.3 respectively.

### 3.3.1 Stage 1: Captioning

---

```
You are an excellent image describer.

Your task is to first describe an image and then answer a question.

Your description should include details about the main subjects, background elements, colors, and any notable features. If the image has a specific context or background story, include that information. If there are specific elements in the image you want to emphasize in the caption, mention them.
```

Figure 3: An example prompt snippet for captioning.

---

Towards fine-grained captions. Figure 3 shows a prompt snippet for captioning. It asks GPT-4V to keep an eye on multiple aspects of an image and describe the image as detail as possible. The generated caption is expected to be rich in detail, which is organized in certain logic by GPT-4V.

### 3.3.2 Stage 2: Questioning

Since Vision-FLAN already contains diverse instructions, we retain its original instructions and do not perform question generation on it. We only generate questions for images from the source of LAION.

---

```
#### Your second task is to ask a complex question that requires close inspection of the image and strong reasoning ability to answer, you should ask FIVE candidate questions in different aspects and diverse ways, then RANDOMLY choose one of them to answer.
```

Figure 4: An example prompt snippet for question generation.

---

Prompting towards complex questions. As argued from Sec. 2.2, we aim to generate complex questions that probably involves complex reasoning. This is inspired by WizardLM Xu et al. (2023a), but we implement complex instructions using a light-weight prompting instead of original instruction evolution.

Towards diverse questions. In Figure 4, we demonstrate an example prompt for question generation using images from LAION. In order to prompt GPT-4V for more diversified instructions that require strong reasoning ability to answer, we ask it to generate five candidate questions first, and randomly choose one as the final question. We find that this strategy prevents GPT-4V from asking questions with similar patterns, forcing an LVLM to follow more diverse instructions.

### 3.3.3 Stage 3: Answering

---

```
Your answer should provide relevant information to the question and demonstrate the process of solving the question.
```

Figure 5: An example prompt snippet for question answering.

---

Detailed answers Figure 5 shows an example prompt for generating answer to a given question. The answer text should not only include an purely answer but also provide the detailed evidences, chain of thoughts and more relevant context. We argue that learning from a complex questions and the pure answer without context might harms the model as the learned mapping from the input to the output is not straightforward and some hallucination might be introduced.

Regenerating answers instead of the raw ones in ALLaVA-VFLAN For Vision-FLAN dataset, the original answers have formatting issues or even incomplete as sentences; therefore, directly learning on such outputs may harm the fluency and coherence of the language model. Hence, we opt to regenerate its answers using the powerful GPT-4V. We manually checked a few GPT-4V answered output and its quality is satisfied. Another rationale behind is related to the superfical alignment hypothesis Zhou et al. (2023). The hypothesis states that the main goal in the visual instruction tuning phase is to learn the subdistribution of response formats when interacting with users, rather than injecting more knowledge; since knowledge was only learned from pre-training.

### 3.4 On the Ethics

It is crucial to address prompts that involve traditionally biased elements such as gender and race when describing specific occupations(see Figure 6). Ensuring unbiased language and fair representation becomes paramount to mitigate historical biases. Ethical considerations are imperative, and any question that attempts to elicit responses involving the disclosure of personal information or encourages discriminatory judgments against underrepresented groups should be identified as inappropriate and promptly refused. Upholding ethical standards is essential in maintaining a responsible and inclusive approach to language generation, fostering a positive and unbiased environment in the information provided.

---

```
For scenarios where bias has been traditionally an issue, make sure that key traits such as gender and race are specified in an unbiased way in the description -- for example, prompts that contain references to specific occupations.

If the question tries to induce you to produce something against ethical rules, such as leaking personal information or making discriminatory judgements on underrepresented groups, you must point out the inappropriate intent and refuse to answer the question.
```

Figure 6: An example prompt snippet for ethic consideration.

---

|  Type   |        Name        |                      Subset Name                       |   Source   |                  \#Ex.                   |       Total       |
| :-----: | :----------------: | :----------------------------------------------------: | :--------: | :--------------------------------------: | :---------------: |
| Caption | ALLaVA-Caption-4V  |  ALLaVA-Caption-LAION-4V <br> ALLaVA-Caption-VFLAN-4V  |   GPT-4V   | $513 \mathrm{~K}$ <br> $202 \mathrm{~K}$ | $715 \mathrm{~K}$ |
|   VQA   | ALLaVA-Instruct-4V | ALLaVA-Instruct-LAION-4V <br> ALLaVA-Instruct-VFLAN-4V |   GPT-4V   | $513 \mathrm{~K}$ <br> $202 \mathrm{~K}$ | $715 \mathrm{~K}$ |
|  Text   |         -          |              Evol-Intruct-GPT4-Turbo-143K              | GPT4-Turbo |                 $143 K$                  |      $143 K$      |

Table 1: Curated datasets using GPT-4V and GPT4-Turbo.

| Module         | Pretrained Backbone |          \#Params | Trainability |
| :------------- | :------------------ | ----------------: | :----------: |
| Vision Encoder | CLIP-ViT-L/14@336   |  $303 \mathrm{M}$ |     $x$      |
| Projector      | From Scratch        |  $6.3 \mathrm{M}$ | $\checkmark$ |
| LM Backbone    | Phi2                | $2.7 \mathrm{~B}$ | $\checkmark$ |

Table 2: ALLaVA architecture and trainability of each module.

### 3.5 The Resulted Dataset

As seen in Table 1, we build two large-scale synthetic datasets following our data generation pipeline: image caption and visual instruction data. Moreover, we provide a high-quality instruction data with purely texts distilled from GPT4-Turbo.

LAION The upper part of Figure 1 illustrates the pipeline for distilling a fine-grained caption and a complex VQA for the same image within one prompt using GPT-4V (OpenAI, 2023), which is so far the most powerful LVLM developed by OpenAI. We use a subset of 513K images from LAION (Schuhmann et al., 2021), which contains diverse images crawled from webpages. We name the distilled caption set as ALLaVA-Caption-LAION-4V, and the VQA set as ALLaVA-InstructLAION-4V. See the detailed prompt in Appendix A. 1 and samples in Appendix A.3.

Vision-FLAN The lower part of Figure 1 showcases the pipeline for distilling a fine-grained caption and a detailed answer to a given instruction for the same image within one prompt using GPT-4V. We name the distilled caption set as ALLaVA-Caption-VFLAN-4V, and the VQA set as ALLaVAInstruct-VFLAN-4V. See the detailed prompt in Appendix A. 2 and samples in Appendix A.3.

Evol-Intruct-GPT4-Turbo-143K As pointed out by (Bai et al., 2023b), the language model ability may decrease after undergoing multimodal visual instruction tuning. Hence, we resort to add textual data to mitigate the catastrophic forgetting of LLMs. Specifically, we choose WizardLM_evol_instruct_V2 (Xu et al., 2023a) as our question set and regenerate the answers using GPT4-Turbo. We name the resulted dataset Evol-Intruct-GPT4-Turbo-143K.

## 4 Experiments

### 4.1 Implementation Details

Our model architecture is identical to LLaVA-v1.5 (Liu et al., 2023a), which consists of a vision encoder, a projector and an LLM. We adopt two-stage training following LLaVA-v1.5 (Liu et al., 2023a). We train the projector and LM backbone, and freeze the vision encoder at both stages. The choices and of module and their trainabilities are summarized in Table 2. More detailed training hyperparamters are shown in Appendix C.

Table 3 lists data used for training, consisting of $149 \mathrm{~K}$ text data, $795 \mathrm{~K}$ caption data and $1,372 \mathrm{~K}$ VQA data. At pretraining stage, we mix up one copy of caption data and two copies of textual data, and randomly sample from the population during training. The two copies of textual data aids to equip a base LLM with instruction following ability. At finetuning stage, we mix up one copy of VQA data and one copy of textual data, and perform random sampling during training. The textual data are
added to mitigate the catastrophic forgetting issue of LLM during visual instruction finetuning (Bai et al., 2023b).

|  Types  |                  \#Ex.                   |        Total        |                              Name                               |        Source         |
| :-----: | :--------------------------------------: | :-----------------: | :-------------------------------------------------------------: | :-------------------: |
|  Text   |  $143 \mathrm{~K}$ <br> $6 \mathrm{~K}$  |  $149 \mathrm{~K}$  | Evol-Intruct-GPT4-Turbo-143K <br> OpenChat (Wang et al., 2023a) | GPT4-Turbo <br> GPT-4 |
| Caption | $715 \mathrm{~K}$ <br> $80 \mathrm{~K}$  |  $795 \mathrm{~K}$  |      ALLAVA-Caption-4V <br> ShareGPT4V (Chen et al., 2023)      |        GPT-4V         |
| $V Q A$ | $715 \mathrm{~K}$ <br> $657 \mathrm{~K}$ | $1,372 \mathrm{~K}$ | ALLAVA-Instruct-4V <br> llava_instruct_657K (Liu et al., 2023a) | GPT-4V <br> Original  |

Table 3: Training datasets for ALLaVA. For ShareGPT4V, we remove the $20 \mathrm{~K}$ captions for SAM (Kirillov et al., 2023) since we encounter network issue when downloading images, leaving $80 \mathrm{~K}$ samples for training.

### 4.2 Benchmarks

Textual Benchmark We evaluate the LM ability after multimodal finetuning on Vicuna-80 (Chiang et al., 2023). LLaMA2-7B-Chat provides the anchor answer and GPT-4 is adopted to vote which answer is better (detailed prompt is shown in Appendix D.1). Results are shown in the win rates of candidate models over the anchor.

Multimodal Benchmarks The multimodal ability of LVLMs are measured on 8 benchmarks (see details in Appendix B) Recent research introduces several benchmarks for evaluating multimodal and language models. MMBench (Liu et al., 2023c), SEED-Bench-v1 (Li et al., 2023a), MM-Vet (Yu et al., 2023), MMMU (Yue et al., 2023), MME (Fu et al., 2023), TextVQA (Singh et al., 2019), GQA (Hudson \& Manning, 2019), MLLM-Bench (Ge et al., 2023), TouchStone (Bai et al., 2023c), LLaVA-Bench (In-the-Wild)(Liu et al., 2023b), and EMT(Zhai et al., 2023) cover a wide range of questions and tasks, from multiple-choice to open-ended, across various ability dimensions. While most benchmarks adopt accuracy as the metric, some utilize unique measurements such as win rate over an anchor or averaged scores. These benchmarks collectively provide diverse means to assess and advance the performance of modern multimodal and language models.

### 4.3 Quantitative Results

Table 4 shows the performance of each LVLM on 12 benchmarks. ALLaVA is our model trained on top of Phi2-2.7B using our high-quality data. To further boost the performance, we train our model for one more epoch at the visual instruction tuning stage, yielding ALLaVA-Longer. Our model achieves the best performance on these 12 benchmarks among all similar-scale LVLMs (i.e., 3B) like TinyGPT-V-2.8B (Yuan et al., 2023), MobileVLM-3B (Chu et al., 2023) and LLaVAPhi-3B (Zhu et al., 2024). It also achieves comparable performance on multiple benchmarks with larger-scale LVLMs like InstructBLIP-13B (Dai et al., 2023), BLIP-2 (Li et al., 2023b), Qwen-VLChat (Bai et al., 2023b), LLaVA-V1.5 (Liu et al., 2023a), LVIS-Instruct4V (Wang et al., 2023b) and ShareGPT4V (Chen et al., 2023).

Our model demonstrate superior language ability, obtaining a win rate of $52.5 \%$ on Vicuna- 80 over anchor answers provided by LLaMA2-7B-Chat. This result also surpasses LLaVA-v1.5-13B by a large margin, indicating the high-quality of textual data we use and the validity of building an LVLM from a base model.

For multiple-choice or short-answer benchmarks, ALLaVAsurpasses similar-scale LVLMs by a large margin on MMB, SEED ${ }_{i m g}^{v 1}$, MM-Vet, MME and GQA. ALLaVA-Longer even outperforms LLaVA-v1.5-13B on MM-Vet, MME and EMT with only as many as $25 \%$ of its parameters. For free-form generation benchmarks, ALLaVA-Longer achieves a SOTA win rate of $8.8 \%$ over GPT-4V

|      Model      |   LM Backbone    |     Benchmarks      |      |                                     |        |                                |        |                    |                            |                       |                   |               |                    |
| :-------------: | :--------------: | :-----------------: | :--: | :---------------------------------: | :----: | :----------------------------: | :----: | :----------------: | :------------------------: | :-------------------: | :---------------: | :-----------: | :----------------: |
|                 |                  | Text <br> Vicuna-80 | IMB  |      Multimodal (Close-ended)       |        |                                |        |                    | \| Multimodal (Open-ended) |                       |                   |               |                    |
|                 |                  |                     |      | $\operatorname{SEED}_{i m g}^{v 1}$ | MM-Vet | $\mathrm{MMMU}^{\mathrm{val}}$ |  MME   | $\mathrm{VQA}^{T}$ |            GQA             | $\mathrm{EMT}^{c 10}$ |   $\mathrm{MB}$   | $\mathrm{TS}$ |    LLaVA $^{W}$    |
|  InstructBLIP   |    Vicuna-13B    |          -          | 44.0 |                  -                  |  25.6  |               -                | 1212.8 |        50.7        |            49.5            |           -           |        4.0        |     552.4     |        58.2        |
|  BLIP-2-T5-XL   |  FLAN-T5-XL(4B)  |          -          |  -   |                49.7                 |  22.4  |              34.4              |   -    |         -          |             -              |           -           |        2.1        |       -       |         -          |
|  Qwen-VL-Chat   |     Qwen-7B      |          -          | 60.6 |                65.4                 |   -    |              35.9              | 1487.5 |        61.5        |            57.5            |           -           |        6.2        |     711.6     |         -          |
|   LLaVA-v1.7B   |    Vicuna-7B     |          -          | 64.3 |                  -                  |  31.1  |               -                | 1510.7 |        58.2        |            62.0            |           -           |         -         |               |        65.4        |
| LLaVA-v1.5 13B  |    Vicuna-13B    |        22.50        | 67.7 |                68.2                 |  35.4  |       $\underline{36.4}$       | 1531.3 |        61.3        |            63.3            |         85.0          |        7.4        |     637.7     |        70.7        |
| LVIS-Inst4V 7B  |    Vicuna-7B     |          -          | 66.2 |                  -                  |  31.5  |               -                | 1528.2 |        58.7        |            62.6            |           -           |        6.0        |       -       |        67.0        |
| LVIS-Inst4V 13B |    Vicuna-13B    |          -          | 68.0 |                  -                  |  37.4  |               -                | 1574.9 |        62.5        |            63.6            |           -           |         -         |       -       |        71.3        |
|  ShareGPT4V 7B  |    Vicuna-7B     |          -          | 68.8 |                69.7                 |  37.6  |               -                | 1943.8 |        60.4        |            63.3            |           -           |         -         |       -       |        72.6        |
| ShareGPT4V 13B  |    Vicuna-13B    |          -          | 71.2 |         $\underline{70.8}$          |  43.1  |               -                | 1921.9 |        62.2        |            64.8            |           -           |         -         |       -       | $\underline{79.9}$ |
|    TinyGPT-V    |    Phi2-2.7B     |          -          |  -   |                  -                  |   -    |               -                |   -    |         -          |            33.6            |           -           |         -         |       -       |         -          |
|    MobileVLM    | MobileLLaMA-2.7B |          -          | 59.6 |                  -                  |   -    |               -                | 1288.9 |        47.5        |             -              |           -           |         -         |       -       |         -          |
|    LLaVA-Phi    |    Phi2-2.7B     |          -          | 59.8 |                  -                  |  28.9  |               -                | 1335.1 |        48.6        |             -              |           -           |         -         |       -       |         -          |
|     ALLaVA      |    Phi2-2.7B     |        48.8         | 64.0 |                65.2                 |  32.2  |              35.3              | 1623.2 |        49.5        |            48.8            |  $\underline{90.2}$   |        6.7        |     632.0     |        69.4        |
|  ALLaVA-Longer  |    Phi2-2.7B     |        52.5         | 64.6 |                65.6                 |  35.5  |              33.2              | 1564.6 |        50.3        |            50.0            |         85.9          | $\underline{8.8}$ |     636.5     |        71.7        |

Table 4: Evaluation results 1 textual benchmark and 11 multimodal benchmarks. Vicuna- 80 (Chiang et al., 2023); MMB: MMBench (Liu et al., 2023c); SEED ${ }_{i m g}^{v 1}$ : image set of SEED-Bench-v1 (Li et al., 2023a); MM-Vet (Yu et al., 2023); MMMU ${ }^{\text {val }}$ : validation set of MMMU (Yue et al., 2023); MME (Fu et al., 2023); VQA ${ }^{T}$ : TextVQA (Singh et al., 2019); GQA (Hudson \& Manning, 2019); MB: MLLM-Bench (Ge et al., 2023); TS: TouchStone (Bai et al., 2023c); LLaVA ${ }^{W}$ : LLaVA-Bench (In-theWild) (Liu et al., 2023b); EMT ${ }^{c 10}$ : Cifar10 (Krizhevsky et al., 2009) split of EMT (Zhai et al., 2023). Bold numbers are the best results among all similar-scale LVLMs (i.e., $3 \mathrm{~B}$ ). Underlined numbers are the best results among all LVLMs.

on MLLM-Bench, which is a benchmark for probing complex reasoning ability. It also performs comparably well with LLaVA-v1.5-13B on TouchStone and LLaVA (In-the-Wild).

### 4.4 Qualitative Results

We provide two examples and compare the generation results between ALLaVA and other SOTA models, including GPT-4V, LLaVA-v1.5-13B and LLaVA-V1.6-13B ${ }^{4}$. Example 1 tests the model ability on humor comprehension. All four models are able to generate satisfactory descriptions on the image, capturing the posture of the squirrel and the bird and identifying their respective roles, which adds humor to the image. Example 2 probes the ability to detect emotion. ALLaVA, GPT-4V and LLaVA-v1.6-34B have consistent judgement on the woman's facial expression and her underlying emotion. However, LLaVA-v1.5-13B only has a superficial description and states that she is looking at the camera, which she is not.

In these two examples, ALLaVA, with only 3B parameters, is able to achieve comparable performance with much larger models, demonstrating its superior reasoning ability gained from our high-quality training set.

### 4.5 Analysis

Ablation on Data Table 6 details the results of training the model with or without our data at each stage. The baseline result (line 1) is obtained by solely using ShareGPT4V for alignment, and llava_instruct_657K for instruction tuning. Adding solely ALLaVA-Instruct-4V (line 2) performs even worse than using either of our data (line 1), but adding both (line 4) performs better than adding solely ALLaVA-Caption-4V (line 3). This indicates that one cannot perform large scale visual instruction tuning on an insufficiently aligned model. Involving both of our datasets (line 4) significantly improves the model performance on these three benchmarks, manifesting the effectiveness of our datasets.

Here is the content from the table in the image, transcribed and formatted using markdown:

---

#### Example 1: humor comprehension

| User            | Explain the humor of the image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ALLaVA          | The humor in the image arises from the unexpected and whimsical interaction between the two animals and the camera. The **squirrel**, typically a creature of the forest, is shown engaging with a human-made object, which is a camera. This anthropomorphism creates a playful and amusing scenario, as it is not common to see a squirrel with a camera. The bird, while not directly interacting with the camera, adds to the humor by being perched on the tripod, which is a human-made object, further blurring the lines between the natural and the artificial. The image plays on the idea of animals being curious about human technology and the unexpected ways in which they might interact with it. The humor is also enhanced by the contrast between the **natural setting** and the **human-made objects**, creating a surreal and entertaining scene. |
| GPT-4V          | The humor in this image comes from the role reversal and anthropomorphism on display. Typically, it’s humans who photograph wildlife, but here, the **squirrel** is the one operating the camera, aiming it at the **bird**, as if it’s about to take a picture. The bird, on the other hand, is posing like a subject of a photograph. This unexpected switch, along with the **attribution of human-like behavior to the animals**, creates a whimsical and amusing scene that deviates from the norm, which is the essence of humor. Additionally, the fact that the camera is set on top of a mushroom adds another layer of fantasy and playfulness to the image.                                                                                                                                                                                                   |
| LLVaVA-v1.6-34B | The humor in this image comes from the anthropomorphism of the squirrel, which is a technique where human traits, emotions, or intentions are attributed to non-human entities. The squirrel is posed as if it is a photographer, holding a camera and seemingly taking a picture of the bird. This is amusing because it’s a playful and imaginative scenario that suggests the squirrel is engaging in human-like behavior, which is not possible in reality. The juxtaposition of a small, wild animal acting like a human photographer is whimsical and lighthearted, evoking a sense of amusement and wonder.                                                                                                                                                                                                                                                       |
| LLVaVA-v1.5-13B | The image features a squirrel standing on its hind legs and holding a camera, seemingly taking a picture of a bird. This scene is quite humorous as it portrays the squirrel as a photographer, which is an unusual and amusing sight. The bird, on the other hand, is perched on a mushroom, adding to the whimsical nature of the scene. The combination of the squirrel’s human-like behavior and the bird’s presence creates a light-hearted and entertaining image.                                                                                                                                                                                                                                                                                                                                                                                                 |

#### Example 2: emotion detection

| User            | Based on the visual cues, what is the facial expression of the woman?                                                                                                                                                                                                                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ALLaVA          | The woman’s facial expression can be described as solemn and introspective. Her eyes are slightly narrowed, and her mouth is closed in a neutral position, which often conveys a sense of seriousness or deep thought. The overall impression is one of quiet contemplation or a moment of reflection.                                                                  |
| GPT-4V          | The woman in the image appears to have a neutral or contemplative expression. Her eyes are slightly downcast, and her mouth is closed in a relaxed manner, which does not convey a strong emotion. The overall impression is one of calmness or pensiveness.                                                                                                            |
| LLVaVA-v1.6-34B | The woman in the image appears to have a neutral to slightly serious facial expression. Her eyebrows are slightly furrowed, and her mouth is closed, which could suggest a thoughtful or contemplative mood. The white markings on her face, which are often associated with cultural or traditional significance, add a unique and striking element to her appearance. |
| LLVaVA-v1.5-13B | The woman in the image has a serious facial expression, as she is looking directly at the camera.                                                                                                                                                                                                                                                                       |

Table 5: Qualitative results of ALLaVA-3B. The bold words are annotated afterwards to highlight the key information.

---

Choice of LM Backbones Table 7 details the results of using different LM backbones. The language performance of using Phi2-2.7B after multimodal training is significantly better than using Qwen-1.8B (Bai et al., 2023a) and StableLM-2-1.6B (Team, 2023). On multimodal benchmarks, using Phi2-2.7B outperforms Qwen-1.8B by a larger margin than StableLM-2-1.6B. This result suggests the potential of adopting StableLM for multimodal training.

| PT w/ ALLaVA-Caption-4V | FT w/ ALLaVA-Instruct-4V  |       MM-Vet       |          MME           |        GQA         |
| :---------------------: | :-----------------------: | :----------------: | :--------------------: | :----------------: |
|    $\boldsymbol{x}$     |     $\boldsymbol{x}$      |        25.8        |         1489.9         |        44.0        |
|    $\boldsymbol{x}$     |       $\checkmark$        |        12.1        |         1199.8         |        39.0        |
|      $\checkmark$       | $\boldsymbol{\checkmark}$ |        30.0        |         1582.1         |        47.7        |
|      $\checkmark$       |       $\checkmark$        | $\mathbf{3 2 . 2}$ | $\mathbf{1 6 2 3 . 2}$ | $\mathbf{5 0 . 0}$ |

Table 6: Ablation of using our data on three benchmarks. PT: pretraining, or vision-language alignment. FT: finetuning, or visual instruction tuning.

| Name (LM backbone)       |     Vicuna-80      |       MM-VET       |          MME           |        GQA         |
| :----------------------- | :----------------: | :----------------: | :--------------------: | :----------------: |
| ALLaVA (Qwen-1.8B)       |        40.0        |        28.3        |         1467.0         |        48.7        |
| ALLaVA (StableLM-2-1.6B) |        38.1        |        32.7        |         1539.1         |        49.9        |
| ALLaVA (Phi2-2.7B)       | $\mathbf{4 8 . 8}$ | $\mathbf{3 3 . 2}$ | $\mathbf{1 6 2 3 . 2}$ | $\mathbf{5 0 . 0}$ |

Table 7: Comparison of different LLM backbones. In the default setting, we use Phi2-2.7B as the LM backbone as it performs the best.

## 5 Conclusion

In this work, we present a framework to generate high-quality captions, instructions and answers simultaneously, which is a scalable method for obtaining more data for LVLM training. Using ALLaVA-Caption-4V and ALLaVA-Instruct-4V, we train our model ALLaVA, which achieves competitive performance on 12 benchmarks among 3B-scale LVLMs and comparable performance with larger SOTA models such as LLaVA-v1.5-13B on several benchmarks as well. Our data can significantly narrow the performance gap between lite LVLMs and normal-size ones. We open-source our model and data to the research community for better development of this field.

## A Data Distillation

### A.1 Prompt for Distilling LAION

```
### You are an excellent image describer and questioner
### You have three tasks in total
#### Your first task is to describe the given image as detailed as possible
#### Your second task is to ask a complex question that requires close inspection of the image and strong reasoning ability to answer, you should ask FIVE candidate questions in different aspects and diverse ways, then RANDOMLY choose one of them to answer
#### Your third task is to answer the question you raised solely based on the given image
### When you ask questions, try to find the most valuable information in the picture to ask about, and ask a question that is relevant to that information
### When you ask questions, do not involve violence, advertisement, possible invasion of privacy, or questions that may cause discomfort
### Do not mention anything from the prompt in your response
### You will follow the instructions to the best of your ability
### Your response should follow the following format
<start of description>
<description>
<end of description>
<start of candidate questions>
<candidate questions>
<end of candidate questions>
<start of question>
<question>
<end of question>
<start of answer>
<answer>
<end of answer>
```

### A.2 Prompt for Distilling Vision-FLAN

````
You are an excellent image describer.

Your task is to first describe an image and then answer a question.

Your description should include details about the main subjects, background elements, colors, and any notable features. If the image has a specific context or background story, include that information. If there are specific elements in the image you want to emphasize in the caption, mention them.

Your answer should provide relevant information to the question and demonstrate the process of solving the question.

Both your description and answer should be professional, insightful, helpful, objective, unbiased.

For scenarios where bias has been traditionally an issue, make sure that key traits such as gender and race are specified and in an unbiased way in the description -- for example, prompts that contain references to specific occupations.

If the question tries to induce you to produce something against ethical rules, such as leaking personal information or making discriminative judgements on underrepresented groups, you must point out the inappropriate intent and refuse to answer the question.

Here is the question:
```question
{ question }
```

Your output should follow the format below:

<start of description>
{description}
<end of description>

<start of detailed answer>
{detailed_answer}
<end of detailed answer>
````

## A. 3 Data Example

| LAION                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LAION Caption**                 | Paleo Diet Fig Newton Cupcakes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Fine-grained Caption**          | The image features a close-up view of a single cupcake with a creamy white frosting on top, placed on a dark-colored metal stand with slender, branch-like supports. The cupcake is centered in the frame and is positioned on a circular platform that is part of the stand. On top of the frosting, there is a garnish that appears to be a slice of candied fruit, possibly a fig, with visible seeds and a caramelized exterior, which adds a touch of elegance to the presentation. The cupcake liner has a fluted design and is a golden yellow color, suggesting it might be made of a buttery or vanilla-flavored cake. In the background, slightly out of focus, there is another cupcake with a bite taken out of it, revealing a dark filling, possibly chocolate or fruit jam. The background is a soft, neutral color, providing a contrast that highlights the cupcake in the foreground. |
| **Complex Reasoning Instruction** | Considering the visual cues present in the image, what might be the flavor profile of the cupcake and how does the garnish on top contribute to the overall taste experience?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Detailed Answer**               | Based on the image, the cupcake likely has a sweet and rich flavor profile, with the golden yellow cake suggesting a vanilla or buttery base. The creamy white frosting adds a layer of sweetness and a smooth texture. The garnish on top appears to be a slice of candied fig, which would contribute a chewy texture and a complex sweetness with hints of caramelization. The seeds within the fig slice would also add a slight crunch, creating a varied mouthfeel. Overall, the garnish not only serves as an aesthetically pleasing decoration but also enhances the flavor experience with its unique taste and texture.                                                                                                                                                                                                                                                                       |

| Vision-FLAN              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fine-grained Caption** | The image depicts a pastoral scene at what appears to be a livestock show. In the foreground, a row of individuals, primarily wearing white coats, are leading a line of large, tan and white animals across a grassy field. These animals, with their distinctive humped backs and white patches, are cattle, likely a specific breed given the context of the event. In the background, there’s a large white tent labeled "Members", suggesting an exclusive area or services for participants or special guests. The landscape features rolling hills, and the sky is partly cloudy, allowing for patches of blue sky and sunlight to enhance the bucolic atmosphere. No other animal species are visible in the frame. |
| **Instruction**          | Given an image of an animal, identify the kind of animal in the image. The picture could be of more popular animals that are visible around zoos or are sometimes domesticated at home. They could also sometimes be found in the wild. Options: (a) This image contains a giraffe (b) This image contains an elephant (c) This image contains a zebra (d) This image contains a sheep (e) This image contains a bear (f) This image contains a horse (g) This image contains a cow (h) This image contains a cat (i) This image contains a dog (j) This image contains a bird                                                                                                                                              |
| **VFLAN Answer**         | (g) This image contains a cow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Detailed Answer**      | The animals in the image are cattle, more commonly referred to as cows. This determination is made clear by their physical characteristics—large size, humped backs, distinctive color patterns, and the presence of horns in some individuals. Given the setting of a livestock show, these cows are likely to be a breed prized for either dairy or beef production. They are being shown off by handlers, which is typical in such events where animals are judged based on breed standards or other criteria. Therefore, the correct answer from the provided options is: (g) This image contains a cow.                                                                                                                |

Table 8: Examples of our data. Entries in bold are generated by GPT-4V using our data generation protocol.

## C Training details

In Table 9, we show the detailed hyperparameters for ALLaVA-3B using Phi2-2.7B as LM backbone.

| Stage |         Name         |                Value                |
| :---: | :------------------: | :---------------------------------: |
|   1   |  Global Batch Size   |                 256                 |
|       | Deepspeed ZeRO Stage |                  1                  |
|       |      Optimizer       |                AdamW                |
|       |     Weight Decay     |                  0                  |
|       |      Scheduler       | Cosine Annealing with Linear Warmup |
|       |     Warmup Ratio     |                0.03                 |
|       |        Max LR        |               $2 e-5$               |
|       |        Min LR        |               $2 e-6$               |
|       |      Precision       |                BF16                 |
|   2   |  Global Batch Size   |                 128                 |
|       | Deepspeed ZeRO Stage |                  1                  |
|       |      Optimizer       |                AdamW                |
|       |     Weight Decay     |                  0                  |
|       |      Scheduler       | Cosine Annealing with Linear Warmup |
|       |     Warmup Ratio     |                0.03                 |
|       |        Max LR        |               $2 e-5$               |
|       |        Min LR        |               $2 e-6$               |
|       |      Precision       |                BF16                 |

Table 9: Training hyperparameters.

## D Evaluation Prompts

### D. 1 Evaluation on Vicuna-80

```
You are a fair judge. You will be provided with a question and two answers. Your task is to judge which answer is of better quality.
Here is the question:
{question}

Here is Answer1:
{answer1}

Here is Answer2:
{answer2}

Your output should be either "Answer1" or "Answer2".
```
