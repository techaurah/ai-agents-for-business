"""Lesson 15: the escalation policy checker.

Rungs: act, draft, ask, escalate. Rules are evaluated in order;
mixed content drops a rung; a second failure escalates outright.
Run: python3 escalation_policy.py
"""
CASES = [
    {"kind": "standard_price_question", "mixed": False, "failures": 0},
    {"kind": "checkup_booking", "mixed": False, "failures": 0},
    {"kind": "booking_plus_symptom_worry", "mixed": True, "failures": 0},
    {"kind": "discount_request", "mixed": False, "failures": 0},
    {"kind": "clinical_question", "mixed": False, "failures": 0},
    {"kind": "complaint", "mixed": False, "failures": 0},
    {"kind": "standard_price_question", "mixed": False, "failures": 2},
]
ESCALATE_KINDS = {"clinical_question", "complaint", "distress", "child_in_pain"}
ASK_KINDS = {"discount_request", "out_of_hours_offer", "channel_switch"}
DRAFT_KINDS = {"treatment_suitability", "weekly_summary"}


def rung(case):
    if case["failures"] >= 2 or case["kind"] in ESCALATE_KINDS:
        return "escalate"
    if case["kind"] in ASK_KINDS:
        return "ask"
    if case["kind"] in DRAFT_KINDS or case["mixed"]:
        return "draft"
    return "act"


def evaluate():
    rungs = [rung(c) for c in CASES]
    return {"cases": len(rungs), "act": rungs.count("act"), "draft": rungs.count("draft"),
            "ask": rungs.count("ask"), "escalate": rungs.count("escalate"), "rungs": rungs}


if __name__ == "__main__":
    for c in CASES:
        print(f"{rung(c):9s}  {c['kind']} (mixed={c['mixed']}, failures={c['failures']})")
    r = evaluate()
    print(f"\n{r['cases']} cases: {r['act']} act, {r['draft']} draft, {r['ask']} ask, {r['escalate']} escalate")
