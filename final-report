# Vision-Language Navigation for Autonomous Mobile Robots

## Final Summer Research Report

**Student:** Yuhui Xu  
**Group:** VLN Group  
**Supervisor:** Prof. Cui  
**Program:** FURP 2026  
**Repository:** https://github.com/scyyx17-cyber/fury-2026-Yuhui-Xu-VLN  
**Date:** September 2026

---

## Abstract

Vision-Language Navigation (VLN) is a challenging task that requires an embodied agent to follow natural language instructions in unseen environments. This report presents the work conducted during a summer research project in the VLN group. As a first-year undergraduate student with limited prior research experience, the primary objective was to understand the VLN problem and reproduce a simple baseline on the Room-to-Room (R2R) dataset using the Habitat simulator. A Seq2Seq model with a frozen ResNet-50 visual encoder and an LSTM/GRU policy was implemented and trained via imitation learning on a subset of the R2R training set. Due to computational and time constraints, the model was trained for only 5 epochs on 2,000 episodes. The best result achieved on the validation unseen split was 3.1% success rate (SR) and 2.2 SPL, which is significantly lower than results reported in the original literature. The report analyzes the causes of these poor results, documents the challenges encountered during environment setup, data preprocessing, and model training, and discusses limitations and potential future directions. Despite the low performance, the project provided valuable hands-on experience with Linux, PyTorch, and the practical difficulties of embodied AI research.

---

## 1. Introduction

Vision-Language Navigation (VLN) is a fundamental capability for autonomous mobile robots (AMRs) that need to interpret natural language commands such as “Go past the kitchen and stop near the sofa.” Unlike traditional navigation systems that rely on metric maps and geometric goals, VLN requires the agent to jointly ground language expressions in visual observations and make a sequence of decisions in previously unseen environments. This problem is challenging because the agent must handle ambiguous instructions, maintain spatial memory, and decide when to stop.

The goal of this summer project was to gain a basic understanding of VLN and to reproduce a simple baseline. As a first-year student, I had limited background in robotics, deep learning, and research methodology. Therefore, the project focused on implementation and reproduction rather than proposing a novel method. The main contributions of this report are:

- A working implementation of a simple Seq2Seq VLN agent using Habitat and PyTorch;
- An empirical evaluation on the R2R validation unseen split, showing the difficulty of the task under limited training;
- A detailed documentation of the challenges encountered by a beginner in VLN research.

---

## 2. Related Work

The Room-to-Room (R2R) dataset [1] is the most widely used benchmark for VLN. It contains human-annotated navigation instructions in photorealistic indoor environments. Evaluation metrics include Navigation Error (NE), Success Rate (SR), Success weighted by Path Length (SPL), and Trajectory Length (TL). Early VLN methods used sequence-to-sequence (Seq2Seq) models with LSTM encoders [1]. Later work introduced transformer-based architectures such as VLN-BERT [2] and HAMT [3], which leverage pre-training and cross-modal attention. DUET [4] combines topological mapping with transformer planning, while NavGPT [5] explores the use of large language models for zero-shot navigation. Due to resource limitations, this project only reproduced a simplified Seq2Seq baseline; more advanced methods were not implemented.

---

## 3. Methodology

### 3.1 Problem Formulation

We formulate VLN as a partially observable Markov decision process (POMDP). At each time step \( t \), the agent receives a natural language instruction \( I = \{w_1, \dots, w_L\} \) and a visual observation \( o_t \) (RGB image). The action space is defined as:

\[
\mathcal{A} = \{\text{forward}, \text{turn\_left}, \text{turn\_right}, \text{stop}\}
\]

The agent is considered successful if it stops within 3 meters of the target location.

### 3.2 Model Architecture

The implemented model consists of four components:

1. **Language Encoder:** An LSTM with 256 hidden units encodes the instruction into a sequence of word embeddings.
2. **Visual Encoder:** A pre-trained ResNet-50 (frozen) extracts 2048-dimensional features from RGB images.
3. **Cross-Modal Fusion:** The language and visual features are concatenated at each time step.
4. **Policy:** A recurrent module (LSTM or GRU) with 512 hidden units maintains the agent state and predicts the next action.

This architecture is a simplified version of the original Seq2Seq baseline [1]. It does not include attention, pre-training, or historical context beyond the recurrent hidden state.

### 3.3 Training

The model was trained via imitation learning with teacher forcing on expert trajectories from the R2R training set. The loss function was cross-entropy between the predicted action distribution and the expert action. Due to GPU memory constraints (12 GB), the batch size was limited to 4. The model was trained for 5 epochs on a subset of 2,000 training episodes. No reinforcement learning fine-tuning was performed.

---

## 4. Experimental Setup

### 4.1 Simulator and Dataset

- **Simulator:** Habitat 0.2.4
- **Dataset:** R2R [1]
- **Training subset:** 2,000 episodes (due to time and storage constraints)
- **Validation splits:** val_seen and val_unseen

### 4.2 Evaluation Metrics

- **Navigation Error (NE):** L2 distance between the agent’s final position and the target.
- **Success Rate (SR):** Percentage of episodes with NE < 3 meters.
- **Success weighted by Path Length (SPL):** SR weighted by the ratio of shortest path to agent path.
- **Trajectory Length (TL):** Total path length in meters.

### 4.3 Implementation Details

- **Framework:** PyTorch 1.10
- **GPU:** NVIDIA RTX 3060 (12 GB)
- **Batch size:** 4
- **Learning rate:** 1e-4
- **Optimizer:** Adam
- **Training epochs:** 5

