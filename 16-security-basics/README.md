# Lesson 16: Security basics: what an agent must never be able to do

**Time:** about 90 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 06, 15 · **You need:** Your access plan and escalation policy.

You do not need to become a security engineer to commission an agent safely. You need to hold five threats in mind and insist, in writing, on the control that answers each. This lesson is the owner's version: what can go wrong, in business language, and what to require from whoever builds or supplies the system. It is a starting framework for a conversation with a professional, not a certification, and Lesson 17 handles the neighbouring privacy duties. The unifying principle is Lesson 06's: design so that when something goes wrong, by malice or by confusion, the blast radius is small, visible, and reversible.

## The five threats, in plain language

One, prompt injection: text the agent reads, an enquiry, a review, a document, contains instructions aimed at the agent (ignore your rules, reveal your data, send this link). The control is architectural: the agent treats all incoming content as data, its real instructions come only from its configuration, and its access is so limited that a steered agent can do little (Lessons 06 and 09). Two, data leakage: the agent repeats something across a boundary, one customer's details to another, internal notes to a customer, because it could read both. Control: data minimisation in scope (Lesson 05's exclusions) and output review on the boundary rungs. Three, excessive agency: the system can do more than its job, the classic being a helper granted delete, payment, or mass send rights for convenience. Control: Lesson 06's bands, decided by name. Four, compromised or careless supply chain: the platform, plugin, or provider is the weak point, through their breach, their update, or their subprocessors. Control: Lesson 10's evidence questions, updated for security, and an exit that works. Five, plain error at scale: no attacker at all, just a wrong rule applied four hundred times before anyone looks. Control: sampling review (Lesson 13), caps, and the twice failed rule (Lesson 15). Note how few of these controls are about the model.

## What to require, whoever builds

Turn the threats into contract and acceptance language. Require: a written list of every system the agent can reach and what it can do there (your access plan, mirrored by the builder). Require that instructions in content are never obeyed, and ask how that is enforced and tested, accepting architecture as an answer and a prompt sentence as a partial one. Require logs sufficient to reconstruct any single case end to end, retained for a stated period, exportable by you. Require a pause mechanism you control (Lesson 06). Require notification duties if the provider has a security incident affecting your data. And require the acceptance set (Lesson 20) to include hostile cases: enquiries containing instructions, requests for another customer's information, and an instruction hidden in a long document. A supplier who finds these requests eccentric is telling you about their other customers' incidents, in advance.

## The running example: BrightSmile Dental

BrightSmile's threat list, one line each with its control: injection via a fake enquiry asking the agent to reveal today's patient list, answered by scope (the agent cannot read the patient list at all) and the never in Lesson 14. Leakage via an agent summarising record notes into a reply, answered by exclusion, notes are out of scope entirely. Excessive agency via a helpful request to let the agent process refunds to speed things up, answered by the access plan's none. Supply chain via the provider's messaging subcontractor, answered by a contract question and the raw data export. Error at scale via a wrong price in the approved list being quoted all weekend, answered by sampled review and the fact that the price list has one owner and one copy (Lesson 05), plus a Monday morning correction drill the operator has actually rehearsed.

## Run it

Run `python3 threat_check.py`. Four of BrightSmile's five controls are architectural or contractual; the fifth is deliberately weak, a prompt only control for error at scale, and the checker calls it out so the lesson can fix it properly in Lesson 20.

## Common failures

- **Accepting be careful as a control..** Instructions to the model are the weakest layer in the building. Where a threat matters, the control must live in scope, access, architecture, or contract.
- **Threat modelling only the attackers..** The likeliest incident in a small business is not a hacker; it is the agent faithfully applying a wrong rule all weekend. Error at scale is a security topic.
- **Forgetting the supplier in the threat list..** Your agent's security includes its provider's. Notification duties and a working exit are security controls, and they belong in the contract, not in hopes.

## Recap checklist

- [ ] My threat list names the five threats for my process, in my words.
- [ ] Every threat has a control, and prompt only controls are marked for upgrade.
- [ ] My acceptance set will include hostile cases, by design.

## Resources

- [Course 3, Build MCP Servers](https://github.com/techaurah/build-mcp-servers)
- [Course glossary](../resources/glossary.md)
