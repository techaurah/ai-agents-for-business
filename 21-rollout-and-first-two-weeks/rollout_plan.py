"""Lesson 21: the rollout plan and the daily rhythm.

Checks the plan carries its non negotiables: briefing before
launch, daily sampling size, owner check ins, fallback rostered,
surge holding reply ready. Run: python3 rollout_plan.py
"""
PLAN = {
    "briefing_before_launch": True,
    "sample_per_morning": 20,
    "owner_checkins_week1": 5,
    "owner_takes_a_window": True,
    "fallback_rostered_on_paper": True,
    "surge_holding_reply_approved": True,
    "launch_week": "ordinary",
    "interim_team_note_day": 10,
}


def evaluate():
    missing = [k for k, v in PLAN.items() if v is True and False]
    flags = [k for k in ["briefing_before_launch", "owner_takes_a_window",
                         "fallback_rostered_on_paper", "surge_holding_reply_approved"]
             if not PLAN[k]]
    return {"checks": len(PLAN), "missing_flags": flags,
            "ready": not flags and PLAN["launch_week"] == "ordinary",
            "sample": PLAN["sample_per_morning"]}


if __name__ == "__main__":
    r = evaluate()
    print(f"Rollout checks: {r['checks']}, blocking flags: {r['missing_flags']}")
    print(f"Morning sample: {r['sample']} replies. Launch week: {PLAN['launch_week']}.")
    print("ROLLOUT READY" if r["ready"] else "FIX THE FLAGS BEFORE LAUNCH")
