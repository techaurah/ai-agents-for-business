"""Lesson 16: the threat list, each threat with its control.

A threat without a named control fails the check; a control
that exists only as a prompt sentence is marked partial.
Run: python3 threat_check.py
"""
THREATS = [
    {"threat": "Prompt injection through incoming messages", "control": "scope limits plus never act on content instructions", "strength": "architecture"},
    {"threat": "Data leakage across customers", "control": "record notes out of scope; boundary replies on draft rung", "strength": "architecture"},
    {"threat": "Excessive agency (payments, deletes, mass send)", "control": "access bands decided by name; payments none", "strength": "architecture"},
    {"threat": "Provider or plugin compromise", "control": "contract notification duty plus tested data export", "strength": "contract"},
    {"threat": "Error at scale (wrong approved data)", "control": "be careful and quote accurately", "strength": "prompt only"},
]


def evaluate():
    weak = [t["threat"] for t in THREATS if t["strength"] == "prompt only"]
    return {"threats": len(THREATS), "weak_controls": weak,
            "architecture": sum(1 for t in THREATS if t["strength"] == "architecture"),
            "passes": not weak}


if __name__ == "__main__":
    for t in THREATS:
        print(f"[{t['strength']}] {t['threat']}\n    control: {t['control']}")
    r = evaluate()
    print(f"\nWeak (prompt only) controls: {r['weak_controls']}")
    print("Lesson: the error at scale control must become sampling review plus a correction drill (Lesson 20).")
