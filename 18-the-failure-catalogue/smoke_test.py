"""Smoke test for Lesson 18: The failure catalogue: how agents go wrong in businesses.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "failure_catalogue.py")
    spec = importlib.util.spec_from_file_location("lesson_18_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['entries'] == 8, ("entries", result.get("entries"))
    assert result['incomplete'] == [], ("incomplete", result.get("incomplete"))
    assert result['operator_owned'] == 4, ("operator_owned", result.get("operator_owned"))
    print("smoke ok: Lesson 18 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
