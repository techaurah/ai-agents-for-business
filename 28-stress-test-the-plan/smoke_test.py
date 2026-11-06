"""Smoke test for Lesson 28: Stress test the plan: red team your own deployment.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "stress_test.py")
    spec = importlib.util.spec_from_file_location("lesson_28_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['handled'] == 5, ("handled", result.get("handled"))
    assert result['gaps'] == 2, ("gaps", result.get("gaps"))
    assert result['unhandled'] == 0, ("unhandled", result.get("unhandled"))
    assert result['stressors'] == 4, ("stressors", result.get("stressors"))
    print("smoke ok: Lesson 28 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
