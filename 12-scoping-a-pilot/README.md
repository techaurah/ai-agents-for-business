# Lesson 12: Scoping a pilot that can actually answer the question

**Time:** about 75 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 04, 08, 11 · **You need:** Your process map, route decision, and cost worksheet.

A pilot is an experiment, and most business pilots are designed, accidentally or otherwise, to be uninterpretable: too broad to fail, too short to learn, judged on feelings because no target was set. The design here is strict. One question, stated as a sentence the scorecard can answer yes or no (can an agent handle first response on the standard path, at our quality bar, at a cost we accept?). One process, the mapped one. One channel first, if the process has several. A fixed window, long enough to include ordinary bad days; four weeks is this course's default for a weekly rhythm business. And exclusions written from the no list and the readiness grades, so the pilot tests the agent on the work it was scoped for, not on the work everyone agreed it should never do.

## Edges are the design

Every boundary of the pilot is a decision with a reason. Channel edge: BrightSmile pilots on web form and Instagram enquiries, not phone, because the phone has no transcript and the acceptance testing (Lesson 20) needs records. Hours edge: the agent works the hours the gap exists, evenings and weekends, while weekday daytime stays human, which also gives the scorecard a natural comparison group. Case edge: standard path only, with Lesson 15's escalation for everything else, and the escalation rate itself is a result, not a failure: a pilot that escalates 40 percent has answered its question, negatively and usefully. Data edge: only ready and in limit partial sources from Lesson 05. Writing the edges down, with reasons, is what lets a disappointing pilot still be a success of method: you will know exactly what was tested.

## The gate at the end, agreed at the start

Before the pilot starts, the owner signs the gate: the scorecard measures from Lesson 13, the thresholds that mean scale, fix and retry, or stop, and the date of the decision meeting. This feels bureaucratic for a small business until the first pilot ends in ambiguity, with the vendor extending week by week and the team's opinion split by anecdote. The gate converts the end of the pilot from a negotiation into an appointment. It also protects the vendor relationship: a stop decision taken against pre agreed thresholds is professional, while the same decision taken on vibes reads as betrayal, and the market for good providers notices how businesses behave at gates. Lesson 22 runs the gate. This lesson's job is to make sure it exists.

## The running example: BrightSmile Dental

BrightSmile's pilot scope, in the artifact's shape: question, can an agent give a correct, on brand first response to standard path enquiries within five minutes, during the hours the desk is closed, at an escalation rate the operator can carry? Window, four weeks from a Monday, including the half term week that is reliably chaotic. In scope: web and Instagram enquiries, standard path per the Lesson 04 map, replies from approved price and diary data only. Out of scope, by name: phone, clinical content, complaints, existing patients' treatment questions, payments. Gate: Lesson 13's targets, decision meeting booked for the Friday of week five, owner chairs, operator presents the scorecard, vendor attends the first half only.

## Run it

Run `python3 pilot_scope.py`. It checks the scope the way Lesson 26's capstone gate will: every required element present, exclusions named rather than implied, and the gate booked before the pilot, not after.

## Common failures

- **Piloting everything, to be fair to the tool..** Breadth is the enemy of evidence. One process, one or two channels, one question; expansion is Lesson 25's decision, taken with data.
- **Letting the vendor set the pilot's edges..** A vendor scoped pilot optimises for a yes. Your exclusions and your residue cases are what make the yes mean something.
- **No gate date in the diary..** An ungated pilot does not end; it drifts into an unpriced, unsupervised deployment. Book the decision meeting before week one.

## Recap checklist

- [ ] My pilot has one question the scorecard can answer yes or no.
- [ ] Exclusions are named, drawn from my no list and readiness grades.
- [ ] The gate, thresholds, and decision meeting exist before the pilot starts.

## Resources

- [Course glossary](../resources/glossary.md)
- [Course 2, AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n)
