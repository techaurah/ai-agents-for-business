"""Lesson 19: the lead response twin.

A standard library simulation of one pilot week at BrightSmile.
Assumptions, stated: 90 enquiries, 78 percent standard path
(Lesson 13 baseline); escalations are the residue plus draft rung
cases, 30 percent of total at base rate; operator capacity is two
30 minute windows at 6 minutes per queued case (100 minutes of
queue time per day across 5 working days is NOT assumed; the rota
gives 60 min/day, 5 days). The agent is not simulated; the
operation around it is. Run: python3 lead_response_twin.py
"""
import random

WEEK = {"arrivals": 90, "standard_pct": 78, "escalation_pct": 30,
        "operator_minutes_per_day": 60, "minutes_per_case": 6, "days": 5}


def simulate(escalation_pct, arrivals=None, seed=7):
    rng = random.Random(seed)
    total = arrivals if arrivals is not None else WEEK["arrivals"]
    per_day = [total // WEEK["days"]] * WEEK["days"]
    capacity = WEEK["operator_minutes_per_day"] // WEEK["minutes_per_case"]
    queue, worst_backlog = 0, 0
    for day_arrivals in per_day:
        queue += round(day_arrivals * escalation_pct / 100)
        queue = max(0, queue - capacity)
        worst_backlog = max(worst_backlog, queue)
    handled_by_agent = round(total * WEEK["standard_pct"] / 100)
    return {"arrivals": total, "escalations": round(total * escalation_pct / 100),
            "capacity_per_day": capacity, "end_backlog": queue,
            "worst_backlog": worst_backlog, "clears": queue == 0,
            "agent_handled_standard": handled_by_agent}


def evaluate():
    base = simulate(WEEK["escalation_pct"])
    stressed = simulate(60)
    surge = simulate(WEEK["escalation_pct"], arrivals=180)
    return {"base_clears": base["clears"], "base_escalations": base["escalations"],
            "stressed_clears": stressed["clears"], "surge_clears": surge["clears"],
            "capacity_per_day": base["capacity_per_day"]}


if __name__ == "__main__":
    for label, args in [("base case", {}), ("double escalation rate", {"escalation_pct": 60}),
                        ("double volume", {"arrivals": 180})]:
        r = simulate(**{**{"escalation_pct": WEEK["escalation_pct"]}, **args})
        print(f"{label}: arrivals {r['arrivals']}, escalations {r['escalations']}, "
              f"end backlog {r['end_backlog']}, clears: {r['clears']}")
    print("\nDouble volume breaks the rota in the base design: the surge rule (pause follow ups first) goes in the pilot file.")
