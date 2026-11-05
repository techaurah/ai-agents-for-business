"""Smoke test for Lesson 14: The agent job description: task, tools, limits, tone.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "job_description.py")
    spec = importlib.util.spec_from_file_location("lesson_14_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['complete'] == True, ("complete", result.get("complete"))
    assert result['nevers'] == 5, ("nevers", result.get("nevers"))
    assert result['exclusions'] == 4, ("exclusions", result.get("exclusions"))
    print("smoke ok: Lesson 14 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
