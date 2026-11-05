"""Lesson 00: verify the environment this course needs.

Checks the Python version, that a spreadsheet friendly CSV can be
written, and prints the course honesty rules. No network, no
credentials. Run: python3 check_environment.py
"""
import csv
import io
import sys

RULES = [
    "Every business number is a worked example with assumptions, or a sourced fact with a date.",
    "No framework is required to pass any lesson; the twins run on the standard library.",
    "No certificate exists. The capstone deployment plan in the showcase is the artifact.",
]


def evaluate():
    major, minor = sys.version_info[:2]
    buf = io.StringIO()
    csv.writer(buf).writerow(["process", "volume_per_week"])
    return {"python": f"{major}.{minor}", "python_ok": (major, minor) >= (3, 11),
            "csv_ok": "volume_per_week" in buf.getvalue(), "rules": len(RULES)}


def main():
    r = evaluate()
    print(f"Python {r['python']}: {'OK' if r['python_ok'] else 'FAIL, this course needs 3.11 or newer'}")
    print(f"CSV writing: {'OK' if r['csv_ok'] else 'FAIL'}")
    print("Honesty rules:")
    for rule in RULES:
        print(" -", rule)
    print("READY" if r["python_ok"] and r["csv_ok"] else "NOT READY")
    return 0 if r["python_ok"] and r["csv_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
