"""Smoke test for Lesson 06: Access readiness: accounts, tools, and least privilege.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "access_plan.py")
    spec = importlib.util.spec_from_file_location("lesson_06_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['external'] == 2, ("external", result.get("external"))
    assert result['no_access'] == 2, ("no_access", result.get("no_access"))
    assert result['least_privilege_ok'] == False, ("least_privilege_ok", result.get("least_privilege_ok"))
    print("smoke ok: Lesson 06 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
