# Lesson 23: Unit economics: what one handled enquiry really costs

**Time:** about 75 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 11, 13, 22 · **You need:** Your cost worksheet, baseline, and scorecard.

Annual totals impress and mislead in equal measure. Unit economics cuts the question to the size of a decision: what does one handled enquiry cost, end to end, under each way of working, counting everything the course has taught you to count? The method is strict symmetry. The manual unit cost includes the staff minutes the process map measured, at loaded rates, plus the supervision and rework the manual process also has (a manager checking bookings is supervision too, just unlabelled). The agent unit cost spreads build, run, supervise, and fix across the units handled in the period, at real volume. Both are computed on the same definition of handled, which excludes escalations resolved by humans under both systems, or the comparison is rigged in the direction of whoever defined the word.

## The honest uses of a unit cost

Three uses survive scrutiny. Pricing headroom: if the agent unit cost, fully loaded, sits well below the manual one at your real volume, expansion decisions (Lesson 25) have an economic leg to stand on beside the service leg (speed, coverage). Volume sensitivity: unit cost moves with volume because build and supervision are semi fixed, so the sheet shows the volume at which the routes cross, which is often the most useful number in a renewal negotiation. And improvement targeting: a unit cost decomposed by family shows whether the next saving lives in run fees (renegotiate or replatform), supervision (better rungs, better data), or fix costs (an error category to kill), which aims Lesson 24 at the largest lever instead of the nearest one. What unit economics must never do is become a savings claim with the assumptions footnoted away; in your own board paper, the assumptions travel with the figure, in the same font size.

## Value is a separate column

Cost per handled enquiry is half a ledger. The other half is what the handling is worth, and this course keeps it in a separate column, in the business's own measured terms: the baseline's never answered rate converted into enquiries now answered, whose value the business estimates from its own conversion history (its booking rate on answered enquiries, its average booking value), stated as a range with its assumptions, never as a multiplier from a brochure. Some deployments justify themselves on cost. Some justify on coverage, an enquiry answered at 9pm that was previously answered never, at a unit cost slightly above manual. Both are respectable cases. The disreputable case is the blended one, where cost and value are merged into a single return figure whose parentage nobody can trace. Keep two columns. Let the owner weigh them in the open.

## The running example: BrightSmile Dental

BrightSmile's unit sheet, worked example with the course's running assumptions: manual handling, nine minutes of work from the Lesson 04 map at the desk's loaded rate plus a share of manager checking, lands at a figure the artifact computes per handled enquiry. Agent handling at pilot volume: total pilot period cost from Lesson 11's families, spread over enquiries the agent handled (escalations counted as human handled under both systems, per the symmetry rule), lands modestly below the manual figure, with supervision the largest component, exactly as Lesson 11 predicted. The value column, kept separate: the never answered rate fell from 11 percent to 1.4, which at the practice's own answered to booked conversion and average first booking value is worth a stated range per month, assumptions attached. The partners' discussion, reportedly, took ten minutes, because every number on the page could be traced to a lesson and a tally.

## Run it

Run `python3 unit_economics.py`. On the stated assumptions the agent unit lands at 3.51 against the manual 4.10, a modest, traceable margin, and the lesson insists you distrust any version of this page where the margin is dramatic and the assumptions are missing.

## Common failures

- **Asymmetric counting..** Excluding the agent's supervision, or the manual process's checking time, rigs the page. Same families, same definition of handled, both columns.
- **Blending value into cost..** A single return figure with untraceable parentage is how businesses talk themselves into renewals. Two columns, each with assumptions, weighed in the open.
- **Quoting the pilot's unit cost at scale volume..** Unit cost is volume sensitive. State the volume beside the figure every time it travels, or it travels as a lie of omission.

## Recap checklist

- [ ] My unit costs are computed symmetrically, escalations counted the same under both systems.
- [ ] I can name the volume at which my routes' unit costs cross.
- [ ] Value sits in its own column, as a range with assumptions, never blended.

## Resources

- [Course glossary](../resources/glossary.md)
