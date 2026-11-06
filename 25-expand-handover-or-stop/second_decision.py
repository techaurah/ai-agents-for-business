"""Lesson 25: the second decision, deltas scored by ceremony.

Expansion types carry different risk, so they carry different
gates. Light: hours or volume deltas. Full: any move of the
bounded judgement frontier. Run: python3 second_decision.py
"""
PROPOSALS = [
    {"proposal": "Add second location enquiries", "kind": "volume", "gate": "light"},
    {"proposal": "Extend agent hours to all day", "kind": "hours", "gate": "light"},
    {"proposal": "Add insurance question handling", "kind": "scope_frontier", "gate": "full"},
    {"proposal": "Move standard path to line ownership", "kind": "handover", "gate": "record"},
    {"proposal": "Stop the follow up experiment", "kind": "stop", "gate": "record"},
]


def evaluate():
    return {"proposals": len(PROPOSALS),
            "full_gate": [p["proposal"] for p in PROPOSALS if p["gate"] == "full"],
            "light": sum(1 for p in PROPOSALS if p["gate"] == "light"),
            "records": sum(1 for p in PROPOSALS if p["gate"] == "record")}


if __name__ == "__main__":
    for p in PROPOSALS:
        print(f"{p['gate']:6s} gate  {p['proposal']}")
    r = evaluate()
    print(f"\nFull gate (new sampling, filter, acceptance cases): {r['full_gate']}")
