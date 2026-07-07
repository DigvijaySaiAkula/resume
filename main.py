import json
import os

from reportlab.platypus import SimpleDocTemplate

from sections.header import add_header
from sections.summary import add_summary
from sections.experience import add_experience
from sections.projects import add_projects
from sections.education import add_education
from sections.skills import add_skills
from sections.certifications import add_certifications

os.makedirs("output", exist_ok=True)

with open("resume.json", "r", encoding="utf-8") as file:
    resume = json.load(file)

doc = SimpleDocTemplate(
    "output/Resume.pdf",
    leftMargin=40,
    rightMargin=40,
    topMargin=28,
    bottomMargin=28,
)

story = []

add_header(story, resume)
add_summary(story, resume)
add_experience(story, resume)
add_projects(story, resume)
add_education(story, resume)
add_skills(story, resume)
add_certifications(story, resume)
doc.build(story)


print("✅ Resume Created Successfully!")