"""Smoke test for Lesson 12: Scoping a pilot that can actually answer the question.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "pilot_scope.py")
    spec = importlib.util.spec_from_file_location("lesson_12_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['complete'] == True, ("complete", result.get("complete"))
    assert result['exclusions'] == 5, ("exclusions", result.get("exclusions"))
    assert result['weeks'] == 4, ("weeks", result.get("weeks"))
    print("smoke ok: Lesson 12 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
