"""Lesson 10: the vendor evaluation scoresheet.

Criteria and weights fixed BEFORE demos (the lesson's rule).
Scores are evidence based, 0 (claim only) to 5 (seen working on
our cases). Worked example: BrightSmile's two finalists.
Run: python3 vendor_score.py
"""
CRITERIA = [
    # name, weight, provider A, provider B
    ("Escalation on residue cases, seen live", 3, 1, 5),
    ("Reporting: raw monthly export, on request", 3, 2, 5),
    ("Data location fits readiness grades", 2, 3, 4),
    ("Diary integration without record access", 2, 4, 3),
    ("Exit terms: data and history out, in writing", 2, 2, 4),
    ("Price transparency: all lines named", 1, 3, 4),
]


def evaluate():
    a = sum(w * s for _n, w, s, _b in [(c[0], c[1], c[2], c[3]) for c in CRITERIA])
    b = sum(c[1] * c[3] for c in CRITERIA)
    return {"criteria": len(CRITERIA), "provider_a": a, "provider_b": b,
            "winner": "B" if b > a else "A"}


if __name__ == "__main__":
    for name, w, a, b in CRITERIA:
        print(f"w{w}  A:{a} B:{b}  {name}")
    r = evaluate()
    print(f"\nTotals: A {r['provider_a']}, B {r['provider_b']}. Winner on evidence: {r['winner']}")
    print("Trust column stays blank until after the pilot, on purpose.")
