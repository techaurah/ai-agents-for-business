# Lesson 28: Stress test the plan: red team your own deployment

**Time:** about 2 hours · **Difficulty:** Advanced · **Prerequisites:** Lesson 27 · **You need:** Your built plan from Lesson 27 and the acceptance set.

A plan that has only been read is a hypothesis. This lesson attacks it, on paper, with the four stressors reality will certainly supply: hostile input, component failure, volume, and time. The method is a structured red team, sized for a small business: you (and ideally one colleague who did not write the plan) work a scripted set of attacks and accidents against the plan's documents, scoring each as handled, handled with a gap, or unhandled, and every score must point at the plan line that earns it. No line, no credit: a defence that exists in the owner's head but not in the plan does not exist at 8pm on a Sunday, which is when it will be needed.

## The four stressors, scripted

Hostile: reuse Lesson 16's cases against the plan, an injected instruction in an enquiry, a social engineering attempt on the operator (a caller claiming to be the owner, authorising a scope change by phone), and a poisoned data attempt (a well meaning staff member pasting an unvetted price list into the agent's source). Component failure: the provider is down for a day, the diary integration silently returns stale data, the operator is sick for a week; for each, the plan's detection and fallback are walked minute by minute. Volume: double arrivals and double escalations simultaneously (Lesson 19's twin, rerun with the plan's real numbers), plus the review that goes well and triples enquiries in a month. Time: the plan read as if it is month nine, the vendor has been acquired, the operator has left, the model has been upgraded twice; which artefacts still protect the business, and which quietly assumed the pilot team would last forever?

## Scoring, fixing, and the honest residue

Fix what the stress test finds, in the plan, and rerun the affected stressor. Expect the fixes to cluster in three places: detection (a stale diary feed has no symptom until a customer complains, so a reconciliation check joins the morning rhythm), authority (the phone authorisation attempt succeeds against most first drafts, so scope changes are defined as written only, whoever asks), and succession (the operator's knowledge lives in the plan's annexes, tested by having the backup operator run one drill unaided). What remains after fixing is the honest residue: risks the plan consciously carries, listed on the plan's risk page with their triggers for revisiting. A plan with no residue page is claiming a certainty no deployment has; a reviewer should trust it less, not more.

## The running example: BrightSmile Dental

BrightSmile's stress results, worked example: hostile cases handled, except the staff pasted price list, which the plan had no defence against beyond trust; fix, the price source becomes a file only the owner can edit, with the change logged, a Lesson 05 grade condition added. Component failure: provider outage handled by the fallback; stale diary data unhandled on first pass, no detection existed; fix, a morning reconciliation of three sample bookings against the diary, added to the operator rhythm and the catalogue. Volume: the twin at double double breaks the rota on day four as designed, surge rule invoked, held. Time: the acquisition scenario exposed that the raw export had never actually been retrieved since the pilot; fix, the monthly export test from Lesson 24 is written into the plan itself rather than living in the course habit. Residue page: five carried risks, each with a revisit trigger.

## Run it

Run `python3 stress_test.py` for the worked results: five handled, two gaps, both fixed in the plan with their plan lines recorded, zero unhandled. Your run should end in the same shape; an all handled first pass means the stressors were too kind.

## Common failures

- **Crediting defences that live in someone's head..** If the plan line cannot be cited, the defence does not exist for the person on duty. Write it, then score it.
- **Stress testing only the technology..** The authority phone call and the pasted spreadsheet are organisational attacks, and they succeed against most first drafts. Include people in the threat model.
- **Fixing without rerunning..** A fix is a claim until the stressor runs again against the edited plan. The rerun is minutes; the confidence is the product.

## Recap checklist

- [ ] My plan has been attacked on paper across hostile, failure, volume, and time.
- [ ] Every score cites a plan line, and every gap is fixed or on the residue page.
- [ ] My residue page lists carried risks with their revisit triggers.

## Resources

- [Course glossary](../resources/glossary.md)
- [Course 3, Build MCP Servers](https://github.com/techaurah/build-mcp-servers)
