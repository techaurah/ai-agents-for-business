# Lesson 02: The opportunity audit: finding the work an agent can carry

**Time:** about 90 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 00 to 01 · **You need:** Your process list from the Lesson 00 exercise, and honest counts or estimates, labelled as estimates.

Agents pay off in a specific shape of work, and the audit exists to find that shape in your business before any vendor does it for you, in the direction of their product. The shape has four features. The work happens often enough that handling it badly costs real money or real customers. Someone waits on it, so speed has value. The judgement involved is real but bounded: a competent person follows recognisable patterns, handles most cases the same few ways, and knows which cases are the exceptions. And the cost of an occasional mistake is recoverable, a corrected message or a rebooked appointment, not a harmed patient or a breached contract. Score every candidate process on those four, and the ranking usually surprises the person who commissioned the audit.

## The four scores, and why each is there

Volume, counted per week from your own tally or system, never from a brochure. Waiting cost: who waits, and what a slow answer loses; an enquiry answered tomorrow is often a customer choosing someone else today, which you can sometimes verify from your own lost enquiry notes. Bounded judgement: sample twenty real cases and sort them into the paths a good staff member actually took; if three paths cover almost all of them and the rest are visibly odd, judgement is bounded. If every case is its own negotiation, it is not, yet. Error cost: the worst plausible mistake the agent could make on this process, priced honestly. A process with a catastrophic worst case does not get a better score for being interesting; it gets Lesson 03's filter first.

## What the audit usually finds

In most small businesses the winner is unglamorous: first response and follow up on enquiries, appointment logistics, review requests and replies, invoice chasing, intake form completion, status updates customers ask for repeatedly. The losers are equally consistent: the owner's own judgement calls, complaint resolution for unhappy customers, anything involving a vulnerable person, and the process nobody can currently describe. The audit's second product matters as much as its ranking: the list of processes that failed on error cost or unbounded judgement is your no list seed, and Lesson 03 sharpens it. Keep both lists. A vendor conversation that starts from your audit sounds completely different from one that starts from their demo.

## The running example: BrightSmile Dental

BrightSmile's audit, computed by this lesson's artifact from the front desk's own two week tally, doubled. Enquiry first response: 90 enquiries a week, patients wait, three paths cover the sampled cases (book a checkup, ask about a treatment price, everything else to a human), worst mistake a clumsy first reply, recoverable. Score: the clear winner. Recall reminders for six month checkups: high volume but fixed steps and no judgement, a workflow, not an agent, and cheaper for it. Treatment plan explanations: low volume, deep judgement, high error cost if a clinical detail is wrong; it ranks last and goes to the no list. The audit did in an afternoon what three vendor demos had not: it separated one agent job from one workflow job from one never job.

## Run it

Run `python3 audit.py`. It scores BrightSmile's five candidate processes and ranks enquiry response first and treatment explanations last. The scoring is deliberately simple; the discipline is in the inputs, which must be your counts and your samples, not the defaults.

## Common failures

- **Scoring from impressions instead of a sample..** Bounded judgement is a claim about real cases. Sort twenty actual cases into paths before you score it, or the audit is astrology.
- **Letting volume dominate..** The highest volume process at BrightSmile needs no judgement at all. Volume without judgement is a workflow purchase, priced differently.
- **Softening the error cost of a favourite..** Score the worst plausible mistake, not the average one. Lesson 03 exists for processes whose worst case you flinched from here.

## Recap checklist

- [ ] I have scored at least four of my own processes on all four factors.
- [ ] My volume figures are my counts, or labelled estimates.
- [ ] I have a ranked winner and a seed for my no list.

## Resources

- [Course 2, AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n)
- [Google and Kaggle, 5 Day AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-ai-agents)
- [Course glossary](../resources/glossary.md)
