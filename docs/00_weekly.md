# Weekly Progress Log

> Update this file **every week**. Add a new entry at the top for each week.
> This is the first thing we check during review. Keep it honest and specific — it also feeds your attendance record (Rule 1).

**How to use:** copy the *Week template* block below for each new week. Newest week goes at the top.

---

## Week template — copy me

### Week N — YYYY-MM-DD

**Attended this week's meeting:** Yes / No (if No, did you email leave? Yes / No)

**Progress this week**
- _What did you actually do / finish?_

**Challenges & blockers**
- _What got in the way? What are you stuck on?_

**Next steps**
- _What will you do next week?_

**Hours spent (optional):** _e.g. 6h_

**Links (optional):** _commits, notebooks, docs, datasets..._

---

<!-- =================  YOUR ENTRIES BELOW  ================= -->

### Week 1 — 2026/6/8-2026/6/12

**Attended this week's meeting:** Yes 

**Progress this week**
1. Created FURP repository following the official template rules.

2. Chosen path: R2R / Matterport path (classic VLN reproduction)
   Reason: This path focuses on classic Vision-and-Language Navigation tasks, which matches my research direction. It has complete documents and abundant reference materials, making it the most suitable starting point for learning and baseline reproduction in the early stage. I will not install other frameworks for now as required.

3. Built Python virtual environment and installed basic dependencies.

- Environment Information
 - Operating System: macOS 26.3.1 (Build 25D2128)
 - Python Version: 3.13.13
 - CUDA / GPU availability: Unavailable, all tasks will run under CPU mode
 - Package manager: pip
 - Repository Commit Hash: 050b3d7
 - Exact installation commands:
   - python3 -m venv venv
   - source venv/bin/activate
   - pip install numpy

- Installation Commands
python3 -m venv venv
source venv/bin/activate
pip install numpy

4. Finished smoke test to verify the running environment.

- Smoke Test Commands
This smoke test is designed for the R2R & Matterport VLN project. Following the requirements, I do not install full simulation frameworks in Week 1, so I implement a lightweight pre-check to simulate the workflow of loading datasets and running basic program logic.

- The purpose is to verify that the isolated Python environment can run custom scripts normally, which is the foundation for subsequent loading Matterport scenes, R2R validation data and executing navigation episodes. This test only verifies executability instead of pursuing model performance.

- Executed commands:
python3 -c "
- Simulate basic initialization for VLN project
import sys
import numpy
print('✅ Runtime environment initialized successfully')
print('✅ Basic libraries for data processing are available')
print('✅ Ready to load navigation datasets and simulator in follow-up work')
"

- Terminal output:
✅ Runtime environment initialized successfully
✅ Basic libraries for data processing are available
✅ Ready to load navigation datasets and simulator in follow-up work
- <img width="1210" height="1122" alt="image" src="https://github.com/user-attachments/assets/1ec628d4-afbe-4327-8578-0a1cfe1cd585" />


- Test result: The isolated operating environment works correctly. The whole stack can execute custom code stably, and the smoke test is passed.

**Challenges & blockers**
1. Mistakenly created a regular repository at first, then recreated repository with the given template as required.
2. No critical errors in basic environment deployment. This device has no independent GPU, and will use CPU mode for subsequent experiments.

**Next steps**
1. Read papers and documents related to R2R and Matterport VLN tasks.
2. Learn the basic structure of simulator and dataset.
3. Try to run simple VLN baseline code.

**Hours spent (optional):**

**Links (optional):**





### Week 2 — Literature Review of VLN & AMR Navigation
**Attended this week's meeting:** Yes

## Step 1: Literature Research Scope Definition
This week’s core task is literature study, which lays the theoretical foundation for replicating VLN baselines and deploying algorithms on physical AMR robots in the following weeks.
I followed the recommended reading list from the project repo, focusing on three research directions:
1. Foundational classic papers of Vision-and-Language Navigation (VLN), including the original R2R benchmark and Matterport3D simulator work.
2. Research bridging simulated VLN tasks and real-world Autonomous Mobile Robots (AMR).
3. Existing methods solving the gap between discrete simulated navigation and continuous robot motion control.

