# Bayesian Study Planner: Agent Instructions

## Project
- This is a small, individual Python coursework project, not a production application.
- Follow the existing `src/`, `tests/`, and `docs/` structure. Keep solutions simple and easy to explain in a presentation.
- Use `pgmpy` for Bayesian inference and the Google Calendar API for scheduling. Prefer the Python standard library for everything else.
- The planned network has 10 variables: difficulty and mastery for each of three concepts, stress, exam urgency, study action, and exam success.
- The available actions are intense study (5 hours), moderate study (2–3 hours), light review (1 hour), and rest (no session).

## Scope and approvals
- Implement only the task explicitly requested in the current prompt. Do not add optional features or work on future project weeks.
- Before editing, state the files you intend to change and a short plan.
- Limit each task to at most three edited files and approximately 120 added lines total. If more is necessary, explain why and ask to split or approve the larger change before editing.
- Do not create new dependencies, directories, frameworks, configuration files, or abstractions unless the requested task requires them.
- Do not refactor unrelated code, rename files, remove working functionality, or change public interfaces without approval.
- Do not commit, push, install packages, or modify a real calendar without explicit permission.
- If a requirement is ambiguous, ask rather than inventing behaviour.

## Coding style
- Prefer the simplest correct and efficient implementation. Avoid overengineering, unnecessary classes, wrappers, helpers, and duplicated logic.
- Write short, readable Python functions with descriptive names. Keep files focused and changes minimal.
- Use type hints where they make behaviour clearer, but avoid excessive type checking or defensive code for impossible inputs.
- Do not add code comments or docstrings unless specifically requested. Explain non-obvious choices in `docs/` when asked.
- Reuse installed dependencies and existing project patterns.

## Bayesian model requirements
- Keep the network at 10 variables or fewer and model at least three concept difficulties.
- Keep model structure, handcrafted CPTs, inference, utility calculations, and calendar integration as separate tasks.
- Use a built-in `pgmpy` inference algorithm; do not implement inference from scratch.
- Make probabilities and utility parameters explicit, documented, and testable. Do not claim invented probabilities are measured data.
- Compare expected utility for every available action and select the highest-utility action. Balance exam success against stress.
- Demonstrate distinct scheduling outcomes for different student scenarios when simulation is requested.

## Testing and reporting
- Add or update only tests relevant to the requested change.
- When possible, run `python -m unittest discover -s tests -v` and report the result honestly.
- At the end, summarise changed files, test results, and any unfinished work. Never claim unrun tests passed.
- Do not expose or commit `credentials.json`, `token.json`, `.env`, or any OAuth secrets.

## Current phase
- Week 8: repository setup, network structure and variable definitions, and preparation for Google Calendar authentication.
- Do not implement full CPTs, probabilistic inference, expected utility, or live calendar event creation until their scheduled tasks are explicitly requested.
