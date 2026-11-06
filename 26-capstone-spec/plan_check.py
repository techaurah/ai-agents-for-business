"""Lesson 26: the capstone plan skeleton, gate checked.

The plan has four sections; each gate has required keys.
Run: python3 plan_check.py, then copy capstone/plan.json as
your starting skeleton in Lesson 27.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
GATES = {
    "readiness": ["data_grades", "access_decisions", "roles_named", "route_decision"],
    "pilot": ["question", "exclusions", "baseline", "thresholds", "job_description"],
    "oversight": ["escalation_policy", "threat_list", "privacy_checklist", "failure_catalogue"],
    "scorecard": ["measures_match_baseline", "verdict_rules", "unit_economics_method", "monthly_agenda"],
}


def evaluate():
    with open(os.path.join(HERE, "capstone", "plan.json")) as f:
        plan = json.load(f)["deployment_plan"]
    missing = {s: [k for k in keys if k not in plan.get(s, {})]
               for s, keys in GATES.items()}
    return {"sections": len(GATES), "complete": all(not m for m in missing.values()),
            "missing": {s: m for s, m in missing.items() if m},
            "required_keys": sum(len(v) for v in GATES.values())}


if __name__ == "__main__":
    r = evaluate()
    print(f"Sections: {r['sections']}, required keys: {r['required_keys']}, missing: {r['missing']}")
    print("This skeleton is the format. Lesson 27 fills it with a real process.")
