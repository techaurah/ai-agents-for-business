"""Lesson 01: agent, chatbot, or workflow? A decision drill.

Classifies described systems by who decides the next step.
Run: python3 classify.py
"""
SYSTEMS = [
    {"name": "Nightly report that emails yesterday's bookings at 7am",
     "acts": True, "model_chooses_steps": False, "only_answers": False},
    {"name": "Website widget answering opening hours from an approved FAQ",
     "acts": False, "model_chooses_steps": False, "only_answers": True},
    {"name": "Enquiry handler that reads each message, picks a path, checks the diary, drafts or escalates",
     "acts": True, "model_chooses_steps": True, "only_answers": False},
    {"name": "Workflow that uses a model step to label enquiries, then routes by fixed rules",
     "acts": True, "model_chooses_steps": False, "only_answers": False},
    {"name": "Assistant that researches a supplier, compares options, and prepares a purchase for approval",
     "acts": True, "model_chooses_steps": True, "only_answers": False},
]


def classify(s):
    if s["only_answers"] or not s["acts"]:
        return "chatbot"
    if s["model_chooses_steps"]:
        return "agent"
    return "workflow"


def evaluate():
    kinds = [classify(s) for s in SYSTEMS]
    return {"systems": len(kinds), "agents": kinds.count("agent"),
            "workflows": kinds.count("workflow"), "chatbots": kinds.count("chatbot"),
            "kinds": kinds}


if __name__ == "__main__":
    for s in SYSTEMS:
        print(f"{classify(s):9s}  {s['name']}")
    r = evaluate()
    print(f"\n{r['systems']} systems: {r['agents']} agents, {r['workflows']} workflows, {r['chatbots']} chatbots")
