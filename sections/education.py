from reportlab.platypus import Paragraph

from styles import college_style

from styles import body_style

from utils import (
    add_section_title,
    add_title_row,
    add_divider,
)


def add_education(story, resume):

    add_section_title(
        story,
        "EDUCATION",
    )

    for edu in resume["education"]:

        # ↓ These lines must be INSIDE the for loop
        add_title_row(
            story,
            edu["degree"],
            edu["year"],
        )

        story.append(
    Paragraph(
        edu["college"],
        college_style,
    )
)

    # ↓ This is OUTSIDE the loop, so only one divider
    #    is added after the entire Education section.
    add_divider(story)