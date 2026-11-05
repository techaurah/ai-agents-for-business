"""Lesson 11: the honest cost worksheet.

WORKED EXAMPLE, assumptions stated, fictional business.
BrightSmile Dental, managed route, 12 months:
- setup fee 1200 once, plus 12 manager hours at 40/hour scoping
- platform and service fee 450/month
- per enquiry charge 0.40, at 90 enquiries/week, 52 weeks
- operator supervision 1 hour/day, 260 days, at 22/hour loaded
- owner review 1 hour/month at 40/hour
- fix allowance 600/year (Lesson 02 graded error cost low)
Currencies are plain units; substitute your own quotes, dated.
Run: python3 cost_worksheet.py
"""
MONTHS = 12


def evaluate():
    build = 1200 + 12 * 40
    run = 450 * MONTHS + 0.40 * 90 * 52
    supervise = 1 * 260 * 22 + 1 * MONTHS * 40
    fix = 600
    total = build + run + supervise + fix
    return {"build": build, "run": round(run), "supervise": supervise,
            "fix": fix, "total": round(total),
            "supervise_share_pct": round(100 * supervise / total)}


if __name__ == "__main__":
    r = evaluate()
    for k in ["build", "run", "supervise", "fix"]:
        print(f"{k:10s} {r[k]:>8,}")
    print(f"{'total':10s} {r['total']:>8,}  (supervision is {r['supervise_share_pct']}% of it)")
    print("Assumptions are in the file header. Your quotes, your volume, your rates.")
