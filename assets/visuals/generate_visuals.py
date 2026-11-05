#!/usr/bin/env python3
"""Generate the course diagram set as clean, branded SVGs.

Style: white canvas, navy (#0B1F4A) primary boxes with white text,
light blue (#E0F2FE) secondary boxes with navy text, cyan (#0891B2)
arrows, amber (#F59E0B) accent for warnings/gates. Run: python3 generate_visuals.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
NAVY = "#0B1F4A"
LIGHT = "#E0F2FE"
CYAN = "#0891B2"
GREY = "#475569"
FONT = "Segoe UI, Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class SVG:
    def __init__(self, w, h, title, subtitle):
        self.w, self.h = w, h
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
            f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>',
            f'<text x="40" y="52" font-family="{FONT}" font-size="30" font-weight="700" fill="{NAVY}">{esc(title)}</text>',
            f'<text x="40" y="82" font-family="{FONT}" font-size="17" fill="{GREY}">{esc(subtitle)}</text>',
            f'<rect x="40" y="98" width="90" height="5" fill="{CYAN}"/>',
        ]

    def box(self, x, y, w, h, label, sub="", style="navy"):
        fill, tcol, scol = (NAVY, "#FFFFFF", "#BFE3F2") if style == "navy" else (LIGHT, NAVY, "#33506E")
        if style == "amber":
            fill, tcol, scol = "#FEF3C7", NAVY, "#7C5A03"
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}"/>')
        if sub:
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 - 4}" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="700" fill="{tcol}">{esc(label)}</text>')
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 + 20}" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{scol}">{esc(sub)}</text>')
        else:
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 + 7}" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="700" fill="{tcol}">{esc(label)}</text>')

    def arrow(self, x1, y1, x2, y2, label=""):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CYAN}" stroke-width="3" marker-end="url(#ah)"/>')
        if label:
            self.parts.append(f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2 - 8}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="600" fill="{CYAN}">{esc(label)}</text>')

    def note(self, x, y, text):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="15" fill="{GREY}">{esc(text)}</text>')

    def save(self, name):
        defs = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                'markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" '
                f'fill="{CYAN}"/></marker></defs>')
        body = "\n".join(self.parts[:2] + [defs] + self.parts[2:]) + "\n</svg>"
        with open(os.path.join(OUT, name), "w") as f:
            f.write(body)
        print("wrote", name)


def hflow(name, title, subtitle, steps, note=""):
    n = len(steps)
    w = 1200
    bw = (w - 80 - (n - 1) * 50) // n
    s = SVG(w, 300, title, subtitle)
    y = 140
    for i, (label, sub) in enumerate(steps):
        x = 40 + i * (bw + 50)
        s.box(x, y, bw, 90, label, sub, "navy" if i in (0, n - 1) else "light")
        if i < n - 1:
            s.arrow(x + bw + 4, y + 45, x + bw + 46, y + 45)
    if note:
        s.note(40, 275, note)
    s.save(name)


def grid(name, title, subtitle, cells, cols=3, note=""):
    rows = (len(cells) + cols - 1) // cols
    w, h = 1200, 140 + rows * 120 + 40
    s = SVG(w, h, title, subtitle)
    bw = (w - 80 - (cols - 1) * 40) // cols
    for i, (label, sub) in enumerate(cells):
        r, c = divmod(i, cols)
        x, y = 40 + c * (bw + 40), 140 + r * 120
        s.box(x, y, bw, 90, label, sub, "light")
    if note:
        s.note(40, h - 18, note)
    s.save(name)


if __name__ == "__main__":
    grid("course-map.svg", "Course map: 30 lessons, one decision",
         "Every module moves one real agent decision closer to a plan you can defend.",
         [("M0 Start here", "Lessons 00 to 01"), ("M1 Where agents pay", "Lessons 02 to 04"),
          ("M2 Readiness", "Lessons 05 to 07"), ("M3 Build buy managed", "Lessons 08 to 11"),
          ("M4 Design the pilot", "Lessons 12 to 14"), ("M5 Oversight and risk", "Lessons 15 to 18"),
          ("M6 Run the pilot", "Lessons 19 to 21"), ("M7 Measure and improve", "Lessons 22 to 25"),
          ("M8 Capstone plan", "Lessons 26 to 29")],
         note="BrightSmile Dental carries the running example. The capstone repeats the motion on your own process.")
    grid("three-kinds.svg", "Three kinds of software, three purchases",
         "The kind follows from who decides the next step.",
         [("Workflow", "rules decide, fixed steps"), ("Chatbot", "answers, no actions"),
          ("Agent", "model decides steps, inside limits")], cols=3,
         note="Vendors blur these words on purpose. Price and risk follow the kind, not the label.")
    grid("opportunity-matrix.svg", "Where agents fit: volume against judgement",
         "High volume with bounded judgement is the starting quadrant.",
         [("High volume, low judgement", "workflow first, agent maybe"), ("High volume, bounded judgement", "the agent sweet spot"),
          ("Low volume, high judgement", "keep human, assist only"), ("Low volume, low judgement", "a rule or a template")], cols=2,
         note="Lesson 03 is the no list: high stakes, irreversible, or judgement heavy work stays human.")
    grid("readiness-triangle.svg", "Readiness has three sides",
         "An agent starts safely only when all three grade ready or partial with a fix dated.",
         [("Data", "true, current, permitted"), ("Access", "least privilege, revocable"),
          ("People", "owner, operator, escalation human")], cols=3,
         note="A missing side is not a detail. It is the pilot's first failure, scheduled early.")
    hflow("three-routes.svg", "Three routes to the same agent",
          "Build it, buy the platform, or have it managed. Compare total cost and control, not demos.",
          [("Build", "your team, your code"), ("Buy", "platform, your operation"),
           ("Managed service", "provider runs it, you supervise"), ("Your decision", "recorded with reasons")],
          note="Lesson 11 costs all three routes on the same worksheet before anyone decides.")
    hflow("oversight-ladder.svg", "The oversight ladder",
          "Autonomy is granted by risk, one rung at a time, and can be taken back.",
          [("Escalate", "human decides"), ("Ask", "agent requests approval"),
           ("Draft", "human edits and sends"), ("Act", "agent acts, logged")],
          note="Every action in a deployment sits on exactly one rung, written in the escalation policy.")
    hflow("capstone-flow.svg", "Capstone: the deployment plan",
          "Audit, pilot, supervise, score: the plan in the order a real deployment happens.",
          [("Readiness audit", "data, access, people"), ("Pilot design", "scope, baseline, target"),
           ("Oversight plan", "ladder, rota, failures"), ("Scorecard", "verdict with evidence")],
          note="Four sections, four gates. A plan missing a section is not finished, however good it reads.")
