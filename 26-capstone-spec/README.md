# Lesson 26: Capstone spec: the deployment plan, fixed in advance

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** All previous lessons · **You need:** Your exercise outputs from across the course. They are the capstone's raw material.

The capstone assembles the whole course into one document for a process from your own business: a complete agent deployment plan. This lesson is the specification, fixed in advance so the build lessons (27 to 29) cannot improvise it. The plan has four sections, in the order a real deployment happens. Readiness: the data, access, and people audits (Lessons 05 to 07) plus the route decision (Lesson 08). Pilot: the scope, baseline, and job description (Lessons 12 to 14) plus the cost worksheet (Lesson 11). Oversight: the escalation policy, threat list, privacy checklist, and failure catalogue (Lessons 15 to 18). Scorecard: the measures, thresholds, unit economics method, and the monthly loop and second decision formats (Lessons 13, 22 to 25). If you did the exercises, you own most of this already; the capstone is an assembly and stress test, not a fresh invention.

## The four gates

Each section passes a gate before the plan counts as complete, and the gates are checkable, several of them by the tools in this repository. Gate one, readiness: every source graded, every external access decided by name, three roles named, and the route decision recorded with its sensitivity sentence. Gate two, pilot: one answerable question, exclusions named, baseline measured or scheduled with dates, thresholds set, job description on one page with its nevers traced to the no list. Gate three, oversight: every action on a rung, hostile cases in the acceptance set, five privacy artefacts present or their gaps owned with dates, catalogue entries with single owners. Gate four, scorecard: measures identical to the baseline's, verdict rules written, unit economics symmetric, monthly agenda and second decision formats filed. The gates are deliberately mundane. A plan that passes them is not guaranteed to succeed; it is guaranteed to be judgeable, which is the property that lets a business learn either way.

## Rules of the build

Three rules govern Lessons 27 to 29. Real process, honestly fictionalised: choose a process from your business or a business you know well, and change names and figures where privacy requires, marking the plan as fictionalised in the places you changed; invented market data is still banned, your own counts and stated assumptions are the currency, as ever. Fixed format: write to the specification's sections even where your material feels thin, because thinness in a section is a finding the stress test (Lesson 28) needs to see, not a formatting problem to hide. And no sales: the plan recommends a route and possibly a category of provider, but it is a decision document for a business, not a pitch; if it reads like marketing, rewrite it until it reads like evidence.

## The running example: BrightSmile Dental

The specification ships with a machine readable skeleton in this lesson's capstone folder: plan.json carries the four sections with their required keys, and tools/validate_course.py at the repository root checks any plan file built to it. BrightSmile's own plan, the running example completed, is summarised at the end of Lesson 27 as your reference for what finished looks like. Your plan's subject should not be BrightSmile; it should be the process you carried from Lesson 00, or a better one the audit revealed. If you arrive here without exercise outputs, Lesson 27 includes the honest shortcut: work the mini versions of the audits in order inside the plan build, accepting the shallower evidence and labelling it as such in the plan itself.

## Run it

Run `python3 plan_check.py` and open capstone/plan.json beside it. The skeleton demonstrates the format with BrightSmile's keys in place; the validator at the repository root enforces the same four sections on any plan built to this spec.

## Common failures

- **Choosing a showcase process instead of a real one..** A plan for an imaginary business teaches formatting only. Real process, fictionalised where privacy needs, labelled where changed.
- **Padding a thin section to look finished..** The gates reward stated gaps with owners and dates, and punish upholstery. Lesson 28's stress test reads thin sections first.
- **Writing the plan as a pitch..** If a paragraph could appear in a vendor brochure, it does not belong in a decision document. Evidence, assumptions, and verdicts; nothing else.

## Recap checklist

- [ ] I can state the four sections and the four gates without reopening the lesson.
- [ ] My capstone process is chosen, real, and fictionalised only where marked.
- [ ] My exercise outputs are gathered; I know which sections they already fill.

## Resources

- [Course glossary](../resources/glossary.md)
