# 2AFC Prompting of Large Multimodal Models for Image Quality Assessment

Hanwei Zhu*, Xiangjie Sui*, Baoliang Chen, Xuelin Liu, Peilin Chen, Yuming Fang, Senior Member, IEEE, and<br>Shiqi Wang, Senior Member, IEEE

#### Abstract

While abundant research has been conducted on improving high-level visual understanding and reasoning capabilities of large multimodal models (LMMs), their visual quality assessment (IQA) ability has been relatively under-explored. Here we take initial steps towards this goal by employing the twoalternative forced choice (2AFC) prompting, as $2 \mathrm{AFC}$ is widely regarded as the most reliable way of collecting human opinions of visual quality. Subsequently, the global quality score of each image estimated by a particular LMM can be efficiently aggregated using the maximum a posterior estimation. Meanwhile, we introduce three evaluation criteria: consistency, accuracy, and correlation, to provide comprehensive quantifications and deeper insights into the IQA capability of five LMMs. Extensive experiments show that existing LMMs exhibit remarkable IQA ability on coarse-grained quality comparison, but there is room for improvement on fine-grained quality discrimination. The proposed dataset sheds light on the future development of IQA models based on LMMs. The codes will be made publicly available at <https://github.com/h4nwei/2AFC-LMMs>.

Index Terms-Large multimodal models, image quality assessment, two-alternative forced choice

## I. INTRODUCTION

$\mathbf{T}$ HE recent breakthroughs in large language models (LLMs) [1] have inspired the development of large multimodal models (LMMs) [2]-[5], aiming to simulate humanlike processing of multimodal information. Three representative abilities-instruction tuning [6], in-context learning [7], and chain-of-thought prompting [8]-highlight the impressive strides made in this field. With the growing interest in LMMs, especially with the emergence phenomenon of models like GPT-4V [5], it becomes crucial to understand their comprehensive capabilities and limitations.

The high-level visual understanding and reasoning abilities of LMMs have been extensively evaluated across numerous benchmarks utilizing popular vision-language tasks [10], such as image captioning, visual question answering, and crossmodality grounding. However, the low-level visual processing and analysis aspects of LMMs remain relatively underexplored. Image quality assessment (IQA), with the goal of evaluating the perceived quality of visual content, serves as[^0]

