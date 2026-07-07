from reportlab.platypus import Paragraph, Spacer

from styles import (
    name_style,
    title_style,
    contact_style,
)

from utils import add_divider


def add_header(story, resume):

    profile = resume["profile"]
    contact = profile["contact"]

    story.append(
        Paragraph(
            f"<b>{profile['name']}</b>",
            name_style,
        )
    )

    story.append(Spacer(1, 2))

    story.append(
    Paragraph(
        profile["title"],
        title_style,
    )
)

    story.append(Spacer(1, 2))

    contact_text = f"""
    <font color="#0A66C2">
    <link href="mailto:{contact['email']}">
    {contact['email']}
    </link>
    </font>

    |

    <font color="#0A66C2">
    <link href="tel:{contact['phone']}">
    {contact['phone']}
    </link>
    </font>

    |

    <font color="#0A66C2">
    <link href="{contact['location_url']}">
    {contact['location']}
    </link>
    </font>

    """#remove this line to add github and linkedin link
    
    #|

    #<font color="#0A66C2">
    #<link href="{contact['linkedin']}">
    #LinkedIn
    #</link>
    #</font>

    
    #|
    #<font color="#0A66C2">
    #<link href="{contact['github']}">
    #GitHub
    #</link>
    #</font> 
    #"""

    story.append(
        Paragraph(
            contact_text,
            contact_style,
        )
    )

    add_divider(story)