# Lesson 09: The framework landscape, in plain language

**Time:** about 75 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 08 · **You need:** Your route decision from Lesson 08.

If Lesson 08 pointed you at build, or at a vendor who builds, you will hear framework names within the hour. This lesson gives you the buyer's translation. A framework is a code library that gives builders the agent's working parts: the loop that alternates thinking and acting, places to keep state between steps, wiring to tools, and hooks for human approval. Frameworks do not supply the model, the business rules, the evaluation set, or the supervision; those remain yours on every route. What a framework choice does decide is how state and approvals are handled, how locked in you are, and how large the pool of people is who can maintain the result. Facts in this lesson were checked against current sources on 2026-11-06 and RESEARCH.md records them; the field moves fast, so the lesson teaches the questions as well as the current answers.

## The names you will hear, translated

LangGraph (from LangChain) models an agent as a graph of steps with explicit, durable state, checkpoints, and built in points where a human can interrupt and approve; guides surveyed for this course consistently pick it when a process has clear steps, approvals, and an audit trail to keep. CrewAI describes agents by role and goal in crews that work through tasks, plus flows for structured execution; its role language is the easiest for a business team to read in a design document, and it is a common fast route to a working prototype. Microsoft's line needs a date stamp: AutoGen, the multi agent framework many older guides recommend, is in maintenance mode, and Microsoft directs new projects to Microsoft Agent Framework (generally available April 2026, open source), so a proposal that says AutoGen in late 2026 owes you an explanation. Around these sit platform agent builders (your CRM or helpdesk's own AI features) and the Model Context Protocol, which standardises how agents use tools, and which Course 3 teaches building.

## What to ask, whoever builds

Four questions cut through framework marketing, for an in house build and a vendor alike. Where does the state live: if the agent forgets everything between messages, multi step work and handovers will hurt, and the answer is a diagram, not an adjective. Where do approvals live: which actions pause for a human, and is that a framework checkpoint or a hopeful prompt instruction (Lesson 15 explains why only the first counts). How do we test a change: a saved set of cases run after every edit (Lesson 20), or a shrug and a demo? And what does migration cost: if this framework is abandoned or repriced, what exactly do we carry away? A builder who answers all four crisply has done production work. A builder who answers with star counts has done reading.

## The running example: BrightSmile Dental

BrightSmile, on the managed route, will never import a framework, and still uses this lesson twice. First, in vendor evaluation (Lesson 10): both finalists were asked the four questions, and one answered the approvals question with framework checkpoints in its orchestration layer, while the other described a prompt that tells the agent to be careful, which Lesson 15 will teach you to score as no control at all. Second, in the contract: the chosen provider's stack is recorded in the decision file, with the migration answer (enquiry history and the approved knowledge base export in standard formats) written as a clause. The practice still could not code a line of it. It did not need to. It needed to know which answers were load bearing.

## Run it

Run `python3 framework_map.py` for the four entries and the four questions in one screen. Take the questions to your next vendor call; the map is the crib sheet, not the point.

## Common failures

- **Ranking frameworks by popularity..** Star counts measure attention, not fit for your approvals, state, and exit needs. The four questions outrank every league table.
- **Repeating an out of date recommendation..** AutoGen's maintenance status is the standing example: any framework claim older than a season needs rechecking before it goes in a plan.
- **Believing the framework supplies governance..** Across the guides surveyed, no framework is a complete governance layer. Permissions, approvals, audit, and evaluation are designed by someone; make sure the proposal names who.

## Recap checklist

- [ ] I can translate the main framework names into shape, fit, and watch out.
- [ ] I have four questions I will ask any builder or vendor, verbatim.
- [ ] I know which framework facts carry dates and need rechecking.

## Resources

- [LangChain documentation](https://docs.langchain.com)
- [CrewAI documentation](https://docs.crewai.com)
- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [Microsoft, AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
