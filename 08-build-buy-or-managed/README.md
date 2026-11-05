# Lesson 08: Build versus buy versus managed service: the fair comparison

**Time:** about 90 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 05 to 07 · **You need:** Your readiness grades from Lessons 05 to 07.

There are three honest routes to the same agent, and the right one depends on your readiness grades, your team's skills, and how unusual your process is. Build: your team, or a developer you hire, assembles the agent from a framework or platform pieces; you own the result and its maintenance. Buy: you configure a vendor's agent platform or product; you own the operation, they own the machinery. Managed service (sometimes called agent as a service): a provider designs, builds, deploys, monitors, and improves the agent for a recurring fee; you own the supervision and the verdict, they own everything technical. None of these is the grown up option. Each is the right answer somewhere, and this lesson's artifact scores them against your facts rather than against a sales narrative.

## The criteria that actually separate the routes

Five questions do most of the work. How unusual is your process: standard processes are served well by products, idiosyncratic ones punish configuration and reward building. Who can supervise changes: every route still needs your operator (Lesson 07), but build and buy also need someone who can change prompts, rules, and integrations safely. How fast must it change: a practice that reprices monthly needs change to be cheap and quick, which favours different routes at different scales. Where does the data live: some platforms require your customer data in their cloud, which your readiness grades and Lesson 17 may refuse. And what does leaving look like: the cost of exiting each route in month thirteen, in money, time, and lost history, is a first class criterion, not a footnote, because switching costs are where recurring fees get their confidence.

## The managed route, fairly stated

A managed service deserves neither the suspicion nor the romance it attracts. Its real offer is that the scarce skills, agent engineering, evaluation, monitoring, prompt and model maintenance, are rented with the system rather than hired into a business too small to employ them. Its real risks are the mirror image: you can supervise a system you do not understand only if the provider reports honestly (demand the scorecard data, raw, on your schedule, Lesson 22), and the knowledge of your process accumulates in their team, which raises the exit cost every month. The fair test is not whether managed is cheaper than building; it is whether the contract gives you the evidence to judge it and the right to leave with your data, your prompts' outputs, and your dignity. Lessons 10 and 11 arm both halves of that test.

## The running example: BrightSmile Dental

BrightSmile scores its three routes in the artifact, on its own facts: a standard process (enquiry triage is well understood), no technical staff, readiness grades mixed (diary ready, descriptions not ready), and a manager who can operate but not build. Build scores worst, honestly: the practice would be hiring skills it cannot evaluate. Buy scores in the middle: platforms exist for dental enquiries, but two finalists wanted the patient record integration the readiness audit had already refused, and configuration would still land on the manager. Managed scores best on this fact pattern, with the exit and evidence clauses from Lesson 10 written into the decision record as conditions, not hopes. A software agency doing the same exercise with developers on staff would land on build, and both answers are the method working.

## Run it

Run `python3 routes.py` for BrightSmile's scored comparison: managed 40, buy 33, build 27 on the stated fact pattern. The artifact's real output is not the winner; it is the weighted criteria you can reuse and argue with.

## Common failures

- **Comparing demos instead of criteria..** All three routes demo beautifully on a standard process. Criteria scored before demos, revisited after, is the only defence.
- **Scoring build with a hypothetical team..** If the developer is a future hire, build's maintenance score belongs to the business you have, not the one in the plan.
- **Ignoring exit cost until renewal..** Month thirteen leverage is decided in month zero. Score it, and let Lesson 10 turn the score into contract questions.

## Recap checklist

- [ ] I have scored all three routes on my facts, with weights I can defend.
- [ ] My decision record names the conditions (evidence, exit) attached to the winner.
- [ ] I know which changed fact would change my answer.

## Resources

- [Course glossary](../resources/glossary.md)
- [Course 1, Agentic AI for Beginners](https://github.com/techaurah/agentic-ai-for-beginners)
