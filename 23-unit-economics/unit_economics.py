"""Lesson 23: unit economics, symmetrically computed.

WORKED EXAMPLE, assumptions stated. Manual: 9 minutes of work
(Lesson 04 map) at 22/hour loaded, plus 1.2 minutes of manager
checking at 40/hour, per handled enquiry. Agent, per 4 week
pilot: run 450/month plus 0.40 per enquiry at 360 enquiries,
operator 20 hours at 22/hour, owner 1 hour at 40, fix 50, build
share (setup 1680 spread over 12 months, one month counted).
Escalations are counted as human handled under BOTH systems.
Run: python3 unit_economics.py
"""


def evaluate():
    manual = 9 * 22 / 60 + 1.2 * 40 / 60
    agent_total = 450 + 0.40 * 360 + 20 * 22 + 1 * 40 + 50 + 1680 / 12
    agent_units = 360
    agent = agent_total / agent_units
    return {"manual_per_enquiry": round(manual, 2), "agent_per_enquiry": round(agent, 2),
            "agent_total": round(agent_total), "units": agent_units,
            "cheaper": "agent" if agent < manual else "manual"}


if __name__ == "__main__":
    r = evaluate()
    print(f"Manual: {r['manual_per_enquiry']} per handled enquiry")
    print(f"Agent:  {r['agent_per_enquiry']} per handled enquiry (total {r['agent_total']} over {r['units']} enquiries)")
    print(f"Lower unit cost on these assumptions: {r['cheaper']}")
    print("Value (coverage gained) is a separate column with its own assumptions. Never blend them.")
