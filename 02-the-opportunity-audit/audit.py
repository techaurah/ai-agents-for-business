"""Lesson 02: the opportunity audit, scored.

Scores candidate processes on volume, waiting cost, bounded
judgement, and error cost (which subtracts). Worked example
figures are BrightSmile Dental's, from the lesson: a fictional
practice, a two week front desk tally doubled, assumptions stated
in the lesson text. Run: python3 audit.py
"""
PROCESSES = [
    {"name": "Enquiry first response and follow up", "volume_wk": 90,
     "waiting": 5, "bounded": 5, "error_cost": 1},
    {"name": "Recall reminders for checkups", "volume_wk": 120,
     "waiting": 2, "bounded": 1, "error_cost": 1},
    {"name": "Review requests and replies", "volume_wk": 35,
     "waiting": 2, "bounded": 4, "error_cost": 2},
    {"name": "Invoice and payment plan chasing", "volume_wk": 25,
     "waiting": 3, "bounded": 3, "error_cost": 3},
    {"name": "Treatment plan explanations", "volume_wk": 12,
     "waiting": 2, "bounded": 1, "error_cost": 5},
]


def score(p):
    volume_pts = min(p["volume_wk"] // 20, 5)
    return volume_pts + p["waiting"] + p["bounded"] - (p["error_cost"] * 2)


def evaluate():
    ranked = sorted(((score(p), p["name"]) for p in PROCESSES), reverse=True)
    return {"processes": len(ranked), "top": ranked[0][1], "top_score": ranked[0][0],
            "bottom": ranked[-1][1], "ranking": [name for _s, name in ranked]}


if __name__ == "__main__":
    r = evaluate()
    for s, name in sorted(((score(p), p["name"]) for p in PROCESSES), reverse=True):
        print(f"{s:3d}  {name}")
    print(f"\nTop candidate: {r['top']} ({r['top_score']}). Last: {r['bottom']}.")
    print("Note: recall reminders score on volume but need no judgement: a workflow job, Lesson 01.")
