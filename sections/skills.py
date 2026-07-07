from reportlab.platypus import Paragraph

from styles import body_style
from utils import (
    add_section_title,
    add_divider,
)


def add_skills(story, resume):

    add_section_title(
        story,
        "SKILLS",
    )

    skills = " • ".join(resume["skills"])

    story.append(
        Paragraph(
            skills,
            body_style,
        )
    )

    add_divider(story)