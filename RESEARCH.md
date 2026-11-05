# Competitor research: learning to use AI agents in a business

Written 2026-11-06, before any lesson was drafted, per the
TechAurah GitHub programme rule: competitor research first,
always. Every fact below was observed in web search results or
pages fetched on that date. Star counts and programme details
are point in time observations from the named source, not live
guarantees, and where a claim is a vendor claim rather than a
verified fact, that is recorded.

## The builder courses: excellent, and aimed at someone else

- **Microsoft, AI Agents for Beginners** (github.com/microsoft/
  ai-agents-for-beginners): the largest free agent curriculum in
  this scan. Eighteen lessons with written material and Python
  samples, covering design patterns, tool use, agentic RAG,
  planning, multi agent systems, trustworthy agents, the MCP
  and A2A protocols, context engineering, memory, computer use
  agents, and securing agents (course guide at taku.ai and the
  course site at microsoft.github.io, read 2026-11-06). One
  review observed it at about 78k stars. Samples use the
  Microsoft Agent Framework with Microsoft Foundry and need an
  Azure account for the full path. Strength: unmatched builder
  depth for free. Gap for us: it teaches people who write code
  how agents work. It does not teach an owner how to decide
  whether her business should have one, what it should cost,
  or how to supervise it.
- **Hugging Face AI Agents Course** (huggingface.co/learn/
  agents-course): free, self paced, five units plus three
  bonus units. Unit 1 covers agent fundamentals (tools,
  thoughts, actions, observations), Unit 2 teaches smolagents,
  LlamaIndex, and LangGraph side by side, Unit 3 is a use case,
  Unit 4 is a final assignment scored on a benchmark, and the
  bonus units cover fine tuning for function calling,
  observability and evaluation, and agents in games. It issues
  a free certificate of fundamentals and a certificate of
  completion. Strength: the best free framework tour. Gap: the
  learner is a builder throughout, the capstone is a benchmark
  score, and no unit asks what the agent is worth to a business
  or who watches it on a Tuesday.
- **Google and Kaggle, 5 Day AI Agents Intensive** (Kaggle
  Learn Guide, reported by KDNuggets, read 2026-11-06): five
  days pairing whitepapers with codelabs on Gemini and the
  Agent Development Kit. Day 1 asks when a task needs an agent
  at all versus a simpler workflow, Day 2 covers tools and MCP
  including human in the loop approval, Day 3 context
  engineering and memory, Day 4 agent quality (logging,
  tracing, metrics, evaluation), Day 5 prototype to production.
  A refreshed vibe coding run ran in June 2026. Strength: the
  Day 1 question and the Day 4 quality day are exactly right.
  Gap: five days, one vendor stack, builder audience, and the
  production day ends at deployment, not at month three of
  running the thing and paying for it.
- **Anthropic and platform academies** (Claude Academy,
  OpenAI's ChatGPT for Small Business programme, reported by
  ASBN, read 2026-11-06): vendor run training, increasingly
  including in person small business academies and partner
  agent lists. Strength: reach and product fluency. Gap: the
  curriculum is the vendor's product surface; an owner learns
  one tool deeply and vendor neutral judgement not at all.

## The business owner courses: right audience, thin method

- **Course Parse, AI for Business Owners** (courseparse.com):
  a free reading and projects course for owners of shops,
  agencies, and clinics, covering a one week time audit, brand
  voice marketing, customer service and reviews, quotes and
  follow ups, admin, hiring, research, automations and buying
  AI tools, and a one page AI policy. Strength: it is the
  closest audience match in this scan, and its time audit
  opening is good practice this course also uses. Gap: agents
  get one module of nine; there is no pilot design, no
  oversight ladder, no costing worksheet, and no capstone plan
  a learner could hand to a vendor or a team.
- **No code agent courses** (for example the MindStudio based
  Build No Code AI Agents course listed on course aggregators):
  five hours of video teaching one platform's agent builder
  for sales, ecommerce, and support, with a certificate.
  Strength: fast to a first demo. Gap: the skill taught is the
  platform; when the platform changes its pricing or its
  builder, the learning expires, and supervision, escalation,
  and measurement are largely absent.
