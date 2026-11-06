"""Lesson 28: the plan stress test, scored against plan lines.

Each stressor case scores handled, gap, or unhandled, and must
cite the plan element that earns the score. No citation, no
credit: the checker enforces it. Run: python3 stress_test.py
"""
CASES = [
    {"stressor": "hostile", "case": "injected instruction in an enquiry", "score": "handled", "plan_line": "job description never 5; access scope"},
    {"stressor": "hostile", "case": "phone call claiming owner authority to widen scope", "score": "handled", "plan_line": "scope changes are written only"},
    {"stressor": "hostile", "case": "staff paste an unvetted price list", "score": "gap", "plan_line": "price source edit rights, added by this test"},
    {"stressor": "failure", "case": "provider down for a day", "score": "handled", "plan_line": "fallback rostered, Lesson 21 rhythm"},
    {"stressor": "failure", "case": "diary feed silently stale", "score": "gap", "plan_line": "morning reconciliation, added by this test"},
    {"stressor": "volume", "case": "double arrivals and escalations", "score": "handled", "plan_line": "surge rule, follow ups pause first"},
    {"stressor": "time", "case": "operator leaves at month nine", "score": "handled", "plan_line": "backup operator drilled unaided"},
]


def evaluate():
    cited = all(c["plan_line"] for c in CASES)
    return {"cases": len(CASES), "handled": sum(1 for c in CASES if c["score"] == "handled"),
            "gaps": sum(1 for c in CASES if c["score"] == "gap"),
            "unhandled": sum(1 for c in CASES if c["score"] == "unhandled"),
            "all_cited": cited, "stressors": len({c["stressor"] for c in CASES})}


if __name__ == "__main__":
    for c in CASES:
        print(f"{c['score']:9s} [{c['stressor']}] {c['case']}\n            plan: {c['plan_line']}")
    r = evaluate()
    print(f"\n{r['handled']} handled, {r['gaps']} gaps fixed in plan, {r['unhandled']} unhandled, across {r['stressors']} stressors")
