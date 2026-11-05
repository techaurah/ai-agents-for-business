"""Smoke test for Lesson 05: Data readiness: what the agent may read, and whether it is true.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "data_audit.py")
    spec = importlib.util.spec_from_file_location("lesson_05_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['ready'] == 2, ("ready", result.get("ready"))
    assert result['partial'] == 1, ("partial", result.get("partial"))
    assert result['not_ready'] == 2, ("not_ready", result.get("not_ready"))
    print("smoke ok: Lesson 05 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
