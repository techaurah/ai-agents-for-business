# Lesson 17: Privacy and compliance basics for owners

**Time:** about 75 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 05, 16 · **You need:** Your data inventory and threat list. This lesson is orientation, not legal advice.

This lesson teaches the slice of privacy and AI regulation a business owner must understand to commission an agent responsibly, and it is explicit about its limit: it is orientation for asking better questions of a qualified professional in your jurisdiction, not legal advice, and not a substitute for it. Three duties recur across most regimes, in different words. Tell people: when a person is interacting with an automated system, or receiving automated messages, disclosure is increasingly a legal requirement and always a trust one. Take only what you need: data minimisation, which you have already practised as scope design in Lesson 05. And keep control: know where the data goes, who else processes it, how long it is kept, and how a person can reach a human or have their data handled on request.

## The regulatory weather, dated

Facts here are stated as observed in sources read on 2026-11-06 and collected in RESEARCH.md; regulations move, so treat this as the shape, rechecked with your adviser for the current state. The EU AI Act regulates AI by risk and, separately, general purpose models. Its transparency duties, telling people they are interacting with an AI system and marking AI generated content, took effect in August 2026, and most high risk system obligations were deferred by the 2026 Digital Omnibus to December 2027 and August 2028. A small business buying an agent is usually a deployer rather than a model provider, but deployer and disclosure duties, and ordinary privacy law (GDPR in Europe, and equivalents elsewhere) about lawful basis, retention, and people's rights over their data, apply to the buyer in full. Regulated sectors add their own layer: a dental practice already lives under health data duties that an enquiry agent touches the moment a message mentions symptoms, which is one more reason Lesson 03 put clinical content on the no list.

## The owner's checklist

Five artefacts answer most of the owner's duties in practice. A disclosure line, approved, used wherever the agent interacts: the reply identifies the practice and that the message is automated with human review, in the channel's own conventions. A data map: what the agent reads, writes, and sends where, which is Lessons 05 and 06 combined and already written. A retention rule: how long enquiry transcripts and logs are kept, by whom, and the deletion route, including from the provider's systems. A human route: how a customer reaches a person, prominently, at every stage; an agent that is hard to escape is a complaint and, in some regimes, a compliance failure in itself. And a review date: the checklist is rechecked when the scope, the provider, or the law changes, with Lesson 24's monthly review carrying the habit. None of this needs a law degree. All of it needs to exist before the first real customer message, not after the first complaint.

## The running example: BrightSmile Dental

BrightSmile's checklist, completed. Disclosure: automated replies carry the practice name and a line noting the reply is automated and reviewed by the team each morning, placed in the message footer where patients already look for the phone number. Data map: the Lessons 05 and 06 documents, attached to the pilot file. Retention: enquiry transcripts kept 90 days in the practice system for quality review, provider copies deleted on the same cycle under the contract's schedule, logs for a year. Human route: every automated message carries the practice phone number and the sentence that a person replies in working hours; the escalation policy guarantees it is true. Review date: the first Monday of each month, inside Lesson 24's review, with the practice's compliance adviser invited quarterly. Five artefacts, none longer than a page, all dated before launch.

## Run it

Run `python3 privacy_check.py`. BrightSmile's five core artefacts are complete and one item stands open on purpose: the professional adviser has not yet been consulted, and the checklist refuses to let that be forgotten before launch.

## Common failures

- **Hiding that a reply is automated..** Apart from the legal direction of travel, discovery is a trust incident: a customer who realises late feels deceived, and tells the story that way. Disclose plainly, early, in the message itself.
- **Keeping everything forever, just in case..** Indefinite retention is a liability wearing a storage costume. Set the period, tie it to a purpose (quality review), and make deletion real, including at the provider.
- **Treating this lesson as the advice..** It is a map for a conversation with a professional in your jurisdiction and sector. The checklist's last item exists because the first five are not a substitute.

## Recap checklist

- [ ] My agent's disclosure line is approved and lives in the messages themselves.
- [ ] Retention, the data map, and the human route are written, dated, and filed.
- [ ] A professional adviser for my sector is consulted, or booked, before launch.

## Resources

- [EU AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [Course glossary](../resources/glossary.md)
