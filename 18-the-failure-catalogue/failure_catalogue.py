"""Lesson 18: the failure catalogue, completeness checked.

Every entry needs detection, first hour response, and one owner.
Run: python3 failure_catalogue.py
"""
CATALOGUE = [
    {"name": "Confident wrong answer", "detection": "sampled morning review", "response": "pause path, fix data, correct affected customers", "owner": "operator"},
    {"name": "Tone failure", "detection": "review sample", "response": "edit tone examples, spot check", "owner": "owner"},
    {"name": "Message loop", "detection": "failures counter and volume alarm", "response": "pause agent, untangle threads manually", "owner": "operator"},
    {"name": "Silent stall", "detection": "daily heartbeat and queue check", "response": "vendor route, manual fallback on", "owner": "operator"},
    {"name": "Boundary leak", "detection": "review or customer report", "response": "incident process, disclose as required", "owner": "owner"},
    {"name": "Scope creep", "detection": "monthly scope review", "response": "revert the change, record it", "owner": "owner"},
    {"name": "Provider outage", "detection": "heartbeat and vendor status", "response": "manual fallback, notify waiting customers", "owner": "operator"},
    {"name": "Success overload", "detection": "scorecard supervision line", "response": "expand decision, not silent decay", "owner": "owner"},
]


def evaluate():
    incomplete = [e["name"] for e in CATALOGUE
                  if not (e["detection"] and e["response"] and e["owner"])]
    return {"entries": len(CATALOGUE), "incomplete": incomplete,
            "operator_owned": sum(1 for e in CATALOGUE if e["owner"] == "operator"),
            "owner_owned": sum(1 for e in CATALOGUE if e["owner"] == "owner")}


if __name__ == "__main__":
    for e in CATALOGUE:
        print(f"{e['name']}: notice by {e['detection']}; first hour: {e['response']}; owner: {e['owner']}")
    r = evaluate()
    print(f"\n{r['entries']} entries, incomplete: {r['incomplete']}")
