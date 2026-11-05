"""Smoke test for Lesson 07: People readiness: owners, operators, and the team that lives with it.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "roles.py")
    spec = importlib.util.spec_from_file_location("lesson_07_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['people_ready'] == True, ("people_ready", result.get("people_ready"))
    assert result['escalation_routes'] == 3, ("escalation_routes", result.get("escalation_routes"))
    assert result['named_roles'] == 3, ("named_roles", result.get("named_roles"))
    print("smoke ok: Lesson 07 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
