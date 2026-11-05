"""Smoke test for Lesson 20: Testing before trust: the acceptance set.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "acceptance_set.py")
    spec = importlib.util.spec_from_file_location("lesson_20_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['complete'] == True, ("complete", result.get("complete"))
    assert result['cases'] == 16, ("cases", result.get("cases"))
    assert result['escalations_expected'] == 3, ("escalations_expected", result.get("escalations_expected"))
    print("smoke ok: Lesson 20 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
