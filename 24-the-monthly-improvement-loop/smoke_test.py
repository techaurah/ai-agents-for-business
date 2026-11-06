"""Smoke test for Lesson 24: The monthly improvement loop.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "monthly_review.py")
    spec = importlib.util.spec_from_file_location("lesson_24_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['complete'] == True, ("complete", result.get("complete"))
    assert result['items_present'] == 5, ("items_present", result.get("items_present"))
    assert result['one_improvement'] == True, ("one_improvement", result.get("one_improvement"))
    print("smoke ok: Lesson 24 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
