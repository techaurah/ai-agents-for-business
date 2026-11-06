"""Smoke test for Lesson 23: Unit economics: what one handled enquiry really costs.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "unit_economics.py")
    spec = importlib.util.spec_from_file_location("lesson_23_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['manual_per_enquiry'] == 4.1, ("manual_per_enquiry", result.get("manual_per_enquiry"))
    assert result['agent_per_enquiry'] == 3.51, ("agent_per_enquiry", result.get("agent_per_enquiry"))
    assert result['cheaper'] == 'agent', ("cheaper", result.get("cheaper"))
    print("smoke ok: Lesson 23 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
