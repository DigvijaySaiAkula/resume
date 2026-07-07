from reportlab.platypus import Paragraph, Spacer

from styles import body_style

from utils import (
    add_section_title,
    add_divider,
)


def add_summary(story, resume):

    add_section_title(
        story,
        "PROFESSIONAL SUMMARY",
    )

    story.append(
        Paragraph(
            resume["profile"]["summary"],
            body_style,
        )
    )

    story.append(Spacer(1, 4))

    add_divider(story)