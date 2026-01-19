---
id: 1
title: Set up project constitution
stage: constitution
date: 2026-01-19
surface: agent
model: gemini-pro
feature: none
branch: master
user: Muhammad-Hammad-Abbasi
command: /sp.constitution
labels: [constitution, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
- .specify/templates/plan-template.md
tests:
- none
---

## Prompt

/sp.constitution # Project Constitution: The Evolution of Todo (Phase I)

## 1. Project Overview
This project is Phase I of "The Evolution of Todo", focusing on building a robust **In-Memory Console Application** using Python. The goal is to strictly follow Spec-Driven Development (SDD) principles.

## 2. Technology Stack & Constraints
* **Language:** Python 3.13+
* **Interface:** Command Line Interface (CLI) / Console App
* **Data Storage:** In-Memory only (Python Lists/Dictionaries).
    * *Constraint:* No external database (SQL/NoSQL) or file persistence (JSON/TXT) is allowed in this phase. Data is lost when the app exits.
* **Package Manager:** UV (if external packages are needed, though standard library is preferred for Phase I).

## 3. Architecture Principles
* **Modularity:** Code must be organized into clean, single-purpose functions (e.g., `add_task`, `view_tasks`).
* **State Management:** Global state (the list of tasks) should be managed cleanly, preferably passed as arguments or contained within a Service class.
* **Error Handling:** The app must not crash on invalid input. It should catch errors (e.g., entering text instead of a Task ID) and show friendly messages.
* **User Experience:** The application must run in a continuous loop (Interactive Menu) until the user explicitly selects "Exit".

## 4. Development Workflow (Spec-Driven)
* **Zero-Inference Rule:** AI Agents must strictly follow the requirements defined in `speckit.specify.md` and `speckit.plan.md`. Do not invent features not requested.
* **Task-Based Implementation:** No code is written unless it maps to a specific Task ID in `speckit.tasks.md`.
* **Code Style:** Follow PEP 8 standards. Use Python Type Hints (e.g., `def add_task(title: str) -> dict:`) for clarity.

## 5. Core Features (Non-Negotiable)
1.  **Add Task:** Must capture a Title (required) and Description (optional). Auto-generate a unique ID.
2.  **View Tasks:** Display ID, Title, and Status (Pending/Completed).
3.  **Update Task:** Modify Title or Description by ID.
4.  **Delete Task:** Remove task by ID.
5.  **Mark Complete:** Toggle status to "Completed".

## Response snapshot

I have set up the project constitution based on your input. I created the `.specify/memory/constitution.md` file and updated the `.specify/templates/plan-template.md` to align with the new constitution.

## Outcome

- ✅ Impact: The project constitution is now defined and the plan template is consistent with it.
- 🧪 Tests: none
- 📁 Files: 
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
- 🔁 Next prompts: none
- 🧠 Reflection: The user provided a very detailed constitution, which made the process straightforward. I was able to map the user's input to the template and update the relevant files.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
