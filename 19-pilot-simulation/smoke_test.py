"""Smoke test for Lesson 19: Pilot simulation: the lead response twin.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "lead_response_twin.py")
    spec = importlib.util.spec_from_file_location("lesson_19_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['base_clears'] == True, ("base_clears", result.get("base_clears"))
    assert result['base_escalations'] == 27, ("base_escalations", result.get("base_escalations"))
    assert result['capacity_per_day'] == 10, ("capacity_per_day", result.get("capacity_per_day"))
    print("smoke ok: Lesson 19 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
