# Lesson 21: Rollout: training the team and the first two weeks

**Time:** about 75 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 07, 19, 20 · **You need:** Your acceptance results, roles sheet, and failure catalogue.

Rollout is where the pilot meets the rota, the team's feelings, and the first genuinely strange case, usually on day two. This lesson's plan is deliberately unglamorous. A briefing that happens before launch and says what changes for whom (Lesson 07 prepared it). A daily review rhythm for the first two weeks: the operator's morning sample, a fifteen minute check in with the owner on days one to five then twice weekly, and a standing rule that any team member can flag a case for review with one click or one sentence, whichever is easier than working around it. And a manual fallback that stays warm: the old way of handling enquiries is not dismantled at launch, it is rostered as the understudy, so a pause (Lesson 18) is an inconvenience, not a crisis.

## The first two weeks are a listening exercise

Schedule the pilot's start for an ordinary week, never the busiest and never the quietest, because both lie. Expect the team's real questions to arrive after they see the first outputs, not at the briefing: the receptionist who asks whether the agent's reply used the patient's first name correctly is doing quality work, and the rhythm should treat those questions as the pilot's data, logged beside the sampled review. Watch for workaround behaviour (Lesson 07's warning) with kind attention: a staff member quietly reanswering the agent's enquiries is telling you the replies are not trusted, which is a finding about tone or accuracy, not about attitude. And protect the operator visibly: when the queue is heavy in week one, the owner takes a window personally at least once. Nothing else you do will communicate the role's value as clearly.

## Communication outside the team

Customers meet the pilot as messages, and the disclosure from Lesson 17 does the formal work. Two practical additions matter. First, the standard reply in a long queue: if a surge hits (Lesson 19's rule), enquiries get an honest holding reply with a time commitment, because silence during an automated pilot reads as a broken business, not a busy one. Second, a feedback route customers can actually find, the human route from Lesson 17, monitored by the operator as a quality signal, not by a marketing inbox monthly. Complaints about the agent in week one are acceptance testing you did not have to design; route them into the scorecard's evidence, thank the senders, and let Lesson 22 weigh them with the rest, neither as veto nor as noise.

## The running example: BrightSmile Dental

BrightSmile's first two weeks, as planned and as the capstone will reuse. Launch Monday of an ordinary week, closed hours only, per the scope. Morning rhythm: operator samples twenty replies (ten minutes, from the queue tool), logs errors against the job description, checks the heartbeat and the arrivals reconciliation from Lesson 18. Fifteen minute owner check in at 9:15 on days one to five: yesterday's numbers, one case read aloud, any rung that felt wrong. Twice in week one the owner takes the 4pm window. The front desk keeps the old enquiry rota on paper as fallback, unstaffed unless invoked, and the team is told invoking it is a success of the drill, not a failure of the pilot. Day ten: the interim note to the whole team, numbers and one honest problem included, because the team that hears results asks better questions in week three.

## Run it

Run `python3 rollout_plan.py`. The checker guards the four items experience says get skipped under launch pressure: briefing first, owner in a window, fallback on paper, and the surge reply approved before it is needed at short notice.

## Common failures

- **Launching in the biggest week to prove it works..** A surge week tests the rota, not the agent, and a failure there poisons a good system. Ordinary week, then let Lesson 25 expand deliberately.
- **Dismantling the manual process at launch..** The fallback is the pilot's insurance. Keep it warm and unstaffed, and praise its use when invoked; the day it is needed, pride about it will be expensive.
- **No channel for quiet workarounds to surface..** If flagging a case is harder than fixing it silently, your data is fiction. One click or one sentence, and a visible fix in response, every time.

## Recap checklist

- [ ] My rollout has a briefing before launch and a daily rhythm for two weeks.
- [ ] The manual fallback is rostered, warm, and praiseworthy to invoke.
- [ ] A surge holding reply exists and the human route is monitored daily.

## Resources

- [Course 2, AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n)
- [Course glossary](../resources/glossary.md)
