# Lesson 06: Access readiness: accounts, tools, and least privilege

**Time:** about 75 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 05 · **You need:** Your data inventory from Lesson 05.

Access readiness asks a narrower, harder question than data readiness: not what the agent may read, but what it can do, under whose identity, and how you take it back. The working principle is least privilege, borrowed from security practice and translated for owners: the agent gets exactly the access its job description (Lesson 14) requires, in its own named account or key wherever the systems allow, never through a person's login, and never with standing permission to do the things on your no list. If you remember one sentence, make it this: an agent should never be able to do anything you would not let a new temp do on their first day, unsupervised.

## Read, write, and the dangerous middle

Grade every access in three bands. Read access (see the diary, read the enquiry) is the default and the pilot's starting point. Write access with a record (create a booking, log a note) is earned once the pilot proves accuracy, and every write should be attributable: the log says the agent did it, when, from what input. The dangerous middle is write access that reaches outside the business: sending messages as the business, charging cards, changing prices, deleting anything. Those are not one band but a list, each item decided separately in the escalation policy, and several belong on the no list permanently. A useful test for any proposed access: if the agent were manipulated or simply confused tonight, what is the worst thing this permission lets it do before a human wakes up? Price that, then decide.

## Identity, revocation, and the vendor question

The agent needs its own identity in every system that supports one, so its actions are auditable and its access is revocable without changing a human's password or breaking a colleague's morning. Where a platform only offers shared logins, that is a readiness finding: partial at best, with the compensating control written down (closer review, narrower scope). Revocation gets rehearsed, not assumed: someone on the team should be able to say, and ideally has practised, the three clicks that pause the agent entirely. Ask vendors the identity question directly: does your agent act as itself or as one of our users, and show me. The answer predicts your audit trail, your incident response, and your leverage at contract end.

## The running example: BrightSmile Dental

BrightSmile's access plan for the pilot. Enquiry inboxes: read, plus the right to label a message handled, under the agent's own mailbox identity. Diary: read only in the pilot; the agent proposes times and a human confirms the booking, a deliberate limit that Lesson 21's rollout relaxes only if the scorecard earns it. Messaging: the agent may send on the standard path only (Lesson 15 draws that line), from a named practice account that identifies automated replies honestly (Lesson 17). Patient record system: no access. Payment anything: no access, not discussed. Practice social accounts: read the enquiry channel, no posting rights. Kill switch: the mailbox rule and the platform toggle, both known to the operator and the practice manager, tested in Lesson 20's acceptance run.

## Run it

Run `python3 access_plan.py`. BrightSmile's plan deliberately contains one undecided external item, social posting, and the checker refuses to call the plan pilot ready until it is decided by name. That refusal is the lesson working as designed.

## Common failures

- **Running the agent as a person..** Shared identity destroys the audit trail and makes revocation painful exactly when you need it fast. The agent gets its own account or the readiness grade drops.
- **Treating send as one permission..** Sending a booking confirmation and sending a price promise are different risk objects. Decide external actions individually.
- **Never rehearsing the pause..** A kill switch nobody has pressed is a hypothesis. Lesson 20 presses it during acceptance testing.

## Recap checklist

- [ ] Every system my agent touches is listed with a band: read, write with record, external, or none.
- [ ] Every external action is decided by name in the policy, or the plan is not pilot ready.
- [ ] The agent has its own identity, and a named person can pause it in minutes.

## Resources

- [Course 3, Build MCP Servers](https://github.com/techaurah/build-mcp-servers)
- [Course glossary](../resources/glossary.md)
