"""Smoke test for Lesson 25: Expand, hand over, or stop: the second decision.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "second_decision.py")
    spec = importlib.util.spec_from_file_location("lesson_25_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['light'] == 2, ("light", result.get("light"))
    assert result['records'] == 2, ("records", result.get("records"))
    assert result['proposals'] == 5, ("proposals", result.get("proposals"))
    print("smoke ok: Lesson 25 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
