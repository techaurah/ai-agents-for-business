"""Lesson 29: the release check for a finished plan.

Runs the ship routine's verifiable parts: all four sections,
the residue page, review dates, and the first page test fields.
Run: python3 release_check.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def evaluate():
    with open(os.path.join(HERE, "capstone", "plan.json")) as f:
        plan = json.load(f)
    checks = {
        "four_sections": all(k in plan for k in ["readiness", "pilot", "oversight", "scorecard"]),
        "residue_page": bool(plan.get("residue")),
        "review_dates": bool(plan.get("review_dates")),
        "first_page_fields": all(k in plan.get("first_page", {}) for k in
                                 ["process", "question", "route", "gate_date"]),
        "decision_recorded": plan.get("decision") in ("proceed to pilot", "revise and return", "do not deploy"),
    }
    return {"checks": len(checks), "passed": sum(1 for v in checks.values() if v),
            "results": checks, "ready": all(checks.values())}


if __name__ == "__main__":
    r = evaluate()
    for k, v in r["results"].items():
        print(f"{'PASS' if v else 'FAIL'}  {k}")
    print(f"\n{r['passed']}/{r['checks']}: {'READY TO PRESENT AND PUBLISH' if r['ready'] else 'NOT READY'}")
