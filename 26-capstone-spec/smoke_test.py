"""Smoke test for Lesson 26: Capstone spec: the deployment plan, fixed in advance.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "plan_check.py")
    spec = importlib.util.spec_from_file_location("lesson_26_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['sections'] == 4, ("sections", result.get("sections"))
    assert result['complete'] == True, ("complete", result.get("complete"))
    assert result['required_keys'] == 17, ("required_keys", result.get("required_keys"))
    print("smoke ok: Lesson 26 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