- **Operator masterclasses** (for example The Agent Ops
  Masterclass at club.reinventing.ai: 48 lessons in three
  parts, part 1 free, the rest paid, with a library of systems
  to resell): aimed at would be agent operators selling
  deployments to businesses, covering guardrails, approval
  gates, onboarding, and pricing an engagement. Strength: it
  names the operator role, which this course also treats as
  real. Gap: it is a paid club with a resale library; nothing
  is forkable, runnable, or inspectable before paying, and the
  buyer of agents (the business owner) is the audience's
  customer, never the learner.

## Framework business guides: accurate parts, no whole

Sources: framework comparison guides at cordum.io, dev.to,
doomshell.com, and blckalpaca.at, read 2026-11-06.

- **LangChain and LangGraph** (LangChain Inc.): LangChain is
  the broad integration framework for LLM applications;
  LangGraph is the low level orchestration layer for stateful,
  long running agents with checkpoints and human in the loop
  interrupts. Multiple guides pick LangGraph when durable
  state and approvals matter most.
- **CrewAI**: role based crews and event driven flows, Python,
  the fastest route to a readable multi agent prototype, and
  the mental model non engineers find easiest to follow in a
  demo. One widely repeated adoption figure in vendor material
  was flagged by a source in this scan as an unaudited company
  claim; this course repeats no such figures.
- **AutoGen and Microsoft Agent Framework**: AutoGen pioneered
  conversational multi agent patterns and is now, per
  Microsoft's roadmap as reported in this scan, in maintenance
  mode, with Microsoft Agent Framework (general availability
  April 2026, MIT licensed, Python and .NET) as the recommended
  successor. A business guide that still says "start with
  AutoGen" without that note is already out of date.
- **The honest shared finding**: across the comparison guides,
  no framework is a governance layer by itself. Permissions,
  approval states, audit evidence, and an evaluation set are
  work the buyer still owns. That sentence is, in effect, this
  course's syllabus.

## Regulation, at the level an owner needs

Sources: EU AI Act explainers from Taylor Wessing, the AI
Policy Desk, and Alice, read 2026-11-06. The EU AI Act
(Regulation (EU) 2024/1689) regulates AI systems by risk and,
separately, general purpose AI models. General purpose AI
provider obligations have applied since 2 August 2025, the
Commission's enforcement powers since 2 August 2026, and
transparency duties (telling people they are interacting with
AI, marking AI generated content) took effect in August 2026,
while most high risk system obligations were deferred by the
2026 Digital Omnibus to December 2027 and August 2028. A small
business that buys an agent is usually a deployer, not a model
provider, but deployer duties, disclosure duties, and ordinary
privacy law still apply. Lesson 17 teaches exactly that slice,
with a plain instruction to get professional advice for
anything beyond it.

## Gaps we can beat

1. **Nobody teaches the buying and running of agents as one
   discipline.** Builder courses end at deployment. Owner
   courses end at a demo and a tools shopping list. The space
   between, choose, scope, pilot, supervise, measure, improve
   or stop, is where businesses actually succeed or waste
   money, and it is unoccupied by a free, complete course.
2. **No forkable, runnable course for operators.** The owner
   courses are video and reading on platforms. A repository
   course where the fork is the workbook, every claim has a
   calculator or simulator behind it, and the capstone is a
   deployment plan for the learner's own process does not
   exist yet for this audience.
3. **Honest costing is missing everywhere.** Vendor material
   leads with unaudited adoption and savings claims. A course
   that forbids invented numbers, states every assumption next
   to every worked example, and teaches total cost (build,
   run, supervise, fix) as a worksheet earns trust the hype
   cannot.
4. **Oversight is taught as a feature, not a job.** Approval
   gates appear in builder courses as a framework interrupt.
   For an operator, oversight is a rota, an escalation policy,
   a failure catalogue, and a monthly review. That operational
   treatment is this course's centre of gravity.
5. **Build, buy, or managed service is rarely compared
   fairly.** Platform courses sell building on their platform;
   agencies sell managed services. A vendor neutral comparison
   with the questions to ask each route, written by a programme
   that publishes its reasoning, is a genuine gap.

## The differentiation this course takes

See DESIGN.md for the full design. In short: the Course 1 to 3
house standard, retargeted from builders to the people who
commission, pay for, and supervise agents. Thirty lessons in
nine modules. One fictional business, BrightSmile Dental,
carries one agent decision through the whole course. Every
lesson is a complete unit with a plain Python calculator,
simulator, or checker on the standard library, one exercise,
and a worked solution. No framework is required, no number is
invented, no certificate is promised; the completion artifact
is the learner's own agent deployment plan, indexed in the
course showcase.
