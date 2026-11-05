# Lesson 07: People readiness: owners, operators, and the team that lives with it

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 05 to 06 · **You need:** Your data and access work from Lessons 05 and 06.

Every failed agent deployment has a technical postmortem available, and most of them are lying by omission. Agents fail in businesses because nobody owned them after launch day: escalations landed in a shared inbox nobody watched, the one enthusiast who understood the system went on holiday, the team whose work changed was told last and consulted never. People readiness names three roles before any pilot starts. The owner, who commissioned the agent, owns its budget and its verdict. The operator, who supervises it day to day, reviews its queue, takes its escalations, and keeps its scorecard. And the escalation human, named per case type, who receives what the agent cannot handle. One person may hold two roles in a small business. Zero people may hold none.

## The operator is a job, not a favour

Operators fail when the role is real but the hours are imaginary. Estimate the operator load from your process map: escalations per day (your residue rate from Lesson 02's sample, times volume), minutes per review, plus a weekly review meeting. Then put those hours in someone's week, by taking something else out or by paying for the time openly. An operator role that exists only as extra work done by a willing person in the gaps will last exactly as long as their goodwill, and the agent's quality will decay on the same schedule, silently, because the person also stops reporting problems they have no time to fix. The scorecard (Lesson 22) therefore tracks operator minutes as a cost line (Lesson 11), not as a rounding error.

## The team that lives with it

The people whose daily work touches the agent's process need three things before the pilot, not after: an honest account of what will change for them, a channel to report the agent being wrong that is easier than working around it, and evidence that reports change something. Working around a bad agent, quietly fixing its bookings, reanswering its enquiries without logging it, is the most dangerous failure mode in this course, because it makes a failing pilot look successful until the workaround artist is away. The rollout lesson (21) builds the reporting rhythm; readiness simply requires that the people are named, briefed, and believed. If the team that does the job today thinks the agent is being done to them, no pilot design survives contact with week two.

## The running example: BrightSmile Dental

BrightSmile's roles sheet. Owner: the practice manager, who holds the budget, chairs the weekly review, and will read the scorecard verdict in Lesson 22. Operator: the senior receptionist, whose rota gains a named thirty minutes at 9am and 4pm for the agent queue, with the Saturday morning phone hour moved to the junior receptionist to make room, an actual trade, written down. Escalation humans: clinical or emotional cases to the practice manager, diary conflicts to the operator herself, technical failures to the vendor contact with the owner copied. Backup operator: the junior receptionist, trained during the pilot, because the senior's August holiday is already booked and readiness means reading the calendar.

## Run it

Run `python3 roles.py`. BrightSmile passes, and the checker shows its working: three named roles, three escalation routes, and hours that exist in a rota rather than in someone's spare time.

## Common failures

- **The shared inbox as escalation destination..** An escalation to everyone is an escalation to no one. Each case type names a person, and Lesson 15 tests the routes.
- **Operator hours by goodwill..** Unbudgeted supervision decays silently and takes the scorecard's honesty with it. Put the minutes in the rota and in Lesson 11's cost sheet.
- **Briefing the team at launch..** People told at launch hear a threat. People consulted during design report problems early, which is the entire value of a pilot.

## Recap checklist

- [ ] Owner, operator, and backup operator are named people in my plan.
- [ ] Every escalation case type has a named human destination.
- [ ] The operator's hours exist in a rota and in the cost worksheet.

## Resources

- [Course glossary](../resources/glossary.md)
- [Course 2, AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n)
