# Lesson 10: Evaluating a vendor or a platform: the demo is not the product

**Time:** about 90 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 08 to 09 · **You need:** Your route decision and framework questions from Lessons 08 and 09.

Vendor evaluation fails in a predictable way: a polished demo on the vendor's data resets your criteria to whatever the demo showed, and scoring afterwards ratifies a decision already made emotionally. The method in this lesson reverses the order. Criteria are written and weighted before any demo, drawn from your readiness grades, your no list, and your access plan. The demo is then run on your cases, including your residue cases from Lesson 02 and at least one case designed to make the agent fail, because how a system and a salesperson handle failure is the most informative ten minutes of the process. References are asked the scorecard question: what does the vendor report to you monthly, unprompted, and can I see a real example with the name removed?

## The traps, named in advance

Five recur often enough to pre print. The savings claim trap: a percentage with no baseline, which your Lesson 13 baseline will make unquotable in your own evaluation, insist on the same standard from them. The data trap: the product works only once your customer data lives in their system in their format, against your readiness grades. The supervision trap: the price assumes the agent runs itself, and your operator cost (Lesson 11) is quietly transferred to your team unbudgeted. The roadmap trap: the feature that closes your gap is coming next quarter; score what exists, in writing, today. The pilot trap: a free pilot scoped so narrowly, on such clean cases, that success is guaranteed and information is zero; Lesson 12 designs pilots that can fail informatively, and a vendor who resists your residue cases has told you something important.

## Scoring, and the evidence standard

Each criterion is scored on evidence, not on answers. A claim about escalation earns points when you watch an escalation happen, in the demo, on your case, with the audit trail visible. A claim about reporting earns points when you hold a sample report. A claim about security earns points for a named architecture (Lesson 06's bands, Lesson 09's checkpoints) and none for the word enterprise grade. Keep the scoresheet; it becomes a contract annex, because the gap between what was scored and what was delivered is your renewal argument and your exit evidence. And leave one column blank on purpose, trust, to be filled after the pilot. Vendors who are good at pilots welcome the blank column; it is the one they intend to fill.

## The running example: BrightSmile Dental

BrightSmile evaluated two managed providers on criteria fixed in advance: escalation behaviour on residue cases (weight 3), reporting quality (3), data location against readiness grades (2), diary integration without patient record access (2), exit terms (2), price transparency (1). Provider A scored well on demos and poorly on evidence: escalation was a prompt instruction (Lesson 09's failure), and the sample report was a marketing dashboard. Provider B was less polished, escalated BrightSmile's two residue cases correctly in the live demo, produced a raw monthly export on request, and accepted the exit clause. The scoresheet read B 56, A 30, and the manager could defend the choice to the practice partners in one page. That defensibility, not the numbers themselves, is the product of this lesson.

## Run it

Run `python3 vendor_score.py` to see the worked scoresheet. Provider B wins 56 to 30, driven by the two heaviest criteria, which is exactly why weights are fixed before anyone demos anything.

## Common failures

- **Writing criteria after the first demo..** Post demo criteria are just the demo, transcribed. If a demo reveals a genuinely new criterion, add it, then re score every vendor including the one who inspired it.
- **Scoring claims instead of evidence..** Every vendor claims escalation, reporting, and security. Points are for watching it happen on your cases and holding the sample report.
- **Skipping the failure case..** A demo with no failure case is a performance. Bring a residue case and an impossible case, and watch both the system and the salesperson.

## Recap checklist

- [ ] My criteria and weights exist in writing, dated before any demo.
- [ ] My demo set includes residue cases and a designed failure.
- [ ] My scoresheet scores evidence, and its trust column waits for the pilot.

## Resources

- [Course glossary](../resources/glossary.md)
- [Course 1, Agentic AI for Beginners](https://github.com/techaurah/agentic-ai-for-beginners)
