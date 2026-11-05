# Lesson 13: Baselines and success metrics: measure before you automate

**Time:** about 90 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 12 · **You need:** Your pilot scope, your process map timestamps, and two ordinary weeks you can observe.

The baseline is the current process, measured the same way the pilot will be measured, before anything changes. Without it, every pilot result is a number looking for a comparison and finding a vendor's claim instead. The measures this course uses are deliberately few and operational: first response time (median and worst decile, not just the average, because customers live in the tail), resolution or correct handling rate on the standard path, escalation rate, error rate from a sampled human review, and cost per handled enquiry from Lesson 11's worksheet run at baseline volume. Two ordinary weeks is enough for most small business processes; a week with a holiday or a crisis in it is not ordinary, and the sheet should say so.

## Targets chosen in advance are targets; targets chosen after are stories

For each measure, the owner sets three thresholds before the pilot: the scale line (results at or beyond this justify expansion), the fix line (between this and the scale line, the pilot taught us something repairable), and the stop line (below this, the honest answer is no). Setting them in advance is uncomfortable precisely because it works: it prevents the week five meeting from moving the goalposts to wherever the ball stopped. Choose thresholds from the baseline and the business need, not from the vendor's brochure. If the baseline first response is five hours and the business need is enquiries answered before a competitor replies, a target of five minutes in closed hours is a business statement. If the vendor promised thirty seconds, note whose number that was.

## Measure the handling, not the theatre

Two measurement traps deserve names. The happiness trap: surveying satisfaction on the pilot's replies while ignoring the enquiries that never got one, because non response is invisible in a survey of responses; the scorecard counts from the inbox's total, not from the replies sent. The speed trap: first response time improves trivially if the agent replies instantly with nothing useful, so speed is always reported beside the correct handling rate from sampled human review, never alone. The review sampling itself is designed here: the operator scores a fixed sample, say twenty cases a week, against the job description's quality bar (Lesson 14), blind to whether the agent or a human handled the case where the design allows. Small, boring, decisive.

## The running example: BrightSmile Dental

BrightSmile's baseline, two ordinary weeks, from inbox timestamps and the front desk's tally: 90 enquiries a week across channels, median first response 4.8 hours in staffed time and effectively next day in closed time, 11 percent never answered at all (found by counting, to the manager's visible discomfort), standard path share 78 percent of sampled cases, current cost per handled enquiry computed on Lesson 11's method with staff time at the desk's loaded rate. Targets set from it: closed hours first response under five minutes, never answered rate under 2 percent, sampled correctness at or above the human sample's, escalation rate the operator can carry at or under 30 percent. Every target is traceable to a baseline line or to a stated business need. Lesson 22 will grade the pilot against exactly this sheet.

## Run it

Run `python3 baseline.py` for the worked baseline and its target table. The most important line cost nothing to collect: 11 percent of enquiries never answered, found by counting inbox arrivals against replies, the leak the whole project exists to close.

## Common failures

- **Baselining from the vendor's discovery call..** A baseline measured by the seller is marketing. Two weeks, your timestamps, your tally, or the pilot has no ground to stand on.
- **Reporting averages only..** Customers experience the tail. Median and worst decile, plus the never answered count, or the baseline flatters the current process.
- **Setting targets in week five..** Thresholds written after results are stories about results. If a target must change mid pilot, change it in writing with a reason, and keep the original on the scorecard.

## Recap checklist

- [ ] My baseline covers the same measures my scorecard will report.
- [ ] Scale, fix, and stop thresholds are written and signed before the pilot.
- [ ] My speed measures are paired with sampled correctness, never alone.

## Resources

- [Course glossary](../resources/glossary.md)
