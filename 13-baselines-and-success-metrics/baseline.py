"""Lesson 13: the baseline sheet and its targets.

WORKED EXAMPLE figures: BrightSmile's two ordinary weeks, from
the lesson (inbox timestamps and a front desk tally), fictional
practice, assumptions as stated there. Run: python3 baseline.py
"""
BASELINE = {
    "enquiries_per_week": 90,
    "median_first_response_hours": 4.8,
    "never_answered_pct": 11,
    "standard_path_pct": 78,
    "sampled_correct_pct": 92,
}
TARGETS = {
    "closed_hours_first_response_minutes": {"scale": 5, "stop": 30},
    "never_answered_pct": {"scale": 2, "stop": 6},
    "sampled_correct_pct": {"scale": 92, "stop": 85},
    "escalation_pct": {"scale_max": 30, "stop": 45},
}


def evaluate():
    return {"measures": len(BASELINE), "targets": len(TARGETS),
            "never_answered_baseline": BASELINE["never_answered_pct"],
            "standard_path_pct": BASELINE["standard_path_pct"]}


if __name__ == "__main__":
    print("Baseline (two ordinary weeks):")
    for k, v in BASELINE.items():
        print(f"  {k}: {v}")
    print("Targets set in advance (scale line / stop line):")
    for k, v in TARGETS.items():
        print(f"  {k}: {v}")
    print("\nThe sheet is signed before the pilot starts. Lesson 22 grades against it.")
