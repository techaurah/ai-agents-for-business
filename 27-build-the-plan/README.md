# Lesson 27: Build the plan: readiness, pilot, oversight

**Time:** about 3 hours · **Difficulty:** Intermediate · **Prerequisites:** Lesson 26 · **You need:** Your skeleton from Lesson 26 and every exercise output it links.

This lesson builds the plan, section by section, in deployment order. The method is assembly with cross checking: each section is written from its source lessons, then read against its neighbours for contradictions, because plans fail at the seams (a pilot scope that assumes diary write access the access plan refused; an escalation policy whose ask rung presumes a rota the people section never staffed; a scorecard measuring a channel the scope excluded). Work in the order given, keep the validator close, and treat every contradiction found as the build succeeding: this is the cheapest possible moment to find them, in a document, before they acquire dates and customers.

## The assembly, with its cross checks

Readiness first, written fresh even where exercises exist, because grades expire: recheck the data grades against this week's reality, confirm the access decisions survived any vendor change since Lesson 10, and reconfirm the named humans still hold their roles. Cross check one: the route decision's assumptions against the readiness grades as they now stand. Pilot second: scope, baseline, thresholds, job description, and cost worksheet, in that order, since each constrains the next. Cross check two: every tool and data source the job description names exists in the access plan at the band the description assumes, and every exclusion in the scope appears in the job description's exclusions, word for word. Oversight third: policy, threats, privacy, catalogue. Cross check three: every ask and escalate destination is a person named in readiness, with hours that cover the pilot's operating window. Scorecard last: measures copied from the baseline, not paraphrased, verdict rules, unit economics method, monthly agenda, second decision formats. Cross check four: every measure on the scorecard is produced by a system named somewhere in the plan; a measure nobody collects is a lie the plan tells itself.

## Length, and what finished looks like

A complete plan for a small business process runs eight to fifteen pages, much of it tables and lists. Longer is not better; a plan that cannot be read in one sitting by its own owner will not be opened during an incident. Attach the long artefacts (acceptance set, full catalogue) as annexes and summarise them in the body with their counts and locations. Finished means: the validator passes, the four cross checks are recorded as done with their findings, every gap carries an owner and a date, and the plan's first page states the process, the question, the route, and the gate date, in that order, so a stranger grasps the deployment in ninety seconds. BrightSmile's completed plan, summarised in this lesson's solution, is your reference for density: it is not long, and every line in it can be traced to a tally, a tally sheet, or a named decision.

## The running example: BrightSmile Dental

BrightSmile's plan, in outline: readiness records four data grades (diary ready, prices partial in limit, descriptions and notes out), access with payments and records at none, three named roles with the rota trade, route managed with the exit and evidence conditions. Pilot records the closed hours question, five named exclusions, the two week baseline with its signed thresholds, the one page job description with five nevers, and the cost worksheet at audited volume. Oversight records the four rung policy with its checker results, five threats with one upgraded control, the privacy checklist with the adviser date booked, and eight catalogue entries. Scorecard copies the baseline's five measures, the verdict rules, the symmetric unit method, and the monthly agenda with its export test. Four cross checks found two real contradictions during the build (a job description assuming diary writes the pilot later restricted, and an ask destination rota gap on Sundays), both fixed in the plan, both recorded.

## Run it

Run `python3 cross_check.py` against the worked example plan in this lesson's capstone folder. Four seam checks, all passing on the corrected plan; the lesson text describes the two contradictions the same checks caught on the first draft.

## Common failures

- **Writing sections in isolation..** Plans fail at seams: scope against access, rungs against rotas, measures against systems. The cross checks are the build, not a polish step.
- **Copying the baseline's measures from memory..** Paraphrased measures break the comparison the whole scorecard depends on. Copy them, character for character, and let the checker prove it.
- **Hiding the gaps found..** The build record lists contradictions found and fixed. A plan with no findings is a plan whose cross checks were not run, and Lesson 28 will assume they were.

## Recap checklist

- [ ] My plan's four sections are assembled and the validator passes.
- [ ] Four cross checks are recorded, with their findings and fixes.
- [ ] Every remaining gap has an owner and a date, on the plan's first pages.

## Resources

- [Course glossary](../resources/glossary.md)
