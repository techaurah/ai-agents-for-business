"""Lesson 12: the pilot scope as checkable data.

A scope is complete when it states its question, window,
channels, in scope paths, exclusions by name, and its gate.
Run: python3 pilot_scope.py
"""
SCOPE = {
    "question": "Can an agent give a correct first response on the standard path within five minutes, in closed hours, at a carryable escalation rate?",
    "weeks": 4,
    "channels": ["web form", "instagram"],
    "in_scope": ["standard path enquiries per the Lesson 04 map"],
    "exclusions": ["phone", "clinical content", "complaints",
                   "treatment questions from existing patients", "payments"],
    "gate": {"decision_meeting_booked": True, "thresholds_set_in_lesson": 13,
             "chair": "owner", "scorecard_presenter": "operator"},
}

REQUIRED = ["question", "weeks", "channels", "in_scope", "exclusions", "gate"]


def evaluate():
    missing = [k for k in REQUIRED if not SCOPE.get(k)]
    return {"complete": not missing, "missing": missing,
            "exclusions": len(SCOPE["exclusions"]), "channels": len(SCOPE["channels"]),
            "weeks": SCOPE["weeks"]}


if __name__ == "__main__":
    r = evaluate()
    print("Question:", SCOPE["question"])
    print(f"Window: {r['weeks']} weeks. Channels: {r['channels']}. Exclusions: {r['exclusions']} named.")
    print("SCOPE COMPLETE" if r["complete"] else f"MISSING: {r['missing']}")
