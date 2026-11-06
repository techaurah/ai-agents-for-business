"""Lesson 27: the plan cross checker.

Checks the seams between sections: scope exclusions match the
job description, escalation destinations are named in readiness,
scorecard measures exist in the baseline. Run on the worked
example plan in capstone/. Run: python3 cross_check.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def evaluate():
    with open(os.path.join(HERE, "capstone", "plan.json")) as f:
        plan = json.load(f)
    checks = {
        "exclusions_match": plan["scope_exclusions"] == plan["job_exclusions"],
        "destinations_named": set(plan["escalation_destinations"]) <= set(plan["roles_named"]),
        "measures_match": plan["scorecard_measures"] == plan["baseline_measures"],
        "tools_within_access": set(plan["job_tools"]) <= set(plan["access_systems"]),
    }
    return {"checks": len(checks), "passed": sum(1 for v in checks.values() if v),
            "results": checks, "all_pass": all(checks.values())}


if __name__ == "__main__":
    r = evaluate()
    for k, v in r["results"].items():
        print(f"{'PASS' if v else 'FAIL'}  {k}")
    print(f"\n{r['passed']}/{r['checks']} cross checks pass")
