"""Smoke test for Lesson 03: Where agents fail: the honest no list.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "no_list.py")
    spec = importlib.util.spec_from_file_location("lesson_03_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['candidates'] == 2, ("candidates", result.get("candidates"))
    assert result['assist'] == 1, ("assist", result.get("assist"))
    assert result['refused'] == 3, ("refused", result.get("refused"))
    print("smoke ok: Lesson 03 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
