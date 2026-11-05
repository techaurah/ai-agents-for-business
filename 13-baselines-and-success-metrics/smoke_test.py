"""Smoke test for Lesson 13: Baselines and success metrics: measure before you automate.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "baseline.py")
    spec = importlib.util.spec_from_file_location("lesson_13_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['measures'] == 5, ("measures", result.get("measures"))
    assert result['targets'] == 4, ("targets", result.get("targets"))
    assert result['never_answered_baseline'] == 11, ("never_answered_baseline", result.get("never_answered_baseline"))
    print("smoke ok: Lesson 13 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