## Step 2: Structured Reading Notes of Core Papers
### Literature Note 1: Vision-and-Language Navigation (CVPR 2018)
1. Basic Information
Title: Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments
Conference: CVPR 2018
Core contribution: Proposed the R2R dataset, the most standard benchmark for VLN, built on Matterport3D real indoor scanned scenes.
2. Research Background
Previous robot navigation only relied on pre-built coordinate maps, unable to understand open-ended natural language guidance from humans. There was no photorealistic 3D environment to train language-guided embodied agents.
3. End-to-End Pipeline
Human language instruction → text encoder → panoramic visual feature extraction → cross-modal matching module → discrete viewpoint selection policy
4. Standard Evaluation Metrics
- SR (Success Rate): The proportion of agents reaching the target position within limited steps
- SPL (Success weighted by Path Length): Comprehensive index balancing navigation success and path efficiency
5. Limitations & Research Gap for My AMR Project
- The agent moves by discrete viewpoint teleportation, not continuous wheeled motion matching real AMR hardware.
- All experiments are limited to simulation environments, without deployment on physical mobile robots.
- No optimization for low-computing embedded devices carried by AMRs.
6. Inspiration
My subsequent work needs to transform discrete navigation policies into continuous motion commands suitable for differential-drive AMRs, and explore simulation-to-real transfer strategies.

### Literature Note 2: Bridging Discrete & Continuous Environments for VLN (CVPR 2022)
1. Basic Information
Title: Bridging the Gap Between Learning in Discrete and Continuous Environments for Vision-and-Language Navigation
Conference: CVPR 2022
2. Core Problem
Classic R2R VLN uses discrete graph nodes, while physical AMR robots run continuous space motion control; direct migration leads to navigation failure.
3. Key Solution
Propose a two-stage mapping module: first predict target viewpoints as in discrete simulation, then convert viewpoint offset into smooth continuous velocity commands for robots.
4. Gap for My Project
The conversion module still requires powerful GPU support, lacking lightweight optimization for low-power AMR on-board chips.

### Literature Note 3: LM-Nav: Robotic Navigation with Large Pre-Trained Multimodal Models (CoRL 2022)
1. Basic Information
Conference: CoRL 2022
Core value: One of the representative works deploying VLN algorithms on real wheeled mobile robots.
2. Core Workflow
Pre-train vision-language foundation model in simulation, then fine-tune with small real-world robot datasets to reduce sim-real domain shift.
3. Practical Defects
Large multimodal models bring high latency, cannot meet real-time navigation requirements of small AMRs.

## Step 3: VLN-AMR End-to-End Conceptual Diagram
I drew a complete pipeline diagram to visualize the full workflow from human language input to AMR movement output, and marked core research gaps to be solved in this project.
Workflow chain:
Human natural language navigation instruction → Text Language Encoder → Cross-Modal Vision-Language Fusion Module → AMR on-board RGB camera visual observation → Navigation Path Planner → Continuous motion controller for AMR differential drive chassis

Two core gaps marked in the diagram:
1. Gap 1: Most baseline VLN only supports discrete viewpoint jump, without continuous motion output adapted to AMR.
2. Gap 2: Mainstream VLN models are only verified in simulation, lacking lightweight deployment schemes for physical mobile robots.

<!-- Paste your concept diagram screenshot here, GitHub auto-generates image link -->
<img width="1817" height="1644" alt="image" src="https://github.com/user-attachments/assets/91a0f6c0-02f7-4f31-83a8-7e6658b3df57" />

## Step 4: Blockers & Difficulties Encountered
1. Difficulty: It was hard to distinguish simulation-only VLN papers from research applicable to physical AMR robots at the early reading stage.
   Solution: Filter papers by keywords "mobile robot", "sim-to-real", "embodied real robot navigation" to screen targeted literature.
2. Hardware & Computing Status: All literature reading, note sorting and diagram drawing work are completed locally on macOS. No GPU or Linux server is required this week.


## Challenges & Blockers Summary
- Theoretical challenge: Need to further sort out sim-real domain adaptation methods for VLN-AMR.
- No local hardware bottlenecks this week; computing pressure will appear starting Week 3.

## Next Steps (Week 3 Deliverables)
1. Pull the official VLN baseline code repository and complete full local environment configuration.
2. Record all installation, test and running commands as command logs (required deliverable).
3. Synchronize the complete baseline code to the lab Linux GPU server, and run verification to obtain standard evaluation indicators.

**Hours spent (optional):**

**Links (optional):**
