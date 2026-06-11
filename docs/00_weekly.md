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
