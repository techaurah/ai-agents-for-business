"""Smoke test for Lesson 15: Human oversight and escalation: the ladder.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "escalation_policy.py")
    spec = importlib.util.spec_from_file_location("lesson_15_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['act'] == 2, ("act", result.get("act"))
    assert result['escalate'] == 3, ("escalate", result.get("escalate"))
    assert result['draft'] == 1, ("draft", result.get("draft"))
    assert result['ask'] == 1, ("ask", result.get("ask"))
    print("smoke ok: Lesson 15 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
