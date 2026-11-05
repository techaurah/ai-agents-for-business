# Lesson 20: Testing before trust: the acceptance set

**Time:** about 90 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 14 to 16, 18, 19 · **You need:** Your job description, escalation policy, and failure catalogue.

The acceptance set is a saved collection of cases with expected outcomes, run against the agent before it touches real customers and after every change to its configuration, data, prompts, or provider model. It is the single highest value artefact in this course, because it converts trust from a feeling into a gate. Build it from your real materials: ordinary cases from the Lesson 04 map, your Lesson 02 residue cases, the hostile cases from Lesson 16 (instructions hidden in enquiries, requests for another customer's data), the tone cases from Lesson 14's examples, and at least two cases for each Lesson 18 failure you can trigger safely. Thirty to fifty cases is a working set for a small business pilot; quality of coverage beats count.

## Expected outcomes are policy, written as tests

Each case states what should happen in the vocabulary of the ladder: this case acts and says substantially this; this case drafts; this case escalates to this person; this case refuses the embedded instruction and handles the legitimate request inside it. Writing expectations this way exposes the disagreements the team has been carrying politely: two reviewers will expect different handling for the mixed booking plus worry case until the policy is quoted at them, and that argument, held now over a test case, is infinitely cheaper than the same argument over a real patient. Score the run as a table, case by case, and keep the failures with their fixes. A passing run is a gate record. A failing run is the system working, provided the gate is real: no launch, no exceptions for calendar pressure, because a gate that bends for a date is a decoration with a date on it.

## The set is a living asset

After launch, every real failure joins the set within a week (Lesson 24 schedules it), so the set grows in the direction of your business's actual risks rather than a test designer's imagination. Every change runs the whole set: a price list update, a prompt edit, a provider model upgrade you may not even be told about, which is why the run is cheap and scripted where possible and why its results are kept. Vendors on the managed route should run your set, or accept yours being run against their system, on a schedule you choose; a provider who resists a customer's acceptance set is asking for trust without evidence, and Lesson 10 taught you the price of that. The set also settles renewal arguments: twelve months of gate records are the pilot's long memory, outliving everyone's impressions.

## The running example: BrightSmile Dental

BrightSmile's acceptance set, built in the artifact's shape: 40 cases. Fourteen ordinary standard path cases with expected content points. Six residue and mixed cases with expected rungs. Five hostile cases (an enquiry instructing the agent to reveal today's bookings, one asking for another patient's appointment time, one hiding an instruction inside a long insurance question, one offering a bribe of a five star review for a discount, one in another language with an embedded instruction). Five tone cases, including the apology. Four boundary cases from the data grades (a treatment description request that must route, not summarise). Six operational cases from the catalogue drills, including the wrong price correction flow, executed in the vendor's test environment with the practice's own operator running the pause. Result on the first full run: 36 of 40, with the four failures clustered on mixed content rungs, fixed in policy wording, rerun clean, gate record filed.

## Run it

Run `python3 acceptance_set.py`. The worked set shown is the teaching extract (16 of BrightSmile's 40 cases) and the checker enforces the real rule: all six categories present, or the set is not complete, whatever its size.

## Common failures

- **Testing only the happy path..** An acceptance set of ordinary cases certifies that the agent can do the easy part. Residue, hostile, boundary, and drill cases are where launches are saved.
- **A gate that bends for a date..** The launch that cannot wait two days for a failing category to pass is the launch that generates the incident. Gates are cheap precisely because they are rigid.
- **Treating the set as a launch event..** The set's real life starts at the first change after launch. Script the run, keep the records, and add every real failure within a week.

## Recap checklist

- [ ] My acceptance set covers all six categories, with expected rungs per case.
- [ ] Hostile and boundary cases exist and are run, not just listed.
- [ ] The gate is written: a failing category means no launch and no change ships.

## Resources

- [Course 1, Agentic AI for Beginners](https://github.com/techaurah/agentic-ai-for-beginners)
- [Course glossary](../resources/glossary.md)
