"""Smoke test for Lesson 27: Build the plan: readiness, pilot, oversight.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "cross_check.py")
    spec = importlib.util.spec_from_file_location("lesson_27_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['all_pass'] == True, ("all_pass", result.get("all_pass"))
    assert result['passed'] == 4, ("passed", result.get("passed"))
    assert result['checks'] == 4, ("checks", result.get("checks"))
    print("smoke ok: Lesson 27 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
