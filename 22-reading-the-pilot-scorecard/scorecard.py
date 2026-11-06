"""Lesson 22: the pilot scorecard, verdicts computed.

WORKED EXAMPLE results: BrightSmile's pilot, fictional, against
the Lesson 13 thresholds. Verdict per measure: scale, fix, stop.
Run: python3 scorecard.py
"""
RESULTS = [
    # measure, result, scale_line, stop_line, lower_is_better
    ("closed hours first response (min)", 3.1, 5, 30, True),
    ("never answered (%)", 1.4, 2, 6, True),
    ("sampled correctness (%)", 90, 92, 85, False),
    ("escalation rate (%)", 27, 30, 45, True),
]


def verdict(result, scale, stop, lower_better):
    if lower_better:
        if result <= scale:
            return "scale"
        return "stop" if result > stop else "fix"
    if result >= scale:
        return "scale"
    return "stop" if result < stop else "fix"


def evaluate():
    vs = {name: verdict(r, s, st, lb) for name, r, s, st, lb in RESULTS}
    overall = "stop" if "stop" in vs.values() else ("fix and rerun" if "fix" in vs.values() else "scale")
    return {"verdicts": vs, "overall": overall, "measures": len(RESULTS)}


if __name__ == "__main__":
    r = evaluate()
    for name, v in r["verdicts"].items():
        print(f"{v:5s}  {name}")
    print(f"\nOverall: {r['overall']}. One rerun, new gate date, then the Lesson 25 decision.")
