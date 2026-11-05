"""Smoke test for Lesson 21: Rollout: training the team and the first two weeks.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "rollout_plan.py")
    spec = importlib.util.spec_from_file_location("lesson_21_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['ready'] == True, ("ready", result.get("ready"))
    assert result['sample'] == 20, ("sample", result.get("sample"))
    assert result['missing_flags'] == [], ("missing_flags", result.get("missing_flags"))
    print("smoke ok: Lesson 21 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
