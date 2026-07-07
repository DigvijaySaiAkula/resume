from reportlab.platypus import Paragraph, Spacer

from styles import (
    technology_style,
)

from utils import (
    add_section_title,
    add_title_row,
    add_bullet,
    add_divider,
)


def add_projects(story, resume):

    add_section_title(
        story,
        "PROJECTS",
    )

    for project in resume["projects"]:

        add_title_row(
            story,
            project["title"],
            project["duration"],
        )

        story.append(
            Paragraph(
                f"<b>Technologies:</b> {project['technology'].replace('|', ' • ')}",
                technology_style,
            )
        )

        story.append(
            Spacer(1, 4)
        )

        for point in project["points"]:

            add_bullet(
                story,
                point,
            )

        add_divider(story)