"""Smoke test for Lesson 11: The honest cost worksheet: build, run, supervise, fix.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "cost_worksheet.py")
    spec = importlib.util.spec_from_file_location("lesson_11_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['total'] == 15752, ("total", result.get("total"))
    assert result['supervise'] == 6200, ("supervise", result.get("supervise"))
    assert result['build'] == 1680, ("build", result.get("build"))
    print("smoke ok: Lesson 11 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
