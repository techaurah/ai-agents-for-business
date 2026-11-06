# Lesson 24: The monthly improvement loop

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 18, 20, 22, 23 · **You need:** Your scorecard method, failure catalogue, and acceptance set.

Agents do not stay good. Data drifts (the price list changes, the diary rules change), the business drifts (new services, new staff, new tone), the provider's model drifts underneath you, and the team's workarounds quietly rewire the process the agent was scoped for. The monthly loop is the countermeasure, a fixed appointment with five standing agenda items that take under an hour when the artefacts are alive: the month's scorecard against the baseline's ghost, the failure catalogue's new entries and edits, the scope check against the no list, the acceptance set's new cases and latest run, and one improvement, chosen deliberately, implemented as a change with a gate, not as a tweak in passing. Compounding is the point: twelve small, verified fixes a year is what a well run agent actually is.

## One improvement, fully gated

The loop's discipline is singularity. Each month picks the single highest value fix the evidence supports: the largest error category from the sampled reviews, the rung that generates pointless drafts, the data grade that can finally move from partial to ready. The fix is then treated with the full ceremony, however small: stated as a change, run through the acceptance set, deployed, and its effect read in the next month's scorecard. The alternative, the continuous drizzle of small edits by whoever has access, destroys the evidence chain (which change caused which effect?), invites scope creep (Lesson 18's sixth failure), and makes the acceptance set perpetually stale. A business too small for ceremony is not too small for one change a month with a before and after; that is the whole ceremony.

## The loop watches the watchers

Two agenda items guard the system itself. The operator health check: minutes spent against rota, queue texture, and the blunt question of whether the role is still staffed as designed, because supervision decay (Lesson 07) announces itself here a month before it announces itself in quality. And the provider check: model or platform changes shipped by the vendor, pricing schedule changes, and the raw data export test, actually performed, a small file requested and received, proving the exit still works while you do not need it. Businesses discover broken exits at contract end, furious and leverage free. The loop's five minutes a month buys the knowledge while it is still cheap. Bring both items to the meeting even when, especially when, everything looks green.

## The running example: BrightSmile Dental

BrightSmile's month two review, as the worked example: scorecard holds its pilot lines with correctness up three points after the mixed content fix (the Lesson 22 rerun closed as scale for the standard path, recorded). Catalogue gains one entry, a holiday weekend surge handled by the rule but noted for a staffing tweak next year. Scope check finds the agent was asked, in a team chat, to start drafting review replies, a Lesson 02 workflow candidate; the request is routed to a proper scope decision next month rather than enabled in passing, and the asking is praised, because the channel worked. Acceptance set gains the month's two real failures as cases and passes at 42 of 42 on the current configuration. The one improvement chosen: the diary conflict rung moves a common sub case from ask to draft, projected to return twenty operator minutes a week, gated through the set, effect to be read in month three.

## Run it

Run `python3 monthly_review.py`. The checker is pedantic on purpose: five agenda items, exactly one improvement, and that improvement gated. A review that chooses three improvements has chosen none of them a gate.

## Common failures

- **Tweaking continuously, reviewing monthly..** Ungated edits between reviews make the scorecard unreadable and the acceptance set fictional. Changes flow through the loop, or the loop is theatre.
- **Skipping the export test while things are fine..** The exit is tested when it is cheap to learn the answer. Five minutes monthly, against the alternative of learning it during a dispute.
- **Letting scope grow by chat message..** New jobs arrive as favours. The scope check routes them to a decision with the no list open, and the routing, not the refusal, is the culture you are building.

## Recap checklist

- [ ] My monthly review has five standing items and a fixed appointment.
- [ ] Exactly one improvement is chosen per month, gated through the acceptance set.
- [ ] Operator health and the provider export are checked while everything looks green.

## Resources

- [Course glossary](../resources/glossary.md)
- [Course 2, AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n)
