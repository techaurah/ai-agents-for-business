"""Lesson 24: the monthly review, agenda enforced.

Five standing items; the review is complete only when each is
present and exactly one improvement is chosen and gated.
Run: python3 monthly_review.py
"""
REVIEW = {
    "scorecard_reviewed": True,
    "catalogue_entries_added_or_edited": 1,
    "scope_checked_against_no_list": True,
    "acceptance_set_updated_and_run": True,
    "acceptance_cases": 42,
    "operator_health_checked": True,
    "provider_export_tested": True,
    "improvements_chosen": ["diary conflict sub case: ask rung to draft rung"],
    "improvement_gated_through_acceptance_set": True,
}


def evaluate():
    items = [REVIEW["scorecard_reviewed"], REVIEW["scope_checked_against_no_list"],
             REVIEW["acceptance_set_updated_and_run"], REVIEW["operator_health_checked"],
             REVIEW["provider_export_tested"]]
    return {"items_present": sum(1 for i in items if i), "items": len(items),
            "one_improvement": len(REVIEW["improvements_chosen"]) == 1,
            "gated": REVIEW["improvement_gated_through_acceptance_set"],
            "complete": all(items) and len(REVIEW["improvements_chosen"]) == 1
                        and REVIEW["improvement_gated_through_acceptance_set"]}


if __name__ == "__main__":
    r = evaluate()
    print(f"Agenda items present: {r['items_present']}/{r['items']}; improvements chosen: {len(REVIEW['improvements_chosen'])}; gated: {r['gated']}")
    print("REVIEW COMPLETE" if r["complete"] else "REVIEW INCOMPLETE")
