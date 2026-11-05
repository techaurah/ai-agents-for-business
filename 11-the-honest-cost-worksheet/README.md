# Lesson 11: The honest cost worksheet: build, run, supervise, fix

**Time:** about 90 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 07 to 10 · **You need:** Your operator estimate from Lesson 07 and any real quotes you hold, labelled with their date.

Agent costs hide in four places, and vendor pricing usually illuminates one of them. Build cost: setup, configuration, integration, and the knowledge work of Lessons 04 to 06, whether paid to a provider or absorbed by your team. Run cost: platform fees, per message or per resolution charges, model usage, and the unglamorous subscriptions around them. Supervise cost: your operator's rota hours at their real loaded rate, the owner's review time, and the escalation humans' interrupted minutes. Fix cost: the mistakes, priced honestly, a rebooked appointment is cheap, a mishandled complaint is not, plus the improvement work of Lesson 24. The worksheet in this lesson totals all four over the same twelve month window for any route, with every assumption printed next to its figure, in the course's house style.

## The worked example discipline

Worked examples are how this course handles money, so be precise about what BrightSmile's numbers are: invented, internally consistent figures for a fictional practice, chosen to be plausible, labelled as assumptions, and useful only as a shape. The shape is the teaching. In the example, over twelve months on the managed route: build is a one off setup fee plus the manager's own scoping time; run is a monthly fee plus per enquiry charges at the audited volume; supervise is the operator's thirty minutes twice a day at a receptionist's loaded rate, which totals to a sum that surprises everyone the first time they compute it; fix is a modest allowance because the pilot's error cost was graded low in Lesson 02. The total is then set against the baseline cost of the current handling in Lesson 23's unit economics, never against a savings percentage.

## Pricing your own shortlist, on the day

This course prints no third party prices, deliberately: platform pricing changes too often for a course to teach, and stale prices are worse than none. Instead, the worksheet has a line for every charge type vendors use (setup, platform, per conversation, per resolution, per seat, overage, exit), and Lesson 10's evaluation requires each finalist to fill it in, in writing, dated. Two questions expose most surprises. What does month thirteen cost if volume doubles (success should not be the expensive scenario)? And what is charged during the pilot if we stop at the gate (the honest pilot price is the price of the information, and it should be known in advance)? A vendor who cannot fill the worksheet is not being mysterious; they are telling you their pricing model cannot survive arithmetic, which is information.

## The running example: BrightSmile Dental

BrightSmile's managed route, twelve months, assumptions as stated in the artifact: setup 1,200 plus manager time, run at 450 per month plus 0.40 per enquiry at 90 a week, supervise at the operator's real hours, fix allowance small. The calculator returns a total in the low five figures, of which run fees are barely half; supervision is roughly a third, which is the single most transferable finding in this course. When the same worksheet was run for the buy route with a platform fee and a part time configurator, the total landed close enough that the decision came back to evidence quality and exit terms, not price. That is what a cost worksheet is for: not to crown the cheap route, but to stop price pretending to be the whole decision.

## Run it

Run `python3 cost_worksheet.py` and read the header before the numbers: every figure traces to a stated assumption. The headline is the supervision share, about a third of total cost, invisible in every vendor quote BrightSmile received.

## Common failures

- **Counting only the invoice..** The platform fee is the cost the vendor chose to show you. Supervision and fix costs are real whether or not they appear on a quote.
- **Using the vendor's volume assumption..** Per unit pricing at the wrong volume is the classic worksheet poison. Volume comes from your Lesson 02 audit, dated.
- **Comparing routes on different windows..** Build looks expensive over three months and cheap over three years. Same window, same four cost families, every route, or the comparison is theatre.

## Recap checklist

- [ ] My worksheet has all four families: build, run, supervise, fix.
- [ ] Every figure traces to a stated assumption or a dated quote.
- [ ] I can name the supervision share of my total, out loud.

## Resources

- [Course glossary](../resources/glossary.md)
