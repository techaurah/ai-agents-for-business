"""Smoke test for Lesson 02: The opportunity audit: finding the work an agent can carry.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "audit.py")
    spec = importlib.util.spec_from_file_location("lesson_02_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['top'] == 'Enquiry first response and follow up', ("top", result.get("top"))
    assert result['bottom'] == 'Treatment plan explanations', ("bottom", result.get("bottom"))
    assert result['processes'] == 5, ("processes", result.get("processes"))
    print("smoke ok: Lesson 02 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
