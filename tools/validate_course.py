#!/usr/bin/env python3
"""Validate every JSON example and capstone plan file in this repo.

Checks:
- Any .json file must parse as JSON.
- Readiness audit files (recognised by a "readiness" key) must
  carry data, access, and people sections each with a grade of
  ready, partial, or not_ready (the vocabulary Lesson 05 to 07
  teach).
- Capstone plan files (recognised by a "deployment_plan" key)
  must carry the four sections Lesson 26 fixes in advance:
  readiness, pilot, oversight, and scorecard.
Exits nonzero on any failure, so CI can gate on it.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRADES = {"ready", "partial", "not_ready"}
PLAN_SECTIONS = ["readiness", "pilot", "oversight", "scorecard"]


def iter_json():
    for dirpath, _dirs, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for name in sorted(files):
            if name.endswith(".json"):
                yield os.path.join(dirpath, name)


def check(data):
    errors = []
    if (isinstance(data, dict) and isinstance(data.get("readiness"), dict)
            and {"data", "access", "people"} & set(data["readiness"])):
        for section in ["data", "access", "people"]:
            entry = data["readiness"].get(section)
            if not isinstance(entry, dict) or entry.get("grade") not in GRADES:
                errors.append(f"readiness.{section}: needs a grade in {sorted(GRADES)}")
    if isinstance(data, dict) and "deployment_plan" in data:
        plan = data["deployment_plan"]
        for section in PLAN_SECTIONS:
            if section not in plan:
                errors.append(f"deployment_plan missing section: {section}")
    return errors


def main():
    total, bad = 0, 0
    for path in iter_json():
        total += 1
        rel = os.path.relpath(path, ROOT)
        try:
            with open(path) as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            bad += 1
            print(f"FAIL {rel}: does not parse: {exc}")
            continue
        errors = check(data)
        if errors:
            bad += 1
            for e in errors:
                print(f"FAIL {rel}: {e}")
        else:
            print(f"OK   {rel}")
    print(f"\n{total} JSON files checked, {bad} failing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
