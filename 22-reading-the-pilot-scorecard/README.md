# Lesson 22: Reading the pilot scorecard

**Time:** about 90 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 11, 13, 21 · **You need:** Your baseline sheet, cost worksheet, and the pilot's raw records.

The scorecard is one page that answers Lesson 12's question with evidence. It reports the pilot's measures in the baseline's exact format (Lesson 13), because a scorecard in new units is a vendor trick even when you play it on yourself. Beside each result sits the threshold set before the pilot: scale line, stop line, and the verdict the comparison dictates. Underneath sit the costs: actual per handled enquiry from Lesson 11's method at pilot volume, and the operator minutes really spent, from the rota log rather than the plan. And at the bottom, the qualitative evidence, labelled as such: the three cases everyone remembers, the complaints, the compliments, each attached to its category so the meeting can weigh anecdote as anecdote and measurement as measurement.

## The verdict discipline

Three verdicts are available and all three are respectable. Scale: thresholds met, expand scope by Lesson 25's deliberate path. Fix and rerun: results between the lines with a diagnosed cause and a bounded fix, one more window, new gate date, and the discipline that a pilot gets one rerun, not a lifestyle. Stop: below the stop line, or a trust failure (a boundary incident, a pattern in complaints), and the deployment ends with the fallback promoted back to the process, the lessons written down, and the money unspent from here counted as the pilot's return, because a pilot that prevents a bad three year contract has paid for itself in the only currency that matters. The meeting's temptation is a fourth verdict, extend and see, which is how pilots become unsupervised deployments. Refuse it by name.

## Reading near the line

Real results land near thresholds, so decide the reading rules now. A measure at the line counts as met only if its evidence quality is high (full period data, honest sampling); a measure carried by a quiet week is read as not yet proven, which usually means fix and rerun with the window moved, not scale. Correctness near the human parity line (Lesson 13) deserves a case level read: are the errors concentrated in one category with a fix (a data grade, a rung assignment), or spread thin as general unreliability? The first is a fix verdict with high confidence. The second is a stop wearing a fix costume, and saying so in the meeting is the owner's job, armed with Lesson 18's catalogue open at the relevant page.

## The running example: BrightSmile Dental

BrightSmile's scorecard, worked example across the artifact: closed hours first response median 3.1 minutes against a scale line of 5, met. Never answered rate 1.4 percent against 2, met. Sampled correctness 90 percent against the parity line of 92 and a stop line of 85: between the lines, and the case read shows the errors concentrated in mixed content phrasing, a tone and drafting fix, not general unreliability. Escalation rate 27 percent against a carryable 30, met, with operator minutes inside the rota in three of four weeks (the half term week needed the surge rule once, executed as written). Cost per handled enquiry below the baseline's, on Lesson 11's method. Verdict: fix and rerun for two weeks on the mixed content fix, gate reconvenes, scale decision deferred with the evidence stated. Not the vendor's preferred headline, and exactly what the gate was designed to produce.

## Run it

Run `python3 scorecard.py` for the worked verdicts: three scale lines met, correctness in the fix band, overall verdict fix and rerun. Notice the meeting still happens on the original date; the gate produced a decision, not a delay.

## Common failures

- **Reporting the pilot in new units..** If the scorecard's measures differ from the baseline's, comparison is impossible and impression wins. Same measures, same sampling, same worksheet method.
- **The fourth verdict, extend and see..** Extension without a diagnosed fix and a new gate date is an unsupervised deployment by instalments. Name it and refuse it.
- **Anecdotes outvoting the table..** The memorable case belongs on the scorecard, labelled qualitative, weighed as one case. The table is the four weeks; the story is a sample of one with good lighting.

## Recap checklist

- [ ] My scorecard reports pilot results in the baseline's format, against pre set thresholds.
- [ ] The verdict is scale, fix and rerun, or stop, and I can defend it line by line.
- [ ] Costs and operator minutes on the scorecard are actuals, not plan figures.

## Resources

- [Course glossary](../resources/glossary.md)
