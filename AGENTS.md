# AGENTS.md

Conventions for AI assistants working in this repository. Human contributors should read CONTRIBUTING.md; this file states the same rules in machine-checkable form.

## Repository shape

- Lessons live in root folders named `NN-kebab-lesson-name`, numbered 00 to 29, matching the lessons table in README.md exactly. Never rename a lesson folder without updating README.md, llms.txt, and PROGRESS.md in the same change.
- Each lesson folder contains: `README.md` (the lesson), runnable artifacts (plain Python calculators, simulators, and checkers), `exercise.md`, and `solution/` with the worked solution.
- Root files: README.md (landing page), llms.txt (course index for AI assistants), PROGRESS.md (learner checklist), DESIGN.md (the design this repo was built to), RESEARCH.md (the competitor scan), resources/, showcase/, translations/, assets/, tools/.

## Writing rules

- Plain language, short sentences. Define every term on first use or ensure it exists in resources/glossary.md.
- No em dashes anywhere, in prose or code comments. Use commas, colons, or full stops instead.
- No invented statistics, market sizes, learner counts, or return on investment claims. A business number is allowed only as a worked example with stated assumptions, or as a sourced fact with its date.
- Do not promise certificates. The course's completion artifact is the public capstone deployment plan in the showcase.
- Lessons never sell a service. The only vendor presence is the published by line and the standard footer in the root README.

## Code rules

- Every Python artifact runs on the standard library (Python 3.11 or newer), offline, with no credentials. Framework code is discussed in prose and named accurately; it is never required to pass a lesson.
- Every JSON example must parse and pass tools/validate_course.py; capstone plan files must carry the sections the validator checks. CI runs it.
- A lesson may ship a `smoke_test.py`; CI runs every file with that name, so keep smoke tests fast, offline, and credential-free.
- All example data is fictional. No real business, customer, or patient data anywhere, including in exercises and solutions.

## Change rules

- Small fixes may go straight to a pull request. New lessons, rewritten lessons, and new translation languages start with an issue (the two-tier rule in CONTRIBUTING.md).
- If lesson titles change, update README.md, llms.txt, and PROGRESS.md together; the three must never disagree.
- Showcase rows are added by learners via PR, one row per learner, format in showcase/README.md.
