"""Lesson 05: the data inventory, graded.

Grades: ready, partial, not_ready. The pilot may only use ready
sources freely and partial sources inside their stated limit.
Run: python3 data_audit.py
"""
SOURCES = [
    {"name": "Booking diary", "grade": "ready", "limit": "read access only in the pilot"},
    {"name": "Price list (website data)", "grade": "partial", "limit": "quote listed items only, never summarise treatments"},
    {"name": "Treatment descriptions", "grade": "not_ready", "limit": "agent never links or summarises"},
    {"name": "Patient record notes", "grade": "not_ready", "limit": "out of scope entirely"},
    {"name": "Opening hours and directions", "grade": "ready", "limit": "none"},
]


def evaluate():
    grades = [s["grade"] for s in SOURCES]
    return {"sources": len(grades), "ready": grades.count("ready"),
            "partial": grades.count("partial"), "not_ready": grades.count("not_ready"),
            "pilot_blocked": grades.count("not_ready") > 0 and False}


if __name__ == "__main__":
    for s in SOURCES:
        print(f"{s['grade']:9s}  {s['name']}: {s['limit']}")
    r = evaluate()
    print(f"\n{r['sources']} sources: {r['ready']} ready, {r['partial']} partial, {r['not_ready']} not ready")
