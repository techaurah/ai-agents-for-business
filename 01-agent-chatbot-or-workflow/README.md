# Lesson 01: Agent, chatbot, or workflow: three different purchases

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 00 · **You need:** Just the lesson files. The classifier runs on the standard library.

Three kinds of software are sold under one word, agent, and they differ in price, risk, and what can go wrong by an order of magnitude. A workflow follows fixed steps in a fixed order; the rules were written by a person and the software makes no judgement calls. A chatbot answers in conversation, from a knowledge base or a fixed set of intents, and takes no actions of its own. An agent takes a goal, uses a model to decide its next steps, calls tools to act on the world, and checks its progress, inside limits a human set. The test that separates them is one question: who decides the next step, a rule, a script, or a model?

## Why the distinction is a purchasing skill

Each kind fails differently. A workflow fails loudly: a step breaks, an error appears, nothing moves. A chatbot fails in words: a wrong answer, embarrassing but usually recoverable. An agent fails in actions: it can send the wrong message to the right person, book the wrong slot, or repeat a mistake at machine speed across a hundred cases before a human notices. Supervision cost follows the failure kind. That is why the same enquiry handling job can be a cheap workflow (send an acknowledgement, create a task, alert the desk), a mid priced chatbot (answer opening hours and prices from approved text), or a genuinely more expensive agent (triage the enquiry, check the diary, propose times, draft a personal reply, escalate the ambiguous). Vendors blur the words because the agent label carries the agent price.

## The classifier, and its one hard question

The artifact in this lesson encodes the test. For any proposed system, ask three questions in order. Does it act on the world, or only answer? If it only answers, it is a chatbot, whatever the brochure says. If it acts, are its steps fixed in advance by a person? Then it is a workflow, and workflow pricing and workflow testing apply. Only if a model chooses among steps at run time, based on what it finds, is it an agent, with agent supervision requirements: an escalation policy, an acceptance test set, and a named operator, all of which this course builds. The hard question is the second one, because modern workflow tools include model steps (classify this message, summarise this thread) inside fixed flows. A model step inside a fixed flow is still a workflow: the model fills a box, it does not choose the road.

## The running example: BrightSmile Dental

A vendor offers BrightSmile an AI receptionist agent. The demo shows it answering questions about whitening prices and booking a hygiene appointment. Run the classifier on what was actually shown: the answers come from an approved price list (chatbot behaviour), and the booking follows one fixed path, check diary, offer slots, confirm (a workflow with a model step for understanding the request). Nothing in the demo had the system choosing among strategies, recovering from a surprise, or deciding what to do about an enquiry that fits no category. BrightSmile may still buy it; enquiry handling is valuable. But they should buy it at workflow-plus-chatbot value, with workflow grade testing, and they should write down the genuinely agentic part they still lack: triage of the messy enquiries that fit no template. Lesson 03 returns to exactly that residue.

## Run it

Run `python3 classify.py`. Five systems are classified by the three questions, including the trap case: a workflow with a model step inside it, which the classifier correctly refuses to call an agent. Then run the smoke test, which checks the counts.

## Common failures

- **Calling anything with a model inside an agent..** A model step in a fixed flow is a workflow. The label matters because supervision duties and honest pricing follow the kind.
- **Assuming agent is the upgrade..** For fixed, high volume work, a workflow is cheaper, faster, and easier to test than an agent. Agent is the tool for the residue that rules cannot cover.
- **Judging by the demo's best minute..** Demos show the path that works. Ask the vendor what the system does with an enquiry that fits no category; the answer reveals the kind.

## Recap checklist

- [ ] I can classify a proposed system as workflow, chatbot, or agent, and say why.
- [ ] I know a model step inside a fixed flow is still a workflow.
- [ ] I know why supervision cost follows the kind, not the label.

## Resources

- [Course 1, Agentic AI for Beginners](https://github.com/techaurah/agentic-ai-for-beginners)
- [Microsoft, AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction)
- [Course glossary](../resources/glossary.md)
