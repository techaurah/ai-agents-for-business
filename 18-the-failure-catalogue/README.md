# Lesson 18: The failure catalogue: how agents go wrong in businesses

**Time:** about 75 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 15 to 17 · **You need:** Your escalation policy, threat list, and checklist.

Pilots do not usually die from one dramatic failure. They die from a small failure handled slowly, discovered by a customer, and discussed by the team as a surprise. The failure catalogue exists to remove the surprise. It lists the failures this kind of agent, in this kind of business, actually has, drawn from the preceding lessons, and for each one writes three lines in advance: how we notice (the detection), what we do in the first hour (the response), and whose job it is (the owner). A catalogue is rehearsed, not just written: Lesson 20's acceptance testing includes a failure drill, and Lesson 21's first week rhythm assumes these pages are open on the operator's desk.

## The eight, and what they teach

The confident wrong answer, usually from stale approved data (Lesson 05), detected by sampled review, answered by correction and a data fix, owned by the operator. The tone failure, a correct message that sounds wrong as your business, detected in review, answered by editing the example set, owned by the owner. The loop, an agent and a customer, or two systems, exchanging messages past all sense, detected by the failures counter and volume alarms, answered by the pause, owned by the operator. The silent stall, the agent stops working and nobody notices because nothing arrives to review, detected by a daily heartbeat check (a queue that is empty for the wrong reason looks like a good day), answered by the vendor route, owned by the operator. The boundary leak, data crossing where it should not (Lesson 16), detected by review or by a customer, answered as an incident with disclosure duties, owned by the owner. The scope creep failure, the agent found doing a no list job someone enabled, detected at monthly review, answered by reverting and recording. The provider outage, answered by the manual fallback the team kept warm. And the success failure: volume doubles, the operator drowns, quality decays; detected by the scorecard's supervision line, answered by Lesson 25's expand decision taken deliberately instead of by exhaustion.

## Writing the response before the adrenaline

Each catalogue entry is short because it must be usable at 8pm by a tired person. Detection first, because most response plans secretly assume someone has already noticed, and in three of the eight entries noticing is the hard part. The first hour only: later steps belong to reviews and postmortems, while the catalogue's job is containment, correction, and communication in the right order, including who tells the affected customer and with what approved wording (the apology from Lesson 14's tone examples earns its place here). Owner last, a single name, because an incident with two owners has none. After any real incident, the catalogue gains an entry or an edit within a week, while memory is fresh; Lesson 24 schedules exactly that. A catalogue that grows is a system learning. A catalogue that never changes is wall decoration.

## The running example: BrightSmile Dental

One BrightSmile entry in full, the confident wrong answer. Detection: operator's morning sample of twenty replies (Lesson 21) or a customer correction, whichever first. Response, first hour: operator pauses the affected path (price answers), checks the approved list against the website data, identifies every reply since the error began from the logs, owner approves the correction message from the tone examples, affected customers are contacted before they discover it themselves where the error touched a booking or a price they relied on, path reopens only after the acceptance spot check (Lesson 20) passes on price cases. Owner: operator for containment, practice manager for the correction decision. Total length, half a page. It was used, in simulation, in Lesson 20, and the drill found the logs took eleven minutes to search, which became a vendor requirement before launch.

## Run it

Run `python3 failure_catalogue.py` for the eight entries in their working format. The checker enforces the format itself: no entry counts unless detection, response, and a single owner are all present.

## Common failures

- **Cataloguing only the dramatic..** Boundary leaks matter, but the catalogue earns its keep on the wrong price, the loop, and the quiet stall. If an entry has never happened anywhere, it probably does not belong in the top eight.
- **Responses that start after detection is assumed..** Half the entries are detection problems wearing response costumes. Write the noticing mechanism first, and make it a rota item.
- **Two owners per entry..** Shared ownership in an incident means a pause while two people assume the other is acting. One name; the other person is the backup from Lesson 07.

## Recap checklist

- [ ] My catalogue covers the eight failure shapes, adapted to my process.
- [ ] Every entry has detection, a first hour response, and one owner.
- [ ] At least one entry has been rehearsed, not just written.

## Resources

- [Course glossary](../resources/glossary.md)
- [Course 3, Build MCP Servers](https://github.com/techaurah/build-mcp-servers)
