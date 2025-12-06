---
id: 0003
title: Update Tasks for Course Modules
stage: tasks
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: physical-ai-robotics
branch: 001-physical-ai-robotics
user: unknown
command: /sp.tasks
labels: ["tasks", "update", "modules"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - D:\book\specs\001-physical-ai-robotics\tasks.md
tests:
null
---

## Prompt

```text
tasks:
  - topic: 📥 Introduction
    filename: intro.md
    requirements:
      - 600–800 words
      - Explain Physical AI & Humanoid Robotics overview
      - Academic CS tone
      - APA-style citations
      - Docusaurus-ready Markdown
      - No plagiarism

  - topic: 🤖 Module 1 – The Robotic Nervous System (ROS 2)
    filename: module1.md
    requirements:
      - 700–900 words
      - Explain ROS 2 nodes, topics, services
      - Explain URDF and Python rclpy integration
      - Academic CS tone
      - APA citations
      - Docusaurus MD format

  - topic: 🛰️ Module 2 – The Digital Twin (Gazebo & Unity)
    filename: module2.md
    requirements:
      - 700–900 words
      - Gazebo physics, gravity, collisions
      - Unity visualization, sensor simulation
      - LiDAR, IMU, depth camera explanation
      - APA citations
      - Docusaurus-ready Markdown

  - topic: 🧠 Module 3 – The AI-Robot Brain (NVIDIA Isaac)
    filename: module3.md
    requirements:
      - 700–900 words
      - Isaac Sim, synthetic data, VSLAM, Nav2
      - Academic tone
      - APA citations
      - Docusaurus MD

  - topic: 🔗 Module 4 – Vision-Language-Action (VLA)
    filename: module4.md
    requirements:
      - 700–900 words
      - Whisper voice commands → robot actions
      - LL
```

## Response snapshot

I have successfully updated the `tasks.md` file with the detailed content creation tasks for each module, incorporating the new filenames and specific requirements you provided.

**Summary of Tasks Update:**
- **Total Tasks**: 24 (renumbered from T001 to T024)
- **Phase 1 & 2**: Marked as completed based on previous actions.
- **Phase 3 (User Story 1 - Course Content Viewing)**:
    - **File Creation**: Tasks T003-T008 now reflect the new filenames (`intro.md`, `module1.md`, etc.).
    - **Content Creation**: Tasks T009-T013 are new, specific tasks for outlining and writing the content for each module, including the detailed requirements.
- **Phase 4 (User Story 2 - Weekly Breakdown Access)**: Tasks T014-T017 remain for integrating weekly breakdowns, updated with new filenames.
- **Phase 5 (User Story 3 - Assessment Task Access)**: Task T018 remains for outlining assessment tasks, updated with new filenames.
- **Phase N (Polish & Cross-Cutting Concerns)**: Tasks T019-T024 are for overall validation and polish, updated with renumbered IDs.

I have also updated your todo list to reflect these changes.

## Outcome

- ✅ Impact: Task list for course modules updated to reflect new requirements and filenames. Todo list synced.
- 🧪 Tests: N/A
- 📁 Files: 1 file modified: D:\book\specs\001-physical-ai-robotics\tasks.md
- 🔁 Next prompts: User can now proceed with /sp.implement to execute the updated tasks.
- 🧠 Reflection: Successfully handled dynamic update of task list based on new user input for `/sp.task`. Manual PHR creation was required due to script failure, which should be investigated.

## Evaluation notes (flywheel)

- Failure modes observed: `create-phr.ps1` script failed to execute on the Windows platform, requiring manual PHR creation.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Debug `create-phr.ps1` for PowerShell compatibility on Windows.