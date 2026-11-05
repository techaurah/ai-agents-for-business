# Lesson 05: Data readiness: what the agent may read, and whether it is true

**Time:** about 90 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 04 · **You need:** Your process map from Lesson 04 and access to the systems it names.

An agent is only as reliable as the least reliable thing it is allowed to read and repeat. Readiness work starts with an inventory: every source the agent will draw on, the price list, the diary, the FAQ document, the customer record, listed with its owner, its update rhythm, and its known failure mode. Then each source gets a grade, ready, partial, or not ready, on three questions. Is it true today (not last year)? Is it the only version, or one of three conflicting copies? And is the agent permitted to use it for this purpose, which is a privacy question as much as a technical one (Lesson 17 goes deeper)? The inventory takes an afternoon. Skipping it costs the pilot.

## The classic data failures, in advance

They are so consistent they can be listed before you look. The price list exists in three places and they disagree on two items, so the agent quotes whichever it read last. The FAQ page describes a service the business stopped offering. The diary the agent can see is not the diary the business actually books into, because the real one lives in a system with no access route. Customer records carry free text notes containing things no agent should repeat and some things it should never have been able to read. None of these are AI problems; they are housekeeping problems the agent exposes at customer facing speed. Grading honestly converts them from pilot incidents into a fix list with dates, which is why the readiness audit (Lesson 26) requires a grade per source, never a global feeling.

## Grade the source, not the hope

Ready means: one canonical copy, a named owner, updated on a rhythm the business actually keeps, and sampled by you personally against reality this week. Partial means usable with a stated constraint, for example, prices are current but treatment descriptions are not, so the agent may quote the first and must never improvise the second. Not ready means the agent does not touch it in the pilot, full stop, and the pilot scope (Lesson 12) is drawn around the gap. This discipline is what separates a pilot that tests the agent from a pilot that tests your data hygiene in public. It also produces the most useful sentence in vendor meetings: our data grades are these, which of your requirements do they fail?

## The running example: BrightSmile Dental

BrightSmile's inventory for the lead response agent. Diary system: ready, it is the real booking diary, one copy, reception owns it, though the agent gets read access only in the pilot (Lesson 06 decides why). Price list: partial, the website copy is current, the printed sheet in reception is two revisions old and the agent's source must be the website data, named explicitly, with the printed sheet destroyed to end the argument. Treatment descriptions: not ready, marketing copy promises outcomes in language the clinicians dislike, so the agent links to them never and summarises them never; it books and prices, humans explain treatment. Patient record notes: not ready and not needed, the agent works from the enquiry and the diary, and Lesson 17 records why the notes stay out of scope entirely.

## Run it

Run `python3 data_audit.py` to see BrightSmile's graded inventory. Note the pattern: each grade travels with its limit in the same line, so the audit doubles as pilot scoping instructions.

## Common failures

- **Grading the intention instead of the copy..** The price list you mean to update is the old one until the day you actually update it. Grade what exists today.
- **Letting the vendor grade your data..** A vendor's readiness check exists to start the project, not to protect it. Your grades, your samples, your dates.
- **One global grade for everything..** Data readiness is per source. A single ready hides the one not ready source the agent will find in week one.

## Recap checklist

- [ ] Every source my agent would touch is inventoried with an owner.
- [ ] Each source has a grade, and partial grades carry their limit in writing.
- [ ] Not ready sources are excluded from pilot scope, by name.

## Resources

- [Course 3, Build MCP Servers](https://github.com/techaurah/build-mcp-servers)
- [Course glossary](../resources/glossary.md)
