"""Lesson 06: the access plan, checked for least privilege.

Bands: read, write_record (writes inside the business, logged),
external (reaches outside: sends, charges, deletes). External
items must each be decided in the escalation policy, by name.
Run: python3 access_plan.py
"""
ACCESS = [
    {"system": "Enquiry inboxes", "band": "write_record", "decided": True},
    {"system": "Booking diary", "band": "read", "decided": True},
    {"system": "Messaging (standard path sends)", "band": "external", "decided": True},
    {"system": "Patient record system", "band": "none", "decided": True},
    {"system": "Payments", "band": "none", "decided": True},
    {"system": "Social posting", "band": "external", "decided": False},
]


def evaluate():
    external = [a for a in ACCESS if a["band"] == "external"]
    undecided = [a["system"] for a in external if not a["decided"]]
    return {"systems": len(ACCESS), "external": len(external),
            "undecided_external": undecided, "least_privilege_ok": not undecided,
            "no_access": sum(1 for a in ACCESS if a["band"] == "none")}


if __name__ == "__main__":
    for a in ACCESS:
        print(f"{a['band']:12s}  {a['system']} (policy decided: {a['decided']})")
    r = evaluate()
    print(f"\nExternal access items: {r['external']}; undecided: {r['undecided_external']}")
    print("Plan is NOT pilot ready until every external item is decided by name." if r["undecided_external"]
          else "Least privilege check passes.")
