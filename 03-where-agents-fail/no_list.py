"""Lesson 03: the no list filter.

Applies the stakes, reversibility, and judgement tests to
candidate jobs. A job failing any test is out; a job failing the
judgement test only may still work as human assist.
Run: python3 no_list.py
"""
JOBS = [
    {"name": "First reply to a standard enquiry", "stakes_ok": True, "reversible": True, "judgement_bounded": True},
    {"name": "Reassuring a patient about symptoms", "stakes_ok": False, "reversible": True, "judgement_bounded": False},
    {"name": "Handling a treatment complaint end to end", "stakes_ok": True, "reversible": False, "judgement_bounded": False},
    {"name": "Drafting a complaint reply for the manager", "stakes_ok": True, "reversible": True, "judgement_bounded": False},
    {"name": "Quoting a price for unexamined treatment", "stakes_ok": True, "reversible": False, "judgement_bounded": True},
    {"name": "Chasing an unpaid invoice politely", "stakes_ok": True, "reversible": True, "judgement_bounded": True},
]


def verdict(j):
    if not j["stakes_ok"]:
        return "no: stakes"
    if not j["reversible"]:
        return "no: not reversible"
    if not j["judgement_bounded"]:
        return "assist only"
    return "agent candidate"


def evaluate():
    out = {j["name"]: verdict(j) for j in JOBS}
    return {"jobs": len(out), "candidates": sum(1 for v in out.values() if v == "agent candidate"),
            "assist": sum(1 for v in out.values() if v == "assist only"),
            "refused": sum(1 for v in out.values() if v.startswith("no")), "verdicts": out}


if __name__ == "__main__":
    for j in JOBS:
        print(f"{verdict(j):18s}  {j['name']}")
    r = evaluate()
    print(f"\n{r['candidates']} agent candidates, {r['assist']} assist only, {r['refused']} refused")
