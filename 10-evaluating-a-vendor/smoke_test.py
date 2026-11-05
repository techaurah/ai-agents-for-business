"""Smoke test for Lesson 10: Evaluating a vendor or a platform: the demo is not the product.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "vendor_score.py")
    spec = importlib.util.spec_from_file_location("lesson_10_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['winner'] == 'B', ("winner", result.get("winner"))
    assert result['provider_b'] == 56, ("provider_b", result.get("provider_b"))
    assert result['provider_a'] == 30, ("provider_a", result.get("provider_a"))
    print("smoke ok: Lesson 10 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
