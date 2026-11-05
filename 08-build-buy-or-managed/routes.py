"""Lesson 08: build, buy, or managed, scored on your facts.

Criteria are scored 1 (poor fit) to 5 (strong fit) per route for
the BrightSmile fact pattern in the lesson: standard process,
no technical staff, mixed readiness. Weights reflect what the
lesson says separates the routes. Run: python3 routes.py
"""
CRITERIA = [
    # name, weight, build, buy, managed
    ("Process is standard, not idiosyncratic", 2, 2, 5, 5),
    ("Team can maintain prompts, rules, integrations", 3, 1, 3, 5),
    ("Data stays where readiness grades require", 2, 5, 2, 3),
    ("Cost of leaving in month thirteen is low", 2, 4, 3, 2),
    ("Speed to a supervised pilot", 1, 2, 4, 5),
]


def evaluate():
    totals = {"build": 0, "buy": 0, "managed": 0}
    for _name, w, b, u, m in CRITERIA:
        totals["build"] += w * b
        totals["buy"] += w * u
        totals["managed"] += w * m
    best = max(totals, key=totals.get)
    return {"totals": totals, "best": best, "criteria": len(CRITERIA)}


if __name__ == "__main__":
    r = evaluate()
    for k, v in r["totals"].items():
        print(f"{k:8s} {v}")
    print(f"\nBest fit on these facts: {r['best']}. Change the facts (a developer on staff) and the answer moves.")
