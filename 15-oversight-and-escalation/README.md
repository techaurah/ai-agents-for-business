# Lesson 15: Human oversight and escalation: the ladder

**Time:** about 90 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 03, 14 · **You need:** Your job description and no list.

Oversight is where agent projects are won quietly or lost loudly. The model in this course is a ladder of four rungs, and every action an agent can take sits on exactly one rung, written down. Act: the agent does it and logs it, for low risk, reversible, high confidence work. Draft: the agent prepares it and a human edits and sends, for work where voice or nuance matters. Ask: the agent pauses and requests a decision before acting, for state changing or money touching steps. Escalate: the agent hands the whole case to a named human with context attached, and steps back. The ladder's power is that it converts a hundred future judgement calls into one policy decision, taken calmly, in advance, by the owner.

## Assigning rungs by risk, not by convenience

Two questions place an action. What is the worst plausible outcome if the agent does this wrong, from Lesson 02's error costing? And how visible is the error, and how fast: a wrong internal label is found at leisure, a wrong message to a customer is found by the customer. High harm or low visibility pushes an action down the ladder toward humans; low harm and instant visibility lets it climb. Confidence matters too, but carefully: an agent that reports its own uncertainty is useful signal for routing borderline cases to Draft, while an agent that is simply often confident is not evidence of anything. The policy also states the escalation service standard: an escalated case carries a summary, the original message, and what the agent already tried, and it lands with the named human inside a stated time, because an escalation that arrives as a bare forward is just the original problem with latency added.

## The policy is testable, so test it

The artifact encodes BrightSmile's policy as rules and runs cases through it, which is more than a convenience: a policy that cannot be executed by a checker is usually a policy with contradictions hiding in its prose. Testing the policy before the pilot, against Lesson 02's residue cases and Lesson 20's acceptance set later, catches the classic faults: a case type claimed by two rungs, a case type claimed by none (the gap always exists; find it on paper), and escalation destinations that name a team instead of a person, against Lesson 07's rule. Expect to revise the policy after the pilot's first week; the scorecard (Lesson 22) reviews rung assignments against the errors that actually happened, and Lesson 24 makes that review monthly. A ladder that never changes is either perfect or unread.

## The running example: BrightSmile Dental

BrightSmile's ladder, in brief. Act: acknowledge and answer standard questions from approved data, label and log every enquiry, send the single polite follow up. Draft: any reply that mentions a specific treatment's suitability, any reply to a message with mixed content (a booking plus a worry), the weekly summary to the partners. Ask: offering a slot outside normal hours, any discount or payment plan mention, contacting an enquiry through a different channel than they used. Escalate: clinical content, complaints, distress, a child in pain, anything the agent has failed at twice, anything from Lesson 03's no list, each to its named human with the full context pack. Two design notes: mixed content defaults down a rung, always, and the twice failed rule makes persistence itself an escalation trigger, because an agent retrying a confused customer is a screenshot in progress.

## Run it

Run `python3 escalation_policy.py`. Watch the two instructive cases: the booking with a symptom worry mixed in drafts rather than acts, and the ordinary price question escalates on its second failure. Both behaviours are policy, executed the same way every time.

## Common failures

- **Escalation as a forward button..** An escalation without summary, original, and attempted steps is the original problem plus delay. The context pack is part of the rung's definition.
- **Confidence as the only router..** Routing borderline cases by the model's self reported confidence alone invites the confidently wrong case to sail through. Risk and visibility place the rung; confidence only moves cases down, never up.
- **A rung nobody staffs..** Ask and escalate presume a human who answers inside a stated time. If the rota (Lesson 07) has no such human at 8pm, the policy is fiction at 8pm.

## Recap checklist

- [ ] Every action my agent can take sits on exactly one rung, in writing.
- [ ] Escalations carry a context pack and land with a named human in a stated time.
- [ ] My policy runs as a checker, and my residue cases pass through it correctly.

## Resources

- [Google and Kaggle, 5 Day AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-ai-agents)
- [Course 1, Agentic AI for Beginners](https://github.com/techaurah/agentic-ai-for-beginners)
- [Course glossary](../resources/glossary.md)
