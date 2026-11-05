"""Lesson 09: the framework landscape as buyer data.

Facts as surveyed 2026-11-06 (see RESEARCH.md): names, one line
buyers can use, and the property that decides fit. This is a map
for asking questions, not a ranking. Run: python3 framework_map.py
"""
FRAMEWORKS = [
    {"name": "LangGraph", "shape": "graph of steps, explicit durable state",
     "fit": "clear steps, approvals, audit trail", "watch": "more assembly required"},
    {"name": "CrewAI", "shape": "role based crews and flows",
     "fit": "readable multi agent prototypes", "watch": "add your own state and eval rigour"},
    {"name": "Microsoft Agent Framework", "shape": "Microsoft's current agent SDK line, Python and .NET",
     "fit": "Microsoft aligned estates", "watch": "AutoGen proposals need a dated explanation"},
    {"name": "Platform agent builders", "shape": "agent features inside a CRM or helpdesk you already pay for",
     "fit": "standard processes inside that platform", "watch": "data location and exit cost"},
]

QUESTIONS = ["Where does the state live?", "Where do approvals live?",
             "How do we test a change?", "What does migration cost?"]


def evaluate():
    return {"frameworks": len(FRAMEWORKS), "questions": len(QUESTIONS),
            "names": [f["name"] for f in FRAMEWORKS]}


if __name__ == "__main__":
    for f in FRAMEWORKS:
        print(f"{f['name']}\n  shape: {f['shape']}\n  fits: {f['fit']}\n  watch: {f['watch']}")
    print("\nAsk every builder:")
    for q in QUESTIONS:
        print(" -", q)
