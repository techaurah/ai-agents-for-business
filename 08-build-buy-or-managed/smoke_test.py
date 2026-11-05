"""Smoke test for Lesson 08: Build versus buy versus managed service: the fair comparison.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "routes.py")
    spec = importlib.util.spec_from_file_location("lesson_08_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['best'] == 'managed', ("best", result.get("best"))
    assert result['criteria'] == 5, ("criteria", result.get("criteria"))
    print("smoke ok: Lesson 08 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
