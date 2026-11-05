# Lesson 04: Mapping a process before you automate it

**Time:** about 90 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 02 to 03 · **You need:** Your winning process from Lesson 02 and someone who does the job today, for twenty minutes of questions.

You cannot scope an agent for a process you cannot draw. The map this lesson teaches fits on one page and has only four kinds of mark: steps (what happens), decisions (where a person chooses a path, and by what rule of thumb), waits (where work sits, and for how long), and handovers (where responsibility moves between people or systems). Most processes, mapped honestly, hold two surprises. The first is how much of the total time is waits, not work; work that takes nine minutes end to end often spans two days elapsed. The second is how many decision points run on rules nobody wrote down, known only as how Sarah handles those. An agent project is, half of it, writing Sarah's rules down.

## Mapping with the person who does the work

Map from real cases, not from the procedure manual. Take five recent, ordinary instances of the process and walk each through with the person who handled it, noting every step they actually took, including the detours: checking a second system, asking a colleague, waiting for a reply, reformatting something by hand. The manual describes the process the business wishes it had; the agent will meet the real one, including the enquiry that arrives as a photo of a handwritten note. Mark waits with real durations from timestamps where you have them. Mark each decision with the decider's actual rule of thumb, in their words. Where two staff members give different rules for the same decision, mark that too; it is a finding, not an embarrassment, and it predicts exactly where an agent would guess inconsistently.

## What the map decides

A finished map settles the pilot design before it starts. The steps before the first decision are usually pure workflow, automatable with rules at workflow prices. The decision points with a writable rule of thumb are the agent's job description in embryo (Lesson 14 writes it formally). The decision points with no writable rule are escalation points, and their frequency, countable from your five cases, predicts the operator's workload better than any vendor estimate. And the waits are the business case in its honest form: if the map shows enquiries waiting an average of five hours for a nine minute handling, the value of the agent is the wait it removes, which Lesson 13 will teach you to baseline and Lesson 22 to verify, rather than a fantasy about staff replaced.

## The running example: BrightSmile Dental

BrightSmile's enquiry map, from five real (fictionalised) cases. Step one, enquiry lands in one of three inboxes, wait begins. Step two, someone notices, average wait five hours in the sample, longest overnight. Step three, read and sort: decision one, is this a standard path (checkup, price of a standard item, directions and hours) or not; rule of thumb, if I can answer from the price list and the diary, it is standard. Step four, check the diary in a second system, two minutes of actual work. Step five, reply, decision two, if they asked anything clinical or emotional, hand to the practice manager, that is a handover with its own wait. Step six, if no reply in a day, decision three, chase once, politely, then stop. Total work, about nine minutes. Total elapsed, up to a day. The agent's job is steps three to six on the standard path, with decision two as its escalation rule.

## Run it

Run `python3 process_map.py` for BrightSmile's map in text form: eight stages, three decisions, one handover, eight hours of waiting around nine minutes of work. Your map will differ; the four kinds of mark and the surprises will not.

## Common failures

- **Mapping the manual instead of the work..** The procedure binder is a wish. Map five real cases with the person who handled them, detours included.
- **Leaving waits unmeasured..** An unmeasured wait cannot become a baseline (Lesson 13) or a verified improvement (Lesson 22). Timestamps exist in your inboxes today; use them.
- **Hiding the unwritten rules..** A decision point where staff disagree on the rule is the single best predictor of agent inconsistency. Mark it in red, do not average it away.

## Recap checklist

- [ ] My process is mapped on one page with steps, decisions, waits, and handovers.
- [ ] Every decision carries its decider's actual rule of thumb, in their words.
- [ ] I can point at the waits, and say what removing them is worth.

## Resources

- [Course 2, AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n)
- [Course glossary](../resources/glossary.md)
