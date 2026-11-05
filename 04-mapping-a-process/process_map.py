"""Lesson 04: a one page process map as data.

BrightSmile's enquiry handling, mapped from five cases in the
lesson. Steps carry their kind; waits carry hours.
Run: python3 process_map.py
"""
STEPS = [
    ("Enquiry lands in one of three inboxes", "step", 0),
    ("Wait until a person notices", "wait", 5.0),
    ("DECIDE: standard path, or not", "decision", 0),
    ("Check the diary in the second system", "step", 0),
    ("Reply with answer or proposed times", "step", 0),
    ("DECIDE: anything clinical or emotional goes to the manager", "decision", 0),
    ("HANDOVER: manager replies", "handover", 3.0),
    ("DECIDE: no reply in a day, chase once then stop", "decision", 0),
]


def evaluate():
    kinds = [k for _n, k, _w in STEPS]
    return {"steps": len(STEPS), "decisions": kinds.count("decision"),
            "handovers": kinds.count("handover"),
            "wait_hours": sum(w for _n, _k, w in STEPS)}


if __name__ == "__main__":
    for name, kind, wait in STEPS:
        tag = f" [{kind}, waits {wait}h]" if kind in ("wait", "handover") else f" [{kind}]"
        print("-", name + tag)
    r = evaluate()
    print(f"\n{r['steps']} stages, {r['decisions']} decisions, {r['handovers']} handover, "
          f"{r['wait_hours']}h of waiting in a process with about 9 minutes of work.")
