from utils import (
    add_section_title,
    add_title_row,
    add_bullet,
    add_divider,
)


def add_certifications(story, resume):

    add_section_title(
        story,
        "CERTIFICATIONS",
    )

    for cert in resume["certifications"]:

        add_title_row(
            story,
            cert["name"],
            cert["year"],
        )

        add_bullet(
            story,
            cert["issuer"],
        )

    add_divider(story)