# Course design: AI Agents for Business

The design this repository was built to. Research behind it:
[RESEARCH.md](RESEARCH.md). House standard inherited from
Course 1, Agentic AI for Beginners, Course 2, AI Automation
with n8n, and Course 3, Build MCP Servers: numbered lesson
folders, every lesson a complete unit (written lesson, runnable
artifact, exercise, worked solution), no em dashes, no invented
statistics, no certificates. This course retargets the standard
from builders to the people who commission agents.

## Title and promise

**AI Agents for Business** is a free, complete course that
teaches business owners, operators, and the consultants who
advise them how to choose, scope, buy or build, pilot,
supervise, and measure an AI agent in a real business, and how
to improve it month to month or stop it honestly.

## Audience

- Owners and operators of small and medium businesses (clinics,
  agencies, home services, real estate, ecommerce, professional
  services) who are being sold agents, or selling themselves on
  one, and want judgement before budget.
- Team leads who will supervise an agent day to day: the
  operator role this course treats as a real job.
- Consultants and freelancers evaluating agents for clients,
  who need a vendor neutral method and a plan format they can
  reuse.

Not for: anyone who wants to learn how agents work inside.
That is Course 1, Agentic AI for Beginners, and this course
cross links it wherever builder depth is the honest next step.
Not for anyone shopping for a certificate. There is none; the
capstone deployment plan in the showcase is the artifact.

## Prerequisites

- No programming experience. Every artifact runs with one
  command and reads like the worksheet it models; learners who
  never open the code still get the worked numbers from the
  lesson text and the solutions.
- Business process literacy: you can describe how a job flows
  through your business today, in a spreadsheet or on paper.
- A spreadsheet tool you are comfortable in, for the costing
  and scorecard lessons (the Python twins mirror the sheets).
- Python 3.11 or newer only for running the twins yourself,
  which Lesson 00 sets up and verifies.

## The arc

One fictional business, BrightSmile Dental, a two location
dental practice first used in Course 2, carries one decision
through the course: new patient enquiries arrive by web form,
Instagram direct message, and phone, and too many wait hours
for a first reply or none at all. Across the modules the
learner audits that process, checks readiness, compares build,
buy, and managed service fairly, designs a four week pilot of
a lead response agent, writes its job description and its
escalation policy, rehearses its failures in simulation, runs
the pilot on paper, scores it honestly, and decides what month
two looks like. The capstone then repeats the whole motion on
a process from the learner's own business, producing a
complete deployment plan: readiness audit, pilot design,
oversight plan, and scorecard.

## Lesson map: 30 lessons, 9 modules

### Module 0: Start here

| # | Lesson | Builds |
|---|--------|--------|
| 00 | Course setup: what you need, and how this course works | A verified setup and the course honesty rules |
| 01 | Agent, chatbot, or workflow: three different purchases | A classifier for vendor claims |

### Module 1: Where agents pay off, and where they do not

| # | Lesson | Builds |
|---|--------|--------|
| 02 | The opportunity audit: finding the work an agent can carry | A scored audit of your own processes |
| 03 | Where agents fail: the honest no list | A filter that kills bad candidates early |
| 04 | Mapping a process before you automate it | A step map with decision points marked |

### Module 2: Readiness: data, access, people

| # | Lesson | Builds |
|---|--------|--------|
| 05 | Data readiness: what the agent may read, and whether it is true | A data inventory with a quality grade |
| 06 | Access readiness: accounts, tools, and least privilege | An access plan that gives the agent only its job |
| 07 | People readiness: owners, operators, and the team that lives with it | A roles sheet with a named operator |

### Module 3: Build, buy, or managed service

| # | Lesson | Builds |
|---|--------|--------|
| 08 | Build versus buy versus managed service: the fair comparison | A route decision with reasons recorded |
| 09 | The framework landscape, in plain language | A shortlist you can defend to a non technical partner |
| 10 | Evaluating a vendor or a platform: the demo is not the product | A scored vendor evaluation with traps marked |
| 11 | The honest cost worksheet: build, run, supervise, fix | A total cost model with assumptions stated |

