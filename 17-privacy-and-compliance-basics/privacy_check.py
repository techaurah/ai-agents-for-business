"""Lesson 17: the owner's privacy and disclosure checklist.

Five artefacts: disclosure, data map, retention, human route,
review date. Orientation only, not legal advice; the lesson says
so and so does this file. Run: python3 privacy_check.py
"""
CHECKLIST = {
    "disclosure_line_approved": True,
    "data_map_attached": True,
    "retention_rule_written": True,
    "human_route_in_every_message": True,
    "review_date_set": True,
    "professional_adviser_consulted": False,
}


def evaluate():
    done = sum(1 for v in CHECKLIST.values() if v)
    core = all(CHECKLIST[k] for k in list(CHECKLIST)[:5])
    return {"items": len(CHECKLIST), "done": done, "core_complete": core,
            "open": [k for k, v in CHECKLIST.items() if not v]}


if __name__ == "__main__":
    for k, v in CHECKLIST.items():
        print(f"{'done' if v else 'OPEN'}  {k}")
    r = evaluate()
    print(f"\nCore artefacts complete: {r['core_complete']}. Open: {r['open']}")
    print("The open item is deliberate in the worked example: book the adviser before launch, not after.")