![](https://cdn.mathpix.com/cropped/2024_02_20_c1b1a52f86e316275051g-1.jpg?height=417&width=881&top_left_y=648&top_left_x=1077)

(a)

Fig. 1. Probing the IQA capability of LMMs via two-alternative forced choice. (a) A pair of images with the corresponding normalized mean opinion scores (MOSs), which is in the range of $[0,100]$. A larger value indicates better visual quality. (b) An order reversed version of (a). Humans can effortlessly select the "Train" image with better visual quality regardless of presentation order, but it is unclear whether the LMMs can make the same right choice. In this example, IDEFICS-Instruct [2] gives the incorrect prediction. MPULGOwl [3] XComposer-VL [4], and Q-Instruct [9] are indifferent to presentation order, and biased towards selecting the second and the first image, respectively. The proprietary GPT-4V [5] is well aligned with human perception of visual quality.

a representative low-level visual task, and holds paramount importance in various image processing [11], [12], computer graphics [13], and computer vision applications [14]. As such, it is highly desirable to evaluate the applicability of LMMs for the IQA task.

Q-Bench [15] presents an early attempt to assess the visual quality understanding abilities of LMMs through binary quality-relevant question answering, standard quality rating, and quality description. Most recently, You et al. [16] emphasized on the importance of more human-like quality description over "contrived" quality rating, and decomposed IQA into three subtasks: quality description, quality comparison, and comparison reasoning. Although these studies may seem appealing at first glance, they require human-verified quality descriptions, which is a more costly and time-consuming process than collecting scalar quality ratings. Moreover, the subjective nature of visual quality adds complexity to aggregating descriptions from various users. Last, the semantic comparison of two quality descriptions [6] represents an unresolved challenge in natural language processing.

The research in visual quality assessment has a long history, and there are many well-established human-rated image quality databases [17]-[23], [23], [24], readily available to test this perceptual aspect of LMMs. In this paper, we propose to adopt the two-alternative forced choice (2AFC) method,

![](https://cdn.mathpix.com/cropped/2024_02_20_c1b1a52f86e316275051g-2.jpg?height=298&width=306&top_left_y=220&top_left_x=172)

(a) AWGN_Level-1

![](https://cdn.mathpix.com/cropped/2024_02_20_c1b1a52f86e316275051g-2.jpg?height=293&width=306&top_left_y=222&top_left_x=454)

(b) AWGN_Level-2

![](https://cdn.mathpix.com/cropped/2024_02_20_c1b1a52f86e316275051g-2.jpg?height=298&width=287&top_left_y=222&top_left_x=735)

(c) JP2K_Level-4

![](https://cdn.mathpix.com/cropped/2024_02_20_c1b1a52f86e316275051g-2.jpg?height=284&width=306&top_left_y=232&top_left_x=1015)

(d) Pink_Level-4

![](https://cdn.mathpix.com/cropped/2024_02_20_c1b1a52f86e316275051g-2.jpg?height=295&width=312&top_left_y=221&top_left_x=1313)

(e) $\operatorname{MOS}=14$

![](https://cdn.mathpix.com/cropped/2024_02_20_c1b1a52f86e316275051g-2.jpg?height=295&width=331&top_left_y=221&top_left_x=1621)

(f) $\operatorname{MOS}=23$

Fig. 2. Illustration of three pairing rules for fine-grained quality comparison. (a)\&(b) Two synthetically distorted images with identical visual content and distortion type but different distortion levels. (c)\&(d) Two synthetically distorted images with identical visual content and distortion level but different distortion types. (e)\&(f) Two realistically distorted images in the MOS interval of $[0,25)$.

also known as the paired comparison to comprehensively evaluate the IQA capability of LMMs on existing image quality datasets. We devise coarse-to-fine pairing rules, and use the maximum a posterior (MAP) estimation [25] to convert pairwise preferences of different LLMs to the global ranking scores. Additionally, we introduce three evaluation criteria, namely consistency, accuracy, and correlation, to quantify different and complementary aspects of the IQA capability of LMMs. These criteria offer deeper insights into the strengths and weaknesses of LMMs in discriminating image quality variations. Extensive experiments on subsets of eight existing image quality datasets reveal many "interesting" behaviors of LMMs (see Fig. 11). Most notably, we find that LMMs generally struggle with the IQA task, some of which exhibit strong biases. On the contrary, the proprietary model GPT$4 \mathrm{~V}$ has exhibited outstanding performance, surpassing the majority of other models by a significant margin. Further testing on more challenging fine-grained pairs reveals that there remains room for improvement.

## II. INGREdientS OF PROBINGg PiPELINE

In this section, we first introduce the coarse-to-fine pairing rules, and then detail the maximum a posterior estimation (MAP) [25] for multiple options. We last introduce three evaluation criteria to benchmark LMMs.

## A. Coarse-to-fine Pairing

To evaluate the IQA capability of LMMs, we devise a set of coarse-to-fine pairing rules. For coarse-grained quality comparison, different images from the same dataset are randomly paired. For fine-grained quality comparison, we propose three pairing rules, as illustrated in Fig. 2. The first rule involves pairing synthetically distorted images with identical visual content and distortion type but different distortion levels. The second rule suggests pairing synthetically distorted images with identical visual content and distortion level but different distortion types. The third rule entails pairing realistically distorted images within the same mean opinion score (MOS) interval (i.e., of similar visual quality).

## B. Maximum a Posterior Estimation

For a complete $2 \mathrm{AFC}$ design, $N$ test stimuli require $\left(\begin{array}{c}N \\ 2\end{array}\right)$ paired comparison to derive the global ranking results, which is infeasible when $N$ gets large. As such, we opt for the maximum a posterior estimation (MAP), which is able to handle $N$ options with fewer needed pairs by solving an optimization problem based on Thurstone's case $\mathrm{V}$ model [25]. We denote a set of images as $\mathcal{D}=\left\{x^{(i)}\right\}_{i=1}^{N}$ and their MOSs as $\left\{q^{(i)}\right\}_{i=1}^{N}$. The LMM is represented by a parametric function $f_{\theta}$, which takes a textual prompt $t$ and two images $\left(x^{(i)}, x^{(j)}\right)$ as inputs, and produces a binary output to indicate whether $x^{(i)}$ is perceived better than $x^{(j)}$. MAP estimation aggregates the quality preference entries $C_{i j}$, which is computed by counting the number of times image $i$ preferred over $j$, into global ranking scores $\left\{q_{\theta}^{(i)}\right\}_{i=1}^{N}$. The log-likelihood of the quality preference matrix $C$ can be defined as

$$
\begin{equation*}
\mathcal{L}\left(q_{\theta} \mid C\right)=\sum_{i, j} C_{i, j} \log \left(\Phi\left(q_{\theta}^{(i)}-q_{\theta}^{(j)}\right)\right) \tag{1}
\end{equation*}
$$

where $\Phi(\cdot)$ is the the standard Normal cumulative distribution function (CDF). The MAP estimation can be formed by solving the above maximum likelihood function with a ridge regularization on the scale values $p\left(q_{\theta}\right)$ :

$$
\begin{array}{ll}
\underset{q_{\theta}}{\arg \max } & \sum_{i, j} C_{i, j} \log \left(\Phi\left(q_{\theta}^{(i)}-q_{\theta}^{(j)}\right)\right)-\sum_{i} \frac{\left(q_{\theta}^{(i)}\right)^{2}}{2}  \tag{2}\\
\text { subject to } & \sum_{i} q_{\theta}^{(i)}=0
\end{array}
$$

Herein, to verify the reliability and effectiveness of MAP estimation, we adopt MOS (to represent the golden human observer), and two no-reference IQA models NIQE [26] and DBCNN [27] as the judges to rank image pairs in the SPAQ dataset [22]. In particular, each image in sampled SPAQ $(N=160)$ is randomly paired with another image in each round, and such pairing process is repeated $M$ rounds until convergence. The winning image shall receive a higher quality score from the judge. We compute the Pearson linear correlation coefficient (PLCC) between the average ranking scores by MAP estimation and MOSs, as shown in Fig. 3 . We find that for different judges, MAP estimation quickly converges to the respective upper bounds (represented by the dashed lines), which are calculated using the raw quality scores. Therefore, we conclude that if the outcome of the pairwise comparison is accurate, MAP estimation will produce reliable global quality ranking scores with a manageable number of paired comparison. By employing LMMs as the judges in the

![](https://cdn.mathpix.com/cropped/2024_02_20_c1b1a52f86e316275051g-3.jpg?height=702&width=827&top_left_y=229&top_left_x=172)

Fig. 3. Validation of MAP estimation in aggregating pairwise rankings from the human observer, NIQE, and DBCNN, respectively. MAP estimation quickly converges as the number of pairing rounds increases, where each round consists of $N$ paired comparisons for $N$ test images. Performance on sampled images from SPAQ $(N=160)$.

MAP estimation, we are able to quantify the capability of LMMs in perceiving visual quality like humans do.

## C. Evaluation Criteria

We propose to quantify the IQA capability of LLMs using the three evaluation criteria.

Consistency $(\kappa)$ measures whether the LLM's prediction is robust to the presentation order of two images:

$$
\begin{equation*}
\kappa=\frac{1}{|\mathcal{P}|} \sum_{(x, y) \in \mathcal{P}} \mathbb{I}\left[f_{\theta}((x, y), t)+f_{\theta}((y, x), t)=1\right] \tag{3}
\end{equation*}
$$

where $|\mathcal{P}|$ denotes the total number of pairs, and $\mathbb{I}[\cdot]$ is the indicator function. $\kappa$ ranges from $[0,1]$ with a larger value indicating higher consistency.

Accuracy $(\alpha)$ measures the accuracy rate of the LLM, provided that the consistency constraint (i.e., $f_{\theta}((x, y), t)+$ $\left.f_{\theta}((y, x), t)=1\right)$ is met:

$$
\begin{equation*}
\alpha=\frac{1}{\left|\mathcal{P}_{s}\right|} \sum_{(x, y) \in \mathcal{P}_{s}} \mathbb{I}[f((x, y), t)=\mathbb{I}[q(x) \geq q(y)]] \tag{4}
\end{equation*}
$$

where $\mathcal{P}_{s} \subset \mathcal{P}$ contains the subset of image pairs that the LLM makes consistent prediction.

Correlation $(\rho)$ measures the linear correlation between the global ranking scores aggregated by MAP and the MOSs:

$$
\begin{equation*}
\rho=\frac{\sum_{i=1}^{N}\left(q^{(i)}-\bar{q}\right)\left(q_{\theta}^{(i)}-\bar{q}_{\theta}\right)}{\sqrt{\sum_{i=1}^{N}\left(q^{(i)}-\bar{q}\right)^{2}} \sqrt{\sum_{i=1}^{N}\left(q_{\theta}^{(i)}-\bar{q}_{\theta}\right)^{2}}}, \tag{5}
\end{equation*}
$$

where $\bar{q}$ and $\bar{q}_{\theta}$ represent the mean MOS and ranking score, respectively. Before computing $\rho$, a simple monotonic function is commonly applied to map the model prediction to the MOS range as a way of compensating prediction nonlinearity [28].

### TABLE I

OVERVIEW OF THE IMAGE SUBSET SAMPLED FROM EIGHT EXISTING IMAGE QUALITY DATASETS. THE TWO NUMBERS SEPARATED BY "/" IN THE LAST TWO COLUMNS REPRESENT THE NUMBER OF REFERENCE AND DISTORTED IMAGES, RESPECTIVELY. WE EMPHASIZE IN THE THIRD SECTION TWO DATASETS-KADIS-700K AND SQAD—THAT ARE LESS LIKELY TO BE INCLUDED FOR TRAINING LMMS DUE TO THE ABSENCE OF MOSS. WE EQUIP THEM WITH MOSS FROM A FORMAL SUBJECTIVE EXPERIMENT TO TEST LMMS WHILE MINIMIZING THE POTENTIAL DATA CONTAMINATION RISK

|                               | Dataset        |            Distortion             |   \# images   | \# samples |
| :---------------------------: | :------------- | :-------------------------------: | :-----------: | :--------: |
| $*$ <br> Coarse- <br> grained | CSIQ [17]      |             Synthetic             |  $30 / 866$   |     30     |
|                               | KADID-10k [18] |             Synthetic             | $81 / 10,125$ |     81     |
|                               | MM21 [19]      |             Synthetic             | $129 / 5,031$ |    129     |
|                               | KLIVE [20]     |             Realistic             |     1,169     |    100     |
|                               | SPAQ [22]      |             Realistic             |    10,074     |    160     |
|                               | KADIS-700k     |             Realistic             |    11,125     |    160     |
|             Fine-             | Synthetic      | $140 \mathrm{k} / 750 \mathrm{k}$ |      100      |            |
|            Frained            | SQAD [23]      |             Realistic             |     3,017     |    100     |

## III. EXPERIMENTS

In this section, we first provide the experimental setups, and then present the coarse-grained and fine-grained IQA results of four LMMs with in-depth analysis. Last, other global ranking aggregation methods are applied to conduct the ablation experiments.

### A. Experimental Setups

We assess five LMMs that accept multiple images as input. These include four open-source models: IDEFICSInstruct (based on LLaMA-9B) [2], mPLUG-Owl (based on LLaMA-7B) [3], XComposer-VL (based on InternLM-7B) [4], and Q-Instruct (based on LLaVA_v1.5-7B) [9] and one closedsource model: GPT-4V [5]. We initialize the open-source models with their default pretrained weights and use the official API to call GPT-4V. We sample a total of 1,060 images from eight image quality datasets to conduct experiments. Synthetically distorted images are selected from CSIQ [17], KADID-10k [18], KADIS-700k [24], and MM21 [19] datasets. Realistically distorted images are chosen from CLIVE [20], KonIQ-10k [21], SPAQ [22], and SQAD [23] datasets. As listed in Table i] the sampled images form two subsets for coarse-grained and fine-grained quality assessment, respectively. It is worth noting that we manually curate 200 images from KADIS-700k and SQAD datasets, which do not contain MOSs. This selection is to avoid data contamination, considering that closed-source LMM, such as GPT-4V, may have been trained on these image quality datasets. To assign MOSs to images from KADIS-700k and SQAD datasets, we conduct subjective testing using the single stimulus continuous methodology [29]. We invite 20 subjects to participate in subjective testing in a controlled laboratory environment, ensuring the ambient illumination does not directly reflect off the displays. We apply the outlier rejection strategy recommended by ITUT BT.500 [29] to filter noisy data. Finally, the mean value of the valid scores for each image is taken as the ground truth quality score.

TABLE II

VQA CAPABILITY COMPARISONS OF THE LMMS IN TERMS OF CONSISTENCY $(\kappa)$, ACCURACY $(\alpha)$, AND CORRELATION $(\rho)$ WITH THE COARSE-GRAINED SETTING. THE WEIGHTED AVERAGE IS COMPUTED BY THE AVERAGE VALUES WEIGHTED BY THE NUMBER OF SAMPLES OF THE CORRESPONDING SUBSETS. THE BEST TWO RESULTS ARE HIGHLIGHTED IN BOLDFACE AND UNDERLINE, RESPECTIVELY

|                  |            | IDEFICS-Instruct $[2]$ | IDEFICS-Instruct $[2]$ | IDEFICS-Instruct $[2]$ |  mPLUG-Owl $[3]$  |  mPLUG-Owl $[3]$  | mPLUG-Owl $[3]$ | XComposer-VL $[4]$ | XComposer-VL $[4]$ | XComposer-VL $[4]$ |  Q-Instruct $[9]$   |  Q-Instruct $[9]$   | Q-Instruct $[9]$ |     GPT-4V $[5]$     |     GPT-4V $[5]$     |     GPT-4V $[5]$     |
| :--------------- | :--------: | :--------------------: | :--------------------: | :--------------------: | :---------------: | :---------------: | :-------------: | :----------------: | :----------------: | :----------------: | :-----------------: | :-----------------: | :--------------: | :------------------: | :------------------: | :------------------: |
| Dataset          | Distortion |   $\kappa \uparrow$    |   $\alpha \uparrow$    |    $\rho \uparrow$     | $\kappa \uparrow$ | $\alpha \uparrow$ | $\rho \uparrow$ | $\kappa \uparrow$  | $\alpha \uparrow$  |  $\rho \uparrow$   |  $\kappa \uparrow$  |  $\alpha \uparrow$  | $\rho \uparrow$  |  $\kappa \uparrow$   |  $\alpha \uparrow$   |   $\rho \uparrow$    |
| CSIQ             | Synthetic  |         0.206          |         0.094          |         0.670          |       0.422       |       0.233       |      0.649      |       0.233        |       0.122        |       0.489        |        0.117        |        0.078        |      0.650       |        0.778         |        0.589         |        0.764         |
| KADID-10k        | Synthetic  |         0.202          |         0.102          |         0.552          |       0.396       |       0.179       |      0.399      |       0.267        |       0.154        |       0.517        |        0.387        |        0.269        |      0.466       |        0.763         |        0.540         |        0.560         |
| MM21             | Synthetic  |         0.337          |         0.173          |         0.338          |       0.385       |       0.204       |      0.319      |       0.171        |       0.109        |       0.411        |        0.480        |        0.324        |      0.392       |        0.792         |        0.544         |        0.474         |
| CLIVE            | Realistic  |         0.323          |         0.152          |         0.492          |       0.365       |       0.180       |      0.444      |       0.133        |       0.092        |       0.489        |        0.327        |        0.195        |      0.432       |        0.837         |        0.685         |        0.785         |
| KonIQ-10k        | Realistic  |         0.251          |         0.119          |         0.479          |       0.399       |       0.214       |      0.448      |       0.148        |       0.058        |       0.463        |        0.489        |        0.344        |      0.512       |        0.836         |        0.691         |        0.800         |
| SPAQ             | Realistic  |         0.330          |         0.148          |         0.474          |       0.332       |       0.152       |      0.326      |       0.208        |       0.081        |       0.457        |        0.485        |        0.332        |      0.397       |        0.871         |        0.736         |        0.876         |
| Weighted average |            |         0.286          |         0.137          |  $\underline{0.470}$   |       0.377       |       0.189       |      0.396      |       0.188        |       0.094        |       0.463        | $\underline{0.432}$ | $\underline{0.292}$ |      0.449       | $\mathbf{0 . 8 2 3}$ | $\mathbf{0 . 6 4 6}$ | $\mathbf{0 . 7 2 1}$ |
| KADIS-700k       | Synthetic  |         0.191          |         0.112          |         0.635          |       0.388       |       0.219       |      0.612      |       0.255        |       0.119        |       0.596        |        0.460        |        0.291        |      0.658       |        0.842         |        0.665         |        0.674         |
|                  | Realistic  |         0.326          |         0.190          |         0.746          |       0.330       |       0.183       |      0.618      |       0.154        |       0.068        |       0.690        |        0.466        |        0.254        |      0.642       |        0.814         |        0.667         |        0.742         |
| Mixed            |            |         0.296          |         0.133          |         0.567          |       0.372       |       0.198       |      0.503      |       0.187        |       0.078        |       0.500        |        0.477        |        0.289        |      0.503       |        0.839         |        0.620         |        0.678         |
| Weighted average |            |         0.289          |         0.136          |  $\underline{0.629}$   |       0.376       |       0.019       |      0.559      |       0.188        |       0.090        |       0.572        | $\underline{0.463}$ | $\underline{0.273}$ |      0.576       | $\mathbf{0 . 8 2 7}$ | $\mathbf{0 . 6 4 0}$ | $\mathbf{0 . 6 9 3}$ |

For image pairs with inconsistent predictions (see Eq. (3)), we exclude them from updating the quality preference matrix $C$. It is worth noting that global ranking scores are re-scale to the range of $[0,100]$. A larger score indicates better visual quality. We set the round number $M$ to 12 in our experiments, which is sufficient for the MAP estimation to converge, as shown in Fig. 3 The pre-defined prompts $t$ are given as follows:

```
prompt = [
 'This is the first image:', <Image x>,
 'This is the second image:' <Image y>,
 'Which image has better visual quality?'
]
```

## B. Coarse-grained IQA Performance

We collect a total of 860 images for the coarse-grained quality comparison from eight IQA datasets. There are three sampling strategies. 1) We ensure the distorted images selected from the synthetic datasets are content-independent; 2) The mean opinion score (MOS) distribution of these images of each dataset is maintained as a roughly uniform distribution across five quality levels (excellent, good, fair, poor bad); 3) We compute the spatial information and colorfulness attributes of the chosen images to ensure the content balance [30].

We conduct the experiments with the images from the same dataset owing to the varying MOS scales across different datasets. The results are shown in Table II. from which we can obtain several interesting observations. First, all open-source LMMs, i.e., IDEFICS-Instruct, mPLUG-Owl, XComposer-VL, and Q-Instruct, show poor performance in terms of prediction consistency, suggesting a tendency to provide biased responses regardless of image content. For instance, we count IDEFICS-Instruct and mPLUG-Owl to demonstrate a percentage exceeding $70 \%$ of choosing the "second" image, while the XComposer-VL exhibits a preference for the "first" image with approximately $80 \%$. Such biased predictions significantly impact the accuracy and consistency of model inference, leading to inferior performance in IQA. In addition, while Q-Instruct claims to achieve competitive lowlevel instruction performance for individual images, it shows subpar performance on comparing the visual quality of a pair of images and indicates the model may suffer from over-fitting issues. Subsequently, GPT-4V outperforms other LMMs across all datasets according to the three proposed evaluation criteria, suggesting its inherent capability to quantify visual quality. To mitigate potential data contamination issues associated with GPT-4V, we strategically select images from the KADIS-700k dataset, which lacks quality-related labels, and the recently released SQAD dataset. Despite these constraints, GPT-4V continues to demonstrate superior performance across these datasets. Notably, the accuracy $\alpha$ of consistent pairs surpasses $60 \%$ when compared to human preferences. Moreover, GPT$4 \mathrm{~V}$ performs better on datasets with realistic distortion compared with synthetic distortion, as shown in Table II. This could be attributed to the fact that LMMs are trained on the pairs of text and images with realistic distortions. Last but not least, despite the increased complexity presented by pairs that contain mixed distortions, GPT-4V still obtains promising results, outperforming the majority of remaining LMMs.

## C. Fine-grained IQA Performance

We utilize sampled images from CSIQ and SPAQ to carry out the fine-grained quality assessment. Specifically, we sample four scenes from the CSIQ dataset. Each of them is degraded by five classical distortion types, including additive white Gaussian noise (AWGN), JPEG, JPEG 2000 (JP2K), pink noise, and blur, and five distortion levels. For realistic distortion, we select SPAQ as our target database, partition the normalized MOS scores at the range of $[0,100]$ into four equidistant intervals, and strictly limit the sampling to 25 images per MOS interval.

Since fine-grained quality comparisons are more challenging, we invite one subject to conduct the experiment in the same setting as the four LMMs. We present the consistency and accuracy in Table III The correlation results are shown in Table IV, For the synthetically distorted images from the CSIQ dataset, we first compare the images with the same content

TABLE III

VQA CAPABILITY COMPARISONS IN TERMS OF CONSISTENCY $(\kappa)$ AND ACCURACY $(\alpha)$ WITH THE FINE-GRAINED SETTING

|            Dataset            |    Type    | IDEFICS-Instruct 2 |                   |   mPLUG-Owl [3]   |                     |   XCompose-VL 4    |                   |  Q-Instruct [9]   |                     |     GPT-4V [5]      |                   |  Single subject   |                   |
| :---------------------------: | :--------: | :----------------: | :---------------: | :---------------: | :-----------------: | :----------------: | :---------------: | :---------------: | :-----------------: | :-----------------: | :---------------: | :---------------: | :---------------: |
|                               |            | $\kappa \uparrow$  | $\alpha \uparrow$ | $\kappa \uparrow$ |      $\alpha$       | $\kappa \uparrow$  | $\alpha \uparrow$ | $\kappa \uparrow$ |  $\alpha \uparrow$  |  $\kappa \uparrow$  | $\alpha \uparrow$ | $\kappa \uparrow$ | $\alpha \uparrow$ |
|             CSIQ              |    AWGN    |       0.000        |       0.000       |       0.448       |        0.260        |       0.354        |       0.302       |       0.083       |        0.042        |        0.219        |       0.219       |       0.885       |       0.865       |
|                               |    JPEG    |       0.000        |       0.000       |       0.448       |        0.250        |       0.448        |       0.177       |       0.073       |        0.073        |        0.490        |       0.459       |       0.885       |       0.865       |
|                               |    JP2K    |       0.323        |       0.323       |       0.438       |        0.188        |       0.448        |       0.146       |       0.115       |        0.083        |        0.542        |       0.542       |       0.844       |       0.823       |
|                               |    Pink    |       0.000        |       0.000       |       0.365       |        0.198        |       0.469        |       0.198       |       0.063       |        0.052        |        0.479        |       0.479       |       0.958       |       0.958       |
|                               |    Blur    |       0.156        |       0.156       |       0.469       |        0.167        |       0.479        |       0.146       |       0.240       |        0.156        |        0.364        |       0.313       |       0.979       |       0.958       |
|            Average            |            |       0.096        |       0.096       |       0.433       | $\underline{0.212}$ |       0.440        |       0.194       |       0.115       |        0.081        | $\underline{0.419}$ |       0.402       |       0.910       |       0.894       |
|             CSIQ              |  Level-1   |       0.000        |       0.000       |       0.552       | $\overline{0.292}$  |       0.177        |       0.073       |       0.104       |        0.042        | $\overline{0.010}$  |       0.000       |       0.406       |       0.354       |
|                               |  Level-2   |       0.000        |       0.000       |       0.407       |        0.229        |       0.355        |       0.271       |       0.146       |        0.094        |        0.063        |       0.042       |       0.708       |       0.563       |
|                               |  Level-3   |       0.000        |       0.000       |       0.500       |        0.282        |       0.375        |       0.094       |       0.135       |        0.052        |        0.344        |       0.333       |       0.885       |       0.813       |
|                               |  Level-4   |       0.125        |       0.104       |       0.385       |        0.188        |       0.448        |       0.292       |       0.083       |        0.052        |        0.604        |       0.531       |       0.885       |       0.802       |
|                               |  Level-5   |       0.427        |       0.427       |       0.458       |        0.219        |       0.458        |       0.208       |       0.115       |        0.104        |        0.604        |       0.313       |       0.958       |       0.927       |
|            Average            |            |       0.110        |       0.106       |       0.460       |        0.242        |       0.363        |       0.187       |       0.117       |        0.069        |        0.325        |       0.244       |       0.769       |       0.692       |
|             SPAQ              |  $[0,25)$  |       0.465        |       0.174       |       0.417       | $\overline{0.201}$  | $\overline{0.153}$ |       0.104       |       0.389       |        0.236        |        0.465        |       0.208       |       0.896       |       0.472       |
|                               | $[25,50)$  |       0.410        |       0.264       |       0.417       |        0.194        |       0.097        |       0.035       |       0.486       |        0.285        |        0.812        |       0.583       |       0.931       |       0.708       |
|                               | $[50,75)$  |       0.451        |       0.215       |       0.458       |        0.271        |       0.160        |       0.035       |       0.493       |        0.229        |        0.674        |       0.382       |       0.806       |       0.507       |
|                               | $[75,100]$ |       0.444        |       0.285       |       0.382       |        0.181        |       0.167        |       0.042       |       0.424       |        0.181        |        0.660        |       0.417       |       0.792       |       0.458       |
| $\frac{1}{\text { Average }}$ |            |       0.443        |       0.235       |       0.419       |        0.212        |       0.144        |       0.054       |       0.448       | $\underline{0.233}$ |        0.653        |       0.398       |       0.856       |       0.536       |

TABLE IV

VQA CAPABILITY COMPARISONS IN TERMS OF CORRELATION $(\rho)$ WITH THE FINE-GRAINED SETTING

|            | IDEFICS- <br> Instruct |   mPLUG- <br> Owl   | XCompose- <br> VL |  Q- <br> Instruct   |     GPT- <br> 4V     | Single <br> subject |
| :--------- | :--------------------: | :-----------------: | :---------------: | :-----------------: | :------------------: | :-----------------: |
| AWGN       |         0.000          |        0.543        |       0.586       |        0.449        |        0.815         |        0.919        |
| JPEG       |         0.000          |        0.482        |       0.148       |        0.560        |        0.933         |        0.929        |
| JP2K       |         0.700          |        0.643        |       0.189       |        0.631        |        0.966         |        0.935        |
| Pink       |         0.000          |        0.396        |       0.085       |        0.563        |        0.921         |        0.951        |
| Blur       |         0.368          |        0.396        |       0.512       |        0.583        |        0.894         |        0.921        |
| Average    |         0.214          |        0.492        |       0.304       | $\underline{0.557}$ | $\mathbf{0 . 9 0 6}$ |        0.931        |
| Level-1    |         0.000          |        0.444        |       0.281       |        0.258        |        0.000         |        0.297        |
| Level-2    |         0.000          |        0.332        |       0.222       |        0.617        |        0.265         |        0.716        |
| Level-3    |         0.000          |        0.499        |       0.409       |        0.664        |        0.492         |        0.769        |
| Level-4    |         0.502          |        0.197        |       0.375       |        0.230        |        0.855         |        0.910        |
| Level-5    |         0.366          |        0.216        |       0.305       |        0.311        |        0.799         |        0.976        |
| Average    |         0.174          |        0.338        |       0.318       | $\underline{0.416}$ | $\mathbf{0 . 4 8 2}$ |        0.734        |
| $[0,25)$   |         0.191          |        0.366        |       0.483       |        0.371        |        0.387         |        0.376        |
| $[25,50)$  |         0.198          |        0.373        |       0.326       |        0.503        |        0.412         |        0.646        |
| $[50,75)$  |         0.140          |        0.405        |       0.287       |        0.268        |        0.573         |        0.610        |
| $[75,100]$ |         0.395          |        0.372        |       0.346       |        0.169        |        0.420         |        0.346        |
| Average    |         0.231          | $\underline{0.379}$ |       0.361       |        0.328        | $\mathbf{0 . 4 4 8}$ |        0.495        |

and identical distortion types but varied distortion levels. From Tables III] [IV and Fig. 2](a)\&(b), we observe that the existing LMMs struggle to distinguish the image with superior quality in such fine-grained comparisons. Although GPT-4V outperforms other LMMs, the average consistency and accuracy values are far from human performance. The AWGN is the most difficult distortion type compared with other distortions for the existing LMMs, possibly due to its rarity in the training data. The correlation of Q-Instruct underperforms IDEFICS-Instruct, indicating that the low-level information of single images does not improve the visual quality comparison capability of the Q-Instruct. Subsequently, we compare the images with the same content and distortion levels but different distortion types. We find that it is challenging to compare a pair of images with slight distortions (e.g., Level-1 and Level-2), and the LMMs recognize them as the same image. However, as the level of distortion increases, different distortions demonstrate distinct visual appearances, making it easier to discern the superior quality image (see Fig. 2 (c)\&(d)). Additionally, mPLUG-Owl outperforms GPT-4V in terms of the consistency criterion and achieves the second-best average accuracy value, which reveals that mPLUG-Owl demonstrates better fine-grained IQA capability compared with other opensource LMMs. For realistically distorted images from the SPAQ dataset, we present four normalized MOS intervals to conduct the fine-grained comparison. Most LMMs perform better for realistic distortions than synthetic distortions. Subjects and LMMs can more readily discern preferences within the quality interval of $[25,50)$. It is reasonable for LMMs to exhibit inferior performance in the quality interval of $[0,25)$ and $[75,100]$ as they represent either severe distortion or highquality visual appearance, both of which pose significant challenges for human observers in selecting an image of superior quality. Overall, GPT-4V demonstrates the best performance in the fine-grained IQA experiment, but there remains ample room for improvement.

## D. Ablation Experiments

In this subsection, we compare the MAP estimation to other global aggregation methods, including the maximum likelihood estimation (MLE) [25], the Perron rank method [31], and the TrueSkill rating system [32]. In contrast to MAP estimation, MLE directly optimizes the log-likelihood function to derive the global ranking scores. The Perron rank method uses the principal eigenvector of a pairwise comparison matrix to generate the global ranking, providing a robust and efficient solution for ranking problems [31]. TrueSkill rating system is a video game ranking algorithm that models the skill of each player as a univariate Gaussian random variable, with mean and variance representing the average skill of each player and the degree of uncertainty, respectively. As shown in Table V we can observe MAP and TrueSkill perform better than other methods. While TrueSkill demonstrates competitive results to MAP, we continue to choose MAP estimation as our default method owing to its mathematically appealing properties.

TABLE V

QUANTITATIVE COMPARISON OF GPT-4V AGGREGATED BY DIFFERENT GLOBAL RANKING METHODS IN TERMS OF PLCC

|     Method     |         CSIQ         |      KADID-10k       |         MM21         |        CLIVE         |      KonIQ-10k       |         SPAQ         |      KADIS-700k      |         SQAD         |
| :------------: | :------------------: | :------------------: | :------------------: | :------------------: | :------------------: | :------------------: | :------------------: | :------------------: |
|    MLE [25]    |        0.757         |        0.575         |        0.472         |        0.745         |        0.734         |        0.828         |        0.667         |        0.676         |
|  Perron [31]   |        0.708         |        0.537         |        0.480         |        0.760         |        0.758         |        0.860         |        0.650         |        0.632         |
| TrueSkill [32] | $\mathbf{0 . 7 9 7}$ |        0.557         | $\mathbf{0 . 4 8 2}$ |        0.773         |        0.793         | $\mathbf{0 . 8 8 7}$ | $\mathbf{0 . 7 2 8}$ |        0.737         |
|    MAP [25]    |        0.764         | $\mathbf{0 . 5 6 0}$ |        0.474         | $\mathbf{0 . 7 8 5}$ | $\mathbf{0 . 8 0 0}$ |        0.876         |        0.674         | $\mathbf{0 . 7 4 2}$ |

## IV. Conclusions

In this work, we have probed the low-level IQA capabilities of LMMs, an area that has been relatively under-explored. We devise coarse-grained and fine-grained pairing rules to evaluate the IQA ability of the state-of-the-art LMMs. The MAP estimation is used for aggregating global ranking scores of different LMMs. We further propose three evaluation criteria, providing a comprehensive evaluation of the LMM's IQA abilities. Our analysis has revealed that most LMMs generally lack IQA capabilities and tend to exhibit biased preferences. The proprietary LMM, GPT-4V, shows promising performance in the coarse-grained subset, indicating potential applicability in IQA. However, there is still considerable room for improvement in the IQA ability of existing LMMs, particularly in the fine-grained subset. We hope that our benchmark and analysis will serve as a catalyst for the development of more advanced and versatile LMMs in the field of visual quality assessment.

## ACKNOWLEDGEMENTS

The authors thank Kede Ma for his insightful discussions and diligent efforts in revising the paper.

## REFERENCES

[1] OpenAI, "GPT-4 technical report," CoRR, vol. abs/2303.08774, 2023.

[2] H. Face, "Introducing IDEFICS: An open reproduction of state-of-theart visual language model," <https://huggingface.co/blog/idefics/> 2023.

[3] Q. Ye, H. Xu, G. Xu, J. Ye, M. Yan, Y. Zhou, J. Wang, A. Hu, P. Shi, Y. Shi, and et al., "mPLUG-Owl: Modularization empowers large language models with multimodality," CoRR, vol. abs/2304.14178, 2023.

[4] P. Zhang, X. D. B. Wang, Y. Cao, C. Xu, L. Ouyang, Z. Zhao, S. Ding, S. Zhang, and et al., "InternLM-XComposer: A vision-language large model for advanced text-image comprehension and composition," CoRR, vol. abs/2309.15112, 2023.

[5] OpenAI, "GPT-4V(ision) system card," <https://cdn.openai.com/papers/> GPTV_System_Card.pdf/ 2023.

[6] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Rozière, N. Goyal, and et al., "LLaMA: Open and efficient foundation language models," CoRR, vol. abs/2302.13971, 2023.

[7] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, and et al., "Language models are few-shot learners," in Neural Information Processing Systems, 2020, pp. 1877-1901.

[8] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, and et al., "Chain-of-thought prompting elicits reasoning in large language models," in Neural Information Processing Systems, 2022, pp. 24 824-24 837 .

[9] H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, K. Xu, C. Li, J. Hou, G. Zhai et al., "Q-Instruct: Improving low-level visual abilities for multi-modality foundation models," CoRR, vol. abs/:2311.06783, 2023.

[10] R. Cai, Z. Song, D. Guan, Z. Chen, X. Luo, C. Yi, and A. Kot, "BenchLMM: Benchmarking cross-style visual capability of large multimodal models," CoRR, vol. abs/2312.02896, 2023.
[11] Q. Wu, H. Li, K. N. Ngan, and K. Ma, "Blind image quality assessment using local consistency aware retriever and uncertainty aware evaluator," IEEE Trans. Circuits and Systems for Video Tech., vol. 28, no. 9, pp. 2078-2089, 2017.

[12] W. Yang, H. Huang, J. Liu, and A. C. Kot, "Facial image compression via neural image manifold compression," IEEE Trans. Circuits and Systems for Video Tech., to appear 2023.

[13] L. Zhao, W. Zheng, Y. Duan, J. Zhou, and J. Lu, "SPTR: Structurepreserving transformer for unsupervised indoor depth completion," IEEE Trans. Circuits and Systems for Video Tech., to appear 2023.

[14] H. Zhu, B. Chen, L. Zhu, and S. Wang, "Learning spatiotemporal interactions for user-generated video quality assessment," IEEE Trans. Circuits and Systems for Video Tech., vol. 33, no. 3, pp. 1031-1042, 2023.

[15] H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, C. Li, W. Sun, Q. Yan, G. Zhai, and W. Lin, "Q-Bench: A benchmark for general-purpose foundation models on low-level vision," CoRR, vol. abs/2309.14181, 2023.

[16] Z. You, Z. Li, J. Gu, Z. Yin, T. Xue, and C. Dong, "Depicting beyond scores: Advancing image quality assessment through multimodal language models," CoRR, vol. abs/2312.08962, 2023.

[17] E. C. Larson and D. M. Chandler, "Most apparent distortion: Fullreference image quality assessment and the role of strategy," Journal of Electronic Imaging, vol. 19, no. 1, pp. 011 006-011 027, 2010.

[18] H. Lin, V. Hosu, and D. Saupe, "KADID-10k: A large-scale artificially distorted IQA database," in IEEE Int. Conf. Multimedia and Expo, 2019, pp. 1-3.

[19] Y. Li, S. Wang, X. Zhang, S. Wang, S. Ma, and Y. Wang, "Quality assessment of end-to-end learned image compression: The benchmark and objective measure," in ACM Int. Conf. on Multimedia, 2021, pp. 4297-4305.

[20] D. Ghadiyaram and A. C. Bovik, "Massive online crowdsourced study of subjective and objective picture quality," IEEE Trans. Image Processing, vol. 25, no. 1, pp. 372-387, 2016.

[21] V. Hosu, H. Lin, T. Sziranyi, and D. Saupe, "KonIQ-10k: An ecologically valid database for deep learning of blind image quality assessment," IEEE Trans. Image Processing, vol. 29, pp. 4041-4056, 2020.

[22] Y. Fang, H. Zhu, Y. Zeng, K. Ma, and Z. Wang, "Perceptual quality assessment of smartphone photography," in IEEE Int. Conf. Computer Vision and Pattern Recognition, 2020, pp. 3677-3686.

[23] Z. Fang, A. Ignatov, E. Zamfir, and R. Timofte, "SQAD: Automatic smartphone camera quality assessment and benchmarking," in IEEE Int. Conf. on Computer Vision, 2023, pp. 20532-20 542.

[24] H. Lin, V. Hosu, and D. Saupe, "DeepFL-IQA: Weak supervision for deep IQA feature learning," CoRR, vol. abs/2001.08113, 2020.

[25] K. Tsukida and M. R. Gupta, "How to analyze paired comparison data," Technical Report UWEETR-2011-0004, University of Washington, 2011.

[26] A. Mittal, R. Soundararajan, and A. C. Bovik, "Making a "completely blind' image quality analyzer," IEEE Signal Processing Letters, vol. 20, no. 3, pp. 209-212, 2013.

[27] W. Zhang, K. Ma, J. Yan, D. Deng, and Z. Wang, "Blind image quality assessment using a deep bilinear convolutional neural network," IEEE Trans. Circuits and Systems for Video Tech., vol. 30, no. 1, pp. 36-47, 2020.

[28] VQEG, "Final report from the video quality experts group on the validation of objective models of video quality assessment," 2000. [Online]. Available: <http://www.vqeg.org>

[29] B. T. ITU-R, "Methodology for the subjective assessment of the quality of television pictures," <https://www.itu.int/rec/R-REC-BT.500> 2002.

[30] S. Winkler, "Analysis of public image and video databases for quality assessment," IEEE Journal of Selected Topics in Signal Processing, vol. 6, no. 6, pp. 616-625, 2012

[31] T. L. Saaty and L. G. Vargas, "Inconsistency and rank preservation," Journal of Mathematical Psychology, vol. 28, no. 2, pp. 205-214, 1984

[32] R. Herbrich, T. Minka, and T. Graepel, "Trueskill" ${ }^{\mathrm{TM}}$ : A bayesian skill rating system," in Neural Information Processing Systems, 2007, pp. 569-576.

[^0]: \*The authors contributed equally to this work.

    Hanwei Zhu, Baoliang Chen, Peilin Chen, and Shiqi Wang are with the Department of Computer Science, City University of Hong Kong, Hong Kong, China. (e-mail: \{hanwei.zhu, blchen6-c\}@my.cityu.edu.hk, \{plchen3, shiqwang $\} @$ cityu.edu.hk.)

    Xiangjie Sui, Xuelin Liu, and Yuming Fang are with the School of Information Management, Jiangxi University of Finance and Economics, Nanchang, Jiangxi, China (e-mail: <xjsui@foxmail.com>, <xuelinliu-bill@foxmail.com>, <fa0001ng@e.ntu.edu.sg>).

    Corresponding author: Shiqi Wang.
