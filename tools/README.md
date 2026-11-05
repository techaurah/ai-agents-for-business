# Repository tools

- `validate_course.py`: checks every JSON file in the repo
  (parses; readiness audits carry graded data, access, and
  people sections; capstone plans carry the four sections
  Lesson 26 fixes). CI runs it on every push.
- `check_links.py`: checks that relative Markdown links resolve
  to files on disk. Run it before a release; external URLs are
  reviewed by humans, not by this script.

Run either from anywhere: `python3 tools/validate_course.py`.
