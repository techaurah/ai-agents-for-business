"""Smoke test for Lesson 01: Agent, chatbot, or workflow: three different purchases.

Imports the lesson artifact, calls its evaluate(), and checks the
values the lesson text quotes. Offline, standard library only.
Run: python3 smoke_test.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    path = os.path.join(HERE, "classify.py")
    spec = importlib.util.spec_from_file_location("lesson_01_artifact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    result = load().evaluate()
    assert result['agents'] == 2, ("agents", result.get("agents"))
    assert result['workflows'] == 2, ("workflows", result.get("workflows"))
    assert result['chatbots'] == 1, ("chatbots", result.get("chatbots"))
    print("smoke ok: Lesson 01 evaluate() matches the lesson text")


if __name__ == "__main__":
    main()
