"""Smoke test for Lesson 29: Ship it: present, publish, and showcase your plan.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "release_check.py")
    spec = importlib.util.spec_from_file_location("lesson_29_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['ready'] == True, ("ready", result.get("ready"))
    assert result['passed'] == 5, ("passed", result.get("passed"))
    assert result['checks'] == 5, ("checks", result.get("checks"))
    print("smoke ok: Lesson 29 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
