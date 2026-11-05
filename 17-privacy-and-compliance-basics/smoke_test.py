"""Smoke test for Lesson 17: Privacy and compliance basics for owners.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "privacy_check.py")
    spec = importlib.util.spec_from_file_location("lesson_17_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['core_complete'] == True, ("core_complete", result.get("core_complete"))
    assert result['done'] == 5, ("done", result.get("done"))
    assert result['items'] == 6, ("items", result.get("items"))
    print("smoke ok: Lesson 17 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
