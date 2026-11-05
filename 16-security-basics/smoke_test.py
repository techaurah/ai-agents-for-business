"""Smoke test for Lesson 16: Security basics: what an agent must never be able to do.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "threat_check.py")
    spec = importlib.util.spec_from_file_location("lesson_16_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['threats'] == 5, ("threats", result.get("threats"))
    assert result['architecture'] == 3, ("architecture", result.get("architecture"))
    assert result['passes'] == False, ("passes", result.get("passes"))
    print("smoke ok: Lesson 16 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
