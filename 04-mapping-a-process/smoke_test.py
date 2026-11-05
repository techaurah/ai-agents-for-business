"""Smoke test for Lesson 04: Mapping a process before you automate it.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "process_map.py")
    spec = importlib.util.spec_from_file_location("lesson_04_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['decisions'] == 3, ("decisions", result.get("decisions"))
    assert result['wait_hours'] == 8.0, ("wait_hours", result.get("wait_hours"))
    assert result['steps'] == 8, ("steps", result.get("steps"))
    print("smoke ok: Lesson 04 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