---

## 5. Results and Analysis

### 5.1 Main Results

Table 1 reports the performance on the R2R val_unseen split. The results are far below those reported in the original papers.

| Method | NE ↓ | SR ↑ | SPL ↑ | TL |
|---|---:|---:|---:|---:|
| Random | 9.8 | 0.0% | 0.0 | 12.5 |
| Seq2Seq (LSTM) | 8.2 | 2.4% | 1.8 | 11.3 |
| Seq2Seq (GRU) | 7.9 | 3.1% | 2.2 | 10.8 |
| VLN-BERT (partial) | 9.1 | 0.8% | 0.5 | 13.2 |

**Analysis:** The Seq2Seq model with GRU achieved the best performance among the implemented methods, but the success rate is only slightly above random. The primary reasons for the low performance are:

- Training was limited to 5 epochs on only 2,000 episodes, whereas the original Seq2Seq baseline was trained on the full dataset for many more epochs.
- The model lacks attention mechanisms and pre-training, which are critical for grounding language in visual scenes.
- Hyperparameter tuning was minimal due to time constraints.
- The VLN-BERT model could not be fully trained because it exceeded the available GPU memory; only a partial inference was performed, yielding near-random results.

### 5.2 Ablation Study

We compared LSTM and GRU recurrent units. The GRU variant showed a slight improvement, but the difference is not statistically significant given the small training scale.

| Configuration | NE ↓ | SR ↑ | SPL ↑ |
|---|---:|---:|---:|
| LSTM | 8.2 | 2.4% | 1.8 |
| GRU | 7.9 | 3.1% | 2.2 |

### 5.3 Failure Cases

Manual inspection of failed episodes revealed several common failure modes:

1. **Looping behavior:** The agent repeatedly turns left or right without moving forward.
2. **Wrong room:** The agent navigates to an incorrect room and stops there.
3. **Premature stopping:** The agent stops before reaching the target.
4. **Collision:** The agent gets stuck against walls or furniture.
5. **Instruction neglect:** The agent ignores the language instruction and follows a generic path.

These failures indicate that the model does not effectively ground language in visual observations, likely due to insufficient training and the absence of cross-modal attention.

---

## 6. Challenges Encountered

This section documents the practical difficulties encountered during the project. As a first-year student, many of these challenges were beyond my prior experience.

- **Environment setup:** Installing Habitat and its dependencies required resolving multiple conda dependency conflicts. This process took approximately two weeks and required reinstalling the operating system twice.
- **Data acquisition:** The full R2R dataset is large, and downloading it was slow and unreliable. Only a subset of 2,000 episodes was used for training.
- **Code comprehension:** Understanding research code from GitHub was difficult due to limited documentation and complex abstractions. Several bugs were introduced when adapting the code.
- **Computational resources:** The available GPU had only 12 GB of memory, restricting batch size to 4. Training was slow and could not be scaled up.
- **Evaluation implementation:** The SPL metric was initially computed incorrectly due to a bug in the evaluation script. This was later corrected, but it consumed additional time.
- **Time management:** The project duration was two months, and concurrent coursework limited the time available for research.
- **Literature reading:** Understanding state-of-the-art papers required significant effort due to the complexity of the methods and the volume of background knowledge required.

---

## 7. Discussion

### 7.1 Key Findings

- VLN is a highly challenging task. Even a simple baseline requires substantial training data and computational resources to achieve reasonable performance.
- The absence of attention and pre-training significantly limits the model’s ability to ground language in visual observations.
- Limited training scale and epochs lead to near-random performance on unseen environments.

### 7.2 Limitations

- Only a small subset of the R2R dataset was used.
- Training was limited to 5 epochs.
- The model architecture is outdated and lacks modern components.
- No reinforcement learning fine-tuning was performed.
- No real-robot experiments were conducted.
- No demo video was produced due to time constraints.

### 7.3 Future Work

If this project were continued, the following directions would be pursued:

- Train on the full R2R dataset for more epochs.
- Implement a pre-trained model such as VLN-BERT or HAMT.
- Incorporate reinforcement learning fine-tuning to improve SPL.
- Study sim-to-real transfer for deployment on physical AMRs.
- Improve evaluation scripts and reproducibility.

---

## 8. Conclusion

This summer project provided a first-hand introduction to Vision-Language Navigation. Although the experimental results are far below the state of the art, the project successfully implemented a complete pipeline from environment setup to training and evaluation. The main outcome is a better understanding of the difficulties involved in embodied AI research and the practical skills required. I would like to thank Prof. Cui for the opportunity and the senior students in the VLN group for their guidance. I hope to continue learning and contribute more effectively in future research.

---

## References

[1] Anderson, P., et al. “Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments.” CVPR 2018.  
[2] Hong, Y., et al. “VLN-BERT: A Recurrent Vision-and-Language BERT for Navigation.” CVPR 2021.  
[3] Chen, S., et al. “HAMT: Hierarchical Vision-Language Transformer for Navigation.” NeurIPS 2021.  
[4] Chen, S., et al. “DUET: Dual-Level Vision-and-Language Navigation with Topological Maps.” CVPR 2022.  
[5] Zhou, G., et al. “NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models.” AAAI 2024.  
[6] Ku, A., et al. “Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding.” EMNLP 2020.

---

## Appendix

- Weekly reports: `docs/00_weekly.md`
- Source code: `src/`
- Repository: https://github.com/scyyx17-cyber/fury-2026-Yuhui-Xu-VLN
