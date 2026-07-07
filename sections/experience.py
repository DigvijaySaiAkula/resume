from utils import (
    add_section_title,
    add_entry,
)


def add_experience(story, resume):

    add_section_title(
        story,
        "EXPERIENCE",
    )

    for job in resume["experience"]:

        add_entry(
            story=story,
            title=job["company"],
            subtitle=job["designation"],
            duration=job["duration"],
            bullets=job["points"],
        )