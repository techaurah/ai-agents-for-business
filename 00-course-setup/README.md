# Lesson 00: Course setup: what you need, and how this course works

**Time:** about 30 minutes · **Difficulty:** Beginner · **Prerequisites:** None · **You need:** Python 3.11 or newer if you want to run the twins, a spreadsheet tool, and a process in your business you care about. No paid accounts, no API keys, no framework installs.

This is a course for the person who signs the cheque and answers for the results, not the person who writes the agent. That changes what setup means. You do not need a cloud account, a model key, or a framework. You need three things: a way to run the small Python calculators and simulators that back every claim in these lessons (or a willingness to read their printed output in the lesson text), a spreadsheet for the costing and scorecard work, and one real process from your own business to carry through the exercises. This lesson verifies the first, explains the second, and helps you pick the third well.

## The honesty rules, stated once

Every business number in this course is one of two things, and it will always say which. Either it is a worked example, computed in front of you from stated assumptions about a fictional business, or it is a fact with a named source and a date, collected in RESEARCH.md. There are no market statistics, no average savings, no typical returns, because those figures, as usually quoted, are vendor claims wearing a lab coat. When a lesson needs a figure for your business, it teaches you to measure your own: your volume, your minutes, your rates. A course that taught you to distrust a vendor's spreadsheet and then handed you its own would have missed its point.

## How to use this repository

Fork the repository; your fork is your workbook and, at the end, holds your capstone deployment plan. Each lesson folder holds a written lesson (README.md), one or more runnable files, one exercise (exercise.md), and a worked solution (solution/SOLUTION.md). Work in order: the BrightSmile Dental example and the vocabulary carry forward, and the capstone in Lessons 26 to 29 assembles everything. Track yourself with PROGRESS.md. Where a lesson ships a smoke_test.py, run it; CI runs every smoke test in the repo, so green locally means green in CI. If you never run a line of code, read the printed outputs quoted in each lesson and do the exercises on paper; the judgement is the course, the code is its evidence.

## The running example: BrightSmile Dental

BrightSmile Dental is a fictional two location dental practice, first used in Course 2, with a front desk team of three and a familiar problem: new patient enquiries arrive through a web form, Instagram messages, and phone calls, and the first reply often takes hours, sometimes until the next working day, and sometimes does not happen at all. Nobody at BrightSmile is lazy; the enquiry channel is simply nobody's named job at 7pm. That shape, valuable work leaking through an ownership gap at the edge of the day, is the shape this course hunts for in Lesson 02, and BrightSmile's lead response process is the running example from here to the capstone.

## Run it

Run `python3 check_environment.py` in this folder. It prints your Python version, confirms it can write the CSV files the costing lessons use, and lists the three honesty rules. Then copy PROGRESS.md into your fork and pick the process you will carry through the exercises: something that happens every week, that a customer or a colleague waits on, and that you can describe step by step today.

## Common failures

- **Picking a process you cannot describe..** If you cannot list its steps on one page, Lesson 04 will stall. Choose the process you know best, not the one that sounds most impressive.
- **Starting with the tool someone is selling you..** A product in search of a process inverts the course. Park the demo, do Lessons 02 to 04, and let the audit choose.
- **Skipping the exercises because the code ran..** The code prints the worked example. The exercise is where your business enters the course; the capstone is built from exercise outputs.

## Recap checklist

- [ ] My Python is 3.11 or newer and the checker says READY, or I am reading outputs on paper by choice.
- [ ] I can state the honesty rule for numbers in this course.
- [ ] I have named the one process I will carry through the exercises.

## Resources

- [Python documentation](https://docs.python.org/3/)
- [Course 1, Agentic AI for Beginners](https://github.com/techaurah/agentic-ai-for-beginners)
- [Course 2, AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n)
- [Course glossary](../resources/glossary.md)