### Module 4: Designing the pilot

| # | Lesson | Builds |
|---|--------|--------|
| 12 | Scoping a pilot that can actually answer the question | A pilot scope with edges drawn on purpose |
| 13 | Baselines and success metrics: measure before you automate | A baseline sheet and a target you chose in advance |
| 14 | The agent job description: task, tools, limits, tone | A one page spec a builder or vendor can price |

### Module 5: Oversight, risk, and trust

| # | Lesson | Builds |
|---|--------|--------|
| 15 | Human oversight and escalation: the ladder | An escalation policy a checker can test |
| 16 | Security basics: what an agent must never be able to do | A threat list for your own process, with controls |
| 17 | Privacy and compliance basics for owners | A disclosure and data handling checklist |
| 18 | The failure catalogue: how agents go wrong in businesses | A rehearsed response for each likely failure |

### Module 6: Running the pilot

| # | Lesson | Builds |
|---|--------|--------|
| 19 | Pilot simulation: the lead response twin | A rehearsal of the pilot week, offline |
| 20 | Testing before trust: the acceptance set | A test set that must pass before real customers |
| 21 | Rollout: training the team and the first two weeks | A rollout plan with a daily review rhythm |

### Module 7: Measure, decide, improve

| # | Lesson | Builds |
|---|--------|--------|
| 22 | Reading the pilot scorecard | A verdict: scale, fix, or stop, with evidence |
| 23 | Unit economics: what one handled enquiry really costs | A per outcome cost you can compare to the manual way |
| 24 | The monthly improvement loop | A review routine that compounds small fixes |
| 25 | Expand, hand over, or stop: the second decision | A decision record for what happens after a pilot |

### Module 8: Capstone: your agent deployment plan

| # | Lesson | Builds |
|---|--------|--------|
| 26 | Capstone spec: the deployment plan, fixed in advance | The plan format and its four gates |
| 27 | Build the plan: readiness, pilot, oversight | The complete plan for your own process |
| 28 | Stress test the plan: red team your own deployment | A plan that survives its failure catalogue |
| 29 | Ship it: present, publish, and showcase your plan | The finished plan, reviewed and shared |

## Visuals

Generated by assets/visuals/generate_visuals.py in the Academy
style family (white canvas, navy primary, light blue secondary,
cyan arrows, amber gates):

| Diagram | Teaches | Used in |
|---|---|---|
| course-map.svg | Nine modules, one decision, one plan | README |
| three-kinds.svg | Agent, chatbot, and workflow, and who decides each step | Lesson 01 |
| opportunity-matrix.svg | Volume against judgement: where agents fit | Lessons 02, 03 |
| readiness-triangle.svg | Data, access, people: all three or not yet | Lessons 05 to 07 |
| three-routes.svg | Build, buy, managed service, honestly compared | Lesson 08 |
| oversight-ladder.svg | Act, draft, ask, escalate: autonomy by risk | Lessons 15, 26 to 28 |
| capstone-flow.svg | Audit, pilot, supervise, score: the plan in order | Lessons 26 to 29 |

## Rules the build followed

- Every framework or product claim names its source or its
  observation date (RESEARCH.md), and fast moving facts (a
  framework's maintenance status, a regulation's dates) carry
  their date in the lesson.
- No third party prices anywhere. Tool and platform pricing
  changes too often to teach; Lesson 11 teaches the learner to
  price their own shortlist on the day, in the worksheet.
- Every business number is a worked example with assumptions
  stated, using the fictional BrightSmile Dental or the
  learner's own figures. Nothing is presented as a market
  statistic.
- Every lesson folder complete on delivery: no stubs anywhere.
- All JSON examples parse and pass tools/validate_course.py;
  all smoke tests pass offline; relative links pass
  tools/check_links.py; em dash count is zero repo wide.
