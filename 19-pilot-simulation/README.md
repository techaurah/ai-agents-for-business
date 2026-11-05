# Lesson 19: Pilot simulation: the lead response twin

**Time:** about 90 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 12 to 15, 18 · **You need:** Your pilot scope and escalation policy.

Before the pilot meets a real customer, it meets a simulated week. The twin in this lesson is a standard library model of BrightSmile's enquiry flow: enquiries arrive with types drawn from the Lesson 02 sample proportions, the agent handles the standard path, escalates by the Lesson 15 policy, errs at a stated rate on a stated category, and the operator's queue accumulates exactly as the rota would meet it. Simulation does not prove the real agent will behave; the real agent is a model, not this code. What simulation proves is whether the operation around the agent works: whether the operator hours suffice at the observed escalation rate, whether the queue clears by the next morning, whether a doubled volume day breaks the rota. Those are arithmetic questions, and arithmetic is cheaper before launch.

## Reading a simulation honestly

The twin's parameters are assumptions, printed at the top of the file, and the lesson's discipline is to vary them, not to admire the base case. Run the week at the audited escalation rate, then at double it, because Lesson 02's sample was twenty cases and the true residue rate has error bars. Run an error day, where the wrong price incident from Lesson 18 fires, and watch whether detection and the queue behave as the catalogue promised. Run the success case, volume up from a good review weekend, and check the operator line, because Lesson 18's eighth failure is the one teams never rehearse. A simulation whose knobs you never turn is a screenshot. A simulation whose knobs you turn is a stress test, and its output belongs in the pilot file beside the scope, as evidence the operation was designed, not hoped.

## What the twin cannot tell you

Say it plainly, because vendors will not: the twin says nothing about reply quality, tone, or the model's judgement on cases unlike the sample. Those are acceptance set questions (Lesson 20) and sampled review questions (Lesson 21). The twin also assumes arrivals behave like the audit said; real arrivals spike around advertising, weather, and a competitor closing, and the rota design should carry a stated surge rule (what gets paused, who is called, what the standard reply says when the queue is long) rather than discovering one. Keep the twin after launch, by the way. When Lesson 24's monthly review proposes a scope change, running the twin at the new volume and residue rates is a ten minute preview of the operator's month, and cheap previews are how small changes stay small.

## The running example: BrightSmile Dental

BrightSmile's simulated week, at the lesson's stated assumptions: 90 arrivals in the audit's proportions (78 percent standard path), agent handling the standard path inside five minutes, escalations at the sample's residue rate plus the policy's draft cases landing in the operator queue, operator capacity at the rota's two thirty minute windows. The queue clears daily with room to spare in the base case. At double the escalation rate it still clears, barely, by borrowing the second window fully. On the simulated error day, the catalogue's detection (morning sample) fires before the tenth wrong reply at these volumes, which converts Lesson 18's wording into a checked expectation. At double volume, the rota breaks on day three, and the surge rule (pause follow ups first, protect first responses) is written into the pilot file as a result.

## Run it

Run `python3 lead_response_twin.py` and turn the knobs yourself in the file: base case, double escalation, double volume. The rota survives the first stress and breaks on the second, and both results are design information, bought for nothing.

## Common failures

- **Simulating the model instead of the operation..** A homemade twin cannot predict a real model's judgement. It predicts queues, hours, and backlogs, which is where pilots actually break.
- **Running only the base case..** Twenty sampled cases gave the residue rate its error bars. Stress at double, and write the surge rule the stress demands.
- **Losing the twin after launch..** Kept, it previews every scope change in Lesson 24. Archived at launch, every later change is a fresh act of faith.

## Recap checklist

- [ ] My pilot week is simulated at base, stressed, and surge settings.
- [ ] The operator rota survives the stresses it must, and the surge rule is written for the ones it cannot.
- [ ] I can say exactly what the twin does and does not prove.

## Resources

- [Course 2, AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n)
- [Course glossary](../resources/glossary.md)
