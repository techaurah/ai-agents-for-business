"""Lesson 07: the roles sheet, completeness checked.

A deployment is people ready when owner, operator, backup
operator, and every escalation destination are named people,
and the operator's hours are in a rota, not in goodwill.
Run: python3 roles.py
"""
ROLES = {
    "owner": "Practice manager",
    "operator": "Senior receptionist",
    "backup_operator": "Junior receptionist",
    "operator_hours_in_rota": True,
    "escalations": {
        "clinical_or_emotional": "Practice manager",
        "diary_conflict": "Senior receptionist",
        "technical_failure": "Vendor contact, owner copied",
    },
}


def evaluate():
    missing = [k for k in ["owner", "operator", "backup_operator"] if not ROLES.get(k)]
    return {"named_roles": 3 - len(missing), "missing": missing,
            "escalation_routes": len(ROLES["escalations"]),
            "hours_in_rota": ROLES["operator_hours_in_rota"],
            "people_ready": not missing and ROLES["operator_hours_in_rota"]}


if __name__ == "__main__":
    r = evaluate()
    print(f"Named roles: {r['named_roles']}/3, escalation routes: {r['escalation_routes']}, "
          f"operator hours in rota: {r['hours_in_rota']}")
    print("PEOPLE READY" if r["people_ready"] else f"NOT READY, missing: {r['missing']}")
