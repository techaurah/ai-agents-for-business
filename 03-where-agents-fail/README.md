# Lesson 03: Where agents fail: the honest no list

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 02 · **You need:** Your audit ranking and residue list from Lesson 02.

Every vendor presentation is a list of things an agent can do. This lesson builds the opposite list, yours, in advance, while nobody is selling you anything. A process belongs on the no list when any one of three tests fails. The stakes test: a mistake could harm a person, a legal position, or a relationship that cannot be repaired with an apology and a correction. The reversibility test: the agent's actions cannot be undone, or can only be undone publicly. The judgement test: competent staff genuinely disagree about the right handling, case by case, because the right answer depends on history, tone, and context no system holds. A process failing any test is not an agent candidate today, however good the demo looks.

## The no list is a design tool, not a mood

Written down, the no list does three jobs. First, it protects the pilot: most agent disasters in small businesses are scope disasters, a system that was fine at answering questions quietly given a second job, complaints, refunds, clinical reassurance, where its failure mode changed category. Second, it gives the operator a sentence they can say under pressure: that case type is on the no list, it goes to a human, no judgement call needed at 7pm. Third, it improves the yes list: an agent whose scope explicitly excludes the dangerous residue can be given more autonomy on the safe remainder, which is where its value is. Notice that items can leave the no list over time, when a process gains structure, a human review step is added, or the stakes change. The list is reviewed monthly (Lesson 24), not carved in stone.

## Assist is not automate

Between yes and no sits the most underused option in this field: the agent assists a human who still decides. Drafting the reply a person edits and sends. Summarising the long thread before the person reads it. Preparing the quote pack the person checks. Assistance keeps the human's judgement in the loop while removing the blank page and the hunting through files, which is where much of the time actually goes. Several processes on a typical no list, complaint handling is the classic, become excellent assist candidates: the agent drafts, gathers the history, and proposes options, and a named human owns the send. When a vendor demo impresses you, ask which of its jobs are assist shaped; you may be able to buy the value without the risk category.

## The running example: BrightSmile Dental

BrightSmile's no list, written after Lesson 02's audit. Never the agent: discussing a diagnosis or reassuring a patient about symptoms (stakes test, clinical harm and false reassurance); handling a complaint about treatment (judgement test, history and tone decide everything); promising a price for treatment not yet examined (reversibility in the practical sense, a quoted figure is a commitment in the patient's mind); anything about a child's pain beyond urging prompt human contact (stakes). Assist instead: the agent drafts replies to complaints for the practice manager with the full history attached, and drafts treatment information answers that a clinician approves in a weekly batch. The lead response agent that survives this filter has a tight, bright scope: timings, prices of standard items, booking, and polite pursuit of the unanswered. Everything else is a handover.

## Run it

Run `python3 no_list.py`. Six BrightSmile jobs are filtered: two survive as agent candidates, drafting a complaint reply lands in assist only, and three are refused, each with the test it failed printed next to it. Your no list should read the same way: every refusal names its test.

## Common failures

- **Writing the no list as vibes..** Someday someone will argue a case at the boundary. A refusal that names its failed test settles the argument; a feeling does not.
- **Forgetting assist entirely..** A no list with no assist column throws away the safest value in the field and pushes people to argue for full automation instead.
- **Letting the pilot creep..** The classic failure is not a bad launch; it is month two, when the agent quietly gains a job from the no list because it seemed to be going well. Lesson 24 reviews scope against this list.

## Recap checklist

- [ ] My no list exists in writing, and every refusal names its failed test.
- [ ] I have an assist column, not just yes and no.
- [ ] I know scope creep, not launch day, is the usual way no list items get automated.

## Resources

- [Course 1, Agentic AI for Beginners](https://github.com/techaurah/agentic-ai-for-beginners)
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction)
- [Course glossary](../resources/glossary.md)
